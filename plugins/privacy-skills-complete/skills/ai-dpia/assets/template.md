# AI Data Protection Impact Assessment Template

## Organisation: Cerebrum AI Labs

---

## SECTION 1: AI SYSTEM IDENTIFICATION

| Field | Value |
|-------|-------|
| DPIA Reference Number | AI-DPIA-2026-___ |
| AI System Name | |
| System Owner | |
| DPO Reviewer | |
| Assessment Date | |
| Version | 1.0 |
| Status | Draft / Under Review / Approved |

---

## SECTION 2: AI SYSTEM DESCRIPTION (Art. 35(7)(a) Extended)

### 2.1 System Overview

| Element | Description |
|---------|-------------|
| Purpose of the AI system | |
| Business justification for using AI | |
| Model type and architecture | |
| Number of model parameters | |
| Explainability level | White-box / Grey-box / Black-box |
| Deployment type | Cloud-hosted / On-premises / Edge / Hybrid |

### 2.2 Training Data Sources

| Source Name | Type | Data Categories | Records | Lawful Basis | Art. 9 Data? | Art. 9(2) Condition |
|-------------|------|----------------|---------|--------------|--------------|---------------------|
| | First-party / Third-party / Public / Scraped | | | Art. 6(1)(a)-(f) | Yes / No | |
| | | | | | | |
| | | | | | | |

### 2.3 Inference Data

| Element | Description |
|---------|-------------|
| Data collected at inference | |
| Data subjects affected | |
| Volume of inference requests (daily/monthly) | |
| Output types | Classification / Score / Recommendation / Generated content |
| Output recipients | |

### 2.4 Data Flow Diagram

```
[Training Data Sources] → [Data Preprocessing] → [Model Training] → [Model Registry]
                                                                           ↓
[Inference Input] → [Preprocessing] → [Model Inference] → [Post-processing] → [Decision/Action]
                                                                                      ↓
                                                                              [Human Review?]
```

Attach detailed data flow diagram as appendix.

### 2.5 Infrastructure and Processors

| Component | Provider | Jurisdiction | Art. 28 Agreement | Transfer Mechanism |
|-----------|----------|-------------|-------------------|-------------------|
| Training compute | | | Yes / No | |
| Data storage | | | Yes / No | |
| Model hosting | | | Yes / No | |
| Labelling service | | | Yes / No | |
| Monitoring platform | | | Yes / No | |

---

## SECTION 3: AI ACT CLASSIFICATION

| Assessment Element | Response |
|-------------------|----------|
| Does the system fall under AI Act Art. 5 prohibited practices? | Yes / No |
| Is the system in an Annex III high-risk category? | Yes / No — Specify category: |
| AI Act risk classification | Unacceptable / High / Limited / Minimal |
| Conformity assessment required? | Yes / No |
| Conformity assessment reference | |

---

## SECTION 4: TRAINING DATA LAWFULNESS ASSESSMENT

### 4.1 Per-Source Assessment

For each training data source, complete:

**Source: _______________**

| Element | Assessment |
|---------|------------|
| Original collection purpose | |
| Is AI training compatible with original purpose? (Art. 6(4)) | Yes / No / N/A |
| Lawful basis for AI training | Art. 6(1)(a)-(f) — Specify: |
| If legitimate interest: balancing test completed? | Yes / No |
| If consent: does consent cover AI training? | Yes / No |
| Special category data present? | Yes / No |
| Art. 9(2) condition | |
| If web-scraped: EDPB heightened scrutiny documented? | Yes / No / N/A |
| Upstream lawful basis verified (third-party data)? | Yes / No / N/A |

### 4.2 Training Data Lawfulness Summary

| Source | Lawful Basis | Compliant? | Issues | Remediation |
|--------|-------------|------------|--------|-------------|
| | | Yes / No | | |
| | | Yes / No | | |

---

## SECTION 5: NECESSITY AND PROPORTIONALITY (Art. 35(7)(b))

| Assessment Question | Response |
|---------------------|----------|
| Is AI necessary for the stated purpose, or could simpler processing achieve it? | |
| Has the controller evaluated non-AI alternatives? | Yes / No |
| Why is AI required? | |
| Can acceptable performance be achieved with less personal data? | |
| Has the minimum dataset been determined (ablation study)? | Yes / No |
| Can synthetic data reduce personal data requirements? | Yes / No |
| Can federated learning reduce centralisation? | Yes / No |
| Can differential privacy reduce individual risk? | Yes / No |
| Are retention periods for training data justified? | |
| Are retention periods for inference logs justified? | |
| Can data subjects exercise rights effectively? | |

---

## SECTION 6: AI-SPECIFIC RISK ASSESSMENT (Art. 35(7)(c))

### 6.1 Risk Register

