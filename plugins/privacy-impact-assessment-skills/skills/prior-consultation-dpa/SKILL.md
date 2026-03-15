---
name: prior-consultation-dpa
description: >-
  Guides the Art. 36 prior consultation process when a DPIA indicates high
  residual risk that cannot be mitigated. Covers required documentation per
  Art. 36(3), the 8-week DPA response timeline, outcome management, and
  interaction protocols with supervisory authorities. Keywords: prior
  consultation, Art. 36, supervisory authority, DPA, high residual risk,
  DPIA escalation, consultation documentation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "prior-consultation, art-36, supervisory-authority, dpa, dpia-escalation"
---

# Conducting Prior Consultation with Supervisory Authority

## Overview

Article 36(1) requires the controller to consult the supervisory authority prior to processing where a DPIA under Art. 35 indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk. Prior consultation is the final safety net when a DPIA reveals risks that cannot be adequately mitigated through technical, organisational, or contractual measures. The supervisory authority has up to 8 weeks (extendable by 6 weeks) to provide written advice. Processing must not commence until the supervisory authority's response is received and addressed.

## When Prior Consultation Is Required

### Art. 36(1) Trigger

Prior consultation is mandatory when:
1. A DPIA has been conducted under Art. 35
2. The DPIA identifies that processing would result in high risk
3. The controller cannot sufficiently mitigate the risk through available measures
4. Residual risk remains High or Very High despite all reasonable mitigations

### Residual Risk Assessment

| Residual Risk Level | Action |
|---------------------|--------|
| Low | No prior consultation needed. Processing may proceed. |
| Medium | No prior consultation required, but DPO should document the acceptance rationale. |
| High | Prior consultation recommended. Processing should not proceed without SA review. |
| Very High | Prior consultation mandatory under Art. 36(1). Processing must not proceed. |

### Practical Examples Triggering Prior Consultation

- Large-scale biometric identification in publicly accessible areas where encryption with exporter-held key is not feasible
- AI system making automated decisions about access to essential services (credit, insurance, healthcare) where residual discrimination risk cannot be fully eliminated
- Processing of genetic data for a novel purpose where no existing Art. 9(2) exemption clearly applies
- Employee monitoring system where proportionality concerns remain despite all mitigations
- International transfer to a country with Very High government access risk where the processing requires clear-text data access

## Art. 36(3) Required Documentation

The controller must provide the supervisory authority with the following information:

| Document | Content | Art. 36(3) Reference |
|----------|---------|---------------------|
| DPIA report | Complete DPIA per Art. 35(7) including systematic description, necessity/proportionality, risk assessment, and mitigation measures | Art. 36(3)(a) — implicit |
| Controller and processor responsibilities | Clear documentation of which entity is responsible for which processing operations and security measures | Art. 36(3)(a) |
| Measures and safeguards | All technical, organisational, and contractual measures implemented to protect data subjects | Art. 36(3)(b) |
| DPO contact details | Contact details of the Data Protection Officer | Art. 36(3)(c) |
| Additional information requested | Any further information the supervisory authority requests during the consultation | Art. 36(3)(d) |

### Supplementary Documentation (Best Practice)

| Document | Purpose |
|----------|---------|
| Executive summary | 1-2 page summary of the processing, identified risks, and reasons for prior consultation |
| Data flow diagram | Visual representation of personal data flows through the processing |
| Risk register | Detailed risk register with inherent and residual risk levels |
| Mitigation measures schedule | Implementation status and timeline for all mitigations |
| DPO advice letter | Written DPO advice per Art. 35(2) and whether it was followed |
| Legitimate interest assessment | If processing relies on Art. 6(1)(f), the documented LIA |
| Art. 35(9) consultation evidence | Documentation of data subject views sought |

## Consultation Process

### Step 1: Preparation (Weeks 1-2)

1. DPO confirms that prior consultation is required based on DPIA residual risk assessment.
2. Processing owner compiles the Art. 36(3) documentation package.
3. DPO reviews the package for completeness and accuracy.
4. Legal counsel reviews for legal accuracy and strategic considerations.
5. Senior management is briefed on the prior consultation and its implications (processing pause).

