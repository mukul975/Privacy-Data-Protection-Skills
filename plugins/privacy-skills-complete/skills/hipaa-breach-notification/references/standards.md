# Standards and Regulatory References — HIPAA Breach Notification

## Primary Legislation

### HITECH Act — Subtitle D (§§13400-13424)
- Section 13402: Notification requirements for breaches of unsecured PHI.
- Section 13401: Definition of "unsecured PHI" — PHI not rendered unusable through encryption or destruction per HHS guidance.
- Section 13407: Temporary breach notification requirement for non-HIPAA entities (vendors of personal health records).

### HIPAA Breach Notification Rule — 45 CFR Part 164, Subpart D
- **§164.400**: Applicability — applies to covered entities and business associates.
- **§164.402**: Definitions — breach, discovery, unsecured PHI, breach exceptions.
- **§164.404**: Individual notification requirements, timeline, content, and substitute notice.
- **§164.406**: Media notification for breaches of 500+ in a state/jurisdiction.
- **§164.408**: HHS/OCR notification requirements (500+ immediate, under 500 annual).
- **§164.410**: Business associate notification obligations to covered entities.
- **§164.412**: State AG notification requirements.
- **§164.414**: Administrative requirements and burden of proof.

### HHS Guidance on Securing PHI (April 2009, updated 2013)
- Specifies that PHI is "secured" (and thus not subject to breach notification) if encrypted per NIST SP 800-111 or destroyed per NIST SP 800-88.
- Encryption must use a process consistent with NIST requirements: valid encryption processes for data at rest (AES-128 or higher) and data in transit (TLS 1.2+).

## Regulatory Guidance

### HHS/OCR Breach Notification Guidance (Updated 2023)
- Provides the four-factor risk assessment methodology.
- Clarifies the "discovery" standard: a breach is "discovered" as of the first day it is known (or should have been known through reasonable diligence).
- The 60-day clock runs from discovery, not from completion of investigation.
- Business associate discovery also triggers the covered entity's obligations.

### HHS/OCR FAQ on Breach Notification Rule
- Substitute notice by web posting must be conspicuous on the entity's home page for at least 90 days.
- The toll-free number for substitute notice must remain active for at least 90 days.
- Annual breach log for under-500 breaches must be submitted to HHS by March 1 following the calendar year of discovery.

## Enforcement Precedents

- **Anthem Inc. (2018)**: $16 million settlement — breach affecting 78.8 million individuals. Largest HIPAA settlement. PHI included names, SSN, dates of birth, addresses, email addresses, and employment information.
- **Premera Blue Cross (2020)**: $6.85 million settlement — breach affecting 10.4 million. Failure to implement adequate security measures; PHI exposed for nearly 9 months before detection.
- **Banner Health (2023)**: $1.25 million settlement — breach affecting 2.81 million. OCR cited inadequate risk analysis and insufficient monitoring.
- **Lafourche Medical Group (2023)**: $480,000 settlement — phishing attack affecting 34,862 individuals. Notable for smaller entity enforcement.
- **CHSPSC LLC (2020)**: $2.3 million — business associate breach affecting 6 million. Demonstrated that BA obligations are independently enforced.

## NIST Standards (Referenced by HHS)

- **NIST SP 800-111**: Guide to Storage Encryption Technologies for End User Devices. Referenced by HHS guidance for defining "secured" PHI encryption requirements.
- **NIST SP 800-88 Rev. 1**: Guidelines for Media Sanitization. Referenced by HHS guidance for defining "secured" PHI destruction requirements.
- **NIST SP 800-66 Rev. 2**: Implementing the HIPAA Security Rule: A Cybersecurity Resource Guide (2024). Provides implementation guidance for the Security Rule that supports breach prevention.
