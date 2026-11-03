"""Reusable data-quality checks for the Global Energy Intelligence project."""
from __future__ import annotations
import pandas as pd

def audit_overview(data: pd.DataFrame) -> pd.DataFrame:
    """Return a concise integrity and coverage summary without modifying data."""
    required = {"country", "year"}
    missing = required.difference(data.columns)
    if missing:
        raise ValueError(f"Required identifier columns are missing: {sorted(missing)}")
    return pd.DataFrame([
        {"measure": "rows", "value": len(data)},
        {"measure": "columns", "value": data.shape[1]},
        {"measure": "distinct_entities", "value": data["country"].nunique(dropna=True)},
        {"measure": "exact_duplicate_rows", "value": int(data.duplicated().sum())},
        {"measure": "duplicate_entity_year_keys", "value": int(data.duplicated(["country", "year"]).sum())},
        {"measure": "missing_cells", "value": int(data.isna().sum().sum())},
        {"measure": "missing_cell_pct", "value": round(float(data.isna().mean().mean() * 100), 2)},
    ])

def missingness_by_column(data: pd.DataFrame) -> pd.DataFrame:
    """Return missing counts and rates for each column."""
    return pd.DataFrame({
        "column": data.columns,
        "missing_count": data.isna().sum().values,
        "missing_pct": (data.isna().mean().values * 100).round(2),
    }).sort_values("missing_pct", ascending=False)
