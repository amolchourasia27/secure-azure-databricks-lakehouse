# Architecture

## Current development architecture

```text
Synthetic Data Generator
        |
        v
CSV files in Codespaces
        |
        v
PostgreSQL in Docker Compose
        |
        v
Baseline SQL Analysis
```

## Target architecture

```text
PostgreSQL operational source
        |
        v
Azure Data Lake Storage: Bronze
        |
        v
Azure Databricks: Silver Delta tables
        |
        v
Azure Databricks: Gold dimensional model
        |
        +--> Unity Catalog, access control, lineage, auditability
        |
        v
Power BI dashboard
```

## Security design principles
- Use synthetic data only in the public portfolio.
- Store credentials in environment variables or Codespaces secrets.
- Apply least-privilege access by role.
- Separate raw, cleaned, and curated data layers.
- Identify and restrict access to PII fields.