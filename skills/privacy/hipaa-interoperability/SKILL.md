---
name: hipaa-interoperability
description: >-
  Addresses HIPAA privacy and security requirements for health data
  interoperability under the 21st Century Cures Act, ONC Health IT
  Certification Program, and CMS Interoperability and Patient Access Final
  Rule. Covers information blocking prohibitions, FHIR API patient access,
  TEFCA exchange purposes, and privacy safeguards for health information
  exchange. Keywords: interoperability, information blocking, FHIR, TEFCA,
  Cures Act, patient access API, health information exchange.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, interoperability, information-blocking, fhir, tefca, cures-act, patient-access, hie"
---

# HIPAA Interoperability — Cures Act, ONC, and CMS Requirements

## Overview

The 21st Century Cures Act (Public Law 114-255, 2016) fundamentally changed the interoperability landscape by prohibiting information blocking and mandating standardized API-based patient access. The ONC Health IT Certification Program (45 CFR Part 170) and the CMS Interoperability and Patient Access Final Rule (CMS-9115-F, 85 FR 25510, May 1, 2020) together require health IT developers, healthcare providers, health information exchanges (HIEs), and health information networks (HINs) to support seamless data exchange while maintaining HIPAA privacy and security protections. The Trusted Exchange Framework and Common Agreement (TEFCA), launched operationally in December 2023, establishes a nationwide framework for health information exchange with defined exchange purposes and privacy requirements.

## Regulatory Framework

### 21st Century Cures Act — Information Blocking

- **Section 4004**: Defines information blocking as a practice that is likely to interfere with, prevent, or materially discourage access, exchange, or use of electronic health information (EHI)
- **Actors covered**: Health IT developers of certified health IT, HIEs, HINs, and healthcare providers
- **EHI definition**: As of October 6, 2022, EHI is the electronic protected health information (ePHI) in a designated record set as defined under HIPAA (45 CFR §171.102), plus any other electronic health information identified by the Secretary

### Information Blocking Exceptions (45 CFR Part 171)

| Exception | Category | Description |
|-----------|----------|-------------|
| Preventing Harm (§171.201) | Not fulfilling requests | Practice is reasonable and necessary to prevent harm to a patient or another person |
| Privacy (§171.202) | Not fulfilling requests | Practice is required by or consistent with HIPAA Privacy Rule obligations |
| Security (§171.203) | Not fulfilling requests | Practice is directly related to safeguarding the confidentiality, integrity, or availability of EHI |
| Infeasibility (§171.204) | Not fulfilling requests | Fulfilling the request is technically infeasible |
| Health IT Performance (§171.205) | Procedures | Practice is for reasonable maintenance or improvements to health IT |
| Content and Manner (§171.301) | Procedures | Actor fulfills a request in an alternative manner or with alternative content |
| Fees (§171.302) | Procedures | Fees charged are reasonable and based on objective, verifiable criteria |
| Licensing (§171.303) | Procedures | Licensing terms are reasonable and non-discriminatory |

### CMS Interoperability and Patient Access Final Rule

- **Patient Access API (§431.60)**: CMS-regulated payers (Medicaid, CHIP, QHP issuers on FFE) must implement a FHIR R4-based Patient Access API allowing patients to access claims, encounter, and clinical data
- **Provider Directory API (§431.70)**: Payers must implement a publicly accessible FHIR-based provider directory
- **Payer-to-Payer Data Exchange (CMS-0057-F, effective January 1, 2026)**: Payers must exchange patient data at the patient's request when they switch plans
- **Prior Authorization API (CMS-0057-F)**: Payers must implement a FHIR-based prior authorization API

### TEFCA Exchange Purposes

| Exchange Purpose | Description | HIPAA Basis |
|-----------------|-------------|-------------|
| Treatment | Direct patient care | §164.506(c)(2) — TPO |
| Payment | Claims, eligibility, coordination of benefits | §164.506(c)(3) — TPO |
| Healthcare Operations | Quality assessment, care coordination | §164.506(c)(5) — TPO |
| Public Health | Reporting to public health authorities | §164.512(b) |
| Benefits Determination | Health plan coverage decisions | §164.506(c)(3) |
| Individual Access | Patient right of access | §164.524 |

## HIPAA Privacy Safeguards for Interoperability

### Patient Access via FHIR API

1. **Identity verification**: Verify patient identity using multi-factor authentication before granting API access (aligned with NIST IAL2/AAL2)
2. **Scope of access**: HIPAA right of access (§164.524) — entire designated record set except psychotherapy notes, information compiled for legal proceedings, and certain lab results under CLIA
3. **Third-party app authorization**: Patient may direct data to third-party apps via SMART on FHIR; once data is shared with a non-covered entity app, HIPAA protections may no longer apply — disclosure notice required
4. **Minimum necessary**: Does NOT apply to individual access requests (§164.502(b)(2)(v)) or treatment disclosures

### HIE/HIN Privacy Requirements

1. Maintain BAAs with all participating providers per §164.502(e)
2. Implement role-based access tied to exchange purpose
3. Apply consent management per state law requirements (particularly for 42 CFR Part 2 substance abuse records and state-specific sensitive categories)
4. Maintain accounting of disclosures per §164.528

## Security Requirements for Interoperable Systems

| Requirement | Regulation | Implementation |
|------------|-----------|----------------|
| Encryption in transit | §164.312(e)(1) | TLS 1.2+ for all FHIR API and HIE connections |
| Access controls | §164.312(a)(1) | OAuth 2.0 / SMART on FHIR authorization |
| Audit controls | §164.312(b) | Log all API requests, queries, and data exchanges with timestamps and actor identity |
| Integrity controls | §164.312(c)(1) | Digital signatures on exchange payloads; FHIR resource versioning |
| Authentication | §164.312(d) | Unique user identification for all API consumers; system-level certificates for point-to-point |

## Enforcement

- **Information blocking penalties**: Health IT developers, HIEs, and HINs face civil monetary penalties up to $1 million per violation under ONC (final rule effective September 1, 2023). Healthcare providers face appropriate disincentives through CMS (final rule pending).
- **HIPAA penalties**: Standard HIPAA enforcement under OCR applies to all privacy and security violations in the interoperability context.

## Integration Points

- **hipaa-privacy-rule**: Interoperability must comply with all Privacy Rule requirements for uses and disclosures
- **hipaa-security-rule**: Technical safeguards for API and exchange security
- **hipaa-minimum-necessary**: Minimum necessary standard applies to most interoperability disclosures (except individual access and treatment)
- **hipaa-baa-management**: BAAs required for all HIE/HIN participants and health IT vendors accessing PHI
- **hipaa-breach-notification**: Breach notification obligations extend to interoperability-related incidents
