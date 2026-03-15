# Consent Form Audit Report Template

## Audit Information

| Field | Value |
|-------|-------|
| **Audit Date** | 2026-03-14 |
| **Controller** | CloudVault SaaS Inc. |
| **Controller Address** | 42 Innovation Drive, Dublin, D02 YX88, Ireland |
| **Auditor** | Marta Kowalski, Data Protection Officer |
| **Consent Form Version** | v3.2 (SHA-256: a1b2c3d4e5f6...) |
| **Environment** | Production (app.cloudvault-saas.eu) |
| **Scope** | Sign-up consent flow, cookie consent banner, preference center |

## Audit Checklist Results

| # | Item | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 1 | Consent separated from ToS | Art. 7(2) | PASS | Consent section has distinct heading and visual separation |
| 2 | No pre-ticked boxes | Art. 4(11), CJEU C-673/17 | PASS | All checkboxes default to unticked state confirmed |
| 3 | Granular per-purpose consent | Recital 32 | PASS | Three separate purposes each with own checkbox |
| 4 | Controller identity stated | Art. 13(1)(a) | PASS | Full legal name, address, and DPO contact displayed |
| 5 | Purpose clearly described | Art. 13(1)(c) | PASS | Plain language descriptions at grade 7 reading level |
| 6 | Data types specified | Art. 13(1)(d) | PASS | Each purpose lists specific data categories collected |
| 7 | Third-party recipients named | Art. 13(1)(e) | FAIL | Analytics purpose lists "third-party partners" without naming Datalytics Partners Ltd. |
| 8 | Withdrawal mechanism explained | Art. 7(3) | PASS | "You can change these choices anytime in Account Settings" displayed |
| 9 | No detriment for refusal | Art. 7(4) | PASS | Account creation proceeds regardless of consent choices |
| 10 | Withdrawal as easy as giving | Art. 7(3) | FAIL | Giving consent: 1 click; withdrawing: 3 clicks (Settings > Privacy > Manage) |
| 11 | Age verification present | Art. 8 | N/A | Service not directed at children; B2B product |
| 12 | Plain language | Art. 7(2) | PASS | Flesch-Kincaid score: 7.2 |
| 13 | Consent records stored | Art. 7(1) | PASS | All required fields present in consent_receipts database table |
| 14 | Re-consent for changes | Art. 13(3) | PASS | Version control system triggers re-consent on text changes |
| 15 | No cookie walls | EDPB 05/2020 | PASS | Full site accessible without cookie consent |

## Summary

| Metric | Value |
|--------|-------|
| **Total Items** | 15 |
| **Passed** | 12 |
| **Failed** | 2 |
| **Not Applicable** | 1 |
| **Compliance Rate** | 85.7% |

## Findings and Remediation

### Finding 1: Third-Party Recipients Not Named (SEVERITY: HIGH)

**Checklist Item:** #7 — Third-party recipients named
**GDPR Reference:** Article 13(1)(e)
**Description:** The analytics consent purpose refers to "third-party partners" generically. Per Article 13(1)(e) and EDPB Guidelines 05/2020 paragraph 34, specific third parties must be identified by name.
**Remediation:** Update consent text for Purpose 3 to read: "Allow CloudVault SaaS Inc. to share anonymized usage statistics with Datalytics Partners Ltd. (registered in Amsterdam, Netherlands) for industry benchmarking."
**Owner:** Elena Rodriguez, Product Legal Counsel
**Deadline:** 2026-04-01
**Priority:** High — directly affects consent validity

### Finding 2: Withdrawal Not Equal Ease (SEVERITY: MEDIUM)

**Checklist Item:** #10 — Withdrawal as easy as giving
**GDPR Reference:** Article 7(3)
**Description:** Consent is given with 1 click during sign-up. Withdrawal requires navigating to Settings > Privacy > Manage Consent (3 clicks). Article 7(3) requires withdrawal to be "as easy" as giving consent.
**Remediation:** Add a persistent "Manage Privacy Choices" link in the main navigation sidebar, reducing withdrawal to 2 clicks. Additionally, add a direct withdrawal toggle in the user dashboard widget.
**Owner:** James Park, Lead Frontend Engineer
**Deadline:** 2026-04-15
**Priority:** Medium — non-compliance risk under Art. 7(3)

## Sign-Off

| Role | Name | Date | Signature |
|------|------|------|-----------|
| DPO | Marta Kowalski | 2026-03-14 | [Signed] |
| Legal Counsel | Elena Rodriguez | 2026-03-14 | [Pending remediation review] |
| Engineering Lead | James Park | 2026-03-14 | [Pending implementation] |

## Next Audit

**Scheduled Date:** 2026-06-14 (Quarterly cadence)
**Trigger Conditions:** Any consent UI deployment, new processing purpose addition, or regulatory guidance update.
