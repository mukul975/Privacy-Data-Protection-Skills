# GPC Implementation Compliance Checklist

## Organization Information

| Field | Value |
|-------|-------|
| **Organization** | CloudVault SaaS Inc. |
| **States Served** | CA, CO, CT, MT, TX, OR, NY, FL, WA, IL |
| **Assessment Date** | 2026-03-14 |
| **Assessor** | Marta Kowalski, Data Protection Officer |
| **GPC Implementation Version** | 2.1 |

## Client-Side Detection Checklist

| # | Requirement | Status | Evidence |
|---|------------|--------|----------|
| 1 | JavaScript checks navigator.globalPrivacyControl before loading tracking scripts | PASS | Privacy init script loads as first script in document head |
| 2 | Third-party tracking scripts blocked when GPC = true | PASS | Network trace shows zero third-party requests when GPC enabled |
| 3 | Cross-site tracking pixels suppressed when GPC = true | PASS | No img/pixel requests to external domains observed |
| 4 | First-party analytics continue functioning (not sale/sharing) | PASS | Internal analytics events still fire for product improvement |
| 5 | Cookie consent banner reflects GPC preference | PASS | Sale/sharing toggles pre-selected to "off" with GPC notice displayed |
| 6 | GPC detection logged to consent system | PASS | gpc_signal_detected events visible in consent audit log |

## Server-Side Processing Checklist

| # | Requirement | Status | Evidence |
|---|------------|--------|----------|
| 7 | Middleware inspects Sec-GPC header on all requests | PASS | Privacy middleware registered as first middleware in chain |
| 8 | Sec-GPC: 1 sets session-level opt-out flag | PASS | Session store shows gpc_opt_out = true for GPC requests |
| 9 | Authenticated users: consent record updated for sale/sharing purposes | PASS | Consent database shows GPC-triggered withdrawal records |
| 10 | Response includes Sec-GPC echo header | PASS | Response headers include Sec-GPC: 1 when request had GPC |
| 11 | GPC events logged with timestamp, user agent, user ID | PASS | Audit log contains all required fields |
| 12 | Downstream systems notified of GPC-triggered opt-outs | PASS | Propagation log shows notifications to Datalytics Partners Ltd. pipeline |

## Conflict Resolution Checklist

| # | Requirement | Status | Evidence |
|---|------------|--------|----------|
| 13 | GPC overrides manual opt-in per AG Reg 11 CCR 7025(c) | PASS | User with prior opt-in has consent withdrawn when GPC detected |
| 14 | User notified of conflict between GPC and prior opt-in | PASS | In-app notification displayed explaining GPC override |
| 15 | User given option to re-confirm financial incentive participation | PASS | Notification includes link to re-confirm in Settings > Privacy |

## State-Specific Compliance

| State | Law | Effective Date | GPC Required | Compliant |
|-------|-----|---------------|-------------|-----------|
| California | CPRA Section 1798.135(e) | 2023-01-01 | Yes | Yes |
| Colorado | CPA Section 6-1-1306(1)(a)(IV)(A) | 2024-07-01 | Yes | Yes |
| Connecticut | CTDPA Section 42-520(b)(5) | 2025-01-01 | Yes | Yes |
| Montana | MCDPA Section 30-14-2807 | 2024-10-01 | Yes | Yes |
| Texas | TDPSA Section 541.055 | 2025-01-01 | Yes | Yes |
| Oregon | OCPA Section 646A.578 | 2024-07-01 | Yes | Yes |

## Verification Test Results

| Test | Browser/Tool | Result |
|------|-------------|--------|
| GPC detection (client-side) | Brave Browser v1.62 | Sec-GPC: 1 sent, tracking blocked |
| GPC detection (client-side) | DuckDuckGo Browser v0.78 | Sec-GPC: 1 sent, tracking blocked |
| GPC detection (client-side) | Firefox + OptMeowt v3.2 | Sec-GPC: 1 sent, tracking blocked |
| GPC detection (server-side) | curl with Sec-GPC: 1 header | Opt-out applied, consent updated |
| Control (no GPC) | Chrome v122 (default settings) | No GPC header, standard consent flow |
| Conflict resolution | Brave + user with prior opt-in | GPC override applied, notification sent |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| DPO | Marta Kowalski | 2026-03-14 |
| Engineering Lead | James Park | 2026-03-14 |
| Legal Counsel | Elena Rodriguez | 2026-03-14 |
