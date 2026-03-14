---
name: hipaa-security-rule
description: >-
  Implements HIPAA Security Rule technical safeguards under 45 CFR §164.312
  for electronic protected health information. Covers access controls with
  unique user identification, emergency access procedures, automatic logoff,
  encryption, audit controls, integrity controls, and transmission security.
  Keywords: HIPAA Security Rule, ePHI, access controls, encryption, audit
  controls, technical safeguards.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, security-rule, ephi, access-controls, encryption, audit-controls, technical-safeguards"
---

# HIPAA Security Rule — Technical Safeguards 45 CFR §164.312

## Overview

The HIPAA Security Rule establishes national standards for protecting electronic protected health information (ePHI) that is created, received, used, or maintained by a covered entity or business associate. Published as a final rule on February 20, 2003 (68 FR 8334), with compliance required by April 20, 2005 (April 20, 2006 for small health plans), the Security Rule operationalizes the Privacy Rule's confidentiality protections through administrative, physical, and technical safeguards. The rule adopts a risk-based, technology-neutral approach — it specifies what must be achieved but allows flexibility in how covered entities implement protections based on their size, complexity, and capabilities.

The Security Rule applies only to ePHI, unlike the Privacy Rule which covers PHI in all forms. The rule organizes its requirements into three safeguard categories (administrative §164.308, physical §164.310, technical §164.312) plus organizational requirements (§164.314) and policies/procedures/documentation (§164.316).

## Technical Safeguards — §164.312

Technical safeguards are the technology and related policies and procedures that protect ePHI and control access to it. Each standard has required implementation specifications (mandatory) and addressable implementation specifications (must be implemented if reasonable and appropriate, with documented rationale if an alternative measure is adopted or the specification is not implemented).

### Access Control — §164.312(a)(1)

**Standard**: Implement technical policies and procedures for electronic information systems that maintain ePHI to allow access only to those persons or software programs that have been granted access rights.

| Implementation Specification | Type | Requirement |
|------------------------------|------|-------------|
| Unique User Identification — §164.312(a)(2)(i) | Required | Assign a unique name and/or number for identifying and tracking user identity |
| Emergency Access Procedure — §164.312(a)(2)(ii) | Required | Establish and implement procedures for obtaining necessary ePHI during an emergency |
| Automatic Logoff — §164.312(a)(2)(iii) | Addressable | Implement electronic procedures that terminate an electronic session after a predetermined time of inactivity |
| Encryption and Decryption — §164.312(a)(2)(iv) | Addressable | Implement a mechanism to encrypt and decrypt ePHI |

#### Unique User Identification

Every workforce member, administrator, and system account accessing ePHI must have a unique identifier. Shared accounts and generic logins are prohibited.

**Asclepius Health Network Implementation**:
- Active Directory assigns unique user IDs in the format `[first initial][last name][employee number]` (e.g., `jsmith4821`)
- Service accounts for application-to-application communication use the format `svc-[application]-[function]` (e.g., `svc-epic-hl7`)
- Privileged administrative accounts are separate from standard user accounts (`adm-jsmith4821`)
- All user accounts are tied to the HR system — terminated employees are automatically disabled within 1 hour of separation processing
- Biometric authentication (fingerprint) is deployed at clinical workstations for single sign-on
- Multi-factor authentication is required for remote access and administrative functions

#### Emergency Access Procedure

Covered entities must have documented procedures for accessing ePHI during emergencies when normal access controls cannot function.

**Asclepius Health Network Implementation**:
- Break-the-glass procedures allow any clinician to access any patient record during declared emergencies
- Break-the-glass events generate immediate alerts to the Privacy Office and require post-event justification within 24 hours
- Disaster recovery accounts with elevated privileges are maintained in sealed envelopes in the IT Operations Center safe
- Emergency access accounts are tested quarterly and passwords rotated after each test or use
- The EHR system maintains a separate emergency mode with simplified authentication (badge + PIN) activated during IT system failures

#### Automatic Logoff

**Asclepius Health Network Implementation**:
- Clinical workstations: 5-minute inactivity timeout with screen lock, 15-minute session termination
- Administrative workstations: 10-minute inactivity timeout with screen lock, 30-minute session termination
- Patient portal sessions: 15-minute inactivity timeout with session termination
- Mobile devices (tablets on clinical carts): 2-minute inactivity lock, requiring biometric re-authentication
- Proximity-based logoff using RFID badges — session locks when clinician's badge moves more than 10 feet from the workstation

#### Encryption and Decryption

Although addressable, OCR has consistently found that failing to encrypt ePHI without documented equivalent alternative measures constitutes a Security Rule violation.

