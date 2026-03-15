# Data Lineage Documentation Report

**Organisation**: Vanguard Financial Services
**Report Date**: 2026-03-14
**Prepared By**: David Okoro, Data Engineering Lead
**Review Period**: Q1 2026
**DPO Approval**: Dr. James Whitfield, DPO

---

## 1. Lineage Scope

| Parameter | Value |
|-----------|-------|
| Data categories in scope | Identity, contact, financial, behavioral, employment, health (Art. 9) |
| Systems in scope | 14 production systems, 3 analytics platforms, 2 backup systems |
| Third-party processors | 4 (CRM provider, cloud hosting, email service, analytics platform) |
| Cross-border transfer destinations | United States (CRM), India (support services) |
| Lineage coverage | 92% of documented processing activities |

---

## 2. Collection Points

| ID | Source | Data Categories | Legal Basis | Art. 13 Notice |
|----|--------|----------------|-------------|----------------|
| COL-001 | Customer registration web form | Name, email, phone, address | Art. 6(1)(b) contract performance | Privacy notice displayed at point of collection, last updated 2026-01-15 |
| COL-002 | Mobile application | Device ID, usage data, GPS location | Art. 6(1)(a) explicit consent via in-app consent dialog | In-app privacy notice with layered disclosure, consent recorded in OneTrust |
| COL-003 | HR Information System | Employee name, payroll, health data, performance reviews | Art. 6(1)(b) employment contract / Art. 9(2)(b) employment obligations | Employee privacy notice issued at onboarding, acknowledged in DocuSign |
| COL-004 | Partner data feed (B2B) | Business contact name, title, company, email | Art. 6(1)(f) legitimate interest (LIA documented 2025-09-20) | Art. 14 notice sent within 5 business days of receipt |
| COL-005 | Customer support tickets | Name, email, issue description, attachments | Art. 6(1)(b) contract performance | Support portal privacy notice, link in ticket confirmation email |

---

## 3. Transformation Chain

| Step | Source | Process | Output | Identifiability Impact |
|------|--------|---------|--------|----------------------|
| T-001 | COL-001, COL-002 -> Production DB | Customer data ETL (Airflow DAG `customer_etl_daily`) | Merged customer profile with usage metrics and derived segment | No change - fully identifiable |
| T-002 | Production DB -> Pseudonymization Service | HMAC-SHA256 tokenization of direct identifiers | Pseudonymized dataset with usage patterns | Reduced - pseudonymized per Art. 4(5), re-identification possible with key |
| T-003 | Pseudonymized dataset -> Analytics DW | Aggregation by customer segment, 30-day rolling windows | Segment-level usage statistics | Reduced further - individual records not retained in aggregated tables |
| T-004 | Production DB -> Reporting Service | Daily extract of order volumes, revenue, active users | Aggregated business metrics dashboard | Anonymized - no personal data in output per WP29 Opinion 05/2014 criteria |
| T-005 | COL-003 -> Payroll Processor | Monthly payroll calculation with tax deductions | Payslip data, tax filings | No change - fully identifiable, Art. 9 special category (health deductions) |

---

## 4. Data Flow Map

### Internal Flows

| Flow ID | Source System | Destination System | Mechanism | Frequency | Encryption in Transit |
|---------|--------------|-------------------|-----------|-----------|----------------------|
| F-001 | Customer Registration Form | Production PostgreSQL DB | PostgreSQL TLS connection | Real-time | TLS 1.3 |
| F-002 | Mobile App | Production PostgreSQL DB | REST API over HTTPS | Real-time | TLS 1.3 |
| F-003 | Production DB | Customer ETL Pipeline | SQL SELECT via Airflow | Daily 02:00 UTC | Internal network, TLS 1.2 |
| F-004 | ETL Pipeline | Pseudonymization Service | gRPC internal API | Daily 03:00 UTC | mTLS |
| F-005 | Pseudonymization Service | Analytics Data Warehouse | BigQuery streaming insert | Daily 04:00 UTC | TLS 1.3 |
| F-006 | Production DB | Encrypted Backup Storage | pg_dump with AES-256 | Daily 01:00 UTC | AES-256 encrypted archive |

### External Transfers

| Flow ID | Source | Destination | Country | Transfer Safeguard | Mechanism | Frequency |
|---------|--------|------------|---------|-------------------|-----------|-----------|
| F-007 | ETL Pipeline | CRM Platform (Salesforce) | United States | EU SCCs 2021/914, Module 1 (controller-to-controller), executed 2025-06-15 | REST API over HTTPS | Weekly, Mondays 06:00 UTC |
| F-008 | Support Tickets | Support Provider (Freshdesk) | India | EU SCCs 2021/914, Module 2 (controller-to-processor), executed 2025-08-22 | REST API over HTTPS | Real-time |

