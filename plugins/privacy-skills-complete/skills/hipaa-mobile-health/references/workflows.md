# HIPAA Mobile Health — Workflows

## Workflow 1: Mobile Device PHI Risk Assessment

```
Mobile Device Risk Assessment Initiation
│
├── Step 1: Device Inventory
│   ├── Identify all mobile device types accessing ePHI
│   │   ├── Organization-issued smartphones
│   │   ├── Organization-issued tablets
│   │   ├── Personal devices (BYOD) with PHI access
│   │   ├── Wearable devices (clinical)
│   │   └── Remote patient monitoring devices
│   │
│   ├── Document: device model, OS version, encryption status, MDM enrollment
│   └── Classify by risk level: high (stores ePHI), medium (transmits ePHI), low (no ePHI)
│
├── Step 2: Threat Identification
│   ├── Loss or theft of device
│   ├── Unauthorized access (weak authentication)
│   ├── Malware / malicious apps
│   ├── Insecure wireless network connections
│   ├── Unencrypted data at rest or in transit
│   ├── Improper disposal / decommissioning
│   └── Insider threat (unauthorized workforce access)
│
├── Step 3: Vulnerability Assessment
│   ├── Is full-disk encryption enabled on all devices?
│   ├── Is MDM enrolled with remote wipe capability?
│   ├── Is automatic logoff configured (2 min inactivity)?
│   ├── Is jailbreak/root detection active?
│   ├── Are OS and apps current on security patches?
│   ├── Is transmission encryption enforced (TLS 1.2+)?
│   └── Is app-level containerization in place for BYOD?
│
├── Step 4: Risk Scoring
│   ├── Likelihood x Impact for each threat-vulnerability pair
│   ├── Score: Critical / High / Medium / Low
│   └── Document risk scoring methodology and results
│
└── Step 5: Risk Mitigation Plan
    ├── Assign remediation actions per finding
    ├── Set deadlines based on risk severity
    ├── Track remediation through completion
    └── Update risk register
```

## Workflow 2: BYOD Enrollment and Lifecycle Management

```
Workforce Member Requests BYOD Access to ePHI Systems
│
├── Step 1: Eligibility Determination
│   ├── Is the workforce member's role authorized for BYOD?
│   ├── Has the member completed HIPAA training (including mobile module)?
│   └── Has the member signed the BYOD acceptable use agreement?
│       ├── YES to all → Proceed to enrollment
│       └── NO → Complete prerequisites before enrollment
│
├── Step 2: Device Compliance Check
│   ├── OS version meets minimum requirement (e.g., iOS 16+, Android 13+)?
│   ├── Device not jailbroken/rooted?
│   ├── Full-disk encryption enabled?
│   ├── Screen lock configured (biometric + 6-digit PIN)?
│   │
│   ├── All checks PASS → Proceed to MDM enrollment
│   └── Any check FAIL → Deny enrollment; provide remediation steps
│
├── Step 3: MDM Enrollment
│   ├── Install MDM profile (e.g., Microsoft Intune, VMware Workspace ONE)
│   ├── Configure work container (separate personal and work data)
│   ├── Install required security apps (mobile threat defense)
│   ├── Enable remote wipe of work container only
│   ├── Configure VPN auto-connect for ePHI applications
│   └── Verify audit logging is active
│
├── Step 4: Ongoing Compliance Monitoring
│   ├── MDM continuous compliance checks (daily)
│   │   ├── Encryption still enabled?
│   │   ├── OS and apps updated within patch window?
│   │   ├── Jailbreak/root detection clear?
│   │   └── MDM profile still active?
│   │
│   ├── Non-compliance detected?
│   │   ├── Grace period: 24 hours for non-critical (OS patch)
│   │   ├── Immediate block for critical (jailbreak, MDM removal)
│   │   └── Notify user and IT security
│   │
│   └── Quarterly access review: still role-appropriate?
│
└── Step 5: Offboarding / Device Retirement
    ├── Workforce termination or role change → Remote wipe work container
    ├── Device replacement → Wipe old device work data; enroll new device
    ├── Confirm wipe completion in MDM console
    ├── Retain audit log of wipe action
    └── Personal data is NOT wiped (container separation)
```

