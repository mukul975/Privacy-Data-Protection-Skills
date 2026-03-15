# TCF v2.2 Implementation Checklist

## Organization: [Organization Name]
## CMP ID: [Assigned by IAB Europe]
## Implementation Date: [YYYY-MM-DD]

---

## 1. CMP Registration

| Item | Status | Notes |
|------|--------|-------|
| CMP registered with IAB Europe | [ ] Done | CMP ID: ___ |
| CMP validation tests passed | [ ] Done | |
| CMP Terms and Conditions accepted | [ ] Done | |
| CMP JavaScript URL configured | [ ] Done | URL: ___ |

## 2. Global Vendor List Integration

| Item | Status | Notes |
|------|--------|-------|
| GVL fetching implemented | [ ] Done | |
| GVL caching (max 24h staleness) | [ ] Done | |
| Vendor subset configured | [ ] Done | ___ vendors |
| Vendor details displayed in UI | [ ] Done | |
| Weekly GVL update automated | [ ] Done | |

## 3. Purpose Configuration

| Purpose | Legal Basis | Publisher Restriction | Notes |
|---------|------------|----------------------|-------|
| 1 — Store/access device | Consent | N/A (always consent) | |
| 2 — Select basic ads | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 3 — Create ad profiles | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 4 — Select personalized ads | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 5 — Create content profiles | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 6 — Select personalized content | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 7 — Measure ad performance | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 8 — Measure content performance | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 9 — Understand audiences | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 10 — Develop/improve services | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |
| 11 — Use limited data for content | [ ] Consent / [ ] LI | [ ] None / [ ] Require consent | |

## 4. Technical Implementation

| Item | Status | Notes |
|------|--------|-------|
| __tcfapi stub loads first | [ ] Done | Before any vendor scripts |
| __tcfapi full implementation | [ ] Done | |
| getTCData command works | [ ] Done | |
| ping command works | [ ] Done | |
| addEventListener command works | [ ] Done | |
| TC String correctly encoded | [ ] Done | Validated with IAB decoder |
| euconsent-v2 cookie set | [ ] Done | |
| TC String in ad bid requests | [ ] Done | OpenRTB consent field |

## 5. Validation

| Test | Pass | Fail | Notes |
|------|------|------|-------|
| TC String decodes correctly | [ ] | [ ] | |
| Purpose consent matches UI | [ ] | [ ] | |
| Vendor consent matches UI | [ ] | [ ] | |
| Publisher restrictions encoded | [ ] | [ ] | |
| GVL version current | [ ] | [ ] | |
| CMP ID in TC String | [ ] | [ ] | |

---

**Implemented by**: [Name] | **Reviewed by**: [DPO Name] | **Date**: [YYYY-MM-DD]
