# ISO/IEC 27701:2019 PIMS - Privacy Skills Mapping

## Document Information

| Field | Value |
|-------|-------|
| **Standard** | ISO/IEC 27701:2019 - Privacy Information Management System (PIMS) |
| **Repository** | Privacy & Data Protection Skills |
| **Skills Mapped** | 258 privacy skills |
| **Last Updated** | 2026-03-15 |
| **Version** | 1.0 |

---

## 1. Standard Overview

### 1.1 What is ISO/IEC 27701?

ISO/IEC 27701:2019 specifies requirements and provides guidance for establishing, implementing, maintaining, and continually improving a Privacy Information Management System (PIMS). It extends ISO/IEC 27001 (Information Security Management) and ISO/IEC 27002 (Security Controls) to include privacy-specific requirements for PII (Personally Identifiable Information) controllers and PII processors.

### 1.2 Standard Structure

| Clause | Title | Scope |
|--------|-------|-------|
| Clause 5 | PIMS-Specific Requirements Relating to ISO/IEC 27001 | Management system requirements extended for privacy |
| Clause 6 | PIMS-Specific Guidance Relating to ISO/IEC 27002 | Security controls adapted for privacy context |
| **Clause 7** | **Additional ISO/IEC 27002 Guidance for PII Controllers** | Controller-specific privacy guidance |
| **Clause 8** | **Additional ISO/IEC 27002 Guidance for PII Processors** | Processor-specific privacy guidance |
| **Annex A** | **PIMS-Specific Reference Control Objectives and Controls (Controllers)** | 31 controls for PII controllers |
| **Annex B** | **PIMS-Specific Reference Control Objectives and Controls (Processors)** | 18 controls for PII processors |
| Annex C | Mapping to ISO/IEC 29100 | Privacy framework alignment |
| **Annex D** | **Mapping to the General Data Protection Regulation** | GDPR cross-reference |
| Annex E | Mapping to ISO/IEC 27018 and ISO/IEC 29151 | Cloud privacy and PII protection |
| Annex F | Application to ISO/IEC 27001 and ISO/IEC 27002 | Integration guidance |

### 1.3 Key Concepts

- **PII Controller**: Entity that determines the purposes and means of processing PII (equivalent to GDPR "data controller")
- **PII Processor**: Entity that processes PII on behalf of a controller (equivalent to GDPR "data processor")
- **PII Principal**: Individual whose PII is processed (equivalent to GDPR "data subject")
- **PIMS**: Privacy Information Management System - the organizational framework for managing privacy

---

## 2. Annex A - PII Controller Controls Mapping

### 2.1 A.7.2 - Conditions for Collection and Processing

Controls governing the lawful basis, purpose limitation, consent, and contractual requirements for PII collection and processing.

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **A.7.2.1** | Identify and document purpose | Document specific, explicit, and legitimate purposes for PII processing | `lawful-basis-assessment`, `building-purpose-limitation-enforcement`, `personal-data-test`, `data-inventory-mapping` | Art. 5(1)(b) |
| **A.7.2.2** | Identify lawful basis | Determine and document the legal basis for each processing activity | `lawful-basis-assessment`, `legit-interest-vs-consent`, `legitimate-interest-lia`, `gdpr-valid-consent` | Art. 6 |
| **A.7.2.3** | Determine when and how consent is to be obtained | Identify where consent is the applicable lawful basis and establish consent processes | `gdpr-valid-consent`, `consent-record-keeping`, `consent-receipt-spec`, `consent-pref-center`, `consent-platform-eval`, `double-opt-in-email`, `managing-consent-for-children`, `managing-consent-for-research`, `managing-mobile-app-consent` | Art. 7 |
| **A.7.2.4** | Obtain and record consent | Implement mechanisms to obtain, record, and manage consent from PII principals | `consent-record-keeping`, `consent-receipt-spec`, `consent-pref-center`, `consent-withdrawal`, `gdpr-valid-consent`, `consent-platform-eval` | Art. 7 |
| **A.7.2.5** | Privacy impact assessment | Conduct assessments for processing activities likely to result in high risk to PII principals | `conducting-gdpr-dpia`, `dpia-automated-decisions`, `dpia-biometric-systems`, `dpia-mitigation-plan`, `dpia-register-mgmt`, `dpia-risk-scoring`, `dpia-stakeholder-consult`, `ai-dpia`, `ai-privacy-assessment`, `ai-privacy-impact-template`, `new-tech-pia`, `pia-health-data`, `pia-large-scale-monitor`, `pia-threshold-screening`, `pia-vendor-processing`, `pia-review-cadence`, `comparing-pia-methodologies`, `biometric-dpia`, `cloud-migration-dpia`, `employee-monitoring-dpia`, `employee-surveillance-dpia`, `health-data-dpia`, `marketing-analytics-dpia`, `privacy-threshold-analysis` | Art. 35 |
| **A.7.2.6** | Contracts with PII processors | Establish documented processing agreements with processors | `gdpr-dpa-art28`, `dpa-drafting`, `sub-processor-management`, `vendor-privacy-due-diligence`, `vendor-privacy-audit`, `cloud-provider-assessment` | Art. 28 |
| **A.7.2.7** | Joint PII controller | Document arrangements and responsibilities for joint controllership | `joint-controller-art26` | Art. 26 |
| **A.7.2.8** | Records related to processing PII | Maintain comprehensive records of processing activities | `controller-ropa-creation`, `processor-ropa-creation`, `ropa-completeness-audit`, `ropa-maintenance-workflow`, `ropa-dpia-linkage`, `ropa-executive-dashboard`, `ropa-tool-integration`, `ropa-250-exemption`, `group-structure-ropa`, `automated-ropa-generation`, `gdpr-ropa-audit` | Art. 30 |

### 2.2 A.7.3 - Obligations to PII Principals

