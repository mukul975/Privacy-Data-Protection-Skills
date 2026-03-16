---
name: us-privacy-federal
description: >-
  Maps the US federal privacy landscape including sectoral laws (HIPAA, GLBA,
  FERPA, COPPA, FCRA, ECPA, VPPA), FTC Section 5 enforcement, proposed
  federal comprehensive legislation, and the interaction between federal and
  state privacy regimes. Keywords: federal privacy, HIPAA, GLBA, FERPA,
  COPPA, FCRA, FTC, sectoral, preemption.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "federal-privacy, hipaa, glba, ferpa, coppa, fcra, ftc, sectoral-privacy"
---

# US Federal Privacy Landscape

## Overview

The United States does not have a single comprehensive federal data protection law equivalent to the GDPR. Instead, the US employs a sectoral approach, with federal laws addressing privacy in specific contexts: health care (HIPAA), financial services (GLBA), children's online data (COPPA), education (FERPA), consumer reporting (FCRA), electronic communications (ECPA), and video rental records (VPPA). The Federal Trade Commission (FTC) exercises broad privacy enforcement authority under Section 5 of the FTC Act, which prohibits unfair or deceptive acts or practices. This patchwork creates a complex compliance landscape that requires mapping federal obligations alongside the growing number of state comprehensive privacy laws.

## Federal Sectoral Privacy Laws

### Health Insurance Portability and Accountability Act (HIPAA)

- **Statute**: Pub. L. 104-191 (1996); HITECH Act, Pub. L. 111-5 (2009)
- **Regulations**: 45 CFR Parts 160, 162, 164
- **Scope**: Covered entities (health plans, health care clearinghouses, health care providers who transmit health information electronically) and their business associates
- **Key Requirements**:
  - Privacy Rule (45 CFR 164 Subpart E): use and disclosure limitations for Protected Health Information (PHI)
  - Security Rule (45 CFR 164 Subpart C): administrative, physical, and technical safeguards for ePHI
  - Breach Notification Rule (45 CFR 164 Subpart D): notification to individuals, HHS, and media for breaches of unsecured PHI
  - Individual rights: access, amendment, accounting of disclosures, restriction requests
- **Enforcement**: HHS Office for Civil Rights (OCR); state attorneys general
- **Penalties**: Up to USD 2,067,813 per violation per calendar year (2024 adjusted); criminal penalties up to USD 250,000 and 10 years imprisonment

### Gramm-Leach-Bliley Act (GLBA)

- **Statute**: Pub. L. 106-102 (1999)
- **Regulations**: Regulation P (12 CFR 1016); FTC Safeguards Rule (16 CFR 314)
- **Scope**: Financial institutions — broadly defined to include entities significantly engaged in financial activities (banks, insurance companies, securities firms, but also tax preparers, auto dealers offering financing, etc.)
- **Key Requirements**:
  - Financial Privacy Rule: notice of privacy practices and opt-out for sharing with non-affiliated third parties
  - Safeguards Rule: comprehensive information security programme with risk assessment, access controls, encryption, multi-factor authentication, incident response
  - Pretexting protections: prohibition on obtaining customer information through false pretences
- **Enforcement**: Prudential regulators (OCC, Fed, FDIC, NCUA), FTC, state insurance regulators, SEC, CFTC
- **2023 Amendments**: FTC Safeguards Rule substantially updated effective June 2023 — mandatory encryption, MFA, CISO designation, written incident response plan, periodic penetration testing

### Family Educational Rights and Privacy Act (FERPA)

- **Statute**: 20 U.S.C. 1232g; 34 CFR Part 99
- **Scope**: Educational agencies and institutions receiving federal funding
- **Key Requirements**:
  - Parents (or eligible students over 18) have the right to access education records and request amendments
  - Written consent required before disclosure of personally identifiable information from education records, with exceptions (directory information, legitimate educational interest, health/safety emergency, judicial order)
  - Annual notification of rights
- **Enforcement**: US Department of Education, Family Policy Compliance Office
- **Penalties**: Withdrawal of federal funding (in practice, compliance agreements and corrective action)

### Children's Online Privacy Protection Act (COPPA)

- **Statute**: 15 U.S.C. 6501-6506 (1998)
- **Regulations**: 16 CFR Part 312 (COPPA Rule)
- **Scope**: Operators of commercial websites and online services directed to children under 13, or that have actual knowledge of collecting personal information from children under 13
- **Key Requirements**:
  - Verifiable parental consent before collecting personal information from children
  - Clear privacy notice describing information practices
  - Parents' rights: review, delete, refuse further collection
  - Reasonable security measures
  - Data retention limitations
- **Enforcement**: FTC; state attorneys general
- **Penalties**: Up to USD 50,120 per violation (2024 adjusted)

