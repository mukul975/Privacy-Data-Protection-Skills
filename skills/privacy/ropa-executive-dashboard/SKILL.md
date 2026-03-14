---
name: ropa-executive-dashboard
description: >-
  Builds RoPA reporting and visualization dashboards including processing
  activity counts, risk heatmaps, compliance scores, trend analysis, and
  supervisory authority readiness indicators. Activate for RoPA dashboard,
  executive reporting, compliance metrics, risk heatmap, trend analysis,
  board reporting, KPI visualization.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, ropa, dashboard, reporting, visualization, heatmap, compliance-score, kpi"
---

# RoPA Executive Dashboard

## Overview

Privacy governance requires not just maintaining records but communicating their status to decision-makers. The DPO must report to senior management and the board under Art. 38(3), and processing records form the evidentiary backbone of this reporting. This skill provides the methodology, metrics, and visualisation approaches for building an executive RoPA dashboard that communicates compliance posture, risk exposure, and supervisory authority readiness in business-relevant terms.

## Dashboard Architecture

### Audience-Specific Views

| Audience | Information Need | Dashboard View |
|----------|-----------------|----------------|
| Board / Audit Committee | High-level compliance posture, trend direction, material risks | Executive summary (1 page) |
| DPO / Privacy Team | Operational metrics, gap details, remediation tracking | Operational dashboard (detailed) |
| Processing Owners | Their entries' status, pending reviews, action items | My processing activities |
| CISO | Security measures coverage, encryption status, access controls | Security overlay |
| Supervisory Authority | Readiness score, export-ready records, response time capability | SA readiness indicator |

## Key Performance Indicators (KPIs)

### Tier 1: Compliance Health (Board-Level)

| KPI | Calculation | Target | Red Threshold |
|-----|-------------|--------|---------------|
| **Overall Completeness Score** | Weighted average of all entry scores (Tier 1 + 2 + 3) | >= 95% | < 80% |
| **Mandatory Field Compliance** | % of entries with all 7 Art. 30(1) fields populated | 100% | < 90% |
| **Review Currency Rate** | % of entries reviewed within past 12 months | >= 95% | < 80% |
| **DPIA Linkage Rate** | % of high-risk entries with linked, approved DPIA | 100% | < 100% |
| **Critical Gap Count** | Number of entries with missing mandatory fields | 0 | > 0 |

### Tier 2: Operational Metrics (DPO-Level)

| KPI | Calculation | Target | Alert Threshold |
|-----|-------------|--------|-----------------|
| **Total Processing Activities** | Count of active RoPA entries | N/A (informational) | Significant change (>10% quarterly) |
| **New Activities This Quarter** | Count of entries created in current quarter | N/A | > 5 (may indicate rapid change requiring attention) |
| **Archived Activities This Quarter** | Count of entries archived | N/A | > 3 (verify archival was intentional) |
| **Average Days Since Last Review** | Mean days since last_reviewed_date across all entries | < 180 | > 270 |
| **Overdue Reviews** | Count of entries past next_review_date | 0 | > 0 |
| **DPA Coverage Rate** | % of processor recipients with documented DPA reference | 100% | < 95% |
| **International Transfer Documentation Rate** | % of transfers with documented safeguard mechanism | 100% | < 100% |
| **Special Category Processing Count** | Number of entries involving Art. 9 data | N/A | Any increase triggers review |
| **Remediation Closure Rate** | % of audit findings remediated within deadline | >= 90% | < 75% |

### Tier 3: Risk Indicators (Combined)

| Indicator | Signal |
|-----------|--------|
| **Entries without assigned owner** | Accountability gap — no one responsible for maintaining record |
| **Entries referencing terminated employees as owners** | Stale ownership — reassignment needed |
| **DPAs expiring within 90 days** | Contract risk — renewal needed before expiry |
| **Entries with vague purpose descriptions** | Regulatory risk — vulnerable to SA challenge |
| **Entries with vague retention periods** | Storage limitation risk — potential breach of Art. 5(1)(e) |
| **High-risk entries without DPIA** | Art. 35 non-compliance risk |
| **Transfers without TIA** | Schrems II compliance risk |

## Visualisation Components

### 1. Compliance Score Gauge

A single gauge showing the overall completeness score (0-100%), colour-coded:
- Green (95-100%): Supervisory authority ready
- Amber (80-94%): Acceptable with improvements needed
- Red (<80%): Requires urgent attention

### 2. Risk Heatmap

A matrix visualisation showing risk concentration across departments and processing types:

|  | Employee Data | Customer Data | Clinical Data | Financial Data | Marketing Data |
|--|-------------|--------------|--------------|---------------|---------------|
| **HR** | Medium | — | — | Medium | — |
| **Clinical Ops** | — | — | **High** | — | — |
| **Sales** | — | Low | — | Low | Low |
| **Finance** | Low | Low | — | Medium | — |
| **Marketing** | — | Low | — | — | Medium |
| **IT** | Low | Low | Low | Low | Low |

Risk levels based on:
- **High**: Special category data + large scale + international transfers
- **Medium**: Special category data OR large scale OR international transfers
- **Low**: Standard personal data, domestic processing, limited scale