---

## 5. Storage Locations

| Location ID | System | Technology | Region | Encryption at Rest | Retention | Deletion Mechanism |
|-------------|--------|-----------|--------|-------------------|-----------|-------------------|
| S-001 | Production Database | PostgreSQL 15 on AWS RDS | eu-west-1 (Dublin) | AES-256 (AWS KMS managed key) | 3 years from last activity | Automated deletion job runs monthly, soft-delete then hard-delete after 30 days |
| S-002 | Analytics Data Warehouse | Google BigQuery | europe-west3 (Frankfurt) | AES-256 (Google default encryption) | 2 years | Table expiration policy, partition-level deletion |
| S-003 | Backup Storage | AWS S3 Glacier | eu-west-1 (Dublin) | AES-256 (SSE-S3) | 4 years (backup rotation) | Lifecycle policy moves to Glacier after 90 days, deletes after 4 years |
| S-004 | HR Database | SAP SuccessFactors | eu-central-1 (Frankfurt) | AES-256 (SAP managed) | Employment duration + 7 years (statutory) | Manual deletion by HR admin post-retention, annual review |
| S-005 | Email Archive | Microsoft 365 | EU Data Boundary | BitLocker + service encryption | 5 years (regulatory correspondence) | Retention label auto-delete policy |

---

## 6. RoPA Cross-Reference

| Lineage Path | RoPA Entry | Status |
|-------------|------------|--------|
| COL-001 -> S-001 -> T-001 -> S-002 | ROPA-001: Customer account management | Linked and validated |
| COL-002 -> S-001 -> T-002 -> S-002 | ROPA-002: Mobile app analytics | Linked and validated |
| COL-003 -> S-004 -> T-005 | ROPA-003: Employee administration | Linked and validated |
| T-001 -> F-007 -> CRM | ROPA-006: CRM integration | Linked and validated |
| COL-005 -> F-008 -> Support Provider | ROPA-007: Customer support | Linked and validated |
| S-001 -> F-006 -> S-003 | ROPA-001: Backup sub-activity | Linked, backup retention noted as longer than production |

---

## 7. Compliance Gap Analysis

| Gap ID | Severity | Description | Remediation | Owner | Deadline |
|--------|----------|-------------|-------------|-------|----------|
| GAP-001 | Medium | Backup retention (4 years) exceeds production retention (3 years) for customer data | Reduce backup rotation to 3 years or document justification for extended backup retention | Infrastructure Team | 2026-04-30 |
| GAP-002 | Low | Analytics DW lineage node missing explicit RoPA linkage for aggregated metrics output | Create ROPA sub-entry for anonymized analytics output or document anonymization exemption | Data Governance | 2026-04-15 |

---

## 8. DSAR Response Coverage

| Right | Systems in Scope | Estimated Response Time |
|-------|-----------------|------------------------|
| Art. 15 Access | S-001 (Production DB), S-002 (Analytics DW), S-004 (HR DB), S-005 (Email Archive), CRM | 5 business days for automated extract, 10 days for manual review |
| Art. 17 Erasure | S-001 (Production DB), S-002 (Analytics DW), CRM, Support platform | 3 business days for primary systems, S-003 (backups) within next rotation cycle (max 4 years) |
| Art. 20 Portability | S-001 (consent/contract data only) | 2 business days for JSON/CSV export |

---

## 9. Validation Record

| Validation Date | Validator | Method | Findings |
|----------------|-----------|--------|----------|
| 2026-01-15 | Data Governance Team | Automated lineage discovery (Airflow metadata + BigQuery INFORMATION_SCHEMA) | 2 new data flows discovered, added to documentation |
| 2026-02-12 | Architecture Team | Manual review of system interconnections | Confirmed all documented flows match current architecture |
| 2026-03-10 | DPO Office | Cross-reference against RoPA register | All active processing activities have corresponding lineage paths |

**Next Scheduled Validation**: 2026-04-15 (Q2 quarterly review)

---

## 10. Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Data Protection Officer | Dr. James Whitfield | 2026-03-14 | Approved |
| Chief Data Officer | Michael Chen | 2026-03-14 | Approved |
| Head of Infrastructure | Sarah Mitchell | 2026-03-14 | Approved |
| Head of Information Security | Robert Okafor | 2026-03-14 | Approved |
