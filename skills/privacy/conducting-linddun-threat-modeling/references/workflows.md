# LINDDUN Threat Modeling Workflows

## Workflow 1: Full LINDDUN PRO Assessment

```
Step 1: Define Scope
├── Identify the system or processing activity to assess
├── Define the system boundary and trust boundaries
├── Identify all external entities (users, third parties, regulators)
├── Gather existing documentation (architecture diagrams, DPIA, Art. 30 records)
└── Assemble the assessment team (privacy engineer, architect, DPO representative)

Step 2: Create Data Flow Diagram
├── Model all external entities (data subjects, third-party services)
├── Model all processes (application logic, APIs, background jobs)
├── Model all data stores (databases, caches, logs, file systems)
├── Model all data flows (API calls, database queries, file transfers)
├── Draw trust boundaries (internal network, cloud, third-party)
└── Validate DFD with system architect for completeness

Step 3: Systematic Threat Identification
├── For each DFD element, evaluate all seven LINDDUN categories:
│   ├── L: Can items be linked? (data stores, flows)
│   ├── I: Can subjects be identified? (all elements)
│   ├── N: Is non-repudiation excessive? (processes, flows)
│   ├── D(etecting): Can existence be detected? (flows, stores)
│   ├── D(isclosure): Can data be disclosed? (stores, flows, processes)
│   ├── U: Are subjects sufficiently informed? (entities, processes)
│   └── N(compliance): Are regulations met? (all elements)
├── Use LINDDUN threat tree catalogs to enumerate specific threats
├── Document each identified threat with description and DFD element
└── Deduplicate and consolidate overlapping threats

Step 4: Risk Assessment
├── For each threat, assess:
│   ├── Likelihood (1-5): How probable is exploitation?
│   ├── Impact (1-5): What is the harm to data subjects?
│   └── Risk = Likelihood × Impact
├── Classify risks: Critical (20-25), High (12-19), Medium (6-11), Low (1-5)
├── Prioritize by risk score
└── Identify risk owners for each high/critical threat

Step 5: Mitigation Selection
├── Map each threat to privacy design patterns (Hoepman)
├── Select specific technical and organizational controls
├── For each mitigation:
│   ├── Document the control description
│   ├── Assign implementation owner
│   ├── Set implementation deadline
│   └── Define verification criteria
├── Assess residual risk after mitigation
└── Accept or escalate residual risks

Step 6: Documentation and Review
├── Produce LINDDUN assessment report
├── Include: DFD, threat register, risk matrix, mitigation plan
├── Review with DPO for completeness and risk acceptance
├── Integrate findings into DPIA (Article 35)
├── Update Article 30 records with threat mitigations
└── Schedule reassessment (annually or on significant system change)
```

## Workflow 2: LINDDUN GO (Agile/Lightweight)

```
Step 1: Preparation (30 minutes)
├── Sketch simplified DFD on whiteboard
├── Identify key data flows and storage points
├── Distribute LINDDUN GO threat cards to team
└── Brief team on the seven threat categories

Step 2: Card-Based Elicitation (60 minutes)
├── For each LINDDUN category card:
│   ├── Read the threat description aloud
│   ├── Each team member identifies applicable threats (sticky notes)
│   ├── Group similar threats
│   └── Dot-vote on highest-risk threats (3 votes per person)
├── Record top-voted threats per category
└── Take photos of whiteboard for documentation

Step 3: Rapid Risk Scoring (30 minutes)
├── For top-voted threats, quick assessment:
│   ├── High/Medium/Low likelihood
│   ├── High/Medium/Low impact
│   └── Priority: immediate / next sprint / backlog
├── Assign owners to high-priority items
└── Create user stories or tickets for mitigations

Step 4: Follow-Up
├── Transfer findings to threat register
├── Create implementation tickets in project tracker
├── Review mitigations in sprint retrospective
└── Schedule next LINDDUN GO session (quarterly)
```
