# Telehealth Privacy — Workflows

## Workflow 1: Telehealth Platform Compliance Evaluation

```
Evaluating Telehealth Platform for HIPAA Compliance
│
├── Step 1: BAA Assessment
│   ├── Does the vendor offer a Business Associate Agreement?
│   │   ├── YES → Review BAA for all required provisions (§164.504(e)(2))
│   │   └── NO → Platform is NOT compliant for HIPAA telehealth
│   │         (Exception: OCR enforcement discretion expired August 2023)
│   │
│   └── Is BAA executed before any PHI transmission?
│
├── Step 2: Technical Safeguards Evaluation
│   │
│   ├── Encryption
│   │   ├── End-to-end encryption for video/audio/data? (minimum AES-128; AES-256 preferred)
│   │   ├── TLS 1.2+ for signaling and control channels?
│   │   ├── SRTP for media streams?
│   │   └── No unencrypted fallback?
│   │
│   ├── Access Controls
│   │   ├── Unique user authentication for providers?
│   │   ├── Patient identity verification process?
│   │   ├── Session-level access controls (each session separate)?
│   │   ├── Automatic session termination on disconnect/inactivity?
│   │   └── MFA for provider access?
│   │
│   ├── Audit Controls
│   │   ├── Session logging (initiation, connection, participants, duration)?
│   │   ├── Recording access logs?
│   │   ├── Log retention (minimum 6 years)?
│   │   └── Tamper-resistant logs?
│   │
│   └── Integrity
│       ├── Tamper-evident session metadata?
│       └── Digital signatures on stored encounters?
│
├── Step 3: Data Handling
│   ├── Where is data stored (geographic location)?
│   ├── How long are recordings retained?
│   ├── Data deletion/retention policies?
│   └── Data portability (can entity retrieve data at termination)?
│
└── Step 4: Approval Decision
    ├── All criteria met → Approved for clinical telehealth
    ├── Deficiencies identified → Remediation required before approval
    └── Document evaluation results and approval
```

## Workflow 2: Telehealth Encounter Privacy Protocol

```
Telehealth Visit Initiated
│
├── Pre-Visit
│   ├── Provider confirms private room with closed door
│   ├── Provider ensures no visible patient information behind camera
│   ├── Provider uses headphones/earbuds
│   ├── Provider uses only approved/managed device
│   └── System verifies platform is BAA-covered
│
├── Visit Start
│   ├── Provider authenticates to platform (MFA)
│   ├── Patient authenticates (portal credentials or identity verification)
│   ├── System prompts: Confirm patient's physical location (state)
│   │   └── Apply location-specific consent and recording requirements
│   │
│   ├── Recording Consent (if applicable)
│   │   ├── Is patient in a two-party consent state?
│   │   │   ├── YES → Display recording notice; require affirmative consent
│   │   │   │   ├── Patient consents → Enable recording
│   │   │   │   └── Patient declines → Proceed without recording
│   │   │   └── NO → Display notice; one-party consent sufficient
│   │   └── Document consent decision
│   │
│   └── Privacy notice displayed to patient:
│       "This visit is conducted on a secure, HIPAA-compliant platform.
│        [Recording notice if applicable]"
│
├── During Visit
│   ├── Maintain encrypted connection throughout
│   ├── Provider documents in EHR (same clinical standards as in-person)
│   ├── If connection drops: re-authenticate before resuming
│   ├── If prescribing controlled substances:
│   │   ├── Verify provider licensed in patient's state
│   │   ├── Check state PDMP
│   │   └── Apply Ryan Haight Act requirements
│   └── Screen sharing: ensure no other patient data visible
│
├── Visit End
│   ├── Provider terminates session
│   ├── System confirms session ended on all endpoints
│   ├── Session metadata logged (duration, participants, location)
│   └── Recording (if any) encrypted and stored in EHR document management
│
└── Post-Visit
    ├── Clinical documentation completed in EHR
    ├── Prescriptions transmitted via e-prescribing (HIPAA-compliant)
    ├── Follow-up communications via secure messaging (patient portal)
    └── Recording access restricted to care team and authorized reviewers
```

## Workflow 3: Remote Patient Monitoring Privacy Setup

```
RPM Program Enrollment
│
├── Step 1: Vendor/Platform Assessment
│   ├── RPM platform vendor has BAA in place?
│   ├── Device-to-cloud communication encrypted?
│   ├── Cloud platform meets HIPAA Security Rule?
│   └── Data integration with EHR is secure (FHIR API + OAuth 2.0)?
│
├── Step 2: Patient Enrollment and Consent
│   ├── Explain data collection scope (what data, how often)
│   ├── Explain who accesses data (care team, monitoring center, BA)
│   ├── Explain how data is used (clinical, AI analytics, quality)
│   ├── Explain patient's right to pause or stop monitoring
│   ├── Explain security measures
│   ├── Explain limitations (not emergency services)
│   ├── Obtain written informed consent
│   └── Document consent in EHR
│
├── Step 3: Device Configuration
│   ├── Configure device with patient-specific encryption keys
│   ├── Enable minimum necessary data collection only
│   ├── Configure secure transmission schedule
│   ├── Register device in asset management system
│   └── Provide patient with setup instructions and privacy tips
│
├── Step 4: Ongoing Monitoring
│   ├── Data flows securely to EHR/monitoring platform
│   ├── Alerts and notifications minimize PHI content
│   ├── Regular data quality checks
│   ├── Quarterly consent review with patient
│   └── Device firmware updates managed securely
│
└── Step 5: Disenrollment
    ├── Patient requests disenrollment or program ends
    ├── Data collection ceases
    ├── Device returned or wiped (NIST SP 800-88)
    ├── Historical data retained in EHR per retention policy
    └── Consent status updated in EHR
```
