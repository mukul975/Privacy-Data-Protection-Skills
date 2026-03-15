---
name: controller-ropa-creation
description: >-
  Creates GDPR Article 30(1) Records of Processing Activities (RoPA) for data
  controllers with all seven mandatory fields: controller identity and contact
  details, processing purposes, data subject categories, personal data
  categories, recipient categories, third country transfers, and retention
  periods. Includes Python generator for automated RoPA creation. Activate for
  controller RoPA, Art. 30(1), processing records, data mapping.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, article-30, ropa, controller, processing-records, data-mapping, accountability"
---

# Controller RoPA Creation

## Overview

GDPR Article 30(1) requires every controller to maintain a written record of processing activities carried out under its responsibility. This skill provides a complete methodology for creating controller RoPA entries that satisfy all seven mandatory field requirements specified in Art. 30(1)(a) through (g), ensuring the organisation can demonstrate accountability under Art. 5(2) and respond to supervisory authority requests under Art. 30(4).

## Mandatory Field Requirements

### Field 1: Controller Identity and Contact Details — Art. 30(1)(a)

This field must identify:

- **Legal entity name**: The registered name of the controller as it appears in the national business register (e.g., Companies House, Handelsregister, Registre du Commerce).
- **Registered address**: The official registered office address.
- **Contact details**: General contact email and telephone for data protection inquiries.
- **Joint controller(s)**: Where processing is jointly determined under Art. 26, the identity and contact details of each joint controller and a reference to the Art. 26 arrangement.
- **EU Representative**: Where the controller is not established in the EEA, the identity and contact details of the Art. 27 representative.
- **Data Protection Officer**: Name, email, and telephone of the DPO appointed under Art. 37, or a statement that no DPO is required with justification.

**Example for Helix Biotech Solutions:**

| Sub-field | Value |
|-----------|-------|
| Legal entity name | Helix Biotech Solutions GmbH |
| Registered address | Leopoldstraße 42, 80802 Munich, Germany |
| Registration | HRB 267891, Amtsgericht Munich |
| Contact email | privacy@helix-biotech.eu |
| DPO | Dr. Elena Voss, dpo@helix-biotech.eu, +49 89 7654 3210 |
| EU Representative | Not applicable (established in EEA) |
| Joint controllers | None for this processing activity |

### Field 2: Purposes of Processing — Art. 30(1)(b)

Each processing activity must have one or more specific, explicit, and legitimate purposes documented. Purposes must be granular enough to demonstrate compliance with the purpose limitation principle under Art. 5(1)(b).

**Avoid vague purposes such as:**
- "Business operations"
- "Internal use"
- "General purposes"
- "As needed"

**Acceptable purpose examples:**

| Processing Activity | Purpose Statement | Lawful Basis Reference |
|---------------------|-------------------|----------------------|
| Employee payroll | Calculation and disbursement of monthly salaries and statutory deductions under employment contract obligation | Art. 6(1)(b) — contract performance |
| Clinical trial data collection | Recording of participant vital signs, adverse events, and treatment outcomes for Phase III oncology trial protocol HBX-2025-ONC-04 | Art. 6(1)(a) — explicit consent; Art. 9(2)(a) — explicit consent for health data |
| Customer account management | Maintaining customer identity, contact, and billing records to fulfil supply agreements for laboratory reagent orders | Art. 6(1)(b) — contract performance |
| Pharmacovigilance reporting | Collection and assessment of adverse drug reaction reports for submission to EMA under EU Regulation 726/2004 | Art. 6(1)(c) — legal obligation |

### Field 3: Categories of Data Subjects — Art. 30(1)(c)

Identify all groups of individuals whose personal data is processed within each activity. Be exhaustive; omitting a data subject category creates a compliance gap.

**Common categories for a biotech organisation:**

- Employees (permanent and fixed-term)
- Contractors and consultants
- Job applicants
- Clinical trial participants
- Patients (post-market surveillance)
- Healthcare professionals (KOL engagement)
- Suppliers and vendor representatives
- Website visitors
- Shareholders and investors

### Field 4: Categories of Personal Data — Art. 30(1)(c)

For each processing activity, specify the types of personal data collected and processed. Flag special category data under Art. 9(1) and criminal conviction data under Art. 10.

**Example data categories by processing activity:**

| Processing Activity | Personal Data Categories | Special Category (Art. 9) |
|---------------------|-------------------------|--------------------------|
| Employee payroll | Name, employee ID, bank account (IBAN), tax ID, salary grade, working hours | No |
| Clinical trial management | Participant ID, date of birth, sex, medical history, genetic markers, treatment allocation, adverse events | Yes — health data, genetic data |
| Pharmacovigilance | Reporter name, patient initials, age, diagnosis, medication history, adverse reaction description | Yes — health data |
| Visitor management | Name, company affiliation, photo ID, visit date/time, host employee | No |

### Field 5: Categories of Recipients — Art. 30(1)(d)

Document all entities that receive personal data, including:

- **Internal recipients**: Departments or roles with access (HR, Finance, IT)
- **Processors**: Third-party service providers acting under Art. 28 DPA (identify by name and reference the DPA)
- **Joint controllers**: Entities jointly determining purposes under Art. 26
- **Public authorities**: Regulators, tax authorities, law enforcement (identify the legal basis for disclosure)
- **Other controllers**: Independent controllers receiving data (e.g., insurance providers)

**Example:**

