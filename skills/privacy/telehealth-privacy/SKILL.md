---
name: telehealth-privacy
description: >-
  Implements telehealth privacy compliance covering HIPAA requirements for
  virtual care, state licensing and recording consent laws, platform security
  with BAA requirements for telehealth vendors, cross-state prescribing
  rules, and OCR enforcement discretion during public health emergencies.
  Keywords: telehealth privacy, virtual care, HIPAA, recording consent,
  platform BAA, cross-state licensing, OCR enforcement.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "telehealth, virtual-care, hipaa, recording-consent, platform-baa, cross-state-licensing, ocr-enforcement"
---

# Telehealth Privacy Compliance

## Overview

Telehealth (also termed telemedicine, virtual care, or remote patient monitoring) involves the delivery of healthcare services through electronic communications technologies when the patient and provider are in different locations. The rapid expansion of telehealth — accelerated during the COVID-19 public health emergency — created a complex regulatory environment where HIPAA, state privacy laws, telecommunications regulations, and professional licensing requirements converge. Privacy compliance for telehealth requires addressing the security of the communication platform, the privacy of the encounter, state-specific consent and recording requirements, cross-state practice considerations, and the obligations of technology vendors as business associates.

## HIPAA Compliance for Telehealth

### Core HIPAA Requirements

Telehealth encounters involve the creation, transmission, and storage of ePHI and are fully subject to HIPAA:

| HIPAA Requirement | Telehealth Application |
|-------------------|----------------------|
| Privacy Rule (§164.500-534) | Telehealth encounters create PHI (notes, prescriptions, diagnoses); all Privacy Rule provisions apply including individual rights, minimum necessary, and authorization requirements |
| Security Rule (§164.312) | Telehealth platform must meet technical safeguards: access controls, audit logs, encryption in transit and at rest, integrity controls |
| Breach Notification Rule (§164.400-414) | Unauthorized access to telehealth session data (recording, transcript, chat) triggers breach notification analysis |
| BAA Requirement (§164.502(e)) | Telehealth technology vendor that creates, receives, maintains, or transmits ePHI must have a BAA with the covered entity |

### Platform Security Requirements

Asclepius Health Network evaluates telehealth platforms against these Security Rule requirements:

**Access Controls (§164.312(a))**:
- Unique user identification for all providers and patients
- Multi-factor authentication for provider access
- Patient authentication through verified identity (DOB verification, registered email/phone, patient portal credentials)
- Session-level access controls — each encounter creates a separate, access-controlled session
- Automatic session termination after provider disconnect or 5-minute inactivity

**Audit Controls (§164.312(b))**:
- Logging of all session events: initiation, connection, disconnection, duration, participants
- Recording access logs (who accessed any stored recordings)
- Chat/messaging logs maintained as part of the medical record
- Logs retained for minimum 6 years

**Transmission Security (§164.312(e))**:
- End-to-end encryption for video, audio, and data channels (minimum AES-128; Asclepius requires AES-256)
- TLS 1.2 or higher for signaling and data transport
- No unencrypted fallback — session fails rather than downgrades
- SRTP (Secure Real-time Transport Protocol) for media streams

**Integrity Controls (§164.312(c))**:
- Tamper-evident session metadata
- Digital signatures on stored encounter records
- Integrity verification on transmitted prescriptions and orders

### Platforms Requiring BAA

| Platform Type | BAA Required | Rationale |
|--------------|-------------|-----------|
| Dedicated telehealth platform (Teladoc, Amwell, Doxy.me) | Yes | Creates, receives, maintains, or transmits ePHI |
| Video conferencing adapted for telehealth (Zoom for Healthcare, Microsoft Teams with BAA) | Yes | ePHI transmitted and potentially stored (recordings, chat) |
| Consumer video platforms without BAA (standard Zoom, FaceTime, Skype, Google Hangouts) | No BAA available — generally not compliant | No BAA offered; ePHI not adequately protected |
| EHR-integrated telehealth (Epic MyChart Video Visit) | Covered by existing EHR BAA | ePHI managed within existing BAA relationship |
| Remote patient monitoring devices | Yes (for cloud-connected devices) | Device data transmitted to vendor cloud containing ePHI |
| Asynchronous telehealth (store-and-forward) | Yes | Images, data transmitted and stored by vendor |
| Patient messaging/portal | Covered by existing EHR/portal BAA | Secure messaging within covered platform |

### OCR Enforcement Discretion During Public Health Emergency

On March 17, 2020, OCR issued a Notification of Enforcement Discretion for Telehealth Remote Communications (85 FR 22024), stating that during the COVID-19 public health emergency, OCR would exercise enforcement discretion and would not impose penalties for noncompliance with HIPAA related to the good-faith provision of telehealth using non-public-facing remote communication technologies:

