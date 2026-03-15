---
name: hipaa-risk-analysis
description: >-
  Conducts HIPAA risk analysis per 45 CFR §164.308(a)(1) following OCR
  guidance methodology. Covers threat identification, vulnerability
  assessment, likelihood and impact determination, risk scoring, and
  mitigation planning for electronic protected health information.
  Keywords: HIPAA risk analysis, OCR guidance, threat assessment,
  vulnerability, risk management, ePHI.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, risk-analysis, ocr-guidance, threat-assessment, vulnerability, risk-management, ephi"
---

# HIPAA Risk Analysis — 45 CFR §164.308(a)(1)

## Overview

The HIPAA Security Rule requires covered entities and business associates to conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI held by the organization. Risk analysis under §164.308(a)(1)(ii)(A) is the foundational requirement of the Security Rule — it drives all subsequent safeguard decisions. OCR has identified failure to conduct a comprehensive, enterprise-wide risk analysis as the most common finding in breach investigations and compliance reviews. The risk analysis must be ongoing, not a one-time event, and must be updated whenever significant changes occur in the environment or in response to security incidents.

## Legal Foundation

### Regulatory Text

45 CFR §164.308(a)(1)(ii)(A) — Risk Analysis (Required):
> "Conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of electronic protected health information held by the covered entity or business associate."

45 CFR §164.308(a)(1)(ii)(B) — Risk Management (Required):
> "Implement security measures sufficient to reduce risks and vulnerabilities to a reasonable and appropriate level to comply with §164.306(a)."

### OCR Guidance Documents

OCR published "Guidance on Risk Analysis Requirements under the HIPAA Security Rule" (July 14, 2010) establishing nine essential elements that an adequate risk analysis must address. This guidance, while not binding regulation, represents OCR's enforcement expectations and has been consistently applied in settlement agreements and corrective action plans.

## OCR Nine Essential Elements

### Element 1: Scope of the Analysis

The risk analysis must encompass all ePHI that the organization creates, receives, maintains, or transmits, in every form and location:

**Asclepius Health Network Scope Inventory**:

| ePHI Location | System/Medium | Data Categories | Volume |
|---------------|---------------|-----------------|--------|
| Electronic Health Record (Epic) | Production servers, disaster recovery site | Complete clinical records, demographics, insurance | 4.2 million patient records |
| Practice Management System | Cloud-hosted (Azure US East) | Scheduling, billing, referrals | 4.2 million patients |
| Laboratory Information System | On-premises servers | Lab orders, results, specimen tracking | 12 million results annually |
| Radiology PACS | On-premises SAN storage | Diagnostic images, reports | 850 TB imaging data |
| Email System (Exchange Online) | Microsoft 365 tenant | Incidental ePHI in clinical communications | Estimated 15,000 messages/day containing ePHI |
| Mobile Devices | 3,200 organization-owned tablets, 800 BYOD smartphones | Clinical reference, secure messaging, patient photos | Variable |
| Medical Devices | 1,400 networked devices (infusion pumps, monitors, ventilators) | Real-time patient data, device logs | Continuous streaming |
| Paper-to-digital Conversion | Scanning workstations, OCR servers | Scanned historical records, faxed referrals | 2,000 pages/day |
| Business Associate Systems | 47 BA relationships with ePHI access | Varies by BA (billing, transcription, cloud hosting, analytics) | Varies |
| Backup and Archive | Tape library, offsite vault, cloud archive | Complete system backups | 6-year retention |
| Health Information Exchange | Regional HIE platform | ADT feeds, CCD documents, lab results | 150,000 transactions/month |

### Element 2: Data Collection

Identify and document where ePHI is stored, received, maintained, or transmitted. Methods include:

- **Automated discovery**: Network scanning tools identifying systems communicating health data (HL7, FHIR, DICOM traffic analysis)
- **Data flow mapping**: Documenting how ePHI moves between systems, departments, and external parties
- **Workforce interviews**: Structured interviews with department managers, clinical informaticists, and IT staff
- **System inventory review**: Cross-referencing CMDB (Configuration Management Database) with ePHI classification tags
- **Vendor assessment questionnaire responses**: BA-reported ePHI handling practices
- **Physical walkthroughs**: Identifying workstations, printers, fax machines, and storage locations processing ePHI

### Element 3: Identify and Document Potential Threats and Vulnerabilities

#### Threat Categories

| Threat Category | Specific Threats | Source |
|----------------|-----------------|--------|
| **Natural** | Flood, earthquake, tornado, hurricane, wildfire, pandemic | Geographic and climate risk assessment |
| **Human — Intentional** | Hacking/IT incident, ransomware, phishing, insider theft, social engineering, nation-state APT | FBI IC3 reports, HHS cybersecurity alerts, threat intelligence feeds |
| **Human — Unintentional** | Misdirected email/fax, lost device, improper disposal, misconfiguration, training failure | Incident history, OCR breach portal patterns |
| **Environmental** | Power failure, HVAC failure, water damage, fire, electromagnetic interference | Facility assessments, utility reliability data |
| **Technical** | Software vulnerability, hardware failure, network outage, cryptographic weakness | CVE databases, vendor advisories, penetration test results |

