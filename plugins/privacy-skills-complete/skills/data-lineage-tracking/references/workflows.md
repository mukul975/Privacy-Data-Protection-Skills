# Data Lineage Tracking - Detailed Workflows

## Workflow 1: Source-to-Sink Lineage Mapping

### Phase 1: Collection Point Inventory

1. Extract system list from data inventory or CMDB
2. For each system, identify all data ingestion interfaces:
   - Web forms (review HTML form fields and backend handlers)
   - API endpoints accepting personal data (review OpenAPI/Swagger specs)
   - File upload mechanisms (SFTP, cloud storage dropzones)
   - Database direct inserts (application-level writes)
   - Message queue consumers (Kafka topics, RabbitMQ queues)
3. For each ingestion point, document:
   - Field-level data elements collected
   - Mapping to GDPR personal data categories (Art. 4(1))
   - Whether special category data under Art. 9 is collected
   - Privacy notice provided (Art. 13 reference)
   - Consent mechanism if applicable (Art. 7 reference)

### Phase 2: Transformation Chain Documentation

1. Identify all ETL/ELT pipelines touching personal data:
   - Scheduled batch jobs (cron, Airflow DAGs, Azure Data Factory)
   - Real-time stream processors (Kafka Streams, Spark Streaming, Flink)
   - Application-level transformations (business logic in microservices)
2. For each pipeline, document:
   - Source tables/topics and target tables/topics
   - Column-level transformations (renaming, type casting, derivation formulas)
   - Filtering logic (which records are included/excluded)
   - Aggregation operations (grouping, summarizing)
   - Pseudonymization steps (hashing, tokenization, encryption)
3. Create directed acyclic graph (DAG) representation:
   - Nodes = systems/tables/columns
   - Edges = data flows with transformation metadata
   - Annotations = legal basis, retention period, access controls

### Phase 3: Storage Location Mapping

1. For each system in the lineage, document storage details:
   - Database engine and version
   - Physical location (data center, cloud region, availability zone)
   - Encryption at rest (algorithm, key management)
   - Access control mechanism (RBAC roles, IAM policies)
   - Backup schedule and backup retention period
2. Cross-reference with retention schedule:
   - Production retention period
   - Archive retention period
   - Backup retention period (often longer than production)
   - Legal hold exceptions

### Phase 4: Output and Deletion Mapping

1. Document all data egress points:
   - Reports and dashboards (who has access, what PII is displayed)
   - API responses to external consumers
   - File exports (automated reports, data extracts)
   - Processor data feeds
   - Cross-border transfers
2. Document deletion mechanisms:
   - Automated deletion jobs (schedule, scope, verification)
   - Manual deletion procedures (DSAR erasure workflow)
   - Anonymization procedures (technique, validation)
   - Backup deletion lag (how long until backups rotate out)

## Workflow 2: Automated Lineage Discovery

### Database-Level Discovery

1. Enable query logging on all databases containing personal data:
   - PostgreSQL: `log_statement = 'all'` or use `pg_stat_statements`
   - MySQL: General query log or Performance Schema
   - SQL Server: Extended Events or SQL Profiler
   - BigQuery: INFORMATION_SCHEMA.JOBS view
2. Parse query logs to extract:
   - Source tables read (FROM clauses, JOINs)
   - Target tables written (INSERT INTO, CREATE TABLE AS)
   - Column-level lineage from SELECT column lists
   - Transformation logic from expressions and functions
3. Build column-level lineage graph from parsed queries

### Application-Level Discovery

1. Instrument application code with distributed tracing:
   - OpenTelemetry spans annotated with data category tags
   - Service mesh telemetry (Istio, Linkerd) for inter-service data flows
2. Analyze API specifications:
   - OpenAPI/Swagger definitions listing request/response fields
   - GraphQL schemas showing data types and relationships
   - gRPC protobuf definitions
3. Review application data models:
   - ORM entity definitions (Django models, SQLAlchemy, Hibernate)
   - Data transfer objects (DTOs) showing field mappings between layers

### Pipeline-Level Discovery

1. Extract metadata from orchestration tools:
   - Apache Airflow: DAG definitions, task dependencies, XCom data
   - dbt: Model SQL files, ref() dependencies, documentation
   - Azure Data Factory: Pipeline JSON definitions, linked services
   - AWS Glue: Job definitions, crawler metadata
2. Parse pipeline definitions to extract:
   - Source and target datasets
   - Transformation logic
   - Schedule and trigger information
   - Error handling and retry behavior

## Workflow 3: RoPA Integration

### Linking Lineage to Art. 30 Records

1. For each processing activity in the RoPA:
   - Identify the corresponding lineage path(s)
   - Verify that all systems in the lineage path are documented in the RoPA
   - Confirm that data categories in the lineage match Art. 30(1)(c) categories
   - Validate that recipients in the lineage match Art. 30(1)(d) disclosures
   - Check that transfers identified in the lineage have Art. 44-49 safeguards
2. Gap analysis:
   - Lineage paths without corresponding RoPA entries indicate undocumented processing
   - RoPA entries without lineage paths may indicate stale records or missing systems
3. Remediation:
   - Create new RoPA entries for undocumented processing
   - Archive or update stale RoPA entries
   - Document newly discovered data flows in lineage and RoPA simultaneously

### Using Lineage for DSAR Response

1. When a data subject exercises Art. 15 (access) or Art. 17 (erasure):
   - Query lineage graph for all nodes containing data for the identified subject
   - Generate list of systems to query/delete from
   - Track completion of action across all lineage nodes
   - Verify backup systems are included (with appropriate deletion timelines)
2. For Art. 20 (portability):
   - Query lineage for data provided by the subject (consent or contract basis)
   - Exclude derived or inferred data (not subject to portability per WP29 Guidelines on Right to Data Portability, WP242)
   - Export from source systems in machine-readable format

## Workflow 4: Lineage Validation and Maintenance

### Quarterly Validation Process

1. **Automated validation**:
   - Run lineage discovery tools and compare output to documented lineage
   - Flag new data flows not in current documentation
   - Flag documented flows no longer observed in system metadata
2. **Manual review**:
   - Data owners review lineage paths for their systems
   - Architecture team validates system interconnections
   - Privacy team validates legal basis and retention assignments
3. **Change reconciliation**:
   - Review change management records for new systems deployed
   - Review decommissioned systems and verify removal from lineage
   - Review new vendor contracts for additional processing

### Annual Comprehensive Review

1. Full lineage walk-through with system architects
2. Cross-reference against current RoPA
3. Update DPIA triggers based on evolved lineage patterns
4. Report lineage coverage metrics to DPO:
   - Percentage of systems with documented lineage
   - Number of lineage paths validated in the quarter
   - Number of gaps identified and remediated
   - Average time to update lineage after system change
