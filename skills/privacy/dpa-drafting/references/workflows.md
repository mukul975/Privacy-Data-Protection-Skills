# Workflows — DPA Drafting

## Workflow 1: New DPA Drafting Process

```
TRIGGER: Vendor due diligence completed with APPROVED or CONDITIONALLY APPROVED decision
  │
  ├─► Step 1: Gather Processing Details (Privacy Team — 3 business days)
  │     ├─ Collect from business unit:
  │     │     ├─ Detailed service description
  │     │     ├─ Personal data categories to be processed
  │     │     ├─ Data subject categories and approximate volumes
  │     │     ├─ Processing operations (collect, store, analyze, delete)
  │     │     └─ Expected processing locations
  │     ├─ Collect from vendor:
  │     │     ├─ Current sub-processor list with locations and functions
  │     │     ├─ Security measures documentation (for Annex II)
  │     │     └─ Existing DPA template (if vendor proposes one)
  │     └─ Cross-reference with due diligence data flow analysis
  │
  ├─► Step 2: Select DPA Template (Privacy Team — 1 business day)
  │     ├─ Option A: Summit Cloud Partners standard DPA template
  │     │     └─ Preferred for all engagements — maintains consistency
  │     ├─ Option B: EU Commission Standard Contractual Clauses (Decision 2021/915)
  │     │     └─ Use when vendor or regulatory requirement mandates
  │     ├─ Option C: Vendor-proposed DPA
  │     │     └─ Only if vendor is non-negotiable — requires legal review against checklist
  │     └─ Document template selection rationale
  │
  ├─► Step 3: Draft DPA Annexes (Privacy Team — 5 business days)
  │     ├─ Annex I — Description of Processing:
  │     │     ├─ Subject-matter and duration
  │     │     ├─ Nature and purpose of processing
  │     │     ├─ Type of personal data (exhaustive list)
  │     │     ├─ Categories of data subjects
  │     │     └─ Processing locations
  │     ├─ Annex II — Technical and Organisational Measures:
  │     │     ├─ Encryption standards (at rest and in transit)
  │     │     ├─ Access control measures
  │     │     ├─ Network security
  │     │     ├─ Physical security
  │     │     ├─ Incident response capabilities
  │     │     ├─ Business continuity / disaster recovery
  │     │     └─ Personnel security (training, confidentiality)
  │     ├─ Annex III — Approved Sub-Processors:
  │     │     ├─ Sub-processor name
  │     │     ├─ Processing location
  │     │     ├─ Processing description
  │     │     └─ Transfer mechanism (if outside EEA)
  │     └─ Annex IV — Controller Instructions (if separate from Annex I)
  │
  ├─► Step 4: Legal Review (Legal Team — 5 business days)
  │     ├─ Verify all 8 mandatory provisions present
  │     ├─ Check liability allocation and indemnification
  │     ├─ Review breach notification timeframe (recommend ≤ 24 hours)
  │     ├─ Confirm audit rights are practical and exercisable
  │     ├─ Verify sub-processor objection mechanism is genuine
  │     ├─ Check international transfer provisions (if applicable)
  │     ├─ Review termination data handling provisions
  │     └─ Issue Legal Review Approval or Revision Requests
  │
  ├─► Step 5: Vendor Negotiation (Legal + Privacy Team — 10 business days)
  │     ├─ Share draft DPA with vendor legal team
  │     ├─ Track redline changes and negotiations
  │     ├─ Non-negotiable provisions:
  │     │     ├─ Audit rights (must remain practical)
  │     │     ├─ Breach notification timeframe (must remain ≤ 48 hours)
  │     │     ├─ Sub-processor objection mechanism (must remain genuine)
  │     │     └─ Deletion certification upon termination
  │     ├─ Negotiable provisions:
  │     │     ├─ Audit frequency and cost allocation
  │     │     ├─ Liability caps (subject to legal approval)
  │     │     └─ Specific security measure implementation details
  │     └─ Escalate unresolved items to DPO
  │
  ├─► Step 6: DPO Approval (DPO — 2 business days)
  │     ├─ Final review of negotiated DPA
  │     ├─ Verify compliance against 17-point checklist
  │     ├─ Approve or request further revisions
  │     └─ Document approval decision
  │
  └─► Step 7: Execution and Filing (Legal Team — 2 business days)
        ├─ Route for authorized signatures
        ├─ Store executed DPA in contract management system
        ├─ Update vendor register with DPA reference
        ├─ Set contract review reminder (aligned with MSA term)
        └─ Distribute copies to Privacy Team and requesting business unit
```

## Workflow 2: DPA Amendment Process

```
TRIGGER: Material change to processing arrangement
  ├─ Change in data categories processed
  ├─ Change in processing locations
  ├─ New sub-processor addition
  ├─ Change in processing purpose
  ├─ Security measure modification
  │
  ├─► Step 1: Change Assessment (Privacy Team — 2 business days)
  │     ├─ Document the proposed change
  │     ├─ Assess impact on existing DPA provisions
  │     ├─ Determine if amendment or full DPA reissue needed
  │     └─ Check if change requires updated DPIA
  │
  ├─► Step 2: Draft Amendment
  │     ├─ Reference original DPA clause numbers
  │     ├─ State the change clearly with before/after comparison
  │     ├─ Update affected annexes
  │     └─ Add amendment effective date
  │
  ├─► Step 3: Approval and Execution
  │     ├─ Legal review of amendment
  │     ├─ DPO approval
  │     ├─ Vendor agreement
  │     └─ Authorized signatures
  │
  └─► Step 4: Records Update
        ├─ Store amendment with original DPA
        ├─ Update vendor register
        └─ Notify affected stakeholders
```

## Workflow 3: DPA Compliance Verification Audit

```
TRIGGER: Annual review cycle or audit schedule
  │
  ├─► Step 1: Pull Current DPA from Records
  │     ├─ Retrieve executed DPA and all amendments
  │     └─ Retrieve vendor's current processing documentation
  │
  ├─► Step 2: Verify Against 17-Point Checklist
  │     ├─ Check each mandatory provision present and current
  │     ├─ Verify data categories still match actual processing
  │     ├─ Confirm sub-processor list is current
  │     ├─ Verify processing locations match actual deployments
  │     └─ Check transfer mechanisms remain valid
  │
  ├─► Step 3: Issue Findings
  │     ├─ Critical: Missing mandatory provisions or material inaccuracies
  │     ├─ Major: Outdated annexes or stale sub-processor lists
  │     ├─ Minor: Formatting issues or non-material discrepancies
  │     └─ Observation: Areas for improvement
  │
  └─► Step 4: Remediation
        ├─ Critical/Major: Initiate DPA amendment process
        ├─ Minor: Add to next scheduled DPA review
        └─ Document all findings and actions in audit trail
```
