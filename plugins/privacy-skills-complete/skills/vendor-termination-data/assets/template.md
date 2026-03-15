# Vendor Termination Data — Return and Deletion Record

## Termination Information

| Field | Value |
|-------|-------|
| **Vendor Name** | [Vendor Legal Name] |
| **DPA Reference** | [DPA-YYYY-XX-NNN] |
| **Termination Trigger** | [Expiry / Convenience / Cause / Migration / Insolvency] |
| **Controller Election** | [Return Only / Delete Only / Return Then Delete] |
| **Initiated Date** | [YYYY-MM-DD] |
| **Return Deadline** | [YYYY-MM-DD] |
| **Deletion Deadline** | [YYYY-MM-DD] |
| **Current Phase** | [Phase] |

## Data Inventory

| # | Category | Location | Format | Volume | Deletion Method | Status |
|---|----------|----------|--------|--------|----------------|--------|
| 1 | [Category] | [Location] | [Format] | [Vol] | [Method] | [Pending/Complete] |

## Data Return Record

| Field | Value |
|-------|-------|
| **Categories Returned** | [List] |
| **Format** | [CSV / JSON / etc.] |
| **Transfer Method** | [SFTP / API / Media] |
| **Record Count** | [Number] |
| **Checksum (SHA-256)** | [Hash] |
| **Transfer Date** | [YYYY-MM-DD] |
| **Validated** | [Yes / No] |
| **Validation Notes** | [Notes] |

## Deletion Certification

| Field | Value |
|-------|-------|
| **Certifying Officer** | [Name, Title] |
| **Certification Date** | [YYYY-MM-DD] |
| **Locations Covered** | [List all locations] |
| **Deletion Methods** | [List methods used] |
| **Sub-Processors Confirmed** | [List sub-processors] |
| **Exceptions** | [Legal retention, if any] |
| **Certification Accepted** | [Yes / No] |
| **Review Notes** | [Notes] |

## Approvals

| Role | Name | Date |
|------|------|------|
| Privacy Team | [Name] | [Date] |
| DPO | [Name] | [Date] |

---

*Per GDPR Article 28(3)(g) and Summit Cloud Partners Vendor Termination Data Policy.*
