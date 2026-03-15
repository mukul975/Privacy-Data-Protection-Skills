# COPPA Compliance Workflows

## Workflow 1: COPPA Applicability Determination

```
New online service or feature under development
│
├─ Is the service a website, app, or online service operated for commercial purposes?
│  ├─ NO → COPPA does not apply. Document determination.
│  └─ YES → Continue assessment.
│
├─ Is the service directed to children under 13?
│  ├─ Evaluate totality of circumstances:
│  │  □ Subject matter appeals to children
│  │  □ Visual content (animated characters, bright colours, cartoon style)
│  │  □ Child-oriented activities or games
│  │  □ Music or audio designed for children
│  │  □ Age of models or actors in promotional material
│  │  □ Presence of child celebrities or influencers
│  │  □ Ads on the service are directed to children
│  │  □ Listed in app store children's categories
│  │  □ Competent evidence of actual child audience
│  │
│  ├─ YES (directed to children) → COPPA applies to ALL users. Proceed to Workflow 2.
│  ├─ MIXED AUDIENCE → COPPA applies to child users. Implement age screen. Proceed to Workflow 3.
│  └─ NO (not directed to children) → Continue assessment.
│
├─ Does the operator have actual knowledge of collecting from children under 13?
│  ├─ YES → COPPA applies. Proceed to Workflow 2.
│  └─ NO → COPPA does not apply. Document determination.
│     NOTE: "Actual knowledge" includes information that would lead a reasonable person
│     to conclude the service is collecting from children. A non-neutral age gate that
│     reveals the threshold can establish constructive knowledge.
│
└─ Document the COPPA applicability determination with date, analysis, and reviewer.
```

## Workflow 2: Full COPPA Compliance Implementation

```
COPPA applies to the service
│
├─ Step 1: Privacy Notice (Section 312.4)
│  ├─ Draft online notice per Section 312.4(b):
│  │  ├─ Operator name, address, email, and phone number
│  │  ├─ Types of personal information collected from children
│  │  ├─ How information is collected (active vs. passive)
│  │  ├─ How information is used
│  │  ├─ Whether information is disclosed to third parties
│  │  ├─ Parental rights (review, delete, refuse further collection)
│  │  └─ Procedures for exercising parental rights
│  │
│  ├─ Post notice prominently on home page and each collection point
│  │
│  └─ Prepare direct notice template per Section 312.4(c):
│     ├─ Statement that operator collected parent's contact info for consent purposes
│     ├─ Operator's information practices
│     ├─ Statement that contact info will be deleted if no response
│     ├─ Link to online notice
│     └─ Means for parent to provide consent
│
├─ Step 2: Verifiable Parental Consent (Section 312.5)
│  ├─ Select consent method based on data use:
│  │  ├─ INTERNAL USE ONLY → Email Plus (Method 7) acceptable
│  │  ├─ THIRD-PARTY DISCLOSURE → Method 1-6 required
│  │  └─ PUBLIC POSTING → Method 1-6 required
│  │
│  ├─ Implement selected consent method (see SKILL.md for method details)
│  ├─ Build consent collection and storage system
│  └─ Test consent flow end-to-end
│
├─ Step 3: Parental Access (Section 312.6)
│  ├─ Build parental dashboard or access mechanism:
│  │  ├─ Parent can view all personal information collected from their child
│  │  ├─ Parent can request deletion of specific data or entire account
│  │  ├─ Parent can refuse further collection and use
│  │  └─ Verification required before granting access
│  │
│  └─ Document access request procedures
│
├─ Step 4: Data Minimisation (Section 312.7)
│  ├─ Audit all data collection against stated purposes
│  ├─ Remove any collection that is not reasonably necessary
│  ├─ Confirm that service access is not conditioned on excess collection
│  └─ Document data minimisation assessment
│
├─ Step 5: Security (Section 312.8)
│  ├─ Implement reasonable security measures:
│  │  ├─ Encryption at rest (AES-256) and in transit (TLS 1.3)
│  │  ├─ Access controls (RBAC, principle of least privilege)
│  │  ├─ Regular security assessments and penetration testing
│  │  ├─ Incident response procedures
│  │  └─ Staff training on COPPA and security requirements
│  │
│  └─ Document security program
│
├─ Step 6: Data Retention (Section 312.10)
│  ├─ Define retention periods for each data category
│  ├─ Implement automated deletion at retention expiry
│  ├─ Verify deletion across all systems including backups
│  └─ Document retention schedule
│
└─ Step 7: Ongoing Compliance
   ├─ Annual COPPA audit (see SKILL.md audit checklist)
   ├─ Quarterly privacy notice review
   ├─ Annual staff training
   ├─ Monitor FTC enforcement actions and guidance updates
   └─ Safe harbor membership renewal (if applicable)
```

