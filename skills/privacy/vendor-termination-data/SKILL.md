---
name: vendor-termination-data
description: >-
  Vendor termination data return and deletion procedures per GDPR Article
  28(3)(g). Covers data extraction formats, deletion certification requirements,
  transition planning, residual data handling, and post-termination verification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-termination, data-return, deletion-certification, art-28-termination, data-portability"
---

# Vendor Termination Data Return and Deletion

## Overview

GDPR Article 28(3)(g) requires that at the choice of the controller, the processor shall "delete or return all the personal data to the controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data." This termination obligation ensures that personal data does not persist at a former processor beyond the legitimate processing period.

The EDPB Guidelines 07/2020 (paragraph 108) emphasize that this obligation extends to all copies, backups, and derived data — not just production data. The deletion must be verifiable, and the controller should obtain written certification.

At Summit Cloud Partners, the Vendor Termination Data Protocol provides a structured process for managing data return and deletion when vendor relationships end.

## Termination Triggers

| Trigger | Description | Timeline Considerations |
|---------|-------------|----------------------|
| Contract expiry (non-renewal) | MSA/DPA term ends without renewal | 90-day notice per DPA |
| Termination for convenience | Controller elects to terminate | Per MSA notice period |
| Termination for cause | Material DPA breach by processor | Immediate or per cure period |
| Service migration | Controller moves to alternative provider | Overlap period for data migration |
| Vendor insolvency | Processor enters insolvency proceedings | Emergency data retrieval |
| Regulatory order | Supervisory authority orders cessation | Per order timeline |

## Data Return Process

### Step 1: Data Inventory and Mapping

Before initiating return, confirm the complete scope of personal data held by the processor:

| Data Category | Location | Format | Volume | Retention Basis |
|--------------|----------|--------|--------|----------------|
| Production data | Primary database | Structured (SQL/JSON) | [Volume] | DPA processing |
| Backup data | Backup storage | Encrypted backup files | [Volume] | Business continuity per DPA |
| Log data | Log storage | Semi-structured (JSON/text) | [Volume] | Security monitoring |
| Derived/aggregated data | Analytics system | Structured | [Volume] | Processing output |
| Metadata | Various systems | Structured | [Volume] | System operation |
| Cached data | CDN/cache layers | Various | [Volume] | Performance |

### Step 2: Data Export Format and Method

**Standard Export Formats:**

| Data Type | Preferred Format | Alternative Format | Notes |
|-----------|-----------------|-------------------|-------|
| Structured data | CSV with defined schema | JSON, XML, Parquet | UTF-8 encoding required |
| Documents | Original format (PDF, DOCX) | ZIP archive | Preserve directory structure |
| Images/media | Original format (PNG, JPEG) | ZIP archive | Preserve metadata |
| Logs | JSON lines (JSONL) | CSV | Include timestamps |
| API-accessible data | Direct API extraction | Bulk export endpoint | Paginated if large |

**Export Methods:**

| Method | When to Use | Security Requirements |
|--------|-----------|----------------------|
| Encrypted file transfer (SFTP) | Large datasets | TLS 1.2+, PGP encryption |
| Secure API extraction | Structured, API-accessible data | OAuth 2.0, TLS 1.3 |
| Encrypted portable media | Very large datasets without bandwidth | AES-256 encryption, tracked courier |
| Cloud-to-cloud migration | Cloud provider transition | Encrypted transfer, access audit |

### Step 3: Data Validation

Upon receiving returned data, Summit Cloud Partners validates:

| Validation Check | Method | Pass Criteria |
|-----------------|--------|---------------|
| Completeness | Record count comparison | Returned count matches source count |
| Integrity | Checksum verification (SHA-256) | Checksums match vendor-provided manifest |
| Format compliance | Schema validation | All fields present per agreed schema |
| Encoding | Character encoding verification | UTF-8 without corruption |
| Sample verification | Random sample manual review | Data content matches expectations |

## Data Deletion Process

### Deletion Scope

The processor must delete ALL copies of personal data, including:

