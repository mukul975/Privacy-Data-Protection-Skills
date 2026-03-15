---
name: vendor-risk-scoring
description: >-
  Vendor privacy risk tiering methodology for processor management. Covers
  scoring factors including data volume, sensitivity, transfer locations,
  certifications, breach history, and control maturity with weighted risk
  calculation and tier assignment.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "vendor-risk-scoring, risk-tiering, privacy-risk, vendor-assessment, control-maturity"
---

# Vendor Privacy Risk Scoring

## Overview

Effective vendor privacy management requires a risk-based approach that allocates oversight resources proportionate to the privacy risk each vendor presents. GDPR Recital 76 states that risk should be assessed based on "the likelihood and severity" of potential impact on data subjects. The EDPB Guidelines 07/2020 (paragraph 86) indicate that the controller's assessment of processor sufficiency must consider expert knowledge, reliability, and resources — factors that feed directly into risk scoring.

At Summit Cloud Partners, the Vendor Privacy Risk Scoring Model assigns each vendor a quantified risk score based on objective factors, enabling consistent risk tiering, proportionate oversight, and audit prioritization.

## Risk Scoring Model

### Scoring Dimensions

The model evaluates seven dimensions, each scored on a 1-5 scale where 1 = lowest risk and 5 = highest risk.

