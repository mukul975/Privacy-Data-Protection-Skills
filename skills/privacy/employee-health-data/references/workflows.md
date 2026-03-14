# Employee Health Data Workflows

## Workflow 1: Sickness Absence Data Flow

```
START: Employee reports sickness absence
│
├─ Days 1-7: Self-certification period
│  ├─ Employee notifies employer of absence (phone, email, app)
│  ├─ Employer records: absence start date, expected return
│  ├─ Employer does NOT request or record diagnosis
│  └─ Manager access: absence dates only
│
├─ Day 8+: Medical certification required
│  ├─ Employee provides fit note / medical certificate from GP
│  ├─ Fit note states: date range, fit/unfit/fit-with-adjustments
│  ├─ HR records: fit note dates, fit/unfit status, adjustments needed
│  ├─ HR does NOT enter diagnosis into HR system
│  └─ Manager access: absence dates + expected return + adjustments (no diagnosis)
│
├─ Week 4+: Occupational health referral (if appropriate)
│  ├─ HR drafts referral with specific questions (fitness, adjustments, return timeline)
│  ├─ Employee informed of referral and consents to OH assessment
│  ├─ OH professional conducts assessment
│  ├─ OH report to employer: fitness conclusion + functional adjustments
│  ├─ OH report does NOT include clinical diagnosis
│  └─ Employee receives copy of OH report before employer
│
└─ END: Employee returns to work. Absence recorded. Health details remain with OH provider.
```

## Workflow 2: Fitness-for-Work Referral

```
START: Concern about employee fitness for safety-critical role
│
├─ Step 1: Referral preparation
│  ├─ HR drafts referral letter with:
│  │  - Specific referral questions (fit for role? adjustments needed?)
│  │  - Employee's job description and physical requirements
│  │  - Relevant absence history (dates, not diagnoses)
│  ├─ HR does NOT include health information in referral
│  └─ Employee informed of referral and purpose
│
├─ Step 2: Employee rights
│  ├─ Employee may see the referral questions before assessment
│  ├─ Employee may request to see the OH report before employer (Access to Medical Reports Act 1988, UK)
│  ├─ Employee may request amendments to factual inaccuracies
│  └─ Employee may withhold consent (but employer may need to make decisions on available information)
│
├─ Step 3: OH assessment
│  ├─ OH professional examines employee
│  ├─ OH professional issues report addressing referral questions ONLY:
│  │  - Fit / Unfit / Fit with adjustments
│  │  - Specific functional adjustments (e.g., "no lifting above 10kg for 6 weeks")
│  │  - Anticipated return date (if currently absent)
│  └─ OH professional does NOT disclose diagnosis to employer
│
├─ Step 4: Employer action
│  ├─ Implement recommended adjustments
│  ├─ Record fitness conclusion in HR system (not diagnosis)
│  ├─ If unfit: manage absence per policy
│  └─ If fit with adjustments: monitor adjustment compliance
│
└─ END: Fitness assessed. Clinical data remains with OH provider.
```

## Workflow 3: Health Data Access Control Review

```
START: Quarterly review of health data access in HR system
│
├─ Step 1: Review access matrix
│  ├─ HR Manager: absence dates + fit/unfit + adjustments [Correct]
│  ├─ Line Manager: absence dates + expected return only [Verify no health fields visible]
│  ├─ Payroll: SSP-relevant absence dates only [Verify no health details]
│  ├─ DPO: audit access, no individual data [Verify]
│  ├─ IT: no health data access [Verify]
│  └─ Identify any role with inappropriate access → Remediate
│
├─ Step 2: Review audit logs
│  ├─ Any unusual access to health data fields? [Investigate]
│  ├─ Any bulk exports of health data? [Investigate]
│  └─ Document review findings
│
├─ Step 3: Review retention compliance
│  ├─ Standard absence records: within 2-year retention? [Verify]
│  ├─ OH records: within applicable retention (6 years standard / 40 years occupational)? [Verify]
│  ├─ COVID testing/vaccination data: deleted if basis expired? [Verify]
│  └─ Identify data past retention → Schedule deletion
│
└─ END: Access review documented. Remediation actions tracked to completion.
```
