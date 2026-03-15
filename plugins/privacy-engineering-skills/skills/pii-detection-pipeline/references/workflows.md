# PII Detection Pipeline — Workflows

## Workflow 1: Pipeline Deployment
1. Install Presidio analyzer and anonymizer with spaCy model
2. Register custom entity recognizers for organization-specific patterns
3. Configure confidence thresholds per entity type
4. Set up batch processing for structured data (CSV, databases)
5. Configure unstructured data scanning (documents, emails)
6. Deploy monitoring and alerting for detection metrics
7. Document entity types and redaction strategies

## Workflow 2: Custom Entity Training
1. Collect training examples for domain-specific entity types
2. Annotate examples with entity spans and labels
3. Fine-tune spaCy NER model on custom entities
4. Evaluate model with precision, recall, F1 metrics
5. Register trained model with Presidio analyzer
6. Validate with representative data samples
7. Deploy to production pipeline

## Workflow 3: AWS Macie Integration
1. Enable Macie in target AWS account
2. Create custom data identifiers for organization patterns
3. Configure classification jobs for target S3 buckets
4. Set up EventBridge rules for finding notifications
5. Deploy Lambda for automated remediation
6. Configure Security Hub integration
7. Establish review cadence for findings

## Workflow 4: Confidence Threshold Tuning
1. Run detection on labeled test dataset
2. Compute precision/recall at each confidence level
3. Select thresholds: auto-redact (>0.95), flag (>0.60), ignore (<0.40)
4. Validate with human review sample
5. Document chosen thresholds and rationale