1. **Production data** — Primary databases and data stores
2. **Backup data** — All backup copies including off-site backups
3. **Disaster recovery copies** — DR site data
4. **Log data** — Application logs, access logs, audit logs containing personal data
5. **Cached data** — CDN caches, application caches, database caches
6. **Derived data** — Analytics outputs, aggregated data containing personal data
7. **Metadata** — System metadata referencing personal data
8. **Archived data** — Any archived copies
9. **Sub-processor data** — Data at all sub-processors

### Deletion Methods

| Data Location | Deletion Method | Verification |
|--------------|----------------|--------------|
| Databases (SQL) | DELETE + VACUUM or DROP TABLE | Query confirmation; storage analysis |
| Object storage (S3/Blob) | Delete all objects + bucket | Bucket listing verification |
| File systems | Secure overwrite (NIST 800-88) | Disk analysis confirmation |
| SSD/Flash storage | Crypto-erase (destroy encryption key) | Vendor attestation |
| Backup tapes | Degaussing or physical destruction | Destruction certificate |
| Application caches | Cache flush + TTL expiry confirmation | Application verification |
| Log systems | Targeted log deletion or retention expiry | Log query confirmation |
| Sub-processors | Cascade deletion instruction | Sub-processor deletion certificate |

### Deletion Timeline

| Phase | Activity | DPA Standard Timeline |
|-------|----------|----------------------|
| T+0 | Controller elects deletion (or return + deletion) | Upon termination notice |
| T+0 to T+30 | Data return completed (if return elected) | 30 calendar days |
| T+30 to T+60 | Production data deletion | 60 calendar days from termination |
| T+60 to T+90 | Backup and archive deletion | 90 calendar days from termination |
| T+90 | Deletion certification issued | 90 calendar days from termination |

### Deletion Exceptions

Article 28(3)(g) permits continued storage where "Union or Member State law requires storage of the personal data." Exceptions must be:

| Requirement | Processor Action |
|------------|-----------------|
| Documented in writing | Processor identifies specific legal requirement |
| Limited to required data | Only data subject to legal retention requirement |
| Isolated from production | Retained data moved to restricted storage |
| Time-limited | Retained only for legally required duration |
| Notified to controller | Controller informed of retention and legal basis |

## Deletion Certification

The processor must provide a written deletion certification containing:

| Field | Content |
|-------|---------|
| Certifying party | Name and title of authorized processor representative |
| Controller name | Summit Cloud Partners |
| DPA reference | Reference to terminated DPA |
| Deletion scope | Description of all data deleted (categories, locations, formats) |
| Deletion date(s) | Date each deletion action was completed |
| Deletion method(s) | Technical method used for each data location |
| Sub-processor deletion | Confirmation that all sub-processors have also deleted data |
| Exceptions | Any data retained under legal obligation (with legal basis citation) |
| Certification date | Date of certification |
| Signature | Authorized officer signature |

## Transition Planning

For service migrations, a transition plan ensures continuity while managing data protection obligations:

| Phase | Activity | Duration |
|-------|----------|----------|
| **Planning** | Define data migration scope, format, timeline | 4-6 weeks |
| **Parallel operation** | Old and new vendor operate simultaneously | 2-4 weeks |
| **Migration** | Data transferred from old to new vendor | 1-2 weeks |
| **Validation** | Verify complete and accurate migration | 1 week |
| **Cutover** | Switch production to new vendor | 1 day |
| **Decommission** | Terminate old vendor; initiate deletion | Per DPA timeline |
| **Deletion verification** | Confirm old vendor data deletion | 90 days |

## Key Regulatory References

- GDPR Article 28(3)(g) — Deletion or return of personal data upon termination
- GDPR Article 17 — Right to erasure (informs deletion standards)
- GDPR Article 5(1)(e) — Storage limitation principle
- EDPB Guidelines 07/2020 — Paragraph 108 on termination data obligations
- NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization
- ISO/IEC 27001:2022 — A.8.10 Information deletion