Controls addressing transparency, data subject rights, and organizational obligations toward individuals whose data is processed.

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **A.7.3.1** | Determine and fulfill obligations to PII principals | Establish and document legal, regulatory, and business obligations to data subjects | `gdpr-accountability`, `gdpr-policy-framework`, `gdpr-compliance-audit`, `privacy-law-gap-analysis`, `multi-jurisdiction-matrix`, `state-law-applicability` | Art. 12-22 |
| **A.7.3.2** | Determine information for PII principals | Define what information must be provided to PII principals about processing | `direct-collection-notice`, `indirect-collection-notice`, `transparent-communication`, `children-privacy-notice` | Art. 13, 14 |
| **A.7.3.3** | Providing information to PII principals | Implement appropriate means to communicate privacy information including notices and points of contact | `direct-collection-notice`, `indirect-collection-notice`, `transparent-communication`, `privacy-api-design` | Art. 12 |
| **A.7.3.4** | Provide mechanism to modify or withdraw consent | Enable PII principals to modify, restrict, or withdraw their consent | `consent-withdrawal`, `consent-pref-center`, `universal-opt-out`, `global-privacy-control`, `cpra-opt-out-signals` | Art. 7(3) |
| **A.7.3.5** | Provide mechanism to object to PII processing | Implement mechanisms for PII principals to object to processing | `right-to-object`, `marketing-objection`, `automated-decision-rights` | Art. 21 |
| **A.7.3.6** | Access, correction, and erasure | Provide PII principals with access to their personal data | `dsar-intake-system`, `dsar-processing`, `california-consumer-rights`, `ccpa-consumer-requests`, `employee-dsar-response` | Art. 15 |
| **A.7.3.7** | PII controllers' obligations to inform third parties | Rectify inaccurate PII and notify recipients of corrections | `right-to-rectification`, `dsar-processing` | Art. 16, 19 |
| **A.7.3.8** | Providing copy of PII processed | Enable erasure of PII and notify processors/third parties | `right-to-erasure`, `ccpa-right-to-delete`, `children-deletion-requests`, `search-engine-erasure`, `backup-retention-erasure` | Art. 17 |
| **A.7.3.9** | Handling requests | Implement data portability mechanisms for PII principals | `data-portability`, `dsar-intake-system`, `dsar-processing` | Art. 20 |
| **A.7.3.10** | Automated decision making | Address obligations related to automated processing and profiling of PII | `automated-decision-rights`, `dpia-automated-decisions`, `ai-automated-decisions`, `children-profiling-limits` | Art. 22 |

### 2.3 A.7.4 - Privacy by Design and Privacy by Default

Controls ensuring data minimization, accuracy, retention limits, and privacy-preserving technical measures throughout the data lifecycle.

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **A.7.4.1** | Limit collection | Limit PII collection to the minimum necessary for the identified purposes | `implementing-data-minimization-architecture`, `children-data-minimization`, `hipaa-minimum-necessary` | Art. 5(1)(c) |
| **A.7.4.2** | Limit processing | Limit PII processing to what is adequate, relevant, and necessary | `building-purpose-limitation-enforcement`, `purpose-based-access`, `restriction-of-processing` | Art. 5(1)(b)(c) |
| **A.7.4.3** | Accuracy and quality | Ensure PII is accurate, complete, and kept up to date | `right-to-rectification`, `implementing-data-protection-by-default` | Art. 5(1)(d) |
| **A.7.4.4** | PII minimization objectives | Define and document data minimization objectives | `implementing-data-minimization-architecture`, `implementing-data-protection-by-default`, `classification-policy` | Art. 25 |
| **A.7.4.5** | PII de-identification and deletion at end of processing | Implement de-identification, anonymization, and pseudonymization techniques | `hipaa-deidentification`, `anonymization-alternative`, `pseudo-vs-anon-data`, `pseudonymization-risk`, `differential-privacy-prod`, `implementing-homomorphic-encryption`, `implementing-secure-multi-party-computation`, `designing-privacy-preserving-analytics`, `ai-federated-learning`, `designing-federated-learning-architecture`, `pii-detection-pipeline`, `pii-in-unstructured`, `privacy-record-linkage` | Art. 5(1)(e), 25 |
| **A.7.4.6** | Temporary files | Ensure temporary files containing PII are disposed of within documented time periods | `auto-deletion-workflow`, `automating-storage-limitation-controls` | Art. 5(1)(e) |
| **A.7.4.7** | Retention | Define, document, and enforce retention schedules for PII | `retention-schedule`, `retention-impact-assess`, `retention-exception-mgmt`, `financial-retention`, `cloud-retention-config`, `automating-storage-limitation-controls`, `ai-data-retention` | Art. 5(1)(e) |
| **A.7.4.8** | Disposal | Implement secure disposal procedures for PII no longer needed | `secure-data-destruction`, `auto-deletion-workflow`, `backup-retention-erasure`, `vendor-termination-data` | Art. 5(1)(e), 17 |
| **A.7.4.9** | PII transmission controls | Implement controls for PII in transit including encryption and access restrictions | `privacy-api-design`, `implementing-homomorphic-encryption`, `implementing-secure-multi-party-computation` | Art. 5(1)(f), 32 |

### 2.4 A.7.5 - PII Sharing, Transfer, and Disclosure

Controls governing international data transfers, adequacy assessments, and transfer documentation.

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **A.7.5.1** | Identify basis for PII transfer between jurisdictions | Establish and document the legal basis for cross-border PII transfers | `transfer-impact-assessment`, `scc-implementation`, `eu-us-dpf-assessment`, `bcr-establishment`, `supplementary-measures`, `consent-for-transfers`, `art49-derogations`, `adequacy-assessment` | Art. 44-49 |
| **A.7.5.2** | Countries and international organizations to which PII may be transferred | Identify and document recipient countries and their adequacy status | `adequacy-assessment`, `multi-jurisdiction-matrix`, `apac-transfers`, `data-localization`, `conflicting-laws-mgmt` | Art. 45 |
| **A.7.5.3** | Records of transfer of PII | Maintain records of all PII transfers including recipients and legal basis | `transfer-records`, `controller-ropa-creation`, `data-flow-mapping` | Art. 30, 46 |
| **A.7.5.4** | Records of PII disclosure to third parties | Document all disclosures of PII to third parties | `privacy-data-sharing`, `transfer-records`, `data-lineage-tracking` | Art. 30 |

---

## 3. Annex B - PII Processor Controls Mapping

### 3.1 B.8.2 - Conditions for Collection and Processing

Controls governing the contractual and operational requirements for processors handling PII.

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **B.8.2.1** | Customer agreement | Ensure processing is governed by documented instructions from the controller | `gdpr-dpa-art28`, `dpa-drafting`, `hipaa-baa-management` | Art. 28(3) |
| **B.8.2.2** | Organization's purposes | Define and document any legitimate processing purposes beyond controller instructions | `lawful-basis-assessment`, `building-purpose-limitation-enforcement` | Art. 28(10) |
| **B.8.2.3** | Marketing and advertising | Restrict use of PII for marketing unless explicitly authorized by the controller | `marketing-objection`, `marketing-analytics-dpia` | Art. 28 |
| **B.8.2.4** | Infringing instruction | Establish procedures for identifying and handling potentially unlawful processing instructions | `conflicting-laws-mgmt`, `gdpr-dpa-cooperation` | Art. 28(3) |
| **B.8.2.5** | Customer obligations | Assist the controller in fulfilling its obligations to PII principals | `sub-processor-management`, `vendor-privacy-audit`, `dsar-processing` | Art. 28(3)(e)(f) |
| **B.8.2.6** | Records related to processing PII | Maintain processing records as required by the controller and applicable regulations | `processor-ropa-creation`, `ropa-completeness-audit`, `automated-ropa-generation` | Art. 30(2) |

