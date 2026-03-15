---
name: ropa-executive-dashboard
description: >-
  Creates executive reporting and visualization from RoPA data including
  processing activity counts, risk heatmaps, compliance scores, trend
  analysis, and supervisory authority readiness indicators. Activate for
  RoPA dashboard, executive reporting, risk heatmap, compliance score,
  trend analysis, board reporting, KPI.
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

The RoPA is a compliance document, but its data also serves as a strategic management tool. Aggregated RoPA data reveals the organisation's processing landscape, risk concentrations, compliance posture, and trends over time. This skill defines the metrics, visualisations, and reporting structures that transform raw RoPA data into executive-level insights for board reporting, DPO annual reports, and supervisory authority readiness assessments.

## Dashboard Metrics Framework

### Tier 1: Compliance Metrics (Supervisory Authority Readiness)

| Metric | Definition | Target | Data Source |
|--------|-----------|--------|-------------|
| RoPA completeness score | Percentage of entries meeting all Art. 30 mandatory fields with quality scoring | >=95% | Completeness audit engine |
| Staleness rate | Percentage of entries not reviewed within 12 months | <=5% | Last reviewed date field |
| DPA coverage | Percentage of processor recipients with documented Art. 28 DPAs | 100% | Recipient and DPA fields |
| Transfer mechanism coverage | Percentage of international transfers with documented safeguard mechanisms | 100% | Transfer field |
| DPIA linkage completeness | Percentage of high-risk entries linked to approved DPIAs | 100% | DPIA reference field |
| Purpose specificity | Percentage of entries with purposes free of vague terms | >=95% | Purpose field text analysis |
| Retention concreteness | Percentage of entries with concrete retention periods | >=95% | Retention field text analysis |

### Tier 2: Risk Metrics

| Metric | Definition | Calculation | Significance |
|--------|-----------|-------------|-------------|
| Special category processing count | Number of entries involving Art. 9 data | Count of entries where special_category != "None" | Higher count = greater regulatory risk |
| High-risk processing ratio | Ratio of DPIA-required entries to total entries | DPIA-required / Total | Indicates processing risk concentration |
| International transfer count | Total number of documented cross-border transfers | Sum of all transfer entries | Each transfer is a potential enforcement point |
| Third-country transfer risk score | Weighted count of transfers by destination risk | Transfers to non-adequate countries weighted 3x, adequacy countries 1x | Highlights transfer risk concentration |
| Processor dependency count | Number of unique external processors | Distinct count of processor recipients | Higher count = greater supply chain risk |
| Average entry age | Mean days since last review across all entries | Sum of days since review / Total entries | Indicates overall currency of records |

### Tier 3: Operational Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| Total processing activities | Count of active RoPA entries | Tracked over time for growth trends |
| Entries per department | Distribution of entries across business units | Balanced coverage expected |
| New entries (quarter) | Entries created in the current quarter | Indicates processing activity discovery rate |
| Archived entries (quarter) | Entries archived in the current quarter | Indicates decommissioning activity |
| Change velocity | Number of RoPA changes per quarter | Stable trend expected; spikes indicate organisational change |
| Remediation closure rate | Percentage of audit findings remediated within deadline | >=90% |
| Processing owner response rate | Percentage of review requests responded to within 14 days | >=95% |

## Visualisation Specifications

### 1. Risk Heatmap: Processing Activities by Risk Level and Department

**Axes**: X = Department (HR, Clinical, Marketing, Finance, IT, Facilities, Sales), Y = Risk Level (Low, Medium, High, Critical)

**Cell content**: Count of processing activities in each cell. Colour intensity proportional to count.

**Risk level determination**:
- **Critical**: DPIA required + special category data + international transfers to non-adequate countries
- **High**: DPIA required OR special category data
- **Medium**: International transfers OR large recipient list (>5 processors)
- **Low**: Standard processing with no risk indicators

**Example heatmap for Helix Biotech Solutions:**

| Department | Low | Medium | High | Critical |
|-----------|-----|--------|------|----------|
| Human Resources | 3 | 2 | 1 | 0 |
| Clinical Operations | 0 | 1 | 2 | 3 |
| Digital Marketing | 2 | 2 | 0 | 0 |
| Finance | 4 | 1 | 0 | 0 |
| IT | 3 | 2 | 0 | 0 |
| Facilities | 1 | 0 | 1 | 0 |
| Sales | 3 | 1 | 0 | 0 |

### 2. Compliance Score Gauge

**Type**: Radial gauge (speedometer style)
**Range**: 0-100%
**Zones**: Red (0-50), Amber (50-70), Yellow (70-85), Green (85-95), Dark Green (95-100)
**Current value**: Overall completeness score from the audit engine
**Comparison**: Previous quarter score shown as reference marker

