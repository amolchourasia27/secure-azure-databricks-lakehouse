# Architecture Decision Log

## ADR-001: Use PostgreSQL as the operational source system

**Status:** Accepted  
**Date:** 2026-07-15

### Context
The project needs a relational source system to simulate operational retail data before ingestion into a lakehouse.

### Decision
Use PostgreSQL running in Docker Compose inside GitHub Codespaces.

### Why
- Relational tables and SQL reflect common source-system patterns.
- Docker Compose makes the setup reproducible.
- Codespaces keeps development, code, documentation, and version control in one cloud environment.
- The database is isolated and uses only synthetic/public data.

### Trade-off
This is a development environment, not a production database. Azure Databricks and Azure storage will be introduced later for the lakehouse processing layer.