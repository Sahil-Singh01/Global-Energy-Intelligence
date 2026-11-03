# Data Quality Report

## Overview

| Check | Result |
|---|---:|
| Rows | 19,494 |
| Columns | 130 |
| Entity labels | 260 |
| Years | 1700–2025 |
| Missing cells | 1,550,291 |
| Missing-cell rate | 61.17% |
| Exact duplicate rows | 0 |
| Duplicate country–year keys | 0 |

## Findings and implications

### Missingness

Missingness is substantial and not uniform across variables. Use the column- and year-level tables in `outputs/tables/` to select defensible analysis windows. Do not impute missing values as zero by default.

### Entity classification

The dataset contains multiple entity labels, including global and source-specific aggregates. Use the `World` record for global trends when suitable, and separate it from country comparisons. ISO-code presence is a practical screening signal only.

### Latest-year coverage

The latest recorded year should not automatically be treated as complete. Use `records_by_year.csv` and `country_benchmark_coverage_recent.csv` to evaluate coverage by year and indicator.

### Growth-rate extremes

Large annual percentage changes can occur with very small baselines. Inspect levels, periods and variable definitions before deciding whether a value is erroneous.

### Range flags

The range checks in `outputs/tables/data_quality_flags.csv` are screening flags. They are not automatic deletion rules. Percentage-change variables and net-import shares have different valid ranges from source shares.

## Recommended actions

1. Verify the definitions and units of variables used in headline results.
2. Keep aggregate and country-level analysis separate.
3. Report valid samples and explicit time windows.
4. Investigate unusual growth rates against underlying levels.
5. Re-run the notebooks before publication.
