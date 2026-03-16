# `era_pl_templates`

Runnable Quarto templates for readers of *Empirical Research in Accounting*.

This repository contains slimmed-down, self-contained versions of selected book chapters with the focus on code that readers can run locally. The initial template is [`bb68.qmd`](bb68.qmd), which reproduces an analogue of Figure 1 from Ball and Brown (1968).

## Downloading the project

Most readers will not need `git`.

1. Open the repository page on GitHub.
2. Click `Code`.
3. Click `Download ZIP`.
4. Unzip the downloaded archive.
5. Open a terminal and change into the unzipped `era_pl_templates` folder.

On macOS:

1. Open Terminal.
2. Run `cd ` and then drag the unzipped `era_pl_templates` folder into the Terminal window.
3. Press Enter.

On Linux:

1. Open your terminal application.
2. Use `cd` to move into the unzipped `era_pl_templates` folder.

On Windows:

1. Open PowerShell.
2. Use `cd` to move into the unzipped `era_pl_templates` folder.

If you prefer, you can also clone the repository with `git clone`.

## Prerequisites

Install the following tools before working with the template:

1. `uv`
2. Quarto CLI

### Install `uv`

On macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

See the official installation instructions at <https://docs.astral.sh/uv/>.

### Install Quarto

Install Quarto CLI from <https://quarto.org/docs/get-started/>.

## Project setup

Run the following commands from a terminal, in the project root directory (the `era_pl_templates` folder that contains this `README.md`).

Create the project virtual environment and install the Python dependencies:

```bash
uv sync
```

This command creates a local `.venv` directory and installs the dependencies listed in [`pyproject.toml`](pyproject.toml).

If you want to be explicit about the interpreter version, you can use:

```bash
uv sync --python 3.13
```

## Environment variables

Still in the project root, create a `.env` file. Do not commit this file.

You can start from the checked-in example:

```bash
cp .env.example .env
```

Then edit `.env` so that it contains your WRDS username and the absolute path to your local Parquet repository:

```env
WRDS_ID=your_wrds_username
DATA_DIR=/absolute/path/to/pq_data
```

## Getting the data from WRDS

The template expects local Parquet versions of a small set of WRDS tables. Those files can be created with [`db2pq`](https://pypi.org/project/db2pq/), which is installed as part of the project environment.

After creating `.env`, run the following command from a terminal in the project root:

```bash
uv run python
```

If you already use either `db2pq` or `wrds2pg`, you may already have `DATA_DIR` set in your shell environment. If you want this repository to use a different `DATA_DIR` from `.env`, run `unset DATA_DIR` before running `uv run python`.

Then, at the Python prompt, run:

```python
from db2pq import wrds_update_pq

# CRSP
wrds_update_pq("msi", "crsp")
wrds_update_pq("msf", "crsp")
wrds_update_pq("stocknames", "crsp")
wrds_update_pq("ccmxpf_lnkhist", "crsp",
               col_types={"lpermno": "int32", "lpermco": "int32"})

# Compustat
wrds_update_pq("funda", "comp")
wrds_update_pq("fundq", "comp")
```

If you prefer a one-liner instead of entering Python interactively, run:

```bash
uv run python -c 'from db2pq import wrds_update_pq; wrds_update_pq("msi", "crsp"); wrds_update_pq("msf", "crsp"); wrds_update_pq("stocknames", "crsp"); wrds_update_pq("ccmxpf_lnkhist", "crsp", col_types={"lpermno": "int32", "lpermco": "int32"}); wrds_update_pq("funda", "comp"); wrds_update_pq("fundq", "comp")'
```

## Working with Jupyter

If you prefer to work with a notebook instead of editing the Quarto source directly, run the following command from a terminal in the project root:

```bash
quarto convert bb68.qmd
```

This creates `bb68.ipynb` in the project root.

You can then open the notebook in JupyterLab with:

```bash
uv run jupyter lab bb68.ipynb
```

## Rendering the template

Render the document with:

```bash
uv run quarto render bb68.qmd
```

For iterative work, preview it with:

```bash
uv run quarto preview bb68.qmd
```
