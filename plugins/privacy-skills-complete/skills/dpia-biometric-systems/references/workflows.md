# Workflow -- DPIA for Biometric Systems

## Phase 1: Pre-Assessment and Scoping

### Step 1.1: Determine DPIA Obligation
- Confirm biometric data is processed for unique identification (Art. 9(1) trigger)
- Check against national DPA DPIA blacklist (CNIL List 11, ICO guidance, AEPD list, BfDI list)
- Identify EDPB WP248rev.01 criteria met (special category + at least one other)
- Document conclusion: mandatory DPIA confirmed / not required with rationale

### Step 1.2: Assemble DPIA Team
- Appoint DPIA lead (typically Privacy/DPO office)
- Engage DPO for mandatory consultation under Art. 35(2)
- Include biometric system vendor/integrator for technical input
- Include IT security for infrastructure and template protection assessment
- Include HR/operations for necessity and proportionality input
- Include employee representatives / works council where required by national law

### Step 1.3: Define Assessment Scope
- Identify all biometric modalities in scope (fingerprint, facial, iris, voice, behavioural)
- Map all processing locations and data flows
- Identify all categories of data subjects
- Determine whether 1:1 (verification) or 1:N (identification) processing
- Document system boundaries and integration points

## Phase 2: Processing Description (Art. 35(7)(a))

### Step 2.1: Document System Architecture
- Biometric capture devices: manufacturer, model, sensor specifications
- Template extraction: algorithm vendor, version, ISO 19795 compliance status
- Template storage: on-device, local database, centralised database, cloud
- Matching engine: location, 1:1 or 1:N mode, matching threshold settings
- Decision output: access granted/denied, time recorded, alert generated
- Integration: access control systems, HR/payroll, CCTV, visitor management

### Step 2.2: Map Data Flows
- Raw biometric capture (image, audio, signal) at enrollment
- Feature extraction and template generation
- Template transmission to storage location
- Matching request flow (capture point to matching engine)
- Decision result flow (matching engine to access control / time system)
- Audit log generation and storage
- Template deletion and lifecycle events

### Step 2.3: Document Data Subject Information
- Number of enrolled individuals (current and projected)
- Categories: employees, contractors, visitors, customers, patients
- Vulnerable groups: employees (power imbalance), children, patients
- Geographic scope: single site, multi-site, cross-border
- Daily transaction volume

## Phase 3: Necessity and Proportionality (Art. 35(7)(b))

### Step 3.1: Assess Lawful Basis
- Identify Art. 6(1) basis for processing (consent, legal obligation, legitimate interest, contract, public interest)
- Identify Art. 9(2) exception for special category biometric data
- For employment context: assess whether consent is freely given (WP29 Opinion 2/2017 power imbalance guidance)
- For public context: identify Member State law basis for public interest processing
- Document legal basis with specific statutory references

### Step 3.2: Conduct Necessity Test
- Define specific, concrete purpose (reject vague purposes like "security" or "efficiency")
- Evaluate less intrusive alternatives systematically:
  - Badge/proximity card + PIN for access control
  - Smart card + password for device authentication
  - Manual sign-in for time and attendance
  - Supervisor verification for identity confirmation
- Document why each alternative is insufficient with evidence (incident reports, audit findings)
- Confirm processing is limited to minimum necessary (no function creep scope)

### Step 3.3: Assess Proportionality
- Compare severity of security risk against intrusiveness of biometric processing
- Assess scope: targeted (specific areas/roles) vs blanket (organisation-wide)
- Confirm alternative non-biometric method exists for objecting individuals
- Assess retention: templates deleted at earliest possible point
- Document proportionality conclusion with reasoning

## Phase 4: Risk Assessment (Art. 35(7)(c))