### 3. Review Currency Timeline

A bar chart showing the distribution of entries by months since last review:

```
0-3 months:   ████████████████████  25 entries (53%)
3-6 months:   ████████████          15 entries (32%)
6-9 months:   ████                   5 entries (11%)
9-12 months:  ██                     2 entries (4%)
>12 months:   ░                      0 entries (0%)  ← TARGET
```

### 4. Processing Activity Trend

A line chart showing processing activity count over time:

```
        Q1 2025    Q2 2025    Q3 2025    Q4 2025    Q1 2026
Active:    42         44         45         47         49
New:        3          2          3          4          3
Archived:   1          0          2          2          1
```

### 5. Department Completeness Comparison

A horizontal bar chart showing per-department average completeness scores:

```
Clinical Ops:  ████████████████████████████░  96%
Finance:       ████████████████████████████   94%
HR:            ██████████████████████████░░   91%
IT:            ████████████████████████░░░░   88%
Sales:         ████████████████████████░░░░   87%
Marketing:     ██████████████████████░░░░░░   82%
Facilities:    ████████████████████░░░░░░░░   78%
```

### 6. Transfer Map

A geographic visualisation showing international data transfer destinations with transfer mechanism indicators:

| Destination | Transfer Count | Mechanism | Status |
|------------|---------------|-----------|--------|
| United States | 4 transfers | 3x DPF, 1x SCCs | All documented |
| United Kingdom | 2 transfers | UK adequacy | All documented |
| India | 1 transfer | SCCs Module 2 | TIA current |
| Switzerland | 1 transfer | Swiss adequacy | All documented |

### 7. Supervisory Authority Readiness Panel

| Readiness Metric | Status |
|-----------------|--------|
| All mandatory fields populated | Yes / No |
| All entries reviewed within 12 months | Yes / No |
| Export available in SA template format | Yes / No |
| Response time for Art. 30(4) request | < 48 hours / > 48 hours |
| All DPIAs for high-risk processing are approved | Yes / No |
| All international transfers documented | Yes / No |
| Overall readiness | READY / NOT READY |

## Reporting Cadence

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| Executive dashboard snapshot | Board / Audit Committee | Quarterly | KPIs, trend, top risks |
| Operational dashboard | DPO, Privacy team | Monthly | Full metrics, gap details, remediation progress |
| Processing owner status | Individual owners | Monthly | Their entries' status, action items |
| SA readiness assessment | DPO | Annually + on demand | Full readiness evaluation |
| Annual DPO report to board | Board | Annually | Comprehensive privacy programme report including RoPA section |

## Data Sources for Dashboard

| Dashboard Element | Data Source | Update Frequency |
|------------------|------------|------------------|
| Completeness scores | RoPA validation script output | Monthly |
| Review currency | last_reviewed_date field from RoPA | Real-time (from platform) |
| Processing activity counts | RoPA register | Real-time |
| Risk heatmap | Combination of data categories, scale, transfers | Quarterly recalculation |
| DPA status | Vendor management / DPA register | Monthly sync |
| DPIA linkage | DPIA register cross-reference | Monthly |
| Remediation tracking | Audit findings register | Weekly |

## Implementation for Helix Biotech Solutions

### Dashboard Report — Q1 2026

**Organisation**: Helix Biotech Solutions GmbH
**Report Period**: Q1 2026 (January — March)
**Prepared By**: Dr. Elena Voss, DPO

#### Executive Summary

| KPI | Value | Trend | Status |
|-----|-------|-------|--------|
| Overall Completeness Score | 93.2% | +2.1% from Q4 2025 | Amber (target: 95%) |
| Total Processing Activities | 49 | +2 from Q4 2025 | Informational |
| Mandatory Field Compliance | 98% (48/49) | Stable | Amber (1 entry incomplete) |
| Review Currency Rate | 96% (47/49) | +4% from Q4 2025 | Green |
| DPIA Linkage Rate | 100% (5/5 high-risk) | Stable | Green |
| Critical Gap Count | 1 | -1 from Q4 2025 | Amber (target: 0) |
| DPA Coverage Rate | 97% | +3% from Q4 2025 | Amber |
| Overdue Reviews | 2 | -3 from Q4 2025 | Amber |

#### Key Actions This Quarter

1. **Resolved**: 3 overdue reviews completed (RPA-019, RPA-031, RPA-038).
2. **New**: 2 new processing activities recorded (RPA-048: Genomic analysis, RPA-049: Salesforce CRM).
3. **Remediation**: 4 of 5 Major audit findings from Q4 2025 audit remediated. 1 remaining (RPA-023 retention — deadline 2026-03-21).
4. **Remaining critical gap**: RPA-049 (new Salesforce CRM) — retention period field awaiting finalisation by Sales Operations. Deadline: 2026-04-15.

#### Recommendations

1. Achieve 100% mandatory field compliance by addressing RPA-049 retention gap before Q2.
2. Conduct targeted review of Marketing department entries (lowest completeness at 82%).
3. Prepare for annual full completeness audit in Q2 2026.
