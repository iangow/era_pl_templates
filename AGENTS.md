# Notes for coding agents

These are Quarto templates for the Python Polars edition of *Empirical
Research in Accounting*. Each `<chapter>.qmd` is self-contained and renders to
PDF. A reader works through one template at a time.

## Environment

- `uv sync` creates `.venv`. Run everything through `uv run ...` so the pinned
  packages are used, not the system Python.
- Render one template with `uv run quarto render <chapter>.qmd`.
- Code cells assume they run top to bottom. Do not run a cell in isolation.

## Data

- `data_manifest.toml` is the single list of the Parquet tables each template
  loads from `DATA_DIR`. Read it before running a chapter.
- `uv run scripts/download_wrds_tables.py --check --chapter <chapter> --json`
  reports which of that chapter's tables are missing. It opens no connection
  and exits 1 when something is missing. Run it before rendering.
- The `[chapters]` lists come from the `load_parquet(...)` calls in each
  template. A few `era_pl` helpers load further tables internally, so a
  chapter can still fail on a missing file after `--check` passes. The error
  names the file. Add the table to the manifest when that happens.
- Chapters with an empty list in the manifest need no local Parquet data.
  Small data sets from the book ship with the `era-py` package and load with
  `era_pl.load_data(...)`.
- Downloading needs a WRDS account. If the user has none, do not look for the
  data elsewhere and do not fabricate stand-in files. Report the missing
  tables and work on the chapters that need none.
- `uv run scripts/download_wrds_tables.py --chapter <chapter>` downloads one
  chapter's tables. Set `DB2PQ_NONINTERACTIVE=1` first so a missing credential
  raises an error instead of waiting for input.
- The `glms.*` tables are not WRDS downloads. See the note at the top of
  `glms.qmd`.

## Files not to touch or commit

- `.env` holds `WRDS_ID` and `DATA_DIR`. Never commit it and never print a
  password or the contents of `~/.pgpass`.
- Parquet files under `DATA_DIR` are licensed data. Do not copy them into the
  repository, into an issue or into a chat.

## Editing a template

- Exercises are for the reader to answer. Do not fill them in unless asked.
- After changing a `load_parquet(...)` call, run
  `uv run scripts/download_wrds_tables.py --scan` and update
  `data_manifest.toml` if it reports a difference.
