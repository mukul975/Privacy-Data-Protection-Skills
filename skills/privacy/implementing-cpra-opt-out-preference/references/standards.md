# Standards and Regulatory References

## Primary Legislation

### California Privacy Rights Act (CPRA) / CCPA as Amended
- **Section 1798.135** — Methods of limiting sale, sharing, and use of personal information
- **Section 1798.135(b)(1)** — Requirement to treat opt-out preference signals as valid opt-out requests
- **Section 1798.135(e)** — Absence of signal does not constitute consent
- **Section 1798.120** — Right to opt-out of sale/sharing (the underlying right)
- **Section 1798.185(a)(19)** — Rulemaking authority for opt-out preference signals

### CCPA Regulations (11 CCR Division 6)
- **Section 7025** — Opt-out preference signals: business obligations, browser/device scope, conflict resolution, verification limitations
- **Section 7026** — Requests to opt-out of sale/sharing: processing requirements

### Colorado Privacy Act (CPA) — C.R.S. Section 6-1-1306
- **Section 6-1-1306(1)(a)(I)(C)** — Universal opt-out mechanism: Colorado also requires businesses to honor opt-out preference signals (effective 01 July 2024)
- **Colorado Attorney General Rules (4 CCR 904-3, Rule 5.11)** — Technical specifications for universal opt-out mechanisms

### Connecticut Data Privacy Act (CTDPA) — Public Act No. 22-15
- **Section 6(a)(6)** — Opt-out preference signals: Connecticut requires honoring opt-out signals (effective 01 January 2025)

## Technical Specifications

### Global Privacy Control (GPC)
- **GPC Specification**: Defines the `Sec-GPC` HTTP header and `navigator.globalPrivacyControl` JavaScript API for communicating user privacy preferences.
- **Supported browsers**: Firefox (built-in since v120), Brave (built-in), DuckDuckGo (built-in), Chrome/Edge/Safari (via extensions).

## Regulatory Guidance

### California Privacy Protection Agency (CPPA)
- **CPPA Enforcement Advisory 2024-01**: Guidance on opt-out preference signal compliance requirements, including technical implementation expectations.

### California Attorney General
- **Sephora Enforcement Action (2022)**: Settlement requiring honoring of GPC signals — first major enforcement action regarding opt-out preference signals under CCPA.
