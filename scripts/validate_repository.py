#!/usr/bin/env python3
"""Validate dataset provenance and local Markdown navigation.

The validator deliberately uses only Python's standard library so contributors
and CI can run it without installing a project toolchain.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import unquote


MANIFEST_RELATIVE_PATH = Path("data/dataset-manifest.json")
SCHEMA_RELATIVE_PATH = Path("schemas/dataset-manifest.schema.json")
DRAFT_2020_12_URI = "https://json-schema.org/draft/2020-12/schema"
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CSV_FILENAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.csv$")
REFERENCE_LINK_PATTERN = re.compile(r"!?\[[^\]\n]+\]\s*\[[^\]\n]*\]")
REFERENCE_DEFINITION_PATTERN = re.compile(r"^[ \t]{0,3}\[[^\]\n]+\]:")
URI_SCHEME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
WINDOWS_ABSOLUTE_PATH_PATTERN = re.compile(r"^[A-Za-z]:[\\/]")
MARKDOWN_DESTINATION_ESCAPE_PATTERN = re.compile(r"\\([\\()])")
REQUIRED_MANIFEST_FIELDS = {"$schema", "schema_version", "datasets"}
REQUIRED_DATASET_FIELDS = {
    "id",
    "path",
    "classification",
    "geographic_scope",
    "temporal_coverage",
    "record_count",
    "source_columns",
    "description",
}
DATASET_CLASSIFICATIONS = {"measured", "research_scaffold"}


class StrictJsonError(ValueError):
    """Raised when a JSON contract uses ambiguous or non-standard constructs."""


class MarkdownLinkSyntaxError(ValueError):
    """Raised when an inline Markdown destination is not closed."""


def _reject_duplicate_json_keys(
    pairs: list[tuple[str, object]],
) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise StrictJsonError(f"duplicate key {key!r}")
        result[key] = value
    return result


def _reject_nonstandard_json_constant(value: str) -> object:
    raise StrictJsonError(f"non-standard constant {value!r}")


def _load_strict_json(path: Path) -> object:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_reject_duplicate_json_keys,
        parse_constant=_reject_nonstandard_json_constant,
    )


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _inside_root(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
    except ValueError:
        return False
    return True


def _has_exact_string_members(value: object, expected: set[str]) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and len(value) == len(set(value))
        and set(value) == expected
    )


def _validate_manifest_schema(root: Path) -> list[str]:
    schema_path = root / SCHEMA_RELATIVE_PATH
    display_path = SCHEMA_RELATIVE_PATH.as_posix()
    try:
        resolved_schema_path = schema_path.resolve()
    except (OSError, RuntimeError) as exc:
        return [f"{display_path}: cannot resolve: {exc}"]
    if not _inside_root(resolved_schema_path, root):
        return [f"{display_path}: path escapes repository"]
    if not resolved_schema_path.is_file():
        return [f"{display_path}: missing or not a regular file"]

    try:
        schema = _load_strict_json(schema_path)
    except StrictJsonError as exc:
        return [f"{display_path}: invalid JSON: {exc}"]
    except json.JSONDecodeError as exc:
        return [f"{display_path}: invalid JSON: {exc}"]
    except UnicodeError as exc:
        return [f"{display_path}: is not valid UTF-8: {exc}"]
    except OSError as exc:
        return [f"{display_path}: cannot read: {exc}"]

    if not isinstance(schema, dict):
        return [f"{display_path}: root must be an object"]

    root_properties = schema.get("properties")
    datasets_schema = (
        root_properties.get("datasets")
        if isinstance(root_properties, dict)
        else None
    )
    dataset_items = (
        datasets_schema.get("items") if isinstance(datasets_schema, dict) else None
    )
    definitions = schema.get("$defs")
    dataset_schema = (
        definitions.get("dataset") if isinstance(definitions, dict) else None
    )
    dataset_properties = (
        dataset_schema.get("properties")
        if isinstance(dataset_schema, dict)
        else None
    )
    contract_is_current = (
        schema.get("$schema") == DRAFT_2020_12_URI
        and schema.get("type") == "object"
        and schema.get("additionalProperties") is False
        and _has_exact_string_members(
            schema.get("required"), REQUIRED_MANIFEST_FIELDS
        )
        and isinstance(root_properties, dict)
        and set(root_properties) == REQUIRED_MANIFEST_FIELDS
        and isinstance(datasets_schema, dict)
        and datasets_schema.get("type") == "array"
        and isinstance(dataset_items, dict)
        and dataset_items.get("$ref") == "#/$defs/dataset"
        and isinstance(dataset_schema, dict)
        and dataset_schema.get("type") == "object"
        and dataset_schema.get("additionalProperties") is False
        and _has_exact_string_members(
            dataset_schema.get("required"), REQUIRED_DATASET_FIELDS
        )
        and isinstance(dataset_properties, dict)
        and set(dataset_properties) == REQUIRED_DATASET_FIELDS
    )
    if not contract_is_current:
        return [f"{display_path}: schema contract drift"]
    return []


def validate_dataset_manifest(root: Path) -> tuple[list[str], int]:
    """Return manifest/CSV errors and the number of indexed datasets."""

    errors: list[str] = []
    root = root.resolve()
    errors.extend(_validate_manifest_schema(root))
    data_dir = root / "data"
    manifest_path = root / MANIFEST_RELATIVE_PATH

    try:
        resolved_data_dir = data_dir.resolve()
    except (OSError, RuntimeError) as exc:
        return ([f"data/: cannot resolve data directory: {exc}"], 0)
    if not _inside_root(resolved_data_dir, root):
        return (["data/: data directory escapes repository"], 0)
    try:
        resolved_manifest_path = manifest_path.resolve()
    except (OSError, RuntimeError) as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: cannot resolve: {exc}"], 0)
    if not _inside_root(resolved_manifest_path, resolved_data_dir):
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: path escapes data/"], 0)
    if not resolved_manifest_path.is_file():
        return (
            [
                f"{MANIFEST_RELATIVE_PATH.as_posix()}: "
                "missing or not a regular file"
            ],
            0,
        )

    try:
        manifest = _load_strict_json(manifest_path)
    except FileNotFoundError:
        return ([f"missing manifest: {MANIFEST_RELATIVE_PATH.as_posix()}"], 0)
    except StrictJsonError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: invalid JSON: {exc}"], 0)
    except json.JSONDecodeError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: invalid JSON: {exc}"], 0)
    except UnicodeError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: is not valid UTF-8: {exc}"], 0)
    except OSError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: cannot read: {exc}"], 0)

    if not isinstance(manifest, dict):
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: root must be an object"], 0)
    extra_manifest_fields = sorted(manifest.keys() - REQUIRED_MANIFEST_FIELDS)
    if extra_manifest_fields:
        errors.append(
            "dataset manifest has unexpected fields: "
            + ", ".join(extra_manifest_fields)
        )
    if manifest.get("$schema") != "../schemas/dataset-manifest.schema.json":
        errors.append("dataset manifest has an unexpected $schema path")
    schema_version = manifest.get("schema_version")
    if (
        isinstance(schema_version, bool)
        or not isinstance(schema_version, int)
        or schema_version != 1
    ):
        errors.append("dataset manifest schema_version must be the integer 1")

    datasets = manifest.get("datasets")
    if not isinstance(datasets, list):
        errors.append("dataset manifest 'datasets' must be an array")
        return (errors, 0)

    seen_ids: set[str] = set()
    seen_paths: set[str] = set()
    seen_csv_targets: dict[Path, str] = {}

    for index, entry in enumerate(datasets):
        prefix = f"datasets[{index}]"
        if not isinstance(entry, dict):
            errors.append(f"{prefix}: entry must be an object")
            continue

        missing = sorted(REQUIRED_DATASET_FIELDS - entry.keys())
        extra = sorted(entry.keys() - REQUIRED_DATASET_FIELDS)
        if missing:
            errors.append(f"{prefix}: missing fields: {', '.join(missing)}")
        if extra:
            errors.append(f"{prefix}: unexpected fields: {', '.join(extra)}")

        dataset_id = entry.get("id")
        if not _nonempty_string(dataset_id) or not ID_PATTERN.fullmatch(dataset_id):
            errors.append(f"{prefix}: invalid id")
        elif dataset_id in seen_ids:
            errors.append(f"{prefix}: duplicate id '{dataset_id}'")
        else:
            seen_ids.add(dataset_id)

        relative_path = entry.get("path")
        path_is_safe = (
            _nonempty_string(relative_path)
            and CSV_FILENAME_PATTERN.fullmatch(relative_path)
        )
        if not path_is_safe:
            errors.append(
                f"{prefix}: path must name one portable CSV directly inside data/"
            )
            continue
        if relative_path in seen_paths:
            errors.append(f"{prefix}: duplicate path '{relative_path}'")
        else:
            seen_paths.add(relative_path)
        if _nonempty_string(dataset_id) and Path(relative_path).stem != dataset_id:
            errors.append(f"{prefix}: id must match the CSV filename stem")

        classification = entry.get("classification")
        if (
            not isinstance(classification, str)
            or classification not in DATASET_CLASSIFICATIONS
        ):
            errors.append(f"{prefix}: invalid classification '{classification}'")

        geographic_scope = entry.get("geographic_scope")
        if not (
            isinstance(geographic_scope, list)
            and geographic_scope
            and all(_nonempty_string(value) for value in geographic_scope)
            and len(geographic_scope) == len(set(geographic_scope))
        ):
            errors.append(f"{prefix}: geographic_scope must contain unique non-empty strings")

        for field in ("temporal_coverage", "description"):
            if not _nonempty_string(entry.get(field)):
                errors.append(f"{prefix}: {field} must be a non-empty string")

        record_count = entry.get("record_count")
        if isinstance(record_count, bool) or not isinstance(record_count, int) or record_count < 1:
            errors.append(f"{prefix}: record_count must be a positive integer")

        source_columns = entry.get("source_columns")
        source_columns_are_valid = (
            isinstance(source_columns, list)
            and all(_nonempty_string(value) for value in source_columns)
            and len(source_columns) == len(set(source_columns))
        )
        if not source_columns_are_valid:
            errors.append(f"{prefix}: source_columns must contain unique non-empty strings")
        elif classification == "measured" and not source_columns:
            errors.append(f"{prefix}: measured datasets require at least one source column")

        try:
            csv_path = (data_dir / relative_path).resolve()
        except (OSError, RuntimeError) as exc:
            errors.append(f"{prefix}: cannot resolve '{relative_path}': {exc}")
            continue
        if not _inside_root(csv_path, resolved_data_dir):
            errors.append(f"{prefix}: path escapes data/")
            continue
        if not csv_path.is_file():
            errors.append(f"{prefix}: missing CSV '{relative_path}'")
            continue
        previous_path = seen_csv_targets.get(csv_path)
        if previous_path is not None:
            errors.append(
                f"{prefix}: '{relative_path}' resolves to the same CSV as "
                f"'{previous_path}'"
            )
        else:
            seen_csv_targets[csv_path] = relative_path

        try:
            with csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
                rows = list(csv.reader(handle, strict=True))
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f"{prefix}: cannot parse '{relative_path}': {exc}")
            continue

        if not rows:
            errors.append(f"{prefix}: '{relative_path}' is empty")
            continue
        header = rows[0]
        if not header or any(not column.strip() for column in header):
            errors.append(f"{prefix}: '{relative_path}' has a blank header")
        if len(header) != len(set(header)):
            errors.append(f"{prefix}: '{relative_path}' has duplicate headers")

        data_rows = rows[1:]
        if isinstance(record_count, int) and not isinstance(record_count, bool):
            if len(data_rows) != record_count:
                errors.append(
                    f"{prefix}: record_count is {record_count}, CSV contains {len(data_rows)} rows"
                )

        blank_rows = [
            line_number
            for line_number, row in enumerate(data_rows, start=2)
            if not any(cell.strip() for cell in row)
        ]
        if blank_rows:
            errors.append(
                f"{prefix}: '{relative_path}' has blank data rows at lines "
                + ", ".join(map(str, blank_rows))
            )

        malformed_rows = [
            line_number
            for line_number, row in enumerate(data_rows, start=2)
            if len(row) != len(header)
        ]
        if malformed_rows:
            errors.append(
                f"{prefix}: '{relative_path}' has wrong-width rows at lines "
                + ", ".join(map(str, malformed_rows))
            )
            continue

        if source_columns_are_valid:
            missing_source_columns = [
                column for column in source_columns if column not in header
            ]
            if missing_source_columns:
                errors.append(
                    f"{prefix}: source columns absent from CSV: "
                    + ", ".join(missing_source_columns)
                )
            elif classification == "measured":
                source_indexes = [header.index(column) for column in source_columns]
                rows_without_source = [
                    line_number
                    for line_number, row in enumerate(data_rows, start=2)
                    if not any(row[source_index].strip() for source_index in source_indexes)
                ]
                if rows_without_source:
                    errors.append(
                        f"{prefix}: measured rows lack a source at lines "
                        + ", ".join(map(str, rows_without_source))
                    )

    actual_csv_paths: set[str] = set()
    try:
        for candidate in data_dir.rglob("*"):
            relative_candidate = candidate.relative_to(data_dir).as_posix()
            if candidate.is_symlink():
                try:
                    resolved_candidate = candidate.resolve()
                except (OSError, RuntimeError) as exc:
                    errors.append(
                        f"data/{relative_candidate}: cannot resolve symlink: {exc}"
                    )
                    continue
                if not _inside_root(resolved_candidate, resolved_data_dir):
                    errors.append(f"data/{relative_candidate}: symlink escapes data/")
            if candidate.suffix.casefold() == ".csv" and (
                candidate.is_file() or candidate.is_symlink()
            ):
                actual_csv_paths.add(relative_candidate)
    except OSError as exc:
        errors.append(f"data/: cannot enumerate CSV files: {exc}")

    for unlisted in sorted(actual_csv_paths - seen_paths):
        errors.append(f"data/{unlisted}: CSV is not listed in the dataset manifest")
    for absent in sorted(seen_paths - actual_csv_paths):
        errors.append(f"data/{absent}: manifest entry has no matching CSV")

    return (errors, len(datasets))


def _markdown_lines_outside_fences(path: Path) -> Iterator[tuple[int, str]]:
    fence: str | None = None
    for line_number, line in enumerate(
        path.read_text(encoding="utf-8").splitlines(), start=1
    ):
        stripped = line.lstrip()
        if stripped.startswith(("```", "~~~")):
            marker = stripped[:3]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            yield line_number, line


def _inline_markdown_targets(line: str) -> Iterator[str]:
    label_stack: list[int] = []
    cursor = 0
    while cursor < len(line):
        character = line[cursor]
        if character == "\\":
            cursor += 2
            continue
        if character == "[":
            label_stack.append(cursor)
            cursor += 1
            continue
        if character != "]" or not label_stack:
            cursor += 1
            continue

        label_stack.pop()
        if cursor + 1 >= len(line) or line[cursor + 1] != "(":
            cursor += 1
            continue

        target_start = cursor + 2
        if target_start < len(line) and line[target_start] == "<":
            index = target_start + 1
            while index < len(line):
                if line[index] == "\\":
                    index += 2
                    continue
                if line[index] == ">":
                    break
                index += 1
            if index >= len(line):
                raise MarkdownLinkSyntaxError("unterminated angle destination")
            target = line[target_start + 1 : index]
            closing = index + 1
            while closing < len(line) and line[closing].isspace():
                closing += 1
            if closing >= len(line) or line[closing] != ")":
                raise MarkdownLinkSyntaxError("angle destination must end with ')'")
            yield target
            cursor = closing + 1
            continue

        depth = 1
        index = target_start
        while index < len(line):
            character = line[index]
            if character == "\\":
                index += 2
                continue
            if character == "(":
                depth += 1
            elif character == ")":
                depth -= 1
                if depth == 0:
                    break
            index += 1
        if depth:
            raise MarkdownLinkSyntaxError("unterminated parenthesized destination")

        raw_target = line[target_start:index].strip()
        parts = raw_target.split(maxsplit=1)
        target = parts[0] if parts else ""
        yield MARKDOWN_DESTINATION_ESCAPE_PATTERN.sub(r"\1", target)
        cursor = index + 1


def validate_markdown_links(root: Path) -> tuple[list[str], int]:
    """Validate canonical inline Markdown link destinations used by the repository."""

    errors: list[str] = []
    checked = 0
    root = root.resolve()

    try:
        candidates = sorted(root.rglob("*"))
    except (OSError, RuntimeError) as exc:
        return ([f"repository: cannot enumerate Markdown sources: {exc}"], 0)

    for markdown_path in candidates:
        display_path = markdown_path.relative_to(root).as_posix()
        if ".git" in markdown_path.relative_to(root).parts:
            continue
        if markdown_path.suffix.casefold() != ".md":
            continue
        try:
            resolved_markdown_path = markdown_path.resolve(strict=True)
        except (OSError, RuntimeError) as exc:
            errors.append(f"{display_path}: cannot resolve Markdown source: {exc}")
            continue
        if not _inside_root(resolved_markdown_path, root):
            errors.append(f"{display_path}: Markdown source escapes repository")
            continue
        if not resolved_markdown_path.is_file():
            errors.append(f"{display_path}: Markdown source is not a regular file")
            continue

        try:
            lines = _markdown_lines_outside_fences(resolved_markdown_path)
            for line_number, line in lines:
                has_reference_style = bool(
                    REFERENCE_LINK_PATTERN.search(line)
                    or REFERENCE_DEFINITION_PATTERN.match(line)
                )
                if has_reference_style:
                    errors.append(
                        f"{display_path}:{line_number}: unsupported reference-style "
                        "link; use inline form"
                    )
                try:
                    targets = list(_inline_markdown_targets(line))
                except MarkdownLinkSyntaxError as exc:
                    errors.append(
                        f"{display_path}:{line_number}: unsupported inline link: {exc}"
                    )
                    continue

                for target in targets:
                    target = target.strip()
                    if not target:
                        continue
                    if WINDOWS_ABSOLUTE_PATH_PATTERN.match(target):
                        checked += 1
                        errors.append(
                            f"{display_path}:{line_number}: local link escapes "
                            f"repository: {target}"
                        )
                        continue
                    if target.startswith("//") or URI_SCHEME_PATTERN.match(target):
                        continue

                    path_part = target.split("#", 1)[0].split("?", 1)[0]
                    if not path_part:
                        continue
                    path_part = unquote(path_part)
                    checked += 1
                    try:
                        if path_part.startswith("/"):
                            resolved = (root / path_part.lstrip("/")).resolve()
                        else:
                            resolved = (
                                resolved_markdown_path.parent / path_part
                            ).resolve()
                    except (OSError, RuntimeError) as exc:
                        errors.append(
                            f"{display_path}:{line_number}: cannot resolve local "
                            f"link target: {target} ({exc})"
                        )
                        continue

                    if not _inside_root(resolved, root):
                        errors.append(
                            f"{display_path}:{line_number}: local link escapes repository: {target}"
                        )
                    elif not resolved.exists():
                        errors.append(
                            f"{display_path}:{line_number}: missing local link target: {target}"
                        )
        except UnicodeError as exc:
            errors.append(f"{display_path}: cannot decode as UTF-8: {exc}")
        except OSError as exc:
            errors.append(f"{display_path}: cannot read Markdown source: {exc}")

    return (errors, checked)


def validate_repository(root: Path) -> list[str]:
    dataset_errors, _ = validate_dataset_manifest(root)
    link_errors, _ = validate_markdown_links(root)
    return dataset_errors + link_errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    dataset_errors, dataset_count = validate_dataset_manifest(root)
    link_errors, link_count = validate_markdown_links(root)
    errors = dataset_errors + link_errors

    if errors:
        print(f"Repository validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Repository validation passed: {dataset_count} datasets indexed; "
        f"{link_count} canonical inline Markdown links resolved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
