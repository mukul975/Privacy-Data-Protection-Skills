---
name: pii-detection-pipeline
description: >-
  Build automated PII detection and redaction pipelines using spaCy NER,
  Microsoft Presidio, and AWS Macie integration. Includes confidence scoring,
  custom entity type definitions, batch processing workflows, and multi-format
  document scanning for structured and unstructured data sources.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-engineering
  tags: "pii-detection, presidio, spacy-ner, data-redaction, aws-macie"
---

# Automated PII Detection and Redaction Pipeline

## Overview

Automated PII detection is a foundational capability for privacy engineering, enabling organizations to discover, classify, and protect personal data at scale. This skill covers building production-grade PII detection pipelines that combine rule-based pattern matching, machine learning-based Named Entity Recognition (NER), and cloud-native discovery services.

## PII Entity Types Catalog

### Direct Identifiers

| Entity Type | Examples | Detection Method | Risk Level |
|------------|---------|-----------------|------------|
| PERSON_NAME | "John Smith", "Maria Garcia" | NER model | High |
| EMAIL_ADDRESS | "user@example.com" | Regex pattern | High |
| PHONE_NUMBER | "+1-555-0123", "(555) 012-3456" | Regex + validation | High |
| SSN | "123-45-6789" | Regex + checksum | Critical |
| PASSPORT_NUMBER | "AB1234567" | Regex per country format | Critical |
| DRIVER_LICENSE | "D123-4567-8901" | Regex per state/country | Critical |
| CREDIT_CARD | "4111-1111-1111-1111" | Regex + Luhn checksum | Critical |
| IBAN | "GB82 WEST 1234 5698 7654 32" | Regex + modulo-97 check | High |
| IP_ADDRESS | "192.168.1.1", "2001:db8::1" | Regex (IPv4/IPv6) | Medium |
| MAC_ADDRESS | "00:1A:2B:3C:4D:5E" | Regex pattern | Medium |

### Quasi-Identifiers

| Entity Type | Examples | Detection Method | Risk Level |
|------------|---------|-----------------|------------|
| DATE_OF_BIRTH | "1990-01-15", "January 15, 1990" | NER + date parsing | Medium |
| POSTAL_CODE | "10001", "SW1A 1AA" | Regex per country | Medium |
| AGE | "35 years old", "age: 42" | NER + context | Low-Medium |
| GENDER | "male", "female", "non-binary" | Dictionary + context | Low |
| NATIONALITY | "British", "Japanese" | Dictionary + NER | Low-Medium |
| LOCATION | "123 Main St", "New York" | NER model | Medium |

### Sensitive Categories

| Entity Type | Examples | Detection Method | Risk Level |
|------------|---------|-----------------|------------|
| MEDICAL_RECORD | "MRN: 12345678" | Regex + context | Critical |
| HEALTH_CONDITION | "diabetes", "HIV positive" | Medical NER + dictionary | Critical |
| RELIGIOUS_BELIEF | "Muslim", "Catholic" | Dictionary + context | High |
| POLITICAL_OPINION | "Democratic Party member" | Dictionary + context | High |
| SEXUAL_ORIENTATION | "gay", "bisexual" | Dictionary + context | High |
| BIOMETRIC_DATA | "fingerprint hash: ..." | Context + pattern | Critical |
| GENETIC_DATA | "BRCA1 positive" | Medical dictionary | Critical |

## Microsoft Presidio Implementation

### Pipeline Architecture

```
Input Data --> Presidio Analyzer --> Detected Entities --> Presidio Anonymizer --> Redacted Output
                    |                      |                      |
                    v                      v                      v
             +------------+        +-------------+        +---------------+
             | Recognizers|        | Score Filter |        | Operators     |
             | - Pattern  |        | (threshold)  |        | - Replace     |
             | - NER      |        |              |        | - Redact      |
             | - Custom   |        |              |        | - Hash        |
             +------------+        +-------------+        | - Mask        |
                                                          | - Encrypt     |
                                                          +---------------+
```

