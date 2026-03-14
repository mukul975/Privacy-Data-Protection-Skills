---
name: soc2-privacy-audit
description: >-
  Guides SOC 2 Type II Privacy Trust Services Criteria preparation and audit
  execution. Covers AICPA TSP Section 100 Privacy criteria P1-P8 including notice,
  choice/consent, collection, use/retention/disposal, access, disclosure, security,
  and quality. Includes evidence collection, control testing, and report review.
  Keywords: SOC 2, privacy criteria, TSP, AICPA, Type II, trust services.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-audit-certification
  tags: "soc2, privacy-criteria, aicpa, tsp, type-ii, trust-services"
---

# SOC 2 Type II Privacy Trust Services Criteria

## Overview

SOC 2 (System and Organization Controls 2) is a reporting framework developed by the American Institute of Certified Public Accountants (AICPA) that evaluates an organization's controls relevant to the Trust Services Criteria (TSC). The Privacy category is one of five TSC categories (Security, Availability, Processing Integrity, Confidentiality, and Privacy) and specifically addresses how the organization collects, uses, retains, discloses, and disposes of personal information in conformity with commitments in its privacy notice and with criteria set forth by the AICPA.

A SOC 2 Type II report covers a specified examination period (typically 6-12 months) during which the auditor (a licensed CPA firm) tests whether controls were not only designed appropriately (Type I) but also operated effectively throughout the period. For the Privacy TSC, this means demonstrating sustained compliance with criteria P1.0 through P8.1 as defined in TSP Section 100 (2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy).

Sentinel Compliance Group undergoes annual SOC 2 Type II examinations including the Privacy TSC to provide contractual assurance to enterprise clients in financial services, healthcare technology, and SaaS sectors.

## Privacy Trust Services Criteria (P1.0 — P8.1)

### P1.0 — Notice

**Criterion**: The entity provides notice to data subjects about its privacy practices.

**P1.1**: The entity provides notice to data subjects about its privacy practices to meet the entity's objectives related to privacy. The notice is updated and communicated to data subjects in a timely manner for changes to the entity's privacy practices, including changes in the use of personal information.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P1.1-01 | Privacy notice is published on all data collection points (website, mobile app, paper forms) | Screenshots of privacy notices on all collection points, version history log |
| P1.1-02 | Privacy notice describes: types of personal information collected, purposes of collection and use, categories of third parties to whom data is disclosed, data subject rights, retention periods | Privacy notice text, legal review records |
| P1.1-03 | Privacy notice is reviewed and updated at minimum annually and when processing changes occur | Annual review meeting minutes, change log, approval records |
| P1.1-04 | Material changes to privacy notice are communicated to affected data subjects via email or in-app notification prior to the change taking effect | Notification records, email delivery logs, communication templates |
| P1.1-05 | Privacy notice is available in languages corresponding to the user base | Translated notice versions, translation vendor records |

### P1.2 — Choice and Consent

