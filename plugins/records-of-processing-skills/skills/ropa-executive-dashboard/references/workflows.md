# RoPA Executive Dashboard Workflow Reference

## Dashboard Data Pipeline

### Monthly Automated Refresh

1. **Export RoPA data**: Extract all records from the RoPA management system in JSON format.
2. **Run completeness scan**: Execute the automated completeness scoring script against all entries.
3. **Calculate metrics**: Compute all Tier 1, Tier 2, and Tier 3 metrics from the extracted data.
4. **Store historical snapshot**: Archive the monthly metrics for trend analysis (retain 24 months minimum).
5. **Generate dashboard**: Update all visualisations with current data.
6. **Distribute alerts**: Send automated alerts for any metric that has crossed a threshold (Green to Amber, or Amber to Red).

### Quarterly Report Generation

1. **Automated data collection**: Collect monthly metrics for the quarter.
2. **Trend calculation**: Compare current quarter to previous quarter and year-over-year.
3. **Remediation status**: Pull current audit finding status from the finding tracker.
4. **Draft report**: Auto-generate the quarterly report structure with current data.
5. **DPO review**: DPO reviews and adds narrative commentary and recommendations.
6. **Distribution**: Distribute to Data Protection Steering Committee 5 business days before the meeting.

### Annual Board Report Preparation

1. **Full year data compilation**: Aggregate all quarterly metrics for the year.
2. **Annual completeness audit**: Conduct the full manual audit (not just automated scan).
3. **Trend analysis**: Compute year-over-year changes for all KPIs.
4. **Narrative preparation**: DPO drafts the narrative sections covering significant changes, regulatory developments, and recommendations.
5. **Board review**: Present to the board audit committee as part of the DPO annual report.

## Alert and Escalation Rules

| Metric | Green | Amber (Alert DPO) | Red (Escalate to Steering Committee) |
|--------|-------|-------------------|-------------------------------------|
| Completeness score | >=95% | 85-94% | <85% |
| Staleness rate | <=5% | 6-15% | >15% |
| DPA coverage | 100% | 90-99% | <90% |
| Transfer mechanism coverage | 100% | 90-99% | <90% |
| DPIA linkage | 100% | 80-99% | <80% |
| Remediation closure rate | >=90% | 70-89% | <70% |
| Review response rate | >=95% | 80-94% | <80% |

## Report Distribution Matrix

| Report | Frequency | Recipients | Format |
|--------|-----------|-----------|--------|
| Dashboard (live) | Real-time | DPO, Privacy team | Web dashboard / BI tool |
| Monthly metrics summary | Monthly | DPO, Privacy team leads | Email + PDF |
| Quarterly report | Quarterly | Steering Committee, entity DPOs | PDF presentation |
| Annual board report | Annually | Board, Audit Committee, Group DPO | Formal board paper |
| SA readiness briefing | On demand | DPO, Legal counsel | PDF + data export |
