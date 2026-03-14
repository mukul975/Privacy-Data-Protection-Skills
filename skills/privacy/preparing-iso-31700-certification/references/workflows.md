# ISO 31700 Certification Workflows

## Workflow 1: ISO 31700 Gap Assessment

```
Step 1: Preparation
├── Assemble assessment team: DPO, privacy engineer, product manager, legal
├── Gather existing documentation: privacy policies, DPIAs, design documents
├── Identify all consumer-facing products and services in scope
├── Obtain copies of ISO 31700-1:2023 and ISO 31700-2:2023
└── Schedule assessment sessions (estimated: 5 days for medium organization)

Step 2: Phase 1 Assessment — Design (Req. 1-16)
├── For each requirement:
│   ├── Review the ISO 31700 requirement text
│   ├── Identify corresponding existing controls, processes, and documentation
│   ├── Interview responsible team members
│   ├── Assess evidence quality and completeness
│   ├── Score maturity (0-5 scale)
│   └── Document findings, gaps, and evidence references
├── Focus areas:
│   ├── Req. 1: Are privacy controls designed into the product?
│   ├── Req. 3: Is data collection minimized and proportionate?
│   ├── Req. 8: Are appropriate security measures in place?
│   ├── Req. 11: Is a privacy risk assessment conducted?
│   ├── Req. 12: Are data subject rights built into the design?
│   └── Req. 14: Are vulnerable consumers (children, elderly) considered?
└── Calculate Phase 1 average maturity score

Step 3: Phase 2 Assessment — Production (Req. 17-24)
├── For each requirement:
│   ├── Review operational procedures and evidence
│   ├── Verify training records, incident response plans, third-party contracts
│   ├── Score maturity and document findings
├── Focus areas:
│   ├── Req. 17: Are personnel trained on privacy?
│   ├── Req. 19: Is there a privacy breach management procedure?
│   ├── Req. 21: Are third parties managed for privacy compliance?
│   └── Req. 24: Are privacy controls monitored for effectiveness?
└── Calculate Phase 2 average maturity score

Step 4: Phase 3 Assessment — Disposal (Req. 25-30)
├── For each requirement:
│   ├── Review end-of-life procedures, disposal documentation
│   ├── Verify data portability and deletion capabilities
│   ├── Check supplier disposal obligations in contracts
│   └── Score maturity and document findings
├── Focus areas:
│   ├── Req. 27: Is PII securely deleted at end of life?
│   ├── Req. 28: Can consumers retrieve their data before disposal?
│   └── Req. 30: Are disposal activities documented?
└── Calculate Phase 3 average maturity score

Step 5: Report Generation
├── Compile gap assessment report with:
│   ├── Executive summary (overall maturity, critical gaps)
│   ├── Per-requirement scoring matrix
│   ├── Gap register (all requirements scoring below 3)
│   ├── Prioritized remediation roadmap
│   └── Resource and timeline estimates
├── Present findings to executive sponsor and DPO
└── Obtain approval for remediation budget and plan
```

## Workflow 2: Remediation Execution

```
Step 1: Remediation Planning
├── Prioritize gaps using risk-based approach:
│   ├── Priority 1: Critical gaps (score 0-1) affecting high-risk processing
│   ├── Priority 2: Foundation requirements (Req. 10, 11) enabling others
│   ├── Priority 3: Remaining gaps below certification threshold (score < 3)
│   └── Priority 4: Improvement opportunities (score 3 → 4)
├── Assign each remediation item to an owner with target completion date
├── Define evidence criteria for each remediation (what proves it is done)
└── Establish weekly progress tracking cadence

Step 2: Remediation Execution
├── Execute remediation items in priority order
├── For each item:
│   ├── Implement the required control, process, or documentation
│   ├── Collect evidence of implementation
│   ├── Verify evidence meets the requirement
│   └── Update the gap register with new maturity score
├── Conduct peer reviews for critical remediations
└── Escalate blockers to executive sponsor

Step 3: Evidence Package Assembly
├── For each requirement, compile:
│   ├── Policy or procedure document
│   ├── Implementation evidence (screenshots, logs, test results)
│   ├── Training records (where applicable)
│   ├── Monitoring metrics (where applicable)
│   └── Audit or review records
├── Organize evidence in a structured folder hierarchy matching ISO 31700 requirements
└── Cross-reference evidence to specific requirement clauses

Step 4: Internal Pre-Audit
├── Engage internal auditor (or qualified consultant) to review all 30 requirements
├── Auditor verifies evidence, interviews staff, observes processes
├── Auditor issues findings: conformities, minor non-conformities, observations
├── Address any non-conformities before external certification audit
└── Document pre-audit results and corrective actions
```

## Workflow 3: Certification Audit Process

```
Step 1: Certification Body Selection
├── Identify accredited certification bodies (ISO/IEC 17065 accredited)
├── Request proposals from 2-3 bodies
├── Evaluate: industry experience, audit team expertise, timeline, cost
├── Select certification body and sign engagement agreement
└── Schedule Stage 1 and Stage 2 audits

Step 2: Stage 1 Audit — Documentation Review
├── Certification body reviews documentation package
├── Auditor assesses: scope definition, management commitment, documentation completeness
├── Auditor identifies areas requiring clarification or additional evidence
├── Stage 1 report issued with readiness assessment
└── Address any findings before proceeding to Stage 2

Step 3: Stage 2 Audit — Implementation Audit
├── On-site (or remote) audit of implementation evidence
├── Auditor interviews: DPO, privacy engineers, product managers, support staff
├── Auditor observes: privacy controls in operation, consumer-facing privacy features
├── Auditor reviews: logs, metrics, incident records, training evidence
├── Auditor issues findings: conformities, non-conformities, observations
├── For major non-conformities: corrective action required before certification
├── For minor non-conformities: corrective action plan accepted
└── Certification decision by certification body's review committee

Step 4: Certification Maintenance
├── Annual surveillance audits (subset of requirements reviewed)
├── Recertification audit every 3 years (full assessment)
├── Maintain evidence package with ongoing updates
├── Report significant changes to certification body (new products, major incidents)
└── Continuous improvement: target maturity progression from Level 3 to Level 4-5
```
