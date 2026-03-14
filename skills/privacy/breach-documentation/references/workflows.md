# Breach Documentation Records Workflow

## Entry Creation (Within 24 Hours of Breach Awareness)

1. **Initiate the register entry**: Upon breach confirmation, the Privacy Incident Coordinator creates a new entry in the OneTrust breach register module.
2. **Assign breach reference**: Generate the next sequential reference number (format: SPG-BREACH-YYYY-NNN).
3. **Populate facts section**: Enter all known facts — discovery timestamp, breach timestamp, type, affected systems, initial scope estimate.
4. **Link supporting documents**: Attach or link the incident report, initial risk assessment, and any SA notification filed.
5. **Set status**: Mark entry as "Open — Investigation in Progress."

## Ongoing Updates (Throughout Investigation)

1. **Update scope as investigation progresses**: Revise data subject counts, data category lists, and affected system inventories as forensic analysis reveals new information.
2. **Document notification decisions**: Record the Art. 33 notification decision with full rationale, DPO recommendation, and management sign-off.
3. **Record SA submissions**: Attach copies of SA notifications, reference numbers, and any SA correspondence.
4. **Record DS communications**: Attach copies of data subject notification letters, distribution logs, and response metrics.
5. **Track remediation**: Update the remediation action list with status (planned, in progress, completed, overdue) and evidence of completion.

## Entry Closure (Upon Investigation Completion)

1. **Final scope confirmation**: Finalize all data subject counts, data categories, and effects based on the completed investigation report.
2. **Remediation completion**: Verify all remediation actions are completed or have a defined timeline with responsible owner.
3. **DPO final review**: DPO reviews the complete register entry for accuracy, completeness, and compliance.
4. **Lessons learned**: Document the lessons learned and any policy or procedure changes resulting from the breach.
5. **Set status**: Mark entry as "Closed — Remediation Complete" (or "Closed — Remediation Ongoing" with a review date).

## Monthly Register Maintenance

1. **Completeness check**: Compare the breach register against the security incident management system (ServiceNow) to identify any security incidents involving personal data that were not added to the register.
2. **Open entry review**: Review all entries with "Open" status. Verify investigation and remediation are progressing. Escalate overdue items to the DPO.
3. **Overdue remediation follow-up**: Contact remediation owners for actions past their target completion date.
4. **Cross-reference verification**: Verify that each entry links to its supporting documentation (risk assessment, SA notification, DS notification, investigation report).

## Annual Register Audit

1. **Sample audit**: Select 20% of entries from the past 12 months for detailed accuracy review against source documentation.
2. **Trend analysis**: Generate reports showing:
   - Total breaches per quarter
   - Breach types (confidentiality/integrity/availability) distribution
   - Root cause categories and frequency
   - SA notification rate (percentage of breaches notified)
   - Mean time from discovery to SA notification
   - Remediation completion rate and mean time to complete
3. **Pattern identification**: Flag recurring root causes or breach types that indicate systemic control weaknesses.
4. **Board report preparation**: Prepare the annual breach summary for the Board Audit Committee.
5. **Register improvement**: Update the register template and fields based on audit findings and regulatory guidance changes.

## Export and Reporting Formats

| Audience | Format | Content |
|----------|--------|---------|
| Supervisory authority (on request) | PDF + CSV | Complete register or specified entries with all mandatory Art. 33(5) fields |
| Board Audit Committee | Executive summary (PDF) | Annual summary: breach counts, types, trends, notification rates, remediation status |
| DPO annual report | Section in DPO report | Breach statistics, notable incidents, lessons learned, recommendations |
| Internal audit | Full register (CSV) + supporting documentation | For compliance audit sampling and verification |
| Cyber insurance | Breach summary (PDF) | Claims-relevant entries with loss details and remediation evidence |
