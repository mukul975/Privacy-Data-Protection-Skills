# Whistleblower Data Protection Workflows

## Workflow 1: Whistleblowing Report Processing

```
START: Report received through internal channel
│
├─ Step 1: Receipt and initial triage (within 7 days)
│  ├─ Designated person (Ethics/Compliance Officer) reviews report
│  ├─ Assign case reference number
│  ├─ Acknowledge receipt to reporter (anonymous: via platform; identified: directly)
│  ├─ Assess whether report falls within Directive scope
│  │  ├─ YES → Proceed to Step 2
│  │  └─ NO → Redirect to appropriate channel (HR grievance, etc.)
│  └─ Conduct initial data minimisation: delete manifestly irrelevant data per Art. 16(2)
│
├─ Step 2: Investigation planning
│  ├─ Determine scope of investigation
│  ├─ Identify investigation team members (need-to-know basis)
│  ├─ Grant case-specific access (revoked on case conclusion)
│  ├─ Assess whether to inform accused person
│  │  ├─ Would informing prejudice investigation? → Delay notification
│  │  └─ Evidence secured? → Inform accused (substance of allegations, not reporter identity)
│  └─ Document investigation plan
│
├─ Step 3: Investigation
│  ├─ Collect evidence (documents, interviews, system logs)
│  ├─ All data processed under purpose limitation: investigation only
│  ├─ Maintain strict confidentiality of reporter identity
│  ├─ If reporter identity becomes necessary for proceedings → Inform reporter first
│  └─ Provide feedback to reporter within 3 months per Directive Art. 9(1)(f)
│
├─ Step 4: Conclusion
│  ├─ Investigation outcome documented
│  ├─ If misconduct confirmed → Escalate to disciplinary / regulatory / criminal process
│  ├─ If no misconduct found → Close case and document reasoning
│  ├─ Inform reporter of outcome
│  └─ Inform accused of outcome
│
├─ Step 5: Retention
│  ├─ Apply retention period per national law:
│  │  - France: 2 months post-closure
│  │  - Germany: 3 years post-closure
│  │  - Spain: 3 months post-closure
│  │  - General: shortest applicable period
│  ├─ If legal proceedings initiated → Retain until proceedings + limitation period
│  ├─ Delete all copies, backups, references
│  └─ Maintain deletion log (metadata only)
│
└─ END: Case closed. Data deleted per schedule.
```

## Workflow 2: Accused Person Notification

```
START: Report names an identifiable accused person
│
├─ Step 1: Assess timing of notification
│  ├─ Would immediate notification prejudice the investigation?
│  │  ├─ Risk of evidence destruction → Delay
│  │  ├─ Risk of witness intimidation → Delay
│  │  ├─ Risk of obstruction → Delay
│  │  └─ No prejudice risk → Notify promptly
│  ├─ Legal basis for delay: Art. 14(5)(b) or Art. 23 GDPR
│  └─ Document the delay decision and reasoning
│
├─ Step 2: Content of notification
│  ├─ INFORM accused of:
│  │  - That allegations have been made
│  │  - Substance of the allegations (sufficient for accused to respond)
│  │  - That personal data is being processed for the investigation
│  │  - Their rights (access, rectification, restriction)
│  │  - The controller's identity
│  ├─ DO NOT inform accused of:
│  │  - Reporter identity
│  │  - Source of the report (unless required by judicial order)
│  │  - Identities of witnesses (unless trial rights require it)
│  └─ Document notification content and delivery method
│
├─ Step 3: Accused person rights
│  ├─ Right of access (Art. 15) → Provide investigation data about the accused
│  │  BUT redact reporter identity and witness identities
│  ├─ Right to rectification (Art. 16) → Allow correction of factual inaccuracies
│  ├─ Right to restriction (Art. 18) → Consider if processing contested
│  └─ Right to object (Art. 21) → Assess; investigation purpose may override
│
└─ END: Accused informed. Rights balanced against investigation integrity.
```

## Workflow 3: Conflict of Interest Routing

```
START: Report concerns a designated person or senior leader
│
├─ Report names the Ethics/Compliance Officer:
│  └─ Auto-route to Chair of Board Audit Committee or external ombudsperson
│
├─ Report names a Board member:
│  └─ Auto-route to external legal counsel or supervisory authority
│
├─ Report names the DPO:
│  └─ Temporarily assign GDPR oversight to external DPO or alternative internal officer
│
├─ Report names the CEO:
│  └─ Route to Chair of the Board or external legal counsel
│
└─ END: Conflict managed. Independent handling ensured.
```