### Fair Credit Reporting Act (FCRA)

- **Statute**: 15 U.S.C. 1681 et seq. (1970, amended by FACTA 2003)
- **Scope**: Consumer reporting agencies, users of consumer reports, furnishers of information
- **Key Requirements**:
  - Permissible purpose required to obtain consumer reports (credit, employment, insurance, government benefit, legitimate business need)
  - Accuracy obligations for furnishers
  - Consumer rights: free annual report, dispute inaccurate information, fraud alerts, credit freezes
  - Adverse action notices when consumer report information is used against the consumer
- **Enforcement**: CFPB, FTC, state attorneys general
- **Private Right of Action**: Yes — statutory damages, actual damages, attorney's fees

### Electronic Communications Privacy Act (ECPA)

- **Statute**: 18 U.S.C. 2510-2522 (Wiretap Act), 18 U.S.C. 2701-2712 (Stored Communications Act), 18 U.S.C. 3121-3127 (Pen Register Act)
- **Scope**: Interception of electronic communications, access to stored electronic communications, pen register and trap-and-trace devices
- **Key Requirements**:
  - Wiretap Act: prohibits intentional interception of wire, oral, or electronic communications (with consent and law enforcement exceptions)
  - Stored Communications Act: protects stored electronic communications from unauthorised access; governs law enforcement access
  - Pen Register Act: regulates real-time collection of metadata
- **Enforcement**: DOJ (criminal); private right of action (Wiretap Act and SCA)

### Video Privacy Protection Act (VPPA)

- **Statute**: 18 U.S.C. 2710 (1988)
- **Scope**: Video tape service providers (interpreted broadly to include streaming services)
- **Key Requirements**: Prohibits disclosure of personally identifiable rental or purchase information without consumer consent
- **Enforcement**: Private right of action; actual damages, punitive damages, attorney's fees
- **Note**: Increasingly relevant to streaming and OTT platforms; active plaintiff class action litigation

## FTC Section 5 Authority

The FTC's authority under Section 5 of the FTC Act (15 U.S.C. 45(a)) serves as a de facto federal privacy enforcement baseline:

- **Unfairness prong**: Practice causes or is likely to cause substantial injury not reasonably avoidable and not outweighed by countervailing benefits
- **Deception prong**: Material representation, omission, or practice likely to mislead consumers acting reasonably
- **Privacy-specific enforcement areas**:
  - Failure to honour privacy policy commitments
  - Inadequate data security practices
  - Deceptive data collection and sharing
  - Dark patterns in consent interfaces
  - Children's privacy violations (COPPA enforcement)
  - Health data practices (Health Breach Notification Rule, 16 CFR 318)

### FTC Health Breach Notification Rule (16 CFR Part 318)

- Applies to vendors of personal health records and PHR-related entities NOT covered by HIPAA
- Requires notification to FTC, individuals, and media of breaches of unsecured health information
- FTC has expanded interpretation to include health apps and connected devices

## Federal Preemption Considerations

The interaction between federal sectoral laws and state comprehensive privacy laws creates complex preemption questions:

- **HIPAA**: Preempts state laws that are contrary to HIPAA, but state laws providing greater protection survive (45 CFR 160.203)
- **GLBA**: Financial Privacy Rule preempts inconsistent state laws; Safeguards Rule does not preempt stricter state requirements
- **FCRA**: Broad preemption of state laws in areas where FCRA is comprehensive (Section 1681t)
- **COPPA**: Does not preempt state laws that are not inconsistent
- **State privacy laws**: Generally exempt HIPAA-covered data, GLBA-covered data, and FCRA-regulated activities from scope

## Proposed Federal Comprehensive Legislation

### American Data Privacy and Protection Act (ADPPA)
- H.R. 8152, 117th Congress (2022) — advanced through committee but not enacted
- Would have established federal consumer privacy rights: access, correction, deletion, portability, opt-out of targeted advertising
- Key unresolved issue: scope of federal preemption over state laws (especially California CCPA/CPRA)

### American Privacy Rights Act (APRA)
- Discussion draft, 118th Congress (2024)
- Bipartisan proposal with data minimisation requirements, private right of action, and FTC enforcement
- Preemption provisions remain the primary obstacle to enactment

## Integration Points

- **42-cfr-part-2**: Substance use disorder records under federal confidentiality protections
- **hipaa-compliance**: HIPAA Privacy, Security, and Breach Notification Rules
- **state-law-tracker**: Federal-state interaction and preemption analysis
- **vendor-privacy-due-diligence**: Business associate agreements (HIPAA) and service provider requirements (GLBA)
- **children-data-protection**: COPPA compliance for services directed at or used by children
