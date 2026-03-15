# LLM Output Privacy Risk — Workflows

## Workflow 1: LLM Output Privacy Risk Assessment

### Trigger
- New LLM deployment planned for production
- Existing LLM model updated or fine-tuned on new data
- Privacy audit scheduled for deployed LLM system

### Steps
1. **Training Data Audit**: Catalogue personal data categories present in training corpus; assess deduplication status and PII scrubbing coverage
2. **Memorisation Testing**: Run extractable memorisation tests using known training data prefixes; measure verbatim reproduction rate
3. **PII Leakage Testing**: Submit structured test prompts designed to elicit PII; scan outputs with NER and regex-based PII detectors
4. **Prompt Injection Testing**: Execute prompt injection test suite (direct injection, indirect injection, system prompt extraction, multi-turn extraction)
5. **Hallucination Assessment**: Test model outputs against known facts about real individuals; measure confabulation rate for biographical queries
6. **Risk Scoring**: Score each dimension (memorisation, leakage, injection resilience, hallucination, monitoring) and compute weighted overall risk
7. **Mitigation Planning**: For elevated/high/critical risk scores, define required mitigations and implementation timeline
8. **DPO Review**: DPO reviews assessment results and approves deployment or requires additional mitigations

### Output
- LLM Output Privacy Risk Assessment Report
- Risk score (0-100) with category breakdown
- Required mitigations with implementation plan
- DPO approval or conditional approval

## Workflow 2: Output PII Scanning Pipeline Setup

### Trigger
- LLM approved for deployment with PII scanning requirement
- Existing PII scanner requires update for new PII categories

### Steps
1. **PII Category Definition**: Define PII categories to detect (emails, phones, national IDs, credit cards, addresses, names, medical info)
2. **Scanner Configuration**: Configure NER models (spaCy, Presidio, or custom) and regex patterns for each PII category
3. **Action Rules**: Define action for each PII category (redact, block, flag for review, log only)
4. **Threshold Calibration**: Test scanner against labelled dataset; tune precision/recall trade-off (target: >95% recall for high-sensitivity PII, >90% precision)
5. **Integration**: Deploy scanner in output pipeline between LLM inference and user delivery
6. **Logging Setup**: Configure logging for all PII detections (timestamp, PII type, action taken, redacted content hash)
7. **Alert Configuration**: Set up alerts for anomalous PII detection rates (>0.1% of outputs per hour)
8. **Validation**: End-to-end test with synthetic PII to verify scanner, redaction, logging, and alerting

### Output
- Deployed PII scanning pipeline
- Scanner performance metrics (precision, recall, F1)
- Alert configuration documentation
- Validation test results

## Workflow 3: Prompt Injection Incident Response

### Trigger
- Prompt injection detection system flags suspicious input pattern
- User reports receiving output containing personal data
- PII scanner detects anomalous spike in PII-containing outputs

### Steps
1. **Triage**: Classify incident severity (confirmed PII exposure, suspected extraction attempt, false positive)
2. **Containment**: If confirmed PII exposure, immediately block the conversation and prevent further outputs to the user
3. **Impact Assessment**: Identify what personal data was exposed, whose data it was, and whether it was training data or hallucinated
4. **Evidence Preservation**: Preserve conversation logs, PII scanner logs, and model inference logs
5. **Breach Assessment**: Determine if the incident meets GDPR Art. 33 breach notification threshold (risk to rights and freedoms)
6. **Notification**: If breach threshold met, notify supervisory authority within 72 hours; notify affected data subjects if high risk (Art. 34)
7. **Remediation**: Update prompt injection detection rules, strengthen PII scanning, retrain alignment if needed
8. **Root Cause Analysis**: Determine whether leakage was from memorisation, hallucination, or filter bypass
9. **Post-Incident Review**: Document lessons learned and update risk assessment

### Output
- Incident report with severity classification
- Breach notification (if applicable)
- Updated prompt injection detection rules
- Remediation plan

## Workflow 4: Hallucinated PII Rectification

### Trigger
- Data subject reports that LLM generates false information about them
- Internal testing discovers model hallucinating facts about real individuals
- Media or external report of inaccurate AI-generated biographical information

### Steps
1. **Verification**: Confirm that the model generates inaccurate personal data about the identified individual
2. **Scope Assessment**: Test related prompts to understand the breadth of inaccurate information
3. **Documentation**: Record the inaccurate outputs and the correct information
4. **Immediate Mitigation**: Add the individual to a rectification blocklist; outputs mentioning them are flagged for accuracy review
5. **Model-Level Fix**: If feasible, apply targeted fine-tuning or prompt engineering to correct the model's knowledge
6. **Verification Testing**: Confirm the fix resolves the inaccuracy without introducing new issues
7. **Data Subject Response**: Inform the data subject of corrective measures taken (Art. 12 timeline: within one month)
8. **Monitoring**: Add ongoing monitoring for the specific individual to detect recurrence

### Output
- Rectification record
- Updated model or guardrail configuration
- Data subject notification
- Monitoring configuration
