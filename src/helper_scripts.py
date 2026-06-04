"""
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