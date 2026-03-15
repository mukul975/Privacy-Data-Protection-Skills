# Data Inventory and Mapping Record

## Organisation: Vanguard Financial Services
## Inventory Reference: DI-2026-CRM-001
## System: Salesforce CRM
## Date: 2026-03-14
## System Owner: Alexandra Wright, Head of Sales Operations
## Privacy Analyst: Sarah Mitchell

---

## 1. System Overview

| Field | Detail |
|-------|--------|
| **System Name** | Salesforce CRM (Sales Cloud Enterprise Edition) |
| **System ID** | SYS-CRM-001 |
| **Type** | SaaS |
| **Vendor** | Salesforce Inc. |
| **Hosting Location** | EU (Frankfurt, AWS eu-central-1) |
| **Department** | Sales, Customer Service, Marketing |
| **Data Subjects** | Customers (2.4M), Prospects (890K), Contact persons at corporate clients (45K) |
| **Processing Purposes** | Customer relationship management, sales pipeline, service delivery, marketing campaigns |
| **System Owner** | Alexandra Wright, Head of Sales Operations |
| **Data Steward** | Thomas Reid, CRM Data Manager |
| **DPA/Processor Agreement** | DPA-SF-2024-001 (executed 2024-03-15, reviewed annually) |
| **DPIA Reference** | DPIA-CRM-2025-001 (completed 2025-11-20) |

---

## 2. Data Element Inventory

| Element ID | Field Name | Data Type | Category | Tier | Source | Lawful Basis | Retention |
|-----------|-----------|-----------|----------|------|--------|-------------|-----------|
| DE-CRM-001 | customer_full_name | VARCHAR(255) | PERSONAL_DIRECT | Confidential | Data subject (onboarding form) | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-002 | customer_email | VARCHAR(255) | PERSONAL_DIRECT | Confidential | Data subject (onboarding form) | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-003 | customer_phone | VARCHAR(20) | PERSONAL_DIRECT | Confidential | Data subject (onboarding form) | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-004 | customer_address | TEXT | PERSONAL_DIRECT | Confidential | Data subject (onboarding form) | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-005 | customer_dob | DATE | PERSONAL_DIRECT | Confidential | Data subject (KYC) | Art. 6(1)(c) Legal obligation | Relationship + 7yr |
| DE-CRM-006 | account_number | VARCHAR(14) | PERSONAL_INDIRECT | Confidential | System generated | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-007 | national_insurance_no | VARCHAR(9) | PERSONAL_DIRECT | Restricted | Data subject (tax reporting) | Art. 6(1)(c) Legal obligation | Relationship + 7yr |
| DE-CRM-008 | passport_scan | BLOB | PERSONAL_DIRECT | Restricted | Data subject (KYC) | Art. 6(1)(c) Legal obligation | 5yr post-verification |
| DE-CRM-009 | transaction_history | JSON | PERSONAL_INDIRECT | Confidential | System generated | Art. 6(1)(b) Contract | Relationship + 7yr |
| DE-CRM-010 | marketing_consent | BOOLEAN | NON_PERSONAL | Internal | Data subject | Art. 6(1)(a) Consent | Duration of consent |
| DE-CRM-011 | ip_address_login | VARCHAR(45) | PERSONAL_INDIRECT | Confidential | Auto-collected | Art. 6(1)(f) Legit interests | 90 days |
| DE-CRM-012 | service_notes | TEXT | PERSONAL_DIRECT | Confidential | Customer service agent | Art. 6(1)(b) Contract | Relationship + 7yr |

**Total Data Elements**: 12 classified fields
**Personal Data Elements**: 11 (92%)
**Restricted Tier**: 2 (NINO, passport scan)

---

## 3. Data Flow Diagram

