# Interoperability Compliance Assessment — Asclepius Health Network

**Assessment Date**: 2026-02-01
**Prepared by**: Dr. James Park, CISO and Marcus Chen, Privacy Analyst
**Scope**: Information blocking, Patient Access API, TEFCA readiness

---

## Organization Profile

| Attribute | Value |
|-----------|-------|
| Organization | Asclepius Health Network |
| Entity Type | Healthcare Provider (hospital system + ambulatory clinics) |
| EHR System | Epic (certified health IT under ONC program) |
| HIE Participation | Statewide HIE (CommonWell + Carequality) |
| TEFCA Status | QHIN evaluation in progress |

## Information Blocking Assessment

### EHI Practices Reviewed

| Practice | Interferes with EHI Access? | Exception Claimed | Documented? | Status |
|----------|----------------------------|-------------------|-------------|--------|
| 42 CFR Part 2 consent gating | Yes | Privacy (§171.202) | Yes | Compliant |
| Psychotherapy notes exclusion from API | Yes | Privacy (§171.202) | Yes | Compliant |
| 48-hour delay for sensitive lab results | Yes | Preventing Harm (§171.201) | Yes | Compliant |
| EHR downtime blocks (monthly maintenance) | Yes | Health IT Performance (§171.205) | Yes | Compliant |
| Denying API access to unverified apps | Yes | Security (§171.203) | Partial | Needs improvement |

### Finding: Incomplete Security Exception Documentation

- **Severity**: High
- **Details**: The practice of denying API access to apps that fail security assessment has a documented policy but lacks the required factual basis showing how each denial is tailored to specific security risks per §171.203.
- **Remediation**: Document specific security risk evaluation criteria and maintain per-app denial records with factual basis.
- **Deadline**: 2026-03-15

## Patient Access API Assessment

### Implementation Status

| Element | Status | Notes |
|---------|--------|-------|
| FHIR R4 endpoint | Implemented | Epic FHIR R4 API (api.fhir.asclepius.health) |
| USCDI data classes | Implemented | USCDI v3 compliant per HTI-1 certification |
| OAuth 2.0 authorization | Implemented | Epic OAuth 2.0 with PKCE |
| SMART on FHIR | Implemented | SMART App Launch v2.0 |
| Patient identity verification | Implemented | MyChart portal with MFA (NIST IAL2/AAL2) |
| Third-party app disclosure | Implemented | In-app notice before third-party authorization |
| Audit logging | Implemented | All API transactions logged in Splunk |
| TLS encryption | Implemented | TLS 1.3 enforced for all API connections |

### Finding: Access Token Lifetime

- **Severity**: Medium
- **Details**: Current access token lifetime is 120 minutes; recommended maximum is 60 minutes.
- **Remediation**: Reduce to 60 minutes with refresh token support.
- **Deadline**: 2026-03-01

## TEFCA Readiness Assessment

| Requirement | Status | Notes |
|-------------|--------|-------|
| QHIN connection | In Progress | Evaluating two QHINs; target connection Q2 2026 |
| Treatment exchange purpose | Ready | Supported via existing HIE connections |
| Payment exchange purpose | Ready | Supported via existing payer integrations |
| Healthcare Operations | Ready | Quality reporting infrastructure in place |
| Public Health | Ready | Electronic lab reporting and immunization registry active |
| Individual Access | Ready | Patient Access API operational |
| Benefits Determination | In Progress | Requires payer API integration |
| Consent management | Implemented | Supports opt-in/opt-out; 42 CFR Part 2 consent tracking |
| BAA with QHIN | Pending | Draft BAA under legal review |

### Finding: BAA Not Yet Executed with QHIN

- **Severity**: High
- **Details**: QHIN BAA is in draft review. No PHI exchange via TEFCA may occur until BAA is executed per §164.502(e).
- **Remediation**: Finalize BAA review and execute before QHIN go-live.
- **Deadline**: Before QHIN activation (target Q2 2026)

## Summary

| Assessment Area | Status | Critical | High | Medium |
|----------------|--------|----------|------|--------|
| Information Blocking | Partially Compliant | 0 | 1 | 0 |
| Patient Access API | Partially Compliant | 0 | 0 | 1 |
| TEFCA Readiness | In Progress | 0 | 1 | 0 |
| **Overall** | **Partially Compliant** | **0** | **2** | **1** |

**Prepared by**: Dr. James Park, CISO
**Reviewed by**: Sarah Mitchell, CPO
