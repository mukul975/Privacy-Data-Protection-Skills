# Employee Biometric Data Workflows

## Workflow 1: Biometric Processing Necessity Assessment

```
START: Proposal to implement biometric system in the workplace
│
├─ Step 1: Define the specific purpose
│  ├─ Is the purpose concrete and documented? [Yes/No → Document first if No]
│  ├─ Examples of valid purposes:
│  │  - Controlling access to high-security area (R&D lab, server room)
│  │  - Contactless identification in cleanroom environment
│  ├─ Examples of insufficient purposes:
│  │  - "Improving workforce management"
│  │  - "Modernising access control"
│  │  - "Ensuring accurate attendance"
│  └─ Document purpose in DPIA
│
├─ Step 2: Evaluate less intrusive alternatives
│  ├─ Would a smart card + PIN achieve the same purpose? [Yes → Use card + PIN]
│  ├─ Would a proximity badge achieve the same purpose? [Yes → Use badge]
│  ├─ Would supervisor sign-off achieve the same purpose? [Yes → Use sign-off]
│  ├─ Are there documented, specific reasons why alternatives are insufficient?
│  │  ├─ Card sharing / tailgating is a documented security problem → May justify biometric
│  │  ├─ Contactless operation is operationally necessary → May justify biometric
│  │  ├─ No documented reason → Biometric is disproportionate
│  └─ Document alternatives assessment
│
├─ Step 3: Identify Art. 9(2) exception
│  ├─ Art. 9(2)(a) Explicit consent → Rarely valid (power imbalance). Check national law.
│  ├─ Art. 9(2)(b) Employment law → Does national law specifically authorise? [Yes/No]
│  ├─ Art. 9(2)(g) Substantial public interest → Does national law provide basis? [Yes/No]
│  ├─ No Art. 9(2) exception identified → Processing cannot proceed
│  └─ Document Art. 9(2) condition and national law reference
│
├─ Step 4: Proportionality check
│  ├─ Is the biometric system targeted (specific areas/roles) or blanket (all employees)?
│  │  └─ Blanket deployment is more difficult to justify
│  ├─ Is an alternative non-biometric method available for objecting employees?
│  │  └─ Must be YES
│  ├─ Are safeguards adequate (encryption, template storage, retention, deletion)?
│  │  └─ Must be YES
│  └─ Decision: [ ] Proportionate → Proceed [ ] Disproportionate → Do not proceed
│
└─ END: Document assessment. If proceeding, conduct DPIA (Workflow 2).
```

## Workflow 2: Biometric System DPIA

### Phase 1: Screening (Day 1)
1. Biometric data is Art. 9(1) special category → DPIA is mandatory.
2. Assign DPIA reference: DPIA-BIO-[YEAR]-[SEQ].
3. Assemble team: HR, IT Security, DPO, Legal, Employee Representative.

### Phase 2: Description (Days 2-10)
1. Document biometric technology: fingerprint, facial recognition, iris, voice, behavioural.
2. Document technical processing: raw data capture → feature extraction → template generation → matching.
3. Document template storage: individual device (preferred) / centralised database.
4. Document data flow: enrolment → storage → authentication → retention → deletion.
5. Document employees in scope, locations, and alternative access methods.

### Phase 3: Risk Assessment (Days 10-20)
1. Assess risks:
   - Template compromise (biometric data cannot be changed if stolen)
   - Accuracy and bias (facial recognition error rates by demographic)
   - Function creep (access data used for performance monitoring)
   - Employee objection (religious, disability, personal)
   - Cross-border transfer of biometric templates
2. Rate each risk: Likelihood x Severity → Risk Level.

### Phase 4: Mitigation (Days 20-30)
1. Template storage on individual device (not centralised database).
2. Raw biometric data not stored — only derived templates.
3. System-specific template format (prevents cross-system matching).
4. AES-256 encryption at rest, TLS 1.3 in transit.
5. Liveness detection / anti-spoofing measures.
6. Alternative non-biometric access method always available.
7. Immediate deletion on termination, objection, or purpose cessation.

### Phase 5: Approval (Days 30-40)
1. DPO review and written advice.
2. Works council consultation (DE, FR, NL, AT, IT).
3. Senior management sign-off.
4. If residual risk remains Very High → Art. 36 prior consultation.

## Workflow 3: Employee Biometric Objection Handling

```
START: Employee objects to biometric enrolment
│
├─ Step 1: Acknowledge objection within 5 working days
│
├─ Step 2: Activate alternative access method immediately
│  ├─ PIN + proximity badge for access control
│  ├─ Manual sign-in for timekeeping
│  ├─ Password / smart card for device authentication
│  └─ No delay or disadvantage for the objecting employee
│
├─ Step 3: Record objection in privacy management system
│  ├─ Employee ID, date, nature of objection
│  ├─ Alternative method activated
│  ├─ No adverse notation in personnel file
│  └─ DPO notified for monitoring
│
├─ Step 4: If biometric data was previously enrolled
│  ├─ Delete biometric template immediately
│  ├─ Verify deletion from all systems and backups
│  ├─ Provide deletion confirmation to the employee
│  └─ Document in data deletion register
│
└─ END: Objection resolved. Alternative access in place. No adverse consequences.
```