```
                    ┌──────────────┐
                    │   Customer   │
                    │ (data subject)│
                    └──────┬───────┘
                           │
              Name, Email, │ Phone, Address,
              DOB, NINO,   │ Passport scan
              [CONFIDENTIAL/RESTRICTED]
                           │
                           ▼
                    ┌──────────────┐     Name, Email, Account
                    │  Salesforce  │────────────────────────────►┌───────────────┐
                    │     CRM      │  [CONFIDENTIAL]             │  Oracle DW    │
                    │  (Frankfurt) │                             │  (London DC)  │
                    └──────┬───┬───┘                             └───────────────┘
                           │   │
            ┌──────────────┘   └──────────────┐
            │                                  │
            ▼                                  ▼
    ┌──────────────┐                   ┌──────────────┐
    │  SharePoint  │                   │ Email Service│
    │  (documents) │                   │ (SendGrid)   │
    │  [CONFID.]   │                   │ [CONFID.]    │
    └──────────────┘                   └──────────────┘

    International Transfer:
    ┌──────────────┐      Metadata      ┌──────────────┐
    │  Salesforce  │─ ─ ─ ─ ─ ─ ─ ─ ─ ►│ Salesforce   │
    │  CRM (EU)    │   [EU-US DPF]      │ Inc. (US)    │
    └──────────────┘                    └──────────────┘
```

---

## 4. Data Flows — Detailed Register

### Inbound Flows

| Flow ID | Source | Data Categories | Mechanism | Frequency |
|---------|--------|----------------|-----------|-----------|
| DF-IN-001 | Customer (web onboarding) | Name, email, phone, address, DOB, NINO | HTTPS web form (TLS 1.3) | Continuous (~200/day) |
| DF-IN-002 | Customer (KYC documents) | Passport scan, utility bill | Encrypted document upload | Continuous (~200/day) |
| DF-IN-003 | Customer service (phone) | Service notes, complaint details | Agent manual entry | Continuous (~500/day) |

### Outbound Flows

| Flow ID | Destination | Data Categories | Mechanism | International? | Safeguard |
|---------|------------|----------------|-----------|---------------|-----------|
| DF-OUT-001 | Oracle Data Warehouse | Name, email, account, transactions | ETL (Azure Data Factory) | No | N/A |
| DF-OUT-002 | SharePoint (client docs) | KYC documents, agreements | API integration | No | N/A |
| DF-OUT-003 | SendGrid (email service) | Name, email | API (encrypted) | Yes (US) | SCCs (2021/914) |
| DF-OUT-004 | Salesforce Inc. (hosting) | All CRM data | SaaS platform | Yes (US) | EU-US DPF |
| DF-OUT-005 | HMRC (tax reporting) | Name, NINO, financial data | Secure file transfer | No | Legal obligation |

---

## 5. Art. 30 Processing Activity Record

| Art. 30(1) Field | Content |
|-----------------|---------|
| **(a) Controller** | Vanguard Financial Services Ltd, 25 Moorgate, London EC2R 6AQ. DPO: Dr. James Whitfield (dpo@vanguardfs.co.uk) |
| **(b) Purposes** | Customer relationship management, financial services delivery, regulatory compliance (KYC/AML), marketing (with consent) |
| **(c) Data subjects** | Customers, prospects, contact persons at corporate clients |
| **(d) Personal data categories** | Identity data (name, DOB, NINO, passport), contact data (email, phone, address), financial data (account, transactions), online identifiers (IP address), service records (notes, complaints) |
| **(e) Recipients** | Salesforce Inc. (processor), SendGrid (processor), HMRC (statutory), Oracle (processor — internal DW) |
| **(f) Transfers** | US — Salesforce Inc. (EU-US DPF), US — SendGrid (SCCs 2021/914) |
| **(g) Retention** | Customer data: duration of relationship + 7 years. Prospect data: 2 years from last contact. KYC documents: 5 years post-verification. IP logs: 90 days. |
| **(h) Security** | Encryption at rest (AES-256, Salesforce Shield), TLS 1.3 in transit, RBAC with MFA, field-level security for NINO/passport, audit trail logging, quarterly access reviews, annual penetration testing |

---

## 6. Review Schedule

| Review Type | Date | Reviewer |
|-------------|------|---------|
| Last full review | 2026-03-14 | Sarah Mitchell, Privacy Analyst |
| Last automated discovery reconciliation | 2026-03-07 | Michael Chen, Privacy Engineering |
| Next scheduled review | 2026-06-14 | Sarah Mitchell |
| Next DPO audit | 2026-09-14 | Dr. James Whitfield |

---

*Inventory maintained per Vanguard Data Classification Policy DCP-2025-v3.1 and Art. 30 GDPR. All changes version-controlled in privacy management platform.*
