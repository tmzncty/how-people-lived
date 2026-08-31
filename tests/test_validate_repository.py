from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import validate_dataset_manifest, validate_repository


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
        (schema_dir / "dataset-manifest.schema.json").write_text(
            json.dumps(
                {
                    "$schema": "https://json-schema.org/draft/2020-12/schema",
                    "type": "object",
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


if __name__ == "__main__":
    unittest.main()