**Dimension 1: Data Volume (Weight: 15%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | < 100 data subjects | Minimal volume processing |
| 2 | 100 – 1,000 data subjects | Low volume |
| 3 | 1,001 – 10,000 data subjects | Moderate volume |
| 4 | 10,001 – 100,000 data subjects | High volume |
| 5 | > 100,000 data subjects | Very high volume |

**Dimension 2: Data Sensitivity (Weight: 25%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | Pseudonymized non-sensitive data only | Minimal identifiability |
| 2 | Non-sensitive personal data (names, email) | Standard personal data |
| 3 | Behavioral data, location data, financial identifiers | Elevated sensitivity |
| 4 | Government IDs, precise geolocation, communications content | High sensitivity |
| 5 | Special category data (Art. 9) or criminal convictions (Art. 10) | Maximum sensitivity |

**Dimension 3: Transfer Locations (Weight: 15%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | Processing exclusively within EEA | No transfer risk |
| 2 | Processing in EEA + adequacy decision countries | Minimal transfer risk |
| 3 | Processing includes non-adequate countries with robust SCCs and supplementary measures | Managed transfer risk |
| 4 | Processing in jurisdictions with government surveillance concerns (per EDPB assessments) | Elevated transfer risk |
| 5 | Processing in jurisdictions lacking rule of law / no valid transfer mechanism | Maximum transfer risk |

**Dimension 4: Certifications and Attestations (Weight: 15%)**

Inverse scoring — higher certifications reduce risk.

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | ISO 27001 + ISO 27701 + SOC 2 Type II + sector-specific cert | Comprehensive certification |
| 2 | ISO 27001 + SOC 2 Type II (or equivalent combination) | Strong certification |
| 3 | ISO 27001 only or SOC 2 Type II only | Moderate certification |
| 4 | Self-assessment or CSA STAR Level 1 only | Limited certification |
| 5 | No recognized certifications or attestations | No certification |

**Dimension 5: Breach and Enforcement History (Weight: 10%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | No breaches, no enforcement actions in past 5 years | Clean record |
| 2 | Minor incident(s) with prompt notification and remediation | Low incident history |
| 3 | One significant breach with adequate response | Moderate history |
| 4 | Multiple breaches or one enforcement action | Elevated history |
| 5 | Major enforcement action or pattern of breach non-compliance | High-risk history |

**Dimension 6: Control Maturity (Weight: 10%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | Optimized — continuous improvement, metrics-driven, automated controls | Industry leading |
| 2 | Managed — controls measured and monitored, regular testing | Mature program |
| 3 | Defined — documented policies and procedures, periodic testing | Established program |
| 4 | Developing — basic controls in place, gaps in documentation | Emerging program |
| 5 | Initial — ad hoc controls, minimal documentation | Immature program |

**Dimension 7: Processing Autonomy (Weight: 10%)**

| Score | Criterion | Description |
|-------|-----------|-------------|
| 1 | No discretion — purely technical processing per exact instructions | Minimal autonomy |
| 2 | Limited discretion — predefined processing options | Low autonomy |
| 3 | Moderate discretion — processor selects technical means | Standard autonomy |
| 4 | Significant discretion — processor defines processing logic | Elevated autonomy |
| 5 | High discretion — processor approaches controller boundary | Maximum autonomy |

### Risk Score Calculation

```
Weighted Risk Score = Σ (Dimension Score × Dimension Weight)

Weighted Risk Score = (D1 × 0.15) + (D2 × 0.25) + (D3 × 0.15) + (D4 × 0.15)
                    + (D5 × 0.10) + (D6 × 0.10) + (D7 × 0.10)
```

### Risk Tier Assignment

| Tier | Score Range | Label | Oversight Level |
|------|-----------|-------|----------------|
| **Tier 1** | 3.5 – 5.0 | High Risk | Maximum oversight: annual on-site audit, quarterly monitoring, full due diligence refresh annually |
| **Tier 2** | 2.5 – 3.4 | Standard Risk | Standard oversight: annual remote audit, semi-annual monitoring, due diligence refresh biennially |
| **Tier 3** | 1.0 – 2.4 | Low Risk | Minimum oversight: biennial documentation audit, annual monitoring, due diligence refresh triennially |

### Tier-Based Oversight Requirements

| Activity | Tier 1 (High) | Tier 2 (Standard) | Tier 3 (Low) |
|----------|--------------|-------------------|--------------|
| Due diligence refresh | Annual | Biennial | Triennial |
| Privacy audit | Annual (Type 2 or 3) | Annual (Type 1) | Biennial (Type 1) |
| Sub-processor review | Quarterly | Semi-annual | Annual |
| DPA review | Annual | Biennial | Triennial |
| Risk score recalculation | Semi-annual | Annual | Biennial |
| Continuous monitoring | Active monitoring | Periodic monitoring | Annual check |

## Scoring Adjustments

### Escalation Triggers

The following events trigger automatic tier escalation (one tier up):

| Trigger | Duration |
|---------|----------|
| Personal data breach at vendor | Until post-breach reassessment completed |
| Regulatory enforcement action | Until remediation verified |
| Certification lapse (> 30 days) | Until certification renewed |
| Material service change without prior notification | Until change assessed |
| Failed audit (Critical findings) | Until remediation verified |

### De-escalation Criteria

Tier reduction requires:

1. At least one completed audit cycle at current tier with no Major or Critical findings
2. Updated certifications covering all processing in scope
3. DPO approval of tier reduction
4. Documentation of rationale

## Aggregated Vendor Risk Dashboard

Summit Cloud Partners maintains an aggregated view of vendor privacy risk:

| Metric | Description |
|--------|-------------|
| Total vendors processing personal data | Count of active vendor DPAs |
| Vendors by tier | Distribution across Tier 1/2/3 |
| Average risk score | Mean weighted score across all vendors |
| Trend | Quarter-over-quarter score movement |
| Overdue assessments | Vendors past their scheduled reassessment date |
| Open audit findings | Total by severity |
| Vendors with third-country transfers | Count and transfer mechanisms used |

## Key Regulatory References

- GDPR Recital 76 — Risk assessment based on likelihood and severity
- GDPR Article 24 — Controller responsibility proportionate to risk
- GDPR Article 28(1) — Sufficient guarantees requirement
- GDPR Article 32(1) — Security measures accounting for risk
- EDPB Guidelines 07/2020 — Processor assessment factors (paragraph 86)
- NIST SP 800-30 Rev. 1 — Guide for Conducting Risk Assessments (methodology reference)
