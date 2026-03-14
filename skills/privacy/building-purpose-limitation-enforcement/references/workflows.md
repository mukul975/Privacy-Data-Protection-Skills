# Purpose Limitation Enforcement Workflows

## Workflow 1: Registering a New Processing Purpose

```
Step 1: Purpose Definition
├── Define the purpose in clear, specific language
├── Identify the lawful basis under Article 6(1)
├── List all personal data categories required for this purpose
├── Define the retention period and trigger event
└── Identify the data controller and responsible team

Step 2: Compatibility Mapping
├── Review existing purposes in the purpose registry
├── Identify purposes that are potentially compatible (shared context, linked goals)
├── Identify purposes that are incompatible (different context, unrelated goals)
├── Document the compatibility rationale for each relationship
└── Pre-populate compatible_purposes and incompatible_purposes fields

Step 3: DPO Review
├── Submit purpose registration to the Data Protection Office
├── DPO reviews lawful basis, data categories, and retention period
├── DPO reviews compatibility mappings for accuracy
├── DPO confirms that the purpose is "specified, explicit and legitimate" per Art. 5(1)(b)
└── DPO approves or requests revisions

Step 4: Technical Implementation
├── Create purpose entry in the purpose registry database
├── Configure purpose tag in the Purpose Tagging Gateway
├── Create OPA policies for purpose-based access control
├── Configure role-purpose authorization matrix entries
├── Set up retention automation linked to the purpose lifecycle
└── Deploy audit logging for all access under this purpose

Step 5: Verification
├── Test that data ingested under the new purpose receives correct purpose tags
├── Test that only authorized roles can access data under this purpose
├── Test that cross-purpose access without a compatibility assessment is blocked
├── Verify audit logs capture purpose context for every access event
└── Document verification results and archive in compliance records
```

## Workflow 2: Article 6(4) Compatibility Assessment

```
Step 1: Request Intake
├── Requesting team submits compatibility assessment request
├── Document: original purpose, proposed new purpose, business justification
├── Identify the data categories to be reprocessed
└── Assign the assessment to a DPO team member

Step 2: Factor Analysis
├── Factor (a) — Link between purposes:
│   ├── Is the new purpose a natural extension of the original?
│   ├── Were both purposes foreseeable at collection time?
│   └── Score: 1 (no link) to 5 (closely linked)
│
├── Factor (b) — Context of collection:
│   ├── What was the relationship between controller and data subject?
│   ├── What would the data subject reasonably expect?
│   └── Score: 1 (unexpected) to 5 (fully expected)
│
├── Factor (c) — Nature of data:
│   ├── Does the data include special categories (Article 9)?
│   ├── Does it include criminal conviction data (Article 10)?
│   └── Score: 1 (special category) to 5 (non-sensitive)
│
├── Factor (d) — Consequences:
│   ├── Could further processing cause material or non-material damage?
│   ├── Could it lead to discrimination, financial loss, or reputational damage?
│   └── Score: 1 (severe consequences) to 5 (minimal impact)
│
└── Factor (e) — Safeguards:
    ├── Is encryption or pseudonymization applied?
    ├── Are access controls purpose-restricted?
    └── Score: 1 (no safeguards) to 5 (comprehensive safeguards)

Step 3: Scoring and Decision
├── Calculate total score (range 5-25)
├── 20-25: Compatible — approve with standard documentation
├── 15-19: Potentially compatible — approve with additional safeguards
├── 10-14: Likely incompatible — escalate to DPO, consider DPIA
├── 5-9: Incompatible — deny, require new consent or separate lawful basis
└── Document decision rationale and any conditions

Step 4: Implementation (if approved)
├── Update the purpose registry with compatibility relationship
├── Configure OPA policy to allow cross-purpose access with conditions
├── Implement any required additional safeguards (pseudonymization, access logging)
├── Set review date for reassessment (maximum 12 months)
└── Notify requesting team of approval and conditions

Step 5: Monitoring
├── Track cross-purpose access volume and patterns
├── Review at scheduled reassessment date
├── Revoke compatibility if conditions change or violations occur
└── Report compatibility assessment outcomes in quarterly DPO report
```

## Workflow 3: Purpose Violation Incident Response

```
Step 1: Detection
├── Policy engine alerts on unauthorized cross-purpose access
├── OR: Audit review identifies access without valid purpose declaration
├── OR: Data subject complaint about unexpected use of their data
└── Log detection source, timestamp, and affected data records

Step 2: Containment
├── Immediately revoke the violating service's access to the affected purpose
├── Preserve audit logs for investigation
├── Notify the Data Protection Officer within 4 hours
└── If data was disclosed externally, assess breach notification under Art. 33/34

Step 3: Investigation
├── Determine root cause: configuration error, policy gap, or intentional misuse
├── Identify all data records accessed outside their authorized purpose
├── Identify all downstream systems that received the data
├── Assess the impact on data subjects
└── Document findings in incident report

Step 4: Remediation
├── Delete or quarantine data processed outside authorized purpose
├── Fix the root cause (policy update, access reconfiguration, training)
├── Implement additional technical controls to prevent recurrence
├── Update the purpose registry if a gap is identified
└── Conduct a post-incident review with affected teams

Step 5: Reporting
├── File internal incident report with DPO
├── If breach threshold is met, notify supervisory authority within 72 hours (Art. 33)
├── If high risk to data subjects, notify affected individuals (Art. 34)
├── Update the Article 30 Records of Processing Activities
└── Schedule follow-up review at 30 and 90 days post-incident
```
