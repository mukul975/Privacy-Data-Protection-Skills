---
name: ropa-completeness-audit
description: >-
  Audits Records of Processing Activities against supervisory authority
  templates from CNIL, ICO, and BfDI. Provides completeness scoring, gap
  identification, and remediation tracking. Activate for RoPA audit,
  completeness check, supervisory authority readiness, CNIL template,
  ICO template, BfDI template, gap analysis.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, ropa, audit, completeness, cnil, ico, bfdi, gap-analysis, remediation"
---

# RoPA Completeness Audit

## Overview

Supervisory authorities across the EEA publish RoPA templates and guidance that extend beyond the bare minimum Art. 30(1) requirements. While Art. 30(1) mandates seven fields, supervisory authorities such as CNIL, ICO, and BfDI expect additional information in practice. This skill provides a methodology for auditing RoPA entries against these expanded expectations, calculating completeness scores, identifying gaps, and tracking remediation to achieve supervisory authority readiness.

## Supervisory Authority Template Comparison

### CNIL (France) Template

The CNIL publishes the most structured RoPA template in the EU, available in both PDF and machine-readable (CSV/JSON) format. The CNIL template requires the Art. 30 mandatory fields plus additional recommended fields:

| Field | Art. 30 Mandatory | CNIL Required | CNIL Recommended |
|-------|-------------------|---------------|------------------|
| Controller identity and contact | Yes (a) | Yes | — |
| Joint controller details | Yes (a) | Yes | — |
| DPO contact | Yes (a) | Yes | — |
| Processing activity name | — | Yes | — |
| Purposes of processing | Yes (b) | Yes | — |
| Lawful basis (Art. 6) | — | — | Yes |
| Data subject categories | Yes (c) | Yes | — |
| Personal data categories | Yes (c) | Yes | — |
| Special category indication (Art. 9) | — | — | Yes |
| Recipient categories | Yes (d) | Yes | — |
| Processor details with DPA reference | — | — | Yes |
| International transfers | Yes (e) | Yes | — |
| Transfer safeguard mechanism | — | Yes | — |
| Retention periods | Yes (f) | Yes | — |
| Security measures | Yes (g) | Yes | — |
| DPIA conducted (yes/no) | — | — | Yes |
| DPIA reference | — | — | Yes |
| Last review date | — | — | Yes |

### ICO (United Kingdom) Template

The ICO template aligns with UK GDPR Art. 30 and includes guidance notes for each field:

| Field | Art. 30 Mandatory | ICO Required | ICO Recommended |
|-------|-------------------|-------------|-----------------|
| Controller name and contact | Yes (a) | Yes | — |
| DPO contact | Yes (a) | Yes | — |
| Purposes of processing | Yes (b) | Yes | — |
| Lawful basis | — | Yes | — |
| Legitimate interest description (if applicable) | — | — | Yes |
| Data subject categories | Yes (c) | Yes | — |
| Personal data categories | Yes (c) | Yes | — |
| Special category data and Art. 9 condition | — | Yes | — |
| Recipients | Yes (d) | Yes | — |
| International transfers with safeguards | Yes (e) | Yes | — |
| Retention periods | Yes (f) | Yes | — |
| Technical and organisational measures | Yes (g) | Yes | — |
| Link to privacy notice | — | — | Yes |
| DPIA reference | — | — | Yes |

### BfDI (Germany) Template

The German Federal Commissioner for Data Protection (BfDI) publishes guidance (Hinweise zum Verzeichnis von Verarbeitungstaetigkeiten) with sector-specific requirements:

| Field | Art. 30 Mandatory | BfDI Required | BfDI Recommended |
|-------|-------------------|--------------|------------------|
| Controller identity (Verantwortlicher) | Yes (a) | Yes | — |
| DPO (Datenschutzbeauftragte/r) | Yes (a) | Yes | — |
| Purpose (Zweck der Verarbeitung) | Yes (b) | Yes | — |
| Lawful basis (Rechtsgrundlage) | — | Yes | — |
| Data subject categories (Kategorien betroffener Personen) | Yes (c) | Yes | — |
| Personal data categories (Kategorien personenbezogener Daten) | Yes (c) | Yes | — |
| Recipients (Empfaenger) | Yes (d) | Yes | — |
| Transfers to third countries (Uebermittlungen in Drittlaender) | Yes (e) | Yes | — |
| Transfer safeguard with reference | — | Yes | — |
| Retention periods (Loeschfristen) | Yes (f) | Yes | — |
| Technical measures (Technische Massnahmen) | Yes (g) | Yes | — |
| Organisational measures (Organisatorische Massnahmen) | — | Yes | — |
| Responsible department (Verantwortliche Fachabteilung) | — | — | Yes |
| IT systems used | — | — | Yes |

## Completeness Scoring Methodology

### Scoring Framework

Each RoPA entry is scored against a three-tier assessment:

1. **Tier 1 — Art. 30 Mandatory Compliance** (40% weight): Are all seven Art. 30(1) mandatory fields populated?
2. **Tier 2 — Supervisory Authority Expectations** (35% weight): Does the entry meet the selected SA's expanded requirements?
3. **Tier 3 — Quality Assessment** (25% weight): Are populated fields specific, accurate, and current?

### Tier 1: Mandatory Field Scoring

