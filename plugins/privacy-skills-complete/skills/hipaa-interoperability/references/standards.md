# Standards and Regulatory References

## Primary Legislation

### 21st Century Cures Act (Public Law 114-255, 2016)
- **Section 4003**: Conditions and maintenance of certification for health IT developers
- **Section 4004**: Prohibition on information blocking — defines the practice and establishes penalties

### ONC Information Blocking Rule — 45 CFR Part 171
- **§171.102**: Definition of electronic health information (EHI) — as of October 6, 2022, includes all ePHI in a designated record set
- **§171.201**: Preventing Harm exception
- **§171.202**: Privacy exception — practice must be required by or consistent with HIPAA Privacy Rule obligations
- **§171.203**: Security exception — practice must be directly related to safeguarding confidentiality, integrity, or availability
- **§171.204**: Infeasibility exception
- **§171.301**: Content and Manner exception — provides alternative content or manner of fulfillment

### CMS Interoperability and Patient Access Final Rule (CMS-9115-F, 85 FR 25510)
- **§431.60**: Patient Access API requirements for Medicaid, CHIP, QHP issuers
- **§431.70**: Provider Directory API requirements
- **Effective dates**: January 1, 2021 (Patient Access API); January 1, 2026 (Payer-to-Payer exchange per CMS-0057-F)

### HIPAA Privacy Rule — Interoperability-Relevant Provisions
- **45 CFR §164.524**: Individual right of access to designated record set
- **45 CFR §164.506**: Uses and disclosures for treatment, payment, and healthcare operations
- **45 CFR §164.502(b)**: Minimum necessary standard and its exceptions
- **45 CFR §164.502(e)**: Business associate agreements required for HIE/HIN participation
- **45 CFR §164.528**: Accounting of disclosures — applies to HIE disclosures not for TPO

### HIPAA Security Rule — API and Exchange Security
- **45 CFR §164.312(a)(1)**: Access control — unique user identification for API consumers
- **45 CFR §164.312(b)**: Audit controls — logging of all API transactions
- **45 CFR §164.312(d)**: Person or entity authentication
- **45 CFR §164.312(e)(1)**: Transmission security — encryption for FHIR API and HIE connections

## Regulatory Guidance

- **ONC Cures Act Final Rule (85 FR 25642, May 1, 2020)**: Established information blocking regulations, updated health IT certification criteria, and mandated standardized API requirements.
- **ONC HTI-1 Final Rule (89 FR 1192, January 9, 2024)**: Updated health IT certification criteria including USCDI v3, decision support interventions, and information blocking enforcement updates.
- **TEFCA Common Agreement Version 2.0 (2024)**: Establishes governance, technical, and policy requirements for nationwide health information exchange through Qualified Health Information Networks (QHINs).
- **HL7 FHIR R4 (v4.0.1, 2019)**: Fast Healthcare Interoperability Resources standard mandated for Patient Access API and interoperability requirements.
- **SMART on FHIR (v2.0, 2023)**: Authorization framework for FHIR-based applications, supporting OAuth 2.0 scopes for granular access control.

## Enforcement Actions and Guidance

- **ONC Information Blocking CMPs (effective September 1, 2023)**: Health IT developers, HIEs, and HINs face penalties up to $1 million per violation. First enforcement actions initiated in 2024.
- **CMS Interoperability Enforcement**: CMS ties interoperability compliance to program participation conditions for Medicaid, CHIP, and Qualified Health Plans.

## Technical Standards

- **USCDI (United States Core Data for Interoperability)**: Standardized health data classes and elements required for certified health IT — USCDI v3 as of HTI-1 rule.
- **NIST SP 800-63-3 (Digital Identity Guidelines)**: Identity assurance levels (IAL) and authenticator assurance levels (AAL) referenced for patient identity verification in API access.
- **ISO/IEC 27001:2022**: Information security management system — applicable to HIE/HIN security governance.
