---
name: iso-27701-pims
description: >-
  Guides ISO 27701 Privacy Information Management System implementation extending
  ISO 27001/27002. Covers Clause 5 PIMS-specific requirements, Clause 6 PIMS guidance
  for ISO 27002, Clause 7 PII controller guidance (Annex A), Clause 8 PII processor
  guidance (Annex B), gap assessment, and certification path. Keywords: ISO 27701,
  PIMS, privacy management system, ISO 27001 extension, certification, Annex A, Annex B.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-audit-certification
  tags: "iso-27701, pims, privacy-management, iso-27001, certification, controller-processor"
---

# ISO 27701 Privacy Information Management System Implementation

## Overview

ISO/IEC 27701:2019 specifies requirements and provides guidance for establishing, implementing, maintaining, and continually improving a Privacy Information Management System (PIMS) as an extension to ISO/IEC 27001:2022 and ISO/IEC 27002:2022. Published in August 2019, ISO 27701 is the first certifiable international standard for privacy management, providing a framework that maps to GDPR, LGPD, PIPA, APPI, and other data protection regulations. The standard transforms an existing Information Security Management System (ISMS) into a PIMS by adding privacy-specific requirements and controls applicable to PII controllers and PII processors.

Organizations such as Sentinel Compliance Group implement ISO 27701 to demonstrate accountability under Art. 5(2) GDPR, satisfy Art. 42 certification requirements, and provide contractual assurance to data subjects, customers, and supervisory authorities that privacy obligations are systematically managed.

## Standard Structure

### Clauses 5-8 Architecture

| Clause | Title | Extends | Applicability |
|--------|-------|---------|---------------|
| Clause 5 | PIMS-Specific Requirements Related to ISO/IEC 27001 | ISO 27001 Clauses 4-10 | All organizations |
| Clause 6 | PIMS-Specific Guidance Related to ISO/IEC 27002 | ISO 27002 Controls | All organizations |
| Clause 7 | Additional ISO/IEC 27002 Guidance for PII Controllers | Annex A controls | PII controllers only |
| Clause 8 | Additional ISO/IEC 27002 Guidance for PII Processors | Annex B controls | PII processors only |
| Annex A | PIMS-Specific Reference Control Objectives and Controls (Controllers) | Normative | PII controllers |
| Annex B | PIMS-Specific Reference Control Objectives and Controls (Processors) | Normative | PII processors |
| Annex C | Mapping to ISO/IEC 29100 | Informative | All organizations |
| Annex D | Mapping to the GDPR | Informative | EU-operating organizations |
| Annex E | Mapping to ISO/IEC 27018 and ISO/IEC 29151 | Informative | Cloud processors |
| Annex F | How to Apply ISO/IEC 27701 to ISO/IEC 27001 and ISO/IEC 27002 | Informative | All organizations |

## Clause 5: PIMS-Specific Requirements

### 5.2 Context of the Organization (extends ISO 27001 Clause 4)

#### 5.2.1 Understanding the Organization and its Context

The organization shall determine external and internal issues relevant to privacy that affect its ability to achieve the intended outcomes of the PIMS. This includes:

- Applicable privacy legislation and regulation (GDPR, CCPA/CPRA, LGPD, PIPA, APPI, PDPA)
- Applicable judicial decisions and court orders
- Applicable administrative regulations and standards
- Contractual obligations related to PII processing
- Organizational governance, policies, and procedures relevant to PII processing
- Decisions regarding PII processing (particularly where the organization acts as both controller and processor for different processing activities)

#### 5.2.2 Understanding the Needs and Expectations of Interested Parties

Interested parties specific to PIMS include:

| Interested Party | Privacy Expectations |
|------------------|---------------------|
| Data subjects (PII principals) | Lawful processing, transparency, rights exercise, data security |
| Supervisory authorities | Compliance with applicable legislation, cooperation, breach notification |
| Customers (B2B) | Contractual compliance, processor obligations, sub-processor management |
| Employees | Workplace privacy, monitoring transparency, data subject rights |
| Third-party processors/sub-processors | Data processing agreement compliance, instruction adherence |
| Certification bodies | Conformity with ISO 27701 requirements |

#### 5.2.3 Determining the Scope of the PIMS

The PIMS scope must define:

- The types of processing performed (collection, storage, use, disclosure, deletion)
- Whether the organization acts as PII controller, PII processor, or both
- The categories of PII processed
- The categories of PII principals affected
- The organizational units, locations, and systems in scope
- Third parties to whom PII is transferred

#### 5.2.4 PIMS

The ISMS shall be extended to include privacy by addressing PII protection requirements in all ISMS processes, including risk assessment, risk treatment, policy, awareness, internal audit, management review, and continual improvement.

