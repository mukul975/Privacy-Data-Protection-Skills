---
name: pia-vendor-processing
description: >-
  Conducts Privacy Impact Assessment for vendor and third-party data processing
  arrangements. Covers processor due diligence, Data Processing Agreement (DPA)
  requirements under GDPR Article 28, sub-processor management, cross-border
  vendor transfers, cloud service provider assessments, and ongoing vendor
  monitoring. Keywords: vendor PIA, processor assessment, DPA, Article 28,
  sub-processor, cloud privacy, third-party risk.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "vendor-pia, processor-assessment, dpa, article-28, sub-processor, cloud-privacy"
---

# Privacy Impact Assessment for Vendor Processing

## Overview

When a controller engages a processor (vendor) to process personal data on its behalf, GDPR Article 28 imposes specific obligations on the controller to ensure that the processor provides sufficient guarantees to implement appropriate technical and organisational measures. The EDPB has repeatedly emphasized that the controller remains accountable for the processing regardless of delegation to a vendor. This skill provides a structured PIA methodology for assessing and managing the privacy risks of vendor data processing arrangements.

## Regulatory Framework

### GDPR Article 28 — Processor Obligations

| Requirement | Description |
|-------------|-------------|
| Art. 28(1) | Controller shall use only processors providing sufficient guarantees |
| Art. 28(2) | Processor shall not engage another processor (sub-processor) without prior specific or general written authorisation |
| Art. 28(3) | Processing governed by a contract or legal act setting out subject matter, duration, nature, purpose, data types, categories of data subjects, and controller obligations/rights |
| Art. 28(3)(a)-(h) | Mandatory DPA clauses: process only on documented instructions, confidentiality, security measures, sub-processor conditions, assist with data subject rights, assist with security/breach/DPIA, delete or return data, provide audit information |
| Art. 28(4) | Sub-processor must be bound by the same data protection obligations |
| Art. 28(5) | Adherence to approved codes of conduct or certification (Art. 42) as elements to demonstrate sufficient guarantees |

### Processor Selection Criteria (EDPB Guidance)

The controller must assess the processor's:
- Technical expertise and security measures
- Track record and reputation (including enforcement history)
- Ability to ensure data subject rights can be exercised
- Data location and cross-border transfer implications
- Sub-processor chain management capability
- Business continuity and data recovery capability
- Willingness to submit to audits

## Vendor Risk Categories

| Risk Category | Examples | Risk Level |
|--------------|----------|-----------|
| Cloud infrastructure (IaaS/PaaS) | AWS, Azure, GCP — hosting personal data | High (data at rest and in transit under vendor control) |
| SaaS applications | CRM, HRIS, email marketing — processing personal data in vendor application | High (vendor application logic and access controls) |
| Analytics providers | Website analytics, marketing attribution — processing behavioural data | Medium-High (data sharing, profiling, cookie compliance) |
| IT support / managed services | Helpdesk, system administration — access to personal data during support | Medium (access-based risk, not purpose-based) |
| Payment processors | Card processing, billing — financial personal data | High (PCI DSS intersection, financial data sensitivity) |
| Sub-processors | Vendor's own vendors processing controller's data | High (reduced visibility and control) |

## PIA Methodology for Vendor Processing

### Phase 1: Vendor Inventory and Classification (Week 1)

1. Inventory all vendors processing personal data on behalf of the organisation.
2. For each vendor, document: personal data categories processed, data subject categories, processing purposes, data volumes, data locations.
3. Classify each vendor by risk category based on data sensitivity, processing scope, and access level.
4. Identify the vendor's sub-processors and their roles.
5. Determine cross-border transfer implications for each vendor.

### Phase 2: Due Diligence Assessment (Week 2)

1. Request and review the vendor's security certifications (ISO 27001, SOC 2, CSA STAR).
2. Review the vendor's privacy certifications and GDPR compliance evidence (ISO 27701, APEC CBPR).
3. Check the vendor's enforcement history with supervisory authorities.
4. Assess the vendor's technical and organisational security measures against the controller's requirements.
5. Evaluate the vendor's data breach notification capability and track record.
6. Review the vendor's sub-processor management process.
7. Assess the vendor's ability to assist with data subject rights requests.

### Phase 3: Data Processing Agreement Review (Week 3)

1. Verify the DPA covers all Art. 28(3) mandatory provisions.
2. Check that processing instructions are specific and documented (not generic catch-all clauses).
3. Verify sub-processor authorisation mechanism: specific or general with notification and objection rights.
4. Ensure data deletion or return obligations at contract termination are clear and enforceable.
5. Verify audit rights: right to conduct or commission audits of the processor.
6. Check cross-border transfer mechanisms (SCCs, BCRs, adequacy) for international vendors.
7. Assess liability and indemnification provisions for data protection breaches.

### Phase 4: Risk Assessment and Mitigation (Week 4)

1. For each vendor, assess the risk to data subjects from the vendor's processing.
2. Consider: data breach at vendor, unauthorised access by vendor employees, sub-processor chain risk, vendor lock-in, business continuity failure.
3. Score risks on likelihood and severity matrix.
4. Identify mitigation measures: encryption (controller-managed keys), pseudonymisation before transfer to vendor, access restrictions, monitoring, contractual controls.
5. Assess residual risk after mitigation.

### Phase 5: Ongoing Monitoring Framework (Week 5)

1. Define vendor review frequency based on risk classification (high-risk: annual; medium: biennial).
2. Establish vendor security questionnaire process for periodic reassessment.
3. Monitor vendor sub-processor changes (notification process, assessment of new sub-processors).
4. Track vendor incidents and breach notifications.
5. Conduct or commission periodic audits for high-risk vendors.
6. Define vendor exit strategy: data return, deletion verification, transition plan.

## Enforcement Precedents

- **CJEU Wirtschaftsakademie (C-210/16, 2018)**: Facebook fan page administrator held to be joint controller with Facebook; controllers cannot avoid responsibility by using a vendor platform.
- **CJEU Fashion ID (C-40/17, 2019)**: Website operator embedding Facebook Like button held to be joint controller for the collection and transmission of data; responsibility for vendor components on own website.
- **Belgian DPA vs IAB Europe (2022)**: EUR 250,000 fine; TCF framework operator held to be controller, not processor; demonstrates that contractual designation does not determine controller/processor status.
- **Spanish AEPD vs Vodafone (2021)**: EUR 8.15 million fine for failure to adequately manage processors and sub-processors handling customer data; insufficient DPA controls.
- **Finnish DPA vs Posti Group (2020)**: EUR 100,000 fine for inadequate processor management; controller failed to verify processor's compliance with data processing instructions.
- **Dutch DPA guidance on cloud services (2022)**: Detailed assessment methodology for cloud vendor privacy compliance, including requirement to conduct DPIA for cloud migrations involving personal data.