### 3. Trend Analysis: Processing Activity Growth Over Time

**Type**: Line chart
**X-axis**: Quarters (8 quarters rolling)
**Y-axis**: Count of active processing activities
**Lines**: Total entries, new entries added, entries archived
**Purpose**: Shows whether the organisation is actively discovering and recording processing or whether the RoPA is stagnating

### 4. International Transfer Map

**Type**: Geographic flow map
**Base**: World map with EEA highlighted
**Flows**: Arrows from organisation location to each transfer destination country
**Arrow width**: Proportional to number of transfers to that country
**Colour**: Green = adequacy decision, Blue = SCCs, Purple = BCRs, Red = no mechanism documented

### 5. Supervisory Authority Readiness Indicator

**Type**: Traffic light indicator per metric
**Metrics displayed**: Each Tier 1 compliance metric with Green/Amber/Red status

| Metric | Status | Value | Threshold |
|--------|--------|-------|-----------|
| Completeness score | Green | 96.2% | Green >=95, Amber >=85, Red <85 |
| Staleness rate | Amber | 7.8% | Green <=5, Amber <=15, Red >15 |
| DPA coverage | Green | 100% | Green = 100, Amber >=90, Red <90 |
| Transfer coverage | Green | 100% | Green = 100, Amber >=90, Red <90 |
| DPIA linkage | Green | 100% | Green = 100, Amber >=80, Red <80 |

## Executive Report Structure

### Quarterly RoPA Report to Data Protection Steering Committee

**Page 1: Executive Summary**
- Overall compliance score (gauge)
- Key changes since last quarter
- Top 3 risks
- Top 3 remediation priorities

**Page 2: Compliance Dashboard**
- Tier 1 compliance metrics table
- SA readiness traffic lights
- Trend chart (4-quarter rolling)

**Page 3: Risk Landscape**
- Risk heatmap by department
- Special category processing summary
- International transfer map
- Processor dependency chart

**Page 4: Operational Metrics**
- Processing activity count and trend
- Change velocity chart
- Remediation closure rate
- Review response rate

**Page 5: Findings and Actions**
- Open audit findings by severity
- Remediation progress tracker
- Upcoming review deadlines
- Recommendations

### Annual DPO Report to the Board

The annual DPO report required under Art. 38(3) should include a RoPA section covering:

1. **Processing landscape overview**: Total activities, departments covered, year-over-year growth.
2. **Compliance posture**: Annual completeness score, comparison to previous year, SA readiness status.
3. **Risk summary**: High-risk processing activities, DPIA coverage, international transfer overview.
4. **Significant changes**: New processing activities, decommissioned activities, major regulatory changes.
5. **Audit outcomes**: Summary of annual completeness audit findings and remediation status.
6. **Recommendations**: Investment needs (tool upgrades, staffing), process improvements, regulatory preparation.

## KPI Definitions

### Primary KPIs (Report to Board)

| KPI | Definition | Target | Frequency |
|-----|-----------|--------|-----------|
| RoPA Compliance Index | Weighted average of all Tier 1 metrics | >=95% | Quarterly |
| Time to Record New Processing | Days from processing activity identification to RoPA entry approval | <=10 business days | Monthly |
| Audit Finding Closure Rate | Percentage of findings closed within deadline | >=90% | Quarterly |
| SA Readiness Score | Composite of compliance metrics indicating ability to respond to SA request within 48 hours | Green | Quarterly |

### Secondary KPIs (Report to DPO/Steering Committee)

| KPI | Definition | Target | Frequency |
|-----|-----------|--------|-----------|
| Review Response Rate | Percentage of annual review requests completed on time | >=95% | Annually |
| Change Management Integration | Percentage of IT change requests that complete privacy impact screening | >=98% | Monthly |
| Automated Discovery Coverage | Percentage of IT systems covered by automated RoPA scanning | >=80% | Quarterly |
| Cross-Reference Integrity | Percentage of RoPA-DPIA cross-references that are valid | 100% | Quarterly |

## Data Sources for Dashboard

| Metric | Primary Source | Refresh Frequency |
|--------|---------------|-------------------|
| Completeness scores | Completeness audit script output | Monthly (automated), Annually (manual) |
| Staleness data | RoPA last_reviewed_date field | Real-time |
| Risk indicators | DPIA reference, special category, transfer fields | Real-time |
| Trend data | Historical RoPA snapshots (stored quarterly) | Quarterly |
| Remediation data | Audit finding tracker | Weekly |
| Change velocity | RoPA change log | Real-time |
| Processing owner response | Review workflow system | Per review cycle |