### 5.4 Planning (extends ISO 27001 Clause 6)

#### 5.4.1.2 Privacy Risk Assessment

The organization shall implement a privacy risk assessment process that:

1. Identifies risks to PII principals (not just to the organization) arising from loss of confidentiality, integrity, and availability of PII
2. Considers privacy-specific threats: unauthorized access, unauthorized modification, unauthorized disclosure, unlawful processing, excessive data collection, failure to honor data subject rights, cross-border transfer without safeguards
3. Assesses the likelihood and impact of each risk from the perspective of the PII principal
4. Determines risk levels using a privacy-specific risk matrix

#### 5.4.1.3 Privacy Risk Treatment

The risk treatment process shall select controls from:

- ISO/IEC 27001 Annex A (information security controls)
- ISO/IEC 27701 Annex A (PII controller controls) — when acting as controller
- ISO/IEC 27701 Annex B (PII processor controls) — when acting as processor
- Additional controls from other sources as needed

The Statement of Applicability (SoA) must be extended to include applicable Annex A and/or Annex B controls with justification for inclusion or exclusion of each control.

### 5.5 Support (extends ISO 27001 Clause 7)

#### 5.5.1 Competence

Personnel performing privacy-related functions must demonstrate competence through:

- Formal privacy training (CIPP/E, CIPM, CIPT, ISO 27701 Lead Implementer, ISO 27701 Lead Auditor)
- Knowledge of applicable privacy legislation
- Understanding of PII processing operations within their scope
- Competence records maintained as documented information

#### 5.5.2 Awareness

All persons doing work under the organization's control must be aware of:

- The privacy policy
- Their contribution to the effectiveness of the PIMS
- The implications of not conforming with PIMS requirements
- The potential consequences (including sanctions) of privacy violations

## Annex A: PII Controller Controls

### A.7 — Conditions for Collection and Processing

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| A.7.2.1 | Identify and document purpose | Art. 5(1)(b), Art. 13-14 |
| A.7.2.2 | Identify lawful basis | Art. 6(1), Art. 9(2) |
| A.7.2.3 | Determine when and how consent is to be obtained | Art. 7 |
| A.7.2.4 | Obtain and record consent | Art. 7(1) |
| A.7.2.5 | Privacy impact assessment | Art. 35 |
| A.7.2.6 | Contracts with PII processors | Art. 28 |
| A.7.2.7 | Joint PII controller | Art. 26 |
| A.7.2.8 | Records related to processing PII | Art. 30 |

### A.7.3 — Obligations to PII Principals

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| A.7.3.1 | Determining and fulfilling obligations to PII principals | Art. 12-22 |
| A.7.3.2 | Determining information for PII principals | Art. 13-14 |
| A.7.3.3 | Providing information to PII principals | Art. 12 |
| A.7.3.4 | Providing mechanism to modify or withdraw consent | Art. 7(3) |
| A.7.3.5 | Providing mechanism to object to PII processing | Art. 21 |
| A.7.3.6 | Access, correction and/or erasure | Art. 15-17 |
| A.7.3.7 | PII controllers' obligations to inform third parties | Art. 19 |
| A.7.3.8 | Providing copy of PII processed | Art. 15(3), Art. 20 |
| A.7.3.9 | Handling requests | Art. 12(3)-(4) |
| A.7.3.10 | Automated decision making | Art. 22 |

### A.7.4 — Privacy by Design and Privacy by Default

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| A.7.4.1 | Limit collection | Art. 5(1)(c) |
| A.7.4.2 | Limit processing | Art. 5(1)(b) |
| A.7.4.3 | Accuracy and quality | Art. 5(1)(d) |
| A.7.4.4 | PII minimization objectives | Art. 25(2) |
| A.7.4.5 | PII de-identification and deletion at end of processing | Art. 5(1)(e), Art. 17 |
| A.7.4.6 | Temporary files | Art. 5(1)(e) |
| A.7.4.7 | Retention | Art. 5(1)(e) |
| A.7.4.8 | Disposal | Art. 17 |
| A.7.4.9 | PII transmission controls | Art. 32 |

### A.7.5 — PII Sharing, Transfer, and Disclosure

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| A.7.5.1 | Identify basis for PII transfer between jurisdictions | Art. 44-49 |
| A.7.5.2 | Countries and international organizations to which PII can be transferred | Art. 45 |
| A.7.5.3 | Records of PII disclosure to third parties | Art. 30(1)(d) |
| A.7.5.4 | Notification of PII disclosure requests | Art. 19 |

## Annex B: PII Processor Controls

