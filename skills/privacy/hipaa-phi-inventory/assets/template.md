# PHI Inventory Assessment Report — Asclepius Health Network

**Assessment Date**: 2026-01-10
**Prepared by**: Kevin Torres, IT Security Manager
**Reviewed by**: Dr. James Park, CISO
**Scope**: Enterprise-wide ePHI asset identification and data flow mapping

---

## Organization Profile

| Attribute | Value |
|-----------|-------|
| Organization | Asclepius Health Network |
| Entity Type | Covered Entity — Healthcare Provider |
| Facilities | 3 hospitals, 12 outpatient clinics, 1 data center |
| Workforce | 4,200 |
| Business Associates with PHI Access | 47 |

## ePHI Asset Inventory

### Clinical Systems

| System | Owner | PHI Types | Records (approx.) | Location | Encrypted (Rest/Transit) | BAA |
|--------|-------|-----------|-------------------:|----------|:---:|:---:|
| Epic EHR | Clinical Informatics | Demographics, clinical, lab, pharmacy, imaging | 2,400,000 | On-premises (data center) | Yes/Yes | N/A (owned) |
| Sunquest LIS | Lab Director | Lab orders, results, patient demographics | 1,800,000 | On-premises | Yes/Yes | Yes |
| Sectra PACS | Radiology Director | Imaging studies, radiology reports, demographics | 950,000 | On-premises + cloud archive | Yes/Yes | Yes |
| Omnicell Pharmacy | Pharmacy Director | Medication orders, dispensing, allergies | 2,400,000 | On-premises | Yes/Yes | Yes |
| Amwell Telehealth | CMO | Session metadata, clinical notes, demographics | 85,000 | Cloud (AWS) | Yes/Yes | Yes |
| Biobeat RPM | Cardiology Director | Vitals, device readings, patient ID | 12,000 | Cloud (Azure) | Yes/Yes | Yes |

### Administrative Systems

| System | Owner | PHI Types | Records (approx.) | Location | Encrypted (Rest/Transit) | BAA |
|--------|-------|-----------|-------------------:|----------|:---:|:---:|
| Waystar Revenue Cycle | CFO | Claims, billing, demographics, insurance | 2,400,000 | Cloud (Waystar hosted) | Yes/Yes | Yes |
| Microsoft 365 (Email) | CIO | ePHI in emails and attachments | Variable | Cloud (Microsoft) | Yes/Yes | Yes |
| SharePoint (File Shares) | CIO | Clinical documents, reports, policies | Variable | Cloud (Microsoft) | Yes/Yes | Yes |
| ADP Workforce (HR) | HR Director | Employee health records, workers' comp | 4,200 | Cloud (ADP hosted) | Yes/Yes | Yes |

### Infrastructure and Backup

| System | Owner | PHI Types | Location | Encrypted | BAA |
|--------|-------|-----------|----------|:---:|:---:|
| Commvault Backup | IT Director | Complete copies of all clinical and admin systems | On-premises (tape + disk) | Yes (AES-256) | N/A |
| Azure Disaster Recovery | IT Director | Replicated EHR, LIS, billing data | Cloud (Azure East US) | Yes | Yes |

### Mobile Devices

| Category | Count | MDM Enrolled | Encrypted |
|----------|------:|:---:|:---:|
| Organization smartphones | 320 | Yes | Yes |
| Organization tablets | 85 | Yes | Yes |
| BYOD smartphones | 410 | Yes | Yes (98.6%) |
| BYOD tablets | 45 | Yes | Yes (95.6%) |

## Data Flow Map Summary

| Flow | Source | Destination | Method | Encryption | Volume |
|------|--------|-------------|--------|-----------|--------|
| Clinical documentation | Provider workstations | Epic EHR | HTTPS/HL7 FHIR | TLS 1.3 | Continuous |
| Lab orders/results | Epic EHR | Sunquest LIS | HL7v2 over TLS | TLS 1.2 | ~2,000/day |
| Imaging orders/results | Epic EHR | Sectra PACS | DICOM over TLS | TLS 1.2 | ~500/day |
| Claims submission | Waystar | Clearinghouse (Change Healthcare) | EDI 837/835 | TLS 1.2 | ~1,500/day |
| Patient portal access | Patient devices | Epic MyChart | HTTPS | TLS 1.3 | ~3,000/day |
| HIE exchange | Epic EHR | Statewide HIE (CommonWell) | FHIR R4 | TLS 1.2 | ~800/day |
| Remote patient monitoring | Biobeat devices | Biobeat cloud | MQTT over TLS | TLS 1.2 | Continuous |
| Backup | All production systems | Commvault | Backup agent | AES-256 | Nightly |
| DR replication | On-premises | Azure DR site | VPN | AES-256 + TLS | Continuous |
| Email (clinical) | Workforce | Microsoft 365 | SMTP over TLS | TLS 1.2 | ~5,000/day |

## Findings

### Finding 1: Unencrypted BYOD Devices (Critical)

- **Regulation**: 45 CFR §164.312(a)(2)(iv)
- **Details**: 14 BYOD devices (1.4% of fleet) detected with encryption disabled. See mobile health assessment for details.
- **Remediation**: Reduce MDM compliance check interval; implement immediate access block.
- **Status**: Remediated January 25, 2026

### Finding 2: Shadow IT Discovery (High)

- **Regulation**: 45 CFR §164.308(a)(1)(ii)(A)
- **Details**: Network scan identified 3 department-level cloud services (Google Drive, Dropbox, Box) being used by 8 workforce members to store clinical documents. These services are not in the PHI inventory, have no BAAs, and are not approved for ePHI.
- **Remediation**: Block unauthorized cloud services at network/proxy level. Migrate data to approved SharePoint. Retrain workforce members. Execute BAAs if services are to be approved, or terminate use.
- **Deadline**: 2026-02-15

### Finding 3: Stale Risk Assessment for LIS (Medium)

- **Regulation**: 45 CFR §164.308(a)(1)(ii)(A)
- **Details**: Last risk assessment for Sunquest LIS was conducted on 2024-08-15 (528 days ago). The system underwent a major version upgrade in 2025 that was not followed by an updated risk assessment.
- **Remediation**: Conduct updated risk assessment for LIS covering the new version.
- **Deadline**: 2026-02-28

## Summary Statistics

| Metric | Value |
|--------|-------|
| Total ePHI assets inventoried | 16 systems + 860 mobile devices |
| Data flows documented | 10 primary flows |
| Business associates with PHI access | 47 |
| Assets with encryption at rest | 100% (systems); 98.6% (mobile) |
| Assets with encryption in transit | 100% |
| BAAs current | 45 of 47 (95.7%) |
| Risk assessments current (< 12 months) | 14 of 16 (87.5%) |

**Prepared by**: Kevin Torres, IT Security Manager
**Approved by**: Compliance Committee, January 2026
