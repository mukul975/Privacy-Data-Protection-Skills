---
name: state-law-tracker
description: >-
  Tracks and monitors US state privacy legislation across all 50 states, DC,
  and territories. Covers enacted comprehensive privacy laws (California CCPA/CPRA,
  Virginia VCDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, and subsequent
  enactments), pending bills, effective dates, and key requirement differences.
  Keywords: state privacy law, CCPA, CPRA, VCDPA, CPA, CTDPA, UCPA, multi-state.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "state-privacy, multi-state, ccpa, cpra, vcdpa, cpa, comprehensive-privacy"
---

# US State Privacy Law Tracker

## Overview

The United States does not have a single comprehensive federal privacy law. Instead, a patchwork of state-level comprehensive privacy statutes has emerged since the California Consumer Privacy Act (CCPA) was enacted in 2018. As of early 2026, twenty states have enacted comprehensive consumer privacy laws, with additional states introducing legislation in each legislative session. This skill tracks the status of enacted laws, key provisions, effective dates, and substantive differences that drive multi-state compliance obligations.

## Enacted Comprehensive State Privacy Laws

| State | Law | Enacted | Effective | Enforcer |
|-------|-----|---------|-----------|----------|
| California | CCPA/CPRA | 2018/2020 | 1 Jan 2020 / 1 Jan 2023 | CPPA + AG |
| Virginia | VCDPA | 2021 | 1 Jan 2023 | AG |
| Colorado | CPA | 2021 | 1 Jul 2023 | AG |
| Connecticut | CTDPA | 2022 | 1 Jul 2023 | AG |
| Utah | UCPA | 2022 | 31 Dec 2023 | AG |
| Iowa | ICDPA | 2023 | 1 Jan 2025 | AG |
| Indiana | INCDPA | 2023 | 1 Jan 2026 | AG |
| Tennessee | TIPA | 2023 | 1 Jul 2025 | AG |
| Montana | MCDPA | 2023 | 1 Oct 2024 | AG |
| Texas | TDPSA | 2023 | 1 Jul 2024 | AG |
| Oregon | OCPA | 2023 | 1 Jul 2024 | AG |
| Delaware | DPDPA | 2023 | 1 Jan 2025 | AG |
| New Hampshire | NHPA | 2024 | 1 Jan 2025 | AG |
| New Jersey | NJDPA | 2024 | 15 Jan 2025 | AG |
| Nebraska | NDPA | 2024 | 1 Jan 2025 | AG |
| Minnesota | MCDPA | 2024 | 31 Jul 2025 | AG |
| Maryland | MODPA | 2024 | 1 Oct 2025 | AG |
| Rhode Island | RIDPA | 2024 | 1 Jan 2026 | AG |
| Kentucky | KCDPA | 2024 | 1 Jan 2026 | AG |
| Vermont | VDPA | 2024 | 1 Jul 2025 | AG |

## Key Compliance Variables Across States

### Applicability Thresholds

States differ in what triggers applicability:

- **Revenue threshold**: California (USD 25 million gross revenue) is the only state with a revenue trigger
- **Consumer volume**: Most states use 100,000 consumers; Texas uses 50,000 (if revenue derived from data sales); Montana uses 50,000 (total population consideration)
- **Revenue from data sales**: Most states apply if 25% or more of revenue comes from selling personal data (for businesses processing 25,000+ consumers)

### Consumer Rights Comparison

| Right | CA | VA | CO | CT | TX | OR | NJ | MD |
|-------|----|----|----|----|----|----|----|----|
| Access | Y | Y | Y | Y | Y | Y | Y | Y |
| Delete | Y | Y | Y | Y | Y | Y | Y | Y |
| Correct | Y | Y | Y | Y | Y | Y | Y | Y |
| Portability | Y | Y | Y | Y | Y | Y | Y | Y |
| Opt-out of sale | Y | Y | Y | Y | Y | Y | Y | Y |
| Opt-out of targeted ads | Y | Y | Y | Y | Y | Y | Y | Y |
| Opt-out of profiling | N* | Y | Y | Y | Y | Y | Y | Y |
| Appeal right | N | Y | Y | Y | Y | Y | Y | Y |
| Private right of action | Y** | N | N | N | N | N | N | N |

*California CPRA provides limited automated decision-making rights via regulations
**California PRA limited to data breaches involving specified personal information

### Cure Period Variations

- **30-day cure**: Virginia, Utah, Iowa, Indiana, Tennessee, Kentucky
- **60-day cure**: Colorado (expires 1 Jan 2025), Connecticut (expires 31 Dec 2024)
- **No cure period**: California (CPPA discretion), Texas, Oregon, New Jersey, Maryland
- **AG discretion**: Several states allow AG to determine cure appropriateness

### Universal Opt-Out Mechanism

States increasingly recognise universal opt-out signals:
- **Required**: California (CPRA regulations), Colorado, Connecticut, Texas, Montana, Oregon, Delaware, New Hampshire, New Jersey, Minnesota, Maryland, Vermont
- **Not required**: Virginia, Utah, Iowa, Indiana, Tennessee, Kentucky

## Monitoring Methodology

This tracker is updated by reviewing:
1. National Conference of State Legislatures (NCSL) privacy legislation database
2. International Association of Privacy Professionals (IAPP) state law comparison tool
3. Individual state legislature bill tracking systems
4. Attorney General enforcement announcements

## Integration Points

- **state-law-applicability**: Uses tracker data to determine which state laws apply to a specific organisation
- **multi-state-compliance**: Operationalises tracker data into a unified compliance programme
- **universal-opt-out**: Implements technical mechanisms required by states mandating GPC/universal opt-out
- **ccpa-consumer-requests**: California-specific consumer request handling
- **vcdpa-compliance**: Virginia-specific compliance operations
- **texas-tdpsa-compliance**: Texas-specific compliance operations
