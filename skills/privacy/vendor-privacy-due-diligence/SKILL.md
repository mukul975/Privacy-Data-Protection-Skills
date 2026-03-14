---
name: vendor-privacy-due-diligence
description: >-
  Pre-contract vendor privacy due diligence per GDPR Article 28(1). Covers risk
  questionnaires, technical controls assessment, certification review, data flow
  analysis, and documented sufficiency decisions for processor engagement.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-due-diligence, art-28, processor-assessment, privacy-risk, vendor-onboarding"
---

# Vendor Privacy Due Diligence

## Overview

GDPR Article 28(1) requires controllers to use only processors providing "sufficient guarantees to implement appropriate technical and organisational measures" to meet GDPR requirements and protect data subject rights. This obligation means controllers must conduct thorough privacy due diligence before engaging any vendor that will process personal data. The European Data Protection Board (EDPB) Guidelines 07/2020 on controller and processor concepts reinforce that this assessment must be documented and proportionate to the risk involved.

At Summit Cloud Partners, the Vendor Privacy Due Diligence Program establishes a structured process for evaluating prospective vendors before any personal data processing begins.

## Due Diligence Framework

### Phase 1: Initial Screening

Before engaging in detailed evaluation, determine whether the vendor will process personal data at all.

**Processing Determination Checklist:**

| Question | If YES |
|----------|--------|
| Will the vendor access, store, or transmit personal data? | Proceed to full due diligence |
| Will the vendor host systems containing personal data? | Proceed to full due diligence |
| Will the vendor have logical or physical access to infrastructure holding personal data? | Proceed to full due diligence |
| Is the vendor providing purely non-personal-data services (e.g., office supplies)? | No due diligence required — document determination |

**Data Flow Preliminary Analysis:**

Map the anticipated data flows before proceeding:

1. What categories of personal data will the vendor process?
2. How many data subjects are affected (approximate volume)?
3. Will special category data (Article 9) be involved?
4. Where will processing occur geographically?
5. Will the vendor engage sub-processors?

### Phase 2: Privacy Risk Questionnaire

Summit Cloud Partners issues a standardized Privacy Risk Questionnaire to all prospective vendors scoring above the initial screening threshold.

**Section A — Legal and Governance**

| # | Question | Expected Response |
|---|----------|-------------------|
| A1 | Does your organization have a designated Data Protection Officer (DPO) or equivalent privacy lead? | Named individual with contact details |
| A2 | In which jurisdictions is your organization established? | List of all establishment countries |
| A3 | What is your GDPR compliance governance structure? | Documented privacy program with assigned responsibilities |
| A4 | Have you been subject to any regulatory enforcement actions, fines, or investigations in the past 5 years? | Disclosure of any actions with remediation status |
| A5 | Do you maintain a Record of Processing Activities per Article 30(2)? | Confirmation with sample structure |
| A6 | What lawful bases do you rely on for your own processing activities? | Documented lawful basis assessment |
| A7 | Do you have a process for conducting Data Protection Impact Assessments per Article 35? | DPIA methodology description |

**Section B — Technical Security Controls**

| # | Question | Expected Response |
|---|----------|-------------------|
| B1 | Describe your encryption approach for data at rest and in transit | AES-256 for at-rest, TLS 1.2+ for in-transit minimum |
| B2 | How do you manage access controls and authentication? | RBAC, MFA, principle of least privilege |
| B3 | Describe your vulnerability management program | Regular scanning, patching cadence, penetration testing |
| B4 | What logging and monitoring controls are in place? | SIEM, access logging, anomaly detection |
| B5 | Describe your incident detection and response capabilities | 24/7 monitoring, documented IRP, mean time to detect |
| B6 | How do you secure development practices? | SDLC, code review, OWASP compliance |
| B7 | What physical security controls protect data processing facilities? | Access controls, CCTV, environmental controls |

**Section C — Data Handling Practices**

| # | Question | Expected Response |
|---|----------|-------------------|
| C1 | How do you segregate client data from other clients? | Logical or physical segregation description |
| C2 | What is your data retention and deletion approach? | Defined retention periods, certified deletion |
| C3 | How do you handle data subject access requests forwarded by controllers? | Process description with SLA commitments |
| C4 | Describe your data backup and recovery procedures | Backup frequency, encryption, tested recovery |
| C5 | Do you process personal data in any country outside the EEA? | List of all processing locations with transfer mechanisms |
| C6 | What is your sub-processor engagement process? | Notification mechanism, assessment requirements |

**Section D — Certifications and Attestations**

| # | Question | Expected Response |
|---|----------|-------------------|
| D1 | Do you hold ISO 27001 certification? | Certificate with scope and certification body |
| D2 | Do you hold ISO 27701 certification? | Certificate with scope |
| D3 | Do you hold SOC 2 Type II attestation? | Report with scope and period |
| D4 | Do you hold any cloud-specific certifications (CSA STAR, ISO 27017/27018)? | Certificate details |
| D5 | Do you adhere to any approved GDPR Code of Conduct per Article 40? | Code of Conduct reference and adherence documentation |
| D6 | Have you obtained any GDPR certification per Article 42? | Certification details |