### Core Implementation

```python
"""
PII detection and redaction pipeline using Microsoft Presidio.
Supports structured and unstructured text with configurable
entity types, confidence thresholds, and redaction strategies.
"""

from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_analyzer.nlp_engine import NlpEngineProvider
from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import OperatorConfig
import json
from dataclasses import dataclass, field


@dataclass
class DetectionResult:
    entity_type: str
    text: str
    start: int
    end: int
    score: float
    source: str


@dataclass
class PipelineConfig:
    language: str = "en"
    score_threshold: float = 0.5
    entities_to_detect: list[str] = field(default_factory=lambda: [
        "PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "CREDIT_CARD",
        "US_SSN", "US_DRIVER_LICENSE", "IBAN_CODE", "IP_ADDRESS",
        "LOCATION", "DATE_TIME", "NRP", "MEDICAL_LICENSE",
        "US_PASSPORT", "US_BANK_NUMBER", "UK_NHS"
    ])
    redaction_strategy: str = "replace"  # replace, redact, hash, mask, encrypt


class PIIDetectionPipeline:
    """
    Production PII detection pipeline built on Microsoft Presidio.
    Supports custom entity types and configurable redaction strategies.
    """

    def __init__(self, config: PipelineConfig):
        self.config = config

        # Initialize NLP engine with spaCy
        nlp_config = {
            "nlp_engine_name": "spacy",
            "models": [{"lang_code": config.language, "model_name": "en_core_web_lg"}]
        }
        nlp_engine = NlpEngineProvider(nlp_configuration=nlp_config).create_engine()

        # Initialize analyzer
        self.analyzer = AnalyzerEngine(nlp_engine=nlp_engine)

        # Register custom recognizers
        self._register_custom_recognizers()

        # Initialize anonymizer
        self.anonymizer = AnonymizerEngine()

    def _register_custom_recognizers(self):
        """Register custom PII recognizers beyond built-in types."""

        # UK National Insurance Number
        nino_pattern = Pattern(
            name="uk_nino",
            regex=r"\b[A-CEGHJ-PR-TW-Z]{2}\s?\d{2}\s?\d{2}\s?\d{2}\s?[A-D]\b",
            score=0.85
        )
        nino_recognizer = PatternRecognizer(
            supported_entity="UK_NINO",
            patterns=[nino_pattern],
            supported_language="en"
        )
        self.analyzer.registry.add_recognizer(nino_recognizer)

        # Vehicle Registration Number (UK format)
        vrn_pattern = Pattern(
            name="uk_vrn",
            regex=r"\b[A-Z]{2}\d{2}\s?[A-Z]{3}\b",
            score=0.6
        )
        vrn_recognizer = PatternRecognizer(
            supported_entity="UK_VRN",
            patterns=[vrn_pattern],
            supported_language="en"
        )
        self.analyzer.registry.add_recognizer(vrn_recognizer)

        # Employee ID (Cipher Engineering Labs format: CEL-XXXXX)
        emp_id_pattern = Pattern(
            name="employee_id",
            regex=r"\bCEL-\d{5}\b",
            score=0.95
        )
        emp_id_recognizer = PatternRecognizer(
            supported_entity="EMPLOYEE_ID",
            patterns=[emp_id_pattern],
            supported_language="en"
        )
        self.analyzer.registry.add_recognizer(emp_id_recognizer)

    def detect(self, text: str) -> list[DetectionResult]:
        """
        Detect PII entities in text.

        Args:
            text: Input text to scan

        Returns:
            List of detected PII entities with confidence scores
        """
        results = self.analyzer.analyze(
            text=text,
            entities=self.config.entities_to_detect,
            language=self.config.language,
            score_threshold=self.config.score_threshold
        )

        return [
            DetectionResult(
                entity_type=r.entity_type,
                text=text[r.start:r.end],
                start=r.start,
                end=r.end,
                score=r.score,
                source=r.analysis_explanation.recognizer if r.analysis_explanation else "unknown"
            )
            for r in results
        ]

    def redact(self, text: str) -> tuple[str, list[DetectionResult]]:
        """
        Detect and redact PII from text.

        Returns:
            Tuple of (redacted_text, list_of_detections)
        """
        # Detect entities
        analyzer_results = self.analyzer.analyze(
            text=text,
            entities=self.config.entities_to_detect,
            language=self.config.language,
            score_threshold=self.config.score_threshold
        )

        # Configure redaction operator
        operators = self._get_operators()

        # Apply redaction
        anonymized = self.anonymizer.anonymize(
            text=text,
            analyzer_results=analyzer_results,
            operators=operators
        )

        detections = [
            DetectionResult(
                entity_type=r.entity_type,
                text=text[r.start:r.end],
                start=r.start,
                end=r.end,
                score=r.score,
                source="presidio"
            )
            for r in analyzer_results
        ]

        return anonymized.text, detections

    def _get_operators(self) -> dict:
        """Configure anonymization operators based on strategy."""
        if self.config.redaction_strategy == "replace":
            return {"DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"})}
        elif self.config.redaction_strategy == "hash":
            return {"DEFAULT": OperatorConfig("hash", {"hash_type": "sha256"})}
        elif self.config.redaction_strategy == "mask":
            return {"DEFAULT": OperatorConfig("mask", {
                "type": "mask",
                "masking_char": "*",
                "chars_to_mask": 100,
                "from_end": False
            })}
        elif self.config.redaction_strategy == "redact":
            return {"DEFAULT": OperatorConfig("redact", {})}
        else:
            return {"DEFAULT": OperatorConfig("replace", {"new_value": "<REDACTED>"})}


class BatchPIIProcessor:
    """
    Process large volumes of documents for PII detection.
    Supports structured (CSV/JSON) and unstructured (text) formats.
    """

    def __init__(self, pipeline: PIIDetectionPipeline):
        self.pipeline = pipeline

    def process_csv(
        self,
        input_path: str,
        output_path: str,
        columns_to_scan: list[str] = None
    ) -> dict:
        """
        Scan and redact PII in a CSV file.

        Args:
            input_path: Path to input CSV
            output_path: Path to write redacted CSV
            columns_to_scan: Columns to scan (all if None)

        Returns:
            Summary statistics of detections
        """
        import pandas as pd

        df = pd.read_csv(input_path)
        stats = {"total_rows": len(df), "detections": {}, "columns_scanned": []}

        scan_columns = columns_to_scan or df.columns.tolist()

        for col in scan_columns:
            if col not in df.columns:
                continue

            stats["columns_scanned"].append(col)
            col_detections = []

            for idx, value in df[col].items():
                if pd.isna(value):
                    continue

                text = str(value)
                redacted, detections = self.pipeline.redact(text)
                df.at[idx, col] = redacted

                for d in detections:
                    col_detections.append(d.entity_type)

            # Count detection types for this column
            for entity_type in set(col_detections):
                count = col_detections.count(entity_type)
                key = f"{col}:{entity_type}"
                stats["detections"][key] = count

        df.to_csv(output_path, index=False)
        stats["total_detections"] = sum(stats["detections"].values())

        return stats

    def process_text_files(
        self,
        file_paths: list[str],
        output_dir: str
    ) -> dict:
        """
        Batch process text files for PII detection and redaction.

        Returns summary statistics.
        """
        import os

        stats = {
            "files_processed": 0,
            "total_detections": 0,
            "entity_counts": {},
            "high_risk_files": []
        }

        for file_path in file_paths:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            redacted, detections = self.pipeline.redact(text)

            # Write redacted output
            output_path = os.path.join(output_dir, os.path.basename(file_path))
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(redacted)

            # Update statistics
            stats["files_processed"] += 1
            stats["total_detections"] += len(detections)

            for d in detections:
                stats["entity_counts"][d.entity_type] = (
                    stats["entity_counts"].get(d.entity_type, 0) + 1
                )

            # Flag high-risk files (contain critical PII)
            critical_types = {"US_SSN", "CREDIT_CARD", "MEDICAL_LICENSE", "UK_NHS"}
            if any(d.entity_type in critical_types for d in detections):
                stats["high_risk_files"].append(file_path)

        return stats
```

