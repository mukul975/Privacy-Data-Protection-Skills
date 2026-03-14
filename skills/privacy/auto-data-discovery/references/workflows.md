# Workflows — Automated Data Discovery

## Workflow 1: Initial Discovery Deployment

### Purpose
Deploy automated PII discovery across Vanguard Financial Services enterprise data estate.

### Process Flow

```
START: Privacy program decision to implement automated discovery
  │
  ├─► Step 1: Data Source Inventory
  │     - Catalogue all data repositories: databases, file shares, cloud storage,
  │       SaaS applications, email systems, collaboration platforms
  │     - Classify sources by priority: Tier 1 (customer-facing, >10K records),
  │       Tier 2 (internal operations), Tier 3 (archival/backup)
  │     - Identify connectivity requirements: network access, authentication,
  │       API availability, agent deployment needs
  │     Output: Prioritised data source inventory with connectivity details
  │
  ├─► Step 2: Platform Selection and Configuration
  │     - Select scanning platform based on data estate profile
  │     - For Vanguard: Microsoft Purview (primary — Azure/M365 estate) +
  │       AWS Macie (S3 buckets) + BigID (cross-platform correlation)
  │     - Install self-hosted integration runtimes for on-premises sources
  │     - Configure authentication: managed identity for Azure, IAM role for AWS,
  │       service account for on-premises
  │     Output: Platform deployed with connectivity established
  │
  ├─► Step 3: Classification Rule Configuration
  │     - Enable all GDPR-relevant built-in classifiers
  │     - Create custom classifiers for organisation-specific patterns
  │     - Set confidence thresholds: HIGH (>85%) for automated labelling,
  │       MEDIUM (75-85%) for review queue, LOW (<75%) for suppression
  │     - Configure false positive suppression rules
  │     Output: Classification rules configured and tested
  │
  ├─► Step 4: Pilot Scan (Tier 1 Sources)
  │     - Run full scan on 2-3 Tier 1 sources (e.g., CRM database, HR system)
  │     - Review results for accuracy: sample 100 items, verify classification
  │     - Measure precision and recall against known data elements
  │     - Tune rules based on pilot results
  │     Output: Pilot scan results with accuracy metrics
  │
  ├─► Step 5: Full Deployment
  │     - Extend scanning to all Tier 1 and Tier 2 sources
  │     - Configure scanning schedules (monthly full, weekly incremental)
  │     - Enable alerting: new PII discovered in unexpected locations,
  │       classification changes, scan failures
  │     - Configure integration with privacy management platform
  │     Output: Full deployment operational
  │
  └─► Step 6: Baseline Report
        - Generate initial data discovery report for DPO and senior management
        - Compare automated findings to manual data inventory
        - Identify gaps: data in manual inventory not found by scanner,
          data found by scanner not in manual inventory
        - Establish accuracy baseline for ongoing monitoring
        Output: Baseline discovery report and accuracy metrics
```

## Workflow 2: Ongoing Discovery Operations

### Purpose
Maintain continuous PII visibility through scheduled scanning and exception management.

### Process Flow

```
WEEKLY CYCLE
  │
  ├─► Monday: Review Previous Week's Scan Results
  │     - Check scan completion status across all sources
  │     - Review new PII discoveries (items found for first time)
  │     - Review classification changes (items reclassified)
  │     - Triage alerts: scan failures, connectivity issues
  │     Output: Weekly discovery status report
  │
  ├─► Tuesday-Thursday: Exception Management
  │     - Review medium-confidence classifications (75-85%)
  │     - Validate or override classifications in review queue
  │     - Investigate false positives and update suppression rules
  │     - Investigate false negatives reported by business users
  │     Output: Updated classification rules
  │
  ├─► Friday: Integration Updates
  │     - Push confirmed classifications to data inventory (Art. 30 RoPA)
  │     - Update sensitivity labels based on new discoveries
  │     - Trigger DLP policy updates if new high-risk data locations identified
  │     - Report material findings to DPO
  │     Output: Updated inventory and labels
  │
  MONTHLY CYCLE
  │
  ├─► Full scan execution (first weekend)
  ├─► Accuracy measurement (sample 100 classified items)
  ├─► Rule tuning based on accuracy results
  ├─► New data source onboarding (if any registered in month)
  ├─► Monthly discovery report to DPO
  │
  QUARTERLY CYCLE
  │
  ├─► Platform health review (performance, storage, licensing)
  ├─► Cross-platform reconciliation (Purview vs BigID vs Macie findings)
  ├─► Accuracy audit by independent reviewer
  ├─► Classification rule review with business stakeholders
  └─► Report to Privacy Steering Committee
```

## Workflow 3: Incident-Triggered Discovery

### Purpose
Rapid targeted scanning in response to data incidents or regulatory inquiries.

### Process Flow

```
TRIGGER: Data breach, regulatory inquiry, or DSAR requiring full data location
  │
  ├─► Step 1: Scope Definition
  │     - Define the data elements of interest (e.g., "all instances of customer
  │       account number VFS-2847593012")
  │     - Define the system scope (all systems, or specific suspect systems)
  │     - Determine urgency: breach response (hours), DSAR (days), audit (weeks)
  │     Output: Scan scope and priority
  │
  ├─► Step 2: Targeted Scan Execution
  │     - Configure on-demand scan job targeting specific data elements
  │     - For Purview: use content search in Microsoft 365 Compliance Center
  │     - For BigID: use identity-centric search across all connected sources
  │     - For Macie: create one-time classification job with custom identifier
  │     Output: Scan results
  │
  ├─► Step 3: Results Analysis
  │     - Identify all locations where the target data resides
  │     - Map data flows: how did the data reach each location?
  │     - Assess whether data was shared with unauthorised recipients
  │     - Determine retention status: should the data still exist?
  │     Output: Data location map and flow analysis
  │
  └─► Step 4: Response Actions
        - For breach: inform incident response team of affected data scope
        - For DSAR: compile data from all identified locations for response
        - For audit: provide evidence of data location and controls
        - Document findings for regulatory record
        Output: Response package
```
