# Workflows — US Federal Privacy Landscape

## Workflow 1: Federal Privacy Applicability Assessment

```
TRIGGER: Organisation needs to determine which federal privacy laws apply
  │
  ├─► Phase 1: Entity Classification
  │     ├─ Step 1.1: Health sector assessment
  │     │     ├─ Is the organisation a HIPAA covered entity?
  │     │     │     ├─ Health plan (insurer, HMO, employer-sponsored plan)
  │     │     │     ├─ Health care clearinghouse
  │     │     │     └─ Health care provider conducting standard electronic transactions
  │     │     ├─ Is the organisation a HIPAA business associate?
  │     │     │     └─ Performs functions involving PHI on behalf of a covered entity
  │     │     ├─ Does 42 CFR Part 2 apply?
  │     │     │     └─ Operates a substance use disorder treatment programme receiving federal funding
  │     │     └─ Does the FTC Health Breach Notification Rule apply?
  │     │           └─ Vendor of personal health records NOT covered by HIPAA
  │     │
  │     ├─ Step 1.2: Financial sector assessment
  │     │     ├─ Is the organisation a financial institution under GLBA?
  │     │     │     ├─ Bank, thrift, credit union
  │     │     │     ├─ Securities broker/dealer, investment adviser
  │     │     │     ├─ Insurance company
  │     │     │     └─ Other entity significantly engaged in financial activities
  │     │     │         (tax preparers, mortgage brokers, auto dealers with financing)
  │     │     ├─ Which regulator oversees GLBA compliance?
  │     │     │     ├─ OCC (national banks), Fed (state member banks)
  │     │     │     ├─ FDIC (state non-member banks), NCUA (credit unions)
  │     │     │     ├─ SEC (broker-dealers), CFTC (futures)
  │     │     │     └─ FTC (non-bank financial institutions)
  │     │     └─ Does FCRA apply?
  │     │           ├─ Consumer reporting agency
  │     │           ├─ User of consumer reports
  │     │           └─ Furnisher of information to consumer reporting agencies
  │     │
  │     ├─ Step 1.3: Children and education assessment
  │     │     ├─ Does COPPA apply?
  │     │     │     ├─ Website or online service directed to children under 13
  │     │     │     └─ Actual knowledge of collecting data from children under 13
  │     │     └─ Does FERPA apply?
  │     │           └─ Educational agency or institution receiving federal funding
  │     │
  │     ├─ Step 1.4: Communications assessment
  │     │     ├─ Does ECPA/Wiretap Act apply?
  │     │     │     └─ Intercepting, recording, or monitoring electronic communications
  │     │     ├─ Does the Stored Communications Act apply?
  │     │     │     └─ Providing electronic communication service or remote computing service
  │     │     └─ Does VPPA apply?
  │     │           └─ Video tape service provider (including streaming services)
  │     │
  │     └─ Step 1.5: FTC Section 5 baseline
  │           ├─ FTC jurisdiction applies unless entity is a common carrier,
  │           │   non-profit, bank, or other exempt entity under 15 U.S.C. 44-45
  │           └─ Document FTC jurisdiction status
  │
  └─► Phase 2: Compliance Obligation Mapping
        ├─ Step 2.1: For each applicable law, document:
        │     ├─ Specific regulatory requirements
        │     ├─ Data categories covered
        │     ├─ Individual rights obligations
        │     ├─ Security requirements
        │     ├─ Breach notification obligations
        │     ├─ Record-keeping requirements
        │     └─ Enforcement authority and penalties
        │
        ├─ Step 2.2: Identify overlap and preemption issues:
        │     ├─ HIPAA preemption of state health privacy laws
        │     ├─ GLBA preemption of state financial privacy laws
        │     ├─ FCRA preemption of state credit reporting laws
        │     └─ State comprehensive privacy law exemptions for federally regulated data
        │
        └─ Step 2.3: Create integrated compliance matrix
```

## Workflow 2: HIPAA Compliance Programme