**Asclepius Health Network Implementation**:
- Data at rest: AES-256 encryption on all storage volumes containing ePHI (database tablespace encryption, full disk encryption on endpoints)
- Data in transit: TLS 1.2 minimum (TLS 1.3 preferred) for all network communications containing ePHI
- Database field-level encryption for highly sensitive fields (SSN, substance abuse diagnoses, HIV status, mental health notes)
- Encryption key management through a FIPS 140-2 Level 3 validated hardware security module (HSM)
- Key rotation: Annual for data-at-rest keys, per-session for TLS, quarterly for application-level encryption keys

### Audit Controls — §164.312(b)

**Standard**: Implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use ePHI.

No implementation specifications are designated — the standard itself is required.

**Asclepius Health Network Implementation**:

**What is logged**:
- All authentication events (successful and failed logins, logoffs, account lockouts)
- All access to ePHI (reads, writes, modifications, deletions) including the specific records accessed
- All administrative actions (user creation, privilege changes, configuration modifications)
- All system events (startup, shutdown, errors, backup operations)
- All network events involving ePHI systems (connections, disconnections, firewall events)
- Break-the-glass access events with enhanced detail

**Log management**:
- Centralized log aggregation using SIEM (Security Information and Event Management) platform
- Real-time correlation and alerting for suspicious patterns (multiple failed logins, unusual access volumes, after-hours access to records outside care team)
- Immutable log storage — logs are write-once to prevent tampering
- Log retention: minimum 6 years (aligned with HIPAA documentation retention requirement under §164.530(j))
- Daily automated log review reports provided to the Security Operations Center
- Monthly audit sample: random selection of 50 patient records reviewed for access appropriateness

**Audit triggers and alerts**:

| Trigger | Response SLA | Action |
|---------|-------------|--------|
| 5+ failed login attempts in 10 minutes | Immediate | Account lockout, alert to SOC |
| Access to VIP/employee patient records | Immediate | Alert to Privacy Office for review |
| Bulk record access (>50 records in 1 hour by single user) | 15 minutes | SOC review, possible account suspension |
| After-hours access from unusual location | 1 hour | Review by SOC next business day or immediate if high risk |
| Break-the-glass event | 24 hours | Privacy Office justification review |
| Administrative privilege escalation | Immediate | SOC verification of change ticket |

### Integrity — §164.312(c)(1)

**Standard**: Implement policies and procedures to protect ePHI from improper alteration or destruction.

| Implementation Specification | Type | Requirement |
|------------------------------|------|-------------|
| Mechanism to Authenticate ePHI — §164.312(c)(2) | Addressable | Implement electronic mechanisms to corroborate that ePHI has not been altered or destroyed in an unauthorized manner |

**Asclepius Health Network Implementation**:
- Database integrity: SHA-256 checksums on clinical document records; tamper-evident logging of all modifications
- Append-only clinical documentation model — original entries are never deleted or overwritten; amendments are linked to original records with author, timestamp, and reason
- Digital signatures on laboratory results, radiology reports, and medication orders using PKI certificates
- Daily integrity verification scans comparing file checksums against known-good baselines
- Backup integrity verification: automated restore testing of randomly selected backup sets weekly

### Person or Entity Authentication — §164.312(d)

**Standard**: Implement procedures to verify that a person or entity seeking access to ePHI is the one claimed. This standard is required with no implementation specifications.

**Asclepius Health Network Implementation**:
- Internal workforce: Multi-factor authentication (badge + PIN for workstations; authenticator app + password for remote)
- External providers (Health Information Exchange): Digital certificate-based mutual TLS authentication
- Patient portal: Knowledge-based authentication for enrollment; username + password + SMS/email verification code for ongoing access
- Business associates accessing Asclepius systems: VPN with certificate + password + hardware token
- Application-to-application: OAuth 2.0 with client credentials and mutual TLS

### Transmission Security — §164.312(e)(1)

**Standard**: Implement technical security measures to guard against unauthorized access to ePHI that is being transmitted over an electronic communications network.

| Implementation Specification | Type | Requirement |
|------------------------------|------|-------------|
| Integrity Controls — §164.312(e)(2)(i) | Addressable | Implement security measures to ensure electronically transmitted ePHI is not improperly modified without detection |
| Encryption — §164.312(e)(2)(ii) | Addressable | Implement a mechanism to encrypt ePHI whenever deemed appropriate |

