from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_repository


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

    def test_broken_local_markdown_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "README.md").write_text(
                "# Fixture\n\n[Missing](does-not-exist.md)\n", encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(any("missing local link target" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
