# Data Portability Response Letter Template

**CONFIDENTIAL**

---

**From:** Meridian Analytics Ltd
Data Protection Office
47 Canary Wharf Tower, London E14 5AB
dpo@meridiananalytics.co.uk

**Date:** 14 March 2026

**To:** David Okafor
8 Victoria Embankment
London EC4Y 0DZ

**Reference:** PORT-2026-0213

**Subject:** Response to Your Data Portability Request

---

Dear Mr Okafor,

Thank you for your data portability request received on 13 February 2026. We have processed your request in accordance with Article 20 of the UK General Data Protection Regulation (UK GDPR).

## 1. Scope of Portable Data

Under Article 20, the right to portability applies to personal data that you have provided to us, where processing is based on your consent or our contract with you, and is carried out by automated means. We have identified the following data categories as portable:

| Category | Source | Legal Basis | Included |
|----------|--------|-------------|----------|
| Account information | Provided by you | Art. 6(1)(b) — Contract | Yes |
| Contact details | Provided by you | Art. 6(1)(b) — Contract | Yes |
| Transaction history | Generated through your use of the service | Art. 6(1)(b) — Contract | Yes |
| Platform activity logs | Observed through your use of the service | Art. 6(1)(a) — Consent | Yes |
| Preferences and settings | Provided by you | Art. 6(1)(b) — Contract | Yes |

The following categories are **not included** in the portability export:

| Category | Reason for Exclusion |
|----------|---------------------|
| Analytics profiling segments | Inferred data — created by Meridian Analytics Ltd through algorithmic processing. Not data "provided by" the data subject per EDPB Guidelines WP242 rev.01, paragraph 2.2 |
| Credit risk assessment scores | Derived data — controller's analytical output, not subject to portability |
| Internal account notes | Created by Meridian Analytics Ltd staff, not by or through the data subject |

## 2. Data Format

Your data has been exported in **JSON format** (application/json), which is a structured, commonly used, and machine-readable format as required by Article 20(1). The export contains the following files:

| File | Description | Records |
|------|-------------|---------|
| manifest.json | Export metadata, file list, and checksums | 1 |
| account_data.json | Account details, identity, contact, preferences | 1 |
| transactions.json | Payment and subscription transaction history | 34 |
| activity_logs.json | Platform usage logs (dashboard views, reports, API calls) | 1,247 |

Total export size: 2.4 MB (compressed)

## 3. Delivery Method

Your data export is available for secure download:

- **Download link:** Sent to your registered email address (d.okafor@northgatefs.co.uk)
- **Link expiry:** 72 hours from issuance (expires 17 March 2026 at 14:00 UTC)
- **Encryption:** AES-256 encrypted ZIP archive
- **Decryption password:** Sent to your registered mobile number via SMS

If you require the data in a different format (CSV or XML), or if you would like us to transmit the data directly to another controller under Article 20(2), please contact us at the address above.

## 4. Important Notes

- This portability export does not result in the deletion of your data from our systems. If you wish to request erasure, please submit a separate request under Article 17.
- Your existing service and account remain active and unaffected by this export.
- The data provided is accurate as of the export date (14 March 2026). Any data changes after this date are not reflected in the export.

## 5. Further Enquiries

If you have questions about this response or wish to exercise any other data protection right, please contact our Data Protection Officer at dpo@meridiananalytics.co.uk.

Yours sincerely,

**Dr Sarah Chen**
Data Protection Officer
Meridian Analytics Ltd

---

**Enclosures:**
1. Secure download link (sent separately to registered email)
2. Decryption password (sent separately via SMS)
