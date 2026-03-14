# RoPA Maintenance Workflow Reference

## Change Request Workflow

### Step 1: Trigger Detection

| Source | Detection Method | Responsible |
|--------|-----------------|-------------|
| IT change management | Privacy impact field on change request form | IT Change Manager |
| Vendor management | New vendor onboarding checklist, annual vendor review | Procurement |
| HR | New department creation, role changes, DPO appointment | HR Business Partner |
| Legal | Regulatory change monitoring, contract changes | Legal counsel |
| DPO office | Periodic review schedule, audit findings, DPIA outcomes | DPO / Privacy analyst |
| Incident response | Post-breach remediation, lessons learned | Incident Response Lead |
| Data subjects | Complaints, access requests revealing unrecorded processing | DPO office |

### Step 2: Impact Assessment

Upon trigger detection, the DPO office assesses:

1. Which RoPA entry (or entries) is affected?
2. Which specific fields require update?
3. Is this a new entry (major version), field update (minor version), or correction (patch)?
4. Does the change affect other entries (e.g., a processor change affecting multiple processing activities)?
5. Does the change require a DPIA or DPIA update?

### Step 3: Draft Update

1. The privacy analyst drafts the RoPA amendment, documenting old values and new values.
2. For new entries, all seven Art. 30(1) fields (or four Art. 30(2) fields) must be completed using the standard template.
3. Supporting evidence is attached: change request reference, DPA reference, DPIA reference, or regulatory citation.

### Step 4: Review and Approval

| Change Type | Reviewer | Approver | SLA |
|-------------|----------|----------|-----|
| New processing activity | DPO + Legal | DPO | 5 business days |
| Field update (purpose, recipients, transfers) | DPO | DPO | 3 business days |
| Administrative correction | Privacy analyst | DPO | 1 business day |
| Emergency update (breach-related, regulatory order) | DPO | DPO | Same day |

### Step 5: Implementation

1. Update the RoPA management system with approved changes.
2. Increment the version number according to the versioning scheme.
3. Update the change log with all required metadata.
4. Notify the processing owner that their entry has been updated.
5. If the change affects privacy notices, flag for privacy notice update.

### Step 6: Verification

1. Within 7 days, verify the update is correctly reflected in the RoPA system.
2. Run the automated validation script to confirm completeness.
3. For IT-triggered changes, verify post-deployment that the production system matches the RoPA description.

## Annual Review Workflow

### Preparation (Week 1-2)

1. Export current RoPA entries from the management system.
2. Generate a staleness report identifying entries not reviewed in the past 11+ months.
3. Generate a completeness report identifying any field gaps or vague terms.
4. Cross-reference against IT application inventory for coverage gaps.
5. Prepare per-department review packages for processing owners.

### Distribution and Self-Review (Week 3-4)

1. Email review packages to each processing owner with instructions.
2. Each processing owner reviews their entries and completes a confirmation form:
   - "I confirm all fields are accurate as of [date]" — OR —
   - "The following changes are required: [list changes]"
3. Follow up with non-respondents at the end of Week 4.

### Consolidation (Week 5)

1. Collect all responses and consolidate required changes.
2. Identify conflicts (e.g., two departments claiming different retention periods for shared data).
3. Resolve conflicts through discussion with affected owners.

### DPO Review (Week 6)

1. DPO reviews all proposed changes for legal accuracy.
2. DPO flags any entries requiring deeper investigation (e.g., suspected unrecorded processing, questionable lawful basis).
3. DPO confirms purposes align with current privacy notices.

### Finalisation (Week 7)

1. Processing owners provide final sign-off on updated entries.
2. Updated RoPA version is published.
3. Change log is updated.
4. Next review dates are set.

### Reporting (Week 8)

1. Produce annual RoPA maintenance report covering:
   - Total number of entries (start of year vs end of year)
   - Number of changes made during the year (categorised by type)
   - Completeness score trend
   - Outstanding findings from the annual review
   - Recommendations for process improvement
2. Present to the Data Protection Steering Committee.
3. Include in the DPO annual report to the board.

## Escalation Procedures

| Scenario | Escalation Path | Timeline |
|----------|----------------|----------|
| Processing owner does not respond to review request within 14 days | DPO escalates to department head | Within 2 business days of deadline |
| Processing discovered that is not recorded in RoPA | DPO raises with processing owner and senior management; RoPA entry created immediately | Same day detection |
| Processing owner refuses to update a record | DPO escalates to Chief Privacy Officer or General Counsel | Within 5 business days |
| Systemic maintenance failure (>20% of entries stale) | DPO reports to board audit committee | Within 10 business days |
| Supervisory authority requests RoPA and entries are stale | DPO coordinates rapid update and response; legal counsel engaged | Per supervisory authority deadline |