### 3.2 B.8.3 - Obligations to PII Principals

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **B.8.3.1** | Obligations to PII principals | Assist the controller in fulfilling data subject rights requests and privacy impact assessments | `dsar-processing`, `dsar-intake-system`, `employee-dsar-response`, `dpia-stakeholder-consult` | Art. 28(3)(e) |

### 3.3 B.8.4 - Privacy by Design and Privacy by Default

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **B.8.4.1** | Temporary files | Ensure temporary files created during processing are disposed of within documented time periods | `auto-deletion-workflow`, `automating-storage-limitation-controls` | Art. 5(1)(e), 28 |
| **B.8.4.2** | Return, transfer, or disposal of PII | Provide capability to return, securely transfer, or dispose of PII and make disposal policy available to the controller | `vendor-termination-data`, `secure-data-destruction`, `backup-retention-erasure` | Art. 28(3)(g) |
| **B.8.4.3** | PII transmission controls | Implement controls governing PII in transit, including encryption | `privacy-api-design`, `implementing-homomorphic-encryption` | Art. 32 |

### 3.4 B.8.5 - PII Sharing, Transfer, and Disclosure

| Control | Title | Description | Mapped Skills | GDPR Article |
|---------|-------|-------------|---------------|--------------|
| **B.8.5.1** | Basis for PII transfer between jurisdictions | Identify and document the legal basis for cross-border transfers on behalf of the controller | `transfer-impact-assessment`, `scc-implementation`, `supplementary-measures` | Art. 44-49 |
| **B.8.5.2** | Countries and international organizations to which PII may be transferred | Document recipient countries/organizations and inform the controller | `adequacy-assessment`, `multi-jurisdiction-matrix`, `data-localization` | Art. 44, 45 |
| **B.8.5.3** | Records of PII disclosure to third parties | Maintain records of disclosures including to sub-processors | `transfer-records`, `data-lineage-tracking` | Art. 30(2) |
| **B.8.5.4** | Notification of PII disclosure requests | Notify the controller of legally binding requests for PII disclosure (e.g., law enforcement) | `breach-multi-jurisdiction`, `conflicting-laws-mgmt`, `regulatory-complaints` | Art. 28(3)(a) |
| **B.8.5.5** | Legally binding PII disclosures | Handle mandatory disclosures in compliance with applicable law while notifying the controller | `conflicting-laws-mgmt`, `litigation-hold-mgmt` | Art. 28 |
| **B.8.5.6** | Disclosure of subcontractors used to process PII | Inform the controller about the use of sub-processors before processing begins | `sub-processor-management`, `vendor-monitoring-program` | Art. 28(2) |
| **B.8.5.7** | Engagement of a subcontractor to process PII | Establish written agreements with sub-processors imposing equivalent data protection obligations | `sub-processor-management`, `dpa-drafting`, `vendor-privacy-due-diligence` | Art. 28(4) |
| **B.8.5.8** | Change of subcontractor to process PII | Inform the controller of intended changes to sub-processors and allow objection | `sub-processor-management`, `vendor-monitoring-program`, `vendor-breach-cascade` | Art. 28(2) |

---

## 4. Clause 5 and 6 - PIMS Management System Controls Mapping

### 4.1 Clause 5 - PIMS-Specific Requirements (ISO 27001 Extension)

These clauses extend ISO 27001 management system requirements with privacy-specific considerations.

| Clause | Title | Mapped Skills |
|--------|-------|---------------|
| 5.2.1 | Understanding the organization and its context | `privacy-maturity-model`, `privacy-law-gap-analysis`, `multi-jurisdiction-matrix`, `state-law-applicability` |
| 5.2.2 | Understanding the needs and expectations of interested parties | `gdpr-accountability`, `privacy-program-metrics`, `regulatory-complaints` |
| 5.2.3 | Determining the scope of the PIMS | `data-inventory-mapping`, `data-flow-mapping`, `classification-policy` |
| 5.2.4 | PIMS | `iso-27701-pims`, `privacy-maturity-model`, `continuous-compliance` |
| 5.4.1.2 | Information security risk assessment (privacy) | `audit-risk-assessment`, `dpia-risk-scoring`, `privacy-threshold-analysis` |
| 5.4.1.3 | Information security risk treatment (privacy) | `dpia-mitigation-plan`, `gdpr-remediation-roadmap`, `audit-remediation-program` |

### 4.2 Clause 6 - PIMS-Specific Guidance (ISO 27002 Extension)

| Clause | Title | Mapped Skills |
|--------|-------|---------------|
| 6.2.1.1 | Information security roles and responsibilities (privacy) | `gdpr-accountability`, `gdpr-policy-framework` |
| 6.3.1.1 | Screening (privacy) | `background-check-privacy`, `employee-health-data` |
| 6.3.2.1 | Terms and conditions of employment (privacy) | `employment-consent-limits`, `workplace-email-privacy`, `byod-privacy-policy` |
| 6.4.2.2 | Information security awareness, education and training (privacy) | `hipaa-employee-training`, `breach-simulation` |
| 6.5.2.1 | Classification of information (privacy) | `classification-policy`, `data-labeling-system`, `cross-jurisdiction-class` |
| 6.5.2.4 | Information transfer (privacy) | `transfer-impact-assessment`, `scc-implementation`, `privacy-api-design` |
| 6.5.3.1 | Management of removable media (privacy) | `secure-data-destruction`, `data-localization` |
| 6.5.3.3 | Physical media transfer (privacy) | `secure-data-destruction` |
| 6.6.2.1 | User access management (privacy) | `purpose-based-access`, `hipaa-minimum-necessary` |
| 6.6.2.2 | User access provisioning (privacy) | `purpose-based-access`, `hr-system-privacy-config` |
| 6.9.4.1 | Collection of evidence (privacy) | `audit-evidence-collect`, `breach-forensics`, `breach-documentation` |
| 6.10.2.1 | Compliance with policies and standards (privacy) | `internal-privacy-audit`, `gdpr-compliance-audit`, `gdpr-self-assessment` |
| 6.10.2.2 | Technical compliance checking (privacy) | `cookie-consent-testing`, `cookie-consent-ab-audit`, `pii-detection-pipeline` |
| 6.12.1.1 | Protection of records (privacy) | `controller-ropa-creation`, `processor-ropa-creation`, `ropa-completeness-audit` |
| 6.12.1.2 | Protection of PII (privacy) | `pii-detection-pipeline`, `pii-in-unstructured`, `auto-data-discovery` |
| 6.13.1.1 | Identification of applicable legislation and contractual requirements (privacy) | `privacy-law-monitoring`, `multi-state-compliance`, `state-law-tracker` |
| 6.15.1.1 | Supplier relationships (privacy) | `vendor-privacy-due-diligence`, `vendor-privacy-audit`, `vendor-risk-scoring`, `saas-vendor-inventory` |
| 6.15.1.3 | Supply chain (privacy) | `sub-processor-management`, `vendor-monitoring-program`, `vendor-breach-cascade` |

