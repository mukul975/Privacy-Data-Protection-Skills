# Workflows — Vendor Privacy Audit

## Workflow 1: Annual Vendor Audit Cycle

```
TRIGGER: Annual audit schedule (January planning cycle)
  │
  ├─► Step 1: Vendor Selection and Prioritization (Privacy Team — Week 1-2)
  │     ├─ Review vendor register for all vendors with personal data processing DPAs
  │     ├─ Apply risk-based prioritization:
  │     │     ├─ High-risk vendors (Tier 1): Full audit (Type 2 or 3) annually
  │     │     ├─ Standard-risk vendors (Tier 2): Documentation audit (Type 1) annually
  │     │     ├─ Low-risk vendors (Tier 3): Documentation audit biennially
  │     │     └─ Triggered vendors: Priority audit regardless of schedule
  │     ├─ Produce Annual Audit Plan with:
  │     │     ├─ Vendor list with assigned audit type
  │     │     ├─ Target month for each audit
  │     │     ├─ Assigned audit team lead
  │     │     └─ Budget allocation
  │     └─ DPO approval of Annual Audit Plan
  │
  ├─► Step 2: Audit Preparation (per vendor — 4 weeks before audit)
  │     ├─ Issue 30-day audit notification to vendor
  │     ├─ Send document request list:
  │     │     ├─ Current certifications (ISO 27001, SOC 2, etc.)
  │     │     ├─ DPA compliance self-assessment
  │     │     ├─ Sub-processor register update
  │     │     ├─ Incident log for past 12 months
  │     │     ├─ Training completion records
  │     │     ├─ DSR handling metrics
  │     │     └─ Change management log (security-relevant changes)
  │     ├─ Review previous audit findings and remediation status
  │     └─ Prepare customized audit checklist for vendor's processing
  │
  ├─► Step 3: Pre-Audit Review (Audit Team — 1 week before audit)
  │     ├─ Review all vendor-provided documentation
  │     ├─ Identify focus areas based on:
  │     │     ├─ Open findings from previous audits
  │     │     ├─ Changes in processing since last audit
  │     │     ├─ Certification scope changes
  │     │     └─ Any reported incidents or near-misses
  │     ├─ Prepare interview question sets
  │     └─ Finalize audit agenda and share with vendor
  │
  ├─► Step 4: Audit Execution (varies by type)
  │     ├─ Type 1 — Documentation Review:
  │     │     ├─ Systematic review against audit checklist
  │     │     ├─ Cross-reference certifications against DPA requirements
  │     │     └─ Document findings in working papers
  │     ├─ Type 2 — Remote Technical Audit:
  │     │     ├─ All Type 1 activities
  │     │     ├─ Video-conference interviews (privacy lead, security lead, operations)
  │     │     ├─ Screen-share walkthrough of:
  │     │     │     ├─ Access control configurations
  │     │     │     ├─ Encryption settings
  │     │     │     ├─ Monitoring dashboards
  │     │     │     └─ DSR handling workflow
  │     │     └─ Document findings with screenshots
  │     └─ Type 3 — On-Site Inspection:
  │           ├─ All Type 2 activities
  │           ├─ Physical facility inspection:
  │           │     ├─ Perimeter security and access controls
  │           │     ├─ Server room security
  │           │     ├─ Environmental controls
  │           │     └─ Clean desk compliance
  │           ├─ Personnel interviews
  │           └─ Document findings with photos (where permitted)
  │
  ├─► Step 5: Finding Analysis and Classification (Audit Team — 5 business days)
  │     ├─ Classify each finding:
  │     │     ├─ Critical: Immediate risk — 7-day remediation
  │     │     ├─ Major: Significant gap — 30-day remediation
  │     │     ├─ Minor: Control weakness — 90-day remediation
  │     │     └─ Observation: Improvement area — tracked
  │     ├─ Cross-reference findings against DPA obligations
  │     ├─ Identify root causes where possible
  │     └─ Draft remediation recommendations
  │
  ├─► Step 6: Audit Report (Audit Team Lead — 5 business days)
  │     ├─ Draft Audit Report containing:
  │     │     ├─ Executive summary with overall compliance assessment
  │     │     ├─ Scope and methodology
  │     │     ├─ Detailed findings by checklist area
  │     │     ├─ Finding severity distribution
  │     │     ├─ Remediation recommendations and timelines
  │     │     ├─ Comparison with previous audit (if applicable)
  │     │     └─ Appendices (evidence references, checklist results)
  │     ├─ Internal review by Privacy Team Lead
  │     └─ DPO review and approval
  │
  ├─► Step 7: Report Issuance and Vendor Response (2 weeks)
  │     ├─ Share audit report with vendor privacy contact
  │     ├─ Vendor has 10 business days to:
  │     │     ├─ Acknowledge findings
  │     │     ├─ Provide factual corrections (if any)
  │     │     └─ Submit remediation action plan with timelines
  │     └─ Privacy Team reviews and accepts vendor remediation plan
  │
  └─► Step 8: Remediation Tracking
        ├─ Enter all findings into remediation tracking system
        ├─ Set milestone reminders for each remediation deadline
        ├─ Collect and verify remediation evidence at deadlines
        ├─ Conduct verification audit for Critical findings (within 30 days of deadline)
        └─ Close findings only when evidence is satisfactory
```

