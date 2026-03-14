# DPDP Act Compliance Workflow Reference

## Workflow 1: Consent Collection and Management

### Step 1 — Provide Notice (Section 5)
1. Draft notice containing: description of personal data to be processed, purpose of processing, how to exercise rights, how to complain to the Board.
2. Translate notice into applicable Eighth Schedule languages (at minimum English and Hindi for national operations).
3. Present notice before or at the time of data collection.
4. For existing data (Section 6(4)): provide notice as soon as reasonably practicable after commencement.

### Step 2 — Obtain Consent (Section 6)
1. Present consent request as a clear affirmative action (opt-in checkbox, digital signature, or equivalent).
2. Ensure consent is purpose-specific: separate consent for each distinct processing purpose.
3. Do not bundle consent with other terms or conditions.
4. Record consent with: data principal identifier, timestamp, purpose, version of notice, channel.

### Step 3 — Integrate Consent Manager (Section 6(7))
1. If using a registered Consent Manager, integrate via API.
2. Consent Manager provides the data principal with a unified dashboard showing all active consents.
3. Data principal may manage, review, and withdraw consent through the Consent Manager.
4. Consent Manager maintains auditable records for 7 years.

### Step 4 — Manage Withdrawal
1. Provide withdrawal mechanism that is as easy as giving consent.
2. Upon withdrawal, cease processing within a reasonable period (target: 30 days).
3. Direct all processors to cease processing the affected data.
4. Retain records of withdrawal for audit trail.
5. Inform data principal of consequences of withdrawal before actioning.

## Workflow 2: Legitimate Use Assessment (Section 7)

### Step 1 — Identify Applicable Legitimate Use
1. Review Section 7 categories: voluntary provision (a), State functions (b), legal obligation (c), medical emergency (d), epidemic/disaster (e), employment (f), public interest (g).
2. Document which specific clause applies and the factual basis.
3. For employment purposes (Section 7(f)): confirm the processing falls within enumerated employment activities.

### Step 2 — Document and Record
1. Record the legitimate use determination in the processing activity register.
2. Ensure the data principal is still informed (notice requirements under Section 5 apply even for legitimate uses).
3. Include legitimate use basis in the privacy notice.
4. Review annually or upon material change.

## Workflow 3: Significant Data Fiduciary Compliance

### Step 1 — SDF Designation Assessment
1. Monitor Central Government notifications for SDF designation criteria.
2. Assess against known criteria: volume of data, sensitivity, risk to rights, sovereignty impact.
3. If designated (or likely to be designated), prepare for additional obligations.

### Step 2 — Appoint DPO and Auditor
1. Appoint a DPO based in India (Section 10(2)(a)).
2. DPO must represent the SDF and serve as point of contact for data principals and the Board.
3. Appoint an independent data auditor (Section 10(2)(b)).
4. Independent auditor must not have a material relationship with the SDF.

### Step 3 — Conduct DPIA
1. Conduct Data Protection Impact Assessment per Section 10(2)(c) and prescribed methodology.
2. Assess risks to data principal rights from processing activities.
3. Document mitigation measures for identified risks.
4. Submit audit report to the Board as prescribed.

### Step 4 — Ongoing Compliance
1. Periodic audits by independent data auditor.
2. Submit audit reports to the Board.
3. Address findings within prescribed timelines.
4. Maintain records for Board inspection.

## Workflow 4: Data Subject Rights Response

### Receipt (Day 0)
1. Data principal submits request through privacy portal, email, or Consent Manager interface.
2. Verify identity (Aadhaar-based digital verification, or alternative identity verification as prescribed).
3. Classify: access, correction, erasure, grievance, or nomination.

### Fulfilment (Days 1-28)
1. **Access (Section 11)**: Compile summary of personal data processed and processing activities; identify all processors and fiduciaries who received the data.
2. **Correction (Section 12)**: Validate correction request; update records across all systems and processors.
3. **Erasure (Section 12)**: Identify data no longer necessary for purpose; execute deletion; retain data required by law.
4. **Nomination (Section 14)**: Record nominee details; enable nominee to exercise rights upon death or incapacity.

### Response (Day 30 target)
1. Deliver response through the channel used for the request.
2. If unable to fulfil, provide reasons.
3. Inform of right to file complaint with the Grievance Officer and subsequently with the Board.
4. Record in DSR management log.

## Workflow 5: Breach Notification (Section 8(6))

### Detection and Assessment (Hours 0-24)
1. Security incident detected through monitoring or external notification.
2. Determine whether personal data is affected.
3. Assess likelihood of harm to data principals.
4. If personal data breach confirmed and harm likely, activate notification workflow.

### Board Notification (Within 72 hours — draft rules)
1. Prepare notification in prescribed form.
2. Include: nature of breach, data affected, number of data principals, measures taken, contact information.
3. Submit to the Board through prescribed mechanism.

### Data Principal Notification (Within 72 hours — draft rules)
1. Notify each affected data principal individually (where practicable).
2. If individual notification is disproportionate, use public notification mechanisms.
3. Include: description of breach, potential consequences, remedial measures, contact for grievance officer.

### Post-Breach Actions
1. Implement containment and remediation measures.
2. Conduct root cause analysis.
3. Update security safeguards.
4. Report remediation to the Board.
5. Retain breach records for Board inspection.

## Workflow 6: Children's Data Compliance (Section 9)

### Step 1 — Age Verification
1. Implement age verification mechanism at data collection points.
2. For users who indicate age under 18, activate parental consent workflow.
3. Verification mechanism per draft rules (digital identity verification, parental declaration).

### Step 2 — Obtain Verifiable Parental Consent
1. Verify the identity of the parent or lawful guardian.
2. Obtain specific consent for the child's data processing.
3. Inform parent of: data to be processed, purpose, rights, prohibition on harmful processing.

### Step 3 — Processing Restrictions
1. No tracking, behavioural monitoring, or targeted advertising directed at the child.
2. No processing likely to cause detrimental effect on the child's well-being.
3. Monitor for Central Government exemptions for specific fiduciary classes.

### Step 4 — Record-Keeping
1. Maintain records of parental consent verification.
2. Delete child's data when purpose is fulfilled or when the child reaches 18 and does not provide independent consent.
