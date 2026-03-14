# Legitimate Interest Assessment Workflow Reference

## LIA Initiation Workflow

1. **Processing owner request**: The business unit lead submits an LIA request to the DPO office when legitimate interest is identified as the potential lawful basis during the lawful basis assessment.
2. **Preliminary screening**: The DPO reviews the request to confirm that legitimate interest is a plausible basis (i.e., the controller is not a public authority performing its tasks, and no more specific basis is obviously applicable).
3. **Assign assessor**: The DPO assigns a privacy analyst or conducts the LIA personally for high-risk processing.
4. **Gather documentation**: Collect the processing description, data flow map, privacy notice, and any prior assessments or DPIAs related to the processing activity.
5. **Schedule stakeholder meeting**: Arrange a meeting with the processing owner and relevant technical staff to understand the processing in detail.

## Purpose Test Workflow

1. **Articulate the interest**: Ask the processing owner to describe the business need in one sentence. Document the stated interest.
2. **Classify the interest type**:
   - Commercial interest (revenue, cost reduction, competitive advantage)
   - Compliance interest (non-statutory but prudent controls, such as fraud prevention)
   - Societal interest (public benefit, research, safety)
   - Individual interest (exercise of fundamental rights, such as freedom of expression)
3. **Verify legality**: Confirm the interest is not prohibited by any applicable law, regulation, or court order.
4. **Assess specificity**: Reject vague formulations. "Improving our business" is insufficient. "Detecting fraudulent payment transactions to prevent financial loss to customers and the company" is sufficient.
5. **Check GDPR recognition**: Determine whether the interest is explicitly recognised in the GDPR recitals (Recitals 47-50) or case law, which strengthens the position.
6. **Record outcome**: Pass or fail with documented rationale.

## Necessity Test Workflow

1. **Map the processing steps**: Document every step involving personal data from collection to deletion.
2. **For each step, ask**:
   - Can this step be performed without personal data? If yes, remove personal data from that step.
   - Can this step use less personal data? If yes, minimise to the required fields.
   - Can this step use pseudonymised or aggregated data? If yes, implement pseudonymisation.
3. **Identify alternatives**: Document at least two alternative approaches that could achieve the same interest with less data or less intrusive processing. For each alternative, explain why it is or is not feasible.
4. **Proportionality check**: Compare the volume and sensitivity of data processed against the significance of the interest. High-volume processing for a minor interest fails proportionality.
5. **Record outcome**: Pass or fail with documented rationale and any modifications made to meet the necessity test.

## Balancing Test Workflow

1. **Map data subject impact**:
   - List all categories of data subjects affected.
   - For each category, assess: financial impact, emotional impact, social impact, physical safety impact, loss of control, and discrimination risk.
   - Rate each impact: negligible, minor, moderate, significant, severe.

2. **Assess reasonable expectations**:
   - How was the data collected? (directly from the subject, observed, inferred, from third parties)
   - What was the data subject told at collection?
   - Is there an existing relationship? How close?
   - Would a reasonable person in the data subject's position expect this processing?

3. **Evaluate vulnerability factors**:
   - Are any data subjects children (under 16/18 depending on Member State)?
   - Are data subjects in a position of dependency (employees, patients, tenants)?
   - Are data subjects members of a vulnerable group?

4. **Document safeguards in place or to be implemented**:

   | Safeguard | Implementation Detail |
   |-----------|---------------------|
   | Data minimisation | Only fields X, Y, Z are processed |
   | Pseudonymisation | Customer IDs replace names in analytics |
   | Access controls | RBAC restricting access to team of 5 analysts |
   | Retention limitation | Data deleted after 12 months |
   | Encryption | AES-256 at rest, TLS 1.3 in transit |
   | Transparency | Privacy notice updated, processing described |
   | Opt-out mechanism | Unsubscribe link / objection portal available |
   | Audit trail | All access logged and reviewed quarterly |

5. **Apply the balancing formula**:
   - If controller interest is HIGH and data subject impact is LOW/MODERATE with safeguards → balance likely favours controller.
   - If controller interest is MODERATE and data subject impact is MODERATE → safeguards become decisive; robust safeguards may tip the balance.
   - If data subject impact is HIGH or data subjects are vulnerable → balance likely favours data subject regardless of controller interest.
   - If sensitive data or children's data is involved → strong presumption in favour of data subject.

6. **Record outcome**: Pass or fail with full documented rationale.

## Post-Assessment Workflow

1. **Draft the LIA document**: Compile all three test outcomes, rationale, and safeguard commitments into the formal LIA template.
2. **DPO review and sign-off**: The DPO reviews the completed LIA and either approves, requests modifications, or rejects the legitimate interest basis.
3. **Implement safeguards**: All committed safeguards must be implemented before processing begins. The DPO verifies implementation.
4. **Update RoPA**: Record the lawful basis as Art. 6(1)(f) with a reference to the LIA document.
5. **Update privacy notice**: Ensure the privacy notice identifies the specific legitimate interest relied upon, as required by Art. 13(1)(d) and Art. 14(2)(b).
6. **Implement Art. 21 objection mechanism**: Ensure data subjects can exercise their right to object, and that the process for handling objections is documented.
7. **Set review date**: Schedule the next LIA review (annual minimum, or upon trigger events).

## Objection Handling Workflow

When a data subject exercises their Art. 21(1) right to object:

1. **Acknowledge receipt**: Confirm the objection within 48 hours.
2. **Assess grounds**: Can the controller demonstrate compelling legitimate grounds that override the data subject's interests, rights, and freedoms?
3. **If no compelling grounds**: Cease processing the objecting individual's data within 30 days. Confirm to the data subject.
4. **If compelling grounds exist**: Document the specific grounds and communicate to the data subject why processing continues, along with their right to lodge a complaint with the supervisory authority and seek judicial remedy.
5. **For direct marketing objections (Art. 21(2))**: Cease processing immediately without any assessment. The right is absolute.
6. **Record the objection and outcome**: Log in the data subject rights register with the decision rationale.
