# EdTech Privacy Assessment Workflows

## Workflow 1: EdTech Platform Privacy Assessment

```
School or organisation evaluating an EdTech platform for deployment
│
├─ Step 1: Platform classification
│  ├─ Is the platform directed to children under 13? [Y/N]
│  ├─ Will it be used in a school-directed context? [Y/N]
│  ├─ Is it also available for home use outside school? [Y/N]
│  ├─ Does it operate in the US? [Y/N] → COPPA/FERPA apply
│  ├─ Does it operate in the EU/UK? [Y/N] → GDPR/AADC apply
│  └─ Document classification
│
├─ Step 2: Privacy policy review
│  ├─ Does the platform have a COPPA-compliant privacy policy? [Y/N]
│  ├─ Does the policy disclose all data collection practices? [Y/N]
│  ├─ Does the policy state data will not be used for advertising? [Y/N]
│  ├─ Does the policy state data will not be sold? [Y/N]
│  ├─ Does the policy describe deletion practices? [Y/N]
│  ├─ Does the policy name all third parties receiving data? [Y/N]
│  ├─ Is the Student Privacy Pledge signed? [Y/N]
│  └─ Score: [count of YES / 7]
│
├─ Step 3: Data mapping review
│  ├─ Request the platform's data collection inventory:
│  │  ├─ What data elements are collected from students?
│  │  ├─ How is each element collected (active input, passive tracking)?
│  │  ├─ What is the purpose of each element?
│  │  ├─ Who has access to each element?
│  │  ├─ Where is data stored (country, cloud provider)?
│  │  └─ What are retention periods for each element?
│  │
│  ├─ Assess data minimisation:
│  │  ├─ Is each element necessary for the educational purpose?
│  │  ├─ Could the educational purpose be achieved with less data?
│  │  └─ Is there any collection for non-educational purposes?
│  │
│  └─ Flag any concerns
│
├─ Step 4: Third-party and sub-processor review
│  ├─ Request list of all third parties receiving student data
│  ├─ For each third party:
│  │  ├─ What data do they receive?
│  │  ├─ What is the purpose?
│  │  ├─ Is there a data processing agreement?
│  │  ├─ Are they COPPA/GDPR compliant?
│  │  └─ Where do they process data?
│  │
│  └─ Reject platforms that share data with advertising networks
│
├─ Step 5: Security assessment
│  ├─ Encryption at rest? [Y/N]
│  ├─ Encryption in transit (TLS 1.2+)? [Y/N]
│  ├─ Access controls (RBAC)? [Y/N]
│  ├─ Regular security audits/penetration tests? [Y/N]
│  ├─ Incident response plan? [Y/N]
│  ├─ SOC 2 Type II certification? [Y/N]
│  └─ Score: [count of YES / 6]
│
├─ Step 6: Contractual requirements review
│  ├─ Does the proposed contract include:
│  │  ├─ Prohibition on commercial use of student data? [Y/N]
│  │  ├─ Prohibition on advertising to students? [Y/N]
│  │  ├─ Prohibition on selling student data? [Y/N]
│  │  ├─ Data deletion at end of contract and end of year? [Y/N]
│  │  ├─ Breach notification within 24-72 hours? [Y/N]
│  │  ├─ School audit rights? [Y/N]
│  │  ├─ Sub-processor disclosure and restrictions? [Y/N]
│  │  ├─ FERPA school official designation? [Y/N]
│  │  ├─ COPPA school exception acknowledgement? [Y/N]
│  │  └─ GDPR Art. 28 DPA (if EU/UK applicable)? [Y/N]
│  │
│  └─ Score: [count of YES / 10]
│
├─ Step 7: Overall assessment
│  ├─ Privacy policy: [score/7]
│  ├─ Data minimisation: [pass/fail]
│  ├─ Third-party sharing: [pass/fail]
│  ├─ Security: [score/6]
│  ├─ Contract: [score/10]
│  │
│  ├─ APPROVE: All sections pass/high score → Deploy with monitoring
│  ├─ CONDITIONAL: Some concerns → Require remediation before deployment
│  └─ REJECT: Significant concerns → Do not deploy
│
└─ Document assessment with date, assessor, and outcome
```

## Workflow 2: School Exception Consent Implementation

```
School deploys EdTech platform under COPPA school exception
│
├─ Step 1: School authorisation
│  ├─ School administrator reviews the platform's privacy practices
│  ├─ School administrator confirms the platform will be used for educational purposes only
│  ├─ School executes written agreement with the platform (see contractual requirements)
│  └─ School documents its authority to consent on behalf of parents
│
├─ Step 2: Parental notification (school responsibility)
│  ├─ School sends notice to parents:
│  │  ├─ Platform name and description
│  │  ├─ What data will be collected from students
│  │  ├─ How data will be used (educational purposes only)
│  │  ├─ That the school has authorised this on parents' behalf
│  │  ├─ Parents' rights to review and delete data
│  │  └─ Contact information for questions
│  │
│  ├─ Note: under the school exception, parental consent is NOT required
│  │  (the school consents on behalf of parents), but parents must be INFORMED
│  │
│  └─ If a parent objects:
│     ├─ School must provide alternative educational activities
│     ├─ Platform must not collect data from that student
│     └─ Student can participate without digital platform
│
├─ Step 3: Platform configuration for school deployment
│  ├─ Disable all non-educational features (advertising, social, gamification rewards)
│  ├─ Configure data collection to match school agreement scope only
│  ├─ Enable teacher dashboard for classroom management
│  ├─ Configure school administrator access for data oversight
│  ├─ Disable direct marketing communications to students
│  └─ Apply strictest data retention settings
│
├─ Step 4: Ongoing compliance monitoring
│  ├─ Quarterly: school reviews platform's data practices
│  ├─ Annually: school renews agreement and re-assesses privacy
│  ├─ Incident: immediate review if breach or complaint occurs
│  └─ End of contract: verify data deletion
│
└─ Document school exception implementation with dates and approvals
```

