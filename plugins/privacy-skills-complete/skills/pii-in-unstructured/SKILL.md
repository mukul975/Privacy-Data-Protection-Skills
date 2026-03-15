---
name: pii-in-unstructured
description: >-
  Detects PII in unstructured data including emails, documents, images, and logs
  using NER-based detection with spaCy and Microsoft Presidio, regex patterns,
  OCR integration, and confidence scoring. Keywords: PII detection, unstructured
  data, NER, spaCy, Presidio, OCR, regex, email scanning, document scanning.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "pii-detection, unstructured-data, ner, spacy, presidio, ocr, regex"
---

# PII Detection in Unstructured Data

## Overview

Unstructured data — emails, documents, images, chat logs, call transcripts, and system logs — accounts for an estimated 80% of enterprise data and presents the greatest challenge for privacy compliance. Unlike structured databases where personal data resides in known columns, unstructured data contains PII embedded in free text, attached files, scanned images, and metadata. This skill covers detection approaches using Named Entity Recognition (NER), pattern matching, OCR, and hybrid pipelines, with focus on Microsoft Presidio and spaCy as implementation frameworks.

## Unstructured Data Sources at Vanguard Financial Services

| Source | Volume | PII Risk | Detection Challenge |
|--------|--------|----------|-------------------|
| **Email (Exchange Online)** | 2.1M messages/month | HIGH — names, account numbers, financial data in body and attachments | Mixed text and attachments; forwarded chains contain accumulated PII |
| **SharePoint documents** | 4.2TB across 1,200 sites | HIGH — contracts, KYC docs, customer correspondence | Multiple formats (docx, pdf, xlsx); embedded images |
| **Teams chat** | 890K messages/month | MEDIUM — casual references to customers, internal discussions | Short messages, abbreviations, context-dependent PII |
| **Application logs** | 50GB/day | MEDIUM — IP addresses, user IDs, error messages with PII | High volume, mixed with non-PII technical data |
| **Scanned documents** | 45K pages/month | HIGH — passport scans, signed contracts, medical certificates | Requires OCR; variable image quality |
| **Call transcripts** | 8K transcripts/month | HIGH — customers state names, account numbers, personal details | Speech-to-text errors, colloquial language |
| **PDF reports** | 12K documents/month | MEDIUM — financial reports may contain customer lists | Embedded tables, charts with PII labels |

## Detection Architecture

### Microsoft Presidio Pipeline

Presidio is an open-source PII detection and anonymisation SDK developed by Microsoft, designed for integration with enterprise data pipelines.

```
Input Text/Document
       │
       ▼
┌──────────────────┐
│  Pre-processing  │  Format conversion, encoding normalisation,
│  (text extract)  │  OCR for images/scanned PDFs
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Presidio        │  Multiple recognisers run in parallel:
│  Analyzer        │  - NER model (spaCy/transformers)
│                  │  - Pattern recognisers (regex)
│                  │  - Custom recognisers (org-specific)
│                  │  - Context-aware enhancers
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Confidence      │  Each detection assigned confidence score
│  Scoring &       │  Threshold filtering applied
│  Filtering       │  Context enhancement boosts/reduces scores
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Results         │  PII locations, types, confidence scores
│  (structured)    │  Ready for classification, redaction, or alerting
└──────────────────┘
```

### Component Details

**NER Model (spaCy/Transformers)**:
- spaCy `en_core_web_trf` model (transformer-based) for English NER
- Detects: PERSON, ORG, GPE, DATE, MONEY, CARDINAL entities
- Custom-trained NER for financial domain entities (IBAN, account numbers)

**Pattern Recognisers (Regex)**:
- UK National Insurance Number: `[A-CEGHJ-PR-TW-Z]{2}\d{6}[A-D]`
- Email address: `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
- UK phone number: `(?:0|\+44)\d{10,11}`
- IBAN: `[A-Z]{2}\d{2}[A-Z0-9]{4}\d{7}([A-Z0-9]?){0,16}`
- Credit card: `\b(?:\d{4}[-\s]?){3}\d{4}\b` (with Luhn validation)
- IP address (v4): `\b(?:\d{1,3}\.){3}\d{1,3}\b`
- Date of birth patterns: `\b\d{2}[/-]\d{2}[/-]\d{4}\b`
- Vanguard account: `VFS-\d{10}`
- ICD-10 code: `[A-Z]\d{2}\.\d{1,4}`

**Context-Aware Enhancement**:
- Keyword proximity: if "National Insurance" appears within 50 characters of a NINO pattern, boost confidence by 15%
- Section headers: if detected within a section titled "Personal Details" or "Patient Information", boost confidence by 10%
- Negative context: if pattern appears within code blocks, SQL queries, or configuration files, reduce confidence by 25%

## OCR Integration for Scanned Documents

### Pipeline for Image-Based PII Detection

```
Scanned Document / Image
       │
       ▼
