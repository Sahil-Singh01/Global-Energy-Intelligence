"""Consistent plotting helpers for notebooks and scripts."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

def set_project_style():
    """Apply a restrained, readable chart style."""
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update({
        "figure.figsize": (10, 5.5),
        "axes.titleweight": "bold",
        "axes.labelsize": 10,
        "savefig.dpi": 160,
        "figure.autolayout": True,
    })

def save_figure(fig, output_path):
    """Create parent folders and save a figure with tight bounds."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, bbox_inches="tight", dpi=160)
    return output_path