### B.8.2 — Conditions for Collection and Processing

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| B.8.2.1 | Customer agreement | Art. 28(3) |
| B.8.2.2 | Organization's purposes | Art. 28(3)(a) |
| B.8.2.3 | Marketing and advertising use | Art. 28(3)(a) |
| B.8.2.4 | Infringing instruction | Art. 28(3) second subparagraph |
| B.8.2.5 | Customer obligations | Art. 28(3) |
| B.8.2.6 | Records related to processing PII | Art. 30(2) |

### B.8.3 — Obligations to PII Principals

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| B.8.3.1 | Obligations to PII principals | Art. 28(3)(e) |
| B.8.3.2 | Information for PII principals | — |

### B.8.4 — Privacy by Design and Default

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| B.8.4.1 | Temporary files | Art. 28(3)(g) |
| B.8.4.2 | Return, transfer or disposal of PII | Art. 28(3)(g) |
| B.8.4.3 | PII transmission controls | Art. 32 |

### B.8.5 — PII Sharing, Transfer, and Disclosure

| Control | Description | GDPR Mapping |
|---------|-------------|--------------|
| B.8.5.1 | Basis for PII transfer between jurisdictions | Art. 44-49 |
| B.8.5.2 | Countries and international organizations to which PII can be transferred | Art. 45, 46 |
| B.8.5.3 | Records of PII disclosure to third parties | Art. 30(2) |
| B.8.5.4 | Notification of PII disclosure requests | — |
| B.8.5.5 | Legally binding PII disclosures | Art. 28(3)(a) |
| B.8.5.6 | Disclosure of subcontractors used to process PII | Art. 28(2) |
| B.8.5.7 | Engagement of a subcontractor to process PII | Art. 28(2), (4) |
| B.8.5.8 | Change of subcontractor to process PII | Art. 28(2) |

## Gap Assessment Methodology

### Phase 1: Prerequisite Assessment (Weeks 1-2)

Before ISO 27701 implementation, verify that a functioning ISO 27001 ISMS is in place:

1. **ISO 27001 Certification Status**: Confirm valid ISO 27001:2022 certification or at minimum a fully implemented ISMS with completed internal audit cycle
2. **Scope Alignment**: Determine whether the PIMS scope aligns with the existing ISMS scope or requires expansion
3. **Documentation Baseline**: Inventory existing ISMS policies, procedures, and records that will be extended

### Phase 2: Clause 5 Gap Analysis (Weeks 2-4)

For each sub-clause of Clause 5, assess:

| Assessment Rating | Criteria |
|-------------------|----------|
| Fully Implemented | Control/requirement exists, is documented, implemented, and effective |
| Partially Implemented | Control/requirement exists but lacks documentation, full implementation, or evidence of effectiveness |
| Not Implemented | Control/requirement does not exist or is not addressed |
| Not Applicable | Justified exclusion documented in SoA |

Specific gap analysis checklist:

- [ ] Context analysis includes privacy-specific external and internal issues (5.2.1)
- [ ] Interested parties include PII principals and supervisory authorities (5.2.2)
- [ ] PIMS scope defines controller/processor roles per processing activity (5.2.3)
- [ ] Privacy risk assessment addresses risks to PII principals (5.4.1.2)
- [ ] Statement of Applicability includes Annex A/B controls (5.4.1.3)
- [ ] Privacy-specific competence requirements are defined and tracked (5.5.1)
- [ ] Privacy awareness program covers all persons under organizational control (5.5.2)
- [ ] Internal audit scope includes PIMS-specific requirements (5.6)
- [ ] Management review includes privacy performance indicators (5.7)

### Phase 3: Annex A/B Control Gap Analysis (Weeks 4-8)

For organizations acting as PII controllers, assess all 31 Annex A controls. For PII processors, assess all 18 Annex B controls. For organizations acting in both roles, assess both annexes.

**Gap Assessment Template:**

```
Control ID: A.7.2.1
Control Title: Identify and document purpose
Current State: Purposes documented in privacy notice but not in processing register
Gap Description: Processing register lacks specific purpose documentation per activity
Risk Rating: Medium
Remediation Action: Update processing register template, populate for all activities
Owner: Data Protection Officer
Target Date: [date]
```

### Phase 4: Clause 6 Gap Analysis (Weeks 4-8, parallel with Phase 3)

Assess the 34 privacy-specific modifications to ISO 27002 controls in Clause 6:

| ISO 27002 Control | Clause 6 Extension | Key Addition |
|--------------------|--------------------|--------------|
| 5.1 Policies for information security | 6.2.1.1 | Include PII protection policies |
| 5.10 Acceptable use of information | 6.5.2.1 | Cover acceptable use of PII |
| 5.12 Classification of information | 6.5.2.2 | PII classification criteria |
| 5.13 Labelling of information | 6.5.2.3 | PII labelling requirements |
| 5.34 Privacy and protection of PII | 6.5.3.1 | Operational PII handling |
| 6.1 Screening | 6.6.2.1 | Privacy-related screening |
| 6.2 Terms and conditions of employment | 6.6.2.2 | PII processing duties |
| 6.4 Disciplinary process | 6.6.4 | Privacy violation consequences |
| 8.10 Information deletion | 6.9.4.1 | PII deletion requirements |
| 8.11 Data masking | 6.9.4.2 | PII masking/pseudonymisation |

