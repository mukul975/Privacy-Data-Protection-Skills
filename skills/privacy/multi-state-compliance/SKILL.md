---
name: multi-state-compliance
description: >-
  Multi-state harmonized privacy compliance program. Common requirements
  matrix across all US state privacy laws, state-specific deltas, unified
  privacy program architecture, and implementation strategy for operating
  across California, Virginia, Colorado, Connecticut, Texas, Oregon,
  Montana, and Kentucky.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "multi-state, harmonized-compliance, common-requirements, state-deltas, unified-program"
---

# Multi-State Harmonized Compliance Program

## Overview

As of 2026, over 20 US states have enacted comprehensive consumer privacy legislation. Organizations operating nationwide face a complex patchwork of requirements with significant overlap but important state-specific variations. A harmonized multi-state compliance program identifies the common baseline, maps state-specific deltas, and implements a unified privacy architecture that satisfies all applicable laws.

This skill covers the eight major enacted and effective state privacy laws: CCPA/CPRA (California), VCDPA (Virginia), CPA (Colorado), CTDPA (Connecticut), TDPSA (Texas), OCPA (Oregon), MTDPA (Montana), and KPPA (Kentucky).

## Common Requirements Matrix

### Consumer Rights — Universal Baseline

All eight laws provide these core rights:

| Right | CA | VA | CO | CT | TX | OR | MT | KY |
|-------|----|----|----|----|----|----|----|----|
| Access/Know | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Correct | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Delete | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Portability | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Opt-out: targeted ads | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Opt-out: sale | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Opt-out: profiling | No* | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Limit sensitive PI | Yes | N/A | N/A | N/A | N/A | N/A | N/A | N/A |
| Third-party list | No | No | No | No | No | Yes | No | No |
| Appeal | No | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

*California provides opt-out of automated decision-making under pending CPPA regulations.

### Controller Obligations — Universal Baseline

| Obligation | All States |
|-----------|-----------|
| Privacy notice/policy | Required |
| Data minimization | Required |
| Purpose limitation | Required |
| Data security | Required |
| Non-discrimination | Required |
| Response timeline | 45 days (all states) |

## State-Specific Deltas

### California (CCPA/CPRA) — Unique Requirements
- **Revenue threshold**: $25M alternative threshold (no other state has this)
- **Sensitive PI limit right**: Post-collection limit mechanism (other states require pre-collection consent)
- **CPPA enforcement**: Dedicated privacy agency (only state with one)
- **Private right of action**: For data breach claims (only state with any private right of action)
- **Annual metrics**: Required for businesses processing 10M+ consumers
- **Data processing agreements**: Explicit statutory requirement
- **No cure period**: Eliminated by CPRA

### Virginia (VCDPA) — Unique Requirements
- **50% revenue threshold**: Higher revenue percentage requirement than most states

### Colorado (CPA) — Unique Requirements
- **AG rulemaking**: Most detailed implementing regulations (4 CCR 904-3)
- **Universal opt-out**: First mandated (effective July 2024)
- **Profiling opt-out scope**: Broadest definition covering 7+ decision categories
- **$20,000 penalties**: Higher per-violation penalties under Consumer Protection Act

### Connecticut (CTDPA) — Unique Requirements
- **Dark pattern prohibition**: Explicit statutory definition and prohibition
- **Loyalty program exemption**: Bona fide loyalty programs exempt from sale opt-out
- **25% revenue threshold**: Lower than Virginia's 50%

### Texas (TDPSA) — Unique Requirements
- **No revenue/consumer threshold**: Applies to all non-SBA-small businesses
- **Data broker registration**: Secretary of State registration requirement
- **CUBI interaction**: Separate biometric data law (up to $25,000/violation)
- **Broadest applicability**: Largest state population, lowest effective threshold

### Oregon (OCPA) — Unique Requirements
- **Nonprofit coverage**: Applies to nonprofit organizations
- **Third-party list right**: Specific entity names, not just categories
- **De-identified data**: Most detailed compliance requirements
- **Employee data partial exemption**: Unique treatment of employee data
- **Transgender/nonbinary status**: Explicit sensitive data category
- **14-day cure period**: Shortest cure period among states

### Montana (MTDPA) — Unique Requirements
- **50,000 consumer threshold**: Lowest consumer count threshold
- **15-day extension only**: Shorter extension than most states' 45 days
- **Air carrier exemption**: Unique industry exemption

