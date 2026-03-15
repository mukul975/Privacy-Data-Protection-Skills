# Processor RoPA Entry — Helix Biotech Solutions GmbH

**Record ID**: RPP-2025-LAB-001
**Service Name**: Laboratory Information Management System (LIMS) Hosting
**Record Type**: Processor (GDPR Art. 30(2))
**Date Created**: 2023-09-01
**Last Reviewed**: 2025-02-15
**Next Review Due**: 2026-02-15
**Record Owner**: Marcus Steiner, VP Cloud Operations

---

## Art. 30(2)(a) — Processor Identity

| Field | Value |
|-------|-------|
| **Processor legal name** | Helix Biotech Solutions GmbH |
| **Registered address** | Leopoldstrasse 42, 80802 Munich, Germany |
| **Registration** | HRB 267891, Amtsgericht Munich |
| **Contact email** | processor-privacy@helix-biotech.eu |
| **DPO** | Dr. Elena Voss, dpo@helix-biotech.eu, +49 89 7654 3210 |

---

## Art. 30(2)(a) — Controllers Served

| # | Controller Legal Name | Address | Contact | DPO | EU Representative | DPA Reference | DPA Expiry |
|---|----------------------|---------|---------|-----|-------------------|---------------|------------|
| 1 | Universitaetsklinikum Heidelberg | Im Neuenheimer Feld 672, 69120 Heidelberg, Germany | datenschutz@med.uni-heidelberg.de | Prof. Dr. Klaus Weber, dsb@med.uni-heidelberg.de | N/A (EEA established) | DPA-2023-UKH-001 | 2026-08-31 |
| 2 | Charite Universitaetsmedizin Berlin | Chariteplatz 1, 10117 Berlin, Germany | datenschutz@charite.de | Dr. Maria Hoffmann, dsb@charite.de | N/A (EEA established) | DPA-2024-CHB-002 | 2027-03-15 |
| 3 | Centre Hospitalier Universitaire de Strasbourg | 1 Place de l'Hopital, 67091 Strasbourg, France | dpo@chru-strasbourg.fr | Jean-Pierre Laurent, dpo@chru-strasbourg.fr | N/A (EEA established) | DPA-2024-CHS-003 | 2027-06-30 |

---

## Art. 30(2)(b) — Categories of Processing

### Controller 1: Universitaetsklinikum Heidelberg

| # | Processing Category | Description | Start Date | End Date |
|---|---------------------|-------------|------------|----------|
| 1 | LIMS data hosting and storage | Hosting of laboratory test orders, patient sample metadata, and diagnostic results on Helix Cloud (Frankfurt, eu-central-1) | 2023-09-01 | Ongoing |
| 2 | Backup and disaster recovery | Daily encrypted backups of LIMS databases with cross-region replication to Dublin (eu-west-1) | 2023-09-01 | Ongoing |
| 3 | Technical support (Tier 2/3) | Troubleshooting and resolving technical issues requiring access to production LIMS data, under break-glass procedure | 2023-09-01 | Ongoing |

### Controller 2: Charite Universitaetsmedizin Berlin

| # | Processing Category | Description | Start Date | End Date |
|---|---------------------|-------------|------------|----------|
| 1 | LIMS data hosting and storage | Hosting of pathology laboratory data including tissue sample tracking and histology results | 2024-01-15 | Ongoing |
| 2 | Backup and disaster recovery | Daily encrypted backups with cross-region replication | 2024-01-15 | Ongoing |
| 3 | Data migration | One-time migration of legacy LIMS data from on-premises Oracle database to Helix Cloud | 2024-01-15 | 2024-04-30 |

### Controller 3: Centre Hospitalier Universitaire de Strasbourg

| # | Processing Category | Description | Start Date | End Date |
|---|---------------------|-------------|------------|----------|
| 1 | LIMS data hosting and storage | Hosting of clinical chemistry and microbiology laboratory results | 2024-07-01 | Ongoing |
| 2 | Backup and disaster recovery | Daily encrypted backups with cross-region replication | 2024-07-01 | Ongoing |

---

## Sub-Processors