┌──────────────────┐
│  Pre-processing  │  Deskew, denoise, contrast enhancement,
│  (image)         │  resolution upscaling (if < 300 DPI)
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  OCR Engine      │  Tesseract OCR (open-source) or
│                  │  Azure AI Document Intelligence (cloud)
│                  │  Output: extracted text with bounding boxes
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Presidio        │  Standard NER + pattern detection
│  Analyzer        │  on OCR-extracted text
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  Confidence      │  Adjust for OCR quality:
│  Adjustment      │  OCR confidence < 80% → reduce PII confidence by 20%
│                  │  OCR confidence > 95% → no adjustment
└──────────────────┘
```

### Document Type Detection for Vanguard

| Document Type | OCR Strategy | Expected PII |
|--------------|-------------|-------------|
| Passport scan | Azure AI Document Intelligence (ID document model) | Full name, DOB, nationality, passport number, photo (biometric) |
| Utility bill | General OCR + address pattern recognition | Full name, address, account number |
| Medical certificate | General OCR + health NER model | Name, diagnosis, doctor name, dates |
| Signed contract | General OCR + contract template matching | Names, addresses, financial terms, signatures |
| Cheque image | Banking-specific OCR model | Name, account number, sort code, amount |

## Confidence Scoring Framework

### Score Composition

| Component | Weight | Description |
|-----------|--------|-------------|
| **Pattern match confidence** | 40% | Regex pattern specificity and validation (e.g., Luhn check for credit cards) |
| **NER model confidence** | 30% | Model probability score for entity classification |
| **Context enhancement** | 20% | Keyword proximity, section header, document type |
| **Source quality** | 10% | OCR quality score, document resolution, text extraction confidence |

### Confidence Thresholds

| Confidence Level | Score Range | Action |
|-----------------|-------------|--------|
| **HIGH** | 85-100% | Auto-classify and auto-label; include in discovery report |
| **MEDIUM** | 70-84% | Queue for human review; include in discovery report as pending |
| **LOW** | 50-69% | Log for audit; do not auto-classify; available for bulk review |
| **BELOW THRESHOLD** | < 50% | Suppress; do not report unless specifically queried |

## Implementation Patterns

### Pattern 1: Email Scanning Pipeline

```python
# Conceptual pipeline for Exchange Online email scanning
# 1. Microsoft Graph API retrieves email messages
# 2. Extract body text (HTML → plain text conversion)
# 3. Extract attachment text (document parsing)
# 4. Run Presidio analyzer on combined text
# 5. Map findings to email metadata (sender, recipients, date)
# 6. Apply classification labels via Microsoft Purview
```

### Pattern 2: Log File Scanning

For application logs, specific patterns dominate:
- IP addresses in access logs
- User IDs and session tokens in authentication logs
- Email addresses in error messages
- Stack traces containing file paths with usernames

Log scanning requires higher false-positive tolerance and volume-optimised processing.

### Pattern 3: Chat Message Scanning

Teams/Slack messages present unique challenges:
- Short messages with minimal context
- Abbreviations and informal language
- Customer names mentioned without surrounding keywords
- Account numbers shared in fragments across messages

Strategy: scan message threads rather than individual messages to capture context.

## Accuracy Benchmarks

### Expected Performance by Data Source

| Source | Precision Target | Recall Target | Key Challenges |
|--------|-----------------|---------------|---------------|
| Email body text | > 92% | > 88% | Forwarded chains, signatures, disclaimers |
| SharePoint documents (Office formats) | > 90% | > 85% | Embedded tables, headers/footers |
| Scanned documents (OCR) | > 85% | > 80% | OCR errors, handwriting, poor image quality |
| Application logs | > 88% | > 82% | IP address over-detection, reference number ambiguity |
| Chat messages | > 80% | > 75% | Short context, informal language, abbreviations |
| Call transcripts | > 82% | > 78% | Speech-to-text errors, overlapping speech, accents |

## Integration Points

- **auto-data-discovery**: Unstructured PII detection complements structured data discovery platforms
- **data-labeling-system**: Detected PII drives automatic sensitivity label application
- **classification-policy**: Detection results feed into classification tier assignment
- **data-inventory-mapping**: Unstructured PII findings expand the data inventory to include document repositories and email systems
