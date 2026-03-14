---
name: nist-pf-protect
description: >-
  Implement the NIST Privacy Framework PROTECT function covering PR.AC access
  control, PR.DS data security, and PR.PO protective policies. Provides
  technical control implementation guidance, encryption standards, access
  management architectures, and security-privacy integration patterns.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "nist-privacy-framework, protect-function, access-control, data-security, protective-policies"
---

# NIST Privacy Framework — PROTECT Function

## Overview

The PROTECT function develops and implements appropriate data processing safeguards to prevent cybersecurity-related privacy events. This function directly bridges the NIST Cybersecurity Framework and Privacy Framework, addressing the overlap where security controls serve privacy objectives. It covers access control, data security, and protective policies.

## PROTECT Function Subcategories

### PR.AC — Access Control

Managing access to data and systems to protect privacy.

| Subcategory | Description | Implementation Guidance |
|-------------|-------------|------------------------|
| PR.AC-P1 | Identities and credentials are issued, managed, verified, revoked, and audited for authorized individuals, processes, and devices | Implement identity lifecycle management. Enforce MFA for systems processing personal data. Conduct quarterly access reviews. |
| PR.AC-P2 | Physical access to data and devices is managed | Restrict physical access to data centers and server rooms. Implement visitor logging. Secure endpoint devices with encryption and remote wipe capability. |
| PR.AC-P3 | Remote access is managed | Enforce VPN for remote access to personal data systems. Implement zero-trust network architecture. Monitor and log all remote sessions. |
| PR.AC-P4 | Access permissions and authorizations are managed with least privilege and separation of duties | Implement role-based access control (RBAC). Enforce separation of duties for sensitive operations. Regular privileged access reviews. |
| PR.AC-P5 | Network integrity is protected | Network segmentation for systems processing personal data. Intrusion detection/prevention systems. Encrypted network communications. |
| PR.AC-P6 | Individuals and devices are proofed and bound to credentials | Implement strong identity verification for data subject account creation. Device certificate management. Biometric authentication where appropriate. |

### PR.DS — Data Security

Protecting data at rest, in transit, and during processing.

| Subcategory | Description | Implementation Guidance |
|-------------|-------------|------------------------|
| PR.DS-P1 | Data-at-rest are protected | AES-256 encryption for stored personal data. Key management with HSM. Database-level encryption (TDE). |
| PR.DS-P2 | Data-in-transit are protected | TLS 1.3 for all data transmissions. Certificate pinning for mobile applications. End-to-end encryption for sensitive communications. |
| PR.DS-P3 | Systems/products/services and associated data are formally managed throughout removal, transfers, and disposition | Secure media sanitization (NIST SP 800-88). Certificate of destruction for physical media. Verified data deletion from cloud services. |
| PR.DS-P4 | Adequate capacity to ensure availability is maintained | Capacity planning for privacy-critical systems. DDoS protection. Redundancy for data subject rights portals. |
| PR.DS-P5 | Protections against data leaks are implemented | DLP solutions monitoring egress points. Email DLP for personal data. Cloud access security broker (CASB) deployment. |
| PR.DS-P6 | Integrity checking mechanisms are used to verify software, firmware, and information integrity | File integrity monitoring for privacy-critical systems. Code signing for privacy-related applications. Checksum verification for data transfers. |
| PR.DS-P7 | The development and testing environment(s) are separate from the production environment | Separate environments with no production personal data in dev/test. Synthetic data generation for testing. Access controls between environments. |
| PR.DS-P8 | Data disclosures are consistent with the purposes for which the data were collected | Technical enforcement of purpose limitation. API-level access controls tied to documented purposes. Automated purpose verification at query time. |

### PR.PO — Protective Policies

Policies governing protective measures for privacy.

| Subcategory | Description | Implementation Guidance |
|-------------|-------------|------------------------|
| PR.PO-P1 | A baseline configuration of information technology/industrial control systems is created and maintained | Establish secure baselines for all systems processing personal data. Configuration management database. Automated compliance scanning. |
| PR.PO-P2 | Configuration change control processes are in place | Change advisory board review for privacy-impacting changes. Impact assessment for configuration changes. Rollback procedures documented. |
| PR.PO-P3 | Backups of information are conducted, maintained, and tested | Encrypted backups of personal data. Regular restoration testing. Backup retention aligned with data retention policies. |
| PR.PO-P4 | Policy and regulations regarding the physical operating environment are met | Environmental controls for data processing facilities. Compliance with data residency requirements. Physical security audits. |
| PR.PO-P5 | Data destruction processes are defined and managed | Documented destruction procedures per data classification. Verification and certification of destruction. Compliant disposal of hardware containing personal data. |
| PR.PO-P6 | Maintenance and repair of organizational assets are performed and logged | Vendor supervision during maintenance. Data sanitization before equipment service. Maintenance activity logging. |
| PR.PO-P7 | Response plans (Incident Response and Business Continuity) and recovery plans (Incident Recovery and Disaster Recovery) are in place and managed | Privacy-integrated incident response plan. Business continuity for privacy-critical services. Regular tabletop exercises. |
| PR.PO-P8 | Response and recovery plans are tested | Annual incident response exercises including privacy scenarios. DR testing with privacy recovery objectives. Post-exercise improvement plans. |
| PR.PO-P9 | Privacy procedures are included in human resources practices | Background checks for privacy-sensitive roles. Confidentiality agreements. Exit procedures including access revocation. |
| PR.PO-P10 | A vulnerability management plan is developed and implemented | Vulnerability scanning for privacy-critical systems. Patch management prioritizing privacy-impacting vulnerabilities. Penetration testing including privacy controls. |

