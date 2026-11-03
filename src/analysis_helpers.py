"""Small, explicit helpers for analytical calculations."""
from __future__ import annotations
import numpy as np
import pandas as pd

def safe_percent_change(start, end):
    """Return percent change only when the baseline is non-zero and inputs are finite."""
    try:
        start, end = float(start), float(end)
    except (TypeError, ValueError):
        return np.nan
    if not np.isfinite(start) or not np.isfinite(end) or start == 0:
        return np.nan
    return (end / start - 1) * 100

def classify_entity_label(label, iso_code):
    """Use ISO-code presence as a country-candidate signal, not definitive sovereignty."""
    if pd.isna(label):
        return "Missing label"
    if label == "World":
        return "Global aggregate"
    if pd.notna(iso_code):
        return "Country candidate (ISO present)"
    return "Aggregate / non-ISO entity; review label"
