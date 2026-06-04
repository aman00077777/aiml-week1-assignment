"""
WeIntern AIML Internship - Week 1
Project Setup Script

Run this file ONCE at the beginning to create the full
folder structure for your Week 1 assignment.

Usage:
    python setup_project.py
"""

import os
import json

# ─────────────────────────────────────────────
# 1. FOLDER STRUCTURE
# ─────────────────────────────────────────────

folders = [
    "data/raw",        # original dataset goes here — never edit this
    "data/cleaned",    # cleaned dataset saved here after Task 1
    "notebooks",       # your .ipynb Jupyter notebooks
    "outputs/charts",  # all saved plots (PNG)
    "outputs/reports", # business insight report (PDF / markdown)
    "src",             # helper Python scripts (optional)
    "screenshots",     # screenshots for README / submission
]

print("=" * 50)
print("  WeIntern AIML Week 1 — Project Setup")
print("=" * 50)

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"  ✓ Created  {folder}/")

print()

# ─────────────────────────────────────────────
# 2. requirements.txt
# ─────────────────────────────────────────────

requirements = """numpy
pandas
matplotlib
seaborn
scikit-learn
jupyter
notebook
ipykernel
"""

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(requirements.strip())

print("  ✓ Created  requirements.txt")

# ─────────────────────────────────────────────
# 3. .gitignore
# ─────────────────────────────────────────────

gitignore = """# Python
__pycache__/
*.py[cod]
*.pyo
.env
venv/
env/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Data (optional — remove if you want to commit data)
# data/raw/
# data/cleaned/

# OS files
.DS_Store
Thumbs.db
"""

with open(".gitignore", "w", encoding="utf-8") as f:
    f.write(gitignore.strip())

print("  ✓ Created  .gitignore")

# ─────────────────────────────────────────────
# 4. README.md (starter template)
# ─────────────────────────────────────────────

