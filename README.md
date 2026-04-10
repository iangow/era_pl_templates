# `era_pl_templates`

Runnable Quarto templates for readers of *Empirical Research in Accounting*.

This repository contains slimmed-down, self-contained versions of selected book chapters with the focus on code that readers can run locally.

For now, the recommended starting point is [`py-intro.qmd`](py-intro.qmd), a Python introduction template based on early material from the book.

## Step 1: Download the project

1. Open the repository page on GitHub.
2. Click `Code`.
3. Click `Download ZIP`.
4. Find the downloaded ZIP file on your computer.
5. Unzip the downloaded archive.

After unzipping, you should have a folder named something like `era_pl_templates-main`.

You may rename this folder to something more meaningful for your own work, such as `era_homework`.
You may also move the folder to any convenient location on your computer before opening it in Positron.

### If you already created an empty project in Positron

If you used Positron's `New Folder` interface first, that is fine, but the folder is still empty until you copy the repository files into it.

To turn that empty project into a working copy of this template repository:

1. Download this repository from GitHub as a ZIP file.
2. Unzip it.
3. Open the unzipped repository folder in one file browser window.
4. Open your empty Positron project folder in another file browser window.
5. Copy the repository contents into your empty project folder.

Make sure the project folder now contains at least:

- [`pyproject.toml`](pyproject.toml)
- [`py-intro.qmd`](py-intro.qmd)

If you copied the full repository contents, [`uv.lock`](uv.lock) should also be present already. If not, `uv sync` will create it.

Once those files are present, run `uv sync` in that project folder.

If you already created a `.venv` in the empty folder, that is not a problem.
After copying the repository files in, run `uv sync` again from the project root so that the environment matches [`pyproject.toml`](pyproject.toml).

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

## Step 3: Create the project environment

Before opening the folder in Positron, open a terminal in the project root directory.
This is the folder containing [`README.md`](README.md), [`pyproject.toml`](pyproject.toml), and [`py-intro.qmd`](py-intro.qmd).

Create the project virtual environment and install the Python dependencies:

```bash
uv sync
```

This command creates a local `.venv` directory and installs the dependencies listed in [`pyproject.toml`](pyproject.toml).

## Step 4: Open the project in Positron

After `uv sync` finishes:

1. Start Positron.
2. Choose `File` > `Open Folder...` (or the similar option shown on the welcome screen).
3. Select the project folder.
4. Open the folder.
5. Open [`py-intro.qmd`](py-intro.qmd).

You should now see files such as [`README.md`](README.md), [`pyproject.toml`](pyproject.toml), and [`py-intro.qmd`](py-intro.qmd) in the Positron file browser.

Positron should detect and use the Python interpreter from this project's `.venv`.
If it does not, select it manually.
On macOS and Linux, this is usually `.venv/bin/python`.
On Windows, this is usually `.venv\Scripts\python.exe`.

## Step 5: Work with `py-intro.qmd` in Positron

To work on [`py-intro.qmd`](py-intro.qmd) in Positron:

1. Open [`py-intro.qmd`](py-intro.qmd).
2. Use Positron's `Preview` button to render the document.
3. To run code interactively without rendering the whole document, place the cursor in a code cell or highlight selected lines and run them from the editor.

If Positron's preview does not use the Python interpreter in `.venv`, you can render from the terminal instead.
For example, on macOS or Linux:

```bash
QUARTO_PYTHON=./.venv/bin/python uv run quarto preview py-intro.qmd
```

On Windows PowerShell, use:

```powershell
$env:QUARTO_PYTHON = ".venv\Scripts\python.exe"
uv run quarto preview py-intro.qmd
```

For readers who do not want to install Positron, see the optional Jupyter-based path below.

## Step 6: Create environment variables

> [!NOTE]
> You do not need Steps 6 and 7 for Chapters 1 through 5.
> Most readers can skip both steps until they reach Chapter 6.

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

## Step 7: Get data from WRDS

The template expects local Parquet versions of a small set of WRDS tables.
Those files can be created with [`db2pq`](https://pypi.org/project/db2pq/), which is installed as part of the project environment.

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

## Troubleshooting

If Positron does not appear to use the correct Python interpreter, run the following in Positron's Python console:

```python
import sys
sys.executable
```

You should see a path ending in `.venv/bin/python` on macOS or Linux, or `.venv\Scripts\python.exe` on Windows.

Positron may label the interpreter using the project name from [`pyproject.toml`](pyproject.toml), such as `era-pl-templates`, even when it is correctly using the `.venv` in your own folder.

## Optional: Work with Jupyter Instead of Positron

If you do not want to install Positron, you will also need to install Quarto CLI separately. Install Quarto from <https://quarto.org/docs/get-started/>.

If you prefer to work with a notebook instead of editing the Quarto source directly, run the following command from a terminal in the project root:

```bash
quarto convert py-intro.qmd
```

This command creates `py-intro.ipynb` in the project root.

You can then open the notebook in JupyterLab with:

```bash
uv run jupyter lab py-intro.ipynb
```

## Optional: Using Git

Most readers do not need `git` for this repository.

If you already use Git and prefer to clone the repository instead of downloading a ZIP file, you can do that as well.
