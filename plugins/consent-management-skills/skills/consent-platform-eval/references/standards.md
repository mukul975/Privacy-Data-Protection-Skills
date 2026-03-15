# Regulatory Standards — Evaluating Consent Management Platforms

## Primary Regulations

### IAB Transparency and Consent Framework v2.2

CMPs participating in the TCF must:
- Register with IAB Europe and receive a unique CMP ID
- Implement the CMP API (__tcfapi JavaScript function) per specification
- Generate valid TC Strings encoding user consent for purposes 1-11 and vendor-level consent
- Consume and display the Global Vendor List (GVL) to users
- Pass periodic compliance audits conducted by IAB Europe
- Implement publisher restrictions allowing publishers to override vendor-declared legal bases
- TCF v2.2 (mandatory from March 2024) removed the right-to-object UI for LI where publishers require consent-only

### GDPR — Regulation (EU) 2016/679

- **Article 7**: The CMP must enable consent collection that meets all conditions: freely given, specific, informed, unambiguous, clear affirmative action
- **Article 7(1)**: The CMP must maintain consent records sufficient to demonstrate consent
- **Article 7(3)**: The CMP must provide withdrawal mechanisms that are equally easy as consent giving
- **Article 28**: The CMP is a data processor. A Data Processing Agreement is required covering: processing scope, instructions, sub-processors, security measures, audit rights, data return/deletion

### CPRA — California Civil Code Section 1798.100 et seq.

- **Section 1798.135(e)**: The CMP must detect and honor GPC signals (Sec-GPC: 1 header and navigator.globalPrivacyControl API)
- **Section 1798.120**: The CMP must support "Do Not Sell or Share My Personal Information" opt-out functionality

### LGPD — Brazilian Lei 13.709/2018

- **Article 7**: Consent is one of ten lawful bases. CMPs must support consent collection meeting LGPD requirements.
- **Article 8**: Consent must be provided in writing or by other means that demonstrate the free will of the data subject.

## Supervisory Authority Decisions Relevant to CMP Selection

### Belgian DPA v. IAB Europe (February 2022, EUR 250,000)

The Belgian DPA found that IAB Europe acted as a controller (not merely a standards body) for TC String data. Key implications for CMP selection:
- The TC String itself constitutes personal data
- CMPs that generate TC Strings have controller/processor obligations
- Consent records beyond the TC String are necessary to demonstrate compliance
- This decision reinforced the need for detailed consent receipts, not just encoded strings

### CNIL Enforcement (Google, Meta, Microsoft, TikTok — 2022)

These fines established that CMPs must:
- Present "Refuse All" on the first layer with equal prominence
- Not set any non-essential cookies before user choice
- Support 6-month reconsent cycles
- Enable proper consent withdrawal

## Industry Standards

### ISO/IEC 27701:2019 — Privacy Information Management System

CMPs should demonstrate compliance with ISO 27701 for their own data processing, providing assurance that consent records are handled securely. This is a differentiating criterion for vendor selection.

### SOC 2 Type II

CMP vendors should hold SOC 2 Type II certification for their consent record storage and processing infrastructure, confirming security controls are in place and operating effectively.
