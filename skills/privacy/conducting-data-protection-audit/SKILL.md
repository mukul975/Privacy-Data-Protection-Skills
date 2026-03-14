---
name: conducting-data-protection-audit
description: >-
  Guides a comprehensive organisational data protection audit against key GDPR
  requirements including Articles 5, 24, 25, 28, 30, 32, 35, and 37. Includes
  50+ control points covering principles, accountability, security, and governance.
  Activate when performing compliance audits, preparing for supervisory authority
  inspections, or assessing organisational GDPR maturity. Keywords: data protection
  audit, compliance audit, GDPR audit, control points, accountability.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "gdpr, audit, compliance, accountability, security, data-protection"
---

# Conducting Data Protection Audit

## Overview

A data protection audit systematically evaluates an organisation's compliance with GDPR requirements across governance, processing activities, data subject rights, security measures, and third-party arrangements. This skill provides a structured audit framework with 50+ control points mapped to specific GDPR articles, enabling auditors to produce a comprehensive compliance assessment with prioritised remediation recommendations.

## Audit Framework Structure

The audit is organised into eight domains aligned to core GDPR chapters and articles:

1. Data Protection Principles (Art. 5)
2. Accountability and Governance (Art. 24, 5(2))
3. Privacy by Design and Default (Art. 25)
4. Processor Management (Art. 28)
5. Records of Processing (Art. 30)
6. Security of Processing (Art. 32)
7. Data Protection Impact Assessments (Art. 35)
8. Data Protection Officer (Art. 37-39)

## Domain 1: Data Protection Principles (Art. 5)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 1.1 | Processing purposes are specified, explicit, and documented for each activity | Art. 5(1)(a)-(b) | RoPA with specific purpose statements |
| 1.2 | A valid lawful basis is identified and documented for each processing activity | Art. 5(1)(a), 6 | Lawful basis register/assessment records |
| 1.3 | Personal data collected is adequate, relevant, and limited to what is necessary | Art. 5(1)(c) | Data minimisation reviews, field-level justification |
| 1.4 | Personal data is accurate and kept up to date with rectification procedures | Art. 5(1)(d) | Data quality processes, rectification logs |
| 1.5 | Retention periods are defined for all data categories with deletion/anonymisation procedures | Art. 5(1)(e) | Retention schedule, deletion logs |
| 1.6 | Appropriate security measures protect personal data against unauthorised access, loss, or destruction | Art. 5(1)(f) | Security controls documentation, pen test reports |
| 1.7 | The controller can demonstrate compliance with all principles (accountability) | Art. 5(2) | Compiled evidence portfolio |

## Domain 2: Accountability and Governance (Art. 24)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 2.1 | A data protection policy is approved by senior management and communicated to all staff | Art. 24(2) | Signed policy, distribution records |
| 2.2 | Data protection roles and responsibilities are formally assigned across the organisation | Art. 24(1) | RACI matrix, job descriptions |
| 2.3 | Regular data protection training is provided to all staff processing personal data | Art. 39(1)(b) | Training records, attendance logs, completion certificates |
| 2.4 | A data protection governance structure exists with board-level reporting | Art. 24, 38(3) | Governance charter, board meeting minutes |
| 2.5 | Documented procedures exist for all GDPR obligations (breach notification, DSAR, DPIA) | Art. 24(1) | Procedure documents with version control |
| 2.6 | Internal audits of data protection compliance are conducted at defined intervals | Art. 24(1) | Audit schedule, previous audit reports |
| 2.7 | A data protection risk register is maintained and reviewed | Art. 24(1) | Risk register with risk scores and treatment plans |

## Domain 3: Privacy by Design and Default (Art. 25)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 3.1 | Privacy requirements are integrated into the systems development lifecycle | Art. 25(1) | SDLC documentation with privacy checkpoints |
| 3.2 | Privacy impact is assessed before deploying new systems or changing existing processing | Art. 25(1) | DPIA screening records, change management logs |
| 3.3 | Default settings ensure only necessary personal data is processed | Art. 25(2) | Configuration reviews, default settings documentation |
| 3.4 | Data minimisation is applied at the design stage of systems and processes | Art. 25(1) | Design documents showing minimisation decisions |
| 3.5 | Pseudonymisation and encryption are considered in system design | Art. 25(1), 32(1)(a) | Architecture documents, encryption standards |
| 3.6 | User interfaces facilitate data subject rights (access, deletion, portability) | Art. 25(1)-(2) | UI/UX specifications, data export functionality |

## Domain 4: Processor Management (Art. 28)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 4.1 | All processors are identified and recorded in a vendor register | Art. 28(1) | Vendor register with processor classifications |
| 4.2 | Written data processing agreements are in place with all processors containing Art. 28(3) mandatory clauses | Art. 28(3) | DPA register, sample DPA review |
| 4.3 | Processor due diligence is conducted before engagement and periodically thereafter | Art. 28(1) | Due diligence questionnaires, assessment reports |
| 4.4 | Sub-processor authorisation and notification procedures are documented | Art. 28(2)-(4) | Sub-processor clauses, notification records |
| 4.5 | Processor compliance is monitored through audits, certifications, or self-assessments | Art. 28(3)(h) | Audit rights exercised, SOC 2/ISO 27001 certificates |
| 4.6 | Processors return or delete personal data upon contract termination | Art. 28(3)(g) | Data return/deletion confirmations |
| 4.7 | Processor breach notification obligations are contractually defined and tested | Art. 28(3)(f), 33 | DPA breach clauses, incident response test results |

