---
name: auto-data-discovery
description: >-
  Implements automated PII discovery and classification using tools like
  Microsoft Purview, BigID, OneTrust DataDiscovery, and AWS Macie. Covers
  scanning schedules, accuracy tuning, false positive management, and
  integration patterns. Keywords: data discovery, PII scanning, Purview,
  BigID, Macie, OneTrust, automated classification, data cataloging.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "data-discovery, pii-scanning, purview, bigid, macie, onetrust"
---

# Automated PII Discovery and Classification

## Overview

Automated data discovery tools scan structured and unstructured data repositories to identify, classify, and catalogue personal data across the enterprise. Manual data inventories cannot keep pace with the volume, velocity, and variety of modern data processing. Automated discovery provides continuous visibility into where personal data resides, how it flows, and whether it is classified and protected according to policy. This skill covers implementation patterns for four leading platforms — Microsoft Purview, BigID, OneTrust DataDiscovery, and AWS Macie — with focus on scanning configuration, accuracy optimisation, and integration with privacy compliance workflows.

## Platform Comparison

| Capability | Microsoft Purview | BigID | OneTrust DataDiscovery | AWS Macie |
|-----------|------------------|-------|----------------------|-----------|
| **Structured data scanning** | SQL Server, Azure SQL, Synapse, Cosmos DB, Oracle, PostgreSQL, MySQL, Teradata | 100+ connectors including all major RDBMS, NoSQL, data warehouses | 200+ connectors, pre-built integrations with SaaS applications | S3, DynamoDB, RDS (via Lambda) |
| **Unstructured data scanning** | SharePoint, OneDrive, Exchange, Azure Blob, Azure Files, AWS S3, GCP Storage | File shares, email, SharePoint, cloud storage, Slack, Teams, Confluence | File shares, email, cloud storage, collaboration platforms | S3 buckets (primary focus) |
| **Classification method** | 300+ built-in sensitive information types (SITs), trainable classifiers, exact data match (EDM), custom regex | ML-based NER, correlation analysis, pattern matching, custom classifiers | Pattern matching, NER, contextual analysis, custom rules | ML-based pattern matching, custom data identifiers, managed data identifiers |
| **GDPR-specific classifiers** | EU national ID formats, EU passport numbers, EU debit/credit card numbers, EU tax ID numbers per Member State | GDPR personal data taxonomy, Art. 9 special category detection, cross-regulation mapping | Pre-built GDPR data subject types, purpose mapping, lawful basis tagging | EU personal data identifiers (limited — primarily financial and identity patterns) |
| **Accuracy tuning** | Confidence levels (low/medium/high), custom keyword dictionaries, EDM for exact matching, document fingerprinting | ML model retraining, feedback loop, confidence thresholds, correlation rules | Confidence scoring, validation rules, exception management | Custom data identifiers with regex and keyword proximity, severity scoring |
| **Deployment model** | SaaS (Microsoft 365/Azure), hybrid with Purview governance | SaaS, on-premises, hybrid | SaaS, on-premises agent | AWS-native SaaS |
| **Pricing model** | Per information protection unit (Azure), per Microsoft 365 licence tier (E5 includes advanced) | Per data source connector, per TB scanned | Per data source module, per connector | Per S3 bucket evaluated, per GB scanned |

## Implementation Pattern — Microsoft Purview

### Architecture

```
Data Sources                    Microsoft Purview
┌─────────────┐                ┌───────────────────────────┐
│ Azure SQL   │──────scanner──►│ Data Map (metadata store)  │
│ SharePoint  │──────scanner──►│ Data Catalog (search/tag)  │
│ AWS S3      │──────scanner──►│ Data Estate Insights       │
│ On-prem SQL │──self-hosted──►│ Information Protection     │
│ Power BI    │──────scanner──►│ Data Loss Prevention (DLP) │
└─────────────┘                └───────────────────────────┘
```

### Configuration Steps for Vanguard Financial Services

**Step 1: Register Data Sources**
- Register all Azure SQL databases, SharePoint sites, Azure Blob Storage accounts
- Install self-hosted integration runtime for on-premises SQL Server and file shares
- Register AWS S3 buckets via cross-cloud connector
- Register Power BI workspaces for report-level sensitivity scanning

