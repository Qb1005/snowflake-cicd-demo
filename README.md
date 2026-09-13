# Snowflake Data Engineering CI/CD Platform

An end-to-end Data Engineering and DevOps portfolio project exploring automated development, testing, database change management, infrastructure provisioning, and deployment across DEV, TEST, and PROD environments.

## Project Objective

The objective of this project is to simulate an enterprise Data Engineering delivery workflow where changes are version-controlled, automatically tested, and promoted through multiple environments using CI/CD practices.

The project scope brings together:

- **GitHub Actions** for CI/CD orchestration.
- **Snowflake** as the cloud data platform.
- **Schemachange** for database change management.
- **dbt** for data transformation, testing, and documentation.
- **Terraform** for Infrastructure as Code.
- **AWS services** for ingestion and event-driven processing.
- **Python** for utilities, testing, and data processing.

The architecture and roadmap describe the platform’s intended scope. Implementation progress and verification evidence are maintained in GitHub Projects and Issues.

## Architecture

### Delivery Workflow

```text
Developer
    |
    v
Feature Branch
    |
    v
Pull Request
    |
    v
+---------------------------------------+
|              CI Validation            |
|                                       |
|  Python unit tests                    |
|  Python code quality                  |
|  Snowflake SQL linting                |
|  dbt build and data tests              |
|  Terraform validation / plan          |
+-------------------+-------------------+
                    |
                    v
          Required Checks and Review
                    |
                    v
               Merge to main
                    |
                    v
             GitHub Actions CD
                    |
          +---------+----------+
          |         |          |
          v         v          v
      Terraform  Schemachange  dbt
          |         |          |
          v         v          v
   Infrastructure  Database   Analytical
   and Access      Migrations Models
```

Deployment dependencies determine execution order. Infrastructure and database objects must be available before dependent migrations or transformations run.

### Environment Promotion

```text
Reviewed Release Revision
          |
          v
         DEV
          |
      Validation
          |
          v
         TEST
          |
   Integration Checks
          |
          v
       Approval
          |
          v
         PROD
          |
 Post-deployment Checks
```

The same reviewed revision is promoted between environments. Environment-specific configuration supplies the target database, schema, role, and credentials.

### Data Flow

```text
Sample Files / Source Data
          |
          v
AWS Ingestion or Local Simulation
          |
          v
Snowflake Source Tables
          |
          v
dbt Staging Models
          |
          v
Analytical Marts
          |
          v
Validation and Analytical Queries
```

## Technology Responsibilities

| Technology | Responsibility |
|---|---|
| GitHub Actions | Coordinate validation, deployment, and approval workflows |
| Snowflake | Store and process data across environments |
| Python | Implement utilities, connection checks, and processing logic |
| pytest | Test Python behavior |
| Ruff | Check Python code quality |
| SQLFluff | Lint SQL using the Snowflake dialect |
| Schemachange | Apply database migrations and record change history |
| dbt / dbt Cloud | Build, test, document, and orchestrate transformations |
| Terraform | Manage selected infrastructure and configuration |
| AWS | Provide storage, ingestion, processing, and monitoring services |

### Resource Ownership

Each managed object should have one clear owner.

- **Terraform:** Infrastructure, access configuration, and explicitly assigned platform resources.
- **Schemachange:** Database objects and schema changes assigned to migration management.
- **dbt:** Transformation models and their associated tests and documentation.

Ownership boundaries prevent multiple tools from managing the same object.

## Engineering Principles

- Develop changes through feature branches and pull requests.
- Run automated validation before deployment.
- Promote the same reviewed revision across environments.
- Separate environment configuration from application logic.
- Apply environment-appropriate permissions.
- Keep credentials outside version control.
- Record deployment history and verification evidence.
- Test failure and recovery behavior.
- Distinguish executed implementations from simulations and design exercises.

## Local Development

Run the following commands from the repository root with the project’s Python environment activated.

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Quality Checks

```bash
ruff check .
python -m pytest
sqlfluff lint sql/ --dialect snowflake
```

SQL validation should cover additional SQL directories as they are introduced.

Linting does not execute SQL in Snowflake. Successful linting does not guarantee that SQL has the required privileges, executes successfully, or produces the intended business result.

Live connection, migration, and integration checks require separate environment configuration.

## Environment Configuration

The lab uses the following environment naming convention:

| Environment | Database | Application Schema | Deployment Role |
|---|---|---|---|
| DEV | `DEV_DB` | `APP` | `CICD_DEV_ROLE` |
| TEST | `TEST_DB` | `APP` | `CICD_TEST_ROLE` |
| PROD | `PROD_DB` | `APP` | `CICD_PROD_ROLE` |

Connection configuration includes:

- Snowflake account and service identity.
- Authentication settings for the selected method.
- Warehouse.
- Database and schema.
- Deployment role.
- Environment-specific migration history location.

Use GitHub Secrets for sensitive workflow values and environment variables or GitHub environment variables for appropriate configuration.

