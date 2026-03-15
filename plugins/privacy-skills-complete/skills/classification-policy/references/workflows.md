# Workflows — Data Classification Policy

## Workflow 1: New Data Classification

```
START: New data element, system, or processing activity identified
  │
  ├─► Step 1: Data Owner initiates classification
  │     - Identify the data element or dataset
  │     - Describe content, purpose, and data subjects
  │
  ├─► Step 2: Apply GDPR classification
  │     - Personal data test (Art. 4(1))
  │     - Special category check (Art. 9)
  │     - Criminal data check (Art. 10)
  │
  ├─► Step 3: Assign classification tier
  │     - Non-personal, anonymised → PUBLIC or INTERNAL
  │     - Personal data → CONFIDENTIAL (minimum)
  │     - Special category or criminal data → RESTRICTED
  │     - Commercially sensitive → CONFIDENTIAL or RESTRICTED
  │
  ├─► Step 4: Apply label
  │     - Apply metadata label via classification tool
  │     - Apply visual label (header/footer for documents)
  │     - Configure DLP policy association
  │
  ├─► Step 5: Configure handling controls
  │     - Implement per-tier controls (storage, access, encryption)
  │     - Verify compliance before data processing begins
  │
  └─► Step 6: Register in inventory
        - Add to data inventory with classification
        - Set review date
```

## Workflow 2: Classification Audit

```
START: Semi-annual audit schedule
  │
  ├─► Step 1: Sample selection
  │     - 100 items from each tier (random stratified sample)
  │     - Include items from automated discovery findings
  │
  ├─► Step 2: Classification verification
  │     - For each sampled item: Is the current label correct?
  │     - Is the data actually at the sensitivity level indicated?
  │     - Are under-classified items present? (higher sensitivity than label)
  │
  ├─► Step 3: Handling compliance check
  │     - For each sampled item: Are per-tier controls in place?
  │     - Storage location appropriate? Encryption active?
  │     - Access controls correctly configured?
  │
  ├─► Step 4: Findings and remediation
  │     - Document misclassified items
  │     - Reclassify and apply correct controls
  │     - Track remediation to completion
  │
  └─► Step 5: Report
        - Report findings to DPO and Privacy Steering Committee
        - Track classification accuracy metrics over time
        - Identify systemic issues for process improvement
```