## Domain 5: Records of Processing (Art. 30)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 5.1 | A comprehensive RoPA is maintained for all controller processing activities | Art. 30(1) | Complete RoPA with all Art. 30(1)(a)-(g) fields |
| 5.2 | Processor records are maintained for all processing on behalf of controllers | Art. 30(2) | Processor RoPA with Art. 30(2)(a)-(d) fields |
| 5.3 | RoPA is kept up to date with a defined review and update process | Art. 30(1)-(2) | Last review dates, update procedure |
| 5.4 | RoPA can be made available to the supervisory authority on request | Art. 30(4) | Export capability, access procedure |
| 5.5 | RoPA is maintained in writing (including electronic form) | Art. 30(3) | Electronic RoPA system or documented spreadsheet |

## Domain 6: Security of Processing (Art. 32)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 6.1 | Risk assessments are conducted to determine appropriate security measures | Art. 32(1)-(2) | Risk assessment reports for processing activities |
| 6.2 | Pseudonymisation and encryption of personal data are implemented where appropriate | Art. 32(1)(a) | Encryption at rest and in transit documentation |
| 6.3 | Ongoing confidentiality, integrity, availability, and resilience of systems is ensured | Art. 32(1)(b) | ISO 27001 controls, access management, BCP/DR plans |
| 6.4 | Ability to restore access to personal data in a timely manner after an incident | Art. 32(1)(c) | Backup procedures, restoration testing records |
| 6.5 | Regular testing and evaluation of security measures is performed | Art. 32(1)(d) | Penetration test reports, vulnerability scans, audit results |
| 6.6 | Access to personal data is restricted on a need-to-know basis | Art. 32(1)(b) | Access control matrices, user access reviews |
| 6.7 | Physical security controls protect premises where personal data is processed | Art. 32(1)(b) | Physical security policy, access logs |
| 6.8 | Personal data breach detection and response procedures are in place | Art. 33-34 | Incident response plan, breach register |

## Domain 7: Data Protection Impact Assessments (Art. 35)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 7.1 | Criteria for mandatory DPIA are defined and communicated to the organisation | Art. 35(1),(3) | DPIA threshold criteria, DPA blacklist consideration |
| 7.2 | DPIAs are conducted before processing that is likely to result in high risk | Art. 35(1) | DPIA register with completion dates |
| 7.3 | DPIAs contain all Art. 35(7) mandatory elements (description, necessity, risks, measures) | Art. 35(7) | Sample DPIA review for completeness |
| 7.4 | The DPO is consulted during the DPIA process | Art. 35(2) | DPO consultation records, sign-off |
| 7.5 | Data subject views are sought where appropriate | Art. 35(9) | Consultation records or documented rationale for not consulting |
| 7.6 | DPIA outcomes are implemented and monitored | Art. 35(11) | Remediation tracking, follow-up reviews |
| 7.7 | Prior consultation with the supervisory authority is initiated when residual risk remains high | Art. 36 | Prior consultation records (if applicable) |

## Domain 8: Data Protection Officer (Art. 37-39)

| # | Control Point | GDPR Ref | Evidence Required |
|---|--------------|----------|-------------------|
| 8.1 | A DPO is appointed where required (public authority, large-scale monitoring, special categories) | Art. 37(1) | DPO appointment letter, published contact details |
| 8.2 | The DPO has sufficient resources, independence, and access to senior management | Art. 38(1)-(3) | Budget allocation, reporting line documentation |
| 8.3 | The DPO does not receive instructions regarding the exercise of their tasks | Art. 38(3) | Independence clause in employment/service contract |
| 8.4 | The DPO's contact details are published and communicated to the supervisory authority | Art. 37(7) | Website publication, DPA notification records |
| 8.5 | The DPO is involved in all data protection matters in a timely manner | Art. 38(1) | Meeting invitations, consultation records |
| 8.6 | The DPO monitors compliance, provides advice, and cooperates with the supervisory authority | Art. 39(1) | DPO activity reports, advisory records |

## Audit Execution Methodology

### Phase 1: Planning (Week 1)
1. Define audit scope (full organisation or targeted domains).
2. Assemble audit team with data protection and information security expertise.
3. Issue audit notification to business units 2 weeks in advance.
4. Request pre-audit documentation package from each domain owner.

### Phase 2: Document Review (Weeks 2-3)
1. Review all requested evidence against each control point.
2. Classify each control as: Effective, Partially Effective, Ineffective, or Not Implemented.
3. Identify gaps where evidence is missing or insufficient.

### Phase 3: Testing and Interviews (Weeks 3-4)
1. Conduct interviews with processing owners, IT security, HR, legal, and the DPO.
2. Perform sample testing of key controls (e.g., access reviews, breach simulations, DSAR process walkthroughs).
3. Verify technical controls through configuration reviews or tool demonstrations.

### Phase 4: Reporting (Week 5)
1. Produce audit report with findings classified by severity (Critical, Major, Minor, Observation).
2. Include a compliance score per domain and overall maturity rating.
3. Provide prioritised remediation roadmap with owners and deadlines.
4. Present findings to the Data Protection Steering Committee and Board.

### Phase 5: Follow-up (Ongoing)
1. Track remediation actions through the findings register.
2. Conduct follow-up reviews at 30/60/90 day intervals depending on severity.
3. Feed audit findings into the annual DPO report and risk register updates.