---

## 5. GDPR Cross-Reference (Annex D Alignment)

ISO 27701 Annex D provides a mapping between the standard's clauses and GDPR Articles 5-49 (excluding Article 43). The following table maps GDPR articles to both ISO 27701 controls and repository skills.

### 5.1 GDPR Principles (Articles 5-11)

| GDPR Article | Title | ISO 27701 Control | Mapped Skills |
|--------------|-------|-------------------|---------------|
| Art. 5(1)(a) | Lawfulness, fairness, transparency | A.7.2.2, A.7.3.2, A.7.3.3 | `lawful-basis-assessment`, `transparent-communication`, `direct-collection-notice` |
| Art. 5(1)(b) | Purpose limitation | A.7.2.1, A.7.4.2 | `building-purpose-limitation-enforcement`, `purpose-based-access` |
| Art. 5(1)(c) | Data minimization | A.7.4.1, A.7.4.4 | `implementing-data-minimization-architecture`, `children-data-minimization`, `hipaa-minimum-necessary` |
| Art. 5(1)(d) | Accuracy | A.7.4.3 | `right-to-rectification`, `implementing-data-protection-by-default` |
| Art. 5(1)(e) | Storage limitation | A.7.4.5-A.7.4.8 | `retention-schedule`, `auto-deletion-workflow`, `secure-data-destruction`, `automating-storage-limitation-controls` |
| Art. 5(1)(f) | Integrity and confidentiality | A.7.4.9, Clause 6 controls | `privacy-api-design`, `implementing-homomorphic-encryption` |
| Art. 5(2) | Accountability | Clause 5, A.7.2.8 | `gdpr-accountability`, `controller-ropa-creation`, `privacy-program-metrics` |
| Art. 6 | Lawful basis for processing | A.7.2.2 | `lawful-basis-assessment`, `legit-interest-vs-consent`, `legitimate-interest-lia` |
| Art. 7 | Conditions for consent | A.7.2.3, A.7.2.4 | `gdpr-valid-consent`, `consent-record-keeping`, `consent-receipt-spec`, `consent-withdrawal` |
| Art. 8 | Child's consent | A.7.2.3 | `managing-consent-for-children`, `gdpr-parental-consent`, `coppa-compliance`, `age-verification-methods`, `age-gating-services` |
| Art. 9 | Special categories of data | A.7.2.1, A.7.2.2 | `special-category-data`, `employee-biometric-data`, `employee-health-data`, `biometric-dpia`, `criminal-data-handling`, `ai-bias-special-category` |
| Art. 10 | Criminal conviction data | A.7.2.1 | `criminal-data-handling` |
| Art. 11 | Processing not requiring identification | A.7.4.5 | `anonymization-alternative`, `pseudo-vs-anon-data`, `hipaa-deidentification` |

### 5.2 Data Subject Rights (Articles 12-23)

| GDPR Article | Title | ISO 27701 Control | Mapped Skills |
|--------------|-------|-------------------|---------------|
| Art. 12 | Transparent information and communication | A.7.3.3 | `transparent-communication`, `direct-collection-notice`, `indirect-collection-notice` |
| Art. 13 | Information where PII collected from data subject | A.7.3.2, A.7.3.3 | `direct-collection-notice`, `children-privacy-notice` |
| Art. 14 | Information where PII not obtained from data subject | A.7.3.2, A.7.3.3 | `indirect-collection-notice` |
| Art. 15 | Right of access | A.7.3.6 | `dsar-intake-system`, `dsar-processing`, `california-consumer-rights`, `employee-dsar-response` |
| Art. 16 | Right to rectification | A.7.3.7 | `right-to-rectification` |
| Art. 17 | Right to erasure | A.7.3.8, A.7.4.8 | `right-to-erasure`, `ccpa-right-to-delete`, `children-deletion-requests`, `search-engine-erasure`, `backup-retention-erasure` |
| Art. 18 | Right to restriction of processing | A.7.3.4 | `restriction-of-processing` |
| Art. 19 | Notification regarding rectification or erasure | A.7.3.7 | `right-to-rectification`, `right-to-erasure` |
| Art. 20 | Right to data portability | A.7.3.9 | `data-portability` |
| Art. 21 | Right to object | A.7.3.5 | `right-to-object`, `marketing-objection`, `universal-opt-out`, `global-privacy-control` |
| Art. 22 | Automated decision-making | A.7.3.10 | `automated-decision-rights`, `ai-automated-decisions`, `children-profiling-limits` |

### 5.3 Controller and Processor Obligations (Articles 24-43)

| GDPR Article | Title | ISO 27701 Control | Mapped Skills |
|--------------|-------|-------------------|---------------|
| Art. 24 | Responsibility of the controller | A.7.2.1, Clause 5 | `gdpr-accountability`, `gdpr-policy-framework`, `privacy-maturity-model` |
| Art. 25 | Data protection by design and default | A.7.4.1-A.7.4.9 | `implementing-data-protection-by-default`, `implementing-data-minimization-architecture`, `applying-privacy-design-patterns`, `selecting-privacy-enhancing-technologies` |
| Art. 26 | Joint controllers | A.7.2.7 | `joint-controller-art26` |
| Art. 27 | Representatives of controllers not established in EU | Clause 5 | `gdpr-eu-representative` |
| Art. 28 | Processor | B.8.2.1-B.8.5.8 | `gdpr-dpa-art28`, `dpa-drafting`, `sub-processor-management`, `vendor-privacy-due-diligence` |
| Art. 30 | Records of processing activities | A.7.2.8, B.8.2.6 | `controller-ropa-creation`, `processor-ropa-creation`, `ropa-completeness-audit`, `automated-ropa-generation`, `gdpr-ropa-audit` |
| Art. 32 | Security of processing | Clause 6, A.7.4.9, B.8.4.3 | `privacy-api-design`, `implementing-homomorphic-encryption`, `implementing-secure-multi-party-computation` |
| Art. 33 | Notification to supervisory authority | Clause 6 | `breach-72h-notification`, `breach-documentation`, `breach-multi-jurisdiction`, `hipaa-breach-notification`, `hipaa-breach-notify`, `ca-breach-notification` |
| Art. 34 | Communication to data subject | Clause 6 | `breach-subject-comms`, `breach-credit-monitor`, `breach-remediation` |
| Art. 35 | Data protection impact assessment | A.7.2.5 | `conducting-gdpr-dpia`, `dpia-automated-decisions`, `dpia-biometric-systems`, `dpia-mitigation-plan`, `dpia-risk-scoring` |
| Art. 36 | Prior consultation | A.7.2.5 | `gdpr-prior-consultation`, `prior-consultation-dpa` |
| Art. 37-39 | Data Protection Officer | Clause 5 | `gdpr-accountability`, `gdpr-policy-framework` |
| Art. 40 | Codes of conduct | Clause 5 | `gdpr-codes-of-conduct`, `eu-code-of-conduct` |
| Art. 41 | Monitoring of codes of conduct | Clause 5 | `gdpr-codes-of-conduct` |
| Art. 42 | Certification | Clause 5 | `gdpr-certification`, `gdpr-certification-scheme` |

