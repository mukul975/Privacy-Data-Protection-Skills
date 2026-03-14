# RoPA Completeness Audit Workflow Reference

## Pre-Audit Phase

### Planning (1-2 weeks)

1. **Define audit scope**: Full organisational RoPA or targeted (by entity, department, or risk level).
2. **Select SA template**: Choose the primary supervisory authority template (CNIL, ICO, BfDI) based on establishment, pending investigations, or regulatory risk.
3. **Assemble audit team**: Lead auditor (DPO office or internal audit), technical reviewer, business process analyst.
4. **Gather inputs**: Current RoPA export, SA template, previous audit reports, DPIA register, DPA register.
5. **Configure scoring tool**: Load the selected SA template into the scoring engine and configure thresholds.

### Scope Definition

| Parameter | Options |
|-----------|---------|
| Coverage | Full (all entries) / Targeted (specific department/entity/risk level) |
| SA template | CNIL / ICO / BfDI / Custom composite |
| Scoring tiers | All three tiers / Tier 1 only (quick compliance check) |
| Sample verification | With interviews (thorough) / Without interviews (desk review only) |
| Previous findings | Include re-verification of prior audit findings? Yes / No |

## Execution Phase

### Step 1: Automated Field Scan (Day 1)

1. Export the full RoPA in JSON or CSV format.
2. Run the completeness scoring script against every entry.
3. Generate initial findings report with per-entry and aggregate scores.
4. Identify entries with Critical gaps (missing mandatory fields) for immediate attention.

### Step 2: Manual Quality Review (Days 2-5)

For each entry (or a stratified sample for large RoPAs):

1. Read the purpose description: Is it specific enough to demonstrate Art. 5(1)(b) compliance? Or is it a vague department-level statement?
2. Review retention periods: Are they expressed as concrete durations with clear triggers? Or do they use terms like "as long as necessary"?
3. Check transfer documentation: Does each transfer identify the destination country, recipient, and specific safeguard mechanism? Or just "SCCs in place"?
4. Assess security measures: Do they describe actual implemented controls? Or are they generic/aspirational?
5. Verify cross-references: Do processor entries reference DPA identifiers? Do high-risk entries reference DPIAs?
6. Check currency: When was the entry last reviewed? Is the review date within the acceptable threshold?

### Step 3: SA Template Mapping (Days 3-5)

Compare each entry against the selected SA template's additional fields:

1. Is the lawful basis documented? (Required by CNIL, ICO, BfDI — not explicitly required by Art. 30(1))
2. Is special category data flagged with the Art. 9(2) condition? (CNIL recommended, ICO required)
3. Is the DPIA reference included where applicable? (All SAs recommended)
4. Are technical and organisational measures documented separately? (BfDI required)
5. Is the processing owner/responsible department identified? (BfDI recommended)

### Step 4: Scoring Calculation (Day 5)

1. Calculate Tier 1 scores for each entry and in aggregate.
2. Calculate Tier 2 scores against the selected SA template.
3. Calculate Tier 3 quality scores.
4. Compute overall completeness score.
5. Compare against previous audit scores to identify trends.

### Step 5: Sample Verification (Days 6-8, if included)

1. Select a stratified random sample: 20% of entries, representing all departments and risk levels.
2. Interview processing owners to verify RoPA accuracy.
3. Cross-reference stated data flows against actual system configurations.
4. Document discrepancies as additional findings.

## Reporting Phase

### Audit Report Structure (Days 9-10)

1. **Executive summary**: Overall completeness score, comparison to previous audit, key findings, and recommendations.
2. **Methodology**: Scope, SA template used, scoring framework, sample size.
3. **Aggregate results**: Score distribution across all entries, heat map by department/entity.
4. **Detailed findings**: Per-entry gap analysis for entries scoring below threshold.
5. **Trend analysis**: Comparison to previous audits showing improvement or deterioration.
6. **Remediation plan**: Prioritised gap register with owners and deadlines.
7. **Recommendations**: Systemic improvements to prevent recurrence.

### Report Distribution

| Recipient | Content Level | Timeline |
|-----------|--------------|----------|
| DPO | Full report with all findings | Day 10 |
| Data Protection Steering Committee | Executive summary + aggregate results | Day 12 |
| Processing owners | Their entries' findings only | Day 12 |
| Board / Audit Committee | Executive summary + trend analysis | Day 15 |
| External auditor (if applicable) | Full report | On request |

## Post-Audit Remediation Tracking

### Weekly Remediation Review (for Critical findings)

1. DPO reviews progress on all Critical gaps.
2. Processing owners provide status updates.
3. Escalate any blocked remediation to department heads.
4. Update gap register status.

### 30-Day Checkpoint

1. Re-verify all Critical findings. Confirm remediation is effective.
2. Update completeness scores for remediated entries.
3. Escalate any remaining Critical gaps to senior management.

### 60-Day Checkpoint

1. Re-verify all Major findings.
2. Update aggregate completeness scores.
3. Produce interim progress report for the Steering Committee.

### 90-Day Checkpoint

1. Re-verify Minor findings and Enhancement items.
2. Produce final remediation report.
3. Calculate post-remediation completeness score.
4. Schedule next audit cycle.
