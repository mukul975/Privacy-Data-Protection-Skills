# Regulatory Standards — Building Consent Preference Center

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 7(1)**: The controller shall be able to demonstrate that the data subject has consented to processing. This requires a robust audit trail in the preference center.
- **Article 7(3)**: The data subject shall have the right to withdraw consent at any time. It shall be as easy to withdraw as to give consent. This is the foundational requirement for preference center design.
- **Article 12(1)**: The controller shall take appropriate measures to provide information in a concise, transparent, intelligible, and easily accessible form, using clear and plain language. This governs the UX of the preference center.
- **Article 13**: Information to be provided where personal data are collected from the data subject. The preference center must surface this information for each purpose.
- **Article 25**: Data protection by design and by default. The preference center architecture must default to minimal processing (no consent = no processing).

### IAB Transparency and Consent Framework v2.2

The IAB Europe TCF v2.2 (effective September 2023, mandatory compliance from March 2024) is the industry standard for advertising consent management:

- **TC String Specification**: Defines the binary encoding format for consent signals, including version, CMP ID, consent screen, purpose consents, vendor consents, publisher restrictions, and legitimate interest assertions.
- **CMP Requirements**: CMPs must be registered with IAB Europe, implement the CMP API (__tcfapi), and pass periodic compliance audits.
- **Global Vendor List (GVL)**: Published at vendorlist.consensu.org, containing all registered vendors with their declared purposes, legitimate interests, features, and data retention policies.
- **Publisher Restrictions**: Allow publishers to override the default legal basis declared by a vendor (e.g., requiring consent where a vendor declares legitimate interest).
- **Key Change from v2.0**: TCF v2.2 removed the "right to object" UI flow for legitimate interest purposes where a vendor previously claimed LI — now publishers must explicitly configure whether LI is permitted per vendor.

### Kantara Initiative Consent Receipt Specification v1.1

Defines a standard machine-readable format for consent receipts containing:
- Receipt header (jurisdiction, timestamp, receipt ID)
- Data controller information
- Purpose specification (purpose, data categories, retention)
- Consent type (explicit, implied)
- Personally identifiable information fields collected
- Third-party sharing details

## Supervisory Authority Guidance

### EDPB Guidelines 05/2020 on Consent

- **Paragraph 108-120**: Detailed guidance on withdrawal mechanisms. The preference center must enable withdrawal with equal ease, including technical implementation considerations.
- **Paragraph 89-107**: Guidance on demonstrating consent, including what constitutes adequate proof and how to maintain records.

### CNIL Deliberation No. 2020-091

French guidelines requiring that consent interfaces offer equal prominence to "accept" and "refuse" options, directly impacting preference center button design and layout.

### Irish Data Protection Commission Guidance on Consent (December 2020)

As the lead supervisory authority for many technology companies (including those based in Ireland), the DPC guidance emphasizes:
- Preference centers must be accessible without requiring login where technically feasible
- Consent history must be retrievable by the data subject upon request (supporting Article 15 access rights)
- Re-consent must be sought at reasonable intervals (annually recommended for standard processing)