| # | Sub-Processor | Location | Service | Controllers Affected | DPA Reference | Authorisation Type | Authorisation Date |
|---|--------------|----------|---------|---------------------|---------------|-------------------|-------------------|
| 1 | Amazon Web Services EMEA SARL | Luxembourg (hosting in Frankfurt eu-central-1 and Dublin eu-west-1) | IaaS infrastructure for Helix Cloud platform (compute, storage, networking) | All controllers | DPA-2023-AWS-001 | General (with 30-day objection period per DPA clause 7.3) | 2023-08-01 |
| 2 | Datadog EU B.V. | Amsterdam, Netherlands | Infrastructure monitoring and log management (no patient data — metadata only: request counts, latency, error rates) | All controllers | DPA-2024-DD-001 | General (with 30-day objection period) | 2024-03-01 |
| 3 | PagerDuty Ireland Ltd. | Dublin, Ireland | Incident alerting and on-call management (alert metadata only: timestamp, severity, service name) | All controllers | DPA-2024-PD-002 | General (with 30-day objection period) | 2024-05-15 |

---

## Art. 30(2)(c) — International Transfers

| # | Controller | Destination Country | Recipient Entity | Data Transferred | Transfer Mechanism | TIA Reference |
|---|-----------|-------------------|-----------------|------------------|-------------------|---------------|
| 1 | All controllers | United States | Datadog Inc. (parent of Datadog EU B.V.) | Infrastructure metadata only (no patient data): server metrics, request latency, error logs with patient identifiers stripped | EU-US Data Privacy Framework (Datadog Inc. DPF certified) + SCCs Module 3 as fallback | TIA-2024-DD-US-001 |
| 2 | All controllers | United States | PagerDuty Inc. (parent of PagerDuty Ireland Ltd.) | Alert metadata only: timestamp, severity level, service name (no personal data content) | EU-US Data Privacy Framework (PagerDuty Inc. DPF certified) + SCCs Module 3 as fallback | TIA-2024-PD-US-002 |

---

## Art. 30(2)(d) — Technical and Organisational Security Measures

### Technical Measures

- **Encryption at rest**: AES-256 with per-controller encryption keys via AWS Key Management Service; customer-managed keys (CMK) option available
- **Encryption in transit**: TLS 1.3 for all API and web traffic; mutual TLS (mTLS) for inter-service communication within Helix Cloud
- **Tenant isolation**: Dedicated PostgreSQL schemas per controller with row-level security; separate AWS VPCs per production environment; network ACLs preventing cross-tenant traffic
- **Access control**: RBAC with named-user accounts; principle of least privilege; break-glass procedure for production access requiring DPO pre-approval and 48-hour access window
- **Authentication**: MFA for all administrative access via Okta; hardware security keys (YubiKey 5) for production system administrators
- **Audit logging**: Immutable audit trail via AWS CloudTrail and application-level logging; 2-year retention; tamper-evident log integrity verification via SHA-256 hash chains
- **Backup**: Daily encrypted snapshots with 30-day retention in primary region (Frankfurt); cross-region replication to Dublin with 7-day retention; quarterly restore testing documented in QRT log
- **Vulnerability management**: Weekly automated scanning via Qualys; annual penetration testing by Cure53 GmbH (latest report: PT-2024-HC-019, dated 2024-10-22); critical vulnerabilities patched within 24 hours per SLA
- **Endpoint security**: CrowdStrike Falcon EDR on all employee workstations and administrative jump hosts

### Organisational Measures

- **Certifications**: ISO 27001:2022 (cert ref: IS 891245, TUeV Sued, valid until 2027-03-15); SOC 2 Type II (latest report period: 2024-Q3 to 2025-Q2, issued by Deloitte GmbH)
- **Personnel security**: Background checks via First Advantage for all employees with production access; confidentiality agreements signed at onboarding; annual data protection training with role-specific modules for cloud operations team
- **Incident response**: 24-hour initial assessment SLA; controller notification within 36 hours of confirmed personal data breach per Art. 33(2); dedicated incident commander rotation
- **Sub-processor management**: Pre-engagement security assessment using standardised questionnaire (SPA-FORM-2024); annual re-assessment; 30-day advance notification to controllers before new sub-processor engagement
- **Instruction compliance**: All processing restricted to documented controller instructions per Art. 28(3)(a); annual DPA compliance review; controller instruction log maintained in Jira (project: CTRL-INST)

---

## Record Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO | Dr. Elena Voss | 2025-02-15 | E. Voss |
| CISO | Thomas Wehner | 2025-02-17 | T. Wehner |
| Service Owner | Marcus Steiner | 2025-02-18 | M. Steiner |

---

*This record fulfils GDPR Article 30(2) processor obligations. Maintained in electronic form per Art. 30(3). Available to supervisory authorities on request per Art. 30(4).*
