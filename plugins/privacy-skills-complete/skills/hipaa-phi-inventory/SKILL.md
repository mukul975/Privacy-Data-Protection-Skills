---
name: hipaa-phi-inventory
description: >-
  Conducts comprehensive inventory of protected health information across
  the enterprise per HIPAA Security Rule requirements at 45 CFR
  §164.308(a)(1)(ii)(A) and §164.310(d). Covers identification of all
  ePHI repositories, data flow mapping, classification of PHI by
  sensitivity, and integration with risk analysis. Keywords: PHI
  inventory, ePHI, data mapping, information asset, data flow, HIPAA
  risk analysis, designated record set.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, phi-inventory, ephi, data-mapping, information-assets, data-flow, risk-analysis"
---

# HIPAA PHI Inventory — ePHI Asset Identification and Data Flow Mapping

## Overview

The HIPAA Security Rule at 45 CFR §164.308(a)(1)(ii)(A) requires covered entities and business associates to conduct an accurate and thorough assessment of potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI held by the entity. This risk analysis is impossible without first knowing where ePHI resides, how it flows, and who has access. The PHI inventory is the foundational step of HIPAA compliance, supporting risk analysis (§164.308(a)(1)), access management (§164.312(a)), device and media controls (§164.310(d)), and business associate management (§164.502(e)).

## Regulatory Framework

### Security Rule — Risk Analysis Foundation

- **§164.308(a)(1)(ii)(A)**: Conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of ePHI held by the covered entity or business associate
- **§164.310(d)(1)**: Implement policies and procedures that govern the receipt and removal of hardware and electronic media that contain ePHI into and out of a facility, and the movement of these items within the facility
- **§164.312(a)(1)**: Implement technical policies and procedures for electronic information systems that maintain ePHI to allow access only to persons or software programs that have been granted access rights

### OCR Risk Analysis Guidance

OCR guidance identifies the first step of risk analysis as: "Identify where ePHI is created, received, maintained, or transmitted." This requires a comprehensive inventory covering:

1. All electronic media and systems that create, receive, maintain, or transmit ePHI
2. All locations where ePHI is stored (on-premises, cloud, mobile, removable media)
3. All network paths over which ePHI is transmitted
4. All workforce members and roles with access to ePHI
5. All business associates that create, receive, maintain, or transmit ePHI

### PHI Identifiers — 45 CFR §160.103

PHI includes individually identifiable health information transmitted or maintained in any form that relates to past, present, or future physical or mental health condition, provision of healthcare, or payment for healthcare. The 18 HIPAA identifiers are:

| # | Identifier | Examples |
|---|-----------|----------|
| 1 | Names | Full name, maiden name |
| 2 | Geographic data smaller than state | Street address, city, ZIP code |
| 3 | Dates related to individual | Birth date, admission date, discharge date, date of death |
| 4 | Phone numbers | Home, mobile, work |
| 5 | Fax numbers | All fax numbers |
| 6 | Email addresses | Personal and work email |
| 7 | Social Security numbers | SSN |
| 8 | Medical record numbers | MRN, chart number |
| 9 | Health plan beneficiary numbers | Insurance ID, member ID |
| 10 | Account numbers | Patient account, billing account |
| 11 | Certificate/license numbers | Professional license, birth certificate |
| 12 | Vehicle identifiers and serial numbers | VIN, license plate |
| 13 | Device identifiers and serial numbers | Implant serial, medical device ID |
| 14 | Web URLs | Patient portal URLs, personal websites |
| 15 | IP addresses | Device IP addresses |
| 16 | Biometric identifiers | Fingerprints, retinal scans, voiceprints |
| 17 | Full-face photographs | Photos, images |
| 18 | Any other unique identifying number | Any code or characteristic that could identify an individual |

## PHI Inventory Categories

### System Inventory

| System Category | Examples | Typical PHI Content |
|----------------|----------|-------------------|
| Electronic Health Record (EHR) | Epic, Cerner, MEDITECH | Complete clinical records, demographics, diagnoses, medications, lab results |
| Practice Management System | Athenahealth, eClinicalWorks | Scheduling, demographics, insurance, billing |
| Laboratory Information System (LIS) | Sunquest, Orchard | Lab orders, results, specimen data |
| Radiology (PACS/RIS) | Change Healthcare, Sectra | Imaging studies, radiology reports, patient demographics |
| Pharmacy System | Pyxis, Omnicell | Medication orders, dispensing records, patient allergies |
| Billing/Revenue Cycle | Waystar, R1 RCM | Claims, EOBs, patient financial data, demographics |
| Patient Portal | MyChart, Cerner Health | Patient-accessible clinical data, messages, appointments |
| Telehealth Platform | Zoom for Healthcare, Amwell | Session recordings, clinical notes, patient identity |
| Email System | Microsoft 365, Google Workspace | ePHI in attachments and message body |
| File Shares | Network drives, SharePoint | Unstructured clinical documents, reports |
| Mobile Devices | Smartphones, tablets | EHR access, clinical photos, messaging |
| Medical Devices | Infusion pumps, monitors | Patient vitals, device-patient association |
| Backup Systems | Commvault, Veeam | Complete copies of all source system ePHI |

### Data Flow Categories

| Flow Type | Source | Destination | Method | Encryption |
|-----------|--------|-------------|--------|-----------|
| Clinical documentation | Provider workstation | EHR database | HTTPS | TLS 1.2+ |
| Lab orders/results | EHR | LIS | HL7v2 / FHIR | TLS 1.2+ |
| Claims submission | Billing system | Clearinghouse/payer | EDI 837 | TLS 1.2+ |
| Patient portal access | Patient device | Portal server | HTTPS | TLS 1.2+ |
| HIE exchange | EHR | HIE/HIN | FHIR / Direct | TLS 1.2+ |
| BA data sharing | CE system | BA system | SFTP/API | TLS 1.2+ |
| Backup | Production systems | Backup storage | Backup agent | AES-256 |
| Mobile access | Mobile device | EHR (Citrix/VPN) | VPN + HTTPS | TLS 1.2+ |

## Integration Points

- **hipaa-risk-analysis**: PHI inventory is the required first step of risk analysis per §164.308(a)(1)
- **hipaa-security-rule**: Inventory supports access control, audit, and device/media controls
- **hipaa-minimum-necessary**: Inventory informs role-based access to specific PHI categories
- **hipaa-baa-management**: Inventory identifies all BAs that create, receive, maintain, or transmit PHI
- **hipaa-breach-notification**: Inventory determines scope of breach impact assessment
