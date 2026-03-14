# Prior Consultation Submission Record

**Organisation**: Nexus Technologies GmbH
**Processing Activity**: Employee biometric time-and-attendance system
**DPIA Reference**: DPIA-2026-BIO-001
**Submission Date**: 2026-02-15
**Authority**: Bundesbeauftragter fuer den Datenschutz und die Informationsfreiheit (BfDI)

---

## Prior Consultation Trigger

The DPIA for the proposed biometric time-and-attendance system (fingerprint scanning for 380 employees across 3 office locations) identified high residual risk in the following areas:

| Risk Area | Residual Risk Level | Mitigation Applied |
|-----------|--------------------|--------------------|
| Biometric data breach | High | AES-256 encryption, on-device template storage, no central biometric database |
| Function creep (biometric data reuse) | Medium | Technical controls preventing export; policy prohibition on secondary use |
| Employee coercion (lack of genuine consent) | High | Alternative PIN-based system offered; documented employee choice |
| Disproportionate surveillance | Medium | Limited to entry/exit logging only; no continuous monitoring |

Despite mitigation, the BfDI Art. 35(4) DPIA blacklist includes "large-scale processing of biometric data for identification of natural persons" requiring DPIA, and the residual risks of biometric data breach and employee coercion remain high due to the inherent sensitivity of biometric data under Art. 9(1).

---

## Art. 36(3) Documentation Package

| Requirement | Provided | Reference |
|-------------|----------|-----------|
| Responsibilities of controller and processors | Yes | Section 2 of submission: Nexus (controller), BiometriScan GmbH (processor under DPA-2026-BS-001) |
| Purposes and means of processing | Yes | Section 3: Time-and-attendance recording for payroll accuracy; fingerprint scanning at entry/exit points |
| Measures and safeguards | Yes | Section 4: 12 technical and organisational measures documented |
| DPO contact details | Yes | Dr. Katharina Weiss, dpo@nexus-tech.eu, +49 30 2345 6789 |
| Completed DPIA | Yes | DPIA-2026-BIO-001 (42 pages) attached |

---

## Timeline Tracking

| Milestone | Date |
|-----------|------|
| Submission to BfDI | 2026-02-15 |
| 8-week initial deadline | 2026-04-12 |
| Extension notification received | 2026-03-28 (6-week extension granted for complexity) |
| Extended deadline | 2026-05-24 |
| BfDI response received | 2026-05-10 |

---

## Authority Response

The BfDI provided written advice on 2026-05-10 with the following recommendations:

1. **Condition**: The alternative PIN-based system must be genuinely equivalent in convenience; employees choosing the alternative must not experience any operational disadvantage.
2. **Recommendation**: Conduct an annual review of the biometric system proportionality, including employee feedback survey.
3. **Recommendation**: Implement automated deletion of biometric templates within 30 days of employment termination (current policy: 90 days).
4. **No objection**: The BfDI did not exercise corrective powers under Art. 58(2) and did not object to the processing proceeding subject to the above conditions.

---

## Post-Consultation Actions

| Action | Owner | Deadline | Status |
|--------|-------|----------|--------|
| Ensure PIN alternative is operationally equivalent | Andreas Koch, Facilities | 2026-06-01 | Completed |
| Reduce biometric template deletion to 30 days post-termination | IT Operations | 2026-06-15 | Completed |
| Schedule annual proportionality review | DPO Office | 2027-02-15 | Scheduled |
| Update DPIA with consultation outcome | Dr. Katharina Weiss | 2026-06-01 | Completed |
| Commence biometric system deployment | Facilities | 2026-07-01 | Proceeding |

---

**Prepared by**: Dr. Katharina Weiss, DPO
**Approved by**: Jan Mueller, CTO