**What was permitted during enforcement discretion**:
- Use of non-public-facing video platforms (Apple FaceTime, Facebook Messenger video, Google Hangouts video, Zoom, Skype) without a BAA
- Covered entities were expected to use encryption and privacy settings available on these platforms
- OCR encouraged providers to notify patients of potential privacy risks

**What was NOT permitted even during enforcement discretion**:
- Use of public-facing platforms (Facebook Live, Twitch, TikTok) where communications are open to the public
- Abandonment of all privacy protections (providers still had to use reasonable precautions)

**Post-PHE Status**: The COVID-19 PHE ended on May 11, 2023. OCR enforcement discretion for telehealth formally expired on August 9, 2023. All telehealth must now be conducted on HIPAA-compliant platforms with BAAs in place.

**Asclepius Health Network**: Asclepius transitioned all telehealth to BAA-covered platforms (Epic MyChart Video Visit as primary; Zoom for Healthcare as backup) prior to the enforcement discretion expiration. All consumer-grade platform use for clinical telehealth was discontinued.

## State Licensing Requirements

### Cross-State Telehealth Practice

Healthcare providers are generally licensed by individual states. Providing telehealth services to a patient in a state where the provider is not licensed may violate that state's medical practice act.

**Key Licensing Models**:

| Model | Description | Participating States |
|-------|------------|---------------------|
| Interstate Medical Licensure Compact (IMLC) | Expedited licensure pathway for physicians seeking multi-state licenses | 42 states, DC, and Guam as of 2024 |
| Nurse Licensure Compact (NLC) | Multistate license allowing RNs and LPN/VNs to practice across member states | 41 states as of 2024 |
| Psychology Interjurisdictional Compact (PSYPACT) | Allows psychologists to practice telepsychology across member states | 42 states as of 2024 |
| Individual state telehealth licenses | Some states offer special telehealth-only or limited-scope licenses | Varies by state (e.g., Florida, Texas telehealth registrations) |
| Full state licensure | Traditional full license in each state where patients are located | All states |

**Privacy Implication**: The state where the patient is physically located at the time of the telehealth encounter generally controls which state's privacy laws apply. This means the provider must comply with that state's specific privacy, consent, and recording requirements even if the provider is located in a different state.

**Asclepius Health Network**: Asclepius providers are licensed in the 4 states where Asclepius operates. For telehealth, the EHR prompts the provider to confirm the patient's physical location at the start of each encounter. The system applies location-specific consent requirements and recording notices based on the patient's state.

## Recording Consent Requirements

### HIPAA and Recording

HIPAA does not specifically address recording of telehealth encounters, but recordings containing ePHI are subject to all HIPAA protections. Recordings become part of or associated with the medical record and must be:
- Stored securely with encryption
- Subject to access controls
- Retained per the entity's record retention policy
- Made available to patients under the right of access (§164.524) if part of the designated record set

### State Recording Consent Laws

State wiretapping and eavesdropping laws impose consent requirements on the recording of communications:

| Consent Model | Requirement | States |
|--------------|-------------|--------|
| One-party consent | Only one participant needs to consent to recording (the provider can record without patient consent, but best practice is to inform) | 38 states + DC including New York, Texas, Ohio, Georgia, Virginia |
| Two-party (all-party) consent | All participants must consent to recording | 12 states: California, Connecticut, Delaware, Florida, Illinois, Maryland, Massachusetts, Michigan, Montana, New Hampshire, Pennsylvania, Washington |

**Two-party consent states require particular attention**: A provider in a one-party state conducting telehealth with a patient in a two-party state must obtain the patient's consent before recording. The more restrictive state law controls.

**Asclepius Health Network Recording Policy**:
- All telehealth encounters may be recorded for quality assurance and medical record purposes
- Prior to recording, the platform displays a notice and requires patient acknowledgment: "This telehealth visit may be recorded for quality assurance and medical record purposes. Your provider will also be taking notes during the visit. Do you consent to the recording of this visit?"
- For patients in two-party consent states, recording does not proceed without affirmative consent
- For patients who decline recording, the encounter proceeds without recording; the provider documents clinical notes manually
- Recordings are encrypted and stored in the EHR document management system; access is restricted to the care team and authorized quality reviewers

## Cross-State Prescribing

### Federal Requirements

- **DEA**: Practitioners must be registered with the DEA to prescribe controlled substances. For telehealth prescribing of controlled substances, the Ryan Haight Act (21 USC §829(e)) generally requires at least one in-person medical evaluation before prescribing controlled substances via telehealth, with exceptions:
  - During DEA-declared telemedicine exceptions
  - When the patient is at a DEA-registered location (hospital, clinic)
  - Under specific state exemptions authorized by DEA
  - 2024 DEA proposed rule would establish a pathway for initial telehealth prescribing of Schedule III-V controlled substances with conditions

### State Prescribing Rules

