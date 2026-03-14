# Regulatory Standards — Universal Opt-Out Mechanism

## GPC Specification

### Global Privacy Control Specification v1.0

Published by the GPC project. Defines:
- `Sec-GPC` HTTP request header (value: `1` for opt-out)
- `navigator.globalPrivacyControl` JavaScript API (value: `true` for opt-out)
- Header is a structured header per RFC 8941
- Prefix `Sec-` makes it a fetch metadata header (set by browser, not JavaScript)

### Browser Support (as of 2025)
- **Brave**: Built-in GPC support (enabled by default for users who enable shields)
- **Firefox**: GPC support built-in (enabled in settings)
- **DuckDuckGo Browser**: Built-in GPC support
- **Safari**: No native support (available via extension)
- **Chrome**: No native support (available via extensions)

### Extension Support
- Privacy Badger (EFF)
- DuckDuckGo Privacy Essentials
- Disconnect
- OptMeowt

## State Regulatory Requirements

### California — CPPA Regulations §7025

Most detailed requirements:
- §7025(a): Controller must process opt-out preference signals
- §7025(b): Must not use two-step opt-out (no confirmation click)
- §7025(c): No identity verification required
- §7025(d): No pop-up or notification questioning signal
- §7025(e): Apply to browser/device if consumer not identifiable
- §7025(f): Signal takes precedence as most recent expression

### Colorado — 4 CCR 904-3, Rule 5

Most detailed technical standards:
- Rule 5.01: Technical specifications for mechanisms
- Rule 5.10: Controller recognition requirements
- Rule 5.11: Signal processing (no pop-ups, no verification)
- Rule 5.12: Authenticated vs. unauthenticated handling
- Rule 5.13: Conflict resolution (most recent preference)
- Rule 5.14: AG biennial review of recognized mechanisms

### Connecticut — Conn. Gen. Stat. §42-520(a)(6)
Effective January 1, 2025. Requires recognition of universal opt-out mechanisms.

### Montana — MCA §30-14-2808(3)
Effective October 1, 2025. Requires recognition of universal opt-out mechanisms.

## Enforcement Precedent

### In re Sephora Inc. (August 24, 2022)

California AG settlement for $1.2 million. Key findings relevant to GPC:
- Sephora failed to process GPC opt-out signals as valid opt-out requests
- GPC signals must be honored as a valid CCPA opt-out of sale
- Controllers cannot ignore or override GPC signals
- Sharing PI with analytics/advertising partners for services constitutes "sale"

This enforcement action established GPC as a legally enforceable opt-out mechanism.