#### Vulnerability Assessment Methods

- **Penetration testing**: Annual external and internal penetration test by independent third party
- **Vulnerability scanning**: Weekly automated scans of all network-connected assets (Qualys, Nessus, or equivalent)
- **Configuration auditing**: Quarterly review of system configurations against CIS benchmarks
- **Social engineering testing**: Semi-annual phishing simulations; annual physical penetration attempts
- **Application security testing**: SAST/DAST scanning of internally developed applications; third-party code review for critical systems
- **Wireless security assessment**: Quarterly rogue access point scanning; annual wireless penetration test

### Element 4: Assess Current Security Measures

Document existing safeguards and their effectiveness:

**Asclepius Health Network Current Controls Assessment (Sample)**:

| Control Area | Implemented Measure | Effectiveness Rating | Gap Identified |
|-------------|-------------------|---------------------|---------------|
| Access Control | Role-based access in EHR with unique user IDs | Effective | Quarterly access reviews not consistently completed for all departments |
| Encryption at Rest | AES-256 FDE on servers and endpoints | Effective | 12 legacy medical devices running unencrypted embedded systems |
| Encryption in Transit | TLS 1.2+ enforced on all external connections | Effective | 3 internal legacy interfaces still using TLS 1.0 |
| Audit Logging | Centralized SIEM with 6-year retention | Effective | Log review staffing insufficient for alert volume |
| Backup | Daily incremental, weekly full, offsite replication | Effective | Restore testing frequency needs improvement |
| Physical Security | Badge access, CCTV, visitor management | Partially Effective | Server room access badge list includes 15 individuals who no longer require access |
| Anti-Malware | EDR deployed on all managed endpoints | Effective | Coverage gap on BYOD devices with MDM enrollment below 100% |
| Patch Management | Monthly patch cycle, 14-day critical patch SLA | Partially Effective | Medical device patching delayed by manufacturer certification requirements |

### Element 5: Determine the Likelihood of Threat Occurrence

Assign likelihood ratings based on threat capability, motivation, and existing controls:

| Likelihood Level | Definition | Scoring |
|-----------------|-----------|---------|
| Very High | Almost certain to occur within the next year; active exploitation observed | 5 |
| High | Likely to occur; threat source is capable and motivated; controls have known weaknesses | 4 |
| Medium | Possible occurrence; threat source exists and has some capability; controls are partially effective | 3 |
| Low | Unlikely but possible; limited threat capability or motivation; controls are generally effective | 2 |
| Very Low | Remote possibility; no known threat source targeting this vulnerability; strong controls in place | 1 |

### Element 6: Determine the Potential Impact of Threat Occurrence

Assess the magnitude of harm if a threat exploits a vulnerability:

| Impact Level | Definition | Examples | Scoring |
|-------------|-----------|----------|---------|
| Critical | Catastrophic harm to individuals or organization | Breach of >500K records, permanent patient harm from data integrity failure, organizational insolvency | 5 |
| High | Significant harm to many individuals or severe organizational impact | Breach of 10K-500K records, extended system outage affecting patient care, OCR investigation | 4 |
| Medium | Moderate harm to limited individuals or substantial operational disruption | Breach of 500-10K records, multi-day system unavailability, significant remediation costs | 3 |
| Low | Limited harm to few individuals or manageable operational impact | Breach of <500 records, brief system disruption, contained incident | 2 |
| Negligible | Minimal or no harm | No ePHI exposure confirmed, minor operational inconvenience | 1 |

### Element 7: Determine the Level of Risk

Risk is calculated as the product of likelihood and impact:

```
Risk Score = Likelihood × Impact
```

| Risk Score | Risk Level | Action Required |
|-----------|-----------|----------------|
| 20-25 | Critical | Immediate mitigation required; senior leadership notification; consider system suspension |
| 12-19 | High | Mitigation plan required within 30 days; management approval to accept risk |
| 6-11 | Medium | Mitigation plan required within 90 days; documented risk acceptance alternative |
| 2-5 | Low | Monitor and address in normal operations; annual review |
| 1 | Minimal | Accept and document; review at next scheduled risk analysis |

**Asclepius Health Network Risk Register (Sample Entries)**:

