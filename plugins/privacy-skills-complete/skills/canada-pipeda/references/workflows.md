# PIPEDA Compliance Workflows

## Workflow 1: Access Request Processing

```
[Individual Access Request Received]
   (email, web portal, postal mail, in-person)
         |
         v
[Log Request]
   - Requester identity information
   - Date received
   - Channel of receipt
   - Reference number assigned
         |
         v
[Verify Identity of Requester]
   - Request government-issued ID or
   - Match against account credentials or
   - Knowledge-based verification (2+ data points)
         |
         v
[Identity Verified?]
   |--- No ---> Request additional proof
   |            (provide 30 days to respond)
   |
   |--- Yes ---> [Check Grounds for Refusal (Section 9(3))]
                  |--- Solicitor-client privilege?
                  |--- Formal dispute resolution data?
                  |--- Threat to life/security of another?
                  |--- Confidential commercial information?
                  |--- Collected for investigation under law?
                        |
                        v
                  [Any Refusal Grounds Apply?]
                  |--- Yes ---> Deny access (in full or part)
                  |             Provide written reasons
                  |             Inform of right to complain to OPC
                  |
                  |--- No ---> [Collect Information from All Systems]
                               - CRM, HR, billing, analytics, support
                                     |
                                     v
                               [Prepare Response Package]
                               - Existence of personal information held
                               - Description of use and disclosure history
                               - Copy of personal information
                               - Generally understandable format
                               - Minimal or no cost
                                     |
                                     v
                               [Deliver Response Within 30 Days]
                               - Secure delivery mechanism
                               - Confirm receipt
```

## Workflow 2: Consent Collection and Management

```
[New Collection Activity Identified]
         |
         v
[Identify Purpose(s) for Collection]
   - Document each purpose (Principle 2, Clause 4.2)
   - Ensure purposes are reasonable
         |
         v
[Assess Sensitivity of Information]
   |--- High sensitivity (health, financial, children, biometric)
   |    ---> Express consent required
   |
   |--- Medium sensitivity (employment, location)
   |    ---> Express or implied consent, context-dependent
   |
   |--- Low sensitivity (business contact, publicly available)
        ---> Implied consent or opt-out may be acceptable
         |
         v
[Does a Consent Exception Apply? (Section 7)]
   |--- Employment necessity (Section 7(1)(b))
   |--- Legal proceeding (Section 7(1)(c))
   |--- Publicly available information (Section 7(1)(d))
   |--- Journalistic, artistic, or literary purpose (Section 7(1)(c.1))
   |--- Emergency threat to life/health/security (Section 7(1)(a))
        |
        v
[No Exception?]
   ---> [Present Consent Request]
        - State purposes in clear language
        - Identify what information is collected
        - Identify with whom information is shared
        - Identify risks of harm (if applicable)
        - Offer clear yes/no choice
        - Allow withdrawal at any time
              |
              v
        [Record Consent]
        - Timestamp, purpose, mechanism, version
        - Link to privacy notice version
        - Store in consent management system
```

## Workflow 3: Breach Response (Division 1.1)

```
[Security Breach Detected]
         |
         v
[Contain the Breach]
   - Isolate affected systems
   - Preserve evidence
   - Engage incident response team
         |
         v
[Assess Real Risk of Significant Harm (RROSH)]
   Consider:
   - Sensitivity of information involved
   - Probability of misuse
   - Number of individuals affected
   - Type of breach (theft, loss, unauthorized access, accidental disclosure)
         |
         v
[RROSH Determination]
   |--- No RROSH ---> [Record Breach Internally]
   |                   - Maintain record for 24 months (Section 10.3)
   |                   - Document RROSH assessment reasoning
   |
   |--- RROSH Exists ---> [Report to OPC (Section 10.1)]
                           Contents required:
                           - Description of circumstances and cause
                           - Date or period of breach
                           - Description of personal information involved
                           - Number of affected individuals
                           - Steps taken to reduce/mitigate harm
                           - Whether individuals have been notified
                           - Contact person for OPC inquiries
                                 |
                                 v
                           [Notify Affected Individuals (Section 10.1(4))]
                           - As soon as feasible
                           - Direct notification preferred
                           - Contents: breach description, PI involved,
                             organization's mitigation steps, steps
                             individual can take, contact information
                                 |
                                 v
                           [Notify Other Organizations (Section 10.2)]
                           - If notification may reduce risk of harm
                           - Credit bureaus, financial institutions, etc.
                                 |
                                 v
                           [Maintain Breach Record for 24 Months]
                           - Available for OPC inspection on request
```

## Workflow 4: Cross-Border Transfer Assessment

```
[Transfer of Personal Information to Foreign Jurisdiction Proposed]
         |
         v
[Document Transfer Details]
   - Receiving organization identity and jurisdiction
   - Categories of personal information
   - Purpose of transfer
   - Volume and frequency
         |
         v
[Assess Foreign Jurisdiction]
   - Privacy law regime in receiving country
   - Government access or surveillance powers
   - Judicial oversight and rule of law
   - Organization's track record and security posture
         |
         v
[Implement Comparable Protections]
   - Contractual clauses requiring equivalent protection
   - Data processing agreement with Schedule 1 obligations
   - Audit rights and breach notification obligations
   - Limitation on onward transfers
         |
         v
[Update Privacy Policy]
   - Disclose that personal information may be transferred
   - Name the foreign jurisdiction(s)
   - State that information may be accessible to
     foreign governments under lawful authority
         |
         v
[Obtain Consent (if applicable)]
   - Informed consent including awareness of foreign access risk
   - For sensitive information: express consent required
         |
         v
[Monitor and Audit]
   - Periodic review of foreign processor compliance
   - Update transfer assessment if legal landscape changes
```
