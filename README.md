# Snowflake Data Engineering CI/CD Platform

An end-to-end Data Engineering and DevOps portfolio project demonstrating
automated development, testing, database change management, infrastructure
provisioning, and deployment across DEV, TEST, and PROD environments.

## Project Objective

The objective of this project is to simulate an enterprise Data Engineering
delivery workflow where changes are version-controlled, automatically tested,
and promoted through multiple environments using CI/CD practices.

The project integrates:

- GitHub Actions for CI/CD orchestration
- Snowflake as the cloud data platform
- Schemachange for database change management
- dbt for data transformation and testing
- Terraform for Infrastructure as Code
- AWS services for ingestion and event-driven processing
- Python for utilities, testing, and data processing

## Architecture

```text
Developer
    |
    v
Feature Branch
    |
    v
Pull Request
    |
    +---------------- CI ----------------+
    |                                    |
    |  Python tests                      |
    |  Code quality                      |
    |  SQL validation                    |
    |  dbt validation                    |
    |  Terraform validation / plan       |
    |                                    |
    +----------------+-------------------+
                     |
                  Merge Main
                     |
                     v
              GitHub Actions CD
                     |
          +----------+----------+
          |          |          |
          v          v          v
      Terraform  Schemachange  dbt
          |          |          |
          v          v          v
     Infrastructure  SQL     Data Models
                     |
                     v
               DEV -> TEST -> PROD