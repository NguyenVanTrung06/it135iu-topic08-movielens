# IT135IU – Topic 8: Which films should a streaming service promote to a given audience?

Course project for **IT135IU – Introduction to Data Science** (VNU-HCM International University).
Dataset: **MovieLens 1M** (GroupLens Research). Group: _[group name]_.

> Status: skeleton for D2. Sections marked _TODO_ are filled in as the notebook is finalised.

## Repository layout

    notebooks/    analysis notebooks (D2 data profile + cleaning log, later D3)
    tools/        small helper scripts for reproducibility (see below)
    data/         empty on purpose – data is NOT stored in this repository
    requirements.txt   exact package versions taken from the environment that ran the notebook

## Data (not included)

The MovieLens 1M files are not committed: the GroupLens terms of use do not allow
redistribution. Download them from <https://grouplens.org/datasets/movielens/1m/> and place
`ratings.dat`, `movies.dat`, `users.dat` in `data/ml-1m/`. _TODO: confirm with the notebook whether
it downloads the files itself or expects them locally, and fix this paragraph._

Citation required by the terms: F. M. Harper and J. A. Konstan, "The MovieLens Datasets: History
and Context", ACM TiiS 5(4), 2015.

## How to reproduce

1. Use Python _TODO: version from `requirements.txt` header_ (the notebook was run on Google Colab).
2. `pip install -r requirements.txt`
3. Put the data files in `data/ml-1m/` (see above).
4. Open the notebook in `notebooks/` and choose **Restart and run all**.

All randomness is seeded with **42** (_TODO: list the places once confirmed with `tools/check_seed.py`_),
so two runs give the same numbers.

## Helper scripts

| Script | Purpose |
|---|---|
| `tools/freeze_from_notebook.py` | writes `requirements.txt` + `env_report.txt` from the real environment |
| `tools/clean_notebook.py` | removes personal metadata (Colab `executionInfo`) before committing |
| `tools/check_seed.py` | lists every line using randomness and whether a seed is visible |
| `tools/compare_runs.py` | compares text outputs of two executed runs |

## Responsible use

- Source and terms of use: see "Data" above.
- AI assistance: _TODO – state which parts (e.g. README draft) were AI-assisted and reviewed by the team._
- Known data limitation: _TODO – e.g. ratings are from 2000–2003, 1–5 integer scale, only users with ≥ 20 ratings._
