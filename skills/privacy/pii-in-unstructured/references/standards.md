# Standards and Regulatory References — PII Detection in Unstructured Data

## Primary Legislation

### GDPR — Regulation (EU) 2016/679

- **Article 4(1)**: Personal data definition applies regardless of format — structured databases, free-text documents, images, and audio all fall within scope if they contain information relating to an identifiable natural person.
- **Article 5(1)(d)**: Accuracy principle — controllers must maintain accurate personal data. Detecting PII in unstructured data is prerequisite to ensuring its accuracy.
- **Article 15**: Right of access — data subject access requests require identifying ALL personal data across ALL formats, including unstructured documents, emails, and images.
- **Article 17**: Right to erasure — erasure requests must cover PII in unstructured repositories, not just structured databases.
- **Article 32**: Security of processing — appropriate technical measures include detecting and protecting PII wherever it resides, including unstructured data stores.

## Regulatory Guidance

### ICO — Subject Access Requests Code of Practice (2023)

- **Section 5.3**: Controllers must conduct reasonable and proportionate searches across all data repositories, including email, documents, and other unstructured sources, to fulfil data subject access requests.
- **Section 5.7**: Automated search tools are recommended for large-scale DSAR fulfilment, but results should be reviewed for accuracy before disclosure.

### EDPB Guidelines 01/2022 on Data Subject Rights — Right of Access (2022)

- **Section 4.2**: The scope of the right of access encompasses all personal data regardless of storage format. Controllers must search structured and unstructured data sources.

### NIST SP 800-188 — De-Identifying Government Datasets (2016)

- **Section 3.4**: Guidance on identifying PII in unstructured text, including patterns for names, addresses, phone numbers, and identification numbers. Recommends combination of NER and pattern matching.

## Technical Standards

### Microsoft Presidio — Open Source PII Detection

- **Repository**: github.com/microsoft/presidio
- **Components**: Presidio Analyzer (detection), Presidio Anonymizer (redaction/masking), Presidio Image Redactor (image PII detection)
- **Recognisers**: 30+ built-in recognisers for common PII types, custom recogniser API for organisation-specific patterns
- **NLP Engines**: Supports spaCy, Stanza, and Hugging Face transformers as NER backends
- **Licence**: MIT

### spaCy — Industrial-Strength NLP

- **Repository**: github.com/explosion/spaCy
- **Models**: `en_core_web_sm` (small, fast), `en_core_web_lg` (large, accurate), `en_core_web_trf` (transformer-based, highest accuracy)
- **Entity Types**: PERSON, NORP, FAC, ORG, GPE, LOC, PRODUCT, EVENT, WORK_OF_ART, LAW, LANGUAGE, DATE, TIME, PERCENT, MONEY, QUANTITY, ORDINAL, CARDINAL
- **Performance**: en_core_web_trf achieves F1 > 0.90 on OntoNotes 5 NER benchmark
- **Licence**: MIT

### Tesseract OCR

- **Repository**: github.com/tesseract-ocr/tesseract
- **Version**: 5.x (LSTM-based recognition engine)
- **Languages**: 100+ languages supported
- **Accuracy**: 95%+ on clean printed text at 300+ DPI; degrades significantly below 200 DPI or with handwriting
- **Licence**: Apache 2.0

### Azure AI Document Intelligence (formerly Form Recognizer)

- **Service**: Azure cloud OCR and document understanding service
- **Pre-built Models**: Invoice, receipt, ID document, business card, tax form
- **Custom Models**: Train on organisation-specific document layouts
- **Accuracy**: 97%+ on printed text; ID document model extracts structured fields with 95%+ accuracy
