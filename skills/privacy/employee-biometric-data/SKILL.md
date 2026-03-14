---
name: employee-biometric-data
description: >-
  Governs biometric data processing for employee timekeeping and access control
  under Art. 9 GDPR special category rules. Covers fingerprint, facial
  recognition, iris scanning, and voice recognition. Applies necessity tests,
  evaluates less intrusive alternatives, and implements employee objection
  procedures. Keywords: biometric data, Art. 9, fingerprint, facial
  recognition, access control, timekeeping, special category.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: employee-data-privacy
  tags: "biometric-data, article-9, fingerprint, facial-recognition, access-control, special-category"
---

# Employee Biometric Data

## Overview

Biometric data is classified as a special category of personal data under Art. 9(1) GDPR when processed for the purpose of uniquely identifying a natural person. Processing biometric data for employee timekeeping and access control is one of the most frequently scrutinised activities by European supervisory authorities. The general prohibition on processing special category data under Art. 9(1) means that employers must identify a specific exception under Art. 9(2), satisfy the proportionality requirement, demonstrate that no less intrusive alternative exists, and implement robust safeguards. National DPAs have issued substantial fines for biometric processing that fails these tests, including the landmark Clearview AI enforcement actions and sector-specific decisions on workplace fingerprint systems.

## Legal Framework

### Art. 4(14) — Definition of Biometric Data

"Biometric data means personal data resulting from specific technical processing relating to the physical, physiological or behavioural characteristics of a natural person, which allow or confirm the unique identification of that natural person, such as facial images or dactyloscopic data."

### Art. 9(1) — General Prohibition

"Processing of [...] biometric data for the purpose of uniquely identifying a natural person [...] shall be prohibited."

**Critical distinction**: Biometric data processed for purposes other than unique identification may not be classified as special category data under Art. 9(1). However, in the employment context, biometric processing for timekeeping and access control is almost always for identification purposes.

### Art. 9(2) — Exceptions Applicable to Employment

| Exception | Article | Applicability to Employment Biometrics |
|-----------|---------|---------------------------------------|
| Explicit consent | Art. 9(2)(a) | Rarely valid due to employment power imbalance (see employment-consent-limits skill) |
| Employment law obligation | Art. 9(2)(b) | Valid where national law specifically mandates or authorises biometric processing for employment purposes |
| Substantial public interest | Art. 9(2)(g) | Valid where national law establishes biometric access control requirements for critical infrastructure |
| Not applicable | Art. 9(2)(e) | Data "manifestly made public" — employees do not manifestly make their biometric data public |

### Key National Derogations

**France — Art. L.1121-1 Labour Code + CNIL Framework**:
- CNIL published dedicated guidance: "Règlement type biométrie" (Deliberation No. 2019-001, 10 January 2019)
- Biometric access control is permitted for access to premises, devices, and applications where justified by the context
- Storage preference hierarchy: (1) individual device held by employee (badge), (2) centralised database with employee control, (3) centralised database without employee control (requires strongest justification)
- The employee must be informed and provided an alternative non-biometric access method

**Germany — Section 26(3) BDSG**:
- Processing of special category data including biometrics is permitted for employment purposes where necessary for the exercise of rights or obligations under employment law, social security law, or social protection law
- Works council co-determination rights under Section 87(1)(6) BetrVG apply

**Netherlands — UAVG Art. 29**:
- Biometric processing is permitted for authentication or security purposes where necessary
- The Dutch DPA (Autoriteit Persoonsgegevens) has issued specific guidance restricting biometric processing to high-security contexts

**Italy — Workers' Statute Art. 4 + Garante Guidance**:
- Biometric access control requires trade union agreement or labour inspectorate authorisation
- The Garante has issued multiple decisions restricting biometric timekeeping to specific sectors

**Sweden — Datainspektionen Decisions**:
- The Swedish DPA fined a school SEK 200,000 for using facial recognition for attendance monitoring (DI-2019-2221), setting a strong precedent that biometric monitoring for attendance is disproportionate when simpler alternatives exist

## Biometric Technologies in Employment

### Fingerprint Recognition

**Use cases**: Timekeeping (clocking in/out), physical access control, device authentication.

**Technical processing**: Fingerprint scanner captures an image of friction ridges → image is processed to extract minutiae points → minutiae template is compared against stored templates → match/no-match result.

