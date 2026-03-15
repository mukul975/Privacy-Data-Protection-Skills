# Workflows — Texas TDPSA

## Workflow 1: TDPSA Applicability Determination

```
START: Determine if TDPSA applies to organization
  │
  ├─► Step 1: Business Nexus
  │     ├─ Conducts business in Texas? OR
  │     └─ Produces products/services consumed by Texas residents?
  │
  ├─► Step 2: Data Processing Check
  │     └─ Processes or engages in sale of personal data of Texas residents?
  │
  ├─► Step 3: Entity Exemption Check
  │     ├─ State agency or political subdivision? → EXEMPT
  │     ├─ GLBA-covered financial institution? → EXEMPT
  │     ├─ HIPAA covered entity or business associate? → EXEMPT
  │     ├─ Nonprofit organization? → EXEMPT
  │     ├─ Institution of higher education? → EXEMPT
  │     └─ ERCOT electric utility? → EXEMPT
  │
  ├─► Step 4: Small Business Check
  │     ├─ Determine NAICS code for primary business activity
  │     ├─ Look up SBA size standard for that NAICS code (13 CFR §121.201)
  │     ├─ Compare annual receipts or employee count to threshold
  │     ├─ If small business: Most TDPSA provisions exempt
  │     │     └─ BUT: §541.107(b) prohibition on selling sensitive data still applies
  │     └─ If NOT small business: Full TDPSA applies
  │
  └─► Step 5: Document Determination
        ├─ Record nexus basis, exemption analysis, SBA determination
        └─ Review annually or upon material change
```

## Workflow 2: Consumer Rights Request Processing

```
START: Texas consumer submits rights request
  │
  ├─► Step 1: Log and Classify
  │     ├─ Assign: TX-REQ-YYYY-NNNNN
  │     ├─ Right: Access / Correct / Delete / Portability / Opt-Out
  │     └─ Day 0 of 45-day clock
  │
  ├─► Step 2: Authenticate
  │     └─ Commercially reasonable verification
  │
  ├─► Step 3: Process (45 days, extensible by 45)
  │     ├─ Access: Compile data, categories, sources, purposes, recipients
  │     ├─ Correct: Update records, propagate to processors
  │     ├─ Delete: Cascading deletion, notify processors
  │     ├─ Portability: Generate portable export
  │     └─ Opt-Out: Apply preferences for targeted ads, sale, profiling
  │
  ├─► Step 4: Respond
  │     ├─ Fulfill or deny with basis
  │     ├─ Inform of appeal right
  │     └─ At least one free response per 12 months
  │
  └─► Step 5: Appeal (if filed)
        ├─ Respond within 60 days
        ├─ If denied: inform of right to contact Texas AG
        └─ AG contact: texasattorneygeneral.gov
```

## Workflow 3: Data Broker Registration Check

```
START: Annual review of data broker status
  │
  ├─► Step 1: Assess Principal Revenue Source
  │     ├─ Is principal revenue from collecting, processing, or transferring
  │     │   personal data NOT directly collected from consumers?
  │     ├─ Liberty Commerce Inc.: Principal revenue is e-commerce sales
  │     └─ Determination: NOT a data broker
  │
  ├─► Step 2: If Data Broker:
  │     ├─ Register with Texas Secretary of State (§541.202)
  │     ├─ Pay registration fee
  │     ├─ Disclose: legal name, address, contact, practices, breach history
  │     ├─ Provide clear data broker disclosure to consumers
  │     ├─ Implement consumer opt-out mechanism
  │     └─ Renew registration annually
  │
  └─► Step 3: If NOT Data Broker:
        ├─ Document determination with reasoning
        └─ Review annually if business model changes
```