### Step 2: Submission (Week 3)

1. Identify the competent supervisory authority:
   - Lead SA under one-stop-shop mechanism (Art. 56) for cross-border processing
   - Local SA for purely national processing
2. Submit the consultation package through the SA's designated channel (online portal, registered mail, or both per SA requirements).
3. Confirm receipt and obtain a case reference number.
4. Document the submission date — this starts the 8-week clock.

### Step 3: Supervisory Authority Review Period (Weeks 3-11)

Art. 36(2) timeline:
- **Standard period**: Up to 8 weeks from receipt of the complete consultation request
- **Extension**: The SA may extend the period by up to 6 weeks for complex cases, with notification to the controller within the first month
- **Total maximum**: 14 weeks (8 + 6)

During this period:
1. The SA may request additional information under Art. 36(3)(d). The 8-week clock pauses until the information is provided.
2. The DPO serves as the point of contact for SA communications.
3. Processing must not commence during the consultation period.
4. The controller should continue implementing mitigation measures in preparation.

### Step 4: Outcome Management

| SA Response | Controller Action |
|-------------|------------------|
| **Written advice with no concerns** | Document the SA's response. Proceed with processing. Update DPIA with SA clearance. |
| **Written advice with recommendations** | Implement the SA's recommendations. Update DPIA. Proceed with processing once recommendations are addressed. |
| **Written advice indicating GDPR infringement** | Do not proceed with processing as described. Review processing design to address SA concerns. Consider re-submission after modifications. |
| **No response within the statutory period** | SA silence does not constitute approval. The controller bears responsibility for demonstrating compliance. Proceed with caution, documenting the SA's non-response. |
| **Request for more information** | Provide the requested information promptly. The clock pauses. |

### Step 5: Post-Consultation

1. Document the entire consultation process and outcome in the DPIA register.
2. Update the DPIA with any SA recommendations or requirements.
3. If processing proceeds, implement all SA-recommended measures.
4. Schedule an accelerated DPIA review (6 months post-processing commencement).
5. Maintain the consultation documentation for supervisory authority inspection.

## National Supervisory Authority Consultation Procedures

| SA | Submission Method | Specific Requirements |
|----|------------------|----------------------|
| ICO (UK) | Online consultation request form | Include DPIA, data flow diagram, DPO contact, description of why risk cannot be mitigated |
| CNIL (France) | Online portal (teleservice.cnil.fr) | DPIA in CNIL format; French language required |
| BfDI (Germany) | Written submission to the competent state or federal DPA | German language; DPIA must reference BDSG provisions |
| Garante (Italy) | PEC (certified email) | Italian language; include DPIA, processor agreements, security measures documentation |
| AEPD (Spain) | Sede Electronica portal | Spanish language; include DPIA and all supporting documentation |
| DPC Ireland | Online submission through DPC website | English language; include DPIA and all Art. 36(3) documentation |

## Common Prior Consultation Mistakes

1. **Consulting too early**: Submitting before completing the DPIA and implementing all feasible mitigations. The SA expects to see that all reasonable measures have been taken.
2. **Consulting too late**: Beginning processing before the SA responds. Processing must not start during the consultation period.
3. **Incomplete documentation**: Submitting without all Art. 36(3) required documents, causing delays for information requests.
4. **No DPO involvement**: Submitting without documented DPO advice per Art. 35(2).
5. **Treating SA silence as approval**: SA non-response does not constitute approval or endorsement.
6. **Failing to implement SA recommendations**: Proceeding with processing without addressing SA feedback.

## Enforcement Context

- Art. 36(1) non-compliance (failure to consult when required) can result in administrative fines up to EUR 10 million or 2% of annual worldwide turnover under Art. 83(4)(a).
- **Swedish DPA vs Karolinska (2019)**: Fine included failure to conduct DPIA and consequent failure to identify need for prior consultation.
- **Norwegian DPA vs Municipality (2020)**: Enforcement action for proceeding with high-risk processing without prior consultation.