## Workflow 3: mHealth App Privacy Assessment

```
New mHealth Application Under Consideration
│
├── Step 1: Regulatory Classification
│   ├── Will the app be used by a covered entity or business associate?
│   │   ├── YES → HIPAA applies
│   │   └── NO → Evaluate FTC Health Breach Notification Rule applicability
│   │
│   ├── Does the app meet the FDA definition of a medical device / SaMD?
│   │   ├── YES → FDA regulation applies (in addition to HIPAA if applicable)
│   │   └── NO → General wellness or health management; FDA enforcement discretion
│   │
│   └── Document regulatory classification and rationale
│
├── Step 2: Privacy Impact Assessment
│   ├── What PHI/health data does the app collect?
│   ├── Where is data stored (on-device, cloud, both)?
│   ├── Who is the data shared with (providers, payers, third parties)?
│   ├── What is the lawful basis for each data use?
│   ├── What consent mechanisms are in place?
│   ├── Is data de-identified or aggregated before secondary use?
│   └── What is the data retention period?
│
├── Step 3: Security Assessment
│   ├── Data at rest encrypted (AES-256)?
│   ├── Data in transit encrypted (TLS 1.2+)?
│   ├── Authentication mechanism (biometric, MFA)?
│   ├── App-level session timeout configured?
│   ├── No PHI stored in device logs or crash reports?
│   ├── Certificate pinning implemented?
│   ├── Penetration testing completed?
│   └── OWASP Mobile Top 10 assessment completed?
│
├── Step 4: Vendor Assessment (if third-party app)
│   ├── Is vendor a business associate? → BAA required
│   ├── Has vendor completed SOC 2 Type II audit?
│   ├── Does vendor provide HIPAA compliance documentation?
│   ├── What is vendor's breach notification process?
│   └── What happens to data upon contract termination?
│
└── Step 5: Approval Decision
    ├── All assessments satisfactory → Approve with conditions
    ├── Remediable issues → Conditional approval with remediation timeline
    ├── Critical issues → Deny until resolved
    └── Document decision and conditions in app registry
```

## Workflow 4: Lost/Stolen Mobile Device Response

```
Mobile Device Containing ePHI Reported Lost or Stolen
│
├── Step 1: Immediate Response (Within 1 hour)
│   ├── Workforce member reports loss to IT security / help desk
│   ├── IT initiates remote wipe command via MDM
│   ├── Disable user's VPN and remote access credentials
│   ├── Log incident in incident tracking system
│   └── Notify Privacy Officer and Security Officer
│
├── Step 2: Breach Risk Assessment (Within 24 hours)
│   ├── Was the device encrypted per HHS guidance (NIST standards)?
│   │   ├── YES → Low probability of compromise; may qualify for
│   │   │         safe harbor (not a breach per §164.402)
│   │   └── NO → Presumed breach; proceed to notification assessment
│   │
│   ├── Was the device locked (screen lock active at time of loss)?
│   ├── What ePHI was accessible on the device?
│   ├── Remote wipe confirmed successful?
│   │   ├── YES → Reduced risk
│   │   └── NO → Increased risk (device may be offline)
│   │
│   └── Apply 4-factor breach risk assessment per §164.402(2)
│
├── Step 3: Breach Determination
│   ├── Low probability of compromise → Document; no notification required
│   ├── Breach confirmed → Initiate HIPAA breach notification process
│   └── Document determination rationale with evidence
│
└── Step 4: Post-Incident Actions
    ├── Review and update mobile device policies if gap identified
    ├── Conduct targeted retraining for the workforce member
    ├── Evaluate whether encryption was properly enforced enterprise-wide
    ├── Update risk analysis with incident findings
    └── Report to compliance committee
```
