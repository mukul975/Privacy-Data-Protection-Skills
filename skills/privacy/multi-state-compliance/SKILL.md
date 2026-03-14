---
name: multi-state-compliance
description: >-
  Multi-state harmonized privacy compliance program architecture. Common
  requirements matrix across all US state privacy laws, state-specific
  deltas, unified privacy program design, consumer rights harmonization,
  and operational efficiency for organizations subject to multiple states.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "multi-state, harmonized-compliance, privacy-program, state-matrix, unified-privacy"
---

# Multi-State Harmonized Compliance Program

## Overview

As of 2026, nineteen US states have enacted comprehensive consumer privacy laws. Organizations operating across multiple states face a complex patchwork of requirements with overlapping but not identical provisions. A harmonized multi-state compliance program identifies common requirements, maps state-specific differences, and implements a unified architecture that satisfies the most restrictive standard while maintaining state-specific handling where required.

## Common Requirements Matrix

### Consumer Rights (Available in All Comprehensive State Laws)

| Right | CA | VA | CO | CT | TX | OR | MT | KY | Harmonized Standard |
|-------|----|----|----|----|----|----|----|----|---------------------|
| Access/Know | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Provide all categories + specific pieces |
| Correct | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Correct upon verified request |
| Delete | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Cascading deletion to SPs/processors |
| Portability | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Machine-readable format (JSON) |
| Opt-out: sale | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | "Do Not Sell" link + GPC |
| Opt-out: targeted ads | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Privacy choices page |
| Opt-out: profiling | N/A | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Profiling opt-out mechanism |
| Limit sensitive PI | Yes | N/A | N/A | N/A | N/A | N/A | N/A | N/A | California-specific mechanism |
| Third-party list | N/A | N/A | N/A | N/A | N/A | Yes | N/A | N/A | Oregon-specific disclosure |

### Response Timelines

| State | Initial Response | Extension | Max Total | Appeal Response |
|-------|-----------------|-----------|-----------|-----------------|
| California | 45 days | +45 days | 90 days | N/A (no appeal right) |
| Virginia | 45 days | +45 days | 90 days | 60 days |
| Colorado | 45 days | +45 days | 90 days | 45 days |
| Connecticut | 45 days | +45 days | 90 days | 60 days |
| Texas | 45 days | +45 days | 90 days | 60 days |
| Oregon | 45 days | +45 days | 90 days | 45 days |
| Montana | 45 days | +15 days | **60 days** | 60 days |
| Kentucky | 45 days | +45 days | 90 days | 60 days |
| **Harmonized** | **45 days** | **+15 days** | **60 days** | **45 days** |

**Harmonized standard:** Comply with Montana's shorter timeline (60 days max) to satisfy all states simultaneously.

### Sensitive Data

| State | Approach | Unique Categories |
|-------|----------|-------------------|
| California | Post-collection limit right | Government IDs, account credentials |
| Virginia | Opt-in consent | Standard set |
| Colorado | Opt-in consent | Standard set |
| Connecticut | Opt-in consent (no dark patterns) | Standard set |
| Texas | Opt-in consent | Standard set |
| Oregon | Opt-in consent | Transgender/nonbinary status |
| Montana | Opt-in consent | Standard set |
| Kentucky | Opt-in consent | Standard set |
| **Harmonized** | **Opt-in consent + limit right** | **Include all unique categories** |

**Harmonized standard:** Implement opt-in consent (most restrictive) for all sensitive data categories across all states, plus the California-specific limit mechanism.

### Universal Opt-Out Mechanism

| State | Required | Effective Date |
|-------|----------|---------------|
| California | Yes | January 1, 2023 |
| Colorado | Yes | July 1, 2024 |
| Connecticut | Yes | January 1, 2025 |
| Montana | Yes | October 1, 2025 |
| Oregon | Not required | N/A |
| Virginia | Not required | N/A |
| Texas | Not required | N/A |
| Kentucky | Not required | N/A |
| **Harmonized** | **Yes (implement for all)** | **Now** |

## State-Specific Deltas

