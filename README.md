# Secure Azure Databricks Lakehouse

An end-to-end retail analytics portfolio project that demonstrates how to move operational retail data into a governed, analytics-ready lakehouse.

## Business problem
Retail teams need reliable sales and customer data for reporting. Source data is distributed across operational systems, can contain quality issues, and includes sensitive customer information.

## Proposed solution
This project models a secure data platform:

```text
PostgreSQL source -> Azure Data Lake / Bronze -> Databricks Silver -> Databricks Gold -> Power BI
```

## Current progress
- [x] Created reproducible GitHub Codespaces development environment
- [x] Created Docker PostgreSQL operational source database
- [x] Generated synthetic retail customers, products, and orders
- [x] Loaded source data and completed baseline SQL analysis
- [ ] Build Bronze ingestion layer
- [ ] Build Silver transformations and quality controls
- [ ] Build Gold dimensional model
- [ ] Add governance and security controls
- [ ] Publish dashboard and demo

## Technology stack
- Python
- PostgreSQL
- Docker Compose
- GitHub Codespaces
- SQL
- Azure Databricks and Delta Lake, planned
- Power BI, planned

## Data
The project uses synthetic retail data generated locally by `scripts/generate_data.py`. No client, employer, or personal data is used.

## Repository structure
- `scripts/`: source-data generator and database load scripts
- `sql/`: schema and analysis SQL
- `docs/`: architecture, data dictionary, and design decisions
- `notebooks/`: future Databricks notebooks
- `tests/`: future data-quality tests

## How to run
1. Create a GitHub Codespace from this repository.
2. Rebuild the container if prompted.
3. Run `python scripts/generate_data.py`.
4. Run the schema script using PostgreSQL.
5. Run `python scripts/load_postgres.py`.
6. Run `sql/03_baseline_analysis.sql`.

## Author
[Amol] — [LinkedIn](www.linkedin.com/in/amol-chourasia)