**Privacy considerations**:
- Template storage: Store templates on individual smart cards held by the employee (less intrusive) rather than in a centralised database (more intrusive)
- Revocability: Unlike passwords, fingerprints cannot be changed if compromised
- False acceptance rate (FAR) and false rejection rate (FRR) must be documented
- Employees with skin conditions, injuries, or disabilities affecting fingerprints must have an alternative access method

**Atlas Manufacturing Group Example**: Atlas installed fingerprint scanners for access to its R&D laboratory where proprietary formulations are developed. The DPO approved the deployment based on Art. 9(2)(b) (German BDSG Section 26(3)) for the R&D laboratory only, with the following conditions: (1) fingerprint templates stored on employee ID badges, not in a central database, (2) alternative PIN access available for employees who object or have medical conditions, (3) DPIA completed before deployment, (4) works council consulted and agreement obtained.

### Facial Recognition

**Use cases**: Contactless access control, time and attendance, security zones.

**Technical processing**: Camera captures facial image → facial geometry is measured (distance between eyes, nose shape, jawline contour) → geometry data converted to mathematical template → template compared against enrolled images.

**Privacy considerations**:
- Facial recognition is significantly more intrusive than fingerprint scanning because it can operate without the employee's active cooperation or awareness (passive vs. active biometric)
- Continuous facial recognition in the workplace may constitute systematic monitoring, triggering additional DPIA requirements
- Risk of function creep: facial recognition deployed for access may be expanded to emotion detection, attention monitoring, or behavioural analysis
- Bias and accuracy: Facial recognition systems have documented higher error rates for certain demographic groups, creating discrimination risk

**Supervisory Authority Position**: Most European DPAs take the position that facial recognition for general time and attendance purposes is disproportionate when simpler alternatives (badge, PIN, fingerprint) are available. Facial recognition may be justified only for high-security access control where contactless verification is necessary (cleanroom environments, nuclear facilities).

### Iris Scanning

**Use cases**: High-security access control, authentication in environments where hand-based biometrics are impractical (e.g., clean environments requiring gloves).

**Privacy considerations**:
- Among the most accurate biometric modalities (FAR below 0.0001%)
- Less affected by environmental factors than fingerprint
- Generally limited to high-security contexts where the heightened intrusion is justified

### Voice Recognition

**Use cases**: Telephone-based authentication, call centre agent verification, voice-activated systems.

**Privacy considerations**:
- Voice data may reveal health information (fatigue, intoxication, emotional state), potentially creating additional Art. 9 issues
- Voice templates are more susceptible to spoofing than other biometric modalities
- Ambient noise and voice changes (illness, ageing) affect accuracy

### Behavioural Biometrics

**Use cases**: Keystroke dynamics, gait analysis, mouse movement patterns.

**Privacy considerations**:
- Often collected passively without explicit employee action
- May reveal health conditions (tremor, cognitive impairment)
- The EDPB has not yet issued specific guidance on behavioural biometrics in employment, but existing principles on proportionality and transparency apply

## Necessity Test Framework

Before deploying any biometric system, the employer must demonstrate that the biometric processing is genuinely necessary and that no less intrusive alternative would achieve the same purpose.

### Step 1: Define the Specific Purpose

The purpose must be concrete, documented, and limited:
- "Controlling access to the R&D laboratory containing proprietary formulations" — acceptable
- "Improving workforce management" — too vague
- "Ensuring accurate time and attendance records" — biometric processing is unlikely to be necessary for this purpose

### Step 2: Evaluate Less Intrusive Alternatives

| Purpose | Biometric Solution | Less Intrusive Alternative | Necessity of Biometrics |
|---------|-------------------|---------------------------|------------------------|
| Physical access to high-security area | Fingerprint scanner | Smart card + PIN | Biometric may be justified if tailgating/card sharing is a documented security concern |
| General building access | Facial recognition | Badge/proximity card | Biometric is disproportionate; badge provides equivalent security |
| Time and attendance | Fingerprint clock | Badge, PIN code, supervisor sign-off | Biometric is disproportionate; buddy punching can be addressed through supervision |
| Device authentication | Fingerprint/face unlock | Password, smart card | Biometric may be justified for high-sensitivity devices where password risk is documented |
| Cleanroom access | Iris scan | Badge + airlock | Biometric may be justified where contactless identification is operationally necessary |

### Step 3: Proportionality Assessment

Even if biometric processing passes the necessity test, it must also be proportionate:
- Is the security risk significant enough to justify processing special category data?
- Is the biometric system targeted (limited to specific areas/roles) or blanket (all employees)?
- Are adequate safeguards in place (template storage, retention, access controls)?
- Is an alternative non-biometric method available for employees who object?

