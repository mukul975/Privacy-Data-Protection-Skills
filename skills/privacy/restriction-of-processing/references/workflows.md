# Right to Restriction Workflows

## Workflow 1: Restriction Request Assessment

```
[Restriction Request Received]
         │
         ▼
[Identity Verification]
   ├── Verified ──► [Identify Restriction Ground]
   │                    │
   │                    ├── Art. 18(1)(a): Accuracy contested?
   │                    │     └── Has subject disputed specific data accuracy?
   │                    │
   │                    ├── Art. 18(1)(b): Unlawful processing, erasure opposed?
   │                    │     └── Is processing unlawful AND does subject prefer
   │                    │         restriction over deletion?
   │                    │
   │                    ├── Art. 18(1)(c): Needed for legal claims?
   │                    │     └── Does controller no longer need data AND
   │                    │         does subject need it for legal proceedings?
   │                    │
   │                    └── Art. 18(1)(d): Objection pending?
   │                          └── Has subject objected under Art. 21(1) AND
   │                              is the legitimate grounds assessment pending?
   │                    │
   │                    ▼
   │            [Ground Established?]
   │              ├── Yes ──► [Apply Restriction]
   │              └── No ──► [Refuse with reasons + right to complain]
   │
   └── Not Verified ──► [Request ID, pause clock]
```

## Workflow 2: Technical Restriction Implementation

```
[Restriction Decision: APPLY]
         │
         ▼
[Within 72 Hours]
   │
   ├── [Database Flags]
   │     - Set restriction_flag = TRUE
   │     - Set restriction_date = [current UTC timestamp]
   │     - Set restriction_ground = [a|b|c|d]
   │     - Set restriction_reference = RST-YYYY-NNNN
   │
   ├── [Application Controls]
   │     - Update query filters to exclude restricted records
   │     - Configure API to return 423 Locked for restricted data
   │     - Add batch processing exclusion rules
   │     - Enable UI masking for internal tools
   │
   ├── [Storage Isolation] (if high-risk)
   │     - Move records to restricted partition
   │     - Apply DPO/Legal-only access controls
   │     - Enable access logging
   │
   └── [Art. 19 Notifications]
         - Identify all recipients
         - Send restriction notice to each
         - Request confirmation within 14 days
         │
         ▼
[Restriction Active — Begin Monitoring]
```

## Workflow 3: Permitted Processing During Restriction

```
[Request to Process Restricted Data]
         │
         ▼
[Which permitted purpose applies?]
   │
   ├── Data subject consent?
   │     └── [Obtain and document specific consent for this processing]
   │
   ├── Legal claims?
   │     └── [Identify specific claim, document necessity]
   │
   ├── Protection of rights of another person?
   │     └── [Identify the person and the right to be protected]
   │
   └── Important public interest?
         └── [Identify the specific EU/Member State public interest basis]
         │
         ▼
[Permitted purpose established?]
   ├── Yes ──► [Process with documentation]
   │            - Log: who, what, when, why, permitted purpose
   │            - Minimise processing to what is strictly necessary
   │
   └── No ──► [DENY — processing not permitted]
               - Document the denial
               - Advise requester on alternative approaches
```

## Workflow 4: Lifting Restriction

```
[Resolution Trigger]
   │
   ├── Accuracy verified (Ground a)
   ├── Subject consents to erasure (Ground b)
   ├── Legal proceedings concluded (Ground c)
   └── Art. 21 assessment complete (Ground d)
         │
         ▼
[Pre-Lifting Notification (Art. 18(3))]
   - Notify data subject at least 7 days before lifting
   - State the reason restriction is being lifted
   - Inform of any consequences
   - Inform of right to object or request erasure
         │
         ▼
[7-Day Notice Period]
   │
   ├── Subject does not object ──► [Lift Restriction]
   │     - Remove database flags
   │     - Restore application access
   │     - Move data back from restricted partition
   │     - Notify third-party recipients
   │
   └── Subject objects ──► [Assess objection]
         ├── Valid new ground ──► Maintain restriction
         └── No valid ground ──► Proceed with lifting
         │
         ▼
[Update Register — Close Request]
```
