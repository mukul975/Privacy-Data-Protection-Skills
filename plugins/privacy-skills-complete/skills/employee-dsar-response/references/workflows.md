# Employee DSAR Response Workflows

## Workflow 1: Employee DSAR Processing Timeline

```
DAY 1: Receipt and Acknowledgment
├─ Log DSAR in central register (unique reference: DSAR-EMP-[YEAR]-[SEQ])
├─ Verify employee identity (current employee: employment relationship confirms identity)
├─ Send acknowledgment: confirm receipt, expected response date (30 days)
└─ Assign DSAR coordinator from privacy/DPO team

DAYS 2-5: Scoping
├─ Review request: all data, or specific categories?
├─ If unclear, contact employee to clarify scope
├─ Map request to data source inventory (see comprehensive list in SKILL.md)
├─ Issue collection instructions to data custodians
├─ Assess whether extension is likely needed
└─ If extension needed: notify employee within first month with reasons

DAYS 5-20: Collection
├─ Each custodian searches assigned systems
├─ Email: search employee mailbox + manager mailbox + HR BP mailbox
├─ CCTV: request specific dates/locations from employee if needed
├─ Paper files: retrieve physical personnel file
├─ Monitoring data: extract from monitoring systems
├─ Log all collected data: source, custodian, date, volume
└─ Escalate any access difficulties to DSAR coordinator

DAYS 15-25: Review and Redaction
├─ Review all data for employee's personal data
├─ Identify third-party data → Redact per framework (see SKILL.md)
├─ Identify privileged material → Route to legal counsel for review
├─ Identify exemption candidates → Assess per framework
├─ Compile disclosure package
└─ Create privilege log for withheld documents

DAYS 25-30: Quality Check and Dispatch
├─ DPO / senior privacy officer reviews disclosure
├─ Verify completeness: all data sources searched?
├─ Verify redaction: third-party data properly redacted?
├─ Verify privilege: privilege log complete?
├─ Prepare covering letter (scope, exemptions, complaints right)
├─ Deliver via secure channel (encrypted email / secure portal)
└─ Log completion in DSAR register
```

## Workflow 2: Third-Party Data Redaction Decision Tree

```
START: Document contains personal data of someone other than the requestor
│
├─ Is the third party's identity already known to the requestor?
│  ├─ YES (e.g., their line manager) → Generally may disclose without redaction
│  └─ NO → Continue assessment
│
├─ Has the third party consented to disclosure?
│  ├─ YES → Disclose without redaction
│  └─ NO → Continue assessment
│
├─ Is it reasonable to disclose without consent?
│  ├─ Consider:
│  │  - Nature of the third-party data
│  │  - Third party's reasonable expectations
│  │  - Whether the requestor needs the third-party data to understand their own data
│  │  - Whether the third party would object
│  ├─ REASONABLE → Disclose (document reasoning)
│  └─ NOT REASONABLE → Redact the third-party data
│
├─ Redaction technique:
│  ├─ Replace names with "Person A," "Person B" (consistent throughout)
│  ├─ Redact email addresses, phone numbers, job titles that could identify
│  ├─ Use permanent redaction (not highlight or track-changes)
│  └─ Do NOT redact the requestor's own data
│
└─ END: Document redaction decisions in the DSAR file.
```

## Workflow 3: Legal Privilege Assessment

```
START: Document potentially subject to legal professional privilege
│
├─ Step 1: Route to legal counsel for review
│
├─ Step 2: Legal counsel assesses:
│  ├─ Legal advice privilege?
│  │  ├─ Confidential communication between client and lawyer?
│  │  ├─ For the purpose of obtaining or giving legal advice?
│  │  └─ If BOTH yes → Privileged. Withhold.
│  │
│  ├─ Litigation privilege?
│  │  ├─ Created for the dominant purpose of litigation?
│  │  ├─ Litigation in progress or reasonably anticipated?
│  │  └─ If BOTH yes → Privileged. Withhold.
│  │
│  └─ Without prejudice privilege?
│     ├─ Communication in genuine attempt to settle dispute?
│     └─ If yes → Privileged. Withhold.
│
├─ Step 3: Partial privilege?
│  ├─ If only part of document is privileged → Disclose non-privileged portion
│  └─ Redact privileged content only
│
├─ Step 4: Record in privilege log:
│  ├─ Document reference number
│  ├─ Date of document
│  ├─ Type of privilege claimed
│  ├─ Brief description (without revealing privileged content)
│  └─ Reviewed by [legal counsel name and date]
│
├─ Step 5: Covering letter to employee:
│  ├─ State that certain information has been withheld under legal privilege
│  ├─ Do NOT reveal the privileged content
│  └─ Advise of right to complain to supervisory authority
│
└─ END: Privilege assessment documented. Privileged material withheld.
```
