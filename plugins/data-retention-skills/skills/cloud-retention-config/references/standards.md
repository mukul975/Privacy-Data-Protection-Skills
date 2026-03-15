# Standards and Regulatory References — Cloud Storage Retention Configuration

## Primary Legislation

### GDPR (Regulation (EU) 2016/679)
- **Article 5(1)(e)** — Storage limitation: cloud retention policies enforce this principle
- **Article 25** — Data protection by design: retention configuration as a by-design control
- **Article 28** — Processor obligations: cloud providers as processors must support retention requirements
- **Article 32** — Security of processing: encryption, access controls, and integrity measures for cloud storage

### UK Data Protection Act 2018
- **Section 39** — First data protection principle (lawfulness, fairness, transparency)
- **Section 108** — Storage limitation in intelligence services processing

## Cloud Provider Documentation

### AWS (Amazon Web Services)
- **S3 Object Lifecycle Management** — Lifecycle rules for transition and expiration
- **S3 Object Lock** — WORM compliance: Governance Mode and Compliance Mode
- **S3 Legal Hold** — Independent hold flag for litigation preservation
- **AWS CloudTrail** — Audit logging for all S3 retention and object lock operations
- **AWS Backup** — Centralized backup retention management across AWS services

### Microsoft Azure
- **Azure Blob Storage Immutability Policies** — Time-based retention and legal hold
- **Azure Storage Lifecycle Management** — Automated tiering and deletion rules
- **Microsoft Purview Compliance** — Data lifecycle management and retention labels
- **Azure Event Grid** — Event-driven automation for retention operations

### Google Cloud Platform
- **GCS Bucket-Level Retention Policy** — Minimum retention period enforcement
- **GCS Object Hold** — Temporary hold and event-based hold
- **GCS Object Lifecycle Management** — Automated transitions and deletion
- **Cloud Audit Logs** — Audit trail for retention policy changes

## Regulatory Guidance

### EDPB
- **Guidelines 07/2020 on the concepts of controller and processor** (adopted 7 July 2021) — Cloud provider as processor; retention obligations
- **Guidelines on cloud computing** — Retention and deletion expectations for cloud environments

### ENISA (EU Agency for Cybersecurity)
- **Cloud Security Guide for SMEs** — Retention and deletion considerations for cloud migration

## Technical Standards
- **ISO/IEC 27017:2015** — Code of practice for information security controls for cloud services (includes retention)
- **ISO/IEC 27018:2019** — Protection of PII in public clouds (includes retention and deletion requirements)
- **CSA Cloud Controls Matrix v4** — DSP-04: Data Retention and Disposal
- **NIST SP 800-144** — Guidelines on Security and Privacy in Public Cloud Computing
