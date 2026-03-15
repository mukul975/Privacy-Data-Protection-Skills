# Healthcare AI Privacy Assessment — Template

## AI System Information

| Field | Value |
|-------|-------|
| System Name | |
| Version | |
| Vendor / Developer | |
| Clinical Use Case | |
| Deployment Date | |
| Assessment Date | |

---

## Regulatory Classification

| Framework | Classification | Notes |
|-----------|---------------|-------|
| AI Act | [ ] Unacceptable [ ] High-Risk [ ] Limited [ ] Minimal | |
| FDA | [ ] SaMD (510k/De Novo/PMA) [ ] CDS Exempt [ ] Not SaMD | |
| HIPAA | [ ] Processes PHI [ ] De-identified only | |

---

## Training Data Governance

- [ ] Lawful basis for PHI use documented: _______________
- [ ] Minimum necessary assessment completed
- [ ] De-identification applied: [ ] Safe Harbor [ ] Expert Determination [ ] N/A
- [ ] Data Use Agreement in place (if limited data set)
- [ ] Training data encrypted at rest (AES-256)
- [ ] Access-controlled training environment
- [ ] Audit logging of all data access
- [ ] Training data retention policy (delete within 90 days of model finalization)

---

## Privacy Attack Testing

| Attack Type | Tested | Result | Mitigation Applied |
|------------|--------|--------|-------------------|
| Membership inference | [ ] | | |
| Training data extraction | [ ] | | |
| Model inversion | [ ] | | |
| Attribute inference | [ ] | | |
| Explanation leakage | [ ] | | |

---

## Transparency and Patient Rights

- [ ] NPP updated to disclose AI use in treatment/operations
- [ ] AI-generated content labeled in EHR
- [ ] Patient-facing explanation available
- [ ] Clinician model card with limitations and failure modes
- [ ] Right of access covers AI-generated records
- [ ] Override/opt-out mechanism available

---

## Bias Monitoring

- [ ] Pre-deployment performance disaggregated by demographics
- [ ] Monthly automated bias monitoring configured
- [ ] Quarterly clinical outcome correlation analysis planned
- [ ] Annual independent bias audit scheduled
- [ ] Disparate impact threshold defined: <80% rule

---

## Approval

| Role | Name | Date |
|------|------|------|
| Privacy Officer | | |
| CISO | | |
| Chief Medical Informatics Officer | | |
| AI Ethics Committee Chair | | |
