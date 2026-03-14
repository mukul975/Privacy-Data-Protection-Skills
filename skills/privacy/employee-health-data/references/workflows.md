# Employee Health Data Workflows

## Workflow 1: Sickness Absence Data Flow

```
START: Employee reports sickness absence
│
├─ Day 1-7: Self-certification
│  ├─ Employee notifies manager of absence (reason NOT required)
│  ├─ HR records: absence dates, type (sick leave)
│  └─ HR does NOT record diagnosis or symptoms
│
├─ Day 8+: Fit note / medical certificate required
│  ├─ Employee provides fit note from GP/treating physician
│  ├─ Fit note contains: date range, fit/unfit conclusion, recommended adjustments
│  ├─ HR records: fit note dates, fit/unfit status, adjustment requirements
│  └─ HR does NOT enter diagnosis into HR system (even if visible on certificate)
│
├─ Week 4+: Occupational health referral (optional)
│  ├─ Manager or HR offers OH referral (employee cooperation required)
│  ├─ Referral letter contains: specific questions about fitness and adjustments
│  ├─ Referral does NOT contain health information employer does not already hold
│  ├─ OH provider examines employee
│  ├─ OH report to employer: fit/unfit/fit with adjustments
│  ├─ OH report does NOT contain diagnosis (unless employee consents)
│  └─ Employee receives copy of report; may request amendments before release
│
└─ END: Employer holds absence dates and fitness conclusion only.
```

## Workflow 2: Fitness-for-Work Assessment

```
START: Safety-critical role or return from long-term absence
│
├─ Step 1: Referral
│  ├─ HR drafts referral with specific questions:
│  │  "Is the employee fit to [specific task]?"
│  │  "Are workplace adjustments required?"
│  ├─ Referral reviewed by DPO for data minimisation
│  └─ Employee informed of referral and purpose
│
├─ Step 2: Assessment
│  ├─ OH provider conducts assessment
│  ├─ Employee has right to see report before release (Access to Medical Reports Act 1988, UK)
│  └─ Employee may request factual amendments
│
├─ Step 3: Report to employer
│  ├─ Report contains: fitness conclusion, functional limitations, recommended adjustments, anticipated timeline
│  ├─ Report does NOT contain: diagnosis, treatment details, medication, prognosis
│  └─ Report stored in restricted health data section of HR system
│
├─ Step 4: Employment decision
│  ├─ Manager informed of fitness conclusion and adjustments only
│  ├─ Manager does NOT receive the OH report itself
│  └─ Adjustments implemented; review date set
│
└─ END: Fitness assessed. Data minimised. Access restricted.
```

## Workflow 3: Health Data Retention Review

```
START: Annual retention review or employee termination
│
├─ Step 1: Identify health data held
│  ├─ Absence records (dates and types)
│  ├─ Fit note records
│  ├─ OH referral correspondence
│  ├─ Fitness certificates
│  ├─ COVID testing/vaccination legacy data
│  └─ Disability adjustment records
│
├─ Step 2: Apply retention schedule
│  ├─ Standard absence records: 2 years current + 1 year archive → delete
│  ├─ OH records (standard employment): 6 years post-termination → delete
│  ├─ OH records (occupational health surveillance): 40 years (asbestos/radiation) → archive
│  ├─ COVID data: delete unless ongoing legal obligation
│  ├─ Disability adjustment records: duration of employment + 6 years → delete
│  └─ Wellness programme data: delete on withdrawal or termination
│
├─ Step 3: Execute deletion
│  ├─ Delete expired records from HR system
│  ├─ Verify deletion from backups within backup rotation period
│  ├─ Retain aggregate anonymised statistics where needed
│  └─ Document deletion in retention log
│
└─ END: Health data retention compliant. Schedule next review.
```