## Technical Control Architecture

### Access Control Architecture

```
Identity Provider (IdP)
    |
    v
Multi-Factor Authentication
    |
    v
Authorization Engine (RBAC + ABAC)
    |
    +-- Role-Based Access Control
    |   ├── Privacy Administrator
    |   ├── Data Steward
    |   ├── Data Processor
    |   ├── Data Analyst (aggregated only)
    |   └── Data Subject (own data only)
    |
    +-- Attribute-Based Access Control
    |   ├── Purpose attribute (why accessing)
    |   ├── Data classification (sensitivity level)
    |   ├── Time-based restrictions
    |   └── Location-based restrictions
    |
    v
Audit Logging Engine
```

### Encryption Standards

| Data State | Minimum Standard | Recommended Standard | Key Management |
|-----------|-----------------|---------------------|----------------|
| At Rest | AES-128 | AES-256 | HSM-managed keys, annual rotation |
| In Transit | TLS 1.2 | TLS 1.3 | Certificate management with auto-renewal |
| In Processing | Application-level encryption | Envelope encryption | Per-session keys |
| Backup | AES-256 | AES-256 + separate key | Offline key escrow |
| Archive | AES-256 | AES-256 + integrity check | Long-term key management |

### Data Loss Prevention Configuration

| Channel | DLP Control | Detection Method | Action |
|---------|------------|-----------------|--------|
| Email | Email gateway DLP | Pattern matching (SSN, CC, IBAN) | Block + notify |
| Web upload | Web proxy DLP | Content inspection | Block + notify |
| Cloud storage | CASB | Classification labels | Encrypt + restrict sharing |
| Endpoint | Endpoint DLP | File content scanning | Prevent copy to removable media |
| Database | Database activity monitoring | Query analysis | Alert on bulk extraction |
| API | API gateway | Payload inspection | Rate limit + log |

## Network Security for Privacy

### Segmentation Architecture

```
Internet
    |
    v
[DMZ / WAF]
    |
    v
[Application Tier] ── TLS 1.3 ── [API Gateway]
    |                                    |
    v                                    v
[Business Logic Tier]            [Privacy Services Tier]
    |                            ├── Consent Manager
    v                            ├── DSR Processor
[Data Tier]                      ├── Anonymization Engine
├── PII Database (encrypted)     └── Audit Logger
├── Analytics Database (aggregated)
└── Backup Storage (encrypted, isolated)
```

## Control Mapping

| NIST PF PROTECT | NIST CSF | ISO 27701 | GDPR Article |
|-----------------|----------|-----------|--------------|
| PR.AC-P1 | PR.AC-1 | A.7.2.2 | Art. 32(1)(b) |
| PR.AC-P4 | PR.AC-4 | A.7.2.2 | Art. 25(2) |
| PR.DS-P1 | PR.DS-1 | A.7.4.9 | Art. 32(1)(a) |
| PR.DS-P2 | PR.DS-2 | A.7.4.9 | Art. 32(1)(a) |
| PR.DS-P5 | PR.DS-5 | A.7.4.9 | Art. 32(1)(b) |
| PR.DS-P7 | PR.DS-7 | A.7.4.9 | Art. 32(1)(a) |
| PR.DS-P8 | N/A | A.7.2.2 | Art. 5(1)(b) |
| PR.PO-P3 | PR.IP-4 | A.7.4.9 | Art. 32(1)(c) |
| PR.PO-P5 | PR.IP-6 | A.7.4.7 | Art. 17(1) |
| PR.PO-P7 | PR.IP-9 | A.7.2.8 | Art. 33, 34 |
| PR.PO-P10 | PR.IP-12 | A.7.4.9 | Art. 32(1)(d) |

## References

- NIST Privacy Framework Version 1.0 (January 16, 2020)
- NIST Cybersecurity Framework Version 1.1 (April 16, 2018)
- NIST SP 800-53 Rev. 5 — Security and Privacy Controls for Information Systems
- NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization
- NIST SP 800-175B — Guideline for Using Cryptographic Standards