### 5.4 International Transfers (Articles 44-49)

| GDPR Article | Title | ISO 27701 Control | Mapped Skills |
|--------------|-------|-------------------|---------------|
| Art. 44 | General principle for transfers | A.7.5.1, B.8.5.1 | `transfer-impact-assessment`, `consent-for-transfers` |
| Art. 45 | Transfers on basis of adequacy decision | A.7.5.2, B.8.5.2 | `adequacy-assessment`, `eu-us-dpf-assessment` |
| Art. 46 | Transfers subject to appropriate safeguards | A.7.5.1, B.8.5.1 | `scc-implementation`, `bcr-establishment`, `supplementary-measures` |
| Art. 47 | Binding corporate rules | A.7.5.1 | `bcr-establishment` |
| Art. 48 | Transfers not authorized by Union law | B.8.5.4, B.8.5.5 | `conflicting-laws-mgmt` |
| Art. 49 | Derogations for specific situations | A.7.5.1 | `art49-derogations`, `consent-for-transfers` |

---

## 6. Thematic Skill Coverage by ISO 27701 Domain

### 6.1 Breach Management Skills

| Skill | A.7.x Controls | B.8.x Controls | GDPR Articles |
|-------|----------------|----------------|----------------|
| `breach-72h-notification` | - | B.8.2.5 | Art. 33 |
| `breach-detection-system` | A.7.2.5 | B.8.2.5 | Art. 33 |
| `breach-documentation` | A.7.2.8 | B.8.2.6 | Art. 33(5) |
| `breach-forensics` | - | - | Art. 33(3) |
| `breach-multi-jurisdiction` | A.7.5.1 | B.8.5.4 | Art. 33, 55 |
| `breach-remediation` | A.7.2.5 | B.8.2.5 | Art. 34 |
| `breach-response-playbook` | A.7.3.1 | B.8.2.5 | Art. 33, 34 |
| `breach-risk-assessment` | A.7.2.5 | B.8.2.5 | Art. 33(1) |
| `breach-simulation` | A.7.2.5 | - | Art. 32 |
| `breach-subject-comms` | A.7.3.3 | - | Art. 34 |
| `breach-credit-monitor` | A.7.3.1 | - | Art. 34 |
| `vendor-breach-cascade` | - | B.8.5.6, B.8.5.8 | Art. 28, 33 |

### 6.2 AI and Emerging Technology Skills

| Skill | A.7.x Controls | B.8.x Controls | GDPR Articles |
|-------|----------------|----------------|----------------|
| `ai-automated-decisions` | A.7.3.10 | - | Art. 22 |
| `ai-bias-special-category` | A.7.2.2 | - | Art. 9 |
| `ai-data-retention` | A.7.4.7 | B.8.4.1 | Art. 5(1)(e) |
| `ai-data-subject-rights` | A.7.3.5, A.7.3.6 | B.8.3.1 | Art. 15-22 |
| `ai-deployment-checklist` | A.7.2.5, A.7.4.4 | - | Art. 25, 35 |
| `ai-dpia` | A.7.2.5 | - | Art. 35 |
| `ai-federated-learning` | A.7.4.5 | - | Art. 25 |
| `ai-model-privacy-audit` | A.7.2.5 | - | Art. 5(2) |
| `ai-privacy-assessment` | A.7.2.5 | - | Art. 35 |
| `ai-privacy-impact-template` | A.7.2.5 | - | Art. 35 |
| `ai-privacy-inference` | A.7.4.5 | - | Art. 5(1)(b) |
| `ai-training-data-class` | A.7.4.1, A.7.4.4 | - | Art. 5(1)(c) |
| `ai-training-lawfulness` | A.7.2.2 | - | Art. 6 |
| `ai-transparency-reqs` | A.7.3.2, A.7.3.3 | - | Art. 13, 14 |
| `ai-vendor-privacy-due` | A.7.2.6 | B.8.5.7 | Art. 28 |
| `healthcare-ai-privacy` | A.7.2.2, A.7.2.5 | - | Art. 9, 35 |
| `llm-output-privacy-risk` | A.7.4.5 | - | Art. 5(1)(f) |

### 6.3 Jurisdiction-Specific Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `australia-privacy-act` | 5.2.1 (context) | Australian Privacy Principles compliance |
| `brazil-lgpd` | 5.2.1, A.7.3.1 | Brazil's Lei Geral de Protecao de Dados |
| `canada-pipeda` | 5.2.1, A.7.3.1 | Canadian privacy legislation |
| `china-pipl` | 5.2.1, A.7.5.1 | China's Personal Information Protection Law |
| `india-dpdp-act` | 5.2.1, A.7.3.1 | India's Digital Personal Data Protection Act |
| `japan-appi` | 5.2.1, A.7.5.2 | Japan's Act on Protection of Personal Information |
| `korea-pipa` | 5.2.1, A.7.3.1 | Korea's Personal Information Protection Act |
| `nigeria-ndpr` | 5.2.1, A.7.3.1 | Nigeria Data Protection Regulation |
| `singapore-pdpa` | 5.2.1, A.7.2.3 | Singapore Personal Data Protection Act |
| `south-africa-popia` | 5.2.1, A.7.3.1 | South Africa's Protection of Personal Information Act |
| `thailand-pdpa` | 5.2.1, A.7.2.3 | Thailand Personal Data Protection Act |
| `turkey-kvkk` | 5.2.1, A.7.3.1 | Turkey's data protection law |
| `uae-pdp-law` | 5.2.1, A.7.5.1 | UAE data protection legislation |
| `uk-aadc-implementation` | A.7.3.10, A.7.4.4 | UK Age Appropriate Design Code |
| `uk-transfer-mechanisms` | A.7.5.1 | UK-specific transfer safeguards |

