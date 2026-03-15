---
name: processor-ropa-creation
description: >-
  Creates GDPR Article 30(2) Records of Processing Activities for data
  processors with all four mandatory fields: processor and controller names
  and contact details, categories of processing, third country transfers,
  and security measures description. Activate for processor RoPA, Art. 30(2),
  processor records, sub-processor documentation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, article-30, ropa, processor, processing-records, sub-processor, dpa"
---

# Processor RoPA Creation

## Overview

GDPR Article 30(2) imposes an independent obligation on every processor to maintain a record of all categories of processing activities carried out on behalf of each controller. Unlike controller records under Art. 30(1), processor records are scoped to the processing performed under the controller's instructions and contain four mandatory fields. This skill provides the complete methodology for creating and maintaining processor RoPA entries that satisfy Art. 30(2)(a) through (d).

The processor obligation is independently enforced. The Spanish AEPD sanctioned a processor under PS/00547/2021 for failure to maintain Art. 30(2) records, confirming that compliance is not derivative of the controller's own record-keeping.

## Mandatory Field Requirements — Art. 30(2)

### Field 1: Processor and Controller Identity — Art. 30(2)(a)

This field must identify:

- **Processor legal entity name**: Registered name as it appears in the national business register.
- **Processor contact details**: General contact email and telephone for data protection matters.
- **Each controller on whose behalf the processor acts**: Legal entity name and contact details of every controller whose data the processor processes.
- **Controller's representative (if applicable)**: Where the controller is established outside the EEA and has appointed an Art. 27 representative.
- **DPO**: Contact details of the DPO of both the processor and each controller (if appointed).

**Example for Helix Biotech Solutions acting as a processor:**

Helix Biotech Solutions GmbH provides laboratory information management system (LIMS) hosting services to external pharmaceutical companies.

| Sub-field | Value |
|-----------|-------|
| Processor legal entity | Helix Biotech Solutions GmbH |
| Processor registered address | Leopoldstrasse 42, 80802 Munich, Germany |
| Processor registration | HRB 267891, Amtsgericht Munich |
| Processor contact email | processor-privacy@helix-biotech.eu |
| Processor DPO | Dr. Elena Voss, dpo@helix-biotech.eu |
| Controller 1 | Meridian Pharma AG, Bahnhofstrasse 15, 8001 Zurich, Switzerland |
| Controller 1 DPO | Thomas Keller, dpo@meridian-pharma.ch |
| Controller 1 EU representative | Meridian Pharma EU Representative Ltd, Dublin, Ireland (Art. 27 representative for non-EEA controller) |
| Controller 2 | NovaCure Therapeutics S.A., Avenue Louise 54, 1050 Brussels, Belgium |
| Controller 2 DPO | Marie Dupont, dpo@novacure.eu |
| Art. 28 DPA reference (Controller 1) | DPA-2024-MER-001, executed 2024-05-15 |
| Art. 28 DPA reference (Controller 2) | DPA-2024-NOV-002, executed 2024-08-22 |

### Field 2: Categories of Processing — Art. 30(2)(b)

Document the categories of processing carried out on behalf of each controller. This must describe what the processor actually does with the data, not the controller's broader processing purposes.

**Processing categories must be documented per controller:**

| Controller | Processing Categories | Description |
|------------|----------------------|-------------|
| Meridian Pharma AG | LIMS data hosting and management | Hosting of laboratory test results, sample tracking data, and quality control records on Helix cloud infrastructure. Includes database management, backup, disaster recovery, and system administration. |
| Meridian Pharma AG | Technical support | Troubleshooting and resolving LIMS system issues requiring access to data records. Access logged and time-limited. |
| NovaCure Therapeutics S.A. | LIMS data hosting and management | Hosting of pre-clinical and Phase I clinical laboratory data on dedicated Helix cloud tenant. Includes database management, backup, and disaster recovery. |
| NovaCure Therapeutics S.A. | Data migration | One-time migration of legacy laboratory data from NovaCure on-premises systems to Helix cloud platform. Completed 2024-10-15, data access revoked post-migration. |

**Key distinctions:**

- Processor records describe what the processor does (hosting, storing, transmitting, deleting), not why the controller collects the data.
- Each controller must have separately documented processing categories, even if the categories are identical in practice.
- Time-limited processing (such as migration projects) should include start and end dates.

### Field 3: International Transfers — Art. 30(2)(c)

Record every transfer of personal data to a third country or international organisation that occurs as part of the processor's activities. This includes:

- Transfers by the processor itself (e.g., using sub-processors in third countries)
- Transfers resulting from remote access by support staff in third countries
- Transfers to the controller if the controller is in a third country

**Example:**

| Controller | Destination | Recipient | Data | Safeguard | TIA Ref |
|-----------|-------------|-----------|------|-----------|---------|
| Meridian Pharma AG | Switzerland | Meridian Pharma AG (controller) | Laboratory results and QC data | Swiss adequacy decision (Art. 45) — European Commission Implementing Decision 2000/518/EC as maintained | N/A (adequacy) |
| NovaCure Therapeutics S.A. | India | Wipro Ltd (sub-processor — IT infrastructure support) | System metadata, incidental access to hosted data during support | EU SCCs Module 3 (processor-to-sub-processor), executed 2024-07-01 | TIA-2024-WIPRO-004 |