| Field | Present (1/0) | Quality Score (0-3) |
|-------|--------------|---------------------|
| Art. 30(1)(a) Controller identity | [1/0] | 0 = Missing, 1 = Partial, 2 = Complete, 3 = Excellent |
| Art. 30(1)(b) Purposes | [1/0] | 0-3 |
| Art. 30(1)(c) Data subject categories | [1/0] | 0-3 |
| Art. 30(1)(c) Personal data categories | [1/0] | 0-3 |
| Art. 30(1)(d) Recipients | [1/0] | 0-3 |
| Art. 30(1)(e) International transfers | [1/0] | 0-3 |
| Art. 30(1)(f) Retention periods | [1/0] | 0-3 |
| Art. 30(1)(g) Security measures | [1/0] | 0-3 |

**Quality scoring criteria:**

- **0 (Missing)**: Field is empty or contains only "N/A" where substantive content is expected.
- **1 (Partial)**: Field contains some content but is materially incomplete (e.g., "employees" without further granularity for data subjects).
- **2 (Complete)**: Field satisfies the legal requirement with specific, substantive content.
- **3 (Excellent)**: Field exceeds minimum requirements with cross-references, supporting detail, and regulatory alignment.

### Tier 2: SA-Specific Field Scoring

Score additional fields required or recommended by the target SA. Each SA template adds 3-6 fields beyond Art. 30 minimums.

### Tier 3: Quality Metrics

| Metric | Scoring |
|--------|---------|
| Purpose specificity | 0-3 (penalise vague terms per EDPB guidance) |
| Retention concreteness | 0-3 (penalise "as long as necessary" type terms) |
| Transfer mechanism documentation | 0-3 (must identify specific mechanism, not just "safeguards in place") |
| Review currency | 0-3 (reviewed within 12m = 3, 12-18m = 2, 18-24m = 1, >24m = 0) |
| DPA cross-reference | 0-3 (all processors have DPA refs = 3) |

### Overall Completeness Score Calculation

```
Tier 1 Score = (fields present / 8) * (avg quality / 3) * 100
Tier 2 Score = (SA fields present / SA total fields) * (avg quality / 3) * 100
Tier 3 Score = (sum of quality metrics / max possible) * 100

Overall = (Tier 1 * 0.40) + (Tier 2 * 0.35) + (Tier 3 * 0.25)
```

**Readiness thresholds:**

| Score | Rating | Interpretation |
|-------|--------|---------------|
| 95-100% | Excellent | Supervisory authority ready — no immediate action |
| 85-94% | Good | Minor improvements recommended before SA interaction |
| 70-84% | Acceptable | Material gaps exist — remediation plan required |
| 50-69% | Poor | Significant non-compliance risk — urgent remediation |
| Below 50% | Critical | RoPA fundamentally deficient — rebuild required |

## Gap Identification Process

### Step 1: Template Selection

Select the primary supervisory authority template based on:
- The country where the controller is established (lead SA under one-stop-shop)
- Any pending investigations or correspondence with a specific SA
- Regulatory expectations in the primary market

### Step 2: Field-by-Field Comparison

For each RoPA entry, compare every field against the selected SA template and classify:

| Classification | Definition | Remediation Priority |
|---------------|------------|---------------------|
| Compliant | Field meets or exceeds SA expectations | None |
| Gap — Missing | Required field is absent | High |
| Gap — Incomplete | Field is present but does not meet SA expectations | Medium |
| Gap — Stale | Field content is outdated | Medium |
| Gap — Vague | Field content uses imprecise language | Medium |
| Enhancement | SA-recommended field not present | Low |

### Step 3: Gap Register

Compile all identified gaps into a structured register:

| Gap ID | Record ID | Processing Activity | Field | Classification | SA Template | Description | Severity | Remediation Owner | Target Date | Status |
|--------|-----------|---------------------|-------|----------------|-------------|-------------|----------|------------------|-------------|--------|
| GAP-001 | RPA-023 | Customer analytics | Art. 30(1)(f) | Missing | CNIL | Retention period field is empty | Critical | Stefan Richter | [Date] | Open |
| GAP-002 | RPA-034 | Website analytics | Art. 30(1)(b) | Vague | CNIL | Purpose too broad ("analytics") | Major | Julia Richter | [Date] | Open |

## Remediation Tracking

### Remediation Workflow

1. **Gap register creation**: Compile all gaps from the audit into the register.
2. **Prioritisation**: Sort by severity (Critical > Major > Minor > Enhancement).
3. **Owner assignment**: Assign each gap to the processing owner responsible for the affected entry.
4. **Deadline setting**: Critical = 30 days, Major = 60 days, Minor = 90 days, Enhancement = next annual review.
5. **Progress tracking**: Weekly status updates on Critical items, bi-weekly on Major items.
6. **Verification**: DPO verifies each remediated gap before closing.
7. **Re-scoring**: After remediation cycle, re-calculate completeness scores.

### Remediation Status Dashboard

| Severity | Total | Open | In Progress | Remediated | Verified |
|----------|-------|------|-------------|------------|----------|
| Critical | [n] | [n] | [n] | [n] | [n] |
| Major | [n] | [n] | [n] | [n] | [n] |
| Minor | [n] | [n] | [n] | [n] | [n] |
| Enhancement | [n] | [n] | [n] | [n] | [n] |
| **Total** | **[n]** | **[n]** | **[n]** | **[n]** | **[n]** |

## Audit Frequency

| Audit Type | Frequency | Scope |
|------------|-----------|-------|
| Full completeness audit | Annually | All RoPA entries against selected SA template |
| Targeted audit (post-change) | As needed | Entries affected by organisational or regulatory change |
| Pre-investigation readiness check | On demand | Full RoPA in preparation for SA investigation or inquiry |
| Automated completeness scan | Monthly | All entries — field presence and vague term detection only |
