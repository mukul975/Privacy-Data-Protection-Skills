# Data Protection Impact Assessment -- Biometric System

## Assessment Details

| Field | Value |
|-------|-------|
| DPIA Reference | DPIA-BIO-2026-003 |
| Assessment Date | 2026-03-15 |
| Controller | NovaPharma GmbH |
| DPO | Dr. Sabine Kessler, Group DPO |
| DPIA Lead | Information Security & Privacy Office |
| Review Cycle | Annual (next: 2027-03-15) |

---

## Section 1: Biometric System Description

| Field | Value |
|-------|-------|
| System Name | SecureEntry Fingerprint Access Control |
| Modality | Fingerprint Recognition |
| Matching Mode | 1:1 Verification |
| Template Storage | On-device (employee ID badge) -- CNIL Tier 1 |
| Vendor | Suprema BioStar 2 |
| Enrolled Subjects | 2,400 (employees and contractors) |
| Daily Transactions | 9,600 |
| Deployment Locations | HQ Building A, R&D Laboratory, Data Centre |
| Liveness Detection | Yes (capacitive + temperature sensing, ISO 30107 Level 2) |
| ISO 24745 Compliant | Yes (cancelable biometric templates) |
| Non-Biometric Alternative | PIN + proximity badge available at all access points |

---

## Section 2: DPIA Obligation

| EDPB Criterion | Met | Reason |
|----------------|-----|--------|
| Special category data (Criterion 4) | Yes | Fingerprint data for unique identification under Art. 9(1) |
| Large-scale processing (Criterion 5) | Yes | 2,400 enrolled subjects, 9,600 daily transactions |
| Systematic monitoring (Criterion 3) | No | Fingerprint is active biometric (not passive surveillance) |
| Innovative technology (Criterion 8) | No | Fingerprint verification is established technology |
| Vulnerable data subjects (Criterion 7) | Yes | Employees (power imbalance in employment relationship) |
| Automated decision-making (Criterion 2) | Yes | Automated access grant/deny decisions |

**Conclusion**: DPIA mandatory -- 4 of 6 EDPB criteria met.

---

## Section 3: Necessity and Proportionality

### Purpose
Controlling physical access to R&D laboratory containing proprietary pharmaceutical formulations and data centre housing patient clinical trial data.

### Lawful Basis
Art. 6(1)(b)/(c) Employment + Art. 9(2)(b) Employment Obligations under German BDSG Section 26(3).

### Alternatives Evaluated

| Alternative | Assessment | Reason Insufficient |
|-------------|-----------|-------------------|
| Proximity badge only | Insufficient | 17 tailgating incidents in 12 months; badge sharing in 3 audit findings |
| Badge + PIN | Insufficient | PIN sharing in 8 cases; fails pharmaceutical GMP compliance |
| Smart card + password | Impractical | Cleanroom gloving prevents keyboard input |

### Conclusions

| Test | Result | Rationale |
|------|--------|-----------|
| Necessity | Necessary | Biometric verification required for pharmaceutical cleanroom and data centre; documented failure of less intrusive alternatives |
| Proportionality | Proportionate | Targeted to 3 high-security locations; on-device storage; alternative method available |

### DPO Advice
DPO concurs with necessity finding for R&D and data centre. Recommends annual review and demographic accuracy audit across employee population.

---

## Section 4: Risk Assessment

| Risk ID | Category | Description | Likelihood | Severity | Inherent Score | Inherent Level | Residual Score | Residual Level |
|---------|----------|-------------|-----------|----------|---------------|----------------|---------------|----------------|
| BIO-R1 | Template Breach | Unauthorised access to fingerprint templates; irrevocable identity data | 2 | 4 | 8 | High | 1 | Low |
| BIO-R2 | Function Creep | Access control data repurposed for time monitoring | 2 | 3 | 6 | Medium | 1 | Low |
| BIO-R3 | Discrimination | Varying scanner accuracy by demographic group | 3 | 3 | 9 | High | 2 | Low |
| BIO-R4 | Spoofing | Artificial fingerprint bypass attempt | 2 | 3 | 6 | Medium | 1 | Low |
| BIO-R5 | Vendor Data Access | Vendor support staff accessing templates | 2 | 4 | 8 | High | 1 | Low |
| BIO-R6 | Irrevocability | Lifetime impact of compromised fingerprint data | 2 | 4 | 8 | High | 2 | Low |

