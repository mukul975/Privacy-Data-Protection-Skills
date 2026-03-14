# Processor RoPA Entry Template — Helix Biotech Solutions GmbH

**Record ID**: RPP-[XXX]
**Service Name**: [Name of the processing service provided]
**Record Type**: Processor (GDPR Art. 30(2))
**Date Created**: [YYYY-MM-DD]
**Last Reviewed**: [YYYY-MM-DD]
**Next Review Due**: [YYYY-MM-DD]
**Record Owner**: [Name, Title]

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
| 1 | [Controller name] | [Address] | [Email] | [DPO name, email] | [Rep details or N/A] | [DPA-YYYY-XXX-NNN] | [YYYY-MM-DD] |
| 2 | [Controller name] | [Address] | [Email] | [DPO name, email] | [Rep details or N/A] | [DPA-YYYY-XXX-NNN] | [YYYY-MM-DD] |

---

## Art. 30(2)(b) — Categories of Processing

### Controller 1: [Controller Name]

| # | Processing Category | Description | Start Date | End Date |
|---|---------------------|-------------|------------|----------|
| 1 | [e.g., Data hosting and storage] | [What the processor does with the data] | [YYYY-MM-DD] | [Ongoing / YYYY-MM-DD] |
| 2 | [e.g., Backup and disaster recovery] | [Description] | [YYYY-MM-DD] | [Ongoing / YYYY-MM-DD] |
| 3 | [e.g., Technical support] | [Description] | [YYYY-MM-DD] | [Ongoing / YYYY-MM-DD] |

### Controller 2: [Controller Name]

| # | Processing Category | Description | Start Date | End Date |
|---|---------------------|-------------|------------|----------|
| 1 | [Category] | [Description] | [YYYY-MM-DD] | [Ongoing / YYYY-MM-DD] |

---

## Sub-Processors

| # | Sub-Processor | Location | Service | Controllers Affected | DPA Reference | Authorisation Type | Authorisation Date |
|---|--------------|----------|---------|---------------------|---------------|-------------------|-------------------|
| 1 | [Name] | [City, Country] | [Service description] | [All / Specific controller] | [DPA ref] | [General / Specific] | [YYYY-MM-DD] |

---

## Art. 30(2)(c) — International Transfers

| # | Controller | Destination Country | Recipient Entity | Data Transferred | Transfer Mechanism | TIA Reference |
|---|-----------|-------------------|-----------------|------------------|-------------------|---------------|
| 1 | [Controller name] | [Country] | [Recipient] | [Data description] | [Adequacy / SCCs Module X / BCRs / Art. 49] | [TIA-YYYY-XXX-NNN or N/A] |

**If no international transfers**: No personal data processed on behalf of any controller is transferred outside the European Economic Area.

---

## Art. 30(2)(d) — Technical and Organisational Security Measures

### Technical Measures

- **Encryption at rest**: [e.g., AES-256 with per-controller encryption keys via AWS KMS]
- **Encryption in transit**: [e.g., TLS 1.3 for all data transmission]
- **Tenant isolation**: [e.g., Dedicated database schemas and VPCs per controller]
- **Access control**: [e.g., RBAC with named-user accounts, quarterly reviews]
- **Authentication**: [e.g., MFA for all administrative access]
- **Audit logging**: [e.g., Immutable audit trail via CloudTrail, 2-year retention]
- **Backup**: [e.g., Daily encrypted backups, cross-region replication, quarterly restore tests]
- **Vulnerability management**: [e.g., Weekly automated scanning, annual penetration testing]
- **Endpoint security**: [e.g., EDR on all employee workstations]

### Organisational Measures

- **Certifications**: [e.g., ISO 27001:2022 (cert ref: IS 891245), SOC 2 Type II (latest: 2025-Q3)]
- **Personnel security**: [e.g., Background checks, confidentiality agreements, annual training]
- **Incident response**: [e.g., 24-hour assessment SLA, controller notification per Art. 33(2)]
- **Sub-processor management**: [e.g., Pre-engagement security assessment, annual re-assessment]
- **Instruction compliance**: [e.g., Processing restricted to documented controller instructions per Art. 28(3)(a)]

---

## Record Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO | Dr. Elena Voss | [YYYY-MM-DD] | _________ |
| CISO | [Name] | [YYYY-MM-DD] | _________ |
| Service Owner | [Name] | [YYYY-MM-DD] | _________ |

---

*This record fulfils GDPR Article 30(2) processor obligations. Maintained in electronic form per Art. 30(3). Available to supervisory authorities on request per Art. 30(4).*