| State Requirement | Privacy Implication |
|------------------|-------------------|
| Prescriber must be licensed in patient's state | Provider credential verification creates PHI (license lookup, verification) |
| State prescription drug monitoring program (PDMP) check required | Provider must access the patient's state PDMP — cross-state PDMP data sharing involves PHI |
| State formulary restrictions | May require disclosure of diagnosis to justify off-formulary prescriptions |
| E-prescribing mandates (most states for controlled substances) | Electronic prescription transmission must be HIPAA-compliant; DEA EPCS standards apply |

**Asclepius Health Network**: The telehealth platform integrates with the state PDMP for the patient's location. Providers must complete PDMP checks before prescribing controlled substances. The integration uses a HIPAA-compliant API with the state PDMP system. For cross-state encounters, the system automatically routes prescriptions to the correct state PDMP.

## Remote Patient Monitoring (RPM) Privacy

### RPM-Specific Considerations

Remote patient monitoring involves continuous or periodic collection of health data from devices in the patient's home or on their person:

| RPM Component | Privacy Consideration | HIPAA Requirement |
|---------------|----------------------|-------------------|
| Monitoring devices (blood pressure cuffs, glucometers, pulse oximeters) | Device data is ePHI; device may store data locally | Encryption on device storage; secure transmission |
| Wearable devices (smartwatches, continuous glucose monitors) | Continuous data collection; potential for excessive data collection beyond medical necessity | Minimum necessary — collect only clinically relevant data; patient consent for monitoring scope |
| Cloud platform for data aggregation | Vendor receives and stores ePHI | BAA required with RPM platform vendor |
| Alerts and notifications | Transmitted health data may reach patient's personal device | Patient education on securing personal devices; notification content should minimize PHI |
| Data integration with EHR | RPM data flows into clinical record | Secure integration (FHIR API with OAuth 2.0); data quality validation |

### Patient Consent for RPM

While HIPAA does not require consent for treatment, RPM programs should obtain informed consent addressing:
- What data will be collected and how frequently
- Who will access the data (care team, monitoring center, BA)
- How data will be used (clinical decision-making, AI analytics, quality improvement)
- Patient's ability to pause or stop monitoring
- Security measures protecting transmitted data
- Limitations of RPM (not a substitute for emergency services)

## Asclepius Health Network Telehealth Privacy Program

### Governance

| Component | Implementation |
|-----------|---------------|
| Telehealth Privacy Policy | Comprehensive policy covering platform selection, consent, recording, cross-state compliance, RPM; reviewed annually |
| Platform Approval Process | All telehealth platforms must be approved by IT Security and Privacy Office; BAA executed; security assessment completed |
| Provider Training | Annual telehealth-specific privacy training covering: location verification, consent procedures, recording requirements, secure environment setup |
| Patient Education | Telehealth privacy information provided at scheduling; pre-visit checklist includes privacy tips (private location, headphones, secure WiFi) |
| Incident Response | Telehealth-specific incident playbook covering: unauthorized access to session, recording breach, platform compromise |
| Compliance Monitoring | Monthly audit of telehealth session compliance: location verification completion, consent documentation, platform adherence |

### Environmental Security for Providers

Asclepius requires providers conducting telehealth to:
- Use a private room with closed door (no shared/open workspaces)
- Ensure no patient information visible on whiteboards, screens, or papers behind the provider
- Use headphones or earbuds to prevent audio leakage
- Lock workstation screen when stepping away during a session
- Not conduct telehealth visits from public locations (coffee shops, airports)
- Use only Asclepius-managed or approved devices for telehealth

## Enforcement

- **OCR Enforcement Discretion (2020-2023)**: During the COVID-19 PHE, OCR exercised enforcement discretion for good-faith telehealth. Post-PHE, full HIPAA enforcement applies.
- **No OCR enforcement actions specific to telehealth privacy violations as of early 2025**, but OCR has emphasized that the return to normal enforcement means platforms must be HIPAA-compliant with BAAs.
- **State AG actions**: Multiple state AGs have investigated telehealth companies for privacy practices, particularly regarding consumer-facing telehealth apps that may not be HIPAA-covered entities (Cerebral, Done Health — FTC and state AG investigations in 2023-2024 for unauthorized PHI disclosure to third-party advertisers).

## Integration Points

- **hipaa-privacy-rule**: All telehealth encounters are subject to full Privacy Rule compliance
- **hipaa-security-rule**: Telehealth platforms must meet all technical safeguards; transmission security is paramount
- **hipaa-baa-management**: Telehealth vendors require BAAs; evaluation of vendor security posture is critical
- **hipaa-breach-notify**: Platform compromises or unauthorized recording access trigger breach analysis
- **healthcare-ai-privacy**: AI integrated into telehealth (AI scribes, clinical decision support during visits) creates compound obligations
- **42-cfr-part-2**: Telehealth SUD treatment encounters are subject to Part 2 protections in addition to HIPAA
