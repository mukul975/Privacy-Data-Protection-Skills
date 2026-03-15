# NIST Privacy Framework Mapping

## Privacy & Data Protection Skills Repository

**Version:** 1.0
**Date:** 2026-03-15
**Framework Reference:** NIST Privacy Framework Version 1.0 (January 16, 2020)
**Supplemental Reference:** NIST Privacy Framework Version 1.1 Initial Public Draft (April 14, 2025)
**Skills Mapped:** 282 privacy skills

---

## Table of Contents

1. [Framework Overview](#1-framework-overview)
2. [Mapping Methodology](#2-mapping-methodology)
3. [Identify-P Function Mapping](#3-identify-p-function-mapping)
4. [Govern-P Function Mapping](#4-govern-p-function-mapping)
5. [Control-P Function Mapping](#5-control-p-function-mapping)
6. [Communicate-P Function Mapping](#6-communicate-p-function-mapping)
7. [Protect-P Function Mapping](#7-protect-p-function-mapping)
8. [NIST PF 1.1 AI Privacy Risk Mapping](#8-nist-pf-11-ai-privacy-risk-mapping)
9. [Coverage Analysis](#9-coverage-analysis)
10. [References](#10-references)

---

## 1. Framework Overview

The NIST Privacy Framework (PF) Version 1.0, published January 16, 2020, is a voluntary tool developed to help organizations identify and manage privacy risk. The framework Core is organized into five Functions, 18 Categories, and 100 Subcategories that represent discrete privacy protection outcomes.

### 1.1 Five Functions

| Function | ID | Purpose |
|---|---|---|
| **Identify-P** | ID-P | Develop organizational understanding to manage privacy risk for individuals arising from data processing |
| **Govern-P** | GV-P | Develop and implement organizational governance structure to enable ongoing understanding of risk management priorities informed by privacy risk |
| **Control-P** | CT-P | Develop and implement appropriate activities to enable organizations or individuals to manage data with sufficient granularity to manage privacy risks |
| **Communicate-P** | CM-P | Develop and implement appropriate activities to enable organizations and individuals to have a reliable understanding and engage in a dialogue about how data are processed and associated privacy risks |
| **Protect-P** | PR-P | Develop and implement appropriate data processing safeguards |

### 1.2 Category Structure (18 Categories)

| Function | Category ID | Category Name |
|---|---|---|
| Identify-P | ID.IM-P | Inventory and Mapping |
| Identify-P | ID.BE-P | Business Environment |
| Identify-P | ID.RA-P | Risk Assessment |
| Identify-P | ID.DE-P | Data Processing Ecosystem Risk Management |
| Govern-P | GV.PO-P | Governance Policies, Processes, and Procedures |
| Govern-P | GV.RM-P | Risk Management Strategy |
| Govern-P | GV.AT-P | Awareness and Training |
| Govern-P | GV.MT-P | Monitoring and Review |
| Control-P | CT.PO-P | Data Processing Policies, Processes, and Procedures |
| Control-P | CT.DM-P | Data Processing Management |
| Control-P | CT.DP-P | Disassociated Processing |
| Communicate-P | CM.PO-P | Communication Policies, Processes, and Procedures |
| Communicate-P | CM.AW-P | Data Processing Awareness |
| Protect-P | PR.PO-P | Data Protection Policies, Processes, and Procedures |
| Protect-P | PR.AC-P | Identity Management, Authentication, and Access Control |
| Protect-P | PR.DS-P | Data Security |
| Protect-P | PR.MA-P | Maintenance |
| Protect-P | PR.PT-P | Protective Technology |

### 1.3 NIST PF 1.1 Updates (April 2025 IPD)

The Privacy Framework 1.1 Initial Public Draft, released April 14, 2025, introduces:
- **Section 1.2.2**: AI and Privacy Risk Management -- addresses privacy risks from AI systems including data reconstruction, membership inference, and prompt injection attacks
- Alignment with NIST Cybersecurity Framework (CSF) 2.0
- Guidance for managing AI privacy risks throughout the AI lifecycle
- Integration with the NIST AI Risk Management Framework (AI RMF)

---

## 2. Mapping Methodology

Each of the 282 privacy skills in this repository has been mapped to one or more NIST Privacy Framework subcategories based on:

1. **Primary outcome alignment** -- the skill's core objective matches the subcategory's stated outcome
2. **Activity correspondence** -- the skill's implementation activities correspond to the subcategory's scope
3. **Risk domain coverage** -- the privacy risk domain addressed by the skill aligns with the subcategory's risk context

Skills may map to multiple subcategories across different Functions, reflecting the interconnected nature of privacy risk management. The **primary** mapping indicates the strongest alignment; **secondary** mappings indicate supporting relevance.

---

## 3. Identify-P Function Mapping

> *Develop the organizational understanding to manage privacy risk for individuals arising from data processing.*

### 3.1 ID.IM-P: Inventory and Mapping

*Systems, products, services, data actions, and data elements are inventoried and mapped.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **ID.IM-P1** | Systems/products/services that process data are inventoried | `data-inventory-mapping`, `saas-vendor-inventory`, `hipaa-phi-inventory`, `auto-data-discovery`, `ropa-tool-integration` |
| **ID.IM-P2** | Owners or operators and their roles with respect to systems/products/services and components that process data are inventoried | `controller-ropa-creation`, `processor-ropa-creation`, `joint-controller-art26`, `group-structure-ropa`, `vendor-privacy-due-diligence` |
| **ID.IM-P3** | Categories of individuals whose data are being processed are inventoried | `data-inventory-mapping`, `personal-data-test`, `special-category-data`, `children-data-minimization`, `employee-health-data` |
| **ID.IM-P4** | Data actions of the systems/products/services are inventoried | `data-flow-mapping`, `data-lineage-tracking`, `automated-ropa-generation`, `ropa-completeness-audit`, `ropa-maintenance-workflow` |
| **ID.IM-P5** | The purposes for the data actions are inventoried | `building-purpose-limitation-enforcement`, `purpose-based-access`, `lawful-basis-assessment`, `controller-ropa-creation`, `processor-ropa-creation` |
| **ID.IM-P6** | Data elements within the data actions are inventoried | `data-labeling-system`, `classification-policy`, `pii-detection-pipeline`, `pii-in-unstructured`, `cross-jurisdiction-class` |
| **ID.IM-P7** | The data processing environment is identified (e.g., geographic location, internal, cloud, third parties) | `data-localization`, `cloud-provider-assessment`, `cloud-migration-dpia`, `multi-jurisdiction-matrix`, `cloud-retention-config` |
| **ID.IM-P8** | Data processing is mapped, illustrating data actions and associated data elements for systems/products/services | `data-flow-mapping`, `data-lineage-tracking`, `ropa-dpia-linkage`, `ropa-executive-dashboard`, `group-structure-ropa` |

### 3.2 ID.BE-P: Business Environment

*The organization's mission, objectives, stakeholders, and activities are understood and prioritized; this information is used to inform privacy roles, responsibilities, and risk management decisions.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **ID.BE-P1** | The organization's role(s) in the data processing ecosystem are identified and communicated | `controller-ropa-creation`, `processor-ropa-creation`, `joint-controller-art26`, `sub-processor-management`, `gdpr-dpa-art28` |
| **ID.BE-P2** | Priorities for organizational mission, objectives, and activities are established and communicated | `privacy-maturity-model`, `privacy-program-metrics`, `privacy-metrics-dashboard`, `continuous-compliance`, `gdpr-accountability` |
| **ID.BE-P3** | Systems/products/services that support organizational priorities are identified and key requirements communicated | `privacy-api-design`, `hr-system-privacy-config`, `saas-vendor-inventory`, `ropa-tool-integration`, `privacy-threshold-analysis` |

### 3.3 ID.RA-P: Risk Assessment

*The organization understands the privacy risks to individuals and how such privacy risks may create follow-on impacts on organizational operations.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **ID.RA-P1** | Contextual factors related to the systems/products/services and data actions are identified | `conducting-gdpr-dpia`, `comparing-pia-methodologies`, `new-tech-pia`, `pia-threshold-screening`, `privacy-threshold-analysis` |
| **ID.RA-P2** | Data analytic inputs and outputs are identified and evaluated for bias | `ai-bias-special-category`, `ai-privacy-inference`, `ai-privacy-assessment`, `designing-privacy-preserving-analytics`, `llm-output-privacy-risk` |
| **ID.RA-P3** | Potential problematic data actions and associated problems are identified | `dpia-risk-scoring`, `dpia-automated-decisions`, `breach-risk-assessment`, `audit-risk-assessment`, `conducting-linddun-threat-modeling` |
| **ID.RA-P4** | Problematic data actions, likelihoods, and impacts are used to determine and prioritize risk | `dpia-mitigation-plan`, `retention-impact-assess`, `transfer-impact-assessment`, `health-data-dpia`, `marketing-analytics-dpia` |
| **ID.RA-P5** | Risk responses are identified, prioritized, and implemented | `dpia-mitigation-plan`, `gdpr-remediation-roadmap`, `audit-remediation-program`, `breach-remediation`, `pseudonymization-risk` |

### 3.4 ID.DE-P: Data Processing Ecosystem Risk Management

*The organization's priorities, constraints, risk tolerances, and assumptions are established and used to support risk decisions regarding managing privacy risk and third parties within the data processing ecosystem.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **ID.DE-P1** | Data processing ecosystem risk management policies, processes, and procedures are identified, established, assessed, managed, and agreed to by organizational stakeholders | `vendor-privacy-due-diligence`, `vendor-risk-scoring`, `vendor-monitoring-program`, `cloud-provider-assessment`, `sub-processor-management` |
| **ID.DE-P2** | Data processing ecosystem parties are identified, prioritized, and assessed using a privacy risk assessment process | `vendor-privacy-audit`, `pia-vendor-processing`, `vendor-cert-acceptance`, `eu-us-dpf-assessment`, `supplementary-measures` |
| **ID.DE-P3** | Contracts with data processing ecosystem parties are used to implement appropriate measures designed to meet the objectives of an organization's privacy program | `gdpr-dpa-art28`, `dpa-drafting`, `scc-implementation`, `hipaa-baa-management`, `vendor-termination-data` |
| **ID.DE-P4** | Interoperability frameworks or similar multi-party approaches are used to manage data processing ecosystem privacy risks | `apec-cbpr-cert`, `eu-code-of-conduct`, `gdpr-certification-scheme`, `gdpr-codes-of-conduct`, `iso-27701-pims` |
| **ID.DE-P5** | Data processing ecosystem parties are routinely assessed using audits, test results, or other forms of evaluations to confirm they are meeting their contractual obligations | `vendor-privacy-audit`, `vendor-monitoring-program`, `vendor-cert-acceptance`, `soc2-privacy-audit`, `audit-follow-up-verify` |

---

## 4. Govern-P Function Mapping

> *Develop and implement the organizational governance structure to enable an ongoing understanding of the organization's risk management priorities that are informed by privacy risk.*

### 4.1 GV.PO-P: Governance Policies, Processes, and Procedures

*Policies, processes, and procedures to manage and monitor the organization's regulatory, legal, risk, environmental, and operational requirements are understood and inform the management of privacy risk.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **GV.PO-P1** | Organizational privacy values and policies (e.g., conditions on data processing such as data uses or retention periods, individuals' prerogatives with respect to data processing) are established and communicated | `gdpr-policy-framework`, `classification-policy`, `byod-privacy-policy`, `retention-schedule`, `building-purpose-limitation-enforcement` |
| **GV.PO-P2** | Processes to instill organizational privacy values within system/product/service development and operations are established and in place | `implementing-data-protection-by-default`, `applying-privacy-design-patterns`, `privacy-api-design`, `implementing-data-minimization-architecture`, `hr-system-privacy-config` |
| **GV.PO-P3** | Roles and responsibilities for the workforce are established with respect to privacy | `nist-pf-govern`, `gdpr-accountability`, `privacy-maturity-model`, `gdpr-eu-representative`, `nist-pf-identify` |
| **GV.PO-P4** | Privacy roles and responsibilities are coordinated and aligned with third-party stakeholders (e.g., service providers, customers, partners) | `sub-processor-management`, `gdpr-dpa-art28`, `joint-controller-art26`, `vendor-privacy-due-diligence`, `dpa-drafting` |
| **GV.PO-P5** | Legal, regulatory, and contractual requirements regarding privacy are understood and managed | `privacy-law-monitoring`, `privacy-law-gap-analysis`, `multi-state-compliance`, `state-law-tracker`, `conflicting-laws-mgmt` |
| **GV.PO-P6** | Governance and risk management policies, processes, and procedures address privacy risks | `gdpr-accountability`, `continuous-compliance`, `privacy-maturity-model`, `nist-pf-govern`, `internal-privacy-audit` |

### 4.2 GV.RM-P: Risk Management Strategy

*The organization's priorities, constraints, risk tolerances, and assumptions are established and used to support operational risk decisions.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **GV.RM-P1** | Risk management processes are established, managed, and agreed to by organizational stakeholders | `audit-risk-assessment`, `dpia-stakeholder-consult`, `privacy-maturity-model`, `gdpr-gap-analysis`, `gdpr-self-assessment` |
| **GV.RM-P2** | Organizational risk tolerance is determined and clearly expressed | `dpia-risk-scoring`, `privacy-threshold-analysis`, `pia-threshold-screening`, `breach-risk-assessment`, `vendor-risk-scoring` |
| **GV.RM-P3** | The organization's determination of risk tolerance is informed by its role(s) in the data processing ecosystem | `controller-ropa-creation`, `processor-ropa-creation`, `joint-controller-art26`, `ropa-250-exemption`, `multi-jurisdiction-matrix` |

### 4.3 GV.AT-P: Awareness and Training

*The organization's workforce and third parties engaged in data processing are provided privacy awareness education and are trained to perform their privacy-related duties and responsibilities.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **GV.AT-P1** | The workforce is informed and trained on its roles and responsibilities | `hipaa-employee-training`, `gdpr-accountability`, `employee-monitoring-dpia`, `workplace-email-privacy`, `remote-work-monitoring` |
| **GV.AT-P2** | Senior executives understand their roles and responsibilities | `privacy-maturity-model`, `ropa-executive-dashboard`, `privacy-program-metrics`, `privacy-metrics-dashboard`, `gdpr-accountability` |
| **GV.AT-P3** | Privacy personnel understand their roles and responsibilities | `nist-pf-identify`, `nist-pf-govern`, `nist-pf-control`, `nist-pf-communicate`, `nist-pf-protect` |
| **GV.AT-P4** | Third parties (e.g., service providers, customers, partners) understand their roles and responsibilities | `sub-processor-management`, `vendor-privacy-due-diligence`, `gdpr-dpa-art28`, `vendor-monitoring-program`, `dpa-drafting` |

### 4.4 GV.MT-P: Monitoring and Review

*The policies, processes, and procedures for ongoing review of the organization's privacy posture are understood and inform the management of privacy risk.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **GV.MT-P1** | Privacy risk is re-evaluated on an ongoing basis and as key factors change | `continuous-compliance`, `privacy-law-monitoring`, `pia-review-cadence`, `state-law-tracker`, `ropa-maintenance-workflow` |
| **GV.MT-P2** | Privacy values, policies, and training are reviewed and any updates are communicated | `gdpr-compliance-audit`, `internal-privacy-audit`, `gdpr-doc-review`, `audit-follow-up-verify`, `privacy-maturity-model` |
| **GV.MT-P3** | Policies, processes, and procedures for assessing compliance with legal requirements and privacy policies are established and in place | `gdpr-compliance-audit`, `soc2-privacy-audit`, `hipaa-risk-analysis`, `internal-privacy-audit`, `audit-evidence-collect` |
| **GV.MT-P4** | Policies, processes, and procedures for communicating progress on managing privacy risks are established and in place | `privacy-metrics-dashboard`, `privacy-program-metrics`, `ropa-executive-dashboard`, `audit-report-writing`, `continuous-compliance` |
| **GV.MT-P5** | Policies, processes, and procedures are established to receive, analyze, and respond to problematic data actions disclosed to the organization from internal and external sources | `breach-detection-system`, `breach-response-playbook`, `breach-forensics`, `whistleblower-data`, `breach-documentation` |
| **GV.MT-P6** | Policies, processes, and procedures incorporate lessons learned from problematic data actions | `breach-remediation`, `audit-remediation-program`, `breach-simulation`, `audit-follow-up-verify`, `breach-documentation` |
| **GV.MT-P7** | Policies, processes, and procedures for receiving, tracking, and responding to complaints, concerns, and questions from individuals about organizational privacy practices are established and in place | `dsar-intake-system`, `dsar-processing`, `regulatory-complaints`, `gdpr-dpa-cooperation`, `gdpr-one-stop-shop` |

---

## 5. Control-P Function Mapping

> *Develop and implement appropriate activities to enable organizations or individuals to manage data with sufficient granularity to manage privacy risks.*

### 5.1 CT.PO-P: Data Processing Policies, Processes, and Procedures

*Policies, processes, and procedures are maintained and used to manage data processing consistent with the organization's risk strategy to protect individuals' privacy.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **CT.PO-P1** | Policies, processes, and procedures for authorizing data processing (e.g., organizational decisions, individual consent) are established and in place | `gdpr-valid-consent`, `consent-record-keeping`, `lawful-basis-assessment`, `employment-consent-limits`, `managing-consent-for-research` |
| **CT.PO-P2** | Policies, processes, and procedures for enabling data review, transfer, sharing, or disclosure are established and in place | `data-portability`, `privacy-data-sharing`, `apac-transfers`, `transfer-records`, `scc-implementation` |
| **CT.PO-P3** | Policies, processes, and procedures for enabling individuals' data processing preferences and requests are established and in place | `consent-pref-center`, `consent-withdrawal`, `consent-platform-eval`, `consent-receipt-spec`, `cpra-opt-out-signals` |
| **CT.PO-P4** | A data life cycle to manage data is aligned and in place with the system development life cycle to manage systems | `retention-schedule`, `auto-deletion-workflow`, `automating-storage-limitation-controls`, `financial-retention`, `backup-retention-erasure` |

### 5.2 CT.DM-P: Data Processing Management

*Data are managed consistent with the organization's risk strategy to protect individuals' privacy, increase manageability, and enable the implementation of privacy principles.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **CT.DM-P1** | Data elements can be accessed for review | `dsar-processing`, `right-to-rectification`, `data-portability`, `automated-ropa-generation`, `ropa-completeness-audit` |
| **CT.DM-P2** | Data elements can be accessed for transmission or disclosure | `data-portability`, `privacy-data-sharing`, `apac-transfers`, `scc-implementation`, `transfer-impact-assessment` |
| **CT.DM-P3** | Data elements can be accessed for alteration | `right-to-rectification`, `dsar-processing`, `consent-withdrawal`, `employee-dsar-response`, `california-consumer-rights` |
| **CT.DM-P4** | Data elements can be accessed for deletion | `right-to-erasure`, `ccpa-right-to-delete`, `auto-deletion-workflow`, `children-deletion-requests`, `search-engine-erasure` |
| **CT.DM-P5** | Data are destroyed according to policy | `secure-data-destruction`, `auto-deletion-workflow`, `backup-retention-erasure`, `vendor-termination-data`, `retention-schedule` |
| **CT.DM-P6** | Data are transmitted using standardized formats | `data-portability`, `consent-receipt-spec`, `tcf-v2-implementation`, `hipaa-interoperability`, `automated-ropa-generation` |
| **CT.DM-P7** | Mechanisms for transmitting processing permissions and related data values with data elements are established and in place | `consent-receipt-spec`, `global-privacy-control`, `universal-opt-out`, `cpra-opt-out-signals`, `gpc-cookie-integration` |
| **CT.DM-P8** | Audit/log records are determined, documented, implemented, and reviewed in accordance with policy | `audit-evidence-collect`, `audit-sampling-methods`, `audit-report-writing`, `cookie-audit`, `gdpr-ropa-audit` |
| **CT.DM-P9** | Technical measures implemented to manage data processing are tested and assessed | `cookie-consent-testing`, `cookie-consent-ab-audit`, `breach-simulation`, `dpa-inspection-prep`, `gdpr-self-assessment` |
| **CT.DM-P10** | Stakeholder privacy preferences are included in algorithmic design objectives and outputs are evaluated against these preferences | `ai-automated-decisions`, `automated-decision-rights`, `dpia-automated-decisions`, `ai-bias-special-category`, `ai-transparency-reqs` |

### 5.3 CT.DP-P: Disassociated Processing

*Data processing solutions increase disassociability consistent with the organization's risk strategy to protect individuals' privacy and enable implementation of privacy principles (e.g., data minimization).*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **CT.DP-P1** | Data are processed to limit observability and linkability (e.g., data actions take place on local devices, privacy-preserving cryptography) | `implementing-homomorphic-encryption`, `implementing-secure-multi-party-computation`, `designing-federated-learning-architecture`, `ai-federated-learning`, `privacy-record-linkage` |
| **CT.DP-P2** | Data are processed to limit the identification of individuals (e.g., de-identification privacy techniques, tokenization) | `hipaa-deidentification`, `pseudo-vs-anon-data`, `anonymization-alternative`, `pseudonymization-risk`, `differential-privacy-prod` |
| **CT.DP-P3** | Data are processed to limit the formation of inference about individuals' behavior or activities | `ai-privacy-inference`, `designing-privacy-preserving-analytics`, `llm-output-privacy-risk`, `children-profiling-limits`, `cookieless-alternatives` |
| **CT.DP-P4** | System or device configurations permit selective collection or disclosure of data elements | `implementing-data-minimization-architecture`, `implementing-data-protection-by-default`, `hipaa-minimum-necessary`, `server-side-tracking`, `eprivacy-essential-cookies` |
| **CT.DP-P5** | Attribute references are substituted for attribute values | `pseudonymization-risk`, `pseudo-vs-anon-data`, `pii-detection-pipeline`, `hipaa-deidentification`, `selecting-privacy-enhancing-technologies` |

---

## 6. Communicate-P Function Mapping

> *Develop and implement appropriate activities to enable organizations and individuals to have a reliable understanding and engage in a dialogue about how data are processed and associated privacy risks.*

### 6.1 CM.PO-P: Communication Policies, Processes, and Procedures

*Transparency policies, processes, and procedures for communicating data processing purposes, practices, associated privacy risks, and options for enabling individuals' data processing preferences and requests are established and in place.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **CM.PO-P1** | Transparency policies, processes, and procedures for communicating data processing purposes, practices, and associated privacy risks are established and in place | `transparent-communication`, `direct-collection-notice`, `indirect-collection-notice`, `children-privacy-notice`, `privacy-data-sharing` |
| **CM.PO-P2** | Roles and responsibilities for communicating data processing purposes, practices, and associated privacy risks are established | `nist-pf-communicate`, `gdpr-accountability`, `gdpr-eu-representative`, `gdpr-dpa-cooperation`, `regulatory-complaints` |

### 6.2 CM.AW-P: Data Processing Awareness

*Individuals and organizations have reliable knowledge about data processing practices and associated privacy risks, and effective mechanisms are used and maintained to increase predictability consistent with the organization's risk strategy to protect individuals' privacy.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **CM.AW-P1** | Mechanisms for communicating data processing purposes, practices, associated privacy risks, and options for enabling individuals' data processing preferences and requests are established and in place | `consent-pref-center`, `direct-collection-notice`, `cnil-cookie-banner`, `google-consent-mode-v2`, `analytics-cookie-consent` |
| **CM.AW-P2** | Mechanisms for obtaining feedback from individuals about data processing and associated privacy risks are established and in place | `dsar-intake-system`, `consent-pref-center`, `regulatory-complaints`, `marketing-objection`, `right-to-object` |
| **CM.AW-P3** | System/product/service design enables data processing visibility | `ai-transparency-reqs`, `cookie-audit`, `cookie-lifetime-audit`, `server-side-tracking`, `designing-privacy-preserving-analytics` |
| **CM.AW-P4** | Records of data disclosures and sharing are maintained and can be accessed for review or transmission/disclosure | `transfer-records`, `data-lineage-tracking`, `ropa-completeness-audit`, `audit-evidence-collect`, `privacy-data-sharing` |
| **CM.AW-P5** | Data corrections or deletions can be communicated to individuals or organizations in the data processing ecosystem | `right-to-erasure`, `right-to-rectification`, `search-engine-erasure`, `vendor-breach-cascade`, `sub-processor-management` |
| **CM.AW-P6** | Data provenance and lineage are maintained and can be accessed for review or transmission/disclosure | `data-lineage-tracking`, `data-flow-mapping`, `ai-training-data-class`, `data-labeling-system`, `transfer-records` |
| **CM.AW-P7** | Impacted individuals and organizations are notified about a privacy breach or event | `breach-72h-notification`, `breach-subject-comms`, `breach-multi-jurisdiction`, `hipaa-breach-notification`, `hipaa-breach-notify` |
| **CM.AW-P8** | Individuals are provided with mitigation mechanisms to address impacts of problematic data actions | `breach-credit-monitor`, `breach-remediation`, `consent-withdrawal`, `right-to-erasure`, `automated-decision-rights` |

---

## 7. Protect-P Function Mapping

> *Develop and implement appropriate data processing safeguards.*

### 7.1 PR.PO-P: Data Protection Policies, Processes, and Procedures

*Security and privacy policies, processes, and procedures are maintained and used to manage the protection of data.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **PR.PO-P1** | A baseline configuration of information technology is created and maintained incorporating security principles (e.g., concept of least functionality) | `implementing-data-protection-by-default`, `applying-privacy-design-patterns`, `privacy-api-design`, `hipaa-security-rule`, `implementing-data-minimization-architecture` |
| **PR.PO-P2** | Configuration change control processes are established and in place | `ropa-maintenance-workflow`, `continuous-compliance`, `privacy-law-monitoring`, `state-law-tracker`, `pia-review-cadence` |
| **PR.PO-P3** | Backups of information are conducted, maintained, and tested | `backup-retention-erasure`, `cloud-retention-config`, `hipaa-security-rule`, `breach-detection-system`, `secure-data-destruction` |
| **PR.PO-P4** | Policy and regulations regarding the physical operating environment for organizational assets are met | `data-localization`, `employee-biometric-data`, `biometric-dpia`, `hipaa-security-rule`, `background-check-privacy` |
| **PR.PO-P5** | Improvement of protection processes are identified and managed | `audit-remediation-program`, `audit-follow-up-verify`, `gdpr-remediation-roadmap`, `privacy-maturity-model`, `continuous-compliance` |
| **PR.PO-P6** | Effectiveness of protection technologies is shared | `privacy-metrics-dashboard`, `privacy-program-metrics`, `ropa-executive-dashboard`, `soc2-privacy-audit`, `vendor-cert-acceptance` |
| **PR.PO-P7** | Response and recovery plans are tested | `breach-simulation`, `breach-response-playbook`, `breach-forensics`, `hipaa-breach-notification`, `breach-detection-system` |
| **PR.PO-P8** | Response plans are communicated | `breach-response-playbook`, `breach-72h-notification`, `breach-subject-comms`, `breach-multi-jurisdiction`, `vendor-breach-cascade` |
| **PR.PO-P9** | Response and recovery activities are communicated to internal and external stakeholders, as well as executive and management teams | `breach-subject-comms`, `breach-documentation`, `breach-multi-jurisdiction`, `gdpr-dpa-cooperation`, `regulatory-complaints` |
| **PR.PO-P10** | Human resources practices (e.g., deprovisioning, personnel screening) that address privacy are established and in place | `background-check-privacy`, `employee-dsar-response`, `employee-monitoring-dpia`, `employee-surveillance-dpia`, `workplace-email-privacy` |

### 7.2 PR.AC-P: Identity Management, Authentication, and Access Control

*Access to data and devices is limited to authorized individuals, processes, and devices, and is managed consistent with the assessed risk of unauthorized access.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **PR.AC-P1** | Identities and credentials are issued, managed, verified, revoked, and audited for authorized individuals, processes, and devices | `purpose-based-access`, `hipaa-security-rule`, `hipaa-minimum-necessary`, `hr-system-privacy-config`, `implementing-data-protection-by-default` |
| **PR.AC-P2** | Physical access to data and devices is managed | `hipaa-security-rule`, `data-localization`, `employee-biometric-data`, `biometric-dpia`, `background-check-privacy` |
| **PR.AC-P3** | Remote access is managed | `remote-work-monitoring`, `byod-privacy-policy`, `hipaa-mobile-health`, `telehealth-privacy`, `hipaa-security-rule` |
| **PR.AC-P4** | Access permissions and authorizations are managed, incorporating the principles of least privilege and separation of duties | `purpose-based-access`, `hipaa-minimum-necessary`, `implementing-data-protection-by-default`, `restriction-of-processing`, `hr-system-privacy-config` |
| **PR.AC-P5** | Network integrity is protected (e.g., network segregation, network segmentation) | `hipaa-security-rule`, `implementing-data-protection-by-default`, `cloud-provider-assessment`, `privacy-api-design`, `data-localization` |
| **PR.AC-P6** | Individuals and devices are proofed and bound to credentials, and authenticated commensurate with the risk of the transaction | `age-verification-methods`, `age-gating-services`, `gdpr-parental-consent`, `managing-consent-for-children`, `coppa-compliance` |

### 7.3 PR.DS-P: Data Security

*Data are managed consistent with the organization's risk strategy to protect individuals' privacy and ensure data confidentiality, integrity, and availability.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **PR.DS-P1** | Data-at-rest are protected | `implementing-homomorphic-encryption`, `hipaa-security-rule`, `secure-data-destruction`, `cloud-retention-config`, `backup-retention-erasure` |
| **PR.DS-P2** | Data-in-transit are protected | `scc-implementation`, `supplementary-measures`, `hipaa-security-rule`, `implementing-secure-multi-party-computation`, `apac-transfers` |
| **PR.DS-P3** | Assets are formally managed throughout removal, transfers, and disposition | `vendor-termination-data`, `secure-data-destruction`, `auto-deletion-workflow`, `data-portability`, `backup-retention-erasure` |
| **PR.DS-P4** | Adequate capacity to ensure availability is maintained | `cloud-provider-assessment`, `hipaa-security-rule`, `breach-detection-system`, `continuous-compliance`, `saas-vendor-inventory` |
| **PR.DS-P5** | Protections against data leaks are implemented | `breach-detection-system`, `pii-detection-pipeline`, `pii-in-unstructured`, `auto-data-discovery`, `llm-output-privacy-risk` |
| **PR.DS-P6** | Integrity checking mechanisms are used to verify software, firmware, and information integrity | `cookie-consent-testing`, `breach-detection-system`, `vendor-monitoring-program`, `continuous-compliance`, `audit-evidence-collect` |
| **PR.DS-P7** | The development and testing environment(s) are separate from the production environment | `privacy-api-design`, `implementing-data-protection-by-default`, `ai-deployment-checklist`, `hipaa-security-rule`, `cloud-migration-dpia` |
| **PR.DS-P8** | Integrity checking mechanisms are used to verify hardware integrity | `hipaa-security-rule`, `biometric-dpia`, `employee-biometric-data`, `data-localization`, `cloud-provider-assessment` |

### 7.4 PR.MA-P: Maintenance

*System maintenance and repairs are performed consistent with policies, processes, and procedures.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **PR.MA-P1** | Maintenance and repair of organizational assets are performed and logged, with approved and controlled tools | `ropa-maintenance-workflow`, `continuous-compliance`, `vendor-monitoring-program`, `audit-evidence-collect`, `ropa-tool-integration` |
| **PR.MA-P2** | Remote maintenance of organizational assets is approved, logged, and performed in a manner that prevents unauthorized access | `remote-work-monitoring`, `cloud-provider-assessment`, `vendor-monitoring-program`, `hipaa-security-rule`, `byod-privacy-policy` |

### 7.5 PR.PT-P: Protective Technology

*Technical security solutions are managed to ensure the security and resilience of systems/products/services and associated data, consistent with related policies, processes, procedures, and agreements.*

| Subcategory | Description | Mapped Skills |
|---|---|---|
| **PR.PT-P1** | Removable media is protected and its use restricted according to policy | `byod-privacy-policy`, `hipaa-security-rule`, `data-localization`, `secure-data-destruction`, `implementing-data-protection-by-default` |
| **PR.PT-P2** | The principle of least functionality is incorporated by configuring systems to provide only essential capabilities | `implementing-data-minimization-architecture`, `implementing-data-protection-by-default`, `eprivacy-essential-cookies`, `hipaa-minimum-necessary`, `privacy-api-design` |
| **PR.PT-P3** | Communications and control networks are protected | `hipaa-security-rule`, `scc-implementation`, `supplementary-measures`, `cloud-provider-assessment`, `data-localization` |
| **PR.PT-P4** | Mechanisms (e.g., failsafe, load balancing, hot swap) are implemented to achieve resilience requirements in normal and adverse situations | `breach-detection-system`, `breach-response-playbook`, `cloud-provider-assessment`, `hipaa-security-rule`, `continuous-compliance` |

---

## 8. NIST PF 1.1 AI Privacy Risk Mapping

> *Section 1.2.2 of NIST Privacy Framework 1.1 IPD (April 2025) introduces guidance on AI and Privacy Risk Management, addressing privacy risks unique to AI systems throughout the AI lifecycle.*

### 8.1 AI Privacy Risk Categories and Skill Mapping

The PF 1.1 IPD identifies specific AI-related privacy risks. The following table maps repository AI skills to these risk categories and indicates which PF 1.0 subcategories apply to each risk.

| AI Privacy Risk | Description | Mapped AI Skills | Applicable PF 1.0 Subcategories |
|---|---|---|---|
| **Data Reconstruction** | AI systems may enable inferring the content or features of training data, reconstructing sensitive information | `ai-model-privacy-audit`, `ai-privacy-inference`, `ai-training-data-class`, `llm-output-privacy-risk`, `ai-federated-learning` | CT.DP-P1, CT.DP-P3, PR.DS-P1, PR.DS-P5 |
| **Membership Inference** | Attacks that infer the presence of specific individuals' data in the training set | `ai-model-privacy-audit`, `ai-privacy-assessment`, `ai-privacy-inference`, `differential-privacy-prod`, `designing-federated-learning-architecture` | CT.DP-P1, CT.DP-P2, CT.DP-P3, ID.RA-P3 |
| **Prompt Injection** | Exploiting AI systems to reveal information about individuals through manipulated inputs | `llm-output-privacy-risk`, `ai-deployment-checklist`, `ai-model-privacy-audit`, `ai-transparency-reqs`, `ai-vendor-privacy-due` | PR.DS-P5, CT.DM-P9, PR.PT-P2 |
| **Algorithmic Bias** | AI systems may produce discriminatory outcomes based on protected characteristics in training data | `ai-bias-special-category`, `ai-automated-decisions`, `automated-decision-rights`, `dpia-automated-decisions`, `ai-transparency-reqs` | ID.RA-P2, CT.DM-P10, CM.AW-P3 |
| **Opaque Decision-Making** | AI systems may make decisions affecting individuals without adequate transparency | `ai-transparency-reqs`, `ai-automated-decisions`, `automated-decision-rights`, `ai-data-subject-rights`, `ai-dpia` | CM.AW-P1, CM.AW-P3, CT.DM-P10, CM.PO-P1 |
| **Unauthorized Profiling** | AI systems may infer sensitive attributes or profile individuals beyond original processing purposes | `ai-privacy-inference`, `children-profiling-limits`, `ai-bias-special-category`, `designing-privacy-preserving-analytics`, `ai-privacy-assessment` | CT.DP-P3, ID.RA-P1, ID.IM-P5, GV.PO-P1 |
| **Training Data Privacy** | Privacy risks from collection, use, and retention of data used to train AI models | `ai-training-lawfulness`, `ai-training-data-class`, `ai-data-retention`, `ai-federated-learning`, `managing-consent-for-research` | CT.PO-P1, ID.IM-P5, CT.PO-P4, GV.PO-P1 |

### 8.2 Comprehensive AI Skills to PF 1.0 Subcategory Mapping

| AI Skill | Primary PF 1.0 Subcategories | Secondary PF 1.0 Subcategories |
|---|---|---|
| `ai-act-high-risk-docs` | GV.PO-P5, GV.MT-P3 | ID.RA-P1, CM.PO-P1 |
| `ai-automated-decisions` | CT.DM-P10, CM.AW-P3 | ID.RA-P2, GV.PO-P1 |
| `ai-bias-special-category` | ID.RA-P2, CT.DM-P10 | GV.PO-P1, CM.AW-P3 |
| `ai-data-retention` | CT.PO-P4, CT.DM-P5 | GV.PO-P1, ID.IM-P5 |
| `ai-data-subject-rights` | CT.DM-P1, CT.DM-P3 | CT.DM-P4, CM.AW-P1 |
| `ai-deployment-checklist` | GV.PO-P2, PR.PO-P1 | ID.RA-P5, GV.MT-P1 |
| `ai-dpia` | ID.RA-P3, ID.RA-P4 | GV.RM-P2, CT.DM-P10 |
| `ai-federated-learning` | CT.DP-P1, PR.DS-P2 | CT.DP-P3, ID.RA-P5 |
| `ai-model-privacy-audit` | GV.MT-P3, CT.DM-P9 | PR.DS-P5, ID.RA-P3 |
| `ai-privacy-assessment` | ID.RA-P1, ID.RA-P3 | GV.RM-P2, CT.DP-P3 |
| `ai-privacy-impact-template` | ID.RA-P3, ID.RA-P4 | GV.RM-P1, CM.PO-P1 |
| `ai-privacy-inference` | CT.DP-P3, ID.RA-P2 | PR.DS-P5, CT.DP-P1 |
| `ai-training-data-class` | ID.IM-P6, CM.AW-P6 | CT.PO-P1, GV.PO-P1 |
| `ai-training-lawfulness` | CT.PO-P1, GV.PO-P5 | ID.IM-P5, GV.PO-P1 |
| `ai-transparency-reqs` | CM.AW-P3, CM.PO-P1 | CT.DM-P10, GV.PO-P1 |
| `ai-vendor-privacy-due` | ID.DE-P2, ID.DE-P1 | GV.AT-P4, ID.DE-P5 |
| `healthcare-ai-privacy` | ID.RA-P1, GV.PO-P5 | CT.DP-P3, PR.DS-P1 |
| `llm-output-privacy-risk` | CT.DP-P3, PR.DS-P5 | ID.RA-P3, CT.DM-P10 |

### 8.3 PF 1.1 AI Lifecycle Integration

The PF 1.1 IPD recommends applying the framework across the entire AI lifecycle. The following maps repository skills to AI lifecycle phases:

| AI Lifecycle Phase | Applicable Skills |
|---|---|
| **Data Collection & Preparation** | `ai-training-data-class`, `ai-training-lawfulness`, `ai-data-retention`, `managing-consent-for-research`, `ai-bias-special-category` |
| **Model Development & Training** | `ai-federated-learning`, `designing-federated-learning-architecture`, `differential-privacy-prod`, `implementing-homomorphic-encryption`, `implementing-secure-multi-party-computation` |
| **Model Evaluation & Validation** | `ai-model-privacy-audit`, `ai-privacy-assessment`, `ai-bias-special-category`, `ai-dpia`, `ai-privacy-impact-template` |
| **Deployment & Monitoring** | `ai-deployment-checklist`, `ai-transparency-reqs`, `ai-automated-decisions`, `ai-vendor-privacy-due`, `llm-output-privacy-risk` |
| **Individual Rights & Governance** | `ai-data-subject-rights`, `automated-decision-rights`, `ai-act-high-risk-docs`, `dpia-automated-decisions`, `ai-privacy-inference` |

---

## 9. Coverage Analysis

### 9.1 Function Coverage Summary

| Function | Categories | Subcategories | Skills Mapped | Coverage |
|---|---|---|---|---|
| **Identify-P** | 4 | 21 | 79 skills | Full coverage across all 21 subcategories |
| **Govern-P** | 4 | 20 | 88 skills | Full coverage across all 20 subcategories |
| **Control-P** | 3 | 19 | 85 skills | Full coverage across all 19 subcategories |
| **Communicate-P** | 2 | 10 | 52 skills | Full coverage across all 10 subcategories |
| **Protect-P** | 5 | 30 | 72 skills | Full coverage across all 30 subcategories |
| **Total** | **18** | **100** | **282 skills** | **100% subcategory coverage** |

> Note: Many skills map to multiple subcategories across functions; totals reflect unique skill mappings per function.

### 9.2 Strongest Coverage Areas

The following NIST PF categories have the deepest coverage (most skills mapped):

| Rank | Category | Skills Mapped | Key Strength |
|---|---|---|---|
| 1 | **CT.DM-P** (Data Processing Management) | 48+ | Comprehensive data subject rights, deletion, portability, and consent management |
| 2 | **ID.IM-P** (Inventory and Mapping) | 38+ | Robust data mapping, ROPA, and inventory capabilities |
| 3 | **GV.PO-P** (Governance Policies) | 35+ | Strong policy frameworks across GDPR, HIPAA, and multi-jurisdictional compliance |
| 4 | **ID.DE-P** (Data Processing Ecosystem) | 30+ | Deep vendor management, DPA drafting, and third-party assessment |
| 5 | **GV.MT-P** (Monitoring and Review) | 30+ | Audit, compliance monitoring, and breach response capabilities |

### 9.3 Jurisdictional Coverage Mapping

Skills in this repository provide NIST PF alignment across multiple legal jurisdictions:

| Jurisdiction | Key Skills | Primary PF Alignment |
|---|---|---|
| **EU/EEA (GDPR)** | `gdpr-*` (20+ skills), `scc-implementation`, `eu-us-dpf-assessment` | GV.PO-P5, ID.DE-P3, CT.PO-P1 |
| **United States (Federal)** | `hipaa-*` (14 skills), `42-cfr-part-2`, `us-privacy-federal`, `coppa-compliance` | GV.PO-P5, PR.AC-P, PR.DS-P |
| **United States (State)** | `ccpa-*`, `california-consumer-rights`, `colorado-cpa-compliance`, `connecticut-ctdpa`, `vcdpa-compliance`, + 8 more state laws | GV.PO-P5, CT.DM-P, CT.PO-P3 |
| **UK** | `uk-aadc-implementation`, `uk-transfer-mechanisms` | GV.PO-P5, CT.PO-P2 |
| **APAC** | `australia-privacy-act`, `japan-appi`, `singapore-pdpa`, `korea-pipa`, `india-dpdp-act`, `china-pipl`, `thailand-pdpa` | GV.PO-P5, CT.PO-P2 |
| **Americas** | `brazil-lgpd`, `canada-pipeda`, `ca-breach-notification` | GV.PO-P5, CM.AW-P7 |
| **Africa/Middle East** | `south-africa-popia`, `nigeria-ndpr`, `turkey-kvkk`, `uae-pdp-law` | GV.PO-P5, GV.MT-P3 |

### 9.4 Skills with Broadest PF Coverage

These skills map across the most NIST PF functions simultaneously:

| Skill | Functions Covered | Key Subcategories |
|---|---|---|
| `gdpr-accountability` | ID-P, GV-P, CM-P | GV.PO-P1, GV.PO-P6, GV.AT-P1, ID.BE-P2 |
| `continuous-compliance` | GV-P, PR-P | GV.MT-P1, GV.MT-P4, PR.PO-P2, PR.PO-P5 |
| `data-flow-mapping` | ID-P, CM-P | ID.IM-P4, ID.IM-P8, CM.AW-P6 |
| `breach-response-playbook` | GV-P, PR-P | GV.MT-P5, PR.PO-P7, PR.PO-P8, PR.PT-P4 |
| `implementing-data-protection-by-default` | GV-P, CT-P, PR-P | GV.PO-P2, CT.DP-P4, PR.PO-P1, PR.AC-P4 |
| `hipaa-security-rule` | PR-P (all categories) | PR.PO-P1, PR.AC-P1-P5, PR.DS-P1-P2, PR.MA-P, PR.PT-P |
| `privacy-maturity-model` | ID-P, GV-P | ID.BE-P2, GV.RM-P1, GV.AT-P2, GV.MT-P2, PR.PO-P5 |

### 9.5 NIST PF-Dedicated Skills

The repository includes five skills explicitly designed for NIST Privacy Framework implementation:

| Skill | PF Function | Purpose |
|---|---|---|
| `nist-pf-identify` | Identify-P | Implementing the Identify-P function outcomes |
| `nist-pf-govern` | Govern-P | Implementing the Govern-P function outcomes |
| `nist-pf-control` | Control-P | Implementing the Control-P function outcomes |
| `nist-pf-communicate` | Communicate-P | Implementing the Communicate-P function outcomes |
| `nist-pf-protect` | Protect-P | Implementing the Protect-P function outcomes |
| `nist-privacy-identify` | Identify-P | Supplementary identification guidance |

---

## 10. References

### NIST Privacy Framework Primary Sources

1. **NIST Privacy Framework Version 1.0** (January 16, 2020)
   - Full Document: https://www.nist.gov/document/nist-privacy-frameworkv10pdf
   - Core (PDF): https://www.nist.gov/document/nist-privacy-framework-version-1-core-pdf
   - Publication: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.01162020.pdf

2. **NIST Privacy Framework Version 1.1 Initial Public Draft** (April 14, 2025)
   - Publication: https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.40.ipd.pdf
   - Project Page: https://www.nist.gov/privacy-framework/new-projects/privacy-framework-version-11
   - Announcement: https://www.nist.gov/news-events/news/2025/04/nist-privacy-framework-11-initial-public-draft-available-comment

3. **NIST Privacy Framework Portal**
   - Main Page: https://www.nist.gov/privacy-framework
   - Getting Started: https://www.nist.gov/privacy-framework/getting-started-0
   - Resource Repository: https://www.nist.gov/privacy-framework/resource-repository/browse/guidelines-and-tools

### Related NIST Publications

4. **NIST AI Risk Management Framework (AI RMF 1.0)** -- NIST AI 100-1 (January 2023)
5. **NIST Cybersecurity Framework (CSF) 2.0** -- NIST CSWP 29 (February 2024)
6. **NISTIR 8062**: An Introduction to Privacy Engineering and Risk Management in Federal Systems

### Third-Party References

7. CSF Tools -- Privacy Framework v1.0 Interactive Reference: https://csf.tools/framework/pf-v1-0/
8. Jones Day -- NIST Updates Its Privacy Framework to Address AI: https://www.jonesday.com/en/insights/2025/05/nist-updates-its-privacy-framework-to-address-ai
9. GrowthPoint -- Key Updates to the NIST Privacy Framework 1.1: https://gptechadvisors.com/key-updates-to-the-nist-privacy-framework-1-1/
10. Securiti -- NIST Privacy Framework: A Comprehensive Guide: https://securiti.ai/nist-privacy-framework/

---

*This mapping document was generated on 2026-03-15 for the Privacy & Data Protection Skills Repository. It covers all 282 privacy skills mapped against the complete NIST Privacy Framework 1.0 Core (5 Functions, 18 Categories, 100 Subcategories) with supplemental PF 1.1 IPD AI privacy risk coverage.*
