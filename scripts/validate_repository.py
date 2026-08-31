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
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CSV_FILENAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.csv$")
MARKDOWN_LINK_PATTERN = re.compile(
    r"!?\[[^\]]*\]\((?P<target><[^>\n]+>|[^)\n]+)\)"
)
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

    try:
        manifest = _load_strict_json(manifest_path)
    except FileNotFoundError:
        return ([f"missing manifest: {MANIFEST_RELATIVE_PATH.as_posix()}"], 0)
    except StrictJsonError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: invalid JSON: {exc}"], 0)
    except json.JSONDecodeError as exc:
        return ([f"{MANIFEST_RELATIVE_PATH.as_posix()}: invalid JSON: {exc}"], 0)

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


def validate_markdown_links(root: Path) -> tuple[list[str], int]:
    """Return broken/escaping local-link errors and number of local links checked."""

    errors: list[str] = []
    checked = 0
    root = root.resolve()

    for markdown_path in sorted(root.rglob("*.md")):
        if ".git" in markdown_path.parts:
            continue
        try:
            lines = _markdown_lines_outside_fences(markdown_path)
            for line_number, line in lines:
                for match in MARKDOWN_LINK_PATTERN.finditer(line):
                    target = match.group("target").strip()
                    if target.startswith("<") and target.endswith(">"):
                        target = target[1:-1]
                    else:
                        parts = target.split(maxsplit=1)
                        if not parts:
                            continue
                        target = parts[0]
                    lowered = target.lower()
                    if lowered.startswith(("http://", "https://", "mailto:", "data:")):
                        continue

                    path_part = target.split("#", 1)[0].split("?", 1)[0]
                    if not path_part:
                        continue
                    path_part = unquote(path_part)
                    if path_part.startswith("/"):
                        resolved = (root / path_part.lstrip("/")).resolve()
                    else:
                        resolved = (markdown_path.parent / path_part).resolve()
                    checked += 1

                    display_path = markdown_path.relative_to(root).as_posix()
                    if not _inside_root(resolved, root):
                        errors.append(
                            f"{display_path}:{line_number}: local link escapes repository: {target}"
                        )
                    elif not resolved.exists():
                        errors.append(
                            f"{display_path}:{line_number}: missing local link target: {target}"
                        )
        except UnicodeError as exc:
            display_path = markdown_path.relative_to(root).as_posix()
            errors.append(f"{display_path}: cannot decode as UTF-8: {exc}")

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
        f"{link_count} local Markdown links resolved."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
