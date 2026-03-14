# Workflows — PII Detection in Unstructured Data

## Workflow 1: Enterprise Unstructured Data PII Scan

### Process Flow

```
START: Scheduled or on-demand scan of unstructured data repositories
  │
  ├─► Step 1: Source Identification and Prioritisation
  │     - Email systems (Exchange Online): last 90 days of messages
  │     - Document repositories (SharePoint, file shares): all active sites
  │     - Chat platforms (Teams): channels with customer-facing content
  │     - Application logs: last 30 days
  │     - Scanned document repositories: all images/scanned PDFs
  │     Output: Scan scope with prioritised source list
  │
  ├─► Step 2: Text Extraction
  │     For each source type:
  │     - Email: Microsoft Graph API → HTML body → plain text + attachment extraction
  │     - Office documents: Apache Tika or python-docx/openpyxl for text extraction
  │     - PDF: PyPDF2 for digital PDFs; OCR pipeline for scanned PDFs
  │     - Images: OCR pipeline (Tesseract or Azure AI Document Intelligence)
  │     - Logs: Direct text processing with line-by-line parsing
  │     - Chat: Platform API → message text extraction with thread context
  │     Output: Extracted text corpus with source metadata
  │
  ├─► Step 3: PII Detection
  │     Run Presidio Analyzer with configured recognisers:
  │     - NER model (spaCy en_core_web_trf): PERSON, ORG, GPE, DATE
  │     - Pattern recognisers: NINO, email, phone, IBAN, credit card, IP, DOB
  │     - Custom recognisers: Vanguard account numbers, employee IDs
  │     - Context enhancement: keyword proximity, section headers
  │     Output: Raw detection results with confidence scores
  │
  ├─► Step 4: Confidence Filtering and Deduplication
  │     - Apply confidence thresholds (HIGH > 85%, MEDIUM 70-84%)
  │     - Deduplicate findings (same PII entity across multiple documents)
  │     - Suppress known false positive patterns
  │     - Flag medium-confidence findings for human review
  │     Output: Filtered, deduplicated findings
  │
  ├─► Step 5: Classification and Labelling
  │     - Classify each PII finding by type and sensitivity
  │     - Map to classification tiers (Confidential, Restricted)
  │     - Apply sensitivity labels via Microsoft Purview where supported
  │     - Flag special category data (health terms, biometric indicators)
  │     Output: Classified and labelled findings
  │
  └─► Step 6: Reporting and Remediation
        - Generate scan report with findings by source, type, and confidence
        - Highlight high-risk findings (PII in unexpected locations)
        - Create remediation tasks for data in incorrect locations
        - Update data inventory with unstructured data PII locations
        Output: Scan report and remediation task list
```

## Workflow 2: DSAR Unstructured Data Search

### Process Flow

```
START: Data Subject Access Request received — unstructured data search required
  │
  ├─► Step 1: Identity Resolution
  │     - Extract data subject identifiers: name, email, account number, etc.
  │     - Build search query set: exact matches, name variants, email patterns
  │     Output: Search criteria for unstructured data sources
  │
  ├─► Step 2: Source-Specific Searches
  │     - Email: eDiscovery content search in Microsoft 365 Compliance Center
  │     - SharePoint: Full-text search with data subject identifiers
  │     - Teams: Compliance search across message history
  │     - File shares: Agent-based search with identifier patterns
  │     - Logs: Grep/pattern search for email, IP, user ID
  │     Output: Candidate documents/messages containing data subject's PII
  │
  ├─► Step 3: PII Verification
  │     - Run Presidio analyzer on candidate documents
  │     - Confirm detected PII belongs to the requesting data subject
  │     - Exclude PII of other data subjects (third-party data)
  │     Output: Verified data subject PII across unstructured sources
  │
  ├─► Step 4: Third-Party Redaction
  │     - Use Presidio Anonymizer to redact PII of other individuals
  │     - Manual review of edge cases (shared conversations, group emails)
  │     Output: Redacted documents ready for disclosure
  │
  └─► Step 5: DSAR Response Compilation
        - Compile all unstructured data findings with structured data
        - Organise by data category and source
        - Document search methodology for accountability
        Output: DSAR response package
```