| Risk ID | Category | Description | Likelihood | Severity | Inherent Risk |
|---------|----------|-------------|------------|----------|---------------|
| R001 | Training Data Extraction | | Remote / Possible / Likely / Almost Certain | Negligible / Limited / Significant / Maximum | Low / Medium / High / Very High |
| R002 | Membership Inference | | | | |
| R003 | Model Inversion | | | | |
| R004 | Attribute Inference | | | | |
| R005 | Bias Amplification | | | | |
| R006 | Concept Drift Discrimination | | | | |
| R007 | Re-identification via Output | | | | |
| R008 | Automated Decision Errors | | | | |
| R009 | | | | | |

### 6.2 Technical Privacy Testing Results

| Test | Methodology | Result | Pass/Fail |
|------|------------|--------|-----------|
| Membership inference attack | Shadow model approach | | |
| Training data extraction | Canary insertion and extraction | | |
| Fairness metrics | Demographic parity / Equalized odds | | |
| Model confidence calibration | Expected calibration error | | |
| Output PII detection | PII scanner on sample outputs | | |

---

## SECTION 7: MITIGATION MEASURES (Art. 35(7)(d))

### 7.1 Technical Measures

| Risk ID | Measure | Implementation Status | Owner | Target Date |
|---------|---------|----------------------|-------|-------------|
| | Differential privacy (DP-SGD, ε = ___) | Planned / In Progress / Implemented | | |
| | Model output perturbation | | | |
| | Fairness constraints | | | |
| | Input/output PII filtering | | | |
| | Training data deduplication | | | |
| | Access controls (RBAC) | | | |

### 7.2 Organisational Measures

| Measure | Implementation Status | Owner | Target Date |
|---------|----------------------|-------|-------------|
| AI Ethics Review Board review | | | |
| Model card documentation | | | |
| Regular model privacy audit schedule | | | |
| Training data provenance records | | | |
| AI incident response procedures | | | |
| Staff training on AI privacy | | | |

### 7.3 Residual Risk Assessment

| Risk ID | Inherent Risk | Mitigations Applied | Residual Likelihood | Residual Severity | Residual Risk |
|---------|---------------|--------------------|--------------------|-------------------|---------------|
| | | | | | |
| | | | | | |

---

## SECTION 8: HUMAN OVERSIGHT ASSESSMENT

| Element | Assessment |
|---------|------------|
| Does the AI make solely automated decisions per Art. 22? | Yes / No |
| If yes, which Art. 22(2) exception applies? | Contract / Law / Explicit consent |
| Art. 22(3) safeguards implemented? | |
| Human oversight level | None / Nominal / Meaningful / Full |
| Can the reviewer meaningfully evaluate the AI recommendation? | Yes / No |
| Is sufficient time allocated for review? | Yes / No |
| Does the reviewer have expertise to identify errors? | Yes / No |
| Does the reviewer have authority to override? | Yes / No |
| Are automation bias countermeasures in place? | Yes / No |
| Override rate monitoring in place? | Yes / No |

---

## SECTION 9: DATA SUBJECT RIGHTS

| Right | Mechanism | Operational? |
|-------|-----------|-------------|
| Right to information about AI logic (Arts. 13-14) | | Yes / No |
| Right to explanation of AI decision | | Yes / No |
| Right to contest AI decision | | Yes / No |
| Right to human review of AI decision | | Yes / No |
| Right to erasure from training data | | Yes / No |
| Right of access to training data contribution | | Yes / No |
| Right to correction of AI output | | Yes / No |

---

## SECTION 10: OVERALL ASSESSMENT AND APPROVAL

| Element | Value |
|---------|-------|
| Overall inherent risk level | Low / Medium / High / Very High |
| Overall residual risk level | Low / Medium / High / Very High |
| Prior consultation required (Art. 36)? | Yes / No |
| DPO advice | |
| DPO advice accepted? | Yes / No — If no, reasons: |
| Data subject views sought (Art. 35(9))? | Yes / No — If no, justification: |

### Approval Signatures

| Role | Name | Signature | Date |
|------|------|-----------|------|
| AI System Owner | | | |
| Data Protection Officer | | | |
| Senior Management | | | |
| AI Ethics Board Chair | | | |

### Review Schedule

| Review Type | Date | Trigger |
|-------------|------|---------|
| Scheduled periodic review | [12 months from approval] | Annual review |
| Model retraining review | [As needed] | Retraining event |
| Incident-triggered review | [As needed] | AI privacy incident |

---

## APPENDICES

- [ ] Appendix A: Detailed data flow diagram
- [ ] Appendix B: Training data catalogue
- [ ] Appendix C: Model card
- [ ] Appendix D: Legitimate interest balancing test(s)
- [ ] Appendix E: Technical privacy testing report
- [ ] Appendix F: AI Act conformity assessment (if applicable)
- [ ] Appendix G: DPO written advice
- [ ] Appendix H: Data subject consultation records