### Kentucky (KPPA) — Unique Requirements
- **January 2026 effective date**: Most recently effective among this group
- **50% revenue threshold**: Matches Virginia

## Unified Privacy Program Architecture

### Tier 1: Common Baseline (Apply Everywhere)

These requirements are common across all states and form the foundation:

1. **Privacy notice** with categories of PI, purposes, rights, third parties, contact info
2. **Consumer rights portal** supporting access, correct, delete, portability, opt-out
3. **45-day response SLA** with tracking and metrics
4. **Data minimization** and purpose limitation controls
5. **Reasonable data security** measures
6. **Non-discrimination** protections

### Tier 2: High-Water Mark (Apply to Satisfy Strictest Requirement)

Where state requirements differ, apply the strictest standard universally:

| Area | Strictest Standard | Source State |
|------|--------------------|-------------|
| Sensitive data consent | Opt-in consent before collection | VA, CO, CT, TX, OR, MT, KY |
| Dark pattern prohibition | Consent via dark patterns invalid | CT (explicit), all (implicit) |
| Response extension | 15-day extension only | MT (strictest) or accept state-by-state |
| Universal opt-out | Honor GPC signals | CA, CO, CT, MT |
| Profiling opt-out | Include 7+ decision categories | CO (broadest scope) |
| De-identified data | Full compliance program | OR (most detailed) |
| Privacy notice retention periods | Include per-category retention | CA (CPRA requirement) |

### Tier 3: State-Specific (Apply Only Where Required)

| Requirement | State(s) | Implementation |
|-------------|----------|---------------|
| "Do Not Sell or Share" link | CA | Homepage footer |
| "Limit Sensitive PI" link | CA | Adjacent to opt-out link |
| Specific third-party list | OR | Additional disclosure in Oregon responses |
| Data broker registration | TX | Secretary of State registration (if applicable) |
| Annual metrics disclosure | CA (10M+) | Privacy notice metrics section |
| Loyalty program exemption | CT | Program-specific terms |
| Nonprofit compliance | OR | Full program for Oregon nonprofit operations |

### Implementation Strategy for Liberty Commerce Inc.

**Approach: High-Water Mark with State-Specific Overlays**

Liberty Commerce Inc. implements a unified privacy program at the highest common standard, with state-specific modules activated based on the consumer's state of residence.

```
Consumer Request Received
  │
  ├─► Determine Consumer's State
  │
  ├─► Apply Tier 1 Common Baseline
  │     (Same for all states)
  │
  ├─► Apply Tier 2 High-Water Mark
  │     (Strictest standard, applied universally)
  │
  └─► Apply Tier 3 State-Specific Module
        ├─ California module: CPRA-specific disclosures, sensitive PI limit
        ├─ Oregon module: Third-party specific list
        ├─ Texas module: Data broker check
        └─ Connecticut module: Loyalty program exemption assessment
```

## Harmonized Privacy Notice Template

A multi-state privacy notice should include these sections to satisfy all eight laws:

1. **Categories of PI/personal data collected** (all states)
2. **Categories of sensitive PI/sensitive data collected** (all states)
3. **Purposes for each category** (all states)
4. **Retention period or criteria per category** (CA required; best practice all)
5. **Sources of PI** (CA required; best practice all)
6. **Categories of third parties receiving PI** (all states)
7. **Whether PI is sold or shared** (all states)
8. **Whether targeted advertising is conducted** (all non-CA states)
9. **Whether profiling is conducted** (all non-CA states)
10. **Consumer rights and how to exercise** (all states)
11. **Appeal process** (VA, CO, CT, TX, OR, MT, KY)
12. **Contact information** (all states)
13. **"Do Not Sell or Share" link** (CA)
14. **"Limit Sensitive PI" link** (CA)
15. **Universal opt-out disclosure** (CA, CO, CT, MT)
16. **Last updated date** (CA required; best practice all)
17. **Annual metrics** (CA, if 10M+ consumers)

## Key Regulatory References

- IAPP US State Comprehensive Privacy Law Comparison Chart (updated quarterly)
- CPPA Regulations 11 CCR §7001-7102
- Colorado AG Regulations 4 CCR 904-3
- Global Privacy Control Specification v1.0
