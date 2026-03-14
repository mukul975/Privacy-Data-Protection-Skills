# Biometric Processing DPIA Report

## Reference: DPIA-QLH-2026-0008

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| System | Secure Research Laboratory Fingerprint Access Control |
| Biometric Modality | Fingerprint (minutiae-based template) |
| Processing Mode | Verification (1:1 matching) |
| Date | 2026-03-05 |
| Next Review | 2026-09-05 |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |

---

## 1. System Description

QuantumLeap Health Technologies deploys fingerprint verification scanners at the entrance to the Secure Research Laboratory in Berlin and London offices. The laboratory contains patient clinical trial data, biological samples, and experimental pharmaceutical compounds requiring controlled access under GxP guidelines and EU Clinical Trials Regulation 536/2014.

| Component | Detail |
|-----------|--------|
| Scanner | HID DigitalPersona 4500 optical fingerprint reader |
| Template format | ISO/IEC 19794-2 minutiae template (not raw fingerprint image) |
| Template storage | Encrypted on employee's NFC smart card (not in centralised database) |
| Matching | On-device comparison: live scan matched against card-stored template |
| Enrolled users | 142 research staff with laboratory access authorisation |
| Fallback | Card + PIN access available for all enrolled users without penalty |
| Liveness detection | Capacitive sensor layer detecting live tissue conductivity |

---

## 2. Art. 9 Analysis

### Art. 9(1) Applicability

Fingerprint data processed through the scanner is biometric data under Art. 4(14) processed for the purpose of uniquely identifying natural persons. Art. 9(1) prohibition applies.

### Art. 9(2) Exemption

**Exemption relied upon**: Art. 9(2)(b) — processing is necessary for the purposes of carrying out obligations and exercising specific rights of the controller or of the data subject in the field of employment law.

| Requirement | Compliance |
|-------------|-----------|
| Member State law | BDSG Section 26(3) authorises biometric processing where necessary for the employment relationship and proportionate, with employee rights safeguarded |
| Necessity for employment obligation | GxP regulatory requirements mandate that only authorised personnel access clinical trial materials; identity verification (not just card possession) is a regulatory necessity |
| Proportionality | Fingerprint verification is the least intrusive biometric modality suitable for the purpose; on-card template storage minimises data breach risk |
| Suitable safeguards | Non-biometric fallback available; works council agreement; template on employee card (not centralised); explicit employee information |

**Alternative: Consent (Art. 9(2)(a))**
Consent was considered but rejected. In the employment context, consent is presumptively not freely given due to the power imbalance (WP29 Opinion 2/2017, p.7). Employees may feel compelled to consent to maintain their employment. Art. 9(2)(b) provides a more robust legal basis.

---

## 3. Necessity and Proportionality

### 3.1 Purpose

Controlled physical access to the Secure Research Laboratory to ensure that only authorised research personnel can enter the facility, in compliance with:
- EU Clinical Trials Regulation 536/2014 Art. 61 (facility requirements)
- ICH GCP E6(R2) Section 8 (investigator site documentation and access)
- Company GxP access control policy (GxP-AC-003, version 2.1)

### 3.2 Alternatives Evaluated

| Alternative | Security Level | Outcome |
|-------------|---------------|---------|
| Card/badge access (ALT1) | Medium | **Rejected**: 2025 GxP audit found three incidents of card sharing and one incident of unauthorised access using a found card. Card-based access does not verify identity, only card possession. |
| PIN authentication (ALT2) | Medium | **Rejected**: PIN sharing observed among team members during 2025 audit. PINs written on notes near workstations. |
| Card + PIN (ALT3) | High | **Considered**: Addresses card-only weakness but PIN sharing still possible. Does not meet GxP auditor recommendation for identity verification. |
| **Fingerprint verification (selected)** | **Very High** | **Selected**: Non-transferable authentication. Verifies the individual's identity, not possession of a credential. Meets GxP auditor recommendation for biometric identity verification of laboratory personnel. |

### 3.3 Least Intrusive Biometric Assessment

| Biometric Option | Intrusiveness | Assessment |
|-----------------|---------------|-----------|
| Facial recognition | High (ambient capture, demographic bias) | Rejected — more intrusive than fingerprint; captures all persons in area |
| Iris scanning | Medium (controlled capture) | Rejected — more expensive, no significant security advantage over fingerprint for 1:1 verification |
| **Fingerprint (selected)** | **Low-Medium** | **Selected — requires voluntary physical contact; no ambient capture; well-established accuracy benchmarks; on-card template storage possible** |

---

## 4. Risk Assessment

| Risk | Likelihood | Severity | Level | Mitigation | Residual Level |
|------|-----------|----------|-------|------------|---------------|
| BIO-R1: Fingerprint template breach | Remote | Maximum | Medium | Template stored on employee's smart card (not centralised database); template encrypted with AES-256; card revocation capability | Low |
| BIO-R2: Function creep (templates repurposed for attendance monitoring) | Possible | Significant | High | Technical: scanner system isolated from HR/attendance systems with no data integration. Organisational: works council agreement explicitly prohibits attendance use. Policy: annual audit of biometric data access logs. | Low |
| BIO-R3: False rejection (elderly employees, employees with skin conditions) | Possible | Limited | Medium | Non-biometric fallback (card + PIN) available without penalty. Accommodation process for employees with conditions affecting fingerprint quality. FRR threshold set at 0.1% with manual override. | Low |
| BIO-R4: Spoofing with artificial fingerprint | Remote | Significant | Medium | Capacitive liveness detection. Multi-spectral imaging. Anti-spoofing tested to ISO 30107-3 Level 2. | Low |
| BIO-R5: Irreversibility of compromised biometric data | Remote | Maximum | Medium | On-card storage limits breach scope to individual cards. Cancellable biometric template format enables re-enrollment with different transformation parameters if card compromised. | Low |

---

## 5. Data Subject Rights

| Right | Implementation |
|-------|---------------|
| Information (Art. 13) | Employees receive biometric processing notice at enrollment. Laboratory signage indicates biometric access in use. |
| Access (Art. 15) | Employees can request confirmation of biometric processing and a copy of their template metadata (not the template itself, which is on their card). |
| Erasure (Art. 17) | Upon termination or role change, smart card is returned and template is destroyed. Confirmation of deletion provided. |
| Restriction (Art. 18) | Employee can request switch to card + PIN fallback while processing is restricted. |
| Objection (Art. 21) | Employee can opt for card + PIN alternative at any time without justification required. |

---

## 6. Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-03-05 |
| Head of Research | Prof. Dr. Henrik Johansson | 2026-03-05 |
| Works Council Representative | Thomas Richter | 2026-03-06 |
| CISO | Dr. James Okonkwo | 2026-03-06 |
| COO | Dr. Priya Sharma | 2026-03-07 |