---

## Section 5: Mitigation Measures

### M1: On-Device Template Storage

| Field | Value |
|-------|-------|
| Description | Templates stored exclusively on employee ID badges (CNIL Tier 1); no centralised fingerprint database exists |
| Standard | CNIL Reglement Type Biometrie / ISO/IEC 24745:2022 |
| Addresses | BIO-R1, BIO-R6 |
| Status | Verified |

### M2: Template and Transit Encryption

| Field | Value |
|-------|-------|
| Description | AES-256 encryption of templates on badge chip; TLS 1.3 for all scanner-to-controller communication |
| Standard | GDPR Art. 32(1)(a) |
| Addresses | BIO-R1 |
| Status | Verified |

### M3: Purpose Limitation Architecture

| Field | Value |
|-------|-------|
| Description | Technical controls restricting fingerprint use to physical access only; system architecture prevents data export to HR, payroll, or time and attendance systems |
| Standard | GDPR Art. 5(1)(b) Purpose Limitation |
| Addresses | BIO-R2 |
| Status | Implemented |

### M4: Alternative Access Method

| Field | Value |
|-------|-------|
| Description | PIN + proximity badge alternative available at all access points for employees with skin conditions, injuries, religious objections, or general objection; no adverse consequences policy signed by HR Director |
| Standard | CNIL Reglement Type Biometrie |
| Addresses | BIO-R3 |
| Status | Verified |

### M5: Demographic Accuracy Audit

| Field | Value |
|-------|-------|
| Description | Quarterly accuracy audit across employee demographic groups; scanner recalibration triggered when False Rejection Rate exceeds 2% for any group |
| Standard | ISO/IEC 19795:2021 |
| Addresses | BIO-R3 |
| Status | Implemented (first audit completed Q1 2026) |

### M6: Liveness Detection

| Field | Value |
|-------|-------|
| Description | Suprema BioStar 2 capacitive + temperature sensing liveness detection; ISO 30107 Level 2 certified; defeats photograph, silicone, and gelatin spoofing attacks |
| Standard | ISO/IEC 30107:2023 |
| Addresses | BIO-R4 |
| Status | Verified |

### M7: Vendor Access Restriction

| Field | Value |
|-------|-------|
| Description | Art. 28 DPA with Suprema prohibiting remote template access; all maintenance conducted on-site with DPO observer present; audit clause exercised annually |
| Standard | GDPR Art. 28(3) |
| Addresses | BIO-R5 |
| Status | Verified |

### M8: Cancelable Biometric Transformation

| Field | Value |
|-------|-------|
| Description | System-specific irreversible template transformation using cancelable biometrics; templates from this system cannot be matched against templates in any other biometric system |
| Standard | ISO/IEC 24745:2022 Section 6 |
| Addresses | BIO-R6 |
| Status | Verified |

---

## Section 6: Template Storage Assessment (CNIL Hierarchy)

| Field | Value |
|-------|-------|
| Storage Method | On-device (employee ID badge) |
| CNIL Tier | Tier 1 (Lowest Risk) |
| Justification | Standard justification sufficient |
| Assessment | Compliant with preferred storage method per CNIL Reglement Type Biometrie |

---

## Section 7: Art. 36 Prior Consultation

| Field | Value |
|-------|-------|
| Prior Consultation Required | **No** |
| Rationale | All residual risks reduced to Low after mitigation; no 1:N identification; alternative method available |
| Condition | Re-assess if system expanded beyond current 3 locations or to new modalities |

---

## Section 8: Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Sabine Kessler | 2026-03-15 | DPIA approved; residual risk acceptable |
| CISO | Thomas Richter | 2026-03-15 | Technical safeguards adequate; M5 ongoing audit confirmed |
| Head of R&D | Prof. Dr. Martin Weber | 2026-03-15 | Operational necessity confirmed for cleanroom and data centre |
| Works Council Chair | Andrea Hoffmann | 2026-03-14 | Works council consulted; agreement obtained per BetrVG Section 87(1)(6) |
| Head of HR | Julia Braun | 2026-03-15 | Alternative access method confirmed; no adverse consequences policy signed |