**Criterion**: The entity communicates choices available regarding the collection, use, retention, disclosure, and disposal of personal information.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P1.2-01 | Consent is obtained prior to or at the time of collection of personal information | Consent records, timestamp logs, consent mechanism screenshots |
| P1.2-02 | Data subjects are informed of consequences of refusing to provide personal information | Privacy notice text, consent form text |
| P1.2-03 | Opt-out mechanisms are provided for marketing communications and non-essential processing | Opt-out mechanism evidence, preference center screenshots |
| P1.2-04 | Explicit consent is obtained for sensitive personal information (health, financial, biometric, children's data) | Explicit consent records, separate consent forms |
| P1.2-05 | Consent withdrawal mechanisms are available and accessible | Withdrawal mechanism documentation, processing records showing withdrawal honored |

### P2.1 — Collection

**Criterion**: Personal information is collected consistent with the entity's objectives related to privacy.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P2.1-01 | Personal information collected is limited to that described in the privacy notice and necessary for identified purposes | Data inventory, data mapping, comparison against privacy notice |
| P2.1-02 | Data collection points are inventoried and reviewed quarterly | Collection point inventory, quarterly review records |
| P2.1-03 | Collection of personal information from third-party sources is documented and subject to due diligence | Third-party data source register, due diligence records |
| P2.1-04 | Implicit collection (cookies, device fingerprinting, tracking pixels) is disclosed in the privacy notice | Cookie audit results, tracking technology inventory |

### P3.1 — Use, Retention, and Disposal

**Criterion**: Personal information is used, retained, and disposed of consistent with the entity's objectives.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P3.1-01 | Personal information is used only for purposes identified in the privacy notice | Purpose limitation audit results, processing activity register |
| P3.1-02 | Retention schedules are defined for each category of personal information | Retention schedule document, category-level retention periods |
| P3.1-03 | Automated deletion or anonymization processes execute upon retention period expiry | Deletion job logs, anonymization records, automated process configuration |
| P3.1-04 | Disposal methods ensure personal information is rendered unrecoverable (NIST SP 800-88 Rev. 1 media sanitization) | Disposal certificates, sanitization logs, destruction vendor contracts |
| P3.1-05 | Retention exceptions (litigation hold, regulatory requirement) are documented and time-bound | Litigation hold register, exception approval records |

### P4.1 — Access

**Criterion**: The entity provides data subjects with access to their personal information for review and update.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P4.1-01 | Data subject access request (DSAR) intake mechanism is available (web form, email, in-app) | DSAR portal screenshots, process documentation |
| P4.1-02 | Identity verification is performed prior to fulfilling access requests | Verification procedure document, verification logs |
| P4.1-03 | Access requests are fulfilled within documented timeframes (30 days for GDPR, 45 days for CCPA) | DSAR tracking log with timestamps, response time metrics |
| P4.1-04 | Data subjects can request corrections to inaccurate personal information | Correction mechanism documentation, correction request logs |
| P4.1-05 | Denials of access requests are documented with reasons and communicated to the data subject | Denial records, denial notification templates |

### P5.1 — Disclosure to Third Parties

**Criterion**: Personal information is disclosed to third parties only for identified purposes and with consent.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P5.1-01 | Third parties receiving personal information are identified and documented | Third-party recipient register, data flow diagrams |
| P5.1-02 | Data processing agreements or equivalent contracts are in place with all third parties receiving personal information | Executed DPAs, contract inventory |
| P5.1-03 | Third-party disclosures are consistent with purposes described in the privacy notice | Disclosure audit results, purpose-to-recipient mapping |
| P5.1-04 | Third parties are assessed for adequate privacy and security controls prior to disclosure | Third-party assessment records, vendor risk assessments |
| P5.1-05 | Unauthorized disclosures are reported and investigated | Incident response records, disclosure investigation logs |

### P6.1 — Security for Privacy

**Criterion**: Personal information is protected against unauthorized access, whether physical or logical.

This criterion is met through the Security TSC (CC1.0 through CC9.0, the Common Criteria). Privacy-specific security controls include:

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P6.1-01 | Personal information is encrypted at rest using AES-256 or equivalent | Encryption configuration evidence, key management documentation |
| P6.1-02 | Personal information is encrypted in transit using TLS 1.2 or higher | TLS configuration scans, certificate inventory |
| P6.1-03 | Access to personal information is restricted using role-based access controls (RBAC) | RBAC matrix, access review records, least privilege evidence |
| P6.1-04 | Access to personal information is logged and logs are retained per the audit log retention policy | Log configuration evidence, sample log entries, retention policy |
| P6.1-05 | Privacy-impacting security incidents trigger the breach notification process | Incident classification criteria, breach notification procedure |

### P7.1 — Quality

**Criterion**: Personal information is maintained accurately, completely, and timely for the purposes for which it is used.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P7.1-01 | Data quality processes validate personal information at point of collection | Validation rules documentation, input validation configurations |
| P7.1-02 | Data subjects can request correction of inaccurate personal information | Correction mechanism documentation, correction log |
| P7.1-03 | Personal information is reviewed for accuracy on a periodic basis | Data quality review schedule, review results |

### P8.1 — Monitoring and Enforcement

**Criterion**: The entity monitors compliance with its privacy policies and procedures and has procedures to address privacy-related inquiries, complaints, and disputes.

**Required Controls:**

| Control ID | Control Description | Evidence Required |
|-----------|---------------------|-------------------|
| P8.1-01 | Privacy compliance monitoring is conducted at minimum quarterly | Compliance monitoring reports, finding logs |
| P8.1-02 | A privacy complaint intake mechanism is available and publicized | Complaint mechanism screenshots, privacy notice reference |
| P8.1-03 | Privacy complaints are tracked, investigated, and resolved within documented timeframes | Complaint tracking log, resolution records, SLA metrics |
| P8.1-04 | Employees are trained on privacy obligations at onboarding and annually thereafter | Training records, completion rates, training content |
| P8.1-05 | Disciplinary actions are taken for privacy policy violations | Disciplinary policy, anonymized violation records |

## Evidence Collection Framework

### Documentation Categories

| Category | Examples | Retention Requirement |
|----------|----------|-----------------------|
| Policies and Procedures | Privacy policy, DSAR procedure, breach notification procedure | Current versions plus two prior versions |
| Operational Evidence | DSAR logs, consent records, deletion logs, training records | Throughout examination period plus one year |
| Technical Configuration | Encryption settings, RBAC matrices, log configurations | Point-in-time screenshots plus change records |
| Governance Records | Committee meeting minutes, management review records, risk assessments | Throughout examination period |
| Third-Party Documentation | DPAs, vendor assessments, sub-processor lists | Current plus examination period |

### Evidence Collection Timeline

**Month 1-2 (Pre-Examination Period):**
- Establish evidence repository with access controls
- Create evidence request list mapped to each P-criterion
- Assign evidence owners for each control
- Conduct readiness assessment against all P-criteria

**Months 3-8 (During Examination Period):**
- Collect operational evidence continuously (DSAR logs, deletion records, consent records)
- Maintain running evidence calendar with monthly evidence capture checkpoints
- Document all exceptions and compensating controls
- Conduct mid-period self-assessment at month 5

**Month 9-10 (Pre-Audit Preparation):**
- Complete evidence gap analysis against auditor's request list
- Prepare evidence binders (physical or digital) organized by criterion
- Pre-review all evidence for completeness and consistency
- Prepare key personnel for auditor interviews

### Sample Population Testing

SOC 2 auditors test controls using sampling methodologies based on AICPA AU-C Section 530:

| Examination Period | Population Size | Minimum Sample Size |
|--------------------|----|-----|
| 6 months | 1-50 | All |
| 6 months | 51-250 | 25 |
| 6 months | 251+ | 40 |
| 12 months | 1-50 | All |
| 12 months | 51-250 | 30 |
| 12 months | 251+ | 45 |

For privacy controls, common populations tested include:
- DSAR processing records (testing response timeliness and completeness)
- Consent records (testing capture and withdrawal mechanisms)
- Third-party DPAs (testing completeness and signature)
- Data deletion records (testing timeliness per retention schedule)
- Privacy complaint records (testing investigation and resolution)

## Control Testing Procedures

### Inquiry

The auditor interviews control owners and operators to understand how the control operates in practice:

- Privacy Officer: Overall privacy program governance, policy management, risk assessment
- IT Security: Encryption, access controls, logging, incident response
- Legal: DPA management, privacy notice updates, regulatory monitoring
- Customer Support: DSAR handling, complaint management, consent processes
- HR: Employee training, disciplinary procedures, onboarding privacy requirements

### Observation

The auditor observes controls in operation:

- Walkthrough of DSAR intake and fulfillment process
- Demonstration of consent management platform
- Demonstration of data deletion/anonymization processes
- Walkthrough of privacy complaint handling
- Demonstration of access control review process

### Inspection

The auditor examines evidence artifacts:

- Privacy notice versions and change logs
- DSAR tracking spreadsheets or ticketing system records
- Consent database records with timestamps
- Data deletion job execution logs
- Third-party DPA repository
- Privacy training completion records
- Privacy committee meeting minutes
- Privacy risk assessment documentation

### Reperformance

The auditor independently reperforms a control to verify its effectiveness:

- Submit a test DSAR and verify the response process
- Verify that retention period expiry triggers automated deletion
- Verify that access controls prevent unauthorized access to personal information
- Verify that privacy notice accurately reflects current processing activities

## Report Review

### Management Assertion

The service organization's management provides a written assertion that:

1. The system description is fairly presented
2. Controls were suitably designed (Type I and II)
3. Controls operated effectively throughout the examination period (Type II)

### Auditor's Opinion

The auditor's report contains:

- **Unqualified (clean) opinion**: Controls were suitably designed and operated effectively
- **Qualified opinion**: One or more exceptions noted but controls are generally effective
- **Adverse opinion**: Significant deficiencies exist in control design or operation
- **Disclaimer of opinion**: Sufficient evidence could not be obtained

### Exception Handling

When the auditor identifies exceptions during testing:

1. **Deviation**: A single instance where a control did not operate as designed (e.g., one DSAR exceeded the 30-day response window). The auditor documents the deviation and evaluates whether it represents a systematic failure.
2. **Exception**: A pattern of deviations or a significant individual deviation. Exceptions are described in the report with management's response.
3. **Modified Opinion Threshold**: Typically 3+ exceptions in a single control or exceptions across multiple controls in the same criterion may result in a qualified opinion for that criterion.

### User Entity Considerations (Complementary User Entity Controls — CUECs)

The SOC 2 report identifies controls that user entities (customers) must implement for the system of controls to be effective. Privacy-related CUECs commonly include:

- User entities are responsible for providing accurate personal information to the service organization
- User entities are responsible for reviewing and approving data processing purposes
- User entities are responsible for obtaining consent from their own data subjects before providing personal information to the service organization
- User entities are responsible for notifying the service organization of DSARs that require the service organization's assistance

## SOC 2 Privacy vs. GDPR Comparison

| Aspect | SOC 2 Privacy TSC | GDPR |
|--------|-------------------|------|
| Regulatory nature | Voluntary attestation | Mandatory legislation |
| Scope | Service organization's system | All personal data processing |
| Enforcer | CPA auditor (AICPA standards) | Supervisory authorities |
| Consequence of failure | Qualified/adverse report | Fines up to EUR 20M or 4% global turnover |
| Coverage | Eight criteria (P1-P8) | 99 articles, 173 recitals |
| Lawful basis | Not addressed (consent-focused) | Six lawful bases under Art. 6 |
| Cross-border transfers | Not specifically addressed | Chapters V (Art. 44-49) |
| Data subject rights | Access and correction (P4) | Eight rights (Art. 15-22) |
| Breach notification | Covered under Security TSC | 72-hour DPA notification, data subject notification |

## Sentinel Compliance Group SOC 2 Privacy Implementation

Sentinel Compliance Group maintains an annual SOC 2 Type II examination (12-month period, January 1 — December 31) including the Privacy TSC alongside Security and Confidentiality:

- **Examination Period**: January 1, 2025 — December 31, 2025
- **Auditor**: Deloitte & Touche LLP
- **Criteria Included**: Security (CC), Confidentiality (C), Privacy (P)
- **Controls Tested**: 142 total controls, 38 Privacy-specific
- **Result**: Unqualified opinion with zero exceptions for Privacy criteria
- **Key Metrics During Period**: 847 DSARs processed (average response time: 12 days), 0 privacy complaints unresolved beyond 30 days, 100% employee privacy training completion, 4 privacy notice updates published
- **Bridge Letter**: Issued quarterly to address the gap between examination period end and report issuance (typically 8-12 weeks after period end)
