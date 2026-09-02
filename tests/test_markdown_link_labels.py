from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import (
    _inline_markdown_targets,
    validate_markdown_links,
)


class MarkdownLinkLabelTests(unittest.TestCase):
    def test_nested_and_escaped_labels_resolve_existing_targets(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for target in ("nested.md", "deep.md", "escaped.md", "image.md"):
                (root / target).write_text(f"# {target}\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Outer [context]](nested.md)\n"
                "[Outer [middle [context]]](deep.md)\n"
                "[Closing \\] bracket](escaped.md)\n"
                "![Diagram [detail]](image.md)\n",
                encoding="utf-8",
            )

            errors, checked = validate_markdown_links(root)

            self.assertEqual(errors, [])
            self.assertEqual(checked, 4)

    def test_nested_and_escaped_labels_cannot_hide_missing_targets(self) -> None:
        cases = (
            ("[Outer [context]](does-not-exist.md)", 1),
            ("[Closing \\] bracket](does-not-exist.md)", 1),
            ("[Outer [inner](does-not-exist.md)](outer.md)", 1),
            ("[![Diagram](does-not-exist.md)](outer.md)", 2),
        )
        for markdown, expected_checked in cases:
            with self.subTest(markdown=markdown):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    (root / "outer.md").write_text("# Outer\n", encoding="utf-8")
                    (root / "README.md").write_text(markdown, encoding="utf-8")

                    errors, checked = validate_markdown_links(root)

                    self.assertEqual(checked, expected_checked)
                    self.assertTrue(
                        any("missing local link target" in error for error in errors),
                        errors,
                    )

    def test_nested_constructs_follow_github_link_precedence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for target in ("inner.md", "diagram.png", "page.md", "outer.png"):
                (root / target).write_text("fixture\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Outer [inner](inner.md)](literal.md)\n"
                "[![Diagram](diagram.png)](page.md)\n"
                "![Outer [inner](ignored.md)](outer.png)\n",
                encoding="utf-8",
            )

            errors, checked = validate_markdown_links(root)

            self.assertEqual(errors, [])
            self.assertEqual(checked, 4)

    def test_parser_returns_each_destination_after_complex_labels(self) -> None:
        line = (
            "[Outer [context]](first.md) "
            "[Closing \\] bracket](second.md) "
            "[Linked [inner](third.md)](fourth.md) "
            "[![Diagram](fifth.png)](sixth.md)"
        )

        self.assertEqual(
            list(_inline_markdown_targets(line)),
            [
                "first.md",
                "second.md",
                "third.md",
                "fifth.png",
                "sixth.md",
            ],
        )

    def test_deeply_nested_labels_do_not_depend_on_python_recursion(self) -> None:
        line = "[" * 1_500 + "label" + "]" * 1_500 + "(target.md)"

        self.assertEqual(list(_inline_markdown_targets(line)), ["target.md"])


if __name__ == "__main__":
    unittest.main()
