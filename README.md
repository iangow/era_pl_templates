# `era_pl_templates`

Runnable Quarto templates for readers of *Empirical Research in Accounting*.

This repository contains slimmed-down, self-contained versions of selected book chapters with the focus on code that readers can run locally.

Current templates include:

- [`bb68.qmd`](bb68.qmd), which reproduces an analogue of Figure 1 from Ball and Brown (1968)
- [`py-intro.qmd`](py-intro.qmd), a Python introduction template based on early material from the book

## Step 1: Download the project

1. Open the repository page on GitHub.
2. Click `Code`.
3. Click `Download ZIP`.
4. Find the downloaded ZIP file on your computer.
5. Unzip the downloaded archive.

After unzipping, you should have a folder named something like `era_pl_templates-main`.

You may rename this folder to something more meaningful for your own work, such as `era_homework`.
You may also move the folder to any convenient location on your computer before opening it in Positron.

## Step 2: Install the prerequisites

Install the following tools before working with the template:

1. `uv`
2. Positron

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

### Install Positron

Download Positron from <https://positron.posit.co/download.html> and install it using the normal steps for your operating system.

## Step 3: Set up the project

Open the project folder in Positron:

1. Start Positron.
2. Choose `File` > `Open Folder...` (or the similar option shown on the welcome screen).
3. Select the unzipped repository folder.
4. Open the folder.

You should now see files such as [`README.md`](README.md), [`pyproject.toml`](pyproject.toml), and the `.qmd` template files in the Positron file browser.

Then run the following commands from a terminal, in the project root directory (the folder you opened in Positron and containing this `README.md`).

In Positron, you can open a terminal using `Terminal` > `New Terminal`.

Create the project virtual environment and install the Python dependencies:

```bash
uv sync
```

This command creates a local `.venv` directory and installs the dependencies listed in [`pyproject.toml`](pyproject.toml).
It also installs the bundled `psycopg` PostgreSQL client so macOS users do not need a separate `libpq` installation just to download WRDS tables.

If you want to be explicit about the interpreter version, you can use:

```bash
uv sync --python 3.13
```

If you already ran `uv sync` before this dependency was added and see an error like `ImportError: no pq wrapper available`, run:

```bash
uv sync --reinstall
```

That refreshes the virtual environment and installs the bundled PostgreSQL client library used by `psycopg`.

## Step 4: Create environment variables

> [!NOTE]
> You do not need Steps 4 and 5 for Chapters 1 through 5.
> Most readers can skip both sections until they reach Chapter 6.

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

## Step 5: Get data from WRDS

The template expects local Parquet versions of a small set of WRDS tables. Those files can be created with [`db2pq`](https://pypi.org/project/db2pq/), which is installed as part of the project environment.

After creating `.env`, run the following command from a terminal in the project root:

```bash
uv run python
```

If you already use either `db2pq` or `wrds2pg`, you may already have `DATA_DIR` set in your shell environment. If you want this repository to use a different `DATA_DIR` from `.env`, run `unset DATA_DIR` before launching Python or running the helper script below.

Then, at the Python prompt, run:

```python
from db2pq import wrds_update_pq

# CRSP
wrds_update_pq('ccmxpf_lnkhist', 'crsp', 
               col_types={'lpermno': 'int32',
                          'lpermco': 'int32'})
wrds_update_pq('stocknames', 'crsp')
wrds_update_pq('dsi', 'crsp')
wrds_update_pq('comphist', 'crsp')
wrds_update_pq('dsedelist', 'crsp') 
wrds_update_pq('dseexchdates', 'crsp', force=True)
wrds_update_pq('dsedist', 'crsp')
wrds_update_pq('msi', 'crsp')
wrds_update_pq('mse', 'crsp')
wrds_update_pq('msf', 'crsp')
wrds_update_pq('erdport1', 'crsp')
wrds_update_pq('dsf', 'crsp')

# Fama-French library
wrds_update_pq('factors_daily', 'ff')

# Compustat
wrds_update_pq('company', 'comp')
wrds_update_pq('funda', 'comp')
wrds_update_pq('funda_fncd', 'comp')
wrds_update_pq('fundq', 'comp')
wrds_update_pq('r_auditors', 'comp')
wrds_update_pq('idx_daily', 'comp')
wrds_update_pq('aco_pnfnda', 'comp')

# compseg
wrds_update_pq('seg_customer', 'compseg')
wrds_update_pq('names_seg', 'compseg')
```

If you prefer a script instead of entering Python interactively, run:

```bash
uv run scripts/download_wrds_tables.py
```

## Step 6: Render the template

Choose the template you want to render, then run:

```bash
uv run quarto render bb68.qmd
```

For example, to render the Python introduction template:

```bash
uv run quarto render py-intro.qmd
```

For iterative work, preview a template with:

```bash
uv run quarto preview bb68.qmd
```

## Optional: Work in Positron

To work on a template in Positron:

1. Open the repository folder in Positron.
2. Open the `.qmd` file you want to work on, such as [`bb68.qmd`](bb68.qmd) or [`py-intro.qmd`](py-intro.qmd).
3. Open a terminal in Positron and run `uv sync` if you have not already done so.
4. Render or preview the file from the terminal.

For example:

```bash
uv run quarto preview py-intro.qmd
```

For readers who do not want to install Positron, see the optional Jupyter-based path below.

## Optional: Work with Jupyter Instead of Positron

If you do not want to install Positron, you will also need to install Quarto CLI separately. Install Quarto from <https://quarto.org/docs/get-started/>.

If you prefer to work with a notebook instead of editing the Quarto source directly, first choose the template you want to work on. Then run the following command from a terminal in the project root:

```bash
quarto convert bb68.qmd
```

For example, the command above creates `bb68.ipynb` in the project root. You can do the same for other templates, such as:

```bash
quarto convert py-intro.qmd
```

You can then open the notebook in JupyterLab with:

```bash
uv run jupyter lab bb68.ipynb
```

## Optional: Using Git

Most readers do not need `git` for this repository.

If you already use Git and prefer to clone the repository instead of downloading a ZIP file, you can do that as well.
