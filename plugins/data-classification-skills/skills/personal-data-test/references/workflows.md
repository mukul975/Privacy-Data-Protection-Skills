# Workflows — Personal Data Classification Test

## Workflow 1: Data Element Classification Assessment

### Purpose
Systematically classify each data element in an information system as personal data, non-personal data, or borderline requiring periodic review.

### Participants
- Data Protection Officer (DPO)
- System/Data Owner
- Privacy Analyst
- IT/Data Engineering Representative

### Process Flow

```
START: New data element identified (collection, derivation, or receipt)
  │
  ├─► Step 1: Document Data Element Properties
  │     - Field name, data type, format
  │     - Source: collected, derived, inferred, received
  │     - Volume and frequency
  │     - Retention period
  │     Output: Data element profile record
  │
  ├─► Step 2: Apply Art. 4(1) Four-Element Test
  │     2a. Is this "any information"? → Almost always YES
  │     2b. Does it "relate to" a natural person?
  │         - Content link: Is the information about a person?
  │         - Purpose link: Is it used to evaluate/influence a person?
  │         - Result link: Does processing impact a person's rights?
  │     2c. Is the person "identified or identifiable"?
  │         - Direct identification possible?
  │         - Indirect identification via combination?
  │         - Apply Breyer third-party knowledge test
  │         - Apply Recital 26 "reasonably likely" means test
  │     2d. Is the person a "natural person"? (Living individual)
  │     Output: Four-element assessment record
  │
  ├─► Step 3: Classification Decision
  │     IF all four elements satisfied → PERSONAL DATA
  │     IF clearly fails any element → NOT PERSONAL DATA
  │     IF uncertain on identifiability → BORDERLINE (go to Step 4)
  │     Output: Preliminary classification
  │
  ├─► Step 4: Borderline Assessment (if needed)
  │     4a. Identify all means of identification available to controller
  │     4b. Identify means available to reasonably motivated third parties
  │     4c. Assess cost, time, and technology required for identification
  │     4d. Consider anticipated technology over the retention period
  │     4e. Apply ICO "motivated intruder" test as supplementary check
  │     Output: Borderline assessment with documented reasoning
  │
  ├─► Step 5: DPO Review and Approval
  │     - DPO reviews the classification and supporting analysis
  │     - If special category indicators present, flag for Art. 9 review
  │     - DPO signs off or requests additional analysis
  │     Output: Approved classification
  │
  └─► Step 6: Record and Integrate
        - Update data inventory with classification label
        - Link to Art. 6 lawful basis (if personal data)
        - Link to Art. 9(2) condition (if special category)
        - Set review date (annual for borderline, biennial for clear)
        - Propagate classification to downstream systems
        Output: Updated data inventory entry
```

### SLA Targets for Vanguard Financial Services

| Step | Target Duration | Escalation |
|------|----------------|-----------|
| Step 1: Documentation | 2 business days | Data Owner |
| Step 2: Four-element test | 3 business days | Privacy Analyst |
| Step 3: Classification | 1 business day | Privacy Analyst |
| Step 4: Borderline assessment | 5 business days | DPO |
| Step 5: DPO review | 3 business days | Chief Privacy Officer |
| Step 6: Record and integrate | 2 business days | Data Engineering |
| **Total (clear cases)** | **8 business days** | — |
| **Total (borderline cases)** | **16 business days** | — |

## Workflow 2: Reclassification Trigger Process

### Purpose
Ensure data classifications remain accurate when circumstances change.

### Triggers for Reclassification Review

| Trigger | Example | Initiated By |
|---------|---------|-------------|
| New data partnership or sharing agreement | Vanguard enters data sharing arrangement with analytics vendor | Legal/Procurement |
| Technology change | New AI model can re-identify previously anonymous data | IT Security |
| Regulatory guidance update | EDPB issues new opinion on identifiability | DPO |
| Court ruling | CJEU or national court decision expanding personal data scope | Legal |
| Data breach involving the data type | Breach demonstrates identification risk was underestimated | Incident Response |
| Scheduled annual review | Borderline classifications reviewed per schedule | Privacy Analyst |

### Process Flow

```
TRIGGER EVENT detected
  │
  ├─► Step 1: Impact Scoping
  │     - Identify all data elements potentially affected
  │     - Prioritise by volume and sensitivity
  │     Output: Impacted data element list
  │
  ├─► Step 2: Reassessment
  │     - Re-run the four-element test for each impacted element
  │     - Consider new means of identification introduced by the trigger
  │     Output: Revised classification for each element
  │
  ├─► Step 3: Gap Analysis
  │     - Compare new classification to existing classification
  │     - Identify elements that changed from non-personal to personal
  │     - Identify elements that changed from personal to special category
  │     Output: Classification change register
  │
  ├─► Step 4: Remediation Planning
  │     - For newly classified personal data: establish lawful basis, update RoPA,
  │       update privacy notices, implement data subject rights mechanisms
  │     - For newly classified special category: establish Art. 9(2) condition,
  │       conduct DPIA if required, implement enhanced security measures
  │     Output: Remediation action plan with deadlines
  │
  └─► Step 5: Implementation and Verification
        - Execute remediation actions
        - DPO verifies compliance
        - Update data inventory and classification labels
        Output: Completed reclassification record
```

## Workflow 3: Breyer Test Application Protocol

### Purpose
Structured application of the CJEU Breyer ruling when assessing whether indirect identifiers constitute personal data.

### Process Flow

```
Indirect identifier detected (e.g., IP address, device ID, cookie)
  │
  ├─► Step 1: Identify All Holders of Complementary Data
  │     - Internal departments (IT, HR, Marketing, Customer Service)
  │     - Third-party processors (cloud providers, analytics services)
  │     - Third parties with independent data (ISPs, social media platforms)
  │     - Public sources (registries, directories, social media)
  │     Output: Complementary data holder inventory
  │
  ├─► Step 2: Assess Legal Means of Access
  │     For each holder identified in Step 1:
  │     - Contractual right to request data?
  │     - Legal obligation to share (e.g., court order, regulatory requirement)?
  │     - Existing data sharing agreement?
  │     - Legitimate interest or other lawful basis to request?
  │     Output: Legal access assessment per holder
  │
  ├─► Step 3: Assess Proportionality
  │     For each accessible complementary dataset:
  │     - Cost of obtaining and processing the additional data
  │     - Time required relative to the data retention period
  │     - Technical effort required
  │     - Motivation: Is there a realistic scenario where identification
  │       would be pursued? (commercial value, legal proceedings, curiosity)
  │     Output: Proportionality assessment
  │
  ├─► Step 4: Classification Decision
  │     IF legal means exist AND identification is not disproportionate
  │       → PERSONAL DATA (per Breyer)
  │     IF no legal means exist OR identification is genuinely disproportionate
  │       → NOT personal data for this controller (document reasoning)
  │     NOTE: Classification is controller-specific; the same data element
  │           may be personal data for one controller but not another
  │     Output: Breyer test classification with full reasoning
  │
  └─► Step 5: Document and Monitor
        - Record the full Breyer analysis in the classification file
        - Set review trigger: any new data partnership, legal authority change,
          or technology change that could alter the assessment
        Output: Documented Breyer assessment with monitoring plan
```