readme = """# AIML Internship — Week 1 Assignment

**Organization:** WeIntern Pvt Ltd  
**Intern Name:** Aman Sharma  
**Week:** Week 1 — Data Handling, Cleaning, Visualization & Business Insights

---

## Objective

Analyze a student performance dataset to understand how different features
relate to academic outcomes. Build data cleaning, EDA, visualization, and
business reporting skills.

---

## Dataset

- **Name:** Student Performance Dataset
- **Source:** *(add your Kaggle/UCI link here)*
- **File:** `data/raw/student_performance.csv`
- **Rows:** *(fill after loading)*
- **Columns:** *(fill after loading)*

---

## Libraries Used

| Library     | Purpose                          |
|-------------|----------------------------------|
| NumPy       | Numerical operations             |
| Pandas      | Data loading, cleaning, analysis |
| Matplotlib  | Base plotting & customization    |
| Seaborn     | Statistical visualizations       |

---

## Tasks

### Task 1 — Student Performance Dataset Analysis
- Loaded and inspected the dataset
- Built a feature overview table
- Handled missing values and duplicates
- Standardized categorical labels
- Saved cleaned dataset

### Task 2 — Data Visualization Project
- Score distribution histogram
- Gender / internet access countplot
- Box plot by extra activities
- Study hours vs final score scatter plot
- Correlation heatmap

### Task 3 — Business Insight Report
- 5–7 evidence-based insights
- Actionable recommendations for educators

---

## Key Findings

*(Fill after analysis)*
- Finding 1
- Finding 2
- Finding 3

---

## Folder Structure

```
aiml-week1-assignment/
├── data/
│   ├── raw/               ← original dataset (unchanged)
│   └── cleaned/           ← cleaned dataset
├── notebooks/
│   └── week1_analysis.ipynb
├── outputs/
│   ├── charts/            ← all saved plots
│   └── reports/           ← business insight report
├── src/
│   └── helper_scripts.py  ← optional utility functions
├── screenshots/           ← output screenshots for README
├── setup_project.py       ← run this first!
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/aiml-week1-assignment.git
cd aiml-week1-assignment

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Jupyter
jupyter notebook notebooks/week1_analysis.ipynb
```

---

## Author

**Aman Sharma**  
B.Tech CSE (AI & ML), 3rd Year — G. H. Raisoni College of Engineering, Nagpur  
GitHub: [@aman00077777](https://github.com/aman00077777)
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme.strip())

print("  ✓ Created  README.md")

# ─────────────────────────────────────────────
# 5. Starter notebook config (JSON skeleton)
# ─────────────────────────────────────────────

notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "name": "python",
            "version": "3.10.0"
        }
    },
    "cells": [
        {
            "cell_type": "markdown",
            "id": "title",
            "metadata": {},
            "source": [
                "# WeIntern AIML Internship — Week 1\n",
                "**Student Performance Dataset Analysis**\n\n",
                "**Author:** Aman Sharma  \n",
                "**Date:** 2025  \n",
                "**Tasks:** Data Cleaning | Visualization | Business Insights"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "imports-header",
            "metadata": {},
            "source": ["## 1. Imports & Setup"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "imports",
            "metadata": {},
            "outputs": [],
            "source": [
                "import numpy as np\n",
                "import pandas as pd\n",
                "import matplotlib.pyplot as plt\n",
                "import seaborn as sns\n",
                "\n",
                "# Display settings\n",
                "pd.set_option('display.max_columns', None)\n",
                "sns.set_theme(style='whitegrid')\n",
                "%matplotlib inline\n",
                "\n",
                "print('Libraries loaded successfully!')"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "task1-header",
            "metadata": {},
            "source": ["## 2. Task 1 — Data Loading & Cleaning\n*(Add your cleaning code here)*"]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "id": "load",
            "metadata": {},
            "outputs": [],
            "source": [
                "df = pd.read_csv('../data/raw/student_performance.csv')\n",
                "print(f'Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns')\n",
                "df.head()"
            ]
        },
        {
            "cell_type": "markdown",
            "id": "task2-header",
            "metadata": {},
            "source": ["## 3. Task 2 — Visualizations\n*(Add your charts here)*"]
        },
        {
            "cell_type": "markdown",
            "id": "task3-header",
            "metadata": {},
            "source": ["## 4. Task 3 — Business Insights\n*(Add your report here)*"]
        }
    ]
}

notebook_path = "notebooks/week1_analysis.ipynb"
with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print(f"  ✓ Created  {notebook_path}")

# ─────────────────────────────────────────────
# 6. helper_scripts.py stub
# ─────────────────────────────────────────────

helper = '''"""
src/helper_scripts.py
Reusable utility functions for Week 1 analysis.
Import in notebook: from src.helper_scripts import save_chart
"""

import os
import matplotlib.pyplot as plt


def save_chart(filename: str, folder: str = "outputs/charts", dpi: int = 150):
    """Save the current matplotlib figure to the charts folder."""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    plt.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Chart saved → {path}")


def missing_value_report(df):
    """Print a clean missing value summary table."""
    import pandas as pd
    missing = df.isnull().sum()
    pct = (missing / len(df) * 100).round(2)
    report = pd.DataFrame({
        "Missing Count": missing,
        "Missing %": pct
    })
    report = report[report["Missing Count"] > 0].sort_values("Missing %", ascending=False)
    if report.empty:
        print("No missing values found!")
    else:
        print(report)
    return report
'''

with open("src/helper_scripts.py", "w", encoding="utf-8") as f:
    f.write(helper.strip())

print("  ✓ Created  src/helper_scripts.py")

# ─────────────────────────────────────────────
# DONE
# ─────────────────────────────────────────────

print()
print("=" * 50)
print("  Setup complete! Your project is ready.")
print("=" * 50)
print()
print("  Next steps:")
print("  1. Download a student dataset from Kaggle")
print("     → Save as: data/raw/student_performance.csv")
print()
print("  2. Install dependencies:")
print("     pip install -r requirements.txt")
print()
print("  3. Open the notebook:")
print("     jupyter notebook notebooks/week1_analysis.ipynb")
print()