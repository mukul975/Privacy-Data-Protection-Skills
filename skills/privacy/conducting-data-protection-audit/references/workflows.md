# Data Protection Audit Workflow Reference

## Pre-Audit Planning Workflow

1. **Define scope and objectives**: Determine whether the audit is a full compliance audit across all eight domains or a targeted audit focusing on specific areas (e.g., processor management only, or security controls only).
2. **Identify audit criteria**: Map control points to the specific GDPR articles being assessed.
3. **Assign audit team**:
   - Lead auditor: Senior data protection professional with audit experience
   - Technical auditor: Information security specialist for Art. 32 controls
   - Business process auditor: For operational control testing
4. **Draft audit plan**: Include timeline, domains, interview schedule, document request list.
5. **Issue audit notification**: Notify all in-scope business units and the DPO at least 14 calendar days before fieldwork begins.
6. **Request documentation**: Send the pre-audit document request to each domain owner listing required evidence per control point.

## Evidence Collection Workflow

For each control point:

1. **Document review**: Examine the policy, procedure, or record that demonstrates the control.
2. **Interview**: Speak with the responsible person to understand how the control operates in practice.
3. **Testing**: Perform sample testing to verify the control is operating as described:
   - For access controls: Review a sample of user access permissions against role definitions.
   - For breach procedures: Walk through a simulated breach scenario.
   - For DSAR handling: Submit a test subject access request and track the response process.
   - For retention: Check a sample of records against the retention schedule.
   - For DPAs: Review 5-10 processor agreements against Art. 28(3) mandatory clauses.
4. **Classify the control**:
   - **Effective**: Control is designed and operating as intended with supporting evidence.
   - **Partially Effective**: Control exists but has gaps in design or operation.
   - **Ineffective**: Control exists but is not achieving its objective.
   - **Not Implemented**: No control exists for this requirement.

## Scoring Methodology

### Control-Level Scoring

| Rating | Score | Definition |
|--------|-------|-----------|
| Effective | 3 | Fully implemented, operating as designed, evidence available |
| Partially Effective | 2 | Implemented with gaps, some evidence available |
| Ineffective | 1 | Exists on paper but not operating, insufficient evidence |
| Not Implemented | 0 | No control in place |

### Domain-Level Scoring

Domain score = (Sum of control scores / Maximum possible score) x 100%

### Maturity Rating

| Score Range | Maturity Level | Description |
|-------------|---------------|-------------|
| 90-100% | Optimised | Controls are effective, continuously improved, and integrated into BAU |
| 70-89% | Managed | Controls are effective with minor gaps; monitoring is in place |
| 50-69% | Defined | Controls are designed but inconsistently implemented or monitored |
| 30-49% | Initial | Some controls exist but significant gaps remain |
| 0-29% | Ad Hoc | Minimal or no controls; compliance is not managed |

## Finding Classification Workflow

| Severity | Definition | Remediation Timeline | Escalation |
|----------|-----------|---------------------|------------|
| Critical | Mandatory GDPR requirement not met; imminent regulatory or data subject risk; processing may be unlawful | 30 days | Board and DPA notification consideration |
| Major | Significant gap in compliance; control exists but is materially ineffective; elevated risk | 60 days | Data Protection Steering Committee |
| Minor | Minor gap or improvement needed; control is partially effective with low residual risk | 90 days | Domain owner |
| Observation | Best practice recommendation; no compliance gap identified | Next review cycle | Advisory only |

## Reporting Workflow

1. **Draft report structure**:
   - Executive summary with overall maturity rating and key risks
   - Domain-by-domain results with control scores
   - Detailed findings with evidence, severity, and remediation recommendations
   - Compliance score dashboard
   - Prioritised remediation roadmap

2. **Review cycle**:
   - Draft report to DPO for factual accuracy review (5 business days)
   - Revised report to domain owners for management response (5 business days)
   - Final report to Data Protection Steering Committee and Board

3. **Distribution**: Final report classified as Confidential and distributed to DPO, Chief Information Security Officer, General Counsel, internal audit, and board-level sponsor.

## Remediation Tracking Workflow

1. Each finding is assigned a unique ID, owner, and target completion date.
2. Owners submit remediation plans within 10 business days of report issuance.
3. The DPO office tracks remediation progress monthly.
4. Follow-up testing is conducted:
   - Critical findings: 30-day verification
   - Major findings: 60-day verification
   - Minor findings: next scheduled audit
5. Overdue findings are escalated to the Data Protection Steering Committee.
6. Closure requires evidence of implementation reviewed by the audit team.

## Continuous Monitoring Integration

1. Feed audit findings into the organisational risk register.
2. Update the DPIA screening criteria if the audit reveals previously unidentified high-risk processing.
3. Revise the training programme to address knowledge gaps identified during interviews.
4. Update the audit programme for the next cycle based on findings and emerging regulatory priorities.
5. Include audit outcomes in the annual DPO report to the board per Art. 38(3).
