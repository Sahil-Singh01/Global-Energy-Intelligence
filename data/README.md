# Dataset documentation

## Source

This project uses the Our World in Data (OWID) Energy dataset, stored locally as `owid_energy.csv`.

- [Dataset catalog, codebook, sources and documentation](https://catalog.ourworldindata.org/energy/owid_energy/)
- [OWID energy-data repository](https://github.com/owid/energy-data)
- [OWID guidance on data reuse and attribution](https://ourworldindata.org/faqs#how-should-i-cite-your-data)

The supplied snapshot contains **19,494 rows and 130 columns**, covering entity-year observations from 1700 through 2025. It is the version analyzed in this project, not a promise that the file is the latest release.

## What the dataset contains

The wide country-year table combines energy supply and energy mix indicators, electricity generation and demand, trade, emissions and carbon intensity, fossil-fuel production, population, and GDP. It includes countries as well as regional and global aggregates.

## Licensing and attribution

OWID explains that its dataset combines information from multiple original providers and that the original source licenses continue to apply. Therefore, do not assume the entire CSV has one blanket license. Before redistributing the file or reusing individual indicators, check the relevant source-level terms in the dataset documentation and sources file.

When citing the dataset, credit Our World in Data and the underlying data providers relevant to the indicators used. See the OWID catalog for the dataset's suggested citation and detailed source metadata.

## Reproducibility

The notebooks read this file from `data/owid_energy.csv`. To reproduce the analysis with a different release, download the dataset from the OWID catalog, record the retrieval date and release/version, and rerun all notebooks. Results may change when source data, definitions, or primary-energy methodology are updated.
