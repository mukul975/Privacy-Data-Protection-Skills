# RoPA Executive Dashboard Workflow Reference

## Dashboard Setup Workflow

### Step 1: Define Metrics and Data Sources

1. Select KPIs from the Tier 1 (board), Tier 2 (operational), and Tier 3 (risk) lists.
2. Map each KPI to its data source (RoPA register, DPIA register, audit findings register, DPA register).
3. Define calculation methodology for each KPI (formula, threshold, colour coding).
4. Set baseline values from the most recent audit or current state assessment.

### Step 2: Data Pipeline Configuration

1. Configure automated data extraction from the RoPA management platform (API or scheduled export).
2. Set up automated calculation of derived metrics (completeness scores, currency rates, trend calculations).
3. Configure alert thresholds for each KPI (green/amber/red boundaries).
4. Schedule data refresh: real-time for platform-based metrics, monthly for calculated scores.

### Step 3: Visualisation Build

1. Build the executive summary view (single page, 6-8 KPIs with gauges and trend indicators).
2. Build the operational view (multi-page with drill-down capability).
3. Build the processing owner view (filtered to individual owner's entries).
4. Build the SA readiness view (checklist format with pass/fail indicators).
5. Implement role-based access: board sees executive view only, DPO sees all views.

### Step 4: Validation and Launch

1. Validate all calculations against manual counts from the RoPA register.
2. Review with the DPO for accuracy and relevance.
3. Present prototype to a board member for feedback on clarity and actionability.
4. Launch with initial baseline snapshot.

## Monthly Reporting Workflow

### Data Collection (Day 1-2)

1. Run automated data extraction from RoPA platform.
2. Run validation script for completeness scoring.
3. Pull DPIA register status for linkage metrics.
4. Pull DPA register for coverage metrics.
5. Pull audit findings register for remediation tracking.

### Analysis (Day 3-4)

1. Calculate all KPIs for the current month.
2. Compare against previous month and same month last year.
3. Identify trend direction for each KPI (improving/stable/declining).
4. Flag any KPIs that have crossed threshold boundaries.
5. Identify root causes for significant changes.

### Report Generation (Day 5)

1. Populate the dashboard template with current data.
2. Write executive commentary (2-3 sentences explaining key changes and actions).
3. List recommended actions for any amber or red KPIs.
4. Distribute to defined audiences per the reporting cadence.

## Quarterly Board Report Workflow

### Preparation (2 weeks before board meeting)

1. Generate the quarterly dashboard snapshot.
2. Compile trend analysis for all Tier 1 KPIs over the past 4 quarters.
3. Summarise key events: new processing activities, completed audits, SA interactions, breach impacts on RoPA.
4. Prepare 1-page executive summary suitable for board pack inclusion.

### Content

The quarterly board report should cover:

1. **Compliance posture**: Overall completeness score with trend.
2. **Material changes**: New high-risk processing activities, significant transfers, or regulatory changes.
3. **Risk exposure**: Any critical or major gaps, and remediation progress.
4. **SA readiness**: Assessment of readiness for SA inquiry.
5. **Outlook**: Upcoming changes (new systems, regulatory deadlines, planned audits).

### Presentation

1. Maximum 5 minutes in the board agenda.
2. Lead with the overall score and trend (one number, one direction).
3. Highlight any items requiring board decision or awareness.
4. Avoid technical jargon — frame in business risk terms.

## Annual DPO Report Workflow

### Scope

The annual DPO report under Art. 38(3) includes a dedicated RoPA section covering:

1. Year-over-year comparison of all Tier 1 KPIs.
2. Summary of processing activity landscape (total count, breakdown by department, by risk level).
3. Audit results and remediation outcomes.
4. SA interactions and their impact on RoPA.
5. Assessment of RoPA governance maturity.
6. Recommendations for the coming year.

### Timeline

| Week | Activity |
|------|----------|
| W1 | Data extraction and KPI calculation for full year |
| W2 | Trend analysis and year-over-year comparison |
| W3 | Draft report preparation |
| W4 | DPO review and finalisation |
| W5 | Presentation to board |
