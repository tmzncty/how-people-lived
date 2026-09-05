from __future__ import annotations

import copy
import json
import os
import re
import tempfile
import unittest
from pathlib import Path

from scripts.validate_repository import (
    _canonical_json,
    _schema_annotation_error,
    _schema_behavior_projection,
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
        canonical_schema = (
            Path(__file__).resolve().parents[1] / "schemas/dataset-manifest.schema.json"
        )
        (schema_dir / "dataset-manifest.schema.json").write_text(
            canonical_schema.read_text(encoding="utf-8"),
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

    def test_manifest_schema_and_python_reject_the_same_whitespace_values(self) -> None:
        schema = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "schemas/dataset-manifest.schema.json"
            ).read_text(encoding="utf-8")
        )
        properties = schema["$defs"]["dataset"]["properties"]
        schema_cases = (
            ("geographic_scope item", properties["geographic_scope"]["items"]),
            ("temporal_coverage", properties["temporal_coverage"]),
            ("source_columns item", properties["source_columns"]["items"]),
            ("description", properties["description"]),
        )
        python_whitespace_code_points = (
            *range(0x0009, 0x000E),
            *range(0x001C, 0x0021),
            0x0085,
            0x00A0,
            0x1680,
            *range(0x2000, 0x200B),
            0x2028,
            0x2029,
            0x202F,
            0x205F,
            0x3000,
        )
        whitespace_values = (
            "",
            *(chr(code_point) for code_point in python_whitespace_code_points),
            "".join(chr(code_point) for code_point in python_whitespace_code_points),
        )
        for field, field_schema in schema_cases:
            with self.subTest(contract="schema", field=field):
                pattern = field_schema["pattern"]
                for whitespace in whitespace_values:
                    self.assertIsNone(re.search(pattern, whitespace))
                for non_whitespace in ("value", "\u200b", "\ufeff"):
                    self.assertIsNotNone(re.search(pattern, non_whitespace))

        manifest_cases = (
            (
                "geographic_scope",
                [" \t\r\n"],
                "geographic_scope must contain unique non-empty strings",
            ),
            (
                "temporal_coverage",
                " \t\r\n",
                "temporal_coverage must be a non-empty string",
            ),
            (
                "source_columns",
                [" \t\r\n"],
                "source_columns must contain unique non-empty strings",
            ),
            (
                "description",
                " \t\r\n",
                "description must be a non-empty string",
            ),
        )
        for field, whitespace_value, expected_error in manifest_cases:
            with self.subTest(contract="python", field=field):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["datasets"][0][field] = whitespace_value
                    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(expected_error in error for error in errors),
                        errors,
                    )

        for whitespace in ("\u001c", "\u001d", "\u001e", "\u001f", "\u0085"):
            with self.subTest(
                contract="python-ecma-difference",
                value=ord(whitespace),
            ):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    manifest_path = root / "data/dataset-manifest.json"
                    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
                    manifest["datasets"][0]["description"] = whitespace
                    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(
                            "description must be a non-empty string" in error
                            for error in errors
                        ),
                        errors,
                    )

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            manifest_path = root / "data/dataset-manifest.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["datasets"][0]["description"] = "\ufeff"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

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
            self.assertTrue(
                any("CSV contains 1 rows" in error for error in errors), errors
            )

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
                        any(
                            "schema_version must be the integer 1" in error
                            for error in errors
                        ),
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

            self.assertTrue(
                any("is not valid UTF-8" in error for error in errors), errors
            )

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
                        schema["$schema"] = (
                            "https://json-schema.org/draft/2019-09/schema"
                        )
                    elif case == "open-root":
                        schema["additionalProperties"] = True
                    elif case == "root-required":
                        schema["required"].remove("schema_version")
                    elif case == "datasets-type":
                        schema["properties"]["datasets"]["type"] = "object"
                    elif case == "items-ref":
                        schema["properties"]["datasets"]["items"][
                            "$ref"
                        ] = "#/$defs/other"
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

    def test_manifest_schema_behavior_mutants_are_rejected(self) -> None:
        delete = object()
        cases = (
            ("root-id-non-string", ("$id",), 7),
            (
                "nested-id-rebases-ref",
                ("properties", "datasets", "$id"),
                "https://example.test/nested-datasets",
            ),
            ("manifest-schema-const", ("properties", "$schema", "const"), "other"),
            ("schema-version-type", ("properties", "schema_version", "type"), "number"),
            ("schema-version-const", ("properties", "schema_version", "const"), 2),
            (
                "schema-version-const-boolean",
                ("properties", "schema_version", "const"),
                True,
            ),
            ("id-type", ("$defs", "dataset", "properties", "id", "type"), "number"),
            (
                "id-pattern-removed",
                ("$defs", "dataset", "properties", "id", "pattern"),
                delete,
            ),
            (
                "id-pattern-weakened",
                ("$defs", "dataset", "properties", "id", "pattern"),
                ".*",
            ),
            (
                "path-pattern-removed",
                ("$defs", "dataset", "properties", "path", "pattern"),
                delete,
            ),
            (
                "path-pattern-weakened",
                ("$defs", "dataset", "properties", "path", "pattern"),
                ".*",
            ),
            (
                "classification-enum-removed",
                ("$defs", "dataset", "properties", "classification", "enum"),
                delete,
            ),
            (
                "classification-enum-weakened",
                ("$defs", "dataset", "properties", "classification", "enum"),
                ["measured", "research_scaffold", "other"],
            ),
            (
                "geographic-min-items-removed",
                ("$defs", "dataset", "properties", "geographic_scope", "minItems"),
                delete,
            ),
            (
                "geographic-min-items-weakened",
                ("$defs", "dataset", "properties", "geographic_scope", "minItems"),
                0,
            ),
            (
                "geographic-min-items-boolean",
                ("$defs", "dataset", "properties", "geographic_scope", "minItems"),
                True,
            ),
            (
                "geographic-unique-items-removed",
                ("$defs", "dataset", "properties", "geographic_scope", "uniqueItems"),
                delete,
            ),
            (
                "geographic-unique-items-weakened",
                ("$defs", "dataset", "properties", "geographic_scope", "uniqueItems"),
                False,
            ),
            (
                "geographic-items-removed",
                ("$defs", "dataset", "properties", "geographic_scope", "items"),
                delete,
            ),
            (
                "geographic-item-type",
                ("$defs", "dataset", "properties", "geographic_scope", "items", "type"),
                "number",
            ),
            (
                "geographic-item-pattern",
                (
                    "$defs",
                    "dataset",
                    "properties",
                    "geographic_scope",
                    "items",
                    "pattern",
                ),
                ".*",
            ),
            (
                "temporal-pattern-removed",
                ("$defs", "dataset", "properties", "temporal_coverage", "pattern"),
                delete,
            ),
            (
                "temporal-pattern-weakened",
                ("$defs", "dataset", "properties", "temporal_coverage", "pattern"),
                ".*",
            ),
            (
                "record-count-type",
                ("$defs", "dataset", "properties", "record_count", "type"),
                "number",
            ),
            (
                "record-count-minimum-removed",
                ("$defs", "dataset", "properties", "record_count", "minimum"),
                delete,
            ),
            (
                "record-count-minimum-weakened",
                ("$defs", "dataset", "properties", "record_count", "minimum"),
                0,
            ),
            (
                "record-count-minimum-boolean",
                ("$defs", "dataset", "properties", "record_count", "minimum"),
                True,
            ),
            (
                "source-unique-items",
                ("$defs", "dataset", "properties", "source_columns", "uniqueItems"),
                False,
            ),
            (
                "source-items-removed",
                ("$defs", "dataset", "properties", "source_columns", "items"),
                delete,
            ),
            (
                "source-item-type",
                ("$defs", "dataset", "properties", "source_columns", "items", "type"),
                "number",
            ),
            (
                "source-item-pattern-removed",
                (
                    "$defs",
                    "dataset",
                    "properties",
                    "source_columns",
                    "items",
                    "pattern",
                ),
                delete,
            ),
            (
                "source-item-pattern-weakened",
                (
                    "$defs",
                    "dataset",
                    "properties",
                    "source_columns",
                    "items",
                    "pattern",
                ),
                ".*",
            ),
            (
                "description-pattern-removed",
                ("$defs", "dataset", "properties", "description", "pattern"),
                delete,
            ),
            (
                "description-pattern-weakened",
                ("$defs", "dataset", "properties", "description", "pattern"),
                ".*",
            ),
            ("measured-conditional-removed", ("$defs", "dataset", "allOf"), delete),
            (
                "measured-condition-const",
                (
                    "$defs",
                    "dataset",
                    "allOf",
                    0,
                    "if",
                    "properties",
                    "classification",
                    "const",
                ),
                "research_scaffold",
            ),
            (
                "measured-min-items-removed",
                (
                    "$defs",
                    "dataset",
                    "allOf",
                    0,
                    "then",
                    "properties",
                    "source_columns",
                    "minItems",
                ),
                delete,
            ),
            (
                "measured-min-items-weakened",
                (
                    "$defs",
                    "dataset",
                    "allOf",
                    0,
                    "then",
                    "properties",
                    "source_columns",
                    "minItems",
                ),
                0,
            ),
            (
                "measured-min-items-boolean",
                (
                    "$defs",
                    "dataset",
                    "allOf",
                    0,
                    "then",
                    "properties",
                    "source_columns",
                    "minItems",
                ),
                True,
            ),
        )
        for case, path, replacement in cases:
            with self.subTest(case=case):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    schema_path = root / "schemas/dataset-manifest.schema.json"
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    target = schema
                    for key in path[:-1]:
                        target = target[key]
                    final_key = path[-1]
                    if replacement is delete:
                        del target[final_key]
                    else:
                        target[final_key] = copy.deepcopy(replacement)
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any("schema contract drift" in error for error in errors),
                        errors,
                    )

    def test_manifest_schema_invalid_annotation_shapes_are_rejected(self) -> None:
        cases = (
            ("root-title", (), "title", 7),
            ("root-description", (), "description", 7),
            ("root-examples", (), "examples", {}),
            ("root-read-only", (), "readOnly", "yes"),
            ("root-comment", (), "$comment", []),
            (
                "nested-title",
                ("$defs", "dataset", "properties", "id"),
                "title",
                7,
            ),
            (
                "nested-description",
                ("$defs", "dataset", "properties", "id"),
                "description",
                7,
            ),
            (
                "nested-examples",
                ("$defs", "dataset", "properties", "id"),
                "examples",
                {},
            ),
            (
                "nested-read-only",
                ("$defs", "dataset", "properties", "id"),
                "readOnly",
                "yes",
            ),
            (
                "nested-comment",
                ("$defs", "dataset", "properties", "id"),
                "$comment",
                [],
            ),
        )
        for case, parent_path, keyword, replacement in cases:
            with self.subTest(case=case):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    schema_path = root / "schemas/dataset-manifest.schema.json"
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    target = schema
                    for key in parent_path:
                        target = target[key]
                    target[keyword] = copy.deepcopy(replacement)
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any(
                            "invalid schema" in error and keyword in error
                            for error in errors
                        ),
                        errors,
                    )

    def test_manifest_schema_unchecked_annotations_are_locked(self) -> None:
        cases = (
            ("root-content-schema", (), "contentSchema", {"type": "string"}),
            (
                "nested-format",
                ("$defs", "dataset", "properties", "id"),
                "format",
                "date-time",
            ),
        )
        for case, parent_path, keyword, value in cases:
            with self.subTest(case=case):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    schema_path = root / "schemas/dataset-manifest.schema.json"
                    schema = json.loads(schema_path.read_text(encoding="utf-8"))
                    target = schema
                    for key in parent_path:
                        target = target[key]
                    target[keyword] = copy.deepcopy(value)
                    schema_path.write_text(json.dumps(schema), encoding="utf-8")

                    errors = validate_repository(root)

                    self.assertTrue(
                        any("schema contract drift" in error for error in errors),
                        errors,
                    )

    def test_manifest_schema_annotations_can_change_without_contract_drift(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            schema_path = root / "schemas/dataset-manifest.schema.json"
            schema = json.loads(schema_path.read_text(encoding="utf-8"))
            schema["title"] = "Renamed manifest schema"
            schema["description"] = "Updated public documentation."
            schema["examples"] = [{"schema_version": 1, "datasets": [], "title": 7}]
            schema["readOnly"] = True
            schema["$comment"] = "Updated root maintainer note."
            id_schema = schema["$defs"]["dataset"]["properties"]["id"]
            id_schema["title"] = "Portable dataset identifier"
            id_schema["description"] = "Updated field documentation."
            id_schema["examples"] = ["sample", {"description": 7}]
            id_schema["readOnly"] = False
            id_schema["$comment"] = "Updated nested maintainer note."
            schema_path.write_text(json.dumps(schema), encoding="utf-8")

            errors = validate_repository(root)

            self.assertEqual(errors, [])

    def test_manifest_schema_annotation_shapes_cover_draft_vocabulary(self) -> None:
        string_keywords = (
            "$comment",
            "contentEncoding",
            "contentMediaType",
            "description",
            "title",
        )
        for keyword in string_keywords:
            with self.subTest(shape="string", keyword=keyword):
                self.assertIsNone(_schema_annotation_error({keyword: ""}))
                error = _schema_annotation_error({keyword: 7})
                self.assertIsNotNone(error)
                self.assertIn(f"/{keyword}: annotation must be a string", error)

        boolean_keywords = ("deprecated", "readOnly", "writeOnly")
        for keyword in boolean_keywords:
            for value in (False, True):
                with self.subTest(
                    shape="boolean-valid",
                    keyword=keyword,
                    value=value,
                ):
                    self.assertIsNone(_schema_annotation_error({keyword: value}))
            for value in (0, 1):
                with self.subTest(
                    shape="boolean-int-invalid",
                    keyword=keyword,
                    value=value,
                ):
                    error = _schema_annotation_error({keyword: value})
                    self.assertIsNotNone(error)
                    self.assertIn(
                        f"/{keyword}: annotation must be a boolean",
                        error,
                    )

        instance_payload = {
            "title": 7,
            "readOnly": 0,
            "properties": {"field": {"description": 9}},
        }
        self.assertIsNone(
            _schema_annotation_error(
                {
                    "default": instance_payload,
                    "examples": [instance_payload],
                }
            )
        )
        examples_error = _schema_annotation_error({"examples": {}})
        self.assertIsNotNone(examples_error)
        self.assertIn("/examples: annotation must be an array", examples_error)

    def test_manifest_schema_annotation_recursion_covers_all_subschemas(self) -> None:
        map_keywords = (
            "$defs",
            "dependentSchemas",
            "patternProperties",
            "properties",
        )
        for keyword in map_keywords:
            with self.subTest(container="map", keyword=keyword):
                error = _schema_annotation_error({keyword: {"title": {"readOnly": 0}}})
                self.assertIsNotNone(error)
                self.assertIn(f"/{keyword}/title/readOnly", error)
                self.assertEqual(
                    _schema_behavior_projection(
                        {
                            keyword: {
                                "title": {
                                    "type": "string",
                                    "title": "Ignored child annotation",
                                }
                            }
                        }
                    ),
                    {keyword: {"title": {"type": "string"}}},
                )

        single_child_keywords = (
            "additionalProperties",
            "contains",
            "else",
            "if",
            "items",
            "not",
            "propertyNames",
            "then",
            "unevaluatedItems",
            "unevaluatedProperties",
        )
        for keyword in single_child_keywords:
            with self.subTest(container="single", keyword=keyword):
                self.assertIsNone(_schema_annotation_error({keyword: False}))
                self.assertIsNone(_schema_annotation_error({keyword: True}))
                error = _schema_annotation_error({keyword: {"writeOnly": 1}})
                self.assertIsNotNone(error)
                self.assertIn(f"/{keyword}/writeOnly", error)
                self.assertEqual(
                    _schema_behavior_projection(
                        {
                            keyword: {
                                "type": "string",
                                "title": "Ignored child annotation",
                            }
                        }
                    ),
                    {keyword: {"type": "string"}},
                )

        array_child_keywords = ("allOf", "anyOf", "oneOf", "prefixItems")
        for keyword in array_child_keywords:
            with self.subTest(container="array", keyword=keyword):
                error = _schema_annotation_error(
                    {keyword: [False, {"deprecated": 0}, True]}
                )
                self.assertIsNotNone(error)
                self.assertIn(f"/{keyword}/1/deprecated", error)
                self.assertEqual(
                    _schema_behavior_projection(
                        {
                            keyword: [
                                {
                                    "type": "string",
                                    "title": "Ignored child annotation",
                                }
                            ]
                        }
                    ),
                    {keyword: [{"type": "string"}]},
                )

    def test_manifest_schema_projection_preserves_opaque_json(self) -> None:
        content_schema = {
            "title": "Locked content annotation",
            "properties": {
                "default": {"const": {"examples": [1, 2]}},
            },
        }
        projected = _schema_behavior_projection(
            {
                "title": "Ignored schema annotation",
                "default": {"title": 7},
                "examples": [{"readOnly": 0}],
                "properties": {
                    "title": {
                        "type": "string",
                        "title": "Ignored child annotation",
                    },
                    "default": {
                        "type": "number",
                        "default": {"title": 7},
                    },
                    "examples": {
                        "type": "boolean",
                        "examples": [{"description": 9}],
                    },
                },
                "const": {"title": 7, "readOnly": 0},
                "enum": [{"title": 7}, {"description": 9}],
                "contentSchema": content_schema,
                "format": "date-time",
            }
        )

        self.assertEqual(
            projected,
            {
                "properties": {
                    "title": {"type": "string"},
                    "default": {"type": "number"},
                    "examples": {"type": "boolean"},
                },
                "const": {"title": 7, "readOnly": 0},
                "enum": [{"description": 9}, {"title": 7}],
                "contentSchema": content_schema,
                "format": "date-time",
            },
        )

        first = _schema_behavior_projection(
            {
                "required": ["second", "first"],
                "type": ["null", "string"],
                "enum": [{"title": 7}, True, 1],
            }
        )
        reordered = _schema_behavior_projection(
            {
                "required": ["first", "second"],
                "type": ["string", "null"],
                "enum": [1, {"title": 7}, True],
            }
        )
        self.assertEqual(_canonical_json(first), _canonical_json(reordered))
        self.assertNotEqual(_canonical_json(True), _canonical_json(1))
        self.assertNotEqual(_canonical_json(False), _canonical_json(0))

    def test_unindexed_nested_and_mixed_case_csvs_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            nested = root / "data/nested"
            nested.mkdir()
            (nested / "unindexed.csv").write_text("value\n1\n", encoding="utf-8")
            (root / "data/UNINDEXED.CSV").write_text("value\n1\n", encoding="utf-8")

            errors = validate_repository(root)

            self.assertTrue(
                any("data/nested/unindexed.csv" in error for error in errors), errors
            )
            self.assertTrue(
                any("data/UNINDEXED.CSV" in error for error in errors), errors
            )

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

            self.assertTrue(
                any("cannot parse 'sample.csv'" in error for error in errors), errors
            )

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

            self.assertTrue(
                any("data directory escapes repository" in error for error in errors),
                errors,
            )

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

            self.assertTrue(
                any("path escapes data/" in error for error in errors), errors
            )

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

            self.assertTrue(
                any("resolves to the same CSV" in error for error in errors), errors
            )

    def test_broken_local_markdown_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            (root / "README.md").write_text(
                "# Fixture\n\n[Missing](does-not-exist.md)\n", encoding="utf-8"
            )
            errors = validate_repository(root)
            self.assertTrue(
                any("missing local link target" in error for error in errors), errors
            )

    def test_only_gfm_fence_indentation_hides_markdown_links(self) -> None:
        cases = (
            ("flush left", "", True),
            ("one space", " ", True),
            ("two spaces", "  ", True),
            ("three spaces", "   ", True),
            ("four spaces", "    ", False),
            ("tab", "\t", False),
            ("non-breaking space", "\u00a0", False),
        )
        for marker in ("```", "~~~"):
            for name, prefix, is_fence in cases:
                with self.subTest(marker=marker, indentation=name):
                    with tempfile.TemporaryDirectory() as directory:
                        root = Path(directory)
                        self.make_fixture(root)
                        (root / "README.md").write_text(
                            f"{prefix}{marker}\n"
                            "[Missing](does-not-exist.md)\n"
                            f"{prefix}{marker}\n",
                            encoding="utf-8",
                        )

                        errors, checked = validate_markdown_links(root)

                        if is_fence:
                            self.assertEqual(errors, [])
                            self.assertEqual(checked, 0)
                        else:
                            self.assertEqual(checked, 1)
                            self.assertTrue(
                                any(
                                    "missing local link target" in error
                                    for error in errors
                                ),
                                errors,
                            )

    def test_four_space_marker_cannot_close_a_gfm_fence(self) -> None:
        for marker in ("```", "~~~"):
            with self.subTest(marker=marker):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    (root / "README.md").write_text(
                        f"{marker}\n"
                        f"    {marker}\n"
                        "[Inside](missing-inside.md)\n"
                        f"{marker}\n"
                        "[Outside](missing-outside.md)\n",
                        encoding="utf-8",
                    )

                    errors, checked = validate_markdown_links(root)

                    self.assertEqual(checked, 1)
                    self.assertTrue(
                        any("missing-outside.md" in error for error in errors),
                        errors,
                    )
                    self.assertFalse(
                        any("missing-inside.md" in error for error in errors),
                        errors,
                    )

    def test_gfm_fence_closers_require_sufficient_length_and_no_info(self) -> None:
        for character in ("`", "~"):
            opener = character * 4
            for name, pseudo_closer in (
                ("shorter marker", character * 3),
                ("trailing info", f"{opener} not-a-closer"),
            ):
                with self.subTest(character=character, closer=name):
                    with tempfile.TemporaryDirectory() as directory:
                        root = Path(directory)
                        self.make_fixture(root)
                        (root / "README.md").write_text(
                            f"{opener}\n"
                            f"{pseudo_closer}\n"
                            "[Inside](missing-inside.md)\n"
                            f"{character * 5}\n"
                            "[Outside](missing-outside.md)\n",
                            encoding="utf-8",
                        )

                        errors, checked = validate_markdown_links(root)

                        self.assertEqual(checked, 1)
                        self.assertTrue(
                            any("missing-outside.md" in error for error in errors),
                            errors,
                        )
                        self.assertFalse(
                            any("missing-inside.md" in error for error in errors),
                            errors,
                        )

    def test_backtick_fence_info_cannot_contain_backticks(self) -> None:
        cases = (
            ("backtick", "```yaml`invalid", "```", False),
            ("tilde control", "~~~yaml`valid", "~~~", True),
        )
        for name, opener, closer, is_fence in cases:
            with self.subTest(case=name):
                with tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    self.make_fixture(root)
                    (root / "README.md").write_text(
                        f"{opener}\n" "[Missing](does-not-exist.md)\n" f"{closer}\n",
                        encoding="utf-8",
                    )

                    errors, checked = validate_markdown_links(root)

                    if is_fence:
                        self.assertEqual(errors, [])
                        self.assertEqual(checked, 0)
                    else:
                        self.assertEqual(checked, 1)
                        self.assertTrue(
                            any(
                                "missing local link target" in error for error in errors
                            ),
                            errors,
                        )

    def test_non_commonmark_separators_do_not_split_fence_lines(self) -> None:
        separators = (
            ("vertical tab", "\v"),
            ("form feed", "\f"),
            ("file separator", "\x1c"),
            ("group separator", "\x1d"),
            ("record separator", "\x1e"),
            ("next line", "\x85"),
            ("line separator", "\u2028"),
            ("paragraph separator", "\u2029"),
        )
        for marker in ("```", "~~~"):
            for name, separator in separators:
                with self.subTest(marker=marker, separator=name):
                    with tempfile.TemporaryDirectory() as directory:
                        root = Path(directory)
                        self.make_fixture(root)
                        (root / "README.md").write_bytes(
                            (
                                f"{marker} text\n"
                                "[Inside A](missing-inside-a.md)\n"
                                f"{marker}{separator}not-a-closer\n"
                                "[Inside B](missing-inside-b.md)\n"
                                f"{marker}\n"
                                "[Outside](missing-outside.md)\n"
                            ).encode("utf-8")
                        )

                        errors, checked = validate_markdown_links(root)

                        self.assertEqual(checked, 1)
                        self.assertEqual(
                            errors,
                            [
                                "README.md:6: missing local link target: "
                                "missing-outside.md"
                            ],
                        )

    def test_cr_lf_and_crlf_split_fence_lines(self) -> None:
        for name, line_ending in (
            ("CR", "\r"),
            ("LF", "\n"),
            ("CRLF", "\r\n"),
        ):
            for marker in ("```", "~~~"):
                with self.subTest(line_ending=name, marker=marker):
                    with tempfile.TemporaryDirectory() as directory:
                        root = Path(directory)
                        self.make_fixture(root)
                        document = line_ending.join(
                            (
                                f"{marker} text",
                                "[Inside](missing-inside.md)",
                                marker,
                                "[Outside](missing-outside.md)",
                                "",
                            )
                        )
                        (root / "README.md").write_bytes(document.encode("utf-8"))

                        errors, checked = validate_markdown_links(root)

                        self.assertEqual(checked, 1)
                        self.assertEqual(
                            errors,
                            [
                                "README.md:4: missing local link target: "
                                "missing-outside.md"
                            ],
                        )

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
                "[FTP](ftp://host/a) [Custom](custom:opaque) " "[Network](//host/a)\n",
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
                        any(
                            "local link escapes repository" in error for error in errors
                        ),
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
                            "unsupported reference-style link; use inline form" in error
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

            self.assertTrue(
                any("cannot decode as UTF-8" in error for error in errors), errors
            )

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
                any(
                    "cannot resolve local link target: loop" in error
                    for error in errors
                ),
                errors,
            )

    @unittest.skipUnless(hasattr(os, "mkfifo"), "FIFOs unavailable")
    def test_markdown_fifo_is_rejected_without_being_opened(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_fixture(root)
            os.mkfifo(root / "pipe.md")

            errors, _ = validate_markdown_links(root)

            self.assertTrue(
                any("not a regular file" in error for error in errors), errors
            )


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
