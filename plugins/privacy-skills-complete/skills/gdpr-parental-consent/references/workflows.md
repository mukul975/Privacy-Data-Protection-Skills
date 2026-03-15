# Parental Consent Verification Workflows

## Workflow 1: Age Determination and Consent Routing

```
User initiates account registration
│
├─ Display neutral age prompt: "What is your date of birth?"
│  [Scrollable date picker — no default date, no threshold hint]
│
├─ Calculate user's age from date of birth
│
├─ Determine applicable jurisdiction from:
│  ├─ User's declared country of residence, OR
│  ├─ IP geolocation (as fallback), OR
│  └─ Service's primary operating jurisdiction (as last resort)
│
├─ Look up national age threshold for the jurisdiction:
│  ├─ Austria: 14 | Belgium: 13 | Bulgaria: 14 | Croatia: 16
│  ├─ Cyprus: 14 | Czech Republic: 15 | Denmark: 13 | Estonia: 13
│  ├─ Finland: 13 | France: 15 | Germany: 16 | Greece: 15
│  ├─ Hungary: 16 | Ireland: 16 | Italy: 14 | Latvia: 13
│  ├─ Lithuania: 14 | Luxembourg: 16 | Malta: 13 | Netherlands: 16
│  ├─ Norway: 13 | Poland: 16 | Portugal: 13 | Romania: 16
│  ├─ Slovakia: 16 | Slovenia: 16 | Spain: 14 | Sweden: 13
│  └─ UK: 13
│
├─ Age >= applicable threshold?
│  ├─ YES → User can consent independently
│  │         ├─ Proceed with standard consent flow
│  │         ├─ Display age-appropriate privacy notice
│  │         └─ Record consent with standard Art. 7(1) fields
│  │
│  └─ NO → Parental consent required
│           ├─ Route to Workflow 2 (Parental Verification)
│           ├─ Display child-friendly message explaining parental involvement
│           └─ Collect parent's contact information (email)
│
└─ Log the age determination decision:
   ├─ User age, jurisdiction, threshold applied
   ├─ Routing decision (independent / parental)
   └─ Timestamp
```

## Workflow 2: Parental Consent Collection and Verification

```
Parental consent flow initiated
│
├─ Step 1: Contact Parent
│  ├─ Send email to parent's provided email address
│  ├─ Email contains:
│  │  ├─ Explanation: "[Child's first name] wants to join [Service Name]"
│  │  ├─ Service description and data practices summary
│  │  ├─ Link to full privacy notice
│  │  ├─ Unique verification link (valid for 72 hours)
│  │  └─ Statement: "If you did not expect this email, please ignore it."
│  ├─ If no response within 72 hours:
│  │  ├─ Send one reminder email
│  │  └─ If no response within 7 days: delete parent contact info and child's registration data
│  └─ Parent clicks verification link
│
├─ Step 2: Verify Parental Identity
│  ├─ Determine verification level based on processing risk:
│  │  ├─ LOW RISK (educational content, no social features):
│  │  │  └─ Email Plus: parent confirms via email response + delayed confirmation
│  │  ├─ MEDIUM RISK (interactive features, progress tracking):
│  │  │  └─ Credit card micro-transaction (EUR/USD/GBP 0.50, refunded within 48h)
│  │  └─ HIGH RISK (social features, messaging, special category data):
│  │     └─ Government ID upload OR video verification call
│  │
│  ├─ Parent completes verification
│  ├─ Verification outcome recorded: verified / failed / expired
│  └─ If verification fails: allow one retry; then require escalation to higher-assurance method
│
├─ Step 3: Present Consent Choices
│  ├─ Display granular consent form to parent:
│  │  ├─ Purpose 1: [Account creation and service delivery] — Required
│  │  ├─ Purpose 2: [Learning progress reports for parent] — Optional [toggle]
│  │  ├─ Purpose 3: [Content personalisation based on learning level] — Optional [toggle]
│  │  └─ Purpose 4: [Anonymous aggregated analytics] — Optional [toggle]
│  │
│  ├─ Each purpose includes:
│  │  ├─ Plain language description
│  │  ├─ Data categories involved
│  │  ├─ Retention period
│  │  └─ How to withdraw consent later
│  │
│  └─ Parent makes selections and confirms
│
├─ Step 4: Record Consent
│  ├─ Generate consent record with all Art. 7(1) fields:
│  │  ├─ consent_id, child_id, parent_id
│  │  ├─ verification_method, verification_outcome
│  │  ├─ purposes_consented (array), purposes_refused (array)
│  │  ├─ consent_text_version (SHA-256 hash)
│  │  ├─ timestamp, IP address, user agent
│  │  └─ expiry_date (12 months from grant)
│  │
│  └─ Store in consent registry database
│
├─ Step 5: Activate Child Account
│  ├─ Create child account with age-appropriate defaults
│  ├─ Apply consent-limited feature set (only consented purposes)
│  ├─ Send confirmation email to parent with:
│  │  ├─ Summary of consent granted
│  │  ├─ Link to parental dashboard
│  │  └─ Instructions for withdrawal
│  │
│  └─ Child account is now active
│
└─ END: Consent collection complete
```

