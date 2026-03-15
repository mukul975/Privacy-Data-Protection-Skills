# Workflows — Managing Consent for Children

## Workflow 1: Age Gate and Parental Consent Collection

```
START: New user begins CloudVault SaaS Inc. registration
  │
  ├─► Step 1: Collect date of birth
  │     ├─ Display: "Enter your date of birth"
  │     ├─ Input: date picker (day/month/year)
  │     └─ Do NOT store DOB if user is above all applicable thresholds
  │         (data minimization per Art. 5(1)(c))
  │
  ├─► Step 2: Determine age and applicable threshold
  │     ├─ Calculate age from DOB
  │     ├─ Determine user's country (from registration country selection)
  │     └─ Look up age threshold for that country
  │
  ├─► IF age >= threshold:
  │     ├─ Proceed with standard adult consent flow
  │     └─ Do not store DOB (not needed; only age-above-threshold fact retained)
  │
  └─► IF age < threshold:
        │
        ├─► Step 3: Display child-friendly notice
        │     "Welcome! Because you're under [threshold] in [country],
        │      we need a parent or guardian to set up your account.
        │      Please ask your parent or guardian to help you."
        │
        ├─► Step 4: Collect parent/guardian contact information
        │     ├─ Parent's name
        │     ├─ Parent's email address (must differ from child's)
        │     └─ Relationship to child (parent / legal guardian)
        │
        ├─► Step 5: Send parental consent email
        │     ├─ From: privacy@cloudvault-saas.eu
        │     ├─ Subject: "CloudVault SaaS Inc. — Your Child's Account Needs Your Approval"
        │     ├─ Content:
        │     │   ├─ Child's first name (no surname for minimization)
        │     │   ├─ What the service does (cloud storage for files)
        │     │   ├─ Personal data collected: name, email, file metadata, usage logs
        │     │   ├─ Purposes: account management, optional analytics, optional emails
        │     │   ├─ Retention: until account deletion or child turns [threshold]
        │     │   ├─ Rights: access, rectification, erasure, restriction, withdrawal
        │     │   └─ Consent link (HMAC-signed, expires 48 hours)
        │     └─ Reminder email sent at 24 hours if no response
        │
        ├─► Step 6: Parent clicks consent link
        │     ├─ Verify link signature and expiration
        │     ├─ Display full consent form with per-purpose toggles:
        │     │   ├─ [Required] Account Management — cannot be unticked
        │     │   ├─ [Optional] Service Improvement Analytics
        │     │   ├─ [Optional] Product Update Emails
        │     │   └─ [Optional] Industry Benchmarking (flagged as high-risk)
        │     │
        │     ├─ For high-risk purposes:
        │     │   └─ Require credit card micro-transaction ($0.50, refundable)
        │     │
        │     └─ Parent clicks "Approve Account" or "Decline Account"
        │
        ├─► Step 7: Record parental consent
        │     ├─ Parent identifier (email hash)
        │     ├─ Child identifier (account UUID)
        │     ├─ Verification method: email + [credit_card if applicable]
        │     ├─ Per-purpose consent decisions
        │     ├─ Timestamp, IP, user agent
        │     └─ Consent text version hash
        │
        └─► Step 8: Activate or deny account
              ├─ If approved: create child account with age-appropriate defaults
              │   ├─ Profiling: disabled by default (ICO Children's Code Standard 11)
              │   ├─ Geolocation: disabled by default (Standard 9)
              │   ├─ Data sharing: disabled by default (Standard 8)
              │   └─ Privacy settings: highest level by default (Standard 6)
              │
              └─ If declined: inform child, do not create account, delete collected data
```

## Workflow 2: Parent Dashboard Management

```
START: Parent logs into CloudVault SaaS Inc. parent dashboard
  │
  ├─► Display linked child accounts
  │     └─ For each child: name, age, account status, consent summary
  │
  ├─► Parent selects a child account
  │     │
  │     ├─► View current consent state per purpose
  │     │     ├─ Account Management: Required (cannot withdraw)
  │     │     ├─ Service Improvement Analytics: Granted (2026-01-15)
  │     │     ├─ Product Update Emails: Not Granted
  │     │     └─ Industry Benchmarking: Not Granted
  │     │
  │     ├─► Modify consent (grant or withdraw per purpose)
  │     │     ├─ Same one-click mechanism as adult preference center
  │     │     └─ Confirmation dialog with child-impact explanation
  │     │
  │     ├─► View child's data (proxy for child's Art. 15 access right)
  │     │
  │     ├─► Request data deletion (proxy for child's Art. 17 erasure right)
  │     │
  │     └─► Request account deletion
  │           ├─ Confirmation: "This will permanently delete [child]'s account and all data"
  │           └─ 30-day cooling-off period before permanent deletion
  │
  └─► Age Transition Monitoring
        ├─ When child reaches age threshold:
        │   ├─ Notify parent: "Your child has reached the age of digital consent in [country]"
        │   ├─ Notify child: "You can now manage your own privacy settings"
        │   ├─ Transfer consent management from parent dashboard to child's account
        │   └─ Child must re-confirm or withdraw existing consents independently
        └─ Log transition event in audit trail
```

## Workflow 3: COPPA Compliance for US Users

```
TRIGGER: User registration from United States (detected via country selection)
  │
  ├─► Apply COPPA threshold: age 13 (federal law, no state variation)
  │
  ├─► If age < 13:
  │     ├─ Apply FTC COPPA Rule (16 CFR Part 312) requirements:
  │     │   ├─ Verifiable parental consent required before ANY data collection
  │     │   ├─ Direct notice to parent with complete information
  │     │   ├─ Accepted verification methods per 16 CFR 312.5(b):
  │     │   │   ├─ Signed consent form (physical or electronic)
  │     │   │   ├─ Credit card or other online payment system transaction
  │     │   │   ├─ Call to toll-free number staffed by trained personnel
  │     │   │   ├─ Video conference with parent presenting ID
  │     │   │   └─ Government-issued ID + knowledge-based questions
  │     │   │
  │     │   ├─ CloudVault SaaS Inc. uses: credit card micro-transaction
  │     │   │   (approved method per FTC COPPA Rule 312.5(b)(2))
  │     │   │
  │     │   └─ Additional COPPA requirements:
  │     │       ├─ Do not condition child's participation on data collection
  │     │       ├─ Maintain confidentiality of collected information
  │     │       ├─ Retain data only as long as necessary for purpose
  │     │       └─ Delete data upon parent request (within 48 hours)
  │     │
  │     └─ Publish privacy notice compliant with 16 CFR 312.4:
  │           ├─ Name, address, phone, email of all operators collecting data
  │           ├─ Description of personal information collected
  │           ├─ Description of uses of personal information
  │           ├─ Whether information is disclosed to third parties
  │           ├─ Parent's right to review, delete, and refuse further collection
  │           └─ Link must be prominent on homepage and every page where data collected
  │
  └─► If age >= 13:
        └─ Apply standard CPRA/state privacy law consent flow
```
