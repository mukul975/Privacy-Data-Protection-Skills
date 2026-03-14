---
name: state-law-applicability
description: >-
  US state privacy law applicability assessment tool. Evaluates revenue
  thresholds, data volume thresholds, business exemptions (GLBA, HIPAA,
  nonprofits), employee data carve-outs, and SBA small business
  determinations across all enacted state privacy laws.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "applicability, thresholds, exemptions, glba, hipaa, small-business"
---

# State Privacy Law Applicability Assessment

## Overview

Determining which US state privacy laws apply to an organization requires evaluating multiple criteria: revenue thresholds, consumer/data volume thresholds, industry-specific exemptions, entity-type exemptions, and data-type exemptions. This skill provides a systematic assessment framework and Python automation tool for evaluating applicability across all major enacted state privacy laws.

## Assessment Framework

### Step 1: Geographic Nexus

For each state, determine if the organization has nexus through:
- **Conducting business** in the state (physical presence, employees, registered entity)
- **Targeting residents** of the state (marketing, advertising, or providing products/services specifically to state residents)
- **Producing products/services** consumed by state residents

Most state laws use "conducts business in [state] OR produces products or services targeted to [state] residents" as the nexus requirement.

### Step 2: Threshold Assessment

| State | Threshold 1 | Threshold 2 | Revenue Alternative |
|-------|------------|-------------|---------------------|
| California | 100,000 consumers/households | 50% revenue from sale/sharing | $25,000,000 annual gross revenue |
| Virginia | 100,000 consumers | 25,000 consumers + 50% revenue from sale | None |
| Colorado | 100,000 consumers | 25,000 consumers + revenue/discount from sale | None |
| Connecticut | 100,000 consumers (excl. payment) | 25,000 consumers + 25% revenue from sale | None |
| Texas | Non-SBA small business | N/A | None (no threshold) |
| Oregon | 100,000 consumers (excl. payment) | 25,000 consumers + 25% revenue from sale | None |
| Montana | 50,000 consumers (excl. payment) | 25,000 consumers + 25% revenue from sale | None |
| Kentucky | 100,000 consumers | 25,000 consumers + 50% revenue from sale | None |

### Step 3: Entity-Level Exemptions

| Exemption | CA | VA | CO | CT | TX | OR | MT | KY |
|-----------|----|----|----|----|----|----|----|----|
| Government | N/A (for-profit only) | Exempt | Exempt | Exempt | Exempt | Exempt | Exempt | Exempt |
| GLBA financial institutions | Data-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level |
| HIPAA covered entities | Data-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level | Entity-level |
| Nonprofits | Not exempt | Exempt | Exempt | Exempt | Exempt | **Not exempt** | Exempt | Exempt |
| Higher education | Not exempt | Exempt | Exempt | Exempt | Exempt | Not exempt | Exempt | Exempt |
| Air carriers | Not exempt | Not exempt | Not exempt | Not exempt | Not exempt | Not exempt | **Exempt** | Not exempt |

### Step 4: Data-Level Exemptions

Data that is already governed by certain federal laws may be exempt even if the organization itself is not:

| Federal Law | Full Name | Data Type |
|-------------|-----------|-----------|
| GLBA | Gramm-Leach-Bliley Act (15 U.S.C. §6801) | Financial data under GLBA privacy rules |
| HIPAA | Health Insurance Portability and Accountability Act (42 U.S.C. §1320d) | Protected health information (PHI) |
| FERPA | Family Educational Rights and Privacy Act (20 U.S.C. §1232g) | Education records |
| FCRA | Fair Credit Reporting Act (15 U.S.C. §1681) | Consumer credit reports |
| DPPA | Driver's Privacy Protection Act (18 U.S.C. §2721) | Motor vehicle records |
| COPPA | Children's Online Privacy Protection Act (15 U.S.C. §6501) | Children's data under COPPA |
| Farm Credit Act | Farm Credit Act of 1971 (12 U.S.C. §2001) | Farm credit data |

**California distinction:** CCPA/CPRA exempts the **data** governed by these federal laws, not the **entity**. A GLBA-covered bank is still subject to CCPA for personal data that falls outside GLBA's scope (e.g., marketing data not related to financial products).

### Step 5: Employee Data Assessment

| State | Employee Data Status |
|-------|---------------------|
| California | Fully covered (CPRA removed prior partial exemption) |
| Virginia | Exempt from consumer rights; controller duties apply |
| Colorado | Exempt from consumer rights; controller duties apply |
| Connecticut | Exempt from consumer rights; controller duties apply |
| Texas | Exempt from consumer rights; controller duties apply |
| Oregon | **Partial exemption**: Rights exempt; controller duties, DPIAs, sensitive consent apply |
| Montana | Exempt from consumer rights; controller duties apply |
| Kentucky | Exempt from consumer rights; controller duties apply |

### Step 6: SBA Small Business Determination (Texas TDPSA)

The TDPSA is the only state law that uses the SBA small business definition. Key steps:

1. Identify the organization's primary NAICS code
2. Look up the SBA size standard for that NAICS code in 13 CFR §121.201
3. Compare the organization's annual receipts or employee count to the threshold
4. If the organization qualifies as a small business:
   - Most TDPSA provisions are **exempt**
   - Prohibition on selling sensitive data without consent **still applies** (§541.107(b))

Common SBA thresholds for technology/retail companies:

| NAICS | Industry | Revenue Threshold |
|-------|----------|-------------------|
| 454110 | Electronic shopping | $40,000,000 |
| 519130 | Internet publishing and web search portals | $47,000,000 |
| 518210 | Data processing and hosting | $35,000,000 |
| 511210 | Software publishers | $47,000,000 |
| 541511 | Custom computer programming | $34,000,000 |

## Liberty Commerce Inc. Assessment Summary

| State | Consumers | Revenue from Sale | Applicable | Basis |
|-------|-----------|-------------------|------------|-------|
| California | 320,000 | 12% | **YES** | Revenue >$25M + 100K consumers |
| Virginia | 145,000 | 12% | **YES** | 100K+ consumers |
| Colorado | 98,000 | 12% | **YES** | 25K+ with revenue from sale |
| Connecticut | 87,000 | 12% | **Borderline** | Below 100K; below 25% revenue |
| Texas | 410,000 | 12% | **YES** | Non-SBA small business |
| Oregon | 72,000 | 12% | **NO** | Below both thresholds |
| Montana | 28,000 | 12% | **NO** | Below both thresholds |
| Kentucky | 68,000 | 12% | **NO** | Below both thresholds |

## Key Regulatory References

- SBA Size Standards: 13 CFR §121.201
- GLBA: 15 U.S.C. §6801-6809
- HIPAA: 42 U.S.C. §1320d et seq.; 45 CFR Parts 160, 164
- FERPA: 20 U.S.C. §1232g
- FCRA: 15 U.S.C. §1681 et seq.
- COPPA: 15 U.S.C. §6501-6506
- DPPA: 18 U.S.C. §2721-2725