### 6.4 US State Privacy Law Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `california-consumer-rights` | A.7.3.6 | CCPA/CPRA consumer access rights |
| `ccpa-consumer-requests` | A.7.3.6, A.7.3.9 | CCPA data subject request handling |
| `ccpa-cpra-compliance` | A.7.3.1, A.7.3.5 | California comprehensive compliance |
| `ccpa-right-to-delete` | A.7.3.8 | California deletion rights |
| `colorado-cpa-compliance` | A.7.3.1 | Colorado Privacy Act |
| `connecticut-ctdpa` | A.7.3.1 | Connecticut data protection |
| `cpra-opt-out-signals` | A.7.3.4 | CPRA opt-out preference signals |
| `cpra-sensitive-pi` | A.7.2.2 | CPRA sensitive personal information |
| `delaware-dppa` | A.7.3.1 | Delaware data privacy |
| `iowa-consumer-privacy` | A.7.3.1 | Iowa consumer privacy |
| `kentucky-kppa` | A.7.3.1 | Kentucky privacy protection |
| `montana-mtdpa` | A.7.3.1 | Montana data protection |
| `multi-state-compliance` | 5.2.1, A.7.3.1 | Multi-state compliance framework |
| `new-jersey-dpa` | A.7.3.1 | New Jersey data protection |
| `oregon-ocpa-compliance` | A.7.3.1 | Oregon consumer privacy |
| `state-law-applicability` | 5.2.1 | State law threshold analysis |
| `state-law-tracker` | 5.2.1 | Monitoring state legislation |
| `texas-tdpsa-compliance` | A.7.3.1 | Texas data privacy |
| `vcdpa-compliance` | A.7.3.1 | Virginia consumer data protection |
| `ca-breach-notification` | Clause 6 | California breach notification |

### 6.5 Healthcare and HIPAA Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `42-cfr-part-2` | A.7.2.2 | Substance abuse records confidentiality |
| `hipaa-baa-management` | B.8.2.1, A.7.2.6 | Business Associate Agreements |
| `hipaa-breach-notification` | Clause 6 | HIPAA breach notification rule |
| `hipaa-breach-notify` | Clause 6 | HIPAA breach notification procedures |
| `hipaa-deidentification` | A.7.4.5 | Safe Harbor and Expert Determination |
| `hipaa-employee-training` | Clause 6 | Privacy and security training |
| `hipaa-interoperability` | A.7.4.9 | Health data exchange requirements |
| `hipaa-minimum-necessary` | A.7.4.1 | Minimum Necessary Standard |
| `hipaa-mobile-health` | A.7.4.9 | Mobile health application privacy |
| `hipaa-phi-inventory` | A.7.2.8 | PHI data inventory |
| `hipaa-privacy-rule` | A.7.3.1 | HIPAA Privacy Rule requirements |
| `hipaa-research-privacy` | A.7.2.3 | Research data consent requirements |
| `hipaa-risk-analysis` | A.7.2.5 | Risk analysis per Security Rule |
| `hipaa-security-rule` | Clause 6, A.7.4.9 | Technical safeguards |
| `hitech-act-privacy` | A.7.3.1 | HITECH Act privacy provisions |
| `pia-health-data` | A.7.2.5 | Health data impact assessments |
| `telehealth-privacy` | A.7.4.9 | Telehealth-specific privacy controls |
| `edtech-privacy-assessment` | A.7.2.5 | Educational technology privacy |

### 6.6 Cookie and Tracking Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `analytics-cookie-consent` | A.7.2.3, A.7.2.4 | Analytics cookie consent management |
| `cnil-compliant-cookies` | A.7.2.3 | CNIL cookie compliance |
| `cnil-cookie-banner` | A.7.3.3 | CNIL-compliant cookie banners |
| `cookie-audit` | A.7.2.8, A.7.4.2 | Comprehensive cookie audit |
| `cookie-consent-ab-audit` | A.7.2.4 | A/B testing of consent flows |
| `cookie-consent-testing` | A.7.2.4 | Consent mechanism testing |
| `cookieless-alternatives` | A.7.4.5 | Privacy-preserving analytics alternatives |
| `cookie-lifetime-audit` | A.7.4.7 | Cookie retention audit |
| `cross-jurisdiction-cookies` | A.7.5.2 | Multi-jurisdiction cookie compliance |
| `eprivacy-essential-cookies` | A.7.2.3 | ePrivacy Directive cookie classification |
| `google-consent-mode-v2` | A.7.2.4 | Google Consent Mode implementation |
| `gpc-cookie-integration` | A.7.3.4 | Global Privacy Control integration |
| `server-side-tracking` | A.7.4.5 | Server-side tracking privacy |
| `tcf-v2-implementation` | A.7.2.4 | IAB Transparency & Consent Framework |

### 6.7 Vendor and Processor Management Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `cloud-provider-assessment` | A.7.2.6 | Cloud processor risk assessment |
| `dpa-drafting` | A.7.2.6, B.8.2.1 | Data Processing Agreement drafting |
| `gdpr-dpa-art28` | A.7.2.6, B.8.2.1 | Art. 28 compliant processor agreements |
| `saas-vendor-inventory` | A.7.2.6 | SaaS vendor data inventory |
| `sub-processor-management` | B.8.5.6, B.8.5.7, B.8.5.8 | Sub-processor lifecycle management |
| `vendor-breach-cascade` | B.8.5.6 | Vendor breach notification cascade |
| `vendor-cert-acceptance` | A.7.2.6 | Vendor certification acceptance criteria |
| `vendor-monitoring-program` | B.8.5.6 | Ongoing vendor monitoring |
| `vendor-privacy-audit` | A.7.2.6 | Vendor privacy audit program |
| `vendor-privacy-due-diligence` | A.7.2.6, B.8.5.7 | Pre-engagement privacy due diligence |
| `vendor-risk-scoring` | A.7.2.6 | Vendor risk scoring methodology |
| `vendor-termination-data` | B.8.4.2 | Data handling at vendor termination |

### 6.8 NIST, SOC2, and Framework Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `nist-pf-communicate` | A.7.3.3 | NIST Privacy Framework - Communicate |
| `nist-pf-control` | A.7.4.1-A.7.4.9 | NIST Privacy Framework - Control |
| `nist-pf-govern` | Clause 5 | NIST Privacy Framework - Govern |
| `nist-pf-identify` | A.7.2.1, A.7.2.8 | NIST Privacy Framework - Identify |
| `nist-pf-protect` | A.7.4.9, Clause 6 | NIST Privacy Framework - Protect |
| `nist-privacy-identify` | A.7.2.1 | NIST privacy identification |
| `soc2-privacy-audit` | Clause 5, A.7.2.5 | SOC 2 privacy trust criteria audit |
| `apec-cbpr-cert` | A.7.5.1 | APEC Cross-Border Privacy Rules certification |
| `iso-27701-pims` | All clauses | Direct ISO 27701 PIMS implementation |
| `preparing-iso-31700-certification` | A.7.4.1-A.7.4.4 | ISO 31700 Privacy by Design |

### 6.9 Employment and HR Privacy Skills

