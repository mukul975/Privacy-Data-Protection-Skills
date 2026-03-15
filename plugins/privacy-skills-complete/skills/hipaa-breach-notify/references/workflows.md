# HIPAA Breach Notification — Workflows

## Workflow 1: Breach Discovery and Determination

```
Potential Breach Event Detected
│
├── Step 1: Incident Identification (Day 0)
│   ├── Source: workforce report, BA notification, audit finding, external notification
│   ├── Log incident in tracking system with timestamp
│   ├── Notify Privacy Officer and CISO immediately
│   └── "Discovery" date = first day breach is known or should have been known
│
├── Step 2: Was there an impermissible use or disclosure of PHI? (Days 1-7)
│   ├── YES → Presumed breach; proceed to risk assessment
│   └── NO → Not a breach; document and close
│
├── Step 3: Does a breach exception apply? (§164.402(1))
│   ├── Exception 1: Unintentional good-faith acquisition by workforce member
│   │   ├── Within scope of authority? AND
│   │   ├── No further impermissible use/disclosure?
│   │   └── If both YES → Not a breach; document and close
│   │
│   ├── Exception 2: Inadvertent disclosure between authorized persons
│   │   ├── Same CE, BA, or organized healthcare arrangement? AND
│   │   ├── No further impermissible use/disclosure?
│   │   └── If both YES → Not a breach; document and close
│   │
│   └── Exception 3: Good-faith belief recipient cannot retain information
│       ├── Would person reasonably not be able to retain PHI?
│       └── If YES → Not a breach; document and close
│
├── Step 4: Four-Factor Risk Assessment (Days 7-14)
│   ├── Factor 1: Nature and extent of PHI involved
│   │   └── What types of identifiers? Clinical data? SSN? Financial?
│   ├── Factor 2: Unauthorized person who used/received PHI
│   │   └── Who accessed it? Obligation to protect? Motive?
│   ├── Factor 3: Was PHI actually acquired or viewed?
│   │   └── Forensic evidence of access? Was it encrypted?
│   ├── Factor 4: Extent risk has been mitigated
│   │   └── Assurances obtained? PHI recovered? Recipient destroyed?
│   │
│   └── Low probability of compromise across all four factors?
│       ├── YES → Not a breach; document risk assessment; close
│       └── NO → BREACH CONFIRMED → Trigger notification workflow
│
└── Step 5: Document Determination
    ├── Record all findings and analysis
    ├── Retain documentation for minimum 6 years
    └── Even non-breach determinations must be documented
```

## Workflow 2: Breach Notification Execution

```
Breach Confirmed — Notification Required
│
├── Step 1: Scope Determination (Days 14-21)
│   ├── Identify all affected individuals
│   ├── Determine number of affected individuals
│   ├── Identify states of residence of affected individuals
│   ├── Count affected individuals per state
│   └── Classify: 500+ overall? 500+ in any single state?
│
├── Step 2: Notification Preparation (Days 21-30)
│   │
│   ├── Individual Notification Letters
│   │   ├── Draft using pre-approved template
│   │   ├── Include all §164.404(c) required elements
│   │   ├── Legal counsel review
│   │   ├── Prepare call center scripts and train staff
│   │   └── Arrange credit monitoring vendor (if applicable)
│   │
│   ├── HHS Notification
│   │   ├── 500+ individuals: Prepare immediate HHS portal submission
│   │   ├── <500 individuals: Log for annual submission
│   │   └── Gather all required portal fields
│   │
│   ├── State AG Notification (if 500+ in any state)
│   │   ├── Identify AG notification requirements per state
│   │   ├── Prepare state-specific notifications
│   │   └── Legal counsel review per state
│   │
│   └── Media Notification (if 500+ in any state)
│       ├── Draft press release
│       ├── Communications team review
│       └── Identify prominent media outlets in affected states
│
├── Step 3: Notification Execution (Days 30-60)
│   │
│   ├── Individual Notices
│   │   ├── Mail first-class letters to last known addresses
│   │   ├── Email if individual agreed to electronic notice
│   │   ├── If 10+ individuals with insufficient contact info:
│   │   │   post conspicuous notice on website for 90 days
│   │   │   OR notice in major media
│   │   └── Track delivery and returned mail
│   │
│   ├── HHS Portal Submission (500+)
│   │   └── Submit via ocrportal.hhs.gov concurrent with individual notice
│   │
│   ├── State AG Notification (if applicable)
│   │   └── Submit per state-specific requirements concurrent with individual notice
│   │
│   └── Media Notification (if applicable)
│       └── Distribute press release to prominent outlets in affected states
│
├── Step 4: Post-Notification Activities (Day 60+)
│   ├── Monitor call center volume and issues
│   ├── Track credit monitoring enrollment
│   ├── Process returned mail; attempt updated addresses
│   ├── Post substitute notice if needed
│   ├── Document all notification activities
│   └── Respond to OCR inquiries
│
└── HARD DEADLINE: All individual notifications must be completed
    within 60 calendar days of discovery
```

## Workflow 3: Business Associate Breach Chain

```
Breach Occurs at Business Associate or Subcontractor
│
├── Subcontractor Level
│   ├── Subcontractor discovers breach
│   ├── Notifies Business Associate within BAA timeframe (typically 24 hours)
│   ├── Provides: nature of breach, PHI involved, individuals affected (if known)
│   └── Cooperates with BA investigation
│
├── Business Associate Level
│   ├── BA validates and investigates
│   ├── Identifies affected individuals to extent possible
│   ├── Notifies Covered Entity within BAA timeframe (typically 5 business days)
│   ├── Provides all information CE needs for notification obligations
│   └── Cooperates with CE investigation and notification
│
├── Covered Entity Level
│   ├── CE receives BA breach notification
│   ├── Conducts independent four-factor risk assessment
│   ├── Determines if notification is required
│   ├── Fulfills all notification obligations (individual, HHS, AG, media)
│   └── Documents entire chain of notification
│
└── Cost Allocation
    ├── Per BAA terms: party responsible for breach bears notification costs
    ├── Asclepius standard: BA bears costs if breach results from BA acts/omissions
    └── Including: notification mailing, call center, credit monitoring, legal fees
```
