# Automated Data Discovery Configuration and Results Report

## Organisation: Vanguard Financial Services
## Report Reference: DISC-RPT-2026-Q1
## Reporting Period: 2026-01-01 to 2026-03-14
## Prepared By: Michael Chen, Privacy Engineering Lead
## Reviewed By: Dr. James Whitfield, Data Protection Officer

---

## 1. Discovery Platform Configuration

### Primary Platform: Microsoft Purview

| Configuration Item | Setting |
|-------------------|---------|
| **Tenant** | vanguardfs.onmicrosoft.com |
| **Data Map Sources Registered** | 47 sources across Azure, AWS, and on-premises |
| **Self-Hosted Integration Runtimes** | 3 (London DC, Frankfurt DC, New York DC) |
| **Built-in SITs Enabled** | 156 (all EU and UK specific types) |
| **Custom SITs Created** | 12 (Vanguard-specific identifiers) |
| **Trainable Classifiers** | 3 (health correspondence, financial complaints, regulatory reports) |
| **Exact Data Match (EDM) Schemas** | 2 (customer master, employee master) |
| **Sensitivity Labels** | 4 tiers mapped (Public, Internal, Confidential, Restricted) |

### Secondary Platform: AWS Macie

| Configuration Item | Setting |
|-------------------|---------|
| **Region** | eu-west-2 (London) |
| **S3 Buckets Monitored** | 23 |
| **Custom Data Identifiers** | 8 |
| **Managed Identifiers Enabled** | All EU-region identifiers |
| **Findings Destination** | AWS Security Hub + EventBridge → SIEM |

### Supplementary Platform: BigID

| Configuration Item | Setting |
|-------------------|---------|
| **Deployment** | SaaS (EU-hosted instance) |
| **Data Source Connectors** | 31 (Salesforce, Workday, ADP, Oracle DW, SharePoint, AWS S3) |
| **Identity Correlation** | Enabled across CRM, HR, and Payroll systems |
| **Classification Policies** | GDPR taxonomy (personal, special category, criminal, pseudonymised, anonymous) |

---

## 2. Scanning Schedule

| Scan Type | Platform | Frequency | Window | Last Execution |
|-----------|----------|-----------|--------|---------------|
| Full Discovery | Purview | Monthly | 1st Saturday, 02:00-14:00 UTC | 2026-03-07 |
| Incremental | Purview | Weekly | Saturday, 02:00-06:00 UTC | 2026-03-14 |
| Full Discovery | Macie | Monthly | 1st Sunday, 02:00-08:00 UTC | 2026-03-08 |
| Event-Driven | Macie | On S3 PUT | Continuous | Ongoing |
| Full Correlation | BigID | Weekly | Sunday, 01:00-09:00 UTC | 2026-03-09 |
| Incremental | BigID | Daily | 01:00-03:00 UTC | 2026-03-14 |

---

## 3. Discovery Results Summary — Q1 2026

### Findings by Category

| PII Category | Findings Count | Sources Affected | Highest Risk |
|-------------|---------------|-----------------|-------------|
| Direct Identifiers (names, IDs, email) | 1,247,832 | 38 | Confidential |
| Financial Data (IBAN, card numbers) | 892,451 | 22 | Restricted |
| Special Category — Art. 9 (health, biometric) | 23,847 | 5 | Restricted |
| Criminal Data — Art. 10 | 4,219 | 3 | Restricted |
| Online Identifiers (IP, cookies) | 2,891,003 | 12 | Confidential |
| Indirect Identifiers (customer IDs, employee IDs) | 3,412,908 | 41 | Confidential |
| Location Data | 156,294 | 7 | Confidential |
| Pseudonymised Data | 891,204 | 8 | Internal |
| **Total** | **9,519,758** | **47** | — |

### Findings by Data Source (Top 10)

| Data Source | Type | Findings | Primary Categories |
|------------|------|----------|-------------------|
| Salesforce CRM | SaaS | 2,847,102 | Direct identifiers, financial |
| Oracle Data Warehouse | Database | 2,103,847 | All categories |
| SharePoint Online | Collaboration | 1,204,592 | Direct identifiers, documents |
| Workday HR | SaaS | 487,291 | Direct identifiers, special category |
| AWS S3 — Data Lake | Cloud Storage | 1,892,038 | All categories |
| Exchange Online | Email | 394,827 | Direct identifiers, health (in body) |
| ADP Payroll | SaaS | 201,847 | Financial, trade union |
| Azure SQL — Trading | Database | 178,294 | Financial, indirect identifiers |
| On-Prem File Share — Legal | File Share | 92,481 | Criminal data, legal claims |
| Cority Occ Health | SaaS | 23,847 | Health data (Art. 9) |

### New Discoveries (Not in Previous Manual Inventory)

| Finding | Source | Category | Action Required |
|---------|--------|----------|----------------|
| Customer IP addresses logged in application debug files | AWS S3 — App Logs bucket | Online identifier | Review retention; apply access controls; add to RoPA |
| Employee health keywords in HR case management free-text notes | Workday HR | Special category (health) | Apply Restricted label; restrict access; assess Art. 9 compliance |
| Scanned passport images in SharePoint Legal folder | SharePoint Online | Direct identifier (biometric if facial recognition applied) | Apply Restricted label; verify purpose; assess retention |
| Customer IBAN numbers in Excel exports on shared drive | On-Prem File Share | Financial | Migrate to secure system; delete from file share; apply DLP policy |

---

## 4. Accuracy Metrics

### Monthly Accuracy Measurements

| Month | Sample Size | Precision | Recall | F1 Score | FP Rate |
|-------|------------|-----------|--------|----------|---------|
| January 2026 | 100 | 91% | 87% | 0.89 | 8% |
| February 2026 | 100 | 93% | 89% | 0.91 | 6% |
| March 2026 | 100 | 94% | 90% | 0.92 | 5% |

### Tuning Actions Taken This Quarter

| Issue | Action | Impact |
|-------|--------|--------|
| UK phone numbers flagged as NINO | Added negative keywords ("phone", "tel", "mobile", "direct line") | FP rate reduced from 12% to 5% for NINO SIT |
| Internal reference codes flagged as customer accounts | Implemented EDM schema for verified customer account numbers | FP rate reduced from 15% to 2% for account SIT |
| Health data in email not detected | Trained health correspondence classifier with 75 positive examples | Recall for health data improved from 72% to 88% |
| Passport numbers over-detected (9-digit number ambiguity) | Required proximity to "passport" keyword within 50 characters | FP rate reduced from 34% to 8% for passport SIT |

---

## 5. Recommendations

| Priority | Recommendation | Rationale |
|----------|---------------|-----------|
| HIGH | Remediate customer IBANs found in file share Excel exports | Financial PII in uncontrolled location; breach risk |
| HIGH | Apply DLP policy to prevent export of Restricted data to unmanaged locations | 4 new instances of PII data sprawl discovered this quarter |
| MEDIUM | Extend Purview scanning to Teams chat channels | Collaboration platform not yet covered; likely contains PII |
| MEDIUM | Implement auto-labelling for high-confidence (>90%) special category findings | Currently only 68% of Art. 9 data has Restricted label applied |
| LOW | Evaluate BigID correlation engine accuracy vs Purview standalone | Determine if cross-platform correlation adds sufficient value to justify cost |

---

*Report generated in accordance with Vanguard Financial Services Privacy Engineering Standard PES-2025-003. Next quarterly report: 2026-06-15.*
