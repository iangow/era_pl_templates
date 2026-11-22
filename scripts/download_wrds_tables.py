"""Download, or just check, the WRDS tables the templates read.

    uv run scripts/download_wrds_tables.py                  # download everything
    uv run scripts/download_wrds_tables.py --chapter pead   # only one chapter's tables
    uv run scripts/download_wrds_tables.py --check          # report what is missing
    uv run scripts/download_wrds_tables.py --check --json   # the same, as JSON

`--check` opens no connection and needs no WRDS account. It exits with status 1
when a table is missing. The table list lives in `data_manifest.toml`.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data_manifest.toml"
LOAD_PARQUET = re.compile(
    r'load_parquet\(\s*(?:table\s*=\s*)?"(\w+)"\s*,\s*(?:schema\s*=\s*)?"(\w+)"'
)


def load_manifest() -> dict:
    with MANIFEST.open("rb") as fh:
        return tomllib.load(fh)


def scan_templates() -> dict[str, list[str]]:
    """Tables each template names in a `load_parquet(...)` call."""
    found = {}
    for qmd in sorted(ROOT.glob("*.qmd")):
        text = qmd.read_text(encoding="utf-8")
        found[qmd.stem] = sorted(
            {f"{schema}.{table}" for table, schema in LOAD_PARQUET.findall(text)}
        )
    return found


def data_dir() -> Path:
    from dotenv import load_dotenv

    load_dotenv(ROOT / ".env")
    value = os.getenv("DATA_DIR")
    if not value:
        sys.exit(
            "DATA_DIR is not set. Copy .env.example to .env and set DATA_DIR "
            "to the folder that holds (or will hold) the Parquet files."
        )
    path = Path(value).expanduser()
    return path if path.is_absolute() else (ROOT / path).resolve()


def selected(manifest: dict, chapters: list[str] | None) -> list[str]:
    """`schema.table` names to act on, WRDS tables first in manifest order."""
    wrds = [f"{t['schema']}.{t['table']}" for t in manifest["wrds"]]
    if not chapters:
        return wrds
    unknown = [c for c in chapters if c not in manifest["chapters"]]
    if unknown:
        sys.exit(
            f"Unknown chapter(s): {', '.join(unknown)}. "
            f"Choose from: {', '.join(manifest['chapters'])}."
        )
    wanted = {t for c in chapters for t in manifest["chapters"][c]}
    return [t for t in wrds if t in wanted] + sorted(wanted - set(wrds))


def check(manifest: dict, tables: list[str], root: Path) -> dict:
    wrds = {f"{t['schema']}.{t['table']}" for t in manifest["wrds"]}
    rows = []
    for name in tables:
        schema, table = name.split(".", 1)
        path = root / schema / f"{table}.parquet"
        rows.append(
            {
                "table": name,
                "path": str(path),
                "exists": path.is_file(),
                "source": "wrds" if name in wrds else "other",
                "note": None if name in wrds else manifest.get("other", {}).get(schema),
            }
        )
    missing = [r["table"] for r in rows if not r["exists"]]
    return {"data_dir": str(root), "ok": not missing, "missing": missing, "tables": rows}


def download(manifest: dict, tables: list[str], dry_run: bool) -> None:
    kwargs = {f"{t['schema']}.{t['table']}": t.get("kwargs", {}) for t in manifest["wrds"]}
    todo = [t for t in tables if t in kwargs]
    skipped = [t for t in tables if t not in kwargs]
    if dry_run:
        for name in todo:
            print(f"would download {name} {kwargs[name] or ''}".rstrip())
    else:
        from db2pq import wrds_update_pq

        for name in todo:
            schema, table = name.split(".", 1)
            wrds_update_pq(table, schema, **kwargs[name])
    for name in skipped:
        print(f"not a WRDS download, skipped: {name}", file=sys.stderr)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--chapter", action="append", metavar="NAME",
        help="Template name without .qmd, e.g. pead. Repeat for several.",
    )
    parser.add_argument("--check", action="store_true", help="Only report what is missing.")
    parser.add_argument("--dry-run", action="store_true", help="List downloads, do nothing.")
    parser.add_argument("--json", action="store_true", help="With --check, print JSON.")
    parser.add_argument(
        "--scan", action="store_true",
        help="Compare the [chapters] lists in data_manifest.toml with the templates.",
    )
    args = parser.parse_args(argv)
    manifest = load_manifest()

    if args.scan:
        drift = {
            c: {"manifest": manifest["chapters"].get(c), "templates": t}
            for c, t in scan_templates().items()
            if manifest["chapters"].get(c) != t
        }
        print(json.dumps(drift, indent=2) if drift else "data_manifest.toml matches the templates.")
        return 1 if drift else 0

    tables = selected(manifest, args.chapter)
    if args.check:
        result = check(manifest, tables, data_dir())
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            for row in result["tables"]:
                print(f"{'present' if row['exists'] else 'MISSING'}: {row['table']}")
        return 0 if result["ok"] else 1

    if not args.dry_run:
        data_dir()
    download(manifest, tables, args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