### Phase 3: Technical Controls Assessment

Beyond questionnaire responses, Summit Cloud Partners conducts independent verification of critical controls.

**Assessment Methods:**

1. **Documentation Review**: Examine vendor security policies, procedures, and architectural documentation
2. **Certification Verification**: Independently verify certification validity with issuing bodies
3. **Technical Testing**: Where contractually permitted, conduct or review penetration test results
4. **Reference Checks**: Contact existing clients of the vendor regarding privacy practices
5. **Public Record Search**: Review breach notification databases, regulatory actions, and news reports

**Control Verification Matrix:**

| Control Domain | Questionnaire Claim | Verification Method |
|---------------|---------------------|-------------------|
| Encryption at rest | AES-256 | Review architecture docs, request encryption key management details |
| Encryption in transit | TLS 1.2+ | Technical scan of vendor endpoints |
| Access management | RBAC with MFA | Review IAM policy documentation |
| Incident response | 24/7 SOC | Review SOC 2 Type II report findings |
| Data segregation | Logical separation | Architecture review and documentation |
| Patch management | Monthly cycle | Review vulnerability management reports |

### Phase 4: Data Flow Analysis

Document the complete data flow for the proposed processing arrangement.

**Data Flow Documentation Requirements:**

```
Data Flow: Summit Cloud Partners → [Vendor Name]

1. Data Categories:
   - [List each category of personal data]
   - Classification level per category (Public/Internal/Confidential/Restricted)

2. Data Subjects:
   - [List each category of data subject]
   - Approximate volume per category

3. Transfer Mechanism:
   - Method: [API / SFTP / Direct database access / etc.]
   - Encryption: [Protocol and strength]
   - Authentication: [Method]

4. Processing Locations:
   - Primary: [Country, City, Data Center]
   - Backup/DR: [Country, City, Data Center]
   - Support access: [Countries where staff may access data]

5. Sub-processors:
   - [List known sub-processors with location and function]

6. Data Retention:
   - Processing retention: [Duration]
   - Backup retention: [Duration]
   - Post-termination: [Return/deletion timeline]

7. Return Path:
   - Data subject requests forwarded via: [mechanism]
   - Response SLA: [timeframe]
```

### Phase 5: Sufficiency Decision

The DPO or Privacy Team Lead reviews all collected evidence and issues a documented sufficiency decision.

**Sufficiency Decision Criteria:**

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Legal governance maturity | 15% | 1-5 scale |
| Technical security controls | 25% | 1-5 scale |
| Data handling practices | 20% | 1-5 scale |
| Certifications held | 15% | 1-5 scale |
| Breach and enforcement history | 10% | 1-5 scale (inverse) |
| Sub-processor management | 10% | 1-5 scale |
| Cross-border transfer safeguards | 5% | 1-5 scale |

**Decision Outcomes:**

- **Approved** (weighted score 4.0+): Vendor provides sufficient guarantees. Proceed to DPA negotiation.
- **Conditionally Approved** (weighted score 3.0–3.9): Vendor requires supplementary measures or contractual safeguards before engagement. Document conditions.
- **Rejected** (weighted score below 3.0): Vendor does not provide sufficient guarantees. Document reasons. May be reconsidered after vendor remediation.

**Documentation Requirements per Article 5(2) Accountability:**

The due diligence file must contain:
1. Completed Privacy Risk Questionnaire with vendor responses
2. Evidence of verification activities performed
3. Data flow analysis documentation
4. Sufficiency scoring worksheet
5. Written decision with rationale
6. Approval signature from DPO or designated privacy lead
7. Date of assessment and scheduled reassessment date

## Ongoing Obligations

Due diligence is not a one-time exercise. Article 28(1) imposes a continuing obligation to ensure processors maintain sufficient guarantees. Summit Cloud Partners conducts:

- **Annual Reassessment**: Full questionnaire refresh for high-risk vendors, abbreviated for standard risk
- **Trigger-Based Review**: Reassessment triggered by vendor breach, regulatory action, material service change, or certification lapse
- **Continuous Monitoring**: Automated alerts on vendor security posture changes via risk monitoring services

## Key Regulatory References

- GDPR Article 28(1) — Controller obligation to use processors with sufficient guarantees
- GDPR Article 28(3) — Required DPA provisions
- GDPR Article 5(2) — Accountability principle
- GDPR Article 30(2) — Processor records of processing
- GDPR Article 35 — DPIA requirements
- EDPB Guidelines 07/2020 — Controller and processor concepts under GDPR
- EDPB Recommendations 01/2020 — Supplementary measures for international transfers