```
TRIGGER: Organisation is a covered entity or business associate
  │
  ├─► Step 1: Privacy Rule Compliance
  │     ├─ Designate Privacy Officer
  │     ├─ Develop Notice of Privacy Practices (NPP)
  │     ├─ Implement minimum necessary standard for PHI use and disclosure
  │     ├─ Establish authorisation process for non-routine disclosures
  │     ├─ Implement individual rights:
  │     │     ├─ Access to PHI (within 30 days; 15 days for ePHI in EHR)
  │     │     ├─ Amendment of PHI
  │     │     ├─ Accounting of disclosures
  │     │     ├─ Request restrictions on use/disclosure
  │     │     ├─ Confidential communications
  │     │     └─ Right to receive breach notification
  │     └─ Execute business associate agreements (BAAs) with all business associates
  │
  ├─► Step 2: Security Rule Compliance
  │     ├─ Conduct risk analysis (required, not optional) — 45 CFR 164.308(a)(1)
  │     ├─ Implement administrative safeguards:
  │     │     ├─ Security management process
  │     │     ├─ Assigned security responsibility
  │     │     ├─ Workforce security
  │     │     ├─ Information access management
  │     │     ├─ Security awareness and training
  │     │     └─ Contingency plan
  │     ├─ Implement physical safeguards:
  │     │     ├─ Facility access controls
  │     │     ├─ Workstation use and security
  │     │     └─ Device and media controls
  │     └─ Implement technical safeguards:
  │           ├─ Access control (unique user identification, emergency access)
  │           ├─ Audit controls
  │           ├─ Integrity controls
  │           ├─ Person or entity authentication
  │           └─ Transmission security (encryption)
  │
  ├─► Step 3: Breach Notification Rule Compliance
  │     ├─ Establish breach detection and investigation procedures
  │     ├─ Conduct risk assessment per four-factor test:
  │     │     ├─ Nature and extent of PHI involved
  │     │     ├─ Unauthorised person who used PHI or to whom disclosure was made
  │     │     ├─ Whether PHI was actually acquired or viewed
  │     │     └─ Extent to which risk to PHI has been mitigated
  │     ├─ Notify individuals within 60 days for breaches affecting 500+ persons
  │     ├─ Notify HHS Secretary (annual log for <500; immediate for 500+)
  │     └─ Notify prominent media for breaches affecting 500+ in a state
  │
  └─► Step 4: Ongoing Compliance
        ├─ Conduct annual risk analysis update
        ├─ Maintain training programme for workforce members
        ├─ Review and update policies and procedures
        ├─ Monitor OCR enforcement actions and guidance
        └─ Conduct periodic internal audits
```

## Workflow 3: GLBA Safeguards Rule Compliance (Updated 2023)

```
TRIGGER: Organisation is a financial institution under GLBA
  │
  ├─► Step 1: Establish Information Security Programme
  │     ├─ Designate a Qualified Individual (CISO or equivalent)
  │     ├─ Conduct written risk assessment identifying threats to customer information
  │     ├─ Design and implement safeguards to control identified risks
  │     └─ Regularly test and monitor effectiveness of safeguards
  │
  ├─► Step 2: Implement Required Safeguards (2023 amendments)
  │     ├─ Access controls limiting who can access customer information
  │     ├─ Inventory of data, personnel, devices, systems, and facilities
  │     ├─ Encryption of customer information in transit and at rest
  │     ├─ Multi-factor authentication for any person accessing customer information
  │     ├─ Secure disposal of customer information within 2 years of last use
  │     ├─ Change management procedures
  │     ├─ Monitoring and logging of authorised user activity
  │     └─ Continuous monitoring or annual penetration testing plus
  │         semi-annual vulnerability assessments
  │
  ├─► Step 3: Incident Response
  │     ├─ Written incident response plan
  │     ├─ Incident response plan must address:
  │     │     ├─ Goals of the plan
  │     │     ├─ Internal processes for responding to a security event
  │     │     ├─ Clear roles, responsibilities, and decision-making authority
  │     │     ├─ Communication and information sharing processes
  │     │     ├─ Identification of remediation requirements
  │     │     ├─ Documentation and reporting
  │     │     └─ Post-incident analysis
  │     └─ Notify FTC within 60 days for events affecting 500+ consumers
  │
  └─► Step 4: Oversight and Reporting
        ├─ Qualified Individual reports in writing at least annually to board/governing body
        ├─ Report must include:
        │     ├─ Overall status of information security programme
        │     ├─ Material matters related to the programme
        │     └─ Recommendations for changes
        ├─ Evaluate service providers' ability to maintain safeguards
        └─ Include security requirements in service provider contracts
```

## Workflow 4: COPPA Compliance

```
TRIGGER: Website or online service directed to or knowingly collecting from children under 13
  │
  ├─► Step 1: Determine COPPA Applicability
  │     ├─ Is the site/service directed to children under 13?
  │     │     (consider subject matter, visual content, language, age of models,
  │     │      advertising, presence of child-oriented features)
  │     ├─ Does the operator have actual knowledge of collecting from children under 13?
  │     └─ Is the operator a third party collecting through a child-directed service?
  │
  ├─► Step 2: Implement COPPA Requirements
  │     ├─ Post clear, comprehensive privacy policy
  │     ├─ Provide direct notice to parents
  │     ├─ Obtain verifiable parental consent BEFORE collecting data
  │     │     ├─ Approved methods: signed consent form, credit card transaction,
  │     │     │   toll-free number, video conference, government ID verification,
  │     │     │   knowledge-based authentication, facial recognition comparison
  │     │     └─ Email consent permitted only for internal use (email plus method)
  │     ├─ Allow parents to review, delete, and refuse further collection
  │     ├─ Limit collection to what is reasonably necessary
  │     └─ Implement reasonable security measures
  │
  └─► Step 3: Ongoing Compliance
        ├─ Maintain records of consent for reasonable period
        ├─ Monitor FTC COPPA enforcement actions and FAQ updates
        ├─ Consider joining an FTC-approved COPPA Safe Harbor programme
        └─ Review age-gating mechanisms for effectiveness
```
