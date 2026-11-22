# IT135IU – Topic 8: Which films should a streaming service promote to a given audience?

Course project for **IT135IU – Introduction to Data Science** (VNU-HCM International University).

- **Dataset:** MovieLens 1M (GroupLens Research)
- **Group:** Group 3, Topic 08

## Repository layout

```text
.
├── data/                          # location for a manually downloaded archive if needed
├── notebooks/
│   └── D3_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb   # main analysis notebook (D3 – Analysis)
├── tools/                         # small helper scripts for reproducibility
│   ├── freeze_from_notebook.py
│   ├── clean_notebook.py
│   ├── check_seed.py
│   └── compare_runs.py
├── .gitignore                     # blocks data files (*.dat, *.csv, *.parquet)
├── requirements.txt               # exact package versions from the environment that ran the notebook
└── README.md
```

## Data (not included)

The MovieLens 1M data files are **not committed** to this repository (they are blocked by `.gitignore`). The notebook automatically downloads and extracts the dataset from GroupLens into temporary storage:

`https://files.grouplens.org/datasets/movielens/ml-1m.zip`

An active internet connection is required for automatic download.

### If data download fails

Download [`ml-1m.zip`](https://grouplens.org/datasets/movielens/1m/) manually and place it in the repository's `data/` directory.

**Why is the data not in the repo?** The dataset belongs to GroupLens, and its terms of use do not allow redistribution. Keeping it out also keeps the repository small. Users can obtain the same files from the official source.

**Citation required by the terms:** F. M. Harper and J. A. Konstan, “The MovieLens Datasets: History and Context,” *ACM Transactions on Interactive Intelligent Systems* 5(4), 2015.

## How to reproduce

1. Use **Python 3.13.18**.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open `D3_Topic08_Phuong_LeQuan_Que_HoangQuan_Tuyen_Trung_Cuong.ipynb` and choose **Restart and run all**. The dataset is downloaded automatically.

All randomness is seeded with **`SEED = 42`** at Step 1 to support reproducible results.

## Helper scripts

| Script | Purpose |
|---|---|
| `tools/freeze_from_notebook.py` | Writes `requirements.txt` and `env_report.txt` from the real environment |
| `tools/clean_notebook.py` | Removes personal metadata (Colab `executionInfo`) before committing |
| `tools/check_seed.py` | Lists lines that use randomness and whether a seed is visible |
| `tools/compare_runs.py` | Compares the text outputs of two executed runs |

## Responsible use

- **Source and terms of use:** See “Data (not included)” above.
- **AI assistance:** AI tools (ChatGPT, Gemini, Claude) were used to draft the repository skeleton (README and tool scripts), assist with Git/GitHub commands, and explain specific pandas and Python functions. The project team reviewed and verified all AI-generated output and analysis.
- **Known data limitations:**
  - *Time period:* Ratings were collected from 2000 to 2003 and may not reflect modern streaming audiences.
  - *Rating scale:* Ratings are discrete integers from 1 to 5, with no half-stars.
  - *Selection bias:* Only users with at least 20 ratings are included. Demographic fields (age, gender, occupation) are self-reported and grouped into categories.
