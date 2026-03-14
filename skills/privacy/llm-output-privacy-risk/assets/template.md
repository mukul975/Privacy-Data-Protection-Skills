# LLM Output Privacy Risk Assessment Template

## Organisation: Cerebrum AI Labs

| Field | Value |
|-------|-------|
| LLM System Name | |
| Model Version | |
| Assessment Date | |
| Assessor | |

## MODEL PROPERTIES

| Property | Value |
|----------|-------|
| Model Parameters | |
| Training Data Size | |
| Training Data PII Density | |
| Deduplication Applied | Yes / No |
| DP Training Applied | Yes / No |
| DP Epsilon (if applicable) | |
| Fine-Tuning Data Sources | |

## MEMORISATION TEST RESULTS

| Test ID | Prefix | Verbatim Match | Match Length | Verbatim Ratio | Status |
|---------|--------|---------------|-------------|----------------|--------|
| | | Yes/No | | | Pass/Fail |

## PROMPT INJECTION TEST RESULTS

| Test ID | Attack Type | Prompt Summary | Safe Response | PII Leaked | Notes |
|---------|------------|----------------|---------------|-----------|-------|
| | Direct/Indirect/System/Multi-turn/Jailbreak | | Yes/No | Yes/No | |

## OUTPUT PII SCANNING

| Property | Value |
|----------|-------|
| PII Scanner Deployed | Yes / No |
| Scanner Technology | |
| Scanner Recall | |
| Scanner Precision | |
| PII Categories Covered | |
| Action on Detection | Redact / Block / Flag / Log |

## HALLUCINATION ASSESSMENT

| Property | Value |
|----------|-------|
| Hallucination Rate | |
| Biographical Query Accuracy | |
| Factual Grounding Method | None / RAG / Knowledge Graph |
| Rectification Mechanism | |

## RISK SCORING

| Dimension | Weight | Score (0-100) | Risk Level |
|-----------|--------|--------------|------------|
| Memorisation Exposure | 25% | | |
| PII Leakage Likelihood | 25% | | |
| Prompt Injection Resilience | 20% | | |
| Hallucination Risk | 15% | | |
| Monitoring Coverage | 15% | | |
| **Overall** | **100%** | | |

## RECOMMENDATIONS

| Priority | Recommendation | Owner | Deadline |
|----------|---------------|-------|----------|
| | | | |

## APPROVAL

| Role | Name | Decision | Date |
|------|------|----------|------|
| ML Engineering Lead | | | |
| DPO | | | |
| IT Security | | | |

**Next Review**: _______________
