# GPC Cookie Integration Standards and References

## GPC Specification
- Published at globalprivacycontrol.org
- HTTP header: Sec-GPC: 1
- JavaScript API: navigator.globalPrivacyControl
- Developed by W3C Privacy Community Group

## US State Law Requirements

### California — CCPA/CPRA
- Cal. Civ. Code §1798.135(e): Business must treat GPC as valid opt-out of sale/sharing
- 11 CCR §7025(b)-(c): GPC implementation requirements; no degradation of service
- Effective: January 1, 2023

### Colorado — CPA
- C.R.S. §6-1-1313(1)(a): Must honor universal opt-out mechanism
- 4 CCR 904-3 Rule 5.11: Universal opt-out mechanism requirements
- Effective: July 1, 2024 (UOM: January 1, 2025)

### Connecticut — CTDPA
- P.A. 22-15, §6(a)(6): Must honor opt-out preference signals
- Effective: July 1, 2023 (UOM: January 1, 2025)

## Enforcement Precedent

### Sephora — California AG (August 2022)
- First CCPA enforcement action for failure to honor GPC signal
- $1.2 million settlement
- Required: honor GPC as valid opt-out, update privacy policy, conform selling practices

## Browser Support
- Firefox v120+: Built-in GPC support
- Brave: Built-in, enabled by default
- DuckDuckGo Browser: Built-in, enabled by default
- Chrome/Safari: Via extensions (DuckDuckGo, Privacy Badger, OptMeowt)

## GPC vs DNT
- GPC has legal recognition (CCPA, CPA, CTDPA)
- DNT has no legal enforcement mechanism
- GPC scope: opt-out of sale, sharing, targeted advertising
- DNT scope: general tracking preference (largely ignored)