## spaCy NER Custom Training

### Training Custom Entity Types

```python
"""
Train custom spaCy NER model for domain-specific PII entities.
"""

import spacy
from spacy.training import Example
import random


def create_training_data() -> list[tuple[str, dict]]:
    """
    Create training examples for custom PII entity types.

    Returns list of (text, annotations) tuples.
    """
    training_data = [
        (
            "Patient MRN 12345678 was admitted on 2024-01-15",
            {"entities": [(12, 20, "MEDICAL_RECORD_NUMBER")]}
        ),
        (
            "Employee CEL-00142 reported the incident",
            {"entities": [(9, 18, "EMPLOYEE_ID")]}
        ),
        (
            "Policy holder number PLH-2024-99887 filed a claim",
            {"entities": [(22, 35, "POLICY_NUMBER")]}
        ),
        (
            "The customer with loyalty ID LYL-A1B2C3 requested data export",
            {"entities": [(29, 39, "LOYALTY_ID")]}
        ),
    ]
    return training_data


def train_custom_ner(
    base_model: str = "en_core_web_lg",
    training_data: list = None,
    n_iter: int = 30,
    output_dir: str = "./custom_ner_model"
):
    """
    Fine-tune spaCy NER model with custom PII entity types.

    Args:
        base_model: Base spaCy model to fine-tune
        training_data: List of (text, annotations) tuples
        n_iter: Number of training iterations
        output_dir: Directory to save trained model
    """
    if training_data is None:
        training_data = create_training_data()

    nlp = spacy.load(base_model)

    # Get or create NER pipe
    if "ner" not in nlp.pipe_names:
        ner = nlp.add_pipe("ner", last=True)
    else:
        ner = nlp.get_pipe("ner")

    # Add custom entity labels
    custom_labels = set()
    for _, annotations in training_data:
        for ent in annotations.get("entities", []):
            custom_labels.add(ent[2])

    for label in custom_labels:
        ner.add_label(label)

    # Train
    optimizer = nlp.resume_training()
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

    with nlp.disable_pipes(*other_pipes):
        for iteration in range(n_iter):
            random.shuffle(training_data)
            losses = {}

            for text, annotations in training_data:
                doc = nlp.make_doc(text)
                example = Example.from_dict(doc, annotations)
                nlp.update([example], drop=0.35, sgd=optimizer, losses=losses)

            if iteration % 10 == 0:
                print(f"Iteration {iteration}, Losses: {losses}")

    nlp.to_disk(output_dir)
    return nlp
```

