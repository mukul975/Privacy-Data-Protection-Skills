# Health Data PIA — Workflows

## Workflow 1: Health Data Classification
1. Inventory all data elements in the processing activity.
2. Classify each element: clinical data, administrative health data, genetic/genomic data, mental health data, substance use data, biometric health data.
3. Determine sensitivity tier: Tier 1 (routine clinical), Tier 2 (sensitive diagnoses — mental health, HIV, STI, substance use), Tier 3 (genetic/genomic, uniquely identifying).
4. Identify applicable regulatory regime for each data element (GDPR Art. 9, HIPAA PHI, 42 CFR Part 2).
5. Document classification in the data inventory register.

## Workflow 2: Lawful Basis and Art. 9(2) Exception Determination
1. For each health data processing activity, identify the GDPR Art. 6 lawful basis.
2. Identify the applicable Art. 9(2) exception: explicit consent (a), employment (b), vital interests (c), health care provision (h), public health (i), or research (j).
3. For consent-based processing, verify consent is explicit, specific, informed, and freely given.
4. For Art. 9(2)(h) health care provision, verify processing is by or under the responsibility of a health professional subject to professional secrecy.
5. For Art. 9(2)(j) research, verify Art. 89(1) safeguards are in place (pseudonymisation, data minimisation, ethics approval).
6. Document the determination with supporting evidence.

## Workflow 3: Access Control Assessment
1. Inventory all user roles with access to health data.
2. Verify role-based access control (RBAC) implements principle of least privilege.
3. Review break-glass/emergency access procedures and post-access audit trail.
4. Verify two-factor authentication for health data access.
5. Check audit logging: who accessed what record, when, and for what purpose.
6. Review log monitoring frequency and anomaly detection capability.
7. Document access control findings and remediation actions.

## Workflow 4: De-identification Assessment (HIPAA)
1. Determine if data can be de-identified using HIPAA Safe Harbor (remove 18 identifiers) or Expert Determination methods.
2. For Safe Harbor: verify removal of all 18 identifier categories and no actual knowledge of re-identification risk.
3. For Expert Determination: engage qualified statistical expert to certify that re-identification risk is very small.
4. Document the de-identification method, date, and responsible person.
5. Implement controls to prevent re-identification of de-identified datasets.

## Workflow 5: Health Data Breach Response
1. Detect and classify the health data breach (PHI or Art. 9 data involved).
2. Assess the nature of data compromised and number of individuals affected.
3. Notify supervisory authority within 72 hours (GDPR) or 60 days (HIPAA/HITECH).
4. Notify affected individuals: GDPR requires notification if high risk; HIPAA requires notification for unsecured PHI breaches (>500 individuals requires media notification).
5. For 42 CFR Part 2 data: apply heightened breach response requirements.
6. Document breach in register and conduct root cause analysis.
7. Report to HHS OCR Breach Portal (HIPAA) if applicable.

## Workflow 6: Cross-Border Health Data Transfer
1. Identify all transfers of health data across jurisdictional boundaries.
2. For GDPR: apply Chapter V transfer mechanisms (adequacy, SCCs, BCRs, Art. 49 derogations).
3. For HIPAA: verify BAA covers international processing by business associates.
4. Conduct transfer impact assessment with heightened scrutiny for health data.
5. Implement supplementary measures (encryption, pseudonymisation, access restrictions) if necessary.
6. Document transfer safeguards and review annually.
