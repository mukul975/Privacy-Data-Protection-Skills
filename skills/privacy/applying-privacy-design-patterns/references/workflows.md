# Privacy Design Pattern Workflows

## Workflow 1: Pattern Selection for a New System Design

```
Step 1: Processing Activity Analysis
├── Document the processing activity, purpose, and lawful basis
├── Identify all personal data categories involved
├── Map data flows (collection, processing, storage, sharing, deletion)
├── Identify data subjects and their expectations
└── Classify data sensitivity (direct identifiers, quasi-identifiers, special categories)

Step 2: GDPR Principle Mapping
├── For each GDPR principle (Art. 5), rate relevance to this activity (1-5)
├── Identify the primary GDPR risks (e.g., over-collection, purpose creep, unauthorized access)
├── Map risks to privacy design strategies using the principle-pattern matrix
└── Identify mandatory patterns (those addressing high-risk principles)

Step 3: Pattern Applicability Scoring
├── For each of the eight patterns, score applicability (1-5):
│   ├── MINIMIZE: Can data collection or retention be reduced?
│   ├── HIDE: Can data be encrypted, pseudonymized, or masked?
│   ├── SEPARATE: Can processing be distributed or isolated by purpose?
│   ├── ABSTRACT: Can data be aggregated or generalized?
│   ├── INFORM: How should data subjects be notified?
│   ├── CONTROL: What controls should data subjects have?
│   ├── ENFORCE: What policies need technical enforcement?
│   └── DEMONSTRATE: What compliance evidence is needed?
├── Identify the top 3-5 patterns for this activity
└── Document selection rationale

Step 4: Pattern Implementation Design
├── For each selected pattern, specify:
│   ├── Which sub-pattern(s) apply
│   ├── Where in the architecture the pattern is applied
│   ├── Technical implementation approach
│   ├── Responsible team
│   └── Verification criteria
├── Document in the system design specification
└── Review with DPO and security architecture team

Step 5: Implementation and Verification
├── Implement patterns in the system architecture
├── Verify each pattern against its criteria
├── Conduct privacy architecture review
├── Update DPIA with pattern analysis
└── Document in Article 30 records
```

## Workflow 2: Pattern-Based Privacy Architecture Review

```
Step 1: Inventory Existing Patterns
├── For each processing activity, identify currently implemented patterns
├── Map each pattern to the GDPR principle it addresses
├── Identify gaps: principles without corresponding pattern implementation
└── Document findings in pattern coverage matrix

Step 2: Gap Analysis
├── For each unaddressed GDPR principle:
│   ├── Determine the applicable privacy design pattern
│   ├── Assess implementation feasibility
│   ├── Estimate implementation effort
│   └── Prioritize by risk (likelihood × impact of principle violation)
├── Generate prioritized remediation backlog
└── Review with DPO for risk acceptance decisions

Step 3: Remediation Implementation
├── Execute remediation backlog in priority order
├── For each pattern implementation:
│   ├── Design the technical solution
│   ├── Implement and test
│   ├── Verify against pattern criteria
│   └── Document in architecture records
├── Update pattern coverage matrix
└── Re-run gap analysis to confirm closure

Step 4: Continuous Monitoring
├── Schedule quarterly pattern coverage reviews
├── Trigger review when new processing activities are added
├── Trigger review when system architecture changes
├── Include pattern analysis in DPIA updates
└── Report pattern coverage metrics to DPO
```
