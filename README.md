# Support page for *Empirical Research in Accounting: Tools and Methods*

This page provides support to readers of the (work-in-progress) [Python Polars edition of *Empirical Research in Accounting: Tools and Methods*](https://iangow.github.io/era_pl_book/).
(For support for the [R edition](https://iangow.github.io/far_book/) of the book, please go [here](https://github.com/iangow/far_templates))

This repository contains Quarto templates that readers of *Empirical Research in Accounting* can easily render into PDF documents.
Each template is a slimmed-down, self-contained version of a book chapter with the focus on code that readers can run locally and exercises that readers can answer and submit.

## Templates

### Part I: Foundations

| Chapter | Template |
|---------|----------|
| The basics of data analysis | [py-intro.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/py-intro.qmd) |
| Regression fundamentals | [reg-basics.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/reg-basics.qmd) |
| Causal inference | [causal-inf.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/causal-inf.qmd) |
| Statistical inference | [stat-inf.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/stat-inf.qmd) |
| Financial statements: A first look | [fin-state.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/fin-state.qmd) |
| Linking databases | [identifiers.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/identifiers.qmd) |
| Financial statements: A second look | [fin-state-reprise.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/fin-state-reprise.qmd) |
| Importing data | [web-data.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/web-data.qmd) |

### Part II: Capital Markets Research

| Chapter | Template |
|---------|----------|
| FFJR | [ffjr.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/ffjr.qmd) |
| Ball and Brown (1968) | [bb68.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/bb68.qmd) |
| Beaver (1968) | [beaver68.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/beaver68.qmd) |
| Event studies | [event-studies.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/event-studies.qmd) |
| Post-earnings announcement drift | [pead.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/pead.qmd) |
| Accruals | [accruals.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/accruals.qmd) |
| Earnings management | [earnings-mgt.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/earnings-mgt.qmd) |

### Part III: Causal Inference

| Chapter | Template |
|---------|----------|
| Natural experiments | [natural.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/natural.qmd) |
| Causal mechanisms | [mechanisms.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/mechanisms.qmd) |
| Natural experiments revisited | [natural-revisited.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/natural-revisited.qmd) |
| Instrumental variables | [iv.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/iv.qmd) |
| Panel data | [panel-data.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/panel-data.qmd) |
| Regression discontinuity designs | [rdd.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/rdd.qmd) |

### Part IV: Additional Topics

| Chapter | Template |
|---------|----------|
| Beyond OLS | [glms.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/glms.qmd) |
| Extreme values and sensitivity analysis | [extreme-vals.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/extreme-vals.qmd) |
| Matching | [psm.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/psm.qmd) |
| Prediction | [prediction.qmd](https://raw.githubusercontent.com/iangow/era_pl_templates/main/prediction.qmd) |

## Set-up instructions

At a high level, the required set-up encompasses the following:

1. Installing Python and the third-party packages used in the book.
   Here I emphasize [`uv`](https://docs.astral.sh/uv/), "an extremely fast Python package and project manager" for its ease of use and speed.
2. Installing an integrated development environment (IDE) to edit, interact with, and render code.
   Here I lead with Positron, but suggest alternatives at the end of the document.
3. Downloading WRDS data.
   This is covered in Steps 6 and 7 below.
   **You only need WRDS data starting from Chapter 6** of the book, so you could pause at Step 5 below and still cover Chapters 1--5 of the book (and also Chapters 17 and 18).
   Note that you will need a WRDS ID to get the data from WRDS.

### Step 1: Download the project

1. If you're not already on the GitHub page for this repository, open the repository page on GitHub.
2. Click the `Code` button that looks like this: ![`Code` button](images/github-code-button.svg).
   This button should be somewhere toward the top-right part of this page.
3. Click `Download ZIP`.
4. Find the downloaded ZIP file on your computer.
5. Unzip the downloaded archive.

After unzipping, you should have a folder named something like `era_pl_templates-main`.

You may rename this folder to something more meaningful for your own work, such as `era_homework`.
You may also move the folder to any convenient location on your computer before opening it in Positron.

### Step 2: Install the prerequisites

Install the following tools before working with the template:

1. `uv`
2. Positron

#### Install `uv`

On macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

See the official installation instructions at <https://docs.astral.sh/uv/>.

#### Install Positron

Download Positron from <https://positron.posit.co/download.html> and install it using the normal steps for your operating system.

### Step 3: Create the project environment

Before opening the folder in Positron, open a terminal in the project root directory.
This is the folder containing [`README.md`](README.md), [`pyproject.toml`](pyproject.toml), and [`py-intro.qmd`](py-intro.qmd).

Create the project virtual environment and install the Python dependencies:

```bash
uv sync
```

This command creates a local `.venv` directory and installs the third-party Python packages listed in [`pyproject.toml`](pyproject.toml).
We may update [`pyproject.toml`](pyproject.toml) after you download this repository to reflect changes to the required packages over time.
If so, you can simply copy-paste the updated contents of [`pyproject.toml`](pyproject.toml) into your local copy and then run `uv sync` (as above) to update your local environment.

### Step 4: Open the project in Positron

After `uv sync` finishes:

1. Start Positron.
2. Choose `File` > `Open Folder...` (or the similar option shown on the welcome screen).
3. Select the project folder.
4. Open the folder.
5. Open [`py-intro.qmd`](py-intro.qmd).

You should now see files such as [`README.md`](README.md), [`pyproject.toml`](pyproject.toml), and [`py-intro.qmd`](py-intro.qmd) in the Positron file browser.

Positron should detect and use the Python interpreter from this project's `.venv`.
If it does not, see [Troubleshooting](#troubleshooting).

### Step 5: Work with `py-intro.qmd` in Positron

To work on [`py-intro.qmd`](py-intro.qmd) in Positron, complete the previous step to open `py-intro.qmd` in Positron.
[`py-intro.qmd`](py-intro.qmd) includes detailed instructions for working through this step.

You can run code interactively without rendering the whole document, place the cursor in a code cell or highlight selected lines and run them from the editor.
Note that the code generally assumes that it has been run in order from the cells at the top.
You can use `Run Above` to run cells prior to a given cell, then `Run Cell` to run that cell.

You can also use Positron's `Preview` button to render the document into a PDF.

### Step 6: Create environment variables

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

### Step 7: Get data from WRDS

The code in the book and the templates expect local Parquet versions of a small set of WRDS tables.
Those files can be created with [`db2pq`](https://iangow.github.io/db2pq/), which is installed as part of the project environment.

> [!NOTE]
> The time to download the data will depend a great deal on the speed of your internet connection and your "distance" from the WRDS server.
> On a fast connection in the northeastern United States, the script can take as little as ten minutes to run.
> From the other side of the world (e.g., New Zealand) with modest internet and older hardware, the script might take a couple of hours.
> So this is probably something you want to do when you have a fast connection (e.g., a wired internet connection at a university).

After creating `.env`, run the following command from a terminal in the project root:

```bash
uv run python
```

If you already use either `db2pq` or `wrds2pg`, you may already have `DATA_DIR` set in your shell environment.
If you want this repository to use a different `DATA_DIR` from `.env`, run `unset DATA_DIR` before launching Python or running the helper script below.
If you existing `DATA_DIR` contains data for the R version of this book, you could simply use those data files (the script below will update them to the current data on WRDS, if necessary).

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

### Troubleshooting

If Positron does not appear to use the correct Python interpreter, run the following in Positron's Python console:

```python
import sys
sys.executable
```

You should see a path ending in `.venv/bin/python` on macOS or Linux, or `.venv\Scripts\python.exe` on Windows.

Positron may label the interpreter using the project name from [`pyproject.toml`](pyproject.toml), such as `era-pl-templates`, even when it is correctly using the `.venv` in your own folder.

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

If you had already created an empty project in Positron prior to using these instructions, you can copy the contents of this repository into that project folder, then run `uv sync` from the project root.

If you already created a `.venv` in the empty folder, that is not a problem.
After copying the repository files in, run `uv sync` again from the project root so that the environment matches [`pyproject.toml`](pyproject.toml).

### Optional: Work with Jupyter instead of Positron

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

### Optional: Using Git

Most readers do not need `git` for this repository.
But if you already use Git you might choose to clone the repository instead of downloading a ZIP file.