Do not commit passwords, private keys, local credential files, or generated caches.

## Project Roadmap

The roadmap organizes the platform into 11 phases. Expand a phase to view its objective, implementation scope, and expected evidence.

[Open Project Board](https://github.com/users/Qb1005/projects/1) · [Browse Issues](https://github.com/Qb1005/snowflake-cicd-demo/issues) · [Browse Pull Requests](https://github.com/Qb1005/snowflake-cicd-demo/pulls) · [View Workflow Runs](https://github.com/Qb1005/snowflake-cicd-demo/actions)

<details>
<summary><strong>Phase 1 — GitHub CI Foundation</strong></summary>

### Objective

Establish a repeatable development workflow that validates Python and SQL changes before merging.

### Implementation Scope

- Prepare the repository and local Python environment.
- Record dependencies and exclude generated files.
- Implement meaningful Python unit tests.
- Run Ruff, pytest, and SQLFluff as parallel CI jobs.
- Configure required checks and the intended PR rules.
- Demonstrate failed checks, fixes, branch updates, and reviewed merges.

### Expected Evidence

- Reproducible local setup instructions.
- Passing and deliberately failing CI runs.
- A PR demonstrating the required-check workflow.

</details>

<details>
<summary><strong>Phase 2 — Snowflake Roles and Environments</strong></summary>

### Objective

Separate DEV, TEST, and PROD access and verify that deployment sessions use the intended context.

### Implementation Scope

- Create environment databases and application schemas.
- Configure warehouse access and deployment roles.
- Grant privileges required by the lab exercises.
- Configure GitHub environment secrets and variables.
- Verify the active user, role, database, schema, and warehouse.
- Test permitted operations and denied cross-environment access.
- Document role separation and service identity limitations.

### Expected Evidence

- Environment and access matrices.
- Successful connection checks for each environment.
- Positive and negative permission tests.

</details>

<details>
<summary><strong>Phase 3 — Schemachange Migrations</strong></summary>

### Objective

Introduce tracked database changes through migration files and deployment history.

### Implementation Scope

- Install and configure Schemachange.
- Define migration naming and directory conventions.
- Configure environment-specific change history.
- Deploy the first versioned migration.
- Verify rerun behavior and add a second version.
- Test repeatable migrations and explain always scripts.
- Add migration validation and automated DEV deployment.

### Expected Evidence

- Versioned and repeatable migration files.
- Resulting Snowflake objects.
- Change-history records and rerun results.
- Successful GitHub Actions deployment.

</details>

<details>
<summary><strong>Phase 4 — DEV → TEST → PROD Promotion</strong></summary>

### Objective

Promote the same reviewed revision through validation and approval gates.

### Implementation Scope

- Define release identity and environment configuration.
- Maintain separate migration history per environment.
- Deploy to DEV and run smoke checks.
- Promote to TEST and run integration checks.
- Add an available approval mechanism before PROD.
- Verify post-deployment results.
- Prevent overlapping deployments to the same target.
- Demonstrate that failed validation stops promotion.

### Expected Evidence

- One revision promoted across environments.
- Approval and deployment records.
- History comparison and blocked-promotion tests.

</details>

<details>
<summary><strong>Phase 5 — dbt Transformation Layer</strong></summary>

### Objective

Transform reproducible sample data into tested analytical models.

### Implementation Scope

- Define sample datasets, keys, and data grain.
- Load source data into Snowflake.
- Initialize the dbt project and source definitions.
- Build staging models and analytical marts.
- Document business logic and model dependencies.
- Add uniqueness, null, relationship, and business-rule tests.
- Generate and review model documentation.

### Expected Evidence

- Successful model builds.
- Verified analytical results.
- Meaningful data-test failures and fixes.
- Model documentation and lineage.

</details>

<details>
<summary><strong>Phase 6 — dbt CI/CD and dbt Cloud</strong></summary>

### Objective

Validate transformation changes before release and automate their deployment.

### Implementation Scope

- Run PR builds in an isolated development context.
- Configure source access and temporary-object cleanup.
- Coordinate migrations and transformation deployment.
- Capture build logs and test artifacts.
- Configure dbt Cloud projects, environments, and jobs where available.
- Document the equivalent design when using dbt Core.
- Practice diagnosing transformation and data-test failures.

### Expected Evidence

- Passing and failing PR builds.
- Automated transformation deployment.
- An executed dbt Cloud job or an explicitly labeled design-only mapping.

</details>

<details>
<summary><strong>Phase 7 — Terraform Infrastructure</strong></summary>

### Objective

Manage selected infrastructure through reviewed configuration and controlled changes.

### Implementation Scope

- Define resource ownership and bootstrap requirements.
- Identify existing resources to import or exclude.
- Configure providers, variables, and outputs.
- Plan state storage and access.
- Run formatting, validation, and planning.
- Apply and verify a controlled lab change.
- Integrate checks and approved apply into GitHub Actions.
- Document drift handling, cleanup, and cost considerations.

### Expected Evidence

- Terraform configuration and reviewed plans.
- Verified resources after apply.
- State and ownership documentation.
- CI and controlled deployment results.

</details>

<details>
<summary><strong>Phase 8 — AWS Ingestion</strong></summary>

### Objective

Build a traceable file-ingestion path into Snowflake.

### Implementation Scope

- Define file formats, schemas, and batch identifiers.
- Specify invalid-file and duplicate handling.
- Provision suitable AWS resources or build a local simulation.
- Implement input validation and loading.
- Record batch outcomes and processing logs.
- Verify row counts and sample values.
- Test retries, invalid input, and duplicate delivery.
- Document setup and teardown.

### Expected Evidence

- Reproducible end-to-end ingestion.
- Verified destination data.
- Duplicate and recovery test results.
- Clear identification of real AWS execution or simulation.

</details>

<details>
<summary><strong>Phase 9 — Advanced Authentication</strong></summary>

### Objective

Improve service authentication and environment identity separation.

### Implementation Scope

- Inventory service identities and credential storage.
- Evaluate authentication support across the selected tools.
- Implement supported Snowflake service authentication.
- Configure GitHub-to-AWS federation where available.
- Restrict access to intended repositories and deployment contexts.
- Separate environment identities where practical.
- Test authorized and unauthorized access.
- Retire obsolete credentials after replacement verification.
- Document rotation and revocation procedures.

### Expected Evidence

- Authentication and trust configuration.
- Successful authorized access and denied unauthorized access.
- Updated identity matrix and credential lifecycle documentation.

Credential hygiene applies throughout the project; this phase introduces advanced controls.

</details>

<details>
<summary><strong>Phase 10 — Production Engineering and Recovery</strong></summary>

### Objective

Make pipeline failures observable, understandable, and recoverable.

### Implementation Scope

- Record release revision, target environment, and workflow identity.
- Summarize deployment results and configure failure reporting.
- Practice migration failure recovery.
- Inspect partial execution and determine corrective actions.
- Define deployment concurrency, retry, and timeout behavior.
- Review destructive changes and approval requirements.
- Write runbooks for authentication, migration, transformation, and ingestion failures.
- Rehearse a complete recovery scenario.

### Expected Evidence

- Deployment summaries and useful failure logs.
- Controlled failure and recovery demonstrations.
- Tested operational runbooks.

</details>

<details>
<summary><strong>Phase 11 — Portfolio Documentation and Interview Demo</strong></summary>

### Objective

Present the platform through accurate documentation and verifiable demonstrations.

### Implementation Scope

- Maintain the README and architecture documentation.
- Link roadmap issues to implementation evidence.
- Verify setup instructions from a clean environment.
- Document configuration, teardown, and known limitations.
- Prepare a demonstration of validation, deployment, and recovery.
- Explain tool choices, ownership boundaries, and tradeoffs.
- Check that project claims match executed work.
- Prepare a documented portfolio release.

### Expected Evidence

- Reproducible instructions.
- Architecture documentation.
- Linked PRs and workflow runs.
- A concise demonstration script and release milestone.

Documentation is maintained throughout the project; this phase provides the final portfolio review.

</details>

## Work Tracking

GitHub Projects provides the board, while repository Issues contain the detailed implementation steps and evidence.

```text
Phase Parent Issue
    |
    +── Implementation Sub-issue
    |       |
    |       +── Task Checklist
    |       +── Pull Request / Workflow Evidence
    |       +── Learning Notes
    |
    +── Implementation Sub-issue
```

### Board Workflow

| Status | Meaning |
|---|---|
| Backlog | Planned work |
| Ready | Prerequisites are complete |
| In Progress | Implementation or study is underway |
| Review | Ready for verification and learning review |
| Done | Verified, documented, and closed as completed |

### Definition of Done

A sub-issue is complete when:

- Its objective and acceptance criteria are satisfied.
- Relevant behavior has been verified.
- Implementation and verification evidence are recorded.
- Failures, fixes, and limitations are documented.
- The result can be explained independently.

A phase is complete when its required sub-issues and parent acceptance criteria are satisfied.

## Evidence and Learning Review

Evidence may include:

- Pull requests and reviewed changes.
- Passing and intentionally failing workflow runs.
- Non-sensitive Snowflake verification results.
- Migration-history records.
- dbt build and test results.
- Terraform plans and resource verification.
- Ingestion and recovery results.

Each learning review should answer:

1. What was implemented?
2. Why is it needed?
3. How was it verified?
4. What failed, and how was it fixed?
5. What limitations or follow-up tasks remain?

## Scope and Limitations

This repository is a portfolio lab that simulates enterprise delivery practices.

Cloud-dependent exercises use available services and account capabilities. Where access is unavailable, local simulations or design-only alternatives are documented explicitly.

The roadmap describes project scope, while linked issues and execution evidence establish what has been verified. The lab does not imply production readiness without further operational evaluation.