## AWS Macie Integration

### Architecture

```
S3 Buckets --> Macie Classification Jobs --> Findings --> EventBridge --> Lambda
                                                |                          |
                                                v                          v
                                        Security Hub              Remediation
                                        (centralized)             - Tag sensitive
                                                                  - Encrypt
                                                                  - Notify owner
                                                                  - Quarantine
```

### Macie Job Configuration

```python
"""
AWS Macie integration for cloud-native PII detection in S3 buckets.
"""

import boto3
from datetime import datetime


class MacieIntegration:
    """
    Configure and manage AWS Macie classification jobs for
    automated PII detection across S3 data stores.
    """

    def __init__(self, region: str = "us-east-1"):
        self.macie_client = boto3.client("macie2", region_name=region)

    def create_classification_job(
        self,
        bucket_name: str,
        job_name: str,
        custom_data_identifiers: list[str] = None,
        schedule: str = "ONE_TIME"
    ) -> str:
        """
        Create a Macie classification job for an S3 bucket.

        Args:
            bucket_name: Target S3 bucket
            job_name: Descriptive job name
            custom_data_identifiers: IDs of custom data identifier resources
            schedule: ONE_TIME or SCHEDULED

        Returns:
            Job ID
        """
        job_config = {
            "name": job_name,
            "description": f"PII detection scan for {bucket_name}",
            "jobType": schedule,
            "s3JobDefinition": {
                "bucketDefinitions": [
                    {
                        "accountId": self._get_account_id(),
                        "buckets": [bucket_name]
                    }
                ],
                "scoping": {
                    "includes": {
                        "and": [
                            {
                                "simpleScopeTerm": {
                                    "comparator": "STARTS_WITH",
                                    "key": "OBJECT_EXTENSION",
                                    "values": ["csv", "json", "txt", "pdf", "docx", "xlsx", "parquet"]
                                }
                            }
                        ]
                    }
                }
            },
            "managedDataIdentifierSelector": "ALL",
            "tags": {
                "Team": "Privacy Engineering",
                "Purpose": "PII Detection"
            }
        }

        if custom_data_identifiers:
            job_config["customDataIdentifierIds"] = custom_data_identifiers

        response = self.macie_client.create_classification_job(**job_config)
        return response["jobId"]

    def create_custom_data_identifier(
        self,
        name: str,
        description: str,
        regex: str,
        keywords: list[str] = None,
        maximum_match_distance: int = 50
    ) -> str:
        """
        Create a custom data identifier for organization-specific PII patterns.

        Returns:
            Custom data identifier ID
        """
        params = {
            "name": name,
            "description": description,
            "regex": regex,
            "maximumMatchDistance": maximum_match_distance
        }

        if keywords:
            params["keywords"] = keywords

        response = self.macie_client.create_custom_data_identifier(**params)
        return response["customDataIdentifierId"]

    def _get_account_id(self) -> str:
        """Get the current AWS account ID."""
        sts = boto3.client("sts")
        return sts.get_caller_identity()["Account"]

    def get_findings_summary(self, job_id: str) -> dict:
        """Get summary of findings from a classification job."""
        response = self.macie_client.list_findings(
            findingCriteria={
                "criterion": {
                    "classificationDetails.jobId": {
                        "eq": [job_id]
                    }
                }
            }
        )

        findings = []
        if response["findingIds"]:
            details = self.macie_client.get_findings(findingIds=response["findingIds"])
            findings = details["findings"]

        summary = {
            "total_findings": len(findings),
            "severity_counts": {},
            "entity_type_counts": {},
            "affected_objects": []
        }

        for finding in findings:
            severity = finding.get("severity", {}).get("description", "unknown")
            summary["severity_counts"][severity] = (
                summary["severity_counts"].get(severity, 0) + 1
            )

            sensitive_data = finding.get("classificationDetails", {}).get(
                "result", {}
            ).get("sensitiveData", [])

            for sd in sensitive_data:
                category = sd.get("category", "unknown")
                summary["entity_type_counts"][category] = (
                    summary["entity_type_counts"].get(category, 0)
                    + sd.get("totalCount", 0)
                )

            resource = finding.get("resourcesAffected", {}).get("s3Object", {})
            if resource:
                summary["affected_objects"].append(resource.get("key", "unknown"))

        return summary
```

## Confidence Scoring Framework

| Score Range | Confidence Level | Recommended Action |
|-------------|-----------------|-------------------|
| 0.95 - 1.00 | Very High | Auto-redact |
| 0.80 - 0.94 | High | Auto-redact with logging |
| 0.60 - 0.79 | Medium | Flag for human review |
| 0.40 - 0.59 | Low | Log only, no action |
| 0.00 - 0.39 | Very Low | Ignore |

## References

- Microsoft Presidio Documentation: microsoft.github.io/presidio
- spaCy NER Documentation: spacy.io/usage/linguistic-features#named-entities
- AWS Macie Documentation: docs.aws.amazon.com/macie
- Google Cloud DLP API Documentation
- NIST SP 800-188 — De-Identifying Government Datasets
- Article 29 WP Opinion 05/2014 on Anonymisation Techniques
