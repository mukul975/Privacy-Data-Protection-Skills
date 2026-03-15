# Anonymization as Retention Alternative Templates — Orion Data Vault Corp

## Anonymization Assessment Template

```
ANONYMIZATION ASSESSMENT
Reference: ANON-YYYY-NNN
Date: YYYY-MM-DD
Assessor:

SOURCE DATA:
- Data Category: [CAT-XXX]
- Records: [Count]
- Purpose for anonymized retention: [Statistical/Research/ML/Historical]
- Can purpose be achieved with anonymized data? [Yes/No]

TECHNIQUE SELECTION:
- Primary technique: [Name]
- Secondary technique: [Name]
- Validation method: [k-anonymity/l-diversity/t-closeness]

PARAMETERS:
- k-anonymity target: k = [value]
- l-diversity target: l = [value] (if applicable)
- t-closeness threshold: t = [value] (if applicable)
- Differential privacy epsilon: ε = [value] (if applicable)

QUASI-IDENTIFIERS TREATED:
| Field | Original | Generalized To |
|-------|----------|---------------|
| | | |

DIRECT IDENTIFIERS REMOVED:
| Field | Action |
|-------|--------|
| | Removed / Suppressed |

VALIDATION RESULTS:
- Singling out risk: [%] (threshold: <5%)
- Linkability test: [PASS/FAIL]
- Inference test: [PASS/FAIL]
- Motivated intruder test: [PASS/FAIL]
- Overall: [PASS/FAIL]

DECISION:
□ Anonymization effective — data outside GDPR scope
□ Anonymization insufficient — iterate with stronger parameters
□ Anonymization not feasible — retain as personal data

DPO Approval: _________________ Date: _________
```

## Anonymization Register Template

| Anon Ref | Source Category | Records | Technique | k-value | Re-ID Risk | Date | Next Review |
|----------|----------------|---------|-----------|---------|------------|------|-------------|
| | | | | | | | |

## Annual Re-Identification Risk Review Checklist

- [ ] New external data sources assessed for linkage potential
- [ ] Technology advances reviewed (AI, ML, de-anonymization research)
- [ ] Population/context changes assessed
- [ ] Singling out test re-run
- [ ] Linkability test re-run (with new data sources)
- [ ] Inference test re-run
- [ ] Re-identification risk still acceptable? [Yes/No]
- [ ] Action required? [None / Additional anonymization / Treat as personal data]
- [ ] Anonymization register updated