## Certification Path

### Step 1: Readiness (Months 1-3)

1. Complete gap assessment (Phases 1-4 above)
2. Develop remediation roadmap with prioritized actions
3. Secure management commitment and budget
4. Assign PIMS implementation team

### Step 2: Implementation (Months 3-9)

1. Extend ISMS documentation with PIMS-specific policies and procedures
2. Implement Annex A/B controls per the remediation roadmap
3. Conduct privacy risk assessments for all in-scope processing activities
4. Update Statement of Applicability to include Annex A/B controls
5. Deliver privacy-specific training to all personnel

### Step 3: Internal Audit and Management Review (Months 9-10)

1. Conduct PIMS-specific internal audit covering Clauses 5-8 and applicable Annex controls
2. Document nonconformities and corrective actions
3. Conduct management review with privacy-specific agenda items
4. Verify closure of all major nonconformities

### Step 4: Certification Audit (Months 10-12)

1. **Stage 1 Audit**: Documentation review, scope confirmation, readiness assessment. The certification body reviews PIMS documentation, SoA, risk assessment, and policy framework. Typically 1-2 days on-site.
2. **Stage 2 Audit**: Implementation verification, evidence sampling, interviews with key personnel. The auditor verifies that controls are not just documented but implemented and effective. Typically 3-5 days on-site depending on scope.
3. **Finding Resolution**: Address any nonconformities identified during Stage 2. Major nonconformities must be resolved before certification; minor nonconformities must have accepted corrective action plans.

### Step 5: Surveillance and Recertification

- **Surveillance Audits**: Conducted annually (Year 1 and Year 2) to verify continued conformity
- **Recertification Audit**: Full audit in Year 3 before certificate expiry
- **Scope Changes**: Notify the certification body if significant changes affect the PIMS scope

### Certification Bodies

Accredited certification bodies for ISO 27701 include BSI, SGS, TUV, Bureau Veritas, DNV, LRQA, and Schellman. The certification body must hold accreditation from a national accreditation body (e.g., UKAS, ANAB, DAkkS) specifically for ISO 27701 audits.

## GDPR Alignment via Annex D

Annex D (informative) provides a detailed mapping between ISO 27701 controls and GDPR articles. Key mappings:

| GDPR Article | ISO 27701 Control(s) |
|--------------|----------------------|
| Art. 5 (Principles) | A.7.2.1, A.7.2.2, A.7.4.1-A.7.4.9 |
| Art. 6 (Lawfulness) | A.7.2.2 |
| Art. 7 (Consent) | A.7.2.3, A.7.2.4, A.7.3.4 |
| Art. 13-14 (Information) | A.7.3.2, A.7.3.3 |
| Art. 15-22 (Data subject rights) | A.7.3.1, A.7.3.5-A.7.3.10 |
| Art. 25 (DPbD) | A.7.4.1-A.7.4.5 |
| Art. 28 (Processor) | A.7.2.6, B.8.2.1-B.8.2.6 |
| Art. 30 (Records) | A.7.2.8, B.8.2.6 |
| Art. 32 (Security) | Clause 6 controls |
| Art. 33-34 (Breach) | 6.13.1.1, 6.13.1.5 |
| Art. 35 (DPIA) | A.7.2.5 |
| Art. 44-49 (Transfers) | A.7.5.1-A.7.5.4, B.8.5.1-B.8.5.8 |

## Implementation at Sentinel Compliance Group

Sentinel Compliance Group extended its existing ISO 27001:2022 certified ISMS to ISO 27701 over a 12-month period:

- **Scope**: All customer data processing operations across EU and APAC regions, covering 47 processing activities as both PII controller (23 activities) and PII processor (24 activities)
- **Gap Assessment Results**: 22 of 31 Annex A controls partially implemented; 14 of 18 Annex B controls partially implemented; 7 Clause 5 gaps identified
- **Key Remediation Items**: Privacy risk assessment methodology (5.4.1.2), data subject rights response procedures (A.7.3), sub-processor change management (B.8.5.7-B.8.5.8)
- **Certification Outcome**: Achieved dual ISO 27001 + ISO 27701 certification via BSI, with zero major nonconformities at Stage 2 audit
- **Ongoing**: Annual surveillance audits, quarterly privacy risk reviews, continuous improvement through corrective action tracking