| Skill | Primary ISO 27701 Clause | Description |
|-------|--------------------------|-------------|
| `background-check-privacy` | 6.3.1.1 | Pre-employment screening privacy |
| `byod-privacy-policy` | 6.3.2.1 | BYOD privacy controls |
| `employee-biometric-data` | A.7.2.2 | Employee biometric data processing |
| `employee-dsar-response` | A.7.3.6 | Employee data subject requests |
| `employee-health-data` | A.7.2.2 | Employee health data processing |
| `employee-monitoring-dpia` | A.7.2.5 | Employee monitoring DPIA |
| `employee-surveillance-dpia` | A.7.2.5 | Workplace surveillance assessment |
| `employment-consent-limits` | A.7.2.3 | Employment consent limitations |
| `hr-system-privacy-config` | 6.6.2.2 | HR system privacy configuration |
| `remote-work-monitoring` | A.7.2.5 | Remote work monitoring privacy |
| `whistleblower-data` | A.7.2.2 | Whistleblower data protection |
| `workplace-email-privacy` | 6.3.2.1 | Workplace email monitoring |

---

## 7. ISO/IEC 27701:2025 (Edition 2) Updates

ISO/IEC 27701:2025 was published as a significant revision of the 2019 edition. Organizations with existing ISO 27701:2019 certification must transition by 2028.

### 7.1 Key Structural Changes

| Change | 2019 Edition | 2025 Edition |
|--------|-------------|-------------|
| **Independence** | Extension of ISO 27001/27002 (cannot stand alone) | Standalone management system standard |
| **Structure** | Clauses 5-8 extending ISO 27001/27002 | Clauses 4-10 following ISO Harmonized Structure |
| **Annex A** | Separate Annex A (Controllers) and Annex B (Processors) | Consolidated Annex A with A.1 (Controllers), A.2 (Processors), A.3 (Shared) |
| **Annex B** | 18 processor controls | Merged into consolidated Annex A.2 (21 processor controls) |
| **Control Count** | 31 controller + 18 processor | 31 controller + 21 processor + 31 shared; 52 non-privacy controls removed |
| **Risk Management** | Implied | Formal privacy risk management requirement |
| **Terminology** | "Shall" and "should" mixed | Clear separation: "shall" for requirements, "should"/"may" for guidance |
| **Alignment** | ISO 27001:2013, ISO 27002:2013 | ISO 27001:2022, ISO 27002:2022 |

### 7.2 New and Modernized Controls

The 2025 edition addresses modern privacy challenges not present in the 2019 version:

| Area | New/Enhanced Controls | Relevant Skills |
|------|----------------------|-----------------|
| **AI and Machine Learning** | Privacy controls for AI systems, automated processing, algorithmic transparency | `ai-dpia`, `ai-automated-decisions`, `ai-transparency-reqs`, `ai-model-privacy-audit`, `ai-training-lawfulness` |
| **Cloud Computing** | Enhanced cloud privacy controls, multi-cloud data flows | `cloud-provider-assessment`, `cloud-migration-dpia`, `cloud-retention-config` |
| **IoT and Biometrics** | Biometric data processing, IoT privacy controls | `biometric-dpia`, `employee-biometric-data`, `dpia-biometric-systems` |
| **Cross-Border Transfers** | Updated transfer mechanisms aligned with evolving regulations | `transfer-impact-assessment`, `scc-implementation`, `eu-us-dpf-assessment`, `supplementary-measures` |
| **Privacy by Design** | Strengthened PbD/PbDefault requirements | `implementing-data-protection-by-default`, `applying-privacy-design-patterns`, `preparing-iso-31700-certification` |
| **Supply Chain** | Extended vendor and sub-processor privacy requirements | `sub-processor-management`, `vendor-monitoring-program`, `vendor-breach-cascade` |

### 7.3 Transition Mapping for Existing Skills

| 2019 Annex A/B | 2025 Annex A | Skills Impacted |
|----------------|-------------|-----------------|
| A.7.2.1-A.7.2.8 | A.1 (Controller collection/processing) | `lawful-basis-assessment`, `consent-record-keeping`, `conducting-gdpr-dpia`, `controller-ropa-creation` |
| A.7.3.1-A.7.3.10 | A.1 (Controller obligations) | `dsar-intake-system`, `right-to-erasure`, `data-portability`, `automated-decision-rights` |
| A.7.4.1-A.7.4.9 | A.1 (Controller PbD) + A.3 (Shared) | `implementing-data-minimization-architecture`, `retention-schedule`, `secure-data-destruction` |
| A.7.5.1-A.7.5.4 | A.1 (Controller transfers) | `transfer-impact-assessment`, `bcr-establishment`, `transfer-records` |
| B.8.2.1-B.8.2.6 | A.2 (Processor conditions) | `gdpr-dpa-art28`, `processor-ropa-creation` |
| B.8.3.1 | A.2 (Processor obligations) | `dsar-processing`, `employee-dsar-response` |
| B.8.4.1-B.8.4.3 | A.2 (Processor PbD) + A.3 (Shared) | `auto-deletion-workflow`, `vendor-termination-data` |
| B.8.5.1-B.8.5.8 | A.2 (Processor transfers) | `sub-processor-management`, `vendor-monitoring-program` |

---

## 8. Coverage Analysis

### 8.1 Coverage Summary

| ISO 27701 Domain | Total Controls | Skills Mapped | Coverage |
|------------------|---------------|---------------|----------|
| A.7.2 (Collection/Processing) | 8 | 8/8 | 100% |
| A.7.3 (PII Principal Obligations) | 10 | 10/10 | 100% |
| A.7.4 (Privacy by Design/Default) | 9 | 9/9 | 100% |
| A.7.5 (Transfer/Disclosure) | 4 | 4/4 | 100% |
| B.8.2 (Processor Collection/Processing) | 6 | 6/6 | 100% |
| B.8.3 (Processor PII Obligations) | 1 | 1/1 | 100% |
| B.8.4 (Processor PbD/PbDefault) | 3 | 3/3 | 100% |
| B.8.5 (Processor Transfer/Disclosure) | 8 | 8/8 | 100% |
| **Total Annex A + B** | **49** | **49/49** | **100%** |

### 8.2 Depth of Coverage by Control

| Coverage Depth | Description | Controls | Percentage |
|---------------|-------------|----------|------------|
| **Deep** (5+ skills) | Multiple dedicated skills with comprehensive templates, workflows, and automation | A.7.2.3, A.7.2.4, A.7.2.5, A.7.2.8, A.7.3.6, A.7.4.5, A.7.4.7, A.7.5.1 | 16% |
| **Strong** (3-4 skills) | Several skills addressing the control from different perspectives | A.7.2.1, A.7.2.2, A.7.2.6, A.7.3.1, A.7.3.2, A.7.3.4, A.7.3.8, A.7.4.1, A.7.4.4, A.7.4.8, B.8.2.5, B.8.5.7 | 24% |
| **Adequate** (2 skills) | Core coverage with at least two relevant skills | A.7.2.7, A.7.3.3, A.7.3.5, A.7.3.7, A.7.3.9, A.7.4.2, A.7.4.3, A.7.5.2, A.7.5.3, A.7.5.4, B.8.2.1, B.8.2.2, B.8.2.6, B.8.3.1, B.8.4.1, B.8.4.2, B.8.4.3, B.8.5.1, B.8.5.2, B.8.5.3, B.8.5.6, B.8.5.8 | 45% |
| **Basic** (1 skill) | Single skill covering the control | A.7.3.10, A.7.4.6, A.7.4.9, B.8.2.3, B.8.2.4, B.8.5.4, B.8.5.5 | 14% |

