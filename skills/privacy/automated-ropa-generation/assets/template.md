# Automated RoPA Generation — IT System Inventory Input Template

**Organisation**: Helix Biotech Solutions GmbH
**Scan Date**: [YYYY-MM-DD]
**Prepared By**: [Name, Title]

---

## Azure AD / Identity Provider Inventory

### Enterprise Applications

| # | Application Name | Publisher | Type | Assigned Groups | Personal Data Likely | Department |
|---|-----------------|-----------|------|-----------------|---------------------|------------|
| 1 | SAP SuccessFactors | SAP SE | SaaS (HR) | SG-HR-All | Yes | Human Resources |
| 2 | Veeva Vault CDMS | Veeva Systems | SaaS (Clinical) | SG-Clinical-Data | Yes (Special Category) | Clinical Operations |
| 3 | Salesforce | Salesforce Inc. | SaaS (CRM) | SG-Sales-All | Yes | Sales |
| 4 | Google Analytics 4 | Google LLC | SaaS (Analytics) | SG-Marketing | Yes (IP, cookies) | Digital Marketing |
| 5 | ADP Workforce Now | ADP Inc. | SaaS (Payroll) | SG-HR-Payroll | Yes (Financial) | Human Resources |
| 6 | ServiceNow | ServiceNow Inc. | SaaS (ITSM) | SG-IT-All | Limited | IT |
| 7 | Workday | Workday Inc. | SaaS (Finance) | SG-Finance-All | Yes (Vendor PII) | Finance |

### Security Groups with Data Access

| Group Name | Members | Systems Accessed | Data Categories |
|-----------|---------|-----------------|-----------------|
| SG-HR-Payroll | 4 | SAP SF, ADP | Employee PII, financial data |
| SG-Clinical-Data | 12 | Veeva Vault | Patient health data, genetic data |
| SG-Sales-All | 28 | Salesforce | Customer PII |
| SG-Finance-AP | 6 | Workday, Banking portal | Vendor PII, financial data |

---

## Cloud Service Inventory

### AWS Services

| Service | Instance/Resource | Region | Data Classification Tag | Encryption | Personal Data Indicator |
|---------|------------------|--------|------------------------|------------|------------------------|
| RDS (PostgreSQL) | helix-hr-prod | eu-central-1 | Confidential | AES-256 (KMS) | Yes — employee data |
| RDS (PostgreSQL) | helix-clinical-prod | eu-central-1 | Restricted | AES-256 (KMS) | Yes — patient data (Art. 9) |
| S3 | helix-clinical-docs | eu-central-1 | Restricted | AES-256 (SSE-KMS) | Yes — clinical documents |
| S3 | helix-marketing-assets | eu-central-1 | Internal | AES-256 (SSE-S3) | Limited — analytics data |
| CloudFront | d1234567.cloudfront.net | Global (edge) | Public | TLS 1.3 | Yes — IP addresses in logs |
| Lambda | payroll-sync | eu-central-1 | Confidential | N/A (stateless) | Yes — processes payroll data |
| SES | helix-email-prod | eu-west-1 | Internal | TLS 1.3 | Yes — email addresses |

### Azure Services

| Service | Instance | Region | Data Classification | Encryption | Personal Data |
|---------|----------|--------|--------------------|-----------|----|
| Azure SQL | helix-finance-db | West Europe | Confidential | TDE + AES-256 | Yes — financial records |
| Azure Blob | helix-compliance-docs | West Europe | Restricted | AES-256 | Yes — compliance documents |
| Azure AD | helix-biotech.onmicrosoft.com | Global | Confidential | Microsoft managed | Yes — identity data |

---

## Database Schema Summary

### helix-hr-prod (PostgreSQL, eu-central-1)

| Table | Row Count | PII Columns Detected | Special Category | Oldest Record |
|-------|-----------|---------------------|-----------------|---------------|
| employees | 342 | 12 (name, email, dob, tax_id, ssn, iban, salary, phone, address, religion) | Yes (religion) | 2018-03-15 |
| contractors | 87 | 8 (name, email, phone, tax_id, bank_account, address) | No | 2020-01-10 |
| applicants | 1,204 | 6 (name, email, phone, dob, address) | No | 2023-06-01 |
| time_records | 48,320 | 2 (employee_id FK, supervisor_name) | No | 2021-01-01 |

### helix-clinical-prod (PostgreSQL, eu-central-1)

| Table | Row Count | PII Columns Detected | Special Category | Oldest Record |
|-------|-----------|---------------------|-----------------|---------------|
| participants | 456 | 8 (dob, diagnosis, medical_history, genetic_biomarker, ethnicity, treatment) | Yes (health, genetic, ethnicity) | 2024-03-01 |
| adverse_events | 89 | 4 (participant_id FK, diagnosis, medication, event_description) | Yes (health) | 2024-04-15 |
| consent_records | 456 | 3 (participant_id FK, consent_date, signature_hash) | No | 2024-03-01 |

---

## API Gateway Endpoints (Personal Data Flows)

| Endpoint | Method | Personal Data Fields | Source | Destination | Daily Volume |
|----------|--------|---------------------|--------|-------------|-------------|
| /api/v2/employees | GET/POST | name, email, department | SuccessFactors | HR Portal | 340 |
| /api/v2/patients/{id} | GET | participant_id, diagnosis, treatment | Veeva Vault | Reporting dashboard | 1,200 |
| /api/v2/customers | GET/POST | name, email, company, phone | Salesforce | Internal apps | 890 |
| /api/v1/analytics | POST | ip_address, user_agent, page_url | Website JS | Google Analytics | 45,000 |

---

## Automated Scan Output Summary

| Metric | Value |
|--------|-------|
| Total applications discovered | [Number] |
| Total cloud services enumerated | [Number] |
| Total databases scanned | [Number] |
| Total PII columns detected | [Number] |
| Special category columns detected | [Number] |
| Potential international transfers flagged | [Number] |
| Draft RoPA entries generated | [Number] |
| Entries requiring human review | [Number] (should be 100%) |

---

*All draft entries generated by automated scanning require DPO and processing owner review before approval. Automated detection supplements but does not replace human assessment of purposes, lawful basis, and proportionality.*
