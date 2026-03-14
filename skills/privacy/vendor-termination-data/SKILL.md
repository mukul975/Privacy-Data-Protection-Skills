---
name: vendor-termination-data
description: >-
  Vendor termination data return and deletion per GDPR Article 28(3)(g). Covers
  data extraction format requirements, certified deletion procedures, transition
  planning, residual data handling, and post-termination verification.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-termination, data-return, data-deletion, art-28-termination, transition-planning"
---

# Vendor Termination Data Return and Deletion

## Overview

GDPR Article 28(3)(g) requires that "at the choice of the controller, [the processor shall] delete or return all the personal data to the controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data." This provision ensures controllers retain control over personal data throughout the vendor lifecycle, including at termination.

The obligation covers all personal data processed under the DPA — not just primary datasets, but also derived data, backup copies, logs containing personal data, cached data, and any copies held by the processor's sub-processors. The EDPB Guidelines 07/2020 emphasize that this obligation must be practical and enforceable, with specific procedures and timelines documented in the DPA.

At Summit Cloud Partners, the Vendor Termination Data Protocol establishes a structured process for data return, verified deletion, and safe transition when a vendor relationship ends.

## Termination Scenarios

| Scenario | Trigger | Timeline | Priority |
|----------|---------|----------|----------|
| Planned termination | Contract expiry, non-renewal | 90-day DPA window | Standard |
| Early termination (convenience) | Business decision to end service | Per MSA notice period + 90-day DPA window | Standard |
| Termination for cause | DPA breach, audit failure, vendor breach | Expedited — per DPA emergency provisions | High |
| Vendor insolvency | Vendor bankruptcy or cessation | Immediate — maximum urgency | Critical |
| Service migration | Transition to replacement vendor | Overlapping with new vendor onboarding | Standard |

## Data Return Requirements

### Controller Choice: Return vs. Delete

Article 28(3)(g) gives the controller the choice between data return and deletion. At Summit Cloud Partners, the default is: **return first, then delete** — ensuring data is safely received before directing deletion.

### Data Return Specifications

**Format Requirements:**

| Aspect | Requirement |
|--------|-------------|
| File format | Machine-readable, commonly used format (CSV, JSON, XML, Parquet, or database dump) |
| Character encoding | UTF-8 |
| Structure | Documented schema with field descriptions |
| Completeness | All personal data categories per DPA Annex I |
| Integrity verification | SHA-256 checksums for all exported files |
| Encryption | AES-256 encrypted during transfer; encryption keys delivered via separate secure channel |
| Transfer method | SFTP, encrypted API endpoint, or secure cloud storage (mutually agreed) |
| Transfer authentication | MFA-protected credentials |

**Return Data Scope:**

| Data Type | Included in Return? | Notes |
|-----------|:------------------:|-------|
| Primary operational data | Yes | All personal data processed per DPA |
| Derived/aggregated data containing personal data | Yes | Analytics outputs, reports with personal data |
| Backup copies | Not returned — deleted | Deletion verification required |
| System logs containing personal data | Not returned — deleted | Deletion verification required |
| Cached data | Not returned — deleted | Deletion verification required |
| Metadata with personal data elements | Yes | Configuration data, user profiles |
| Sub-processor held data | Via processor | Processor coordinates sub-processor return/deletion |

### Return Verification

| Step | Action | Evidence |
|------|--------|---------|
| 1 | Receive exported data from vendor | Transfer receipt confirmation |
| 2 | Verify completeness against DPA Annex I data categories | Completeness checklist |
| 3 | Verify integrity via SHA-256 checksums | Checksum verification log |
| 4 | Validate data structure against documented schema | Validation report |
| 5 | Sample verification — compare records against known data | Sample check results |
| 6 | Import into Summit systems or archive | Import confirmation |
| 7 | Confirm receipt to vendor | Written confirmation |

## Data Deletion Requirements

### Deletion Standards

