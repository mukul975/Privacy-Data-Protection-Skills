# PII Detection Pipeline — Configuration Template

## Pipeline Configuration

| Parameter | Value |
|-----------|-------|
| Detection Engine | Presidio / spaCy / Pattern / AWS Macie |
| spaCy Model | en_core_web_lg / custom |
| Redaction Strategy | replace / mask / hash / redact |
| Minimum Confidence | |
| Custom Entities | |

## Entity Type Configuration

| Entity Type | Detection Method | Confidence Threshold | Action |
|------------|-----------------|---------------------|--------|
| PERSON | NER | 0.80 | Redact |
| EMAIL | Pattern | 0.95 | Redact |
| PHONE | Pattern | 0.75 | Redact |
| SSN | Pattern + checksum | 0.90 | Redact + Alert |
| CREDIT_CARD | Pattern + Luhn | 0.90 | Redact + Alert |
| IP_ADDRESS | Pattern | 0.85 | Redact |

## Scan Results

| Data Source | Records Scanned | Detections | High Risk Files | Action Taken |
|------------|----------------|------------|-----------------|-------------|
| | | | | |

## Sign-Off

| Role | Name | Date |
|------|------|------|
| Privacy Engineer | | |
| Data Steward | | |
| CISO | | |
