# HIPAA Risk Analysis — Workflows

## Workflow 1: Enterprise-Wide Risk Analysis Process

```
Risk Analysis Initiation
│
├── Phase 1: Scoping and Planning (Weeks 1-2)
│   ├── Define scope: all ePHI in all forms and locations
│   ├── Identify assessment team and qualifications
│   ├── Select methodology (NIST 800-30, OCTAVE, FAIR)
│   ├── Establish timeline and resource allocation
│   ├── Obtain executive sponsorship
│   └── Communicate to department managers
│
├── Phase 2: Asset Inventory and Data Collection (Weeks 2-4)
│   ├── Conduct automated network discovery scans
│   ├── Review CMDB and system inventory
│   ├── Map data flows (ePHI creation, receipt, maintenance, transmission)
│   ├── Interview department managers and system administrators
│   ├── Inventory BA systems with ePHI access
│   ├── Document physical locations with ePHI
│   └── Classify assets by ePHI sensitivity and volume
│
├── Phase 3: Threat and Vulnerability Identification (Weeks 4-6)
│   ├── Review threat intelligence (HHS HC3, CISA, FBI IC3)
│   ├── Analyze organization-specific threat history
│   ├── Review vulnerability scan results (current and trending)
│   ├── Review penetration test findings
│   ├── Assess social engineering test results
│   ├── Evaluate physical security assessments
│   └── Document all identified threats and vulnerabilities
│
├── Phase 4: Current Controls Assessment (Weeks 5-7)
│   ├── Review existing administrative safeguards
│   ├── Review existing physical safeguards
│   ├── Review existing technical safeguards
│   ├── Assess control effectiveness through testing
│   ├── Identify control gaps
│   └── Document control status per asset/system
│
├── Phase 5: Risk Determination (Weeks 7-8)
│   ├── Assess likelihood for each threat/vulnerability pair
│   ├── Assess impact for each threat/vulnerability pair
│   ├── Calculate risk scores (Likelihood × Impact)
│   ├── Prioritize risks by score
│   └── Identify risks above acceptable threshold
│
├── Phase 6: Documentation (Week 8)
│   ├── Compile risk analysis report
│   ├── Create risk register with all identified risks
│   ├── Document methodology, assumptions, and limitations
│   ├── Include assessor qualifications
│   └── Obtain management sign-off
│
├── Phase 7: Risk Management Planning (Weeks 8-10)
│   ├── Develop mitigation plans for risks above threshold
│   ├── Assign ownership and timelines
│   ├── Identify resources required
│   ├── Obtain management approval for risk acceptance decisions
│   └── Integrate with security program roadmap
│
└── Phase 8: Ongoing Monitoring
    ├── Track mitigation plan implementation
    ├── Quarterly progress reviews
    ├── Trigger-based updates (new systems, incidents, threats)
    └── Annual comprehensive re-assessment
```

## Workflow 2: Risk Scoring and Prioritization

```
For Each Identified Threat/Vulnerability Pair:
│
├── Step 1: Determine Likelihood (1-5 scale)
│   ├── Threat source capability and motivation
│   ├── Vulnerability severity and exploitability
│   ├── Current control effectiveness
│   ├── Historical incident frequency
│   └── Threat intelligence indicators
│
├── Step 2: Determine Impact (1-5 scale)
│   ├── Number of individuals potentially affected
│   ├── Sensitivity of ePHI at risk
│   ├── Operational impact (clinical care disruption)
│   ├── Financial impact (fines, remediation, litigation)
│   └── Reputational impact
│
├── Step 3: Calculate Risk Score
│   └── Risk = Likelihood × Impact
│       ├── 20-25: Critical → Immediate action required
│       ├── 12-19: High → Action within 30 days
│       ├── 6-11: Medium → Action within 90 days
│       ├── 2-5: Low → Monitor in normal operations
│       └── 1: Minimal → Accept and document
│
└── Step 4: Risk Response Decision
    ├── Mitigate: Implement controls to reduce risk
    ├── Transfer: Insurance, BA contractual allocation
    ├── Accept: Document acceptance with management approval
    └── Avoid: Discontinue the activity creating the risk
```

## Workflow 3: Post-Incident Risk Analysis Update

```
Security Incident or Breach Occurred
│
├── Step 1: Immediate Assessment
│   ├── Was this threat/vulnerability in the current risk register?
│   │   ├── YES → Was the risk score accurate?
│   │   │   ├── YES → Were mitigation plans adequate but not yet implemented?
│   │   │   └── NO → Adjust likelihood and/or impact scores
│   │   └── NO → Add new threat/vulnerability to risk register
│   │
│   └── Were existing controls effective?
│       ├── YES → Incident exploited a gap between controls
│       └── NO → Control effectiveness rating must be downgraded
│
├── Step 2: Risk Register Update
│   ├── Update risk scores for affected threat/vulnerability pairs
│   ├── Add newly identified risks
│   ├── Re-evaluate related risks that may be similarly affected
│   ├── Update current controls assessment
│   └── Document lessons learned
│
├── Step 3: Mitigation Plan Revision
│   ├── Accelerate timelines for related mitigation plans
│   ├── Add new mitigation measures based on incident findings
│   ├── Re-prioritize risk register based on updated scores
│   └── Obtain updated management approval
│
└── Step 4: Communication
    ├── Update executive leadership on revised risk posture
    ├── Report to Board risk/audit committee if material change
    └── Update BA risk notifications if BA systems involved
```