**Step 2: Configure Scanning Rules**
- Enable built-in sensitive information types (SITs) for all EU jurisdictions:
  - UK National Insurance Number (pattern: `[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]`)
  - EU Passport Numbers (per Member State format)
  - International Banking Account Number (IBAN)
  - EU Tax Identification Numbers
  - EU Health Insurance Card Number
- Create custom SITs for Vanguard-specific identifiers:
  - Customer account number format: `VFS-\d{10}`
  - Employee ID format: `EMP-[A-Z]{2}\d{6}`
  - Investment portfolio reference: `PF-\d{8}-[A-Z]{2}`
- Configure confidence levels: HIGH for direct identifiers, MEDIUM for indirect, LOW for contextual matches
- Enable exact data match (EDM) for customer name verification against CRM database

**Step 3: Set Scanning Schedule**
- Full scan: Monthly (first Saturday of each month, 02:00 UTC)
- Incremental scan: Weekly (every Saturday, 02:00 UTC)
- On-demand scan: Triggered by new data source registration or incident response
- Estimated scan duration: 8 hours for full scan across 15 TB of data

**Step 4: Configure Sensitivity Labels**
- Map Purview sensitivity labels to Vanguard classification tiers:
  - `Public` → Purview label: Public
  - `Internal` → Purview label: General
  - `Confidential` → Purview label: Confidential
  - `Restricted` → Purview label: Highly Confidential (auto-applied to Art. 9/Art. 10 data)
- Enable auto-labelling policies: Apply labels based on detected SITs
- Configure label inheritance: Child items inherit parent container label unless higher

**Step 5: DLP Policy Integration**
- Create DLP policies triggered by sensitivity labels:
  - Restricted data: Block external sharing, require encryption, notify DPO
  - Confidential data: Warn on external sharing, audit log, require justification
  - Internal data: Audit log only
- Configure endpoint DLP for Windows devices (prevent copy to USB, print, screenshot for Restricted content)

### Accuracy Tuning for Purview

| Issue | Tuning Approach |
|-------|----------------|
| **False positive: UK phone numbers flagged as National Insurance numbers** | Increase minimum confidence to HIGH for NINO SIT; add negative keyword list ("phone", "tel", "fax", "mobile") |
| **False positive: Internal reference numbers flagged as account numbers** | Create EDM schema for actual customer accounts; custom SIT with proximity to customer-related keywords |
| **False negative: Health data in free-text email bodies** | Enable trainable classifier for health content; train on sample of 50+ positive examples from occupational health correspondence |
| **False negative: Genetic identifiers in research datasets** | Create custom SIT for rs-number pattern (`rs\d{4,12}`), ICD-10 codes, and HUGO gene names |

## Implementation Pattern — BigID

### Architecture

BigID uses a distributed scanning architecture with correlation-based discovery:

```
Data Sources              BigID Platform
┌─────────────┐          ┌──────────────────────────┐
│ Databases   │──scan───►│ Discovery Engine          │
│ File Shares │──scan───►│ Correlation Engine (ML)   │
│ Cloud       │──scan───►│ Classification Engine     │
│ SaaS Apps   │──API────►│ Catalog & Inventory       │
│ Email       │──scan───►│ Privacy Rights Automation │
└─────────────┘          └──────────────────────────┘
```

### Key Differentiator: Correlation-Based Identity Resolution

BigID's ML-based correlation engine identifies personal data by correlating data elements across sources to build identity profiles. This approach detects personal data that pattern matching alone would miss — for example, a customer ID in one system linked to a name in another.

### Configuration for Vanguard

- **Data source connections**: Configure connectors for Salesforce CRM, Workday HR, ADP Payroll, SharePoint, Azure SQL, AWS S3, on-premises Oracle Data Warehouse
- **Correlation rules**: Enable identity correlation across CRM customer ID, HR employee ID, and payroll employee number
- **Classification policies**: Map BigID classifiers to GDPR categories (personal data, special category, criminal data, pseudonymised, anonymised)
- **Scanning schedule**: Incremental scans daily at 01:00 UTC; full correlation rebuild weekly

## Implementation Pattern — OneTrust DataDiscovery

### Architecture

