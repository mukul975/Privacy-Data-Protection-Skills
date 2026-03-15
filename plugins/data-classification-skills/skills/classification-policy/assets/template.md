# Data Classification Policy

## Organisation: Vanguard Financial Services Ltd
## Policy Reference: DCP-2026-v1.0
## Effective Date: 2026-03-14
## Policy Owner: Dr. James Whitfield, Data Protection Officer
## Approved By: Vanguard Privacy Steering Committee

---

## 1. Purpose

This policy establishes the framework for classifying all data created, received, processed, or stored by Vanguard Financial Services according to its sensitivity level. Classification enables the organisation to apply proportionate security controls, meet regulatory obligations under GDPR and financial services regulations, and manage risk effectively.

## 2. Scope

This policy applies to all data in any format (digital, paper, verbal) processed by Vanguard employees, contractors, and third-party processors. It covers data across all systems, platforms, and locations including cloud services, on-premises systems, mobile devices, and physical documents.

## 3. Classification Tiers

| Tier | Label Colour | Description | Examples |
|------|-------------|-------------|---------|
| **Public** | Green | Approved for unrestricted distribution | Published reports, press releases, public website content |
| **Internal** | Blue | For internal use by Vanguard personnel | Internal policies, procedures, organisation charts, meeting notes |
| **Confidential** | Amber | Disclosure would cause significant harm | Customer personal data, financial records, employee records, contracts |
| **Restricted** | Red | Disclosure would cause severe or irreversible harm | Art. 9 health/biometric data, Art. 10 criminal data, AML investigation files, encryption keys |

## 4. Classification Procedures

### 4.1 Who Classifies

- **Data Owner**: Responsible for initial classification of data within their business function
- **All Employees**: Must classify data they create; must not downgrade classification without Data Owner approval
- **Automated Tools**: Microsoft Purview auto-labelling applies Confidential/Restricted labels based on detected content

### 4.2 When to Classify

- At the point of creation or receipt
- When data content or purpose changes
- When automated discovery identifies unclassified data
- During scheduled periodic reviews

## 5. Handling Requirements Summary

| Control | Public | Internal | Confidential | Restricted |
|---------|--------|----------|-------------|-----------|
| Storage | Any | Vanguard systems | Encrypted, Vanguard systems | Designated restricted systems, CMK encryption |
| Access | Open | All employees | RBAC + MFA | Named individuals + dual authorisation + PAM |
| Encryption (rest) | Optional | Recommended | AES-256 | AES-256 + CMK |
| Encryption (transit) | Optional | TLS 1.2+ | TLS 1.3 | TLS 1.3 + E2E |
| External sharing | Open | Data Owner approval | DPO approval + DPA/NDA | DPO + CPO approval + encrypted |
| DLP | None | Warn on external | Warn + block personal email | Block all external + USB + print |
| Audit logging | None | Annual review | Quarterly review | Monthly DPO review |
| Disposal | Standard delete | Secure delete | NIST Clear | NIST Purge + certificate |

## 6. Labelling Requirements

### 6.1 Digital Documents

- Classification label in document header and footer
- Metadata tag applied via Microsoft Purview or manual labelling in Office applications
- Email subject line prefix: [CONFIDENTIAL] or [RESTRICTED] for those tiers

### 6.2 Physical Documents

- Classification label printed on cover page and each subsequent page header
- Restricted documents: red "RESTRICTED" watermark on each page

### 6.3 Systems and Databases

- System-level classification recorded in CMDB and data inventory
- Field-level classification for databases containing mixed-tier data

## 7. Exception Process

Exceptions to handling requirements must be documented and approved:
- **Confidential tier**: Data Owner approval; recorded in exception register
- **Restricted tier**: DPO and CISO joint approval; time-limited (max 12 months)
- All exceptions reviewed at expiry; chronic exceptions trigger process improvement

## 8. Enforcement

- DLP policies technically enforce handling requirements for digital data
- Semi-annual classification audits by DPO (100 items per tier sampled)
- Violations reported to line manager and DPO
- Repeated or deliberate violations subject to disciplinary action per employee handbook

## 9. Training

- All employees: annual classification awareness training (mandatory, tracked in LMS)
- Data Owners and Stewards: advanced classification training upon appointment and annually
- New employees: classification training within first week of onboarding

## 10. Review

This policy is reviewed annually by the Privacy Steering Committee. Interim reviews are triggered by regulatory changes, significant incidents, or audit findings.

| Version | Date | Change |
|---------|------|--------|
| 1.0 | 2026-03-14 | Initial policy release |

---

*Policy maintained by the Data Protection Office. Queries: dpo@vanguardfs.co.uk.*