| Data Location | Deletion Method | Verification |
|--------------|----------------|-------------|
| Primary storage (SSD) | Cryptographic erasure (destroy encryption keys) or NIST SP 800-88 Clear/Purge | Vendor certification |
| Primary storage (HDD) | NIST SP 800-88 Purge or Destroy | Vendor certification |
| Backup media | Overwrite on next backup cycle or physical destruction | Vendor certification with timeline |
| Cloud storage | Provider deletion API + encryption key destruction | Provider deletion confirmation |
| Logs containing personal data | Log rotation with deletion or anonymization | Vendor certification |
| Cached data | Cache flush and verification | Vendor certification |
| Sub-processor storage | Sub-processor-specific deletion per cascaded DPA | Sub-processor certification via processor |
| Development/test environments | Full deletion if containing production personal data | Vendor certification |

### Deletion Timeline

| Data Type | Deletion Deadline | Standard |
|-----------|------------------|----------|
| Primary operational data | Within 30 days of return confirmation | DPA standard |
| Backup copies | Within 90 days of termination (next rotation cycle) | DPA standard |
| Logs | Within 90 days or upon standard log rotation | DPA standard |
| Cached data | Within 7 days of termination | DPA standard |
| Sub-processor data | Within 60 days of termination | DPA standard |
| All residual copies | Within 90 days of termination | DPA maximum |

### Deletion Certification

The vendor must provide a written deletion certification signed by an authorized officer:

**Required Certification Content:**

| Element | Description |
|---------|-------------|
| Certification date | Date deletion was completed |
| Scope | Confirmation that ALL personal data per DPA has been deleted |
| Locations | List of all storage locations from which data was deleted |
| Methods | Deletion methods used per data type |
| Sub-processors | Confirmation that sub-processor deletion has been completed or is in progress with timeline |
| Retained data | If any data retained per legal obligation — identify the data, legal basis, and expected deletion date |
| Authorized signatory | Name, title, and signature of authorized vendor officer |

## Transition Planning

### Pre-Termination Transition Checklist

| # | Action | Responsible | Timeline |
|---|--------|-------------|----------|
| 1 | Notify vendor of termination / non-renewal | Legal/Business Owner | Per MSA notice period |
| 2 | Invoke DPA Article 28(3)(g) — specify return or delete choice | Privacy Team | With termination notice |
| 3 | Agree on data export format and transfer method | Privacy Team + Vendor | 15 days after notice |
| 4 | Vendor provides data export timeline | Vendor | 15 days after notice |
| 5 | Prepare internal systems to receive returned data | IT Team | Before data transfer |
| 6 | Vendor executes data export | Vendor | Per agreed timeline |
| 7 | Summit verifies returned data | Privacy Team + IT | Within 5 days of receipt |
| 8 | Summit confirms receipt to vendor | Privacy Team | Upon verification |
| 9 | Vendor executes deletion | Vendor | Per DPA deletion timeline |
| 10 | Vendor provides deletion certification | Vendor | Within 7 days of deletion |
| 11 | Summit reviews deletion certification | Privacy Team | Within 5 days |
| 12 | Close vendor record in register | Privacy Team | Upon certification acceptance |

### Residual Data Handling

After primary deletion, residual personal data may exist in:

| Location | Risk | Mitigation |
|----------|------|-----------|
| Backup tapes/archives | Data may persist until tape rotation | Require confirmation of backup deletion with specific timeline |
| Disaster recovery sites | Replicated data may persist | Include DR sites in deletion scope |
| Log aggregation systems | Personal data in operational logs | Require log anonymization or deletion |
| Analytics platforms | Derived data sets | Require deletion of all derived data containing personal data |
| Email/communications | Personal data in support tickets, emails | Require deletion from communication systems |
| Vendor employee devices | Data downloaded to laptops/devices | Require confirmation of device-level deletion |

## Key Regulatory References

- GDPR Article 28(3)(g) — Data return or deletion upon termination
- GDPR Article 17(1) — Right to erasure (applies to processor-held data)
- GDPR Article 5(1)(e) — Storage limitation principle
- EDPB Guidelines 07/2020 — Paragraph 108-110 on practical enforceability of deletion
- NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization
- ISO/IEC 27040:2015 — Storage security, including data sanitization
