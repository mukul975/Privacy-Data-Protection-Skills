# Audit Risk Assessment Workflows

## Workflow 1: Annual Privacy Audit Risk Assessment

```
Step 1: Risk Universe Update
├── Review the current privacy audit risk universe
├── Add new auditable entities (new processing activities, systems, vendors)
├── Remove decommissioned entities
├── Validate entity ownership and scope boundaries
└── Confirm entity list with DPO and business unit privacy leads

Step 2: Inherent Risk Scoring
├── For each auditable entity, score the following factors (1-5):
│   ├── Data Volume (weight: 20%)
│   ├── Data Sensitivity (weight: 25%)
│   ├── Regulatory Exposure (weight: 25%)
│   ├── Processing Complexity (weight: 15%)
│   └── External Sharing (weight: 15%)
├── Calculate weighted inherent risk score
├── Document scoring rationale and evidence
└── Peer-review scores for consistency across entities

Step 3: Control Effectiveness Evaluation
├── For each auditable entity:
│   ├── Identify existing privacy controls (policies, procedures, technical measures)
│   ├── Assess control design (does the control address the risk?)
│   ├── Assess control operation (is the control functioning as designed?)
│   └── Rate effectiveness: Effective (1), Partially Effective (2), Ineffective (3)
├── Use prior audit results, incident data, and management attestations as inputs
└── Document control gaps identified

Step 4: Residual Risk Calculation
├── Residual Risk = Inherent Risk Score × Control Effectiveness Score
├── Normalise to 1-5 scale
├── Map to risk rating: Low (1-2), Medium (2.1-3.5), High (3.6-4.5), Critical (4.6-5.0)
└── Generate risk heat map (likelihood × impact matrix)

Step 5: Risk Appetite Comparison
├── Compare residual risk ratings against organisational risk appetite
├── Flag entities exceeding risk appetite (requires management acceptance or additional controls)
├── Document risk acceptance decisions with approving authority
└── Escalate critical risks to board audit committee

Step 6: Audit Plan Development
├── Map audit frequency to residual risk rating:
│   ├── Critical → semi-annual audit + continuous monitoring
│   ├── High → annual audit
│   ├── Medium → biennial audit
│   └── Low → triennial audit or reliance on management self-assessment
├── Adjust for: prior audit findings, regulatory changes, management requests, incidents
├── Allocate audit resources (staff days, specialist skills, technology)
├── Develop detailed engagement timeline
└── Present draft audit plan to audit committee for approval

Step 7: Ongoing Monitoring
├── Track risk indicators between audits (incidents, complaints, regulatory changes)
├── Trigger ad-hoc risk reassessment for material events
├── Update risk scores quarterly for critical and high-risk entities
└── Report risk trends to audit committee quarterly
```

## Workflow 2: Control Effectiveness Testing

```
START: Evaluate control effectiveness for an auditable entity
│
├─ Step 1: Control identification
│  ├── List all controls mapped to the entity from the control register
│  └── Classify as preventive, detective, or corrective
│
├─ Step 2: Design effectiveness
│  ├── Does the control address the identified risk?
│  ├── Is the control documented in a policy or procedure?
│  ├── Are roles and responsibilities clearly assigned?
│  └── Design rating: Adequate / Inadequate
│
├─ Step 3: Operating effectiveness
│  ├── Has the control been executed consistently during the review period?
│  ├── Is there evidence of control execution (logs, approvals, reports)?
│  ├── Were any control failures or exceptions identified?
│  └── Operating rating: Consistent / Inconsistent / Not Operating
│
├─ Step 4: Overall effectiveness rating
│  ├── Design Adequate + Operating Consistent = Effective (1)
│  ├── Design Adequate + Operating Inconsistent = Partially Effective (2)
│  ├── Design Inadequate or Not Operating = Ineffective (3)
│  └── Document rating with supporting evidence
│
END: Return effectiveness score for residual risk calculation
```

## Workflow 3: Emerging Risk Identification

```
Step 1: Regulatory monitoring
├── Track new legislation and regulatory guidance (AI Act, new US state laws, UK reforms)
├── Assess impact on the existing risk universe
└── Add new auditable entities if required

Step 2: Incident analysis
├── Review privacy incidents and near-misses from the past quarter
├── Identify root causes and systemic control weaknesses
└── Adjust risk scores for affected entities

Step 3: Technology change assessment
├── Review new technology deployments (AI/ML, cloud migration, IoT)
├── Assess privacy implications and new risk vectors
└── Score new processing activities and add to risk universe

Step 4: Risk register update
├── Update risk scores based on emerging risk analysis
├── Present updated risk profile to DPO and audit committee
└── Adjust audit plan if priorities have shifted
```
