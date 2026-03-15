# OWASP Top 10 Privacy Risks Mapping

## Repository Skills-to-OWASP Privacy Risks Cross-Reference

**Version:** 1.0
**Date:** 2026-03-15
**Framework:** OWASP Top 10 Privacy Risks v2.0 (2021)
**Skills Mapped:** 282 privacy skills

---

## Table of Contents

1. [Overview](#overview)
2. [OWASP Top 10 Privacy Risks Summary](#owasp-top-10-privacy-risks-summary)
3. [Detailed Mapping by Risk](#detailed-mapping-by-risk)
   - [P1: Web Application Vulnerabilities](#p1-web-application-vulnerabilities)
   - [P2: Operator-sided Data Leakage](#p2-operator-sided-data-leakage)
   - [P3: Insufficient Data Breach Response](#p3-insufficient-data-breach-response)
   - [P4: Consent on Everything](#p4-consent-on-everything)
   - [P5: Non-transparent Policies, Terms and Conditions](#p5-non-transparent-policies-terms-and-conditions)
   - [P6: Insufficient Deletion of Personal Data](#p6-insufficient-deletion-of-personal-data)
   - [P7: Insufficient Data Quality](#p7-insufficient-data-quality)
   - [P8: Missing or Insufficient Session Expiration](#p8-missing-or-insufficient-session-expiration)
   - [P9: Inability of Users to Access and Modify Data](#p9-inability-of-users-to-access-and-modify-data)
   - [P10: Collection of Data Not Required for the User-Consented Purpose](#p10-collection-of-data-not-required-for-the-user-consented-purpose)
4. [Skills-to-Risks Cross-Reference Table](#skills-to-risks-cross-reference-table)
5. [Coverage Analysis](#coverage-analysis)
6. [Integration Guidance](#integration-guidance)
7. [References](#references)

---

## Overview

This document maps the 282 privacy skills in the `skills/privacy/` directory of this repository to the **OWASP Top 10 Privacy Risks v2.0** framework. The OWASP Top 10 Privacy Risks project provides a ranked list of the most critical privacy risks in web applications and systems, covering both technological and organizational aspects grounded in real-world risks rather than purely legal concerns.

The mapping serves multiple purposes:

- **Gap identification** -- Reveals which OWASP privacy risks have strong skill coverage and which need additional development.
- **Compliance alignment** -- Connects operational privacy skills to an industry-recognized risk framework.
- **Training prioritization** -- Helps organizations focus skill-building efforts on the highest-risk areas.
- **Audit readiness** -- Provides a structured cross-reference for privacy audits that reference OWASP standards.

Each skill may map to one or more OWASP risks. The mapping considers both primary (direct mitigation) and secondary (supporting/contributory) relationships.

---

## OWASP Top 10 Privacy Risks Summary

The OWASP Top 10 Privacy Risks v2.0 (2021) identifies the following risks, ranked by severity:

| Rank | ID | Risk Name | Description |
|------|-----|-----------|-------------|
| 1 | **P1** | Web Application Vulnerabilities | Failure to design, implement, test, or patch applications that guard sensitive user data, encompassing the OWASP Top 10 web application security vulnerabilities and the privacy risks they create. |
| 2 | **P2** | Operator-sided Data Leakage | Failure to prevent leakage of user data to unauthorized parties, whether through intentional breach or unintentional error such as insufficient access controls, insecure storage, data duplication, or lack of awareness. |
| 3 | **P3** | Insufficient Data Breach Response | Not informing affected data subjects about breaches or data leaks (intentional or unintentional), failing to remedy the cause, and not attempting to limit the impact. |
| 4 | **P4** | Consent on Everything | Aggregation or inappropriate use of consent to legitimize processing. Consent is bundled ("on everything") rather than collected separately for each distinct purpose. |
| 5 | **P5** | Non-transparent Policies, Terms and Conditions | Not providing sufficient, easily accessible, and understandable information about how data is collected, stored, and processed. |
| 6 | **P6** | Insufficient Deletion of Personal Data | Failure to effectively and/or timely delete personal data after the specified purpose has ended or upon user request. |
| 7 | **P7** | Insufficient Data Quality | Use of outdated, incorrect, or bogus user data, combined with failure to update or correct it. |
| 8 | **P8** | Missing or Insufficient Session Expiration | Failure to enforce session termination effectively, resulting in collection of additional user data without consent or awareness. |
| 9 | **P9** | Inability of Users to Access and Modify Data | Users lack the ability to access, change, or delete data related to them. |
| 10 | **P10** | Collection of Data Not Required for the User-Consented Purpose | Collecting descriptive, demographic, or other user-related data not needed for system purposes or for which the user did not provide consent. |

---

## Detailed Mapping by Risk

### P1: Web Application Vulnerabilities

**Risk Description:** Vulnerability is a key problem in any system that guards or operates on sensitive user data. Failure to suitably design and implement an application, detect a problem, or promptly apply a fix (patch) is likely to result in a privacy breach. This encompasses the OWASP Top 10 List of web application security vulnerabilities.

**Key Countermeasures:** Secure development lifecycle, regular vulnerability scanning, penetration testing, patch management, security-by-design architecture, privacy-by-design patterns.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `privacy-api-design` | Primary | Designing APIs with privacy controls directly addresses application-level vulnerabilities. |
| `implementing-data-protection-by-default` | Primary | Building default protections into application architecture mitigates vulnerability exposure. |
| `applying-privacy-design-patterns` | Primary | Privacy design patterns prevent architectural vulnerabilities that lead to data exposure. |
| `conducting-linddun-threat-modeling` | Primary | LINDDUN threat modeling identifies privacy-specific application vulnerabilities. |
| `linddun-threat-model` | Primary | Directly models privacy threats in application design. |
| `ai-deployment-checklist` | Primary | Pre-deployment security/privacy checks for AI systems. |
| `ai-privacy-assessment` | Primary | Assesses AI systems for privacy vulnerabilities. |
| `ai-privacy-impact-template` | Primary | Structured privacy impact assessment for AI applications. |
| `ai-model-privacy-audit` | Primary | Audits AI models for privacy-related vulnerabilities. |
| `cloud-migration-dpia` | Secondary | DPIAs for cloud migration identify vulnerability risks. |
| `cloud-provider-assessment` | Secondary | Evaluates cloud vendor security posture. |
| `implementing-homomorphic-encryption` | Secondary | Cryptographic protection reduces vulnerability impact. |
| `implementing-secure-multi-party-computation` | Secondary | Secure computation prevents data exposure through processing. |
| `differential-privacy-prod` | Secondary | Reduces data exposure even when vulnerabilities exist. |
| `designing-federated-learning-architecture` | Secondary | Distributed architecture reduces centralized vulnerability surface. |
| `selecting-privacy-enhancing-technologies` | Secondary | PETs selection addresses technical vulnerability mitigation. |
| `pii-detection-pipeline` | Secondary | Automated PII detection catches vulnerabilities in data handling. |
| `pii-in-unstructured` | Secondary | Finding PII in unstructured data prevents unintended exposure. |
| `biometric-dpia` | Secondary | Biometric systems require heightened vulnerability assessment. |
| `health-data-dpia` | Secondary | Health data systems need rigorous vulnerability controls. |
| `dpia-biometric-systems` | Secondary | Assesses biometric system vulnerabilities. |
| `hipaa-security-rule` | Secondary | HIPAA security requirements address application security. |
| `hipaa-risk-analysis` | Secondary | Risk analysis identifies application vulnerabilities. |
| `soc2-privacy-audit` | Secondary | SOC2 audits evaluate application security controls. |
| `internal-privacy-audit` | Secondary | Internal audits identify vulnerability gaps. |
| `gdpr-compliance-audit` | Secondary | GDPR audits include technical security assessment. |
| `new-tech-pia` | Secondary | New technology assessments catch vulnerability risks early. |
| `edtech-privacy-assessment` | Secondary | EdTech assessments evaluate application vulnerabilities. |

**Skill Count:** 28 skills (10 primary, 18 secondary)

---

### P2: Operator-sided Data Leakage

**Risk Description:** Failure to prevent the leakage of any information containing or related to user data, or the data itself, to any unauthorized party. Caused by intentional malicious breach or unintentional mistakes such as insufficient access management, insecure storage, data duplication, or lack of awareness.

**Key Countermeasures:** Encryption of personal data, identity and access management, anonymization/pseudonymization, awareness campaigns, ISO 27001/27002 controls, data loss prevention.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `implementing-homomorphic-encryption` | Primary | Encryption of data in use prevents leakage during processing. |
| `implementing-secure-multi-party-computation` | Primary | Prevents data exposure during multi-party computation. |
| `differential-privacy-prod` | Primary | Differential privacy prevents data leakage through query results. |
| `anonymization-alternative` | Primary | Anonymization eliminates identifiability if data leaks. |
| `pseudo-vs-anon-data` | Primary | Proper pseudonymization/anonymization reduces leakage impact. |
| `pseudonymization-risk` | Primary | Risk assessment of pseudonymization effectiveness. |
| `implementing-data-minimization-architecture` | Primary | Minimized data reduces leakage surface area. |
| `data-localization` | Primary | Data localization controls reduce cross-border leakage risk. |
| `secure-data-destruction` | Primary | Proper destruction prevents leakage from decommissioned storage. |
| `classification-policy` | Primary | Data classification drives appropriate protection levels. |
| `data-flow-mapping` | Primary | Mapping flows identifies leakage exposure points. |
| `data-inventory-mapping` | Primary | Knowing what data exists prevents uncontrolled leakage. |
| `data-lineage-tracking` | Primary | Tracking data lineage identifies leakage vectors. |
| `data-labeling-system` | Primary | Labeling ensures proper handling to prevent leakage. |
| `pii-detection-pipeline` | Primary | Automated PII detection catches data before it leaks. |
| `pii-in-unstructured` | Primary | Finding hidden PII in unstructured data prevents leakage. |
| `privacy-record-linkage` | Primary | Controls re-identification risk that compounds leakage. |
| `purpose-based-access` | Primary | Limits access to data per purpose, reducing leakage risk. |
| `auto-data-discovery` | Primary | Automated discovery finds data that might leak unmonitored. |
| `designing-privacy-preserving-analytics` | Primary | Privacy-preserving analytics prevents leakage through insights. |
| `cloud-provider-assessment` | Secondary | Ensures cloud operators have leakage controls. |
| `cloud-retention-config` | Secondary | Proper cloud retention limits leakage exposure window. |
| `vendor-privacy-audit` | Secondary | Auditing vendors prevents third-party leakage. |
| `vendor-privacy-due-diligence` | Secondary | Due diligence prevents selecting vendors prone to leakage. |
| `vendor-monitoring-program` | Secondary | Ongoing monitoring catches vendor-side leakage. |
| `vendor-risk-scoring` | Secondary | Risk scoring prioritizes vendor leakage controls. |
| `vendor-termination-data` | Secondary | Proper data handling at termination prevents leakage. |
| `vendor-breach-cascade` | Secondary | Understanding cascade effects of vendor breaches. |
| `sub-processor-management` | Secondary | Managing sub-processors prevents downstream leakage. |
| `saas-vendor-inventory` | Secondary | Inventorying SaaS vendors identifies leakage exposure. |
| `dpa-drafting` | Secondary | DPA clauses require leakage prevention controls. |
| `gdpr-dpa-art28` | Secondary | Article 28 agreements mandate processor leakage controls. |
| `employee-monitoring-dpia` | Secondary | Monitoring assessments address employee data leakage. |
| `employee-surveillance-dpia` | Secondary | Surveillance assessments identify leakage risks. |
| `byod-privacy-policy` | Secondary | BYOD policies prevent device-based data leakage. |
| `remote-work-monitoring` | Secondary | Remote work controls prevent decentralized leakage. |
| `workplace-email-privacy` | Secondary | Email privacy controls prevent communication leakage. |
| `backup-retention-erasure` | Secondary | Backup controls prevent leakage from residual copies. |
| `hipaa-minimum-necessary` | Secondary | Minimum necessary standard limits leakage exposure. |
| `hipaa-deidentification` | Secondary | De-identification prevents leakage of health identifiers. |
| `supplementary-measures` | Secondary | Additional transfer safeguards prevent cross-border leakage. |
| `scc-implementation` | Secondary | SCCs include leakage protection obligations. |
| `transfer-impact-assessment` | Secondary | Transfer assessments evaluate leakage risk. |
| `iso-27701-pims` | Secondary | ISO 27701 mandates leakage prevention controls. |
| `nist-pf-protect` | Secondary | NIST Protect function addresses leakage prevention. |
| `llm-output-privacy-risk` | Secondary | LLM outputs can leak training data or PII. |
| `ai-privacy-inference` | Secondary | AI inference can leak sensitive information. |
| `server-side-tracking` | Secondary | Server-side tracking controls prevent leakage to third parties. |

**Skill Count:** 48 skills (20 primary, 28 secondary)

---

### P3: Insufficient Data Breach Response

**Risk Description:** Not informing affected data subjects about a possible breach or data leak; failure to remedy the situation by fixing the cause; not attempting to limit the leaks. Applies to both intentional and unintentional events.

**Key Countermeasures:** Incident response plan, incident management team, periodic testing of response plans, breach notification procedures, forensic capabilities, remediation workflows.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `breach-response-playbook` | Primary | Defines the complete breach response workflow. |
| `breach-detection-system` | Primary | Detection is the first step in effective breach response. |
| `breach-72h-notification` | Primary | GDPR 72-hour notification obligation. |
| `breach-documentation` | Primary | Documenting breaches for regulatory compliance. |
| `breach-forensics` | Primary | Forensic investigation to identify breach cause. |
| `breach-multi-jurisdiction` | Primary | Managing breach response across multiple legal jurisdictions. |
| `breach-remediation` | Primary | Fixing the root cause after a breach. |
| `breach-risk-assessment` | Primary | Assessing breach severity and risk to data subjects. |
| `breach-simulation` | Primary | Testing breach response through simulation exercises. |
| `breach-subject-comms` | Primary | Communicating with affected data subjects after a breach. |
| `breach-credit-monitor` | Primary | Providing credit monitoring to affected individuals. |
| `vendor-breach-cascade` | Primary | Managing cascade effects when a vendor experiences a breach. |
| `ca-breach-notification` | Primary | California-specific breach notification requirements. |
| `hipaa-breach-notification` | Primary | HIPAA breach notification rule compliance. |
| `hipaa-breach-notify` | Primary | HIPAA-specific breach notification procedures. |
| `gdpr-dpa-cooperation` | Secondary | Cooperating with DPAs during breach investigations. |
| `dpa-inspection-prep` | Secondary | Preparing for DPA inspections following breaches. |
| `regulatory-complaints` | Secondary | Handling regulatory complaints arising from breaches. |
| `audit-remediation-program` | Secondary | Post-breach remediation through audit programs. |
| `audit-follow-up-verify` | Secondary | Verifying breach remediation effectiveness. |
| `privacy-metrics-dashboard` | Secondary | Dashboards track breach response metrics. |
| `privacy-program-metrics` | Secondary | Program metrics include breach response KPIs. |
| `continuous-compliance` | Secondary | Continuous compliance includes breach readiness monitoring. |

**Skill Count:** 23 skills (15 primary, 8 secondary)

---

### P4: Consent on Everything

**Risk Description:** Aggregation or inappropriate use of consent to legitimize processing. Consent is "on everything" -- not collected separately for each distinct purpose (e.g., bundling website use consent with advertising profiling consent).

**Key Countermeasures:** Granular, purpose-specific consent collection; distinct consent for each processing purpose; opt-in mechanisms for non-essential processing; consent management platforms; regular consent audits.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `gdpr-valid-consent` | Primary | Ensures consent meets GDPR validity requirements (granular, specific, freely given). |
| `consent-pref-center` | Primary | Preference centers enable granular, purpose-specific consent. |
| `consent-record-keeping` | Primary | Recording consent separately per purpose demonstrates granularity. |
| `consent-receipt-spec` | Primary | Consent receipts document specific purposes consented to. |
| `consent-withdrawal` | Primary | Enables withdrawal of consent for specific purposes. |
| `consent-for-transfers` | Primary | Separate consent for data transfers. |
| `consent-platform-eval` | Primary | Evaluating platforms for granular consent capabilities. |
| `managing-consent-for-children` | Primary | Child consent requires heightened specificity. |
| `managing-consent-for-research` | Primary | Research consent must be purpose-specific. |
| `managing-mobile-app-consent` | Primary | Mobile consent must be granular and non-bundled. |
| `gdpr-parental-consent` | Primary | Parental consent requirements for children's data. |
| `employment-consent-limits` | Primary | Employment context limits bundled consent. |
| `analytics-cookie-consent` | Primary | Separate consent for analytics cookies. |
| `cnil-compliant-cookies` | Primary | CNIL requires specific consent for cookie categories. |
| `cnil-cookie-banner` | Primary | Cookie banners must offer granular choices. |
| `cookie-consent-ab-audit` | Primary | Auditing consent A/B testing for manipulation. |
| `cookie-consent-testing` | Primary | Testing cookie consent for proper granularity. |
| `google-consent-mode-v2` | Primary | Google Consent Mode v2 supports granular consent signals. |
| `tcf-v2-implementation` | Primary | IAB Transparency and Consent Framework v2 enables purpose-level consent. |
| `double-opt-in-email` | Primary | Double opt-in ensures affirmative, specific consent. |
| `cpra-opt-out-signals` | Secondary | Opt-out mechanisms complement granular consent. |
| `universal-opt-out` | Secondary | Universal opt-out supports disaggregated consent choices. |
| `global-privacy-control` | Secondary | GPC as a mechanism to disaggregate consent. |
| `gpc-cookie-integration` | Secondary | Integrating GPC with cookie consent for granular control. |
| `lawful-basis-assessment` | Secondary | Ensures consent is used only where appropriate, not as a catch-all. |
| `legitimate-interest-lia` | Secondary | LIA provides alternative to inappropriate blanket consent. |
| `legit-interest-vs-consent` | Secondary | Distinguishing when consent vs. legitimate interest applies. |
| `building-purpose-limitation-enforcement` | Secondary | Purpose limitation prevents consent overreach. |
| `california-consumer-rights` | Secondary | California rights include consent-related protections. |
| `ccpa-consumer-requests` | Secondary | Consumer request handling includes consent preferences. |

**Skill Count:** 30 skills (20 primary, 10 secondary)

---

### P5: Non-transparent Policies, Terms and Conditions

**Risk Description:** Not providing sufficient information describing how data is processed, including collection, storage, and processing. Failure to make this information easily accessible and understandable for non-lawyers.

**Key Countermeasures:** Specific, differentiated terms and conditions; plain-language privacy notices; layered privacy information; accessible data processing descriptions; regular policy reviews and updates.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `transparent-communication` | Primary | Directly addresses clear privacy communication to data subjects. |
| `direct-collection-notice` | Primary | Notices at point of collection ensure transparency. |
| `indirect-collection-notice` | Primary | Notices when data is obtained from third parties. |
| `children-privacy-notice` | Primary | Age-appropriate transparency for children. |
| `gdpr-policy-framework` | Primary | GDPR-compliant policy frameworks ensure transparency. |
| `gdpr-doc-review` | Primary | Document review ensures policies remain accurate and transparent. |
| `privacy-law-monitoring` | Primary | Monitoring law changes keeps policies current. |
| `privacy-threshold-analysis` | Primary | Threshold analysis determines when transparency obligations apply. |
| `nist-pf-communicate` | Primary | NIST Privacy Framework Communicate function addresses transparency. |
| `eprivacy-essential-cookies` | Secondary | ePrivacy cookie classification supports transparent disclosure. |
| `cookie-audit` | Secondary | Auditing cookies ensures accurate privacy disclosures. |
| `cookieless-alternatives` | Secondary | Transparent alternatives to opaque cookie tracking. |
| `cookie-lifetime-audit` | Secondary | Auditing cookie lifetimes supports accurate disclosures. |
| `privacy-data-sharing` | Secondary | Data sharing arrangements require transparent disclosure. |
| `gdpr-accountability` | Secondary | Accountability principle underpins transparency obligations. |
| `gdpr-codes-of-conduct` | Secondary | Codes of conduct standardize transparent practices. |
| `eu-code-of-conduct` | Secondary | EU codes promote standardized transparency. |
| `multi-jurisdiction-matrix` | Secondary | Multi-jurisdiction policies require tailored transparency. |
| `cross-jurisdiction-cookies` | Secondary | Cross-jurisdiction cookie compliance requires transparent disclosures. |
| `telehealth-privacy` | Secondary | Telehealth requires specific transparent disclosures. |
| `uk-aadc-implementation` | Secondary | Age-appropriate design code requires child-friendly transparency. |

**Skill Count:** 21 skills (9 primary, 12 secondary)

---

### P6: Insufficient Deletion of Personal Data

**Risk Description:** Failure to effectively and/or timely delete personal data after termination of the specified purpose or upon request by the data subject.

**Key Countermeasures:** Defined retention periods per data category, automated deletion processes, verified deletion workflows, right to erasure procedures, backup and archive deletion, vendor data deletion verification.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `right-to-erasure` | Primary | Directly implements data subject right to deletion. |
| `ccpa-right-to-delete` | Primary | CCPA-specific right to delete implementation. |
| `auto-deletion-workflow` | Primary | Automated workflows ensure timely deletion. |
| `secure-data-destruction` | Primary | Secure destruction ensures complete and irreversible deletion. |
| `retention-schedule` | Primary | Defined schedules trigger deletion at purpose expiry. |
| `retention-impact-assess` | Primary | Assessing retention impact drives appropriate deletion. |
| `retention-exception-mgmt` | Primary | Managing exceptions to standard deletion timelines. |
| `automating-storage-limitation-controls` | Primary | Automated storage limitation enforces deletion requirements. |
| `backup-retention-erasure` | Primary | Ensuring deletion extends to backup copies. |
| `cloud-retention-config` | Primary | Configuring cloud retention for automated deletion. |
| `financial-retention` | Primary | Financial data retention and deletion requirements. |
| `children-deletion-requests` | Primary | Children's data deletion requests require prompt handling. |
| `litigation-hold-mgmt` | Primary | Managing deletion pauses during litigation holds. |
| `vendor-termination-data` | Primary | Ensuring vendor data deletion at contract end. |
| `search-engine-erasure` | Primary | Right to erasure from search engine results. |
| `hipaa-phi-inventory` | Secondary | PHI inventory supports identification of data for deletion. |
| `data-inventory-mapping` | Secondary | Inventory enables comprehensive deletion. |
| `auto-data-discovery` | Secondary | Discovering data ensures nothing is missed during deletion. |
| `controller-ropa-creation` | Secondary | ROPA identifies what data requires deletion. |
| `processor-ropa-creation` | Secondary | Processor ROPA tracks delegated deletion obligations. |

**Skill Count:** 20 skills (15 primary, 5 secondary)

---

### P7: Insufficient Data Quality

**Risk Description:** The use of outdated, incorrect, or bogus user data. Failure to update or correct data upon user request or proactive identification.

**Key Countermeasures:** Data quality checks, user-facing correction mechanisms, right to rectification processes, data validation, regular data quality audits, data lifecycle management.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `right-to-rectification` | Primary | Directly enables data subjects to correct their data. |
| `data-lineage-tracking` | Primary | Lineage tracking ensures corrections propagate correctly. |
| `data-inventory-mapping` | Primary | Inventory enables systematic data quality management. |
| `data-labeling-system` | Primary | Labeling supports quality classification and tracking. |
| `ropa-completeness-audit` | Primary | Auditing ROPA completeness ensures data records are accurate. |
| `ropa-maintenance-workflow` | Primary | Ongoing maintenance keeps records current. |
| `gdpr-ropa-audit` | Primary | GDPR ROPA audits verify data accuracy. |
| `hipaa-phi-inventory` | Secondary | PHI inventory maintenance supports data quality. |
| `personal-data-test` | Secondary | Testing personal data identification supports quality. |
| `ai-data-retention` | Secondary | AI data retention policies address data currency. |
| `ai-training-data-class` | Secondary | Training data classification supports quality controls. |
| `dsar-processing` | Secondary | Processing DSARs reveals data quality issues. |
| `dsar-intake-system` | Secondary | DSAR intake captures data quality correction requests. |
| `employee-dsar-response` | Secondary | Employee DSARs include rectification requests. |
| `privacy-metrics-dashboard` | Secondary | Dashboards track data quality metrics. |

**Skill Count:** 15 skills (7 primary, 8 secondary)

---

### P8: Missing or Insufficient Session Expiration

**Risk Description:** Failure to effectively enforce session termination. May result in collection of additional user data without the user's consent or awareness.

**Key Countermeasures:** Appropriate session timeouts, re-authentication for sensitive operations, session management best practices, cookie expiration controls, idle timeout enforcement.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `cookie-lifetime-audit` | Primary | Auditing cookie lifetimes directly addresses session expiration controls. |
| `cookie-audit` | Primary | Comprehensive cookie audits include session cookie management. |
| `analytics-cookie-consent` | Secondary | Analytics session management relates to session controls. |
| `eprivacy-essential-cookies` | Secondary | Essential cookie classification includes session cookies. |
| `server-side-tracking` | Secondary | Server-side session management and tracking controls. |
| `hipaa-security-rule` | Secondary | HIPAA security includes session management requirements. |
| `privacy-api-design` | Secondary | API design includes session token management. |
| `implementing-data-protection-by-default` | Secondary | Default protection includes appropriate session expiration. |

**Skill Count:** 8 skills (2 primary, 6 secondary)

---

### P9: Inability of Users to Access and Modify Data

**Risk Description:** Users do not have the ability to access, change, or delete data related to them.

**Key Countermeasures:** Data subject access request processes, self-service data portals, right to access implementation, right to rectification workflows, right to data portability, automated DSAR handling.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `dsar-intake-system` | Primary | Intake system enables users to submit access requests. |
| `dsar-processing` | Primary | Processing DSARs fulfills user access rights. |
| `employee-dsar-response` | Primary | Employee-specific data access response. |
| `right-to-rectification` | Primary | Enables users to modify their data. |
| `right-to-erasure` | Primary | Enables users to delete their data. |
| `right-to-object` | Primary | Enables users to object to processing. |
| `data-portability` | Primary | Users can access and port their data. |
| `restriction-of-processing` | Primary | Users can restrict how their data is processed. |
| `automated-decision-rights` | Primary | Rights related to automated decision-making. |
| `ai-data-subject-rights` | Primary | AI-specific data subject access and modification rights. |
| `california-consumer-rights` | Primary | California consumer access and modification rights. |
| `ccpa-consumer-requests` | Primary | CCPA consumer request handling for data access. |
| `ccpa-right-to-delete` | Primary | CCPA right to delete as user modification capability. |
| `ccpa-cpra-compliance` | Primary | CPRA compliance includes enhanced access rights. |
| `search-engine-erasure` | Primary | Right to access/modify search engine data. |
| `marketing-objection` | Primary | Right to object to marketing data processing. |
| `consent-withdrawal` | Secondary | Withdrawal as a form of modifying data processing choices. |
| `consent-pref-center` | Secondary | Preference centers enable users to view and modify choices. |
| `gdpr-self-assessment` | Secondary | Self-assessments evaluate user access capabilities. |
| `hipaa-interoperability` | Secondary | Interoperability supports patient data access. |
| `hipaa-privacy-rule` | Secondary | HIPAA Privacy Rule mandates patient access rights. |
| `children-deletion-requests` | Secondary | Children's right to access and delete data. |
| `transparent-communication` | Secondary | Transparency about how to access and modify data. |

**Skill Count:** 23 skills (16 primary, 7 secondary)

---

### P10: Collection of Data Not Required for the User-Consented Purpose

**Risk Description:** Collecting descriptive, demographic, or any other user-related data that are not needed for the purposes of the system. Also applies to data for which the user did not provide consent.

**Key Countermeasures:** Data minimization, purpose limitation enforcement, data collection audits, privacy impact assessments, purpose-specific data inventories, collection necessity reviews.

| Skill | Relevance | Mapping Rationale |
|-------|-----------|-------------------|
| `implementing-data-minimization-architecture` | Primary | Architectural data minimization prevents unnecessary collection. |
| `children-data-minimization` | Primary | Specific data minimization for children's data. |
| `building-purpose-limitation-enforcement` | Primary | Purpose limitation prevents collection beyond consent scope. |
| `hipaa-minimum-necessary` | Primary | Minimum necessary standard restricts collection. |
| `data-flow-mapping` | Primary | Flow mapping reveals unnecessary data collection points. |
| `data-inventory-mapping` | Primary | Inventory identifies data collected beyond purpose. |
| `classification-policy` | Primary | Classification identifies which data is necessary per purpose. |
| `personal-data-test` | Primary | Tests whether data qualifies as personal data requiring justification. |
| `lawful-basis-assessment` | Primary | Assesses whether collection has a valid legal basis. |
| `legitimate-interest-lia` | Primary | LIA evaluates necessity of collection for legitimate interest. |
| `pia-threshold-screening` | Primary | Screening determines if collection triggers assessment requirements. |
| `pia-vendor-processing` | Primary | Vendor processing assessments evaluate data collection scope. |
| `new-tech-pia` | Primary | New technology assessments evaluate collection proportionality. |
| `conducting-gdpr-dpia` | Primary | DPIAs assess whether collection is proportionate. |
| `dpia-automated-decisions` | Primary | Automated decision DPIAs evaluate data necessity. |
| `pia-large-scale-monitor` | Primary | Large-scale monitoring assessments evaluate collection scope. |
| `pia-health-data` | Primary | Health data assessments evaluate collection necessity. |
| `privacy-threshold-analysis` | Primary | Threshold analysis determines collection boundaries. |
| `comparing-pia-methodologies` | Secondary | Methodology comparison helps select best collection assessment. |
| `nist-pf-identify` | Secondary | NIST Identify function inventories data collection. |
| `nist-pf-govern` | Secondary | NIST Govern function sets collection governance. |
| `nist-pf-control` | Secondary | NIST Control function manages data collection. |
| `nist-privacy-identify` | Secondary | NIST privacy identification of data collection scope. |
| `designing-privacy-preserving-analytics` | Secondary | Privacy-preserving analytics limits unnecessary data collection. |
| `special-category-data` | Secondary | Special category data requires stricter collection justification. |
| `criminal-data-handling` | Secondary | Criminal data has strict collection limitations. |
| `biometric-dpia` | Secondary | Biometric data collection requires necessity justification. |
| `employee-biometric-data` | Secondary | Employee biometric collection must be proportionate. |
| `employee-health-data` | Secondary | Employee health data collection must be necessary. |
| `age-verification-methods` | Secondary | Age verification should minimize data collected. |
| `age-gating-services` | Secondary | Age gating should use proportionate data collection. |
| `background-check-privacy` | Secondary | Background checks must collect only necessary data. |
| `ai-training-lawfulness` | Secondary | AI training data collection must be lawful and necessary. |
| `ai-training-data-class` | Secondary | Training data classification evaluates collection scope. |
| `coppa-compliance` | Secondary | COPPA restricts unnecessary collection of children's data. |
| `cookieless-alternatives` | Secondary | Cookieless approaches can reduce unnecessary data collection. |

**Skill Count:** 36 skills (18 primary, 18 secondary)

---

## Skills-to-Risks Cross-Reference Table

The following table provides a reverse mapping, showing which OWASP risks each skill addresses. Skills are listed alphabetically. Only skills with at least one mapping are included.

| Skill | P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | P9 | P10 |
|-------|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| `42-cfr-part-2` | | | | | | | | | | |
| `adequacy-assessment` | | | | | | | | | | |
| `age-gating-services` | | | | | | | | | | s |
| `age-verification-methods` | | | | | | | | | | s |
| `ai-act-high-risk-docs` | | | | | | | | | | |
| `ai-automated-decisions` | | | | | | | | | | |
| `ai-bias-special-category` | | | | | | | | | | |
| `ai-data-retention` | | | | | | | s | | | |
| `ai-data-subject-rights` | | | | | | | | | **P** | |
| `ai-deployment-checklist` | **P** | | | | | | | | | |
| `ai-dpia` | | | | | | | | | | |
| `ai-federated-learning` | | | | | | | | | | |
| `ai-model-privacy-audit` | **P** | | | | | | | | | |
| `ai-privacy-assessment` | **P** | | | | | | | | | |
| `ai-privacy-impact-template` | **P** | | | | | | | | | |
| `ai-privacy-inference` | | s | | | | | | | | |
| `ai-training-data-class` | | | | | | | s | | | s |
| `ai-training-lawfulness` | | | | | | | | | | s |
| `ai-transparency-reqs` | | | | | | | | | | |
| `ai-vendor-privacy-due` | | | | | | | | | | |
| `analytics-cookie-consent` | | | | **P** | | | | s | | |
| `anonymization-alternative` | | **P** | | | | | | | | |
| `apac-transfers` | | | | | | | | | | |
| `apec-cbpr-cert` | | | | | | | | | | |
| `applying-privacy-design-patterns` | **P** | | | | | | | | | |
| `art49-derogations` | | | | | | | | | | |
| `audit-evidence-collect` | | | | | | | | | | |
| `audit-follow-up-verify` | | | s | | | | | | | |
| `audit-remediation-program` | | | s | | | | | | | |
| `audit-report-writing` | | | | | | | | | | |
| `audit-risk-assessment` | | | | | | | | | | |
| `audit-sampling-methods` | | | | | | | | | | |
| `auto-data-discovery` | | **P** | | | | s | | | | |
| `auto-deletion-workflow` | | | | | | **P** | | | | |
| `automated-decision-rights` | | | | | | | | | **P** | |
| `automated-ropa-generation` | | | | | | | | | | |
| `automating-storage-limitation-controls` | | | | | | **P** | | | | |
| `background-check-privacy` | | | | | | | | | | s |
| `backup-retention-erasure` | | s | | | | **P** | | | | |
| `bcr-establishment` | | | | | | | | | | |
| `biometric-dpia` | s | | | | | | | | | s |
| `breach-72h-notification` | | | **P** | | | | | | | |
| `breach-credit-monitor` | | | **P** | | | | | | | |
| `breach-detection-system` | | | **P** | | | | | | | |
| `breach-documentation` | | | **P** | | | | | | | |
| `breach-forensics` | | | **P** | | | | | | | |
| `breach-multi-jurisdiction` | | | **P** | | | | | | | |
| `breach-remediation` | | | **P** | | | | | | | |
| `breach-response-playbook` | | | **P** | | | | | | | |
| `breach-risk-assessment` | | | **P** | | | | | | | |
| `breach-simulation` | | | **P** | | | | | | | |
| `breach-subject-comms` | | | **P** | | | | | | | |
| `building-purpose-limitation-enforcement` | | | | s | | | | | | **P** |
| `byod-privacy-policy` | | s | | | | | | | | |
| `ca-breach-notification` | | | **P** | | | | | | | |
| `california-consumer-rights` | | | | s | | | | | **P** | |
| `canada-pipeda` | | | | | | | | | | |
| `ccpa-consumer-requests` | | | | s | | | | | **P** | |
| `ccpa-cpra-compliance` | | | | | | | | | **P** | |
| `ccpa-right-to-delete` | | | | | | **P** | | | **P** | |
| `children-data-minimization` | | | | | | | | | | **P** |
| `children-deletion-requests` | | | | | | **P** | | | s | |
| `children-privacy-notice` | | | | | **P** | | | | | |
| `children-profiling-limits` | | | | | | | | | | |
| `classification-policy` | | **P** | | | | | | | | **P** |
| `cloud-migration-dpia` | s | | | | | | | | | |
| `cloud-provider-assessment` | s | s | | | | | | | | |
| `cloud-retention-config` | | s | | | | **P** | | | | |
| `cnil-compliant-cookies` | | | | **P** | | | | | | |
| `cnil-cookie-banner` | | | | **P** | | | | | | |
| `comparing-pia-methodologies` | | | | | | | | | | s |
| `conducting-gdpr-dpia` | | | | | | | | | | **P** |
| `conducting-linddun-threat-modeling` | **P** | | | | | | | | | |
| `conflicting-laws-mgmt` | | | | | | | | | | |
| `consent-for-transfers` | | | | **P** | | | | | | |
| `consent-platform-eval` | | | | **P** | | | | | | |
| `consent-pref-center` | | | | **P** | | | | | s | |
| `consent-receipt-spec` | | | | **P** | | | | | | |
| `consent-record-keeping` | | | | **P** | | | | | | |
| `consent-withdrawal` | | | | **P** | | | | | s | |
| `continuous-compliance` | | | s | | | | | | | |
| `controller-ropa-creation` | | | | | | s | | | | |
| `cookie-audit` | | | | | s | | | **P** | | |
| `cookie-consent-ab-audit` | | | | **P** | | | | | | |
| `cookie-consent-testing` | | | | **P** | | | | | | |
| `cookie-lifetime-audit` | | | | | s | | | **P** | | |
| `cookieless-alternatives` | | | | | s | | | | | s |
| `coppa-compliance` | | | | | | | | | | s |
| `cpra-opt-out-signals` | | | | s | | | | | | |
| `cpra-sensitive-pi` | | | | | | | | | | |
| `criminal-data-handling` | | | | | | | | | | s |
| `cross-jurisdiction-cookies` | | | | | s | | | | | |
| `data-flow-mapping` | | **P** | | | | | | | | **P** |
| `data-inventory-mapping` | | **P** | | | | s | **P** | | | **P** |
| `data-labeling-system` | | **P** | | | | | **P** | | | |
| `data-lineage-tracking` | | **P** | | | | | **P** | | | |
| `data-localization` | | **P** | | | | | | | | |
| `data-portability` | | | | | | | | | **P** | |
| `designing-federated-learning-architecture` | s | | | | | | | | | |
| `designing-privacy-preserving-analytics` | | **P** | | | | | | | | s |
| `differential-privacy-prod` | s | **P** | | | | | | | | |
| `direct-collection-notice` | | | | | **P** | | | | | |
| `double-opt-in-email` | | | | **P** | | | | | | |
| `dpa-drafting` | | s | | | | | | | | |
| `dpa-inspection-prep` | | | s | | | | | | | |
| `dpia-automated-decisions` | | | | | | | | | | **P** |
| `dpia-biometric-systems` | s | | | | | | | | | |
| `dpia-mitigation-plan` | | | | | | | | | | |
| `dpia-register-mgmt` | | | | | | | | | | |
| `dpia-risk-scoring` | | | | | | | | | | |
| `dpia-stakeholder-consult` | | | | | | | | | | |
| `dsar-intake-system` | | | | | | | s | | **P** | |
| `dsar-processing` | | | | | | | s | | **P** | |
| `edtech-privacy-assessment` | s | | | | | | | | | |
| `employee-biometric-data` | | | | | | | | | | s |
| `employee-dsar-response` | | | | | | | s | | **P** | |
| `employee-health-data` | | | | | | | | | | s |
| `employee-monitoring-dpia` | | s | | | | | | | | |
| `employee-surveillance-dpia` | | s | | | | | | | | |
| `employment-consent-limits` | | | | **P** | | | | | | |
| `eprivacy-essential-cookies` | | | | | s | | | s | | |
| `eu-code-of-conduct` | | | | | s | | | | | |
| `financial-retention` | | | | | | **P** | | | | |
| `gdpr-accountability` | | | | | s | | | | | |
| `gdpr-codes-of-conduct` | | | | | s | | | | | |
| `gdpr-compliance-audit` | s | | | | | | | | | |
| `gdpr-doc-review` | | | | | **P** | | | | | |
| `gdpr-dpa-art28` | | s | | | | | | | | |
| `gdpr-dpa-cooperation` | | | s | | | | | | | |
| `gdpr-parental-consent` | | | | **P** | | | | | | |
| `gdpr-policy-framework` | | | | | **P** | | | | | |
| `gdpr-ropa-audit` | | | | | | | **P** | | | |
| `gdpr-self-assessment` | | | | | | | | | s | |
| `gdpr-valid-consent` | | | | **P** | | | | | | |
| `global-privacy-control` | | | | s | | | | | | |
| `google-consent-mode-v2` | | | | **P** | | | | | | |
| `gpc-cookie-integration` | | | | s | | | | | | |
| `health-data-dpia` | s | | | | | | | | | |
| `hipaa-breach-notification` | | | **P** | | | | | | | |
| `hipaa-breach-notify` | | | **P** | | | | | | | |
| `hipaa-deidentification` | | s | | | | | | | | |
| `hipaa-interoperability` | | | | | | | | | s | |
| `hipaa-minimum-necessary` | | s | | | | | | | | **P** |
| `hipaa-phi-inventory` | | | | | | s | s | | | |
| `hipaa-privacy-rule` | | | | | | | | | s | |
| `hipaa-risk-analysis` | s | | | | | | | | | |
| `hipaa-security-rule` | s | | | | | | | s | | |
| `implementing-data-minimization-architecture` | | **P** | | | | | | | | **P** |
| `implementing-data-protection-by-default` | **P** | | | | | | | s | | |
| `implementing-homomorphic-encryption` | s | **P** | | | | | | | | |
| `implementing-secure-multi-party-computation` | s | **P** | | | | | | | | |
| `indirect-collection-notice` | | | | | **P** | | | | | |
| `internal-privacy-audit` | s | | | | | | | | | |
| `iso-27701-pims` | | s | | | | | | | | |
| `lawful-basis-assessment` | | | | s | | | | | | **P** |
| `legit-interest-vs-consent` | | | | s | | | | | | |
| `legitimate-interest-lia` | | | | s | | | | | | **P** |
| `linddun-threat-model` | **P** | | | | | | | | | |
| `litigation-hold-mgmt` | | | | | | **P** | | | | |
| `llm-output-privacy-risk` | | s | | | | | | | | |
| `managing-consent-for-children` | | | | **P** | | | | | | |
| `managing-consent-for-research` | | | | **P** | | | | | | |
| `managing-mobile-app-consent` | | | | **P** | | | | | | |
| `marketing-objection` | | | | | | | | | **P** | |
| `multi-jurisdiction-matrix` | | | | | s | | | | | |
| `new-tech-pia` | s | | | | | | | | | **P** |
| `nist-pf-communicate` | | | | | **P** | | | | | |
| `nist-pf-control` | | | | | | | | | | s |
| `nist-pf-govern` | | | | | | | | | | s |
| `nist-pf-identify` | | | | | | | | | | s |
| `nist-pf-protect` | | s | | | | | | | | |
| `nist-privacy-identify` | | | | | | | | | | s |
| `personal-data-test` | | | | | | | s | | | **P** |
| `pia-health-data` | | | | | | | | | | **P** |
| `pia-large-scale-monitor` | | | | | | | | | | **P** |
| `pia-threshold-screening` | | | | | | | | | | **P** |
| `pia-vendor-processing` | | | | | | | | | | **P** |
| `pii-detection-pipeline` | s | **P** | | | | | | | | |
| `pii-in-unstructured` | s | **P** | | | | | | | | |
| `privacy-api-design` | **P** | | | | | | | s | | |
| `privacy-data-sharing` | | | | | s | | | | | |
| `privacy-law-monitoring` | | | | | **P** | | | | | |
| `privacy-metrics-dashboard` | | | s | | | | s | | | |
| `privacy-program-metrics` | | | s | | | | | | | |
| `privacy-record-linkage` | | **P** | | | | | | | | |
| `privacy-threshold-analysis` | | | | | **P** | | | | | **P** |
| `processor-ropa-creation` | | | | | | s | | | | |
| `pseudo-vs-anon-data` | | **P** | | | | | | | | |
| `pseudonymization-risk` | | **P** | | | | | | | | |
| `purpose-based-access` | | **P** | | | | | | | | |
| `regulatory-complaints` | | | s | | | | | | | |
| `remote-work-monitoring` | | s | | | | | | | | |
| `restriction-of-processing` | | | | | | | | | **P** | |
| `retention-exception-mgmt` | | | | | | **P** | | | | |
| `retention-impact-assess` | | | | | | **P** | | | | |
| `retention-schedule` | | | | | | **P** | | | | |
| `right-to-erasure` | | | | | | **P** | | | **P** | |
| `right-to-object` | | | | | | | | | **P** | |
| `right-to-rectification` | | | | | | | **P** | | **P** | |
| `ropa-completeness-audit` | | | | | | | **P** | | | |
| `ropa-maintenance-workflow` | | | | | | | **P** | | | |
| `saas-vendor-inventory` | | s | | | | | | | | |
| `scc-implementation` | | s | | | | | | | | |
| `search-engine-erasure` | | | | | | **P** | | | **P** | |
| `secure-data-destruction` | | **P** | | | | **P** | | | | |
| `selecting-privacy-enhancing-technologies` | s | | | | | | | | | |
| `server-side-tracking` | | s | | | | | | s | | |
| `soc2-privacy-audit` | s | | | | | | | | | |
| `special-category-data` | | | | | | | | | | s |
| `sub-processor-management` | | s | | | | | | | | |
| `supplementary-measures` | | s | | | | | | | | |
| `tcf-v2-implementation` | | | | **P** | | | | | | |
| `telehealth-privacy` | | | | | s | | | | | |
| `transfer-impact-assessment` | | s | | | | | | | | |
| `transparent-communication` | | | | | **P** | | | | s | |
| `uk-aadc-implementation` | | | | | s | | | | | |
| `universal-opt-out` | | | | s | | | | | | |
| `vendor-breach-cascade` | | s | **P** | | | | | | | |
| `vendor-monitoring-program` | | s | | | | | | | | |
| `vendor-privacy-audit` | | s | | | | | | | | |
| `vendor-privacy-due-diligence` | | s | | | | | | | | |
| `vendor-risk-scoring` | | s | | | | | | | | |
| `vendor-termination-data` | | s | | | | **P** | | | | |
| `workplace-email-privacy` | | s | | | | | | | | |

**Legend:** **P** = Primary mapping (skill directly addresses the risk), **s** = Secondary mapping (skill supports mitigation of the risk)

---

## Coverage Analysis

### Quantitative Summary

| OWASP Risk | ID | Primary Skills | Secondary Skills | Total Skills | Coverage Rating |
|------------|-----|:--------------:|:----------------:|:------------:|:---------------:|
| Web Application Vulnerabilities | P1 | 10 | 18 | 28 | Strong |
| Operator-sided Data Leakage | P2 | 20 | 28 | 48 | Excellent |
| Insufficient Data Breach Response | P3 | 15 | 8 | 23 | Strong |
| Consent on Everything | P4 | 20 | 10 | 30 | Excellent |
| Non-transparent Policies | P5 | 9 | 12 | 21 | Strong |
| Insufficient Deletion of Personal Data | P6 | 15 | 5 | 20 | Strong |
| Insufficient Data Quality | P7 | 7 | 8 | 15 | Moderate |
| Missing/Insufficient Session Expiration | P8 | 2 | 6 | 8 | Limited |
| Inability to Access and Modify Data | P9 | 16 | 7 | 23 | Strong |
| Collection of Unnecessary Data | P10 | 18 | 18 | 36 | Excellent |

### Coverage Distribution

```
P2  |================================================| 48 skills
P10 |====================================            | 36 skills
P4  |==============================                  | 30 skills
P1  |============================                    | 28 skills
P3  |=======================                         | 23 skills
P9  |=======================                         | 23 skills
P5  |=====================                           | 21 skills
P6  |====================                            | 20 skills
P7  |===============                                 | 15 skills
P8  |========                                        |  8 skills
```

### Coverage Rating Criteria

| Rating | Criteria |
|--------|----------|
| **Excellent** | 30+ skills, strong primary mapping, comprehensive coverage |
| **Strong** | 15-29 skills, solid primary mapping, good operational coverage |
| **Moderate** | 10-14 skills, adequate primary mapping, may need supplementation |
| **Limited** | Under 10 skills, few primary mappings, significant gaps |

### Gap Analysis

**Well-Covered Areas (Excellent/Strong):**
- **P2 (Data Leakage)** -- 48 skills. The strongest coverage area, reflecting the repository's deep investment in data protection, encryption, vendor management, and data flow controls.
- **P10 (Unnecessary Collection)** -- 36 skills. Extensive coverage through data minimization, purpose limitation, and comprehensive PIA/DPIA skills.
- **P4 (Consent)** -- 30 skills. Rich consent management ecosystem covering GDPR, CCPA, cookies, children, and consent platforms.
- **P1 (Web Vulnerabilities)** -- 28 skills. Good coverage via privacy-by-design, threat modeling, and AI security assessment skills.
- **P3 (Breach Response)** -- 23 skills. Comprehensive breach lifecycle coverage from detection through remediation and notification.
- **P9 (User Access/Modify)** -- 23 skills. Strong DSAR and data subject rights coverage across multiple jurisdictions.
- **P6 (Data Deletion)** -- 20 skills. Solid coverage of retention, erasure, and automated deletion workflows.
- **P5 (Transparency)** -- 21 skills. Good coverage of notices, policies, and communication frameworks.

**Areas Requiring Development:**
- **P7 (Data Quality)** -- 15 skills (Moderate). While rectification rights and ROPA audits are covered, the repository lacks dedicated data quality validation, data cleansing, and proactive quality monitoring skills.
- **P8 (Session Expiration)** -- 8 skills (Limited). This is the most significant gap. The repository's privacy skills are predominantly organizational and compliance-focused; session management is more of a technical security concern that falls at the intersection of privacy and application security. Consideration should be given to adding skills for session lifecycle management, authentication timeout policies, and privacy-aware session design.

### Unmapped Skills

The following 30 skills do not have a direct or secondary mapping to any OWASP Top 10 Privacy Risk. These skills typically address jurisdiction-specific compliance, organizational governance, or cross-border transfer mechanisms that do not map neatly to individual OWASP risks but contribute to the overall privacy posture:

- `42-cfr-part-2` -- Substance abuse records regulation (specialized compliance)
- `adequacy-assessment` -- EU adequacy decision assessment (cross-border transfers)
- `ai-act-high-risk-docs` -- EU AI Act documentation (AI governance)
- `ai-automated-decisions` -- AI automated decision governance (AI governance)
- `ai-bias-special-category` -- AI bias in special category data (fairness)
- `ai-dpia` -- AI-specific DPIA (general assessment; overlaps with other DPIA skills)
- `ai-federated-learning` -- Federated learning implementation (architecture)
- `ai-transparency-reqs` -- AI transparency requirements (AI governance)
- `ai-vendor-privacy-due` -- AI vendor due diligence (vendor management)
- `apac-transfers` -- APAC cross-border transfers (jurisdiction-specific)
- `apec-cbpr-cert` -- APEC CBPR certification (certification)
- `art49-derogations` -- Article 49 transfer derogations (cross-border transfers)
- `audit-evidence-collect` -- Audit evidence collection (audit methodology)
- `audit-report-writing` -- Audit report writing (audit methodology)
- `audit-risk-assessment` -- Audit risk assessment (audit methodology)
- `audit-sampling-methods` -- Audit sampling methods (audit methodology)
- `automated-ropa-generation` -- Automated ROPA generation (automation tooling)
- `bcr-establishment` -- Binding Corporate Rules (cross-border transfers)
- `canada-pipeda` -- Canadian PIPEDA compliance (jurisdiction-specific)
- `children-profiling-limits` -- Children's profiling restrictions (children's privacy)
- `conflicting-laws-mgmt` -- Conflicting laws management (multi-jurisdiction)
- `cpra-sensitive-pi` -- CPRA sensitive personal information (jurisdiction-specific)
- `dpia-mitigation-plan` -- DPIA mitigation planning (assessment process)
- `dpia-register-mgmt` -- DPIA register management (assessment process)
- `dpia-risk-scoring` -- DPIA risk scoring (assessment process)
- `dpia-stakeholder-consult` -- DPIA stakeholder consultation (assessment process)
- `pia-review-cadence` -- PIA review cadence (assessment process)
- `privacy-law-gap-analysis` -- Privacy law gap analysis (multi-jurisdiction)
- `privacy-maturity-model` -- Privacy maturity model (organizational governance)
- And additional jurisdiction-specific skills (brazil-lgpd, china-pipl, india-dpdp-act, japan-appi, korea-pipa, etc.)

These unmapped skills are not gaps -- they serve important functions in comprehensive privacy programs but operate at a level of specificity (jurisdiction, organizational process) that sits outside the OWASP Top 10 Privacy Risks categorization.

---

## Integration Guidance

### How to Use This Mapping

**1. Risk-Based Skill Prioritization**

When building or evaluating a privacy program, use this mapping to ensure that skills addressing the highest-ranked OWASP risks are prioritized:

- Start with **P1-P3** skills as the foundation (vulnerabilities, leakage, breach response)
- Build out **P4-P6** for consent, transparency, and deletion maturity
- Address **P7-P10** for data quality, session management, access rights, and minimization

**2. Audit and Assessment Integration**

When conducting privacy audits referencing the OWASP framework:

- Use the **Detailed Mapping by Risk** section to identify which skills should be assessed for each risk
- Skills marked as **Primary** should be mandatory audit targets
- Skills marked as **Secondary** provide supporting evidence of risk mitigation
- Use the **Coverage Analysis** to identify areas requiring compensating controls

**3. Training Program Design**

Map training curricula to OWASP risks:

- **Technical teams**: Focus on P1 (vulnerabilities), P2 (leakage), P8 (sessions)
- **Legal/compliance teams**: Focus on P3 (breach response), P4 (consent), P5 (transparency)
- **Data management teams**: Focus on P6 (deletion), P7 (data quality), P10 (data minimization)
- **Product teams**: Focus on P9 (user access/modify), P4 (consent), P5 (transparency)

**4. Gap Remediation Roadmap**

For areas identified as Limited or Moderate coverage:

| Gap Area | Recommended New Skills | Priority |
|----------|----------------------|----------|
| P8 (Session Expiration) | `session-lifecycle-management`, `authentication-timeout-policy`, `privacy-aware-session-design`, `session-cookie-security` | High |
| P7 (Data Quality) | `data-quality-monitoring`, `proactive-data-cleansing`, `data-accuracy-validation`, `automated-data-quality-checks` | Medium |

**5. Continuous Monitoring**

- Review this mapping quarterly as new skills are added to the repository
- Update risk coverage ratings when skills are added, modified, or deprecated
- Track OWASP Top 10 Privacy Risks project updates for potential v3.0 changes

### Mapping to Other Frameworks

This OWASP mapping complements other framework mappings:

| OWASP Privacy Risk | Related GDPR Articles | Related NIST PF Functions |
|--------------------|-----------------------|---------------------------|
| P1 | Art. 25, 32 | Protect, Control |
| P2 | Art. 5(1)(f), 28, 32 | Protect, Control |
| P3 | Art. 33, 34 | Respond, Communicate |
| P4 | Art. 6, 7 | Govern, Control |
| P5 | Art. 12, 13, 14 | Communicate, Govern |
| P6 | Art. 5(1)(e), 17 | Control, Protect |
| P7 | Art. 5(1)(d), 16 | Identify, Control |
| P8 | Art. 5(1)(f), 25 | Protect, Control |
| P9 | Art. 12-22 | Communicate, Control |
| P10 | Art. 5(1)(b)(c), 6, 9 | Identify, Govern, Control |

---

## References

1. **OWASP Top 10 Privacy Risks Project** -- [https://owasp.org/www-project-top-10-privacy-risks/](https://owasp.org/www-project-top-10-privacy-risks/)
2. **OWASP Top 10 Privacy Risks v2.0 (2021)** -- [https://github.com/OWASP/www-project-top-10-privacy-risks/blob/master/tab_topprivacy.md](https://github.com/OWASP/www-project-top-10-privacy-risks/blob/master/tab_topprivacy.md)
3. **OWASP Top 10 Privacy Risks Countermeasures v2.0** -- [https://owasp.org/www-project-top-10-privacy-risks/OWASP_Top_10_Privacy_Risks_Countermeasures_v2.0.pdf](https://owasp.org/www-project-top-10-privacy-risks/OWASP_Top_10_Privacy_Risks_Countermeasures_v2.0.pdf)
4. **OWASP Top 10 Privacy Risks v2.0 Presentation** -- [https://owasp.org/www-chapter-germany/stammtische/hamburg/assets/slides/2021-08-05_OWASP%20Top%2010%20Privacy%20Risks%20v2.0.pdf](https://owasp.org/www-chapter-germany/stammtische/hamburg/assets/slides/2021-08-05_OWASP%20Top%2010%20Privacy%20Risks%20v2.0.pdf)
5. **OWASP Top 10 Privacy Risks -- Tarlogic Analysis** -- [https://www.tarlogic.com/blog/owasp-top-10-privacy-risks/](https://www.tarlogic.com/blog/owasp-top-10-privacy-risks/)
6. **OWASP Top 10 Privacy Risks -- TSH Analysis** -- [https://tsh.io/blog/owasp-top-10-privacy-risks](https://tsh.io/blog/owasp-top-10-privacy-risks)
7. **IAPP: OWASP Top 10 Privacy Risks at IPEN Workshop** -- [https://iapp.org/news/a/owasp-top-10-privacy-risks-presented-at-inaugural-ipen-workshop-in-berlin](https://iapp.org/news/a/owasp-top-10-privacy-risks-presented-at-inaugural-ipen-workshop-in-berlin)

---

*Document generated: 2026-03-15 | Framework version: OWASP Top 10 Privacy Risks v2.0 (2021) | Repository skills count: 282*