| Risk ID | Threat/Vulnerability | Likelihood | Impact | Risk Score | Risk Level |
|---------|---------------------|-----------|--------|-----------|-----------|
| R-001 | Ransomware attack on clinical systems | 4 (High) | 5 (Critical) | 20 | Critical |
| R-002 | Insider unauthorized access to celebrity patient records | 4 (High) | 3 (Medium) | 12 | High |
| R-003 | Unencrypted legacy medical device data exposure | 3 (Medium) | 4 (High) | 12 | High |
| R-004 | Phishing leading to credential compromise | 4 (High) | 4 (High) | 16 | High |
| R-005 | Lost/stolen unencrypted mobile device | 2 (Low) | 3 (Medium) | 6 | Medium |
| R-006 | Misdirected fax containing ePHI | 3 (Medium) | 2 (Low) | 6 | Medium |
| R-007 | Natural disaster affecting primary data center | 2 (Low) | 5 (Critical) | 10 | Medium |

### Element 8: Finalize Documentation

The risk analysis must be documented in sufficient detail to demonstrate:

1. The scope covered all ePHI
2. Threats and vulnerabilities were comprehensively identified
3. Current security measures were evaluated
4. Likelihood and impact were assessed using a consistent methodology
5. Risk levels were determined
6. The analysis was conducted by qualified personnel

**Required Documentation Components**:
- Date of analysis and date range covered
- Personnel conducting the analysis (names, qualifications)
- Methodology description
- Complete asset inventory with ePHI classification
- Threat and vulnerability catalog
- Current controls inventory
- Risk scoring matrix and ratings
- Risk register with all identified risks
- Executive summary for leadership

### Element 9: Periodic Review and Updates

The risk analysis is not a one-time activity. It must be updated:

- At least annually as a scheduled comprehensive review
- When new systems, applications, or technologies are implemented
- When significant changes to the operating environment occur (mergers, relocations, new facilities)
- After a security incident or breach
- When new threats are identified (new malware families, regulatory changes, threat intelligence alerts)
- When OCR or industry guidance identifies new risk areas

## Risk Management and Mitigation Planning — §164.308(a)(1)(ii)(B)

For each risk above the organization's acceptable risk threshold, develop and implement a mitigation plan:

**Mitigation Plan Template (Risk R-001: Ransomware)**:

| Element | Detail |
|---------|--------|
| **Risk ID** | R-001 |
| **Risk Description** | Ransomware attack encrypting clinical systems, rendering ePHI unavailable |
| **Current Risk Score** | 20 (Critical) |
| **Mitigation Measures** | (1) Deploy advanced EDR with behavioral ransomware detection; (2) Implement network segmentation isolating clinical systems; (3) Maintain immutable backup copies with air-gapped storage; (4) Conduct quarterly tabletop ransomware exercises; (5) Implement application whitelisting on clinical workstations |
| **Implementation Timeline** | EDR: Complete; Segmentation: 60 days; Immutable backups: 90 days; Tabletop: Quarterly; Whitelisting: 120 days |
| **Responsible Party** | CISO (overall); Network Engineering (segmentation); Backup Administrator (immutable backups) |
| **Target Risk Score** | 8 (Medium) — likelihood reduced from 4 to 2 through layered controls |
| **Residual Risk Acceptance** | Approved by CIO and CPO on documented risk acceptance form |
| **Review Date** | Next comprehensive review or 90 days post-implementation |

## Common OCR Findings

OCR consistently identifies the following deficiencies in risk analyses:

1. **Not enterprise-wide**: Analysis limited to EHR system only, excluding email, mobile devices, medical devices, and BA systems
2. **Not updated**: One-time analysis without periodic review or updates after significant changes
3. **Not thorough**: Failure to identify all ePHI assets, particularly shadow IT, personal devices, and cloud services
4. **No documentation**: Analysis conducted informally without written documentation
5. **No risk management follow-through**: Risks identified but no mitigation plans developed or implemented
6. **Inadequate methodology**: No structured approach to likelihood/impact determination; subjective risk ratings without defined criteria

## Enforcement Actions for Risk Analysis Failures

Risk analysis deficiency is cited in the majority of OCR enforcement actions:

- **Anthem Inc. (2018)**: $16 million — failed to conduct enterprise-wide risk analysis prior to breach affecting 78.8 million
- **Premera Blue Cross (2020)**: $6.85 million — risk analysis failed to identify risks across the enterprise; did not assess all systems with ePHI
- **Banner Health (2023)**: $1.25 million — risk analysis was not accurate and thorough; did not identify all risks to ePHI
- **CHSPSC LLC (2020)**: $2.3 million — failed to conduct accurate risk analysis and implement risk management measures
- **University of Massachusetts Amherst (2020)**: $650,000 — failure to conduct risk analysis of ePHI maintained by research programs
- **Metro Community Provider Network (2017)**: $400,000 — risk analysis not conducted to sufficient depth

## Integration Points

- **hipaa-security-rule**: Risk analysis drives implementation decisions for all technical, administrative, and physical safeguards
- **hipaa-breach-notify**: Post-breach risk analysis updates feed into breach risk assessment under §164.402
- **hipaa-baa-management**: Risk analysis must include ePHI held by or accessible to business associates
- **hipaa-privacy-rule**: Privacy risk assessments complement security risk analysis for comprehensive PHI protection
