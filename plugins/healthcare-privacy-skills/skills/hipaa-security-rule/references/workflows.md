# HIPAA Security Rule — Workflows

## Workflow 1: Addressable Implementation Specification Decision

```
Addressable Implementation Specification Identified
│
├── Step 1: Assess reasonableness and appropriateness
│   ├── Consider organization size, complexity, and capabilities
│   ├── Consider technical infrastructure, hardware, and software
│   ├── Consider costs of security measures
│   ├── Consider probability and criticality of risks to ePHI
│   │
│   └── Is the specification reasonable and appropriate?
│       │
│       ├── YES → Implement the specification
│       │         Document implementation details
│       │
│       └── NO → Continue evaluation
│
├── Step 2: Evaluate alternative measures
│   ├── Is there an equivalent alternative that achieves the standard?
│   │   ├── YES → Implement the alternative measure
│   │   │         Document why specification is not appropriate
│   │   │         Document the alternative and why it is equivalent
│   │   │
│   │   └── NO → Continue evaluation
│   │
│   └── Can the standard be met without this specification or alternative?
│       ├── YES → Document why the standard is met without it
│       │         Must be supportable under regulatory scrutiny
│       │
│       └── NO → The specification IS required
│                 Implement regardless of cost/complexity
│
└── CRITICAL: "Addressable" never means "optional"
    All decisions must be documented and retained for 6 years
```

## Workflow 2: Security Incident Response

```
Potential Security Incident Detected
│
├── Step 1: Detection and Initial Assessment (0-1 hour)
│   ├── Incident detected via: SIEM alert / User report / Audit review / Vendor notification
│   ├── Security analyst performs initial triage
│   ├── Classify severity: Critical / High / Medium / Low
│   └── Activate incident response team if Medium or above
│
├── Step 2: Containment (1-4 hours for Critical/High)
│   ├── Isolate affected systems from network
│   ├── Preserve forensic evidence (memory dumps, disk images, logs)
│   ├── Block malicious IP addresses, accounts, or processes
│   ├── Activate backup communication channels if primary compromised
│   └── Document all containment actions with timestamps
│
├── Step 3: Investigation (4-72 hours)
│   ├── Determine scope: which systems, which ePHI, how many records
│   ├── Identify attack vector and timeline
│   ├── Assess whether ePHI was accessed, acquired, used, or disclosed
│   ├── Determine if ePHI was encrypted (unsecured PHI test)
│   └── Identify all affected individuals
│
├── Step 4: Breach Determination (parallel with investigation)
│   ├── Was there an impermissible use or disclosure of PHI?
│   │   ├── NO → Document incident; close with lessons learned
│   │   └── YES → Conduct four-factor risk assessment (§164.402(2))
│   │             Does one of the three breach exceptions apply?
│   │             Is there low probability of compromise?
│   │             → If breach confirmed: trigger breach notification workflow
│   │
│   └── Notify Privacy Officer and Legal Counsel
│
├── Step 5: Eradication and Recovery (after containment)
│   ├── Remove malware, patch vulnerabilities, close attack vector
│   ├── Rebuild affected systems from known-good images
│   ├── Restore data from verified clean backups
│   ├── Verify system integrity before reconnecting to network
│   └── Implement additional monitoring on restored systems
│
├── Step 6: Post-Incident Activities
│   ├── Lessons learned review within 14 days
│   ├── Update risk analysis with new threat/vulnerability information
│   ├── Implement corrective actions
│   ├── Update incident response plan based on lessons learned
│   └── Retain all incident documentation for 6 years minimum
│
└── Reporting Requirements
    ├── Internal: Executive leadership, Board (for material incidents)
    ├── Breach Notification: Per §164.400-414 if breach confirmed
    ├── Law Enforcement: If criminal activity suspected (coordinate with legal)
    └── Cyber Insurance: Per policy notification requirements
```

## Workflow 3: Access Control Provisioning and De-provisioning

```
Access Request/Change Event
│
├── New Hire Provisioning
│   ├── HR sends hire notification to IT
│   ├── Manager submits access request specifying role and department
│   ├── IT creates unique user ID per naming convention
│   ├── Role-based access profile assigned based on job function
│   ├── MFA enrollment completed
│   ├── User signs acceptable use agreement
│   ├── Security awareness training completed before ePHI access granted
│   └── Access activated on start date — not before
│
├── Role Change / Transfer
│   ├── Manager submits role change request
│   ├── Previous role access reviewed and revoked within 3 business days
│   ├── New role access provisioned per new job function
│   └── Audit trail of all access changes maintained
│
├── Termination De-provisioning
│   ├── HR sends termination notification
│   ├── Voluntary termination: access disabled on last day of employment
│   ├── Involuntary termination: access disabled immediately upon notification
│   ├── All physical access credentials collected (badges, keys, tokens)
│   ├── Remote access revoked (VPN certificates, MFA tokens)
│   ├── Shared passwords rotated if the user had knowledge
│   └── IT confirms deactivation within 1 hour of termination processing
│
└── Periodic Access Review
    ├── Quarterly: Managers certify active access for their direct reports
    ├── Semi-annual: Privileged access review (admin accounts, elevated roles)
    ├── Annual: Comprehensive access audit across all ePHI systems
    └── Any access without current manager certification → suspended pending review
```

## Workflow 4: Encryption Implementation Decision

```
ePHI Storage or Transmission Identified
│
├── Is ePHI at rest or in transit?
│   │
│   ├── AT REST
│   │   ├── Server/database storage → AES-256 volume or tablespace encryption
│   │   ├── Endpoint (laptop, workstation) → Full disk encryption (BitLocker, FileVault)
│   │   ├── Portable media (USB, external drive) → AES-256 hardware or software encryption
│   │   ├── Backup media → Encrypted backup with separate key management
│   │   ├── Cloud storage → Provider-managed encryption (customer-managed keys preferred)
│   │   └── Medical devices → Assess device capability; implement if supported
│   │       └── If device cannot encrypt → Document compensating controls
│   │           (network segmentation, physical access restriction, monitoring)
│   │
│   └── IN TRANSIT
│       ├── Internal network → TLS 1.2+ between systems containing ePHI
│       ├── External network → TLS 1.3 preferred; TLS 1.2 minimum
│       ├── Email → TLS enforced; encrypted email gateway for external ePHI
│       ├── VPN → IPsec or TLS VPN for remote access
│       ├── Wireless → WPA3 Enterprise with RADIUS
│       ├── API communications → Mutual TLS + OAuth 2.0
│       └── File transfers → SFTP or FTPS; no unencrypted FTP
│
├── Key Management
│   ├── Use FIPS 140-2/140-3 validated cryptographic modules
│   ├── Key generation using approved random number generators
│   ├── Key storage in HSM or equivalent secure key store
│   ├── Key rotation schedule: annual minimum, per-session for TLS
│   ├── Key backup and recovery procedures documented and tested
│   └── Key destruction when no longer needed (NIST SP 800-57)
│
└── Documentation
    ├── Encryption standards policy documenting all implementations
    ├── Approved algorithm and key length specifications
    ├── Exception documentation for systems that cannot encrypt
    └── Annual review of encryption implementation against current standards
```
