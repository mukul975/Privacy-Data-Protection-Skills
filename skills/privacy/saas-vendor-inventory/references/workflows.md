# Workflows — SaaS Vendor Inventory

## Workflow 1: Shadow IT Discovery and Remediation

```
TRIGGER: CASB, DNS analysis, SSO log, or expense analysis detects unsanctioned SaaS application
  │
  ├─► Step 1: Detection and Logging (InfoSec / Privacy Team — 1 business day)
  │     ├─ Log detection in shadow IT register:
  │     │     ├─ Application name and vendor
  │     │     ├─ Detection method and date
  │     │     ├─ Estimated user count and departments
  │     │     └─ Preliminary data flow assessment
  │     └─ Classify urgency:
  │           ├─ Critical: Application likely processes special category or high-volume data
  │           ├─ Standard: Application processes standard personal data
  │           └─ Low: Application may not process personal data (investigation needed)
  │
  ├─► Step 2: Investigation (Privacy Team — 5 business days)
  │     ├─ Contact identified business unit users
  │     ├─ Determine:
  │     │     ├─ What personal data is being shared with the application
  │     │     ├─ How many data subjects are affected
  │     │     ├─ What processing purpose the application serves
  │     │     ├─ Whether alternatives exist among sanctioned applications
  │     │     └─ How long the application has been in use
  │     └─ Document findings
  │
  ├─► Step 3: Risk Assessment and Decision (Privacy Team Lead — 3 business days)
  │     ├─ Option A: SANCTION — Application needed, vendor acceptable
  │     │     ├─ Initiate formal vendor due diligence
  │     │     ├─ Execute DPA
  │     │     ├─ Add to sanctioned inventory (Tier 1)
  │     │     └─ Conduct retrospective privacy review
  │     │
  │     ├─ Option B: BLOCK — Unacceptable risk or sanctioned alternative exists
  │     │     ├─ Notify business unit of blocking decision with rationale
  │     │     ├─ Block application at network level (CASB/firewall)
  │     │     ├─ Request vendor data deletion if personal data was shared
  │     │     └─ Guide users to approved alternative
  │     │
  │     └─ Option C: INVESTIGATE FURTHER — Insufficient information
  │           ├─ Request vendor privacy documentation
  │           ├─ Conduct detailed data flow analysis
  │           └─ Re-evaluate within 10 business days
  │
  └─► Step 4: Documentation and Lessons Learned
        ├─ Update shadow IT register with outcome
        ├─ If breach of controller obligations identified:
        │     ├─ Assess whether data subject notification required
        │     └─ Document in incident register
        └─ Feed insights into procurement policy improvements
```

## Workflow 2: Quarterly Inventory Reconciliation

```
TRIGGER: Quarterly schedule (end of Q1, Q2, Q3, Q4)
  │
  ├─► Step 1: Data Collection (Privacy Team + InfoSec — 5 business days)
  │     ├─ Extract CASB discovery report (all detected SaaS applications)
  │     ├─ Extract SSO/IdP integration list (all OAuth/SAML connected apps)
  │     ├─ Extract procurement system active subscriptions
  │     ├─ Extract expense system recurring software charges
  │     └─ Compile into reconciliation dataset
  │
  ├─► Step 2: Reconciliation (Privacy Team — 5 business days)
  │     ├─ Match against current Tier 1 inventory
  │     ├─ Identify discrepancies:
  │     │     ├─ NEW: Applications in discovery data but not in inventory
  │     │     ├─ REMOVED: Applications in inventory but not in discovery data
  │     │     ├─ CHANGED: Applications with different usage patterns or integrations
  │     │     └─ EXPIRING: Contracts within 90-day expiry window
  │     └─ Classify each discrepancy
  │
  ├─► Step 3: Action Items
  │     ├─ NEW applications → Initiate Shadow IT Discovery workflow
  │     ├─ REMOVED applications → Verify proper termination and data deletion
  │     ├─ CHANGED applications → Assess if DPA amendment needed
  │     ├─ EXPIRING contracts → Initiate renewal privacy review
  │     └─ Update DPA status for all vendors
  │
  └─► Step 4: Reporting
        ├─ Produce Quarterly Inventory Reconciliation Report:
        │     ├─ Total sanctioned SaaS applications
        │     ├─ New applications added
        │     ├─ Applications removed
        │     ├─ Shadow IT instances detected and remediated
        │     ├─ DPA coverage rate (% of Tier 1 with executed DPA)
        │     └─ Contract status summary
        └─ Submit to DPO
```

## Workflow 3: New SaaS Application Procurement Privacy Gate

```
TRIGGER: Business unit submits procurement request for new SaaS application
  │
  ├─► Step 1: Privacy Screening (Privacy Team — 2 business days)
  │     ├─ Will the application process personal data?
  │     │     ├─ YES → Proceed to full privacy review
  │     │     └─ NO → Document determination; add to Tier 3; approve procurement
  │     └─ Initial risk classification based on intended use
  │
  ├─► Step 2: Privacy Review (if personal data processing)
  │     ├─ Vendor due diligence (per due diligence workflow)
  │     ├─ DPA negotiation (per DPA drafting workflow)
  │     ├─ Risk scoring (per risk scoring workflow)
  │     ├─ DPIA screening (if high-risk per Art. 35 criteria)
  │     └─ Transfer impact assessment (if vendor outside EEA)
  │
  ├─► Step 3: Privacy Gate Decision
  │     ├─ APPROVED: Privacy requirements met
  │     │     ├─ Add to Tier 1 inventory with all fields populated
  │     │     ├─ Configure monitoring per risk tier
  │     │     └─ Release procurement hold
  │     │
  │     ├─ APPROVED WITH CONDITIONS:
  │     │     ├─ Document conditions and deadlines
  │     │     ├─ Allow provisional procurement
  │     │     └─ Track condition fulfillment
  │     │
  │     └─ REJECTED:
  │           ├─ Document rejection rationale
  │           ├─ Suggest approved alternatives if available
  │           └─ Notify procurement to halt
  │
  └─► Step 4: Post-Deployment Verification (30 days after go-live)
        ├─ Verify data flows match approved scope
        ├─ Confirm SSO integration configured per security requirements
        ├─ Verify no additional personal data categories beyond approved scope
        └─ Update inventory with verified deployment details
```