### Step 4.1: Identify Biometric-Specific Risks
- Template breach and irrevocability (biometric data cannot be reset)
- Function creep (access control data repurposed for monitoring/profiling)
- Discrimination (demographic accuracy disparities)
- Covert collection (passive biometrics without active participation)
- Cross-system linkage (template matching across unrelated databases)
- Spoofing and presentation attacks
- Chilling effect on employee behaviour
- Vendor lock-in and data portability failure

### Step 4.2: Assess Likelihood and Severity
- For each risk, assess likelihood: Negligible (1), Low (2), Medium (3), High (4)
- For each risk, assess severity: Negligible (1), Low (2), Medium (3), High (4)
- Calculate inherent risk score: Likelihood x Severity
- Map to risk level: Low (1-3), Medium (4-6), High (7-9), Very High (10-16)
- Document risk assessment rationale with reference to enforcement precedents

### Step 4.3: Document Risk Register
- Assign unique risk ID to each identified risk
- Record risk description, category, likelihood, severity, inherent score, and level
- Link risks to specific system components and data flows
- Identify risk owners

## Phase 5: Mitigation Measures (Art. 35(7)(d))

### Step 5.1: Design Technical Safeguards
- Template protection per ISO/IEC 24745 (irreversibility, unlinkability, renewability)
- Storage hierarchy per CNIL guidance (on-device preferred over centralised)
- Encryption: AES-256 at rest, TLS 1.3 in transit
- Liveness detection per ISO/IEC 30107 (anti-spoofing)
- Network isolation: biometric system on dedicated VLAN
- Audit logging: immutable logs for all biometric events
- Demographic accuracy testing: validated across representative population groups

### Step 5.2: Design Organisational Safeguards
- Alternative non-biometric access method for all data subjects
- Employee objection procedure with no adverse consequences
- Template deletion upon termination, objection, or purpose cessation
- Vendor Art. 28 DPA with biometric-specific clauses
- Operator training on biometric system and data protection obligations
- Annual DPIA review cycle
- Biometric-specific breach response procedure

### Step 5.3: Calculate Residual Risk
- Re-assess likelihood and severity after applying all planned measures
- Calculate residual risk scores
- Compare against organisational risk appetite
- If residual risk remains High or Very High: prepare Art. 36 prior consultation

## Phase 6: Consultation and Approval

### Step 6.1: DPO Consultation (Art. 35(2))
- Present complete DPIA to DPO for review
- DPO provides written advice on: lawful basis adequacy, necessity test rigour, safeguard sufficiency
- Document DPO advice and controller's response to each recommendation
- If DPO and controller disagree: document disagreement and controller's rationale

### Step 6.2: Data Subject Consultation (Art. 35(9))
- Where appropriate, seek views of data subjects or their representatives
- For employee biometrics: consult works council or employee representatives
- For customer biometrics: conduct user testing or focus groups
- Document views received and how they influenced the DPIA outcome

### Step 6.3: Art. 36 Prior Consultation (if required)
- Prepare submission package: complete DPIA, DPO advice, data subject views
- Submit to lead supervisory authority
- SA has 8 weeks to respond (extendable by 6 weeks for complex cases)
- Do not commence biometric processing until SA response received

### Step 6.4: Final Approval and Sign-Off
- DPIA approved by controller (senior management)
- DPO sign-off confirming adequate assessment
- CISO sign-off confirming technical safeguard adequacy
- Document approval with dates and signatories
- Publish DPIA summary (where required by transparency obligations)

## Phase 7: Ongoing Monitoring

### Step 7.1: Periodic Review
- Review DPIA annually or upon significant system change
- Re-assess risks when biometric vendor updates algorithms
- Re-assess when expanding to new biometric modalities or locations
- Re-assess when data subject population changes significantly

### Step 7.2: Incident Response
- Biometric template breach triggers enhanced notification (emphasise irrevocability)
- Art. 33 notification within 72 hours to supervisory authority
- Art. 34 notification to data subjects with guidance on protective measures
- Post-incident DPIA update incorporating lessons learned
