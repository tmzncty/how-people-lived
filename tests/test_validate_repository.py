from __future__ import annotations

import copy
import json
import os
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import (
    validate_dataset_manifest,
    validate_markdown_links,
    validate_repository,
)


class RepositoryValidatorTests(unittest.TestCase):
    def make_fixture(
        self,
        root: Path,
        *,
        source: str = "https://example.test/source",
        record_count: int = 1,
    ) -> None:
        data_dir = root / "data"
        data_dir.mkdir(parents=True)
        (data_dir / "sample.csv").write_text(
            f"year,value,source\n2000,1,{source}\n", encoding="utf-8"
        )
        manifest = {
            "$schema": "../schemas/dataset-manifest.schema.json",
            "schema_version": 1,
            "datasets": [
                {
                    "id": "sample",
                    "path": "sample.csv",
                    "classification": "measured",
                    "geographic_scope": ["Example"],
                    "temporal_coverage": "2000",
                    "record_count": record_count,
                    "source_columns": ["source"],
                    "description": "Fixture dataset.",
                }
            ],
        }
        (data_dir / "dataset-manifest.json").write_text(
            json.dumps(manifest), encoding="utf-8"
        )
        schema_dir = root / "schemas"
        schema_dir.mkdir()
        manifest_fields = list(manifest)
        dataset_fields = list(manifest["datasets"][0])
        manifest_properties = {field: {} for field in manifest_fields}
        manifest_properties["datasets"] = {
            "type": "array",
            "items": {"$ref": "#/$defs/dataset"}
        }
        (schema_dir / "dataset-manifest.schema.json").write_text(
            json.dumps(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
                    "additionalProperties": False,
                    "required": manifest_fields,
                    "properties": manifest_properties,
                    "$defs": {
                        "dataset": {
                            "type": "object",
                            "additionalProperties": False,
                            "required": dataset_fields,
                            "properties": {field: {} for field in dataset_fields},
                        }
                    },
                }
            ),
            encoding="utf-8",
        )
        (root / "README.md").write_text(
            "# Fixture\n\n[Data](data/sample.csv)\n", encoding="utf-8"
        )

    def test_valid_fixture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            self.assertEqual(validate_repository(root), [])

    def test_unindexed_csv_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "data/unindexed.csv").write_text("value\n1\n", encoding="utf-8")
            errors = validate_repository(root)
            self.assertTrue(any("not listed" in error for error in errors), errors)

    def test_manifest_root_with_unknown_field_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["unexpected"] = True
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            errors = validate_repository(root)

            self.assertTrue(
                any("unexpected fields: unexpected" in error for error in errors),
                errors,
            )

    def test_measured_row_without_source_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root, source="")
            errors = validate_repository(root)
            self.assertTrue(any("lack a source" in error for error in errors), errors)

    def test_record_count_drift_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root, record_count=2)
            errors = validate_repository(root)
            self.assertTrue(any("CSV contains 1 rows" in error for error in errors), errors)

    def test_schema_version_requires_integer_one(self) -> None:
        for invalid_version in (True, 1.0):
            with self.subTest(schema_version=invalid_version):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["schema_version"] = invalid_version
                    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any("schema_version must be the integer 1" in error for error in errors),
                        errors,
                    )

    def test_non_string_classification_is_rejected_without_crashing(self) -> None:
        for invalid_classification in ([], {}):
            with self.subTest(classification=invalid_classification):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["datasets"][0]["classification"] = invalid_classification
                    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any("invalid classification" in error for error in errors),
                        errors,
                    )

    def test_duplicate_manifest_keys_are_rejected(self) -> None:
        replacements = (
            (
                '"schema_version": 1',
                '"schema_version": 999, "schema_version": 1',
                "schema_version",
            ),
            (
                '"classification": "measured"',
                '"classification": [], "classification": "measured"',
                "classification",
            ),
        )
        for original, replacement, duplicated_key in replacements:
            with self.subTest(duplicated_key=duplicated_key):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest_text = manifest_path.read_text(encoding="utf-8")
                    manifest_path.write_text(
                        manifest_text.replace(original, replacement, 1),
                        encoding="utf-8",
                    )

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(
                            f"duplicate key '{duplicated_key}'" in error
                            for error in errors
                        ),
                        errors,
                    )

    def test_nonstandard_json_constants_are_rejected(self) -> None:
        for constant in ("NaN", "Infinity", "-Infinity"):
            with self.subTest(constant=constant):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest_text = manifest_path.read_text(encoding="utf-8")
                    manifest_path.write_text(
                        manifest_text.replace(
                            '"schema_version": 1',
                            f'"schema_version": {constant}',
                            1,
                        ),
                        encoding="utf-8",
                    )

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(
                            f"non-standard constant '{constant}'" in error
                            for error in errors
                        ),
                        errors,
                    )

    def test_non_utf8_manifest_is_rejected_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "data/dataset-manifest.json").write_bytes(b"\xff")

            errors = validate_repository(root)

            self.assertTrue(any("is not valid UTF-8" in error for error in errors), errors)

    def test_missing_manifest_schema_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "schemas/dataset-manifest.schema.json").unlink()

            errors = validate_repository(root)

            self.assertTrue(
                any("missing or not a regular file" in error for error in errors),
                errors,
            )

    def test_invalid_manifest_schema_is_rejected(self) -> None:
        cases = (
            ("{", "invalid JSON"),
            ("[]", "root must be an object"),
            ('{"type":"object","type":"array"}', "duplicate key 'type'"),
            ('{"minimum":NaN}', "non-standard constant 'NaN'"),
        )
        for schema_text, expected_error in cases:
            with self.subTest(schema_text=schema_text):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    (root / "schemas/dataset-manifest.schema.json").write_text(
                        schema_text,
                        encoding="utf-8",
                    )

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(expected_error in error for error in errors),
                        errors,
                    )

    def test_manifest_schema_contract_drift_is_rejected(self) -> None:
        cases = (
            "empty",
            "wrong-draft",
            "open-root",
            "root-required",
            "datasets-type",
            "items-ref",
            "open-dataset",
            "dataset-properties",
        )
        for case in cases:
            with self.subTest(case=case):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    schema_path = root / "schemas/dataset-manifest.schema.json"
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    if case == "empty":
                        schema = {}
                    elif case == "wrong-draft":
                        schema["$schema"] = "https://json-schema.org/draft/2019-09/schema"
                    elif case == "open-root":
                        schema["additionalProperties"] = True
                    elif case == "root-required":
                        schema["required"].remove("schema_version")
                    elif case == "datasets-type":
                        schema["properties"]["datasets"]["type"] = "object"
                    elif case == "items-ref":
                        schema["properties"]["datasets"]["items"]["$ref"] = "#/$defs/other"
                    elif case == "open-dataset":
                        schema["$defs"]["dataset"]["additionalProperties"] = True
                    else:
                        del schema["$defs"]["dataset"]["properties"]["description"]
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any("schema contract drift" in error for error in errors),
                        errors,
                    )

    def test_unindexed_nested_and_mixed_case_csvs_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            nested = root / "data/nested"
            nested.mkdir()
            (nested / "unindexed.csv").write_text("value\n1\n", encoding="utf-8")
            (root / "data/UNINDEXED.CSV").write_text("value\n1\n", encoding="utf-8")

            errors = validate_repository(root)

            self.assertTrue(any("data/nested/unindexed.csv" in error for error in errors), errors)
            self.assertTrue(any("data/UNINDEXED.CSV" in error for error in errors), errors)

    def test_windows_drive_relative_manifest_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["datasets"][0]["path"] = "C:sample.csv"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            errors = validate_repository(root)

            self.assertTrue(
                any("path must name one portable CSV" in error for error in errors),
                errors,
            )

    def test_blank_scaffold_record_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["datasets"][0]["classification"] = "research_scaffold"
            manifest["datasets"][0]["source_columns"] = []
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            (root / "data/sample.csv").write_text(
                "year,value,source\n,,\n", encoding="utf-8"
            )

            errors = validate_repository(root)

            self.assertTrue(any("blank data rows" in error for error in errors), errors)

    def test_malformed_csv_quoting_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "data/sample.csv").write_text(
                'year,value,source\n2000,1,"unterminated\n', encoding="utf-8"
            )

            errors = validate_repository(root)

            self.assertTrue(any("cannot parse 'sample.csv'" in error for error in errors), errors)

    def test_data_directory_symlink_cannot_escape_repository(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "repository"
            root.mkdir()
            self.make_fixture(root)
            outside_data = parent / "outside-data"
            (root / "data").rename(outside_data)
            try:
                (root / "data").symlink_to(outside_data, target_is_directory=True)
            except OSError as exc:
                self.skipTest(f"directory symlinks unavailable: {exc}")

            errors, _ = validate_dataset_manifest(root)

            self.assertTrue(any("data directory escapes repository" in error for error in errors), errors)

    def test_manifest_symlink_cannot_escape_data_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            parent = Path(directory)
            root = parent / "repository"
            root.mkdir()
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            outside_manifest = parent / "outside-manifest.json"
            manifest_path.rename(outside_manifest)
            try:
                manifest_path.symlink_to(outside_manifest)
            except OSError as exc:
                self.skipTest(f"file symlinks unavailable: {exc}")

            errors, _ = validate_dataset_manifest(root)

            self.assertTrue(any("path escapes data/" in error for error in errors), errors)

    def test_manifest_must_be_a_regular_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            manifest_path.unlink()
            manifest_path.mkdir()

            errors, _ = validate_dataset_manifest(root)

            self.assertTrue(
                any("missing or not a regular file" in error for error in errors),
                errors,
            )

    def test_two_manifest_paths_cannot_resolve_to_the_same_csv(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            alias_path = root / "data/alias.csv"
            try:
                alias_path.symlink_to(root / "data/sample.csv")
            except OSError as exc:
                self.skipTest(f"file symlinks unavailable: {exc}")
            manifest_path = root / "data/dataset-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            alias_entry = copy.deepcopy(manifest["datasets"][0])
            alias_entry["id"] = "alias"
            alias_entry["path"] = "alias.csv"
            manifest["datasets"].append(alias_entry)
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

            errors, _ = validate_dataset_manifest(root)

            self.assertTrue(any("resolves to the same CSV" in error for error in errors), errors)

    def test_broken_local_markdown_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "README.md").write_text(
                "# Fixture\n\n[Missing](does-not-exist.md)\n", encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(any("missing local link target" in error for error in errors), errors)

    def test_balanced_and_angle_inline_destinations_are_supported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "nested(name).md").write_text("# Nested\n", encoding="utf-8")
            nested_dir = root / "dir"
            nested_dir.mkdir()
            (nested_dir / "a (b).md").write_text("# Angled\n", encoding="utf-8")
            (root / "escaped(name).md").write_text("# Escaped\n", encoding="utf-8")
            (root / "README.md").write_text(
                "[Nested](nested(name).md)\n"
                "[Angled](<dir/a (b).md>)\n"
                "[Escaped](escaped\\(name\\).md)\n",
                encoding="utf-8",
            )

            errors, checked = validate_markdown_links(root)

            self.assertEqual(errors, [])
            self.assertEqual(checked, 3)

    def test_all_uri_schemes_and_network_paths_are_external(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "README.md").write_text(
                "[FTP](ftp://host/a) [Custom](custom:opaque) "
                "[Network](//host/a)\n",
                encoding="utf-8",
            )

            errors, checked = validate_markdown_links(root)

            self.assertEqual(errors, [])
            self.assertEqual(checked, 0)

    def test_windows_absolute_markdown_destinations_are_rejected(self) -> None:
        for target in ("C:/missing.md", r"C:\missing.md"):
            with self.subTest(target=target):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    (root / "README.md").write_text(
                        f"[Missing]({target})\n",
                        encoding="utf-8",
                    )

                    errors, checked = validate_markdown_links(root)

                    self.assertEqual(checked, 1)
                    self.assertTrue(
                        any("local link escapes repository" in error for error in errors),
                        errors,
                    )

    def test_reference_style_links_are_rejected_with_guidance(self) -> None:
        cases = (
            "[Missing][target]\n[target]: missing.md\n",
            "[Missing][]\n",
        )
        for markdown in cases:
            with self.subTest(markdown=markdown):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    (root / "README.md").write_text(markdown, encoding="utf-8")

                    errors, checked = validate_markdown_links(root)

                    self.assertTrue(
                        any(
                            "unsupported reference-style link; use inline form"
                            in error
                            for error in errors
                        ),
                        errors,
                    )
                    self.assertEqual(checked, 0)

    def test_markdown_source_must_be_a_regular_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            readme = root / "README.md"
            readme.unlink()
            readme.mkdir()

            errors, _ = validate_markdown_links(root)

            self.assertTrue(
                any("not a regular file" in error for error in errors),
                errors,
            )

    def test_non_utf8_markdown_source_is_rejected_without_crashing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "README.md").write_bytes(b"\xff")

            errors, _ = validate_markdown_links(root)

            self.assertTrue(any("cannot decode as UTF-8" in error for error in errors), errors)

    def test_markdown_symlinks_cannot_escape_or_dangle(self) -> None:
        cases = ("external", "dangling")
        for case in cases:
            with self.subTest(case=case):
                with tempfile.TemporaryDirectory() as directory:
                    parent = Path(directory)
                    root = parent / "repository"
                    root.mkdir()
                    self.make_fixture(root)
                    link_path = root / f"{case}.md"
                    if case == "external":
                        target = parent / "outside.md"
                        target.write_text("# Outside\n", encoding="utf-8")
                    else:
                        target = root / "missing.md"
                    try:
                        link_path.symlink_to(target)
                    except OSError as exc:
                        self.skipTest(f"file symlinks unavailable: {exc}")

                    errors, _ = validate_markdown_links(root)

                    expected = (
                        "escapes repository" if case == "external" else "cannot resolve"
                    )
                    self.assertTrue(any(expected in error for error in errors), errors)

    def test_unresolvable_markdown_link_target_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            loop = root / "loop"
            try:
                loop.symlink_to(loop)
            except OSError as exc:
                self.skipTest(f"file symlinks unavailable: {exc}")
            (root / "README.md").write_text("[Loop](loop)\n", encoding="utf-8")

            errors, checked = validate_markdown_links(root)

            self.assertEqual(checked, 1)
            self.assertTrue(
                any("cannot resolve local link target: loop" in error for error in errors),
                errors,
            )

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFOs unavailable")
    def test_markdown_fifo_is_rejected_without_being_opened(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            os.mkfifo(root / "pipe.md")

            errors, _ = validate_markdown_links(root)

            self.assertTrue(any("not a regular file" in error for error in errors), errors)


class ManifestCoverageRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        root = Path(__file__).resolve().parents[1]
        manifest = json.loads(
            (root / "data/dataset-manifest.json").read_text(encoding="utf-8")
        )
        cls.datasets = {dataset["id"]: dataset for dataset in manifest["datasets"]}

    def test_educational_mobility_includes_comparison_cohort(self) -> None:
        dataset = self.datasets["china-educational-mobility-1986-1995-selected"]

        self.assertEqual(
            dataset["temporal_coverage"],
            "offspring birth cohorts 1976-1985 (comparison rows) and 1986-1995",
        )
        self.assertIn(
            "the 1976-1985 rows provide comparisons for 1986-1995",
            dataset["description"],
        )

    def test_old_age_support_names_the_charls_2018_wave(self) -> None:
        dataset = self.datasets["china-old-age-support-expectations-charls"]

        self.assertEqual(
            dataset["temporal_coverage"],
            "CHARLS 2018 retirement-expectation survey analysis",
        )

    def test_2018_time_use_names_both_average_types(self) -> None:
        dataset = self.datasets["china-time-use-2018-selected"]

        self.assertEqual(
            dataset["description"],
            "Selected resident- and participant-average activity times with "
            "accompanying Internet-use measures.",
        )


if __name__ == "__main__":
    unittest.main()