## Workflow 3: Parental Consent Renewal

```
Consent renewal trigger detected
│
├─ Trigger types:
│  ├─ Annual expiry: consent record's expiry_date reached
│  ├─ Purpose change: new processing purpose added to the service
│  ├─ Policy change: privacy policy or consent text materially changed
│  └─ Feature change: new feature introduced that requires additional data
│
├─ Send renewal notification to parent:
│  ├─ Email subject: "Your consent for [Child's name] on [Service Name] needs renewing"
│  ├─ Summary of current consent and what has changed (if applicable)
│  ├─ Link to parental dashboard to review and renew
│  └─ Statement: "If you do not renew within 30 days, we will limit [Child's name]'s account
│     to essential features only and delete data associated with non-renewed purposes."
│
├─ Parent response:
│  ├─ Renews consent → Update consent record with new timestamp and expiry
│  ├─ Partially renews → Withdraw consent for specific purposes; update record
│  ├─ Does not renew within 30 days:
│  │  ├─ Restrict child's account to essential features only
│  │  ├─ Delete data associated with non-renewed purposes
│  │  └─ Send final notification: "We've limited [Child's name]'s account.
│  │     You can restore features at any time from your dashboard."
│  └─ Withdraws all consent:
│     ├─ Deactivate child's account
│     ├─ Execute data deletion (see Workflow 4)
│     └─ Send deletion confirmation
│
└─ Log renewal outcome in consent registry
```

## Workflow 4: Consent Withdrawal and Data Deletion

```
Parent initiates consent withdrawal
│
├─ Via parental dashboard: Click "Withdraw consent" for specific purpose(s) or "Delete account"
├─ Via email to DPO: Request processed within 48 hours
│
├─ Scope determination:
│  ├─ Partial withdrawal (specific purpose):
│  │  ├─ Disable features associated with the withdrawn purpose
│  │  ├─ Delete data collected solely for that purpose
│  │  ├─ Retain data shared with other still-consented purposes
│  │  └─ Update consent record to reflect withdrawal
│  │
│  └─ Full withdrawal / account deletion:
│     ├─ Deactivate child's account immediately
│     ├─ Execute full data deletion per retention schedule
│     ├─ Notify third parties per Art. 17(2) if applicable
│     ├─ Retain consent record for legal compliance (6 years)
│     └─ Send deletion confirmation to parent
│
├─ Timeline:
│  ├─ Feature restriction: within 24 hours
│  ├─ Primary data deletion: within 30 days
│  └─ Backup purge: within 60 days
│
└─ Log withdrawal in consent registry with timestamp and scope
```

## Workflow 5: Age Threshold Transition

```
Child approaches the national age threshold
│
├─ 30 days before threshold birthday:
│  ├─ Send notification to parent:
│  │  "In 30 days, [Child's name] will reach the age where they can manage
│  │   their own privacy choices on [Service Name]. We'll transfer consent
│  │   authority to them at that time."
│  ├─ Send notification to child (age-appropriate):
│  │  "Soon you'll be old enough to manage your own privacy settings!
│  │   We'll show you how when the time comes."
│
├─ On threshold birthday:
│  ├─ Present consent review to the child:
│  │  "You can now decide for yourself which features to use.
│  │   Here are the choices your parent made — you can keep them or change them."
│  ├─ Child reviews each purpose and confirms or changes consent
│  ├─ Generate new consent record under child's own authority
│  ├─ Notify parent:
│  │  "[Child's name] has taken over their privacy choices.
│  │   You can still view their settings in your dashboard."
│  ├─ Adjust parental dashboard:
│  │  ├─ Parent retains read-only visibility (unless child removes)
│  │  └─ Parent can no longer modify child's consent choices
│
└─ Log threshold transition in consent registry
```