**Sub-processor transfers**: When the processor engages sub-processors in third countries, the processor must document these transfers in its Art. 30(2) record even though the controller's Art. 28 authorisation and Art. 30(1)(e) record should also reflect them.

### Field 4: Security Measures — Art. 30(2)(d)

Provide a general description of the technical and organisational security measures implemented by the processor under Art. 32(1). This description should reflect the measures the processor actually applies to protect the controller's data.

**Example security measures description:**

> **Technical measures**: Multi-tenant cloud infrastructure with logical tenant isolation using dedicated database schemas per controller. AES-256 encryption at rest (AWS KMS managed keys, per-controller keys). TLS 1.3 for all data in transit. Network segmentation with dedicated VPCs per tenant. Role-based access control with quarterly access reviews. Multi-factor authentication for all administrative and data access. Immutable audit logging with 2-year retention (AWS CloudTrail). Daily automated backups with cross-region replication and quarterly restore testing. Vulnerability scanning (weekly) and penetration testing (annually by NCC Group). Endpoint detection and response on all employee workstations.
>
> **Organisational measures**: ISO 27001:2022 certified (certificate ref: IS 891245, scope includes LIMS hosting services). SOC 2 Type II audit completed annually (latest report: 2025-Q3). All staff with data access have completed background checks, signed confidentiality agreements, and undergo annual data protection training. Incident response procedure with 24-hour initial assessment and controller notification per Art. 33(2). Sub-processor management programme with security assessments prior to engagement and annual re-assessment. Data processing restricted to documented controller instructions per Art. 28(3)(a).

## Processor RoPA vs Controller RoPA

| Aspect | Controller RoPA (Art. 30(1)) | Processor RoPA (Art. 30(2)) |
|--------|------------------------------|------------------------------|
| Number of mandatory fields | 7 (a through g) | 4 (a through d) |
| Purposes documented | Yes — controller's processing purposes | No — only processing categories (what is done, not why) |
| Data subject categories | Yes | No — not required, though often included for completeness |
| Personal data categories | Yes | No — not required, though often included for completeness |
| Recipient categories | Yes | No — sub-processors are documented in the DPA, not necessarily in the Art. 30(2) record |
| Retention periods | Yes | No — retention is the controller's responsibility |
| International transfers | Yes | Yes |
| Security measures | Yes | Yes |

## Per-Controller Record Separation

A processor must maintain separate documentation for each controller. In practice, this means:

1. **Separate records per controller**: Even if the processing activities are identical (e.g., hosting LIMS for multiple pharmaceutical clients), each controller must have its own entry documenting the processor-controller relationship, processing categories, transfers, and applicable security measures.

2. **Shared infrastructure documentation**: Where security measures are identical across controllers (same infrastructure, same controls), the security measures description may reference a common security practices document, but each controller's record must include or reference this description.

3. **Controller-specific nuances**: Different controllers may have different instructions, different data types, different sub-processor authorisations, or different transfer requirements. Capture these differences in each controller's record.

## Sub-Processor Documentation

When the processor engages sub-processors under Art. 28(2)/(4), the processor's RoPA should reflect:

| Sub-Processor | Controller(s) Affected | Processing Activity | Location | Art. 28 DPA | Authorisation Type |
|---------------|----------------------|---------------------|----------|-------------|-------------------|
| Amazon Web Services EMEA SARL | All controllers | Cloud infrastructure hosting (IaaS) | Frankfurt, Germany (eu-central-1) | DPA-2024-AWS-001 | General written authorisation with notification obligation |
| Wipro Ltd | NovaCure Therapeutics S.A. | IT infrastructure support and monitoring | Bangalore, India | DPA-2024-WIPRO-003 | Specific written authorisation per controller |
| Datadog Inc. | All controllers | Application performance monitoring and logging | EU region (Dublin) | DPA-2024-DD-001 | General written authorisation with notification obligation |

## Common Processor RoPA Mistakes

1. **Not maintaining Art. 30(2) records at all**: Many processors assume only controllers need RoPA. Art. 30(2) is an independent obligation with independent enforcement.

2. **Documenting the controller's purposes instead of processing categories**: The processor records what it does (hosts, stores, backs up, transmits), not why the controller collects the data.

3. **Single record for all controllers**: Each controller relationship must be separately documented, even if processing is identical.

4. **Missing sub-processor transfers**: When a sub-processor is located in a third country, the resulting international transfer must be documented in the processor's Art. 30(2)(c) field.

5. **Copying the controller's security description**: The processor must describe its own security measures, which may differ from the controller's. The processor's controls protect the data during processing, which may involve different infrastructure, different access patterns, and different threat models.

6. **Ignoring the Art. 30(5) exemption limitations**: Even small processors must maintain Art. 30(2) records if the processing is not occasional, involves special category data, or is likely to result in a risk to data subjects' rights. In practice, any processor providing ongoing services (hosting, payroll processing, cloud services) is processing non-occasionally and must maintain records regardless of employee count.
