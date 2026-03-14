# Workplace Email Privacy Workflows

## Workflow 1: Email Monitoring Proportionality Assessment

```
START: Proposal to implement or review email/internet monitoring
│
├─ Step 1: Apply Barbulescu Factor 1 — Prior Notification
│  ├─ Is there an Acceptable Use Policy covering email monitoring? [Yes/No]
│  ├─ Does the AUP specify what is monitored (metadata, content, both)? [Yes/No]
│  ├─ Have all employees acknowledged the AUP? [Yes/No]
│  ├─ ALL Yes → Factor 1 SATISFIED
│  └─ ANY No → Factor 1 FAILED → Remediate before proceeding
│
├─ Step 2: Apply Barbulescu Factor 2 — Extent of Monitoring
│  ├─ Is monitoring limited to metadata? → Low intrusion
│  ├─ Does monitoring include content scanning (DLP)? → Medium intrusion
│  ├─ Does monitoring include human review of content? → High intrusion
│  ├─ Is monitoring continuous or triggered? Continuous → Higher intrusion
│  ├─ ASSESS: Is the extent justified by the purpose?
│  └─ Can scope be reduced? If yes → Reduce before proceeding
│
├─ Step 3: Apply Barbulescu Factor 3 — Legitimate Reasons
│  ├─ Document the specific legitimate aim:
│  │  [ ] Data loss prevention
│  │  [ ] Information security
│  │  [ ] Regulatory compliance (financial services)
│  │  [ ] Investigation of specific misconduct
│  │  [ ] Trade secret protection
│  │  [ ] Other: _____________
│  └─ Is the aim documented and specific? [Yes → Continue / No → Document first]
│
├─ Step 4: Apply Barbulescu Factor 4 — Less Intrusive Alternatives
│  ├─ Could metadata monitoring achieve the aim? [If yes → Use metadata only]
│  ├─ Could automated DLP scanning replace human content review? [If yes → Use DLP]
│  ├─ Could training and policy enforcement replace monitoring? [If yes → Consider]
│  └─ Document why less intrusive alternatives are insufficient
│
├─ Step 5: Apply Barbulescu Factor 5 — Consequences
│  ├─ Can monitoring data lead to disciplinary action? [Yes/No]
│  ├─ Is human review required before any adverse action? [Yes/No]
│  ├─ Is there a separation between monitoring function and disciplinary function? [Yes/No]
│  └─ ASSESS: Are consequences proportionate and safeguarded?
│
├─ Step 6: Apply Barbulescu Factor 6 — Safeguards
│  ├─ [ ] Access to monitoring data restricted to authorised personnel
│  ├─ [ ] Privileged communications excluded (legal, medical, union)
│  ├─ [ ] Retention period defined and enforced
│  ├─ [ ] Audit logging enabled for monitoring data access
│  ├─ [ ] Employee grievance procedure available
│  ├─ [ ] Annual proportionality review scheduled
│  └─ ALL checked → Factor 6 SATISFIED
│
├─ DECISION:
│  ├─ All 6 factors satisfied → Monitoring may proceed. Document assessment.
│  ├─ Some factors failed → Modify monitoring to address gaps. Re-assess.
│  └─ Multiple factors failed → Monitoring should not proceed in current form.
│
└─ END: Record assessment in DPIA register. Schedule annual review.
```

## Workflow 2: Acceptable Use Policy Implementation

```
START: Draft or update AUP for email and internet monitoring
│
├─ Step 1: Define scope
│  ├─ Which systems are covered? (email, internet, messaging, phone, BYOD)
│  ├─ Which employees are covered? (all, specific roles, specific departments)
│  └─ Document scope clearly in Section 1 of AUP
│
├─ Step 2: Define personal use rules
│  ├─ Is limited personal use permitted? [Yes/No]
│  ├─ If Yes: during breaks only? At any time? Volume limits?
│  └─ Document personal use rules clearly in Section 2 of AUP
│
├─ Step 3: Define monitoring disclosure
│  ├─ What is monitored: [ ] Metadata [ ] Content (DLP) [ ] Both
│  ├─ When: [ ] Continuous [ ] Triggered [ ] Periodic
│  ├─ By whom: [ ] IT Security [ ] Compliance [ ] HR [ ] Line Manager
│  └─ Document monitoring specifics in Section 3 of AUP
│
├─ Step 4: Define exclusions
│  ├─ [ ] Legal professional privilege communications excluded
│  ├─ [ ] Medical communications excluded
│  ├─ [ ] Trade union communications excluded
│  └─ Document exclusions in Section 4 of AUP
│
├─ Step 5: Define employee rights
│  ├─ Right to access monitoring data about them (Art. 15)
│  ├─ Right to challenge monitoring decisions
│  ├─ Grievance procedure reference
│  └─ Document rights in Section 5 of AUP
│
├─ Step 6: Review and approval
│  ├─ DPO review and sign-off
│  ├─ Legal counsel review
│  ├─ Works council consultation (where applicable)
│  ├─ Senior management approval
│  └─ Version control: date, version number, approved by
│
├─ Step 7: Distribution
│  ├─ Provide to all employees before monitoring begins
│  ├─ Obtain written acknowledgment from each employee
│  ├─ Make available on intranet
│  └─ Include in new starter onboarding pack
│
└─ END: AUP in force. Schedule annual review.
```

## Workflow 3: Covert Monitoring Authorisation

```
START: Suspicion of criminal activity or serious misconduct
│
├─ Step 1: Pre-conditions check
│  ├─ Is there a reasonable, documented suspicion? [Yes/No → STOP if No]
│  ├─ Has the suspicion been verified through non-intrusive means? [Yes/No]
│  └─ Are less intrusive investigation methods insufficient? [Yes/No → Use them if Yes]
│
├─ Step 2: Authorisation
│  ├─ Senior authoriser identified: [ ] CEO [ ] Board member [ ] Other: _____
│  ├─ Legal counsel consulted: [Yes/No → Must be Yes]
│  ├─ DPO notified: [Yes/No → Must be Yes]
│  └─ Written authorisation obtained with:
│     ├─ Specific justification
│     ├─ Scope (target employee, channels, data types)
│     ├─ Time limit (maximum recommended: 14 days)
│     └─ Review date
│
├─ Step 3: Execution
│  ├─ Monitoring limited to authorised scope
│  ├─ Personal communications excluded where identifiable
│  ├─ All monitoring data secured with restricted access
│  └─ Regular review against time limit
│
├─ Step 4: Conclusion
│  ├─ Misconduct found → Proceed to disciplinary process; disclose monitoring to employee
│  ├─ No misconduct found → Inform employee of monitoring within reasonable time
│  └─ Delete all monitoring data per retention policy
│
└─ END: Document entire process. File with DPO.
```