### California Only
- "Do Not Sell or Share My Personal Information" link (§1798.135(a)(1))
- "Limit the Use of My Sensitive Personal Information" link (§1798.135(a)(2))
- Financial incentive program disclosures (§1798.125(b))
- Annual metrics reporting for 10M+ consumer businesses (CPPA Regs §7101)
- Private right of action for data breaches (§1798.150)
- CPPA as enforcement agency (not just AG)

### Connecticut Only
- Explicit dark pattern prohibition in consent (§42-515(8))
- Bona fide loyalty program exemption (§42-517(c))

### Texas Only
- No revenue/consumer threshold (applies to all non-SBA small businesses)
- Data broker registration with Secretary of State (§541.202)
- CUBI biometric identifier provisions (§503.001)

### Oregon Only
- Specific third-party disclosure right (§646A.578(1)(f))
- Enhanced de-identified data requirements (§646A.586)
- Employee data partial exemption (§646A.572(4))
- Nonprofit applicability
- Transgender/nonbinary status as sensitive data
- 14-day cure period (shortest)

### Montana Only
- 50,000 consumer threshold (lowest)
- 15-day extension only (60 days max)
- Air carrier exemption

## Unified Privacy Program Architecture

### Layer 1: Foundation (Common Requirements)

All state laws share these requirements:
1. **Privacy notice**: Categories, purposes, rights, third parties, contact
2. **Data minimization**: Adequate, relevant, reasonably necessary
3. **Data security**: Appropriate technical and organizational measures
4. **Consumer rights**: Access, correct, delete, portability, opt-out
5. **Processor contracts**: Written agreements with specified terms
6. **Data protection assessments**: For targeted advertising, sale, profiling, sensitive data

### Layer 2: Enhanced Standards (Most Restrictive)

Apply the most restrictive standard across all applicable states:
- **Sensitive data**: Opt-in consent before processing (Virginia model) + California limit right
- **Response timeline**: 45 days + 15 days max extension (Montana standard)
- **Universal opt-out**: Implement for all consumers (California/Colorado/Connecticut standard)
- **Dark pattern prohibition**: Apply Connecticut's explicit standard to all consent interfaces
- **De-identified data**: Apply Oregon's enhanced standards

### Layer 3: State-Specific Modules

Implement state-specific requirements as modular additions:
- California: Limit link, metrics reporting, financial incentive disclosures
- Texas: SBA assessment, data broker registration check
- Oregon: Third-party specific list, employee data partial exemption, nonprofit assessment
- Connecticut: Loyalty program exemption assessment

### Layer 4: Monitoring and Adaptation

- Track new state privacy laws (legislatures active January-June annually)
- Monitor AG enforcement actions for compliance interpretation
- Update common requirements matrix as new laws take effect
- Maintain state-specific delta documentation

## Implementation for Liberty Commerce Inc.

### Unified Consumer Rights Portal

Liberty Commerce Inc. operates a single privacy portal at privacy.libertycommerce.com that:
- Detects consumer location based on account address or self-selection
- Presents all applicable rights for the consumer's state
- Applies the most restrictive standard for overlapping requirements
- Routes state-specific requests to appropriate workflows
- Tracks all requests against the shortest applicable deadline

### Unified Privacy Notice

A single California Privacy Notice (most comprehensive) serves as the base, with state-specific supplements:
- California section: CCPA/CPRA-specific disclosures, limit link, financial incentives
- Multi-state section: Consumer rights available in all states
- State-specific supplements: Oregon third-party list right, Texas data broker status

### Unified Opt-Out Implementation

A single "Your Privacy Choices" mechanism that:
- Honors GPC signals for all states (California, Colorado, Connecticut, Montana)
- Provides opt-out of sale and targeted advertising (all states)
- Provides opt-out of profiling (all states with profiling opt-out)
- Provides California-specific limit of sensitive PI
- Maintains state-specific records for compliance documentation

## Key Regulatory References

- IAPP State Privacy Law Comparison Chart (updated quarterly)
- NIST Privacy Framework v1.0 (baseline program architecture)
- FTC Dark Patterns Report (September 2022) — applicable to Connecticut CTDPA
- Global Privacy Control Specification v1.0 — universal opt-out implementation
