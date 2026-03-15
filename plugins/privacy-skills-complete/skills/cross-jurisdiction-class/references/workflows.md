# Workflows — Cross-Jurisdiction Classification

## Workflow 1: Multi-Jurisdiction Data Classification

```
START: Data element requires classification for multinational processing
  │
  ├─► Step 1: Determine Applicable Jurisdictions
  │     - Where are the data subjects located?
  │     - Where is the data processed and stored?
  │     - Which regulations have extraterritorial application?
  │     Output: List of applicable regulatory frameworks
  │
  ├─► Step 2: Classify Under Each Jurisdiction
  │     - GDPR: Personal / Special category / Criminal / Non-personal
  │     - CCPA: Personal information / Sensitive PI / Neither
  │     - HIPAA: PHI / Non-PHI (only if covered entity/BA involved)
  │     - LGPD: Personal / Sensitive / Non-personal
  │     - US State laws: Sensitive / Non-sensitive per applicable state
  │     Output: Per-jurisdiction classification
  │
  ├─► Step 3: Apply Highest Standard
  │     - Determine the most restrictive classification across jurisdictions
  │     - Map to unified tier (Public/Internal/Confidential/Restricted)
  │     Output: Unified classification tier
  │
  ├─► Step 4: Identify Per-Jurisdiction Obligations
  │     For each applicable jurisdiction, document:
  │     - Specific processing conditions (GDPR Art. 9(2), CCPA §1798.121)
  │     - Consent requirements (LGPD specific consent, CCPA opt-out)
  │     - Data subject rights (GDPR Arts. 15-22, CCPA §1798.100-125)
  │     - Transfer restrictions (GDPR Ch. V, LGPD Art. 33)
  │     Output: Per-jurisdiction obligations register
  │
  └─► Step 5: Document and Implement
        - Record unified classification and all jurisdictional obligations
        - Implement the most restrictive handling requirements
        - Configure DLP and access controls per unified tier
        - Set review trigger for regulatory changes in any jurisdiction
        Output: Multi-jurisdiction classification record
```

## Workflow 2: Regulatory Change Impact Assessment

```
START: New privacy law enacted or existing law amended in a relevant jurisdiction
  │
  ├─► Step 1: Scope Assessment
  │     - Does the change affect classification categories?
  │     - Does it introduce new sensitive data categories?
  │     - Does it change processing conditions?
  │
  ├─► Step 2: Mapping Update
  │     - Update the cross-regulation mapping matrix
  │     - Identify data elements affected by the change
  │     - Determine if any data requires reclassification
  │
  ├─► Step 3: Reclassification
  │     - Apply updated classifications to affected data
  │     - Escalate tier if new regulation is more restrictive
  │     - Update handling procedures if required
  │
  └─► Step 4: Implementation
        - Update automated classification rules
        - Update DLP policies
        - Train staff on changes
        - Document in classification policy change log
```