## Employee Objection Procedures

Regardless of the lawful basis, employers must provide a meaningful objection mechanism:

### Objection Process

1. **Information at enrolment**: When employees are asked to enrol biometric data, they must be informed of:
   - The specific purpose of biometric processing
   - The lawful basis (Art. 9(2) condition and Art. 6(1) basis)
   - The availability of an alternative non-biometric method
   - Their right to object or withdraw (where consent is the basis)
   - Data retention period and deletion procedures

2. **Alternative access method**: A non-biometric alternative must be available at all times:
   - PIN code + proximity badge for access control
   - Manual sign-in sheet or supervisor confirmation for timekeeping
   - Password or smart card for device authentication

3. **No adverse consequences**: Employees who use the alternative method must not suffer any disadvantage:
   - No additional time required to use the alternative
   - No flagging in attendance systems
   - No negative note in personnel records

4. **Formal objection handling**: Objections must be:
   - Recorded in the privacy management system
   - Acknowledged within 5 working days
   - Actioned immediately (switch to alternative method)
   - Reviewed by the DPO

### Special Circumstances

- **Disability**: Employees with conditions affecting biometric characteristics (skin conditions, prosthetics, facial differences) must be provided accessible alternatives without requirement to disclose their condition
- **Religious objections**: Some employees may object to biometric collection on religious grounds; the alternative must accommodate this
- **Trade union representatives**: Works council members may object on behalf of represented employees under national co-determination rights

## Data Protection Safeguards

### Template Storage Hierarchy (per CNIL Règlement Type Biométrie)

| Storage Method | Risk Level | When Appropriate |
|---------------|------------|-----------------|
| Individual device (badge, token) held by employee | Lowest | Default preferred method for all biometric deployments |
| Centralised database with employee-controlled access key | Medium | Where individual device storage is technically infeasible |
| Centralised database without employee control | Highest | Only for specific, documented security requirements with strongest justification |

### Technical Safeguards

- Biometric templates must be encrypted at rest (AES-256 minimum) and in transit (TLS 1.3)
- Raw biometric data (fingerprint images, facial photographs) must not be stored; only derived templates should be retained
- Template format must be system-specific to prevent cross-system matching
- Anti-spoofing measures (liveness detection) must be implemented
- Biometric systems must be isolated from general IT networks
- Access to biometric databases must be restricted to authorised security personnel with multi-factor authentication
- Audit logs of all biometric system access must be maintained

### Retention and Deletion

- Biometric templates must be deleted immediately upon termination of employment
- Biometric templates must be deleted immediately upon employee objection or consent withdrawal
- Biometric templates must be deleted when the processing purpose ceases (e.g., employee transfers to a role that does not require access to the secured area)
- Deletion must be verified and documented with certificates of destruction

## Enforcement Precedents

| Authority | Case | Fine/Outcome | Key Issue |
|-----------|------|-------------|-----------|
| Datainspektionen (Sweden) | DI-2019-2221 | SEK 200,000 | School used facial recognition for student attendance — disproportionate, simpler alternatives available |
| CNIL (France) | Clearview AI, 2022 | EUR 20,000,000 | Biometric processing (facial recognition) without lawful basis or DPIA |
| AEPD (Spain) | PS/00218/2021 | EUR 20,000 | Employer required fingerprint for timekeeping without necessity assessment or alternative method |
| Garante (Italy) | Provvedimento 9832838, 2021 | Processing prohibited | Employer deployed facial recognition for access control without necessity analysis or Art. 9(2) condition |
| Autoriteit Persoonsgegevens (NL) | 2020 Investigation | Warning + cease order | Employer used fingerprint timekeeping; AP found it disproportionate for attendance purposes |
| ICO (UK) | Enforcement notice, 2022 | Processing ordered to cease | Employer deployed palm vein scanning for general access without DPIA |

## Integration Points

- **Employee Monitoring DPIA**: Biometric systems must undergo DPIA (see employee-monitoring-dpia skill).
- **Employment Consent Limits**: Consent for biometric processing is constrained by employment power imbalance (see employment-consent-limits skill).
- **HR System Privacy Config**: Biometric integration with HR/timekeeping systems requires privacy configuration (see hr-system-privacy-config skill).
- **Background Check Privacy**: Biometric data collected for access control must be separated from background check data (see background-check-privacy skill).