OneTrust integrates discovery with its broader privacy management platform:

```
Data Sources              OneTrust Platform
┌─────────────┐          ┌──────────────────────────┐
│ Cloud/SaaS  │──API────►│ DataDiscovery Module      │
│ Databases   │──agent──►│ Data Mapping (Art. 30)    │
│ File Shares │──agent──►│ Assessment Automation     │
│ Endpoints   │──agent──►│ Consent Management        │
└─────────────┘          │ DSAR Automation           │
                         └──────────────────────────┘
```

### Key Differentiator: Privacy Program Integration

OneTrust's value proposition is tight integration between discovery results and privacy program management — discovered personal data feeds directly into Art. 30 records, DPIA assessments, and DSAR fulfilment workflows.

### Configuration for Vanguard

- **Data source inventory**: Use OneTrust's data mapping questionnaires to establish baseline, then deploy automated scanning to validate and enrich
- **Integration with RoPA**: Map discovered data categories to Art. 30 processing activity records
- **DSAR integration**: Configure discovery results to support automated data subject access request fulfilment (locate all data for a given identity across systems)
- **Vendor discovery**: Scan for personal data shared with third-party processors; reconcile with vendor management records

## Implementation Pattern — AWS Macie

### Architecture

Macie is purpose-built for S3 data discovery within AWS:

```
AWS Environment
┌─────────────────────────────────────┐
│  S3 Buckets    ──scan──►  Macie     │
│                          │          │
│  EventBridge  ◄──alerts──┘          │
│  Security Hub ◄──findings──┘        │
│  CloudWatch   ◄──metrics──┘         │
└─────────────────────────────────────┘
```

### Configuration for Vanguard

- **Bucket selection**: Enable Macie for all S3 buckets in eu-west-1 (London) and eu-west-2 (Ireland) regions
- **Custom data identifiers**: Create identifiers for Vanguard-specific patterns (customer account numbers, employee IDs, portfolio references)
- **Managed identifiers**: Enable all EU-region managed data identifiers (UK NINO, IBAN, EU passport)
- **Job scheduling**: Scheduled classification jobs weekly; event-driven scan on new object upload for high-sensitivity buckets
- **Findings integration**: Route findings to AWS Security Hub for centralised monitoring; trigger Lambda function for automated label application

## Scanning Schedule Best Practices

| Scan Type | Frequency | Duration Window | Trigger |
|-----------|-----------|----------------|---------|
| **Full discovery scan** | Monthly | Weekend maintenance window (8-12 hours) | Scheduled |
| **Incremental scan** | Weekly | Off-peak hours (2-4 hours) | Scheduled |
| **New source onboarding scan** | On registration | Within 48 hours of source registration | Event-driven |
| **Post-incident scan** | As needed | Immediate (targeted scope) | Incident response |
| **Pre-DPIA scan** | Before DPIA commencement | 1-2 weeks before DPIA start | Project-triggered |

## Accuracy Metrics and Tuning

### Key Performance Indicators

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **Precision (true positive rate)** | > 90% | Sample 100 classified items monthly; verify classification accuracy |
| **Recall (detection rate)** | > 85% | Plant known PII test data in scan scope; measure detection rate |
| **False positive rate** | < 10% | Count items classified as personal data that are not |
| **False negative rate** | < 15% | Count personal data items missed by the scanner |
| **Classification consistency** | > 95% | Same data element classified consistently across repeat scans |

### Continuous Improvement Cycle

```
Month 1: Baseline scan → establish initial accuracy metrics
Month 2: Review false positives/negatives → tune rules and thresholds
Month 3: Re-scan → measure improvement
Month 4: Expand scope (new data sources) → re-baseline
Month 5: Review edge cases → create custom classifiers
Month 6: Accuracy audit by DPO → formal accuracy report
[Repeat cycle]
```

## Integration Points

- **data-inventory-mapping**: Automated discovery feeds Art. 30 data inventory
- **pii-in-unstructured**: Specialized techniques for unstructured data augment platform capabilities
- **data-labeling-system**: Discovery results drive automated label application
- **classification-policy**: Discovery validates compliance with classification policy tiers
- **data-lineage-tracking**: Discovery combined with lineage provides complete data visibility