## Workflow 3: End-of-Year Data Lifecycle for EdTech

```
Academic year end approaching
│
├─ 60 days before year end:
│  ├─ Platform notifies school administrators:
│  │  "The academic year ends on [date]. Student data will be processed
│  │   according to the end-of-year protocol. Please confirm your preferences."
│  ├─ Provide options to school:
│  │  ├─ Export all student data (CSV, JSON, SIF format)
│  │  ├─ Retain specific data for returning students (opt-in per student)
│  │  ├─ Delete all data at year end (default)
│  │  └─ Custom retention for specific data categories
│  └─ School administrator confirms preferences
│
├─ 30 days before year end:
│  ├─ Notify teachers:
│  │  "Student data will be archived on [date]. Please complete any
│  │   end-of-year assessments and download reports by then."
│  ├─ Generate end-of-year student progress reports
│  ├─ Export reports to school's designated storage
│  └─ Notify parents:
│     "Your child's learning data from [Platform] for this year will be
│      deleted on [date]. Download your child's progress report from your
│      parent dashboard."
│
├─ Year end (last day of academic year):
│  ├─ Deactivate all student accounts for the ending year
│  ├─ Move data to deletion queue
│  ├─ Retain only:
│  │  ├─ Data school has explicitly authorised for retention
│  │  ├─ Aggregate anonymised statistics (for platform improvement)
│  │  └─ School agreement and deletion log (for compliance)
│  └─ Disable teacher access to ended-year data
│
├─ 30 days after year end:
│  ├─ Execute deletion of all data in deletion queue
│  ├─ Deletion scope:
│  │  ├─ Primary database records
│  │  ├─ File storage (assignments, uploads)
│  │  ├─ Search indices
│  │  ├─ Analytics databases
│  │  ├─ Application logs containing student data
│  │  └─ Cache entries
│  ├─ Generate deletion certificate for the school
│  └─ Send certificate to school administrator
│
├─ 60 days after year end:
│  ├─ Purge backups containing deleted student data
│  ├─ Verify deletion across all systems
│  ├─ Send final confirmation to school:
│  │  "All student data from the [year] academic year has been permanently
│  │   deleted. Deletion certificate attached."
│  └─ Retain only: deletion certificate, school agreement, anonymised aggregates
│
└─ Log all lifecycle events for compliance audit trail
```

## Workflow 4: Parental Rights Request Processing (EdTech Context)

```
Parent requests access to or deletion of their child's data
│
├─ Step 1: Determine request type and authority
│  ├─ Is this a school-directed deployment? [Y/N]
│  │  ├─ YES → Both COPPA parental rights and FERPA parental rights apply
│  │  │  Parent may contact either the school or the platform
│  │  └─ NO → Full COPPA applies; parent contacts platform directly
│  │
│  ├─ Request type:
│  │  ├─ ACCESS: Parent wants to review data held about their child
│  │  ├─ DELETE: Parent wants data deleted
│  │  ├─ OPT-OUT: Parent wants to stop further data collection
│  │  └─ CORRECT: Parent wants to correct inaccurate data
│
├─ Step 2: Verify identity
│  ├─ If parent has existing account → verify via account credentials
│  ├─ If parent contacts via school → verify through school administrator
│  └─ If parent contacts platform directly without account → verify per original consent method
│
├─ Step 3: Process request
│  ├─ ACCESS:
│  │  ├─ Compile all personal data held about the child
│  │  ├─ Present to parent via dashboard or email (secure)
│  │  ├─ Timeline: within 30 days (GDPR) / reasonable time (COPPA)
│  │  └─ If school-directed: coordinate with school per FERPA
│  │
│  ├─ DELETE:
│  │  ├─ Identify scope of data to be deleted
│  │  ├─ If school-directed: notify school that parent has requested deletion
│  │  ├─ Execute deletion within 30 days
│  │  ├─ Confirm deletion to parent
│  │  └─ Note: school may need to provide alternative educational access
│  │
│  ├─ OPT-OUT:
│  │  ├─ Stop further collection from the child
│  │  ├─ If school-directed: notify school; school provides alternative
│  │  ├─ Deactivate child's account
│  │  └─ Confirm to parent
│  │
│  └─ CORRECT:
│     ├─ Identify the inaccurate data
│     ├─ Correct as requested
│     ├─ Confirm correction to parent
│     └─ Notify school if school-directed
│
└─ Step 4: Log and report
   ├─ Log request, verification, action taken, timeline
   └─ Include in quarterly compliance report
```