**Asclepius Health Network Implementation**:
- All internal network traffic containing ePHI is encrypted using TLS 1.2+ (network segmentation with ePHI VLAN)
- External transmissions: mandatory TLS 1.2+ or VPN tunnels; unencrypted email containing ePHI is blocked by DLP gateway
- HL7 FHIR API endpoints: mutual TLS with SMART on FHIR authorization
- Direct secure messaging for provider-to-provider ePHI exchange (Direct Protocol with S/MIME encryption)
- Integrity controls: TLS provides built-in integrity via HMAC; additional checksums on batch file transfers (HL7 batch, X12 EDI)
- Wireless networks: WPA3 Enterprise with 802.1X RADIUS authentication on all clinical wireless networks; separate guest network with no ePHI system access

## Administrative Safeguards — §164.308 (Selected Key Requirements)

### Security Management Process — §164.308(a)(1)

| Implementation Specification | Type |
|------------------------------|------|
| Risk Analysis | Required |
| Risk Management | Required |
| Sanction Policy | Required |
| Information System Activity Review | Required |

### Workforce Security — §164.308(a)(3)

| Implementation Specification | Type |
|------------------------------|------|
| Authorization and/or Supervision | Addressable |
| Workforce Clearance Procedure | Addressable |
| Termination Procedures | Addressable |

### Information Access Management — §164.308(a)(4)

| Implementation Specification | Type |
|------------------------------|------|
| Isolating Healthcare Clearinghouse Functions | Required |
| Access Authorization | Addressable |
| Access Establishment and Modification | Addressable |

### Security Awareness and Training — §164.308(a)(5)

| Implementation Specification | Type |
|------------------------------|------|
| Security Reminders | Addressable |
| Protection from Malicious Software | Addressable |
| Log-in Monitoring | Addressable |
| Password Management | Addressable |

### Security Incident Procedures — §164.308(a)(6)

| Implementation Specification | Type |
|------------------------------|------|
| Response and Reporting | Required |

### Contingency Plan — §164.308(a)(7)

| Implementation Specification | Type |
|------------------------------|------|
| Data Backup Plan | Required |
| Disaster Recovery Plan | Required |
| Emergency Mode Operation Plan | Required |
| Testing and Revision Procedures | Addressable |
| Applications and Data Criticality Analysis | Addressable |

## Physical Safeguards — §164.310 (Summary)

### Facility Access Controls — §164.310(a)(1)

Addressable specifications: Contingency operations, facility security plan, access control and validation procedures, maintenance records.

### Workstation Use — §164.310(b)

Required standard specifying appropriate physical environment and manner of use for workstations accessing ePHI.

### Workstation Security — §164.310(c)

Required standard implementing physical safeguards restricting access to workstations that access ePHI.

### Device and Media Controls — §164.310(d)(1)

Required specifications for disposal and media re-use; addressable specifications for accountability and data backup/storage.

## Required vs Addressable: OCR Expectations

OCR has clarified that "addressable" does not mean "optional." For each addressable specification, covered entities must:

1. Assess whether the implementation specification is a reasonable and appropriate safeguard in their environment
2. If yes, implement it
3. If not, document why it is not reasonable and appropriate AND implement an equivalent alternative measure that is reasonable and appropriate OR document why the standard can still be met without the specification or alternative

OCR enforcement actions have found violations where entities failed to encrypt ePHI (addressable) without documenting any alternative measure. In practice, encryption of ePHI at rest and in transit is expected by OCR absent extraordinary documented justification.

## Enforcement Precedents

- **Anthem Inc. (2018)**: $16 million — failure to implement technical safeguards including access controls sufficient to prevent unauthorized access to ePHI of 78.8 million individuals
- **Premera Blue Cross (2020)**: $6.85 million — failure to implement security measures sufficient to reduce risks and vulnerabilities to ePHI; inadequate audit controls
- **CHSPSC LLC (2020)**: $2.3 million — failure to implement information system activity review, inadequate response to known security incident (APT attack affecting 6.1 million individuals)
- **Excellus Health Plan (2021)**: $5.1 million — inadequate access controls, failure to conduct enterprise-wide risk analysis, insufficient technical policies
- **Banner Health (2023)**: $1.25 million — failure to implement audit controls and conduct accurate technical risk analysis after breach of 2.81 million records

## Integration Points

- **hipaa-privacy-rule**: Privacy Rule establishes what must be protected; Security Rule establishes how
- **hipaa-risk-analysis**: Detailed risk analysis methodology mandated by §164.308(a)(1)(ii)(A)
- **hipaa-breach-notify**: Security incidents that result in unauthorized access trigger breach notification
- **hipaa-baa-management**: Business associates must independently comply with all Security Rule standards
