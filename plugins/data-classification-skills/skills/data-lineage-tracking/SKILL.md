---
name: data-lineage-tracking
description: >-
  Implements data lineage tracking for privacy compliance including origin tracking,
  transformation logging, access auditing, deletion verification, and cross-system
  lineage graphs. Covers source-to-sink mapping, GDPR Art. 30 RoPA integration,
  automated lineage discovery, and breach impact scoping. Keywords: data lineage,
  data provenance, data flow mapping, transformation logging, deletion verification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "data-lineage, data-provenance, data-flow-mapping, transformation-logging, deletion-verification"
---

# Data Lineage Tracking

## Purpose

Map and document the complete lifecycle of personal data through organizational systems, from initial collection point through all transformations, transfers, and storage locations to final deletion or anonymization.

## Prerequisites

- Data inventory or asset register identifying systems processing personal data
- Network architecture documentation showing system interconnections
- Access to system metadata, ETL configurations, and API documentation
- Records of Processing Activities (RoPA) under GDPR Article 30

## Workflow

### Step 1: Define Lineage Scope

Determine scope boundaries for the lineage mapping exercise:

1. **Data categories**: Identify which personal data categories to trace (identity data, contact data, financial data, behavioral data, special category data under Art. 9)
2. **System boundaries**: Define which systems are in-scope (production databases, data warehouses, analytics platforms, third-party SaaS, backup systems)
3. **Temporal scope**: Determine whether to map current-state lineage only or include historical data flows
4. **Legal basis mapping**: Link each processing activity in the lineage to its GDPR Article 6 lawful basis

### Step 2: Identify Data Sources (Collection Points)

Document every point where personal data enters the organization:

1. **Direct collection**: Web forms, mobile apps, point-of-sale terminals, customer service interactions, paper forms digitized via scanning
2. **Indirect collection**: Third-party data providers, publicly available sources, data brokers, partner organizations
3. **Derived data**: Data generated through processing (risk scores, customer segments, behavioral profiles)
4. **Inferred data**: Data inferred from other data points (creditworthiness, health predictions, preferences)

For each source, record:
- Source identifier and type
- Data categories collected (referencing Art. 30(1)(c) categories)
- Legal basis under Art. 6(1) and, if applicable, Art. 9(2)
- Information provided to data subjects per Art. 13 or Art. 14
- Volume and frequency of collection

### Step 3: Map Data Transformations

Document every transformation applied to personal data:

1. **ETL processes**: Extract-Transform-Load pipelines moving data between systems
2. **Aggregation**: Grouping individual records into summary statistics
3. **Pseudonymization**: Replacing identifiers with tokens per Art. 4(5) and Recital 26
4. **Anonymization**: Irreversible de-identification per WP29 Opinion 05/2014
5. **Enrichment**: Combining data from multiple sources to create enriched profiles
6. **Format conversion**: Changing data formats (CSV to JSON, database migration)

For each transformation, record:
- Input data categories and source system
- Transformation logic description
- Output data categories and destination system
- Whether transformation changes the identifiability of data subjects
- Retention period at destination per Art. 5(1)(e) storage limitation

### Step 4: Document Data Flows and Transfers

Map all movements of personal data between systems and parties:

1. **Internal flows**: Between departments, systems, databases within the organization
2. **Processor transfers**: To data processors under Art. 28 agreements
3. **Third-country transfers**: Cross-border transfers requiring Art. 44-49 safeguards
4. **Third-party disclosures**: To independent controllers (regulators, partners, law enforcement)

For each flow, record:
- Source and destination system/entity
- Transfer mechanism (API, file transfer, database replication, manual export)
- Legal safeguard for international transfers (SCCs, BCRs, adequacy decision)
- Encryption in transit and at rest
- Frequency and volume

### Step 5: Map Data Storage and Retention

Document where personal data resides at each stage:

1. **Primary storage**: Production databases, CRM systems, HRIS
2. **Secondary storage**: Data warehouses, analytics databases, reporting systems
3. **Archival storage**: Long-term archives, cold storage, compliance archives
4. **Backup storage**: Disaster recovery systems, backup tapes, cloud backup
5. **Temporary storage**: Caches, message queues, log files, session storage

For each storage location, record:
- Storage technology and location (on-premises, cloud region)
- Retention period and legal basis for retention
- Access controls and encryption
- Deletion or anonymization mechanism at end of retention period

### Step 6: Implement Automated Lineage Discovery

Deploy tooling to automate lineage tracking:

1. **Database-level lineage**: Query log analysis, column-level lineage from SQL parsing
2. **Application-level lineage**: API call tracing, service mesh observability
3. **Pipeline-level lineage**: ETL tool metadata (Apache Airflow lineage backend, dbt documentation)
4. **Infrastructure-level lineage**: Network flow logs, data lake audit trails

Use the `scripts/process.py` helper to parse system metadata and generate lineage graphs.

### Step 7: Integrate with RoPA and Compliance

Link lineage data to GDPR compliance documentation:

1. **Art. 30 RoPA**: Each lineage path should map to a processing activity in the RoPA
2. **DPIA triggers**: Flag lineage paths involving Art. 35(3) processing (large-scale profiling, systematic monitoring, special categories)
3. **Data subject rights**: Use lineage to locate all data for DSAR responses (Art. 15 access, Art. 17 erasure, Art. 20 portability)
4. **Breach impact scoping**: Use lineage to determine affected data subjects and categories during incident response per Art. 33(3)

### Step 8: Maintain and Validate

Establish ongoing lineage maintenance:

1. **Change management**: Update lineage when new systems, data flows, or processing activities are introduced
2. **Periodic validation**: Quarterly review to verify lineage accuracy against actual system behavior
3. **Stakeholder review**: Annual sign-off from data owners, system architects, and DPO
4. **Completeness check**: Cross-reference lineage against data inventory and RoPA to identify gaps

## Verification

- [ ] All personal data categories have documented source-to-sink lineage paths
- [ ] Each lineage node includes legal basis, retention period, and access controls
- [ ] Transformation steps document identifiability impact
- [ ] Cross-border transfers identified with Art. 44-49 safeguards documented
- [ ] Lineage integrates with Art. 30 RoPA entries
- [ ] Automated discovery covers at least database and pipeline layers
- [ ] Quarterly validation schedule established with responsible owners assigned