## Workflow 3: Mixed-Audience Service Age Screening

```
Service determined to be mixed-audience (children and adults)
│
├─ Implement neutral age screen before any data collection:
│  ├─ "What is your date of birth?" with scrollable date picker
│  ├─ No indication of the age threshold
│  ├─ No immediate feedback on age gate outcome
│  └─ Cookie-based lockout on failure (24-hour minimum)
│
├─ User age calculated from date of birth
│
├─ Age >= 13?
│  ├─ YES → Standard (non-COPPA) data collection and processing
│  │         ├─ Apply standard privacy policy
│  │         ├─ Standard consent mechanisms
│  │         └─ No parental consent required under COPPA
│  │
│  └─ NO → Full COPPA protections apply
│           ├─ Direct notice sent to parent (312.4(c))
│           ├─ Verifiable parental consent obtained (312.5)
│           ├─ Limited data collection (312.7)
│           ├─ Parental access enabled (312.6)
│           └─ Child-specific retention limits applied (312.10)
│
└─ Log age screening decision for audit trail
```

## Workflow 4: COPPA School Exception Implementation

```
School requests to deploy service for classroom use
│
├─ Step 1: Verify school exception eligibility
│  ├─ Is the collection solely for educational purposes? → Must be YES
│  ├─ Will the operator use data for any commercial purpose? → Must be NO
│  ├─ Will data be disclosed to non-school third parties? → Must be NO
│  ├─ Has the school authorised the specific data collection? → Must be YES
│  │
│  ├─ All conditions met → School exception applies. Proceed.
│  └─ Any condition NOT met → Full COPPA applies. Obtain direct parental consent.
│
├─ Step 2: Execute school agreement
│  ├─ Written agreement documenting:
│  │  ├─ Specific data elements to be collected
│  │  ├─ Educational purposes for each data element
│  │  ├─ Prohibition on commercial use
│  │  ├─ Prohibition on third-party disclosure (except to school)
│  │  ├─ Data security requirements
│  │  ├─ Deletion obligations (end of year and end of contract)
│  │  ├─ Breach notification timeline (24 hours)
│  │  └─ School's confirmation of authority to consent on behalf of parents
│  │
│  └─ Retain executed agreement for audit
│
├─ Step 3: Deploy with school-authorised configuration
│  ├─ Disable all non-educational features (advertising, social, gamification rewards)
│  ├─ Configure data collection to match school agreement scope
│  ├─ Enable teacher dashboard for classroom management
│  ├─ Disable direct parent consent flow (school has consented)
│  └─ Enable parental information mechanism (school informs parents of use)
│
├─ Step 4: End-of-year data lifecycle
│  ├─ 60 days before year end: notify school of impending data deletion
│  ├─ 30 days before year end: provide data export to school
│  ├─ Year end: deactivate student accounts
│  ├─ 30 days after year end: delete all student data
│  └─ 60 days after year end: purge backups; provide deletion certificate
│
└─ Step 5: Annual compliance verification
   ├─ Verify school agreement is current
   ├─ Audit data collection against school agreement scope
   ├─ Confirm no commercial use of school-authorised data
   └─ Document compliance verification outcome
```

## Workflow 5: COPPA Parental Deletion Request

```
Parent requests deletion of child's personal information
│
├─ Step 1: Verify requester identity
│  ├─ Parent has existing account → verify via account credentials
│  ├─ Parent has no account → verify via same method used for original consent
│  └─ If verification fails → request alternative identification
│
├─ Step 2: Identify child's data
│  ├─ Locate all personal information associated with the child
│  ├─ Scope: account data, activity logs, content, communications, analytics
│  └─ Present summary to parent for confirmation
│
├─ Step 3: Execute deletion
│  ├─ Offer parent the option to download data before deletion
│  ├─ Delete from all primary systems
│  ├─ Schedule backup purge within rotation cycle
│  ├─ Notify any third parties that received the data
│  └─ Terminate further collection from the child
│
├─ Step 4: Confirm to parent
│  ├─ Send deletion confirmation with scope summary
│  ├─ Confirm that further collection has ceased
│  └─ Provide contact information for future questions
│
└─ Step 5: Log deletion for audit
   ├─ Deletion reference number
   ├─ Requester identity and verification method
   ├─ Scope of deletion
   ├─ Completion timestamp
   └─ Backup purge scheduled date
```