## Workflow 2: Triggered Vendor Audit

```
TRIGGER: Compliance concern detected
  ├─ Vendor reports personal data breach
  ├─ Sub-processor change not properly notified
  ├─ Data subject complaint indicating vendor non-compliance
  ├─ Certification lapse detected
  ├─ Media report of vendor security incident
  │
  ├─► Step 1: Triage (Privacy Team — 1 business day)
  │     ├─ Assess severity and urgency of trigger
  │     ├─ Determine audit scope (focused on trigger area vs. full audit)
  │     └─ Select audit type based on urgency:
  │           ├─ Critical: Immediate remote audit + on-site within 2 weeks
  │           ├─ Major: Remote audit within 2 weeks
  │           └─ Standard: Accelerated documentation audit within 4 weeks
  │
  ├─► Step 2: Expedited Notification
  │     ├─ Notify vendor of triggered audit
  │     ├─ Shortened notification period (7 days or per DPA emergency provisions)
  │     └─ Request specific documentation related to trigger
  │
  ├─► Step 3: Focused Audit Execution
  │     ├─ Concentrate on trigger-related control areas
  │     ├─ Assess whether trigger indicates systemic weakness
  │     └─ Evaluate vendor's own response to triggering event
  │
  └─► Step 4: Findings and Escalation
        ├─ Issue focused audit report
        ├─ If systemic issues found: Escalate to DPO for vendor relationship review
        ├─ If isolated issue: Standard remediation tracking
        └─ Update vendor risk classification if warranted
```

## Workflow 3: Audit Finding Remediation Verification

```
TRIGGER: Remediation deadline reached for an audit finding
  │
  ├─► Step 1: Request Evidence (Privacy Team — at deadline)
  │     ├─ Contact vendor requesting remediation evidence
  │     ├─ Specify what evidence is needed (per finding record)
  │     └─ 5 business day response window
  │
  ├─► Step 2: Evidence Review
  │     ├─ Assess whether evidence demonstrates finding is remediated
  │     ├─ For Critical findings: Conduct verification audit (remote or on-site)
  │     └─ For Major/Minor: Document-based verification
  │
  ├─► Step 3: Decision
  │     ├─ Remediated: Close finding in tracking system
  │     ├─ Partially Remediated: Extend deadline with conditions
  │     └─ Not Remediated: Escalate to DPO; consider contractual remedies
  │
  └─► Step 4: Record
        ├─ Update finding record with verification outcome
        ├─ Update vendor risk score if applicable
        └─ Report to DPO (Critical and Major findings only)
```