| Recipient | Type | DPA/Agreement Reference |
|-----------|------|------------------------|
| SAP SuccessFactors (SAP SE) | Processor | DPA-2024-SAP-001, executed 2024-02-15 |
| ADP Employer Services GmbH | Processor | DPA-2023-ADP-002, executed 2023-09-01 |
| Finanzamt Munich | Public authority | Section 93 AO — tax reporting obligation |
| AOK Bayern | Other controller | Statutory health insurance reporting under SGB V |
| Helix Biotech Solutions Ltd (UK subsidiary) | Intra-group controller | Art. 26 joint controller arrangement, ref: JCA-2024-UK-001 |

### Field 6: International Transfers — Art. 30(1)(e)

Record every transfer of personal data to a third country (outside the EEA) or international organisation. For each transfer, document:

- Destination country
- Recipient entity
- Transfer mechanism relied upon:
  - Adequacy decision under Art. 45 (specify which decision)
  - Standard Contractual Clauses under Art. 46(2)(c) (specify module and execution date)
  - Binding Corporate Rules under Art. 47 (specify approval reference)
  - Derogation under Art. 49 (specify which derogation and why it applies)
- Transfer Impact Assessment reference (required per EDPB Recommendations 01/2020 for SCCs)

**Example:**

| Destination | Recipient | Mechanism | TIA Reference |
|-------------|-----------|-----------|---------------|
| United States | Veeva Systems Inc. | EU-US Data Privacy Framework adequacy decision (10 July 2023) — Veeva listed on DPF List | TIA-2024-VEEVA-001 |
| United Kingdom | Helix Biotech Solutions Ltd | UK adequacy decision (28 June 2021, extended) | Not required (adequacy) |
| India | Wipro Ltd (IT support) | EU SCCs Module 2 (controller-to-processor), executed 2024-06-01 | TIA-2024-WIPRO-003 |

### Field 7: Retention Periods — Art. 30(1)(f)

Specify the envisaged time limits for erasure of each category of data, or the criteria used to determine the retention period. Periods must be concrete and objectively determinable.

**Example retention schedule:**

| Data Category | Retention Period | Legal Basis for Retention | Deletion Method |
|---------------|-----------------|--------------------------|-----------------|
| Employee payroll records | 10 years from end of employment | Section 257 HGB, Section 147 AO | Automated deletion from SAP HCM |
| Clinical trial data | 25 years from trial completion | Section 13(10) GCP-V; ICH E6(R2) | Archived then destroyed per SOP-DM-012 |
| Job applicant data | 6 months from hiring decision | AGG limitation period | Automated purge from ATS |
| Website analytics | 14 months from collection | CNIL recommendation on analytics retention | GA4 automatic data expiration |
| CCTV footage | 72 hours rolling | Proportionality assessment (DPO approved) | Automated overwrite on NVR |

### Security Measures Description — Art. 30(1)(g)

While not a numbered "field" in the same sense, Art. 30(1)(g) requires a general description of Art. 32 technical and organisational security measures. This description should be meaningful without revealing specific vulnerabilities.

**Example:**

> Technical measures: AES-256 encryption at rest for all databases containing personal data; TLS 1.3 for data in transit; role-based access control (RBAC) with quarterly access reviews; multi-factor authentication for all systems processing personal data; daily encrypted backups with 30-day retention; network segmentation isolating clinical trial systems from corporate IT; endpoint detection and response (EDR) on all workstations; annual penetration testing by independent assessor.
>
> Organisational measures: Mandatory data protection training for all employees (annual refresher); background checks for employees with access to special category data; clean desk policy; data classification scheme (Public, Internal, Confidential, Restricted); incident response procedure with 4-hour initial assessment SLA; vendor security assessments prior to engagement; ISO 27001:2022 certified ISMS (certificate ref: IS 782341).

## RoPA Entry Assembly Workflow

1. **Identify the processing activity**: Start with a specific processing activity, not a department or system. One system may support multiple processing activities, each requiring its own RoPA entry.

2. **Interview the processing owner**: Conduct a structured interview covering all seven fields. Use the data flow as the narrative: "Data comes from [source] about [data subjects], containing [data categories], for the purpose of [purpose], shared with [recipients], transferred to [countries], kept for [duration], protected by [measures]."

3. **Validate against source systems**: Cross-reference interview responses with actual system configurations, data flow diagrams, and contractual documents.

4. **Draft the RoPA entry**: Populate all seven fields using the templates and examples above.

5. **Review with DPO**: The DPO reviews the entry for legal accuracy, particularly the purpose description, lawful basis alignment, and transfer mechanism adequacy.

6. **Obtain processing owner sign-off**: The business owner confirms factual accuracy of the data flows, recipients, and retention periods.

7. **Register in the RoPA management system**: Enter the validated record into the organisation's RoPA tool (e.g., OneTrust, TrustArc, or structured spreadsheet).

8. **Set review date**: Schedule the next review no later than 12 months from creation, or earlier if the processing activity is high-risk.

## Common Pitfalls

1. **Department-level records instead of activity-level**: A single "HR" record covering all HR processing is non-compliant. Each distinct processing activity (payroll, recruitment, performance management, time tracking) requires its own entry.

2. **Missing processor chain documentation**: When a processor engages sub-processors, the RoPA must reflect the entire processing chain, not just the primary processor.

3. **Conflating controller and processor roles**: Where the organisation acts as both controller (for its own processing) and processor (for client data), separate RoPA entries under Art. 30(1) and Art. 30(2) are required.

4. **Ignoring informal processing**: Spreadsheet-based processing, shared drives, and email-based data handling are processing activities that require RoPA entries.

5. **Static retention periods for dynamic data**: Different data elements within the same processing activity may have different retention periods (e.g., contract data vs. marketing preferences collected during onboarding).