### 8.3 Skills with Broadest ISO 27701 Coverage

These skills map to the most ISO 27701 controls, representing cross-cutting capabilities:

| Skill | Controls Mapped | Primary Domain |
|-------|----------------|----------------|
| `gdpr-accountability` | 5.2.2, 5.4, A.7.2.1, A.7.3.1, Clause 6 | Governance and accountability |
| `dsar-processing` | A.7.3.5-A.7.3.9, B.8.2.5, B.8.3.1 | Data subject rights |
| `controller-ropa-creation` | A.7.2.8, A.7.5.3, 6.12.1.1 | Records management |
| `conducting-gdpr-dpia` | A.7.2.5, A.7.4.4 | Risk assessment |
| `transfer-impact-assessment` | A.7.5.1, B.8.5.1, 6.5.2.4 | International transfers |
| `sub-processor-management` | B.8.5.6, B.8.5.7, B.8.5.8, B.8.2.5 | Vendor management |
| `privacy-maturity-model` | 5.2.1, 5.2.4, Clause 5 | Organizational capability |
| `implementing-data-minimization-architecture` | A.7.4.1, A.7.4.4 | Data minimization |
| `lawful-basis-assessment` | A.7.2.1, A.7.2.2, B.8.2.2 | Legal basis |
| `consent-pref-center` | A.7.2.3, A.7.2.4, A.7.3.4 | Consent management |

### 8.4 Gap Analysis

| Area | Gap Description | Recommendation |
|------|----------------|----------------|
| **A.7.4.6 (Temporary files)** | Only indirect coverage via `auto-deletion-workflow` | Consider a dedicated temporary file management skill |
| **A.7.4.9 (Transmission controls)** | Covered through encryption skills but no dedicated transmission control skill | Consider a dedicated PII-in-transit control skill |
| **B.8.2.3 (Marketing restrictions - processor)** | Processor-specific marketing restriction is only indirectly covered | Consider processor-specific marketing compliance skill |
| **B.8.2.4 (Infringing instructions)** | No dedicated skill for handling unlawful controller instructions | Consider adding a processor instruction compliance skill |
| **B.8.5.4-B.8.5.5 (Legal disclosures)** | Limited coverage for government access request handling | Consider dedicated law enforcement request handling skill |
| **ISO 27701:2025 A.3 (Shared controls)** | New shared controls category not yet explicitly addressed | Update skills to reflect 2025 consolidated Annex A structure |

---

## 9. Implementation Guidance

### 9.1 Using This Mapping for ISO 27701 Certification

1. **Scope Definition**: Use skills mapped to Clause 5.2.3 (`data-inventory-mapping`, `data-flow-mapping`) to establish the PIMS scope
2. **Gap Assessment**: Cross-reference your organization's current state against the controls using `gdpr-gap-analysis` and `privacy-maturity-model`
3. **Controller Implementation**: Implement Annex A controls using the mapped skills in Section 2
4. **Processor Implementation**: If acting as a processor, implement Annex B controls using skills in Section 3
5. **Documentation**: Use ROPA skills (`controller-ropa-creation`, `processor-ropa-creation`) and audit skills (`gdpr-compliance-audit`, `internal-privacy-audit`) to maintain evidence
6. **Continuous Improvement**: Leverage `continuous-compliance`, `privacy-metrics-dashboard`, and `privacy-program-metrics` for ongoing monitoring

### 9.2 Certification Readiness Checklist

| Phase | Key Skills | ISO 27701 Clauses |
|-------|-----------|-------------------|
| **Planning** | `iso-27701-pims`, `privacy-maturity-model`, `data-inventory-mapping` | 5.2.1-5.2.4 |
| **Risk Assessment** | `audit-risk-assessment`, `dpia-risk-scoring`, `privacy-threshold-analysis` | 5.4.1.2-5.4.1.3 |
| **Implementation** | All Annex A/B mapped skills | 7.x, 8.x |
| **Internal Audit** | `internal-privacy-audit`, `gdpr-compliance-audit`, `audit-evidence-collect` | Clause 6 |
| **Management Review** | `privacy-metrics-dashboard`, `ropa-executive-dashboard` | 5.2.2 |
| **Certification Audit** | `dpa-inspection-prep`, `audit-report-writing`, `audit-follow-up-verify` | All |

---

## 10. References

### 10.1 ISO Standards

- **ISO/IEC 27701:2019** - Security techniques - Extension to ISO/IEC 27001 and ISO/IEC 27002 for privacy information management
- **ISO/IEC 27701:2025** - Privacy information management system (standalone standard, Edition 2)
- **ISO/IEC 27001:2022** - Information security management systems - Requirements
- **ISO/IEC 27002:2022** - Information security controls
- **ISO/IEC 29100:2011** - Privacy framework
- **ISO/IEC 27018:2019** - Code of practice for protection of PII in public clouds
- **ISO/IEC 29151:2017** - Code of practice for PII protection
- **ISO 31700-1:2023** - Consumer protection - Privacy by design for consumer goods and services

### 10.2 Regulatory References

- **GDPR** - Regulation (EU) 2016/679 - General Data Protection Regulation
- **CCPA/CPRA** - California Consumer Privacy Act / California Privacy Rights Act
- **HIPAA** - Health Insurance Portability and Accountability Act (US)
- **LGPD** - Lei Geral de Protecao de Dados (Brazil)
- **PIPL** - Personal Information Protection Law (China)
- **PIPEDA** - Personal Information Protection and Electronic Documents Act (Canada)
- **APPI** - Act on the Protection of Personal Information (Japan)

### 10.3 Implementation Resources

- BSI Group - ISO/IEC 27701 Implementation Guide
- NQA - ISO 27701 Annex A Controls Analysis
- ISMS.online - ISO 27701 Clause-by-Clause Reference
- Schellman - How to Prepare for ISO 27701:2025
- IAPP - ISO Updates Standard on Managing Privacy Compliance Programs
- Glocert International - ISO 27701:2025 Transition Guide

---

*This mapping document is maintained as part of the Privacy & Data Protection Skills repository. For the latest updates to ISO 27701 controls and skill mappings, consult the individual skill directories and their associated standards references.*
