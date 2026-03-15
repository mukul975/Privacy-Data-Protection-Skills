# Unstructured Data PII Detection Scan Report

## Organisation: Vanguard Financial Services
## Report Reference: UPII-RPT-2026-03
## Scan Period: 2026-03-01 to 2026-03-14
## Prepared By: Michael Chen, Privacy Engineering Lead
## Reviewed By: Dr. James Whitfield, Data Protection Officer

---

## 1. Scan Scope and Configuration

| Parameter | Setting |
|-----------|---------|
| **Detection Engine** | Microsoft Presidio v2.2 with spaCy en_core_web_trf (v3.7) |
| **Pattern Recognisers** | 14 active (NINO, email, phone, IBAN, credit card, IP, DOB, Vanguard account, employee ID, passport, ICD-10, genetic marker, address, postcode) |
| **NER Model** | spaCy en_core_web_trf — PERSON, ORG, GPE, DATE entities |
| **OCR Engine** | Azure AI Document Intelligence (ID document model) + Tesseract 5.3 (general) |
| **Confidence Threshold** | HIGH > 85%, MEDIUM 70-84%, LOW 50-69% |
| **Sources Scanned** | Exchange Online, SharePoint Online, Teams, Application Logs, Scanned Documents |

---

## 2. Executive Summary

| Metric | Value |
|--------|-------|
| **Total items scanned** | 847,293 |
| **Items containing PII** | 312,847 (36.9%) |
| **Total PII detections** | 1,247,392 |
| **High-confidence detections** | 892,104 (71.5%) |
| **Medium-confidence detections** | 287,445 (23.0%) |
| **Special category PII detected** | 4,281 (health codes, biometric references) |
| **PII in unexpected locations** | 23 items flagged for remediation |

---

## 3. Findings by Source

### Exchange Online (Email)

| PII Type | Count | Confidence | Priority |
|----------|-------|-----------|----------|
| Person names (PERSON NER) | 487,291 | 82% avg | Medium |
| Email addresses | 312,847 | 94% avg | Low (expected in email) |
| Vanguard account numbers (VFS-) | 45,892 | 97% avg | High |
| UK National Insurance Numbers | 1,247 | 89% avg | High |
| IBANs | 3,481 | 91% avg | High |
| Phone numbers | 28,943 | 78% avg | Medium |
| IP addresses | 892 | 72% avg | Low |

**Key Finding**: 1,247 emails contain National Insurance Numbers in the body text. 89% are customer-facing emails in the Customer Service mailbox. Recommendation: implement DLP policy to warn agents before sending NINO via email.

### SharePoint Online (Documents)

| PII Type | Count | Confidence | Priority |
|----------|-------|-----------|----------|
| Person names | 234,891 | 85% avg | Medium |
| Customer account numbers | 67,234 | 96% avg | High |
| Financial data (IBANs, sort codes) | 12,481 | 88% avg | High |
| Passport scans (detected via OCR) | 2,847 | 92% avg | Critical |
| Health data (ICD-10 codes) | 847 | 81% avg | Critical |

**Key Finding**: 2,847 passport scan images found in SharePoint Legal library. 234 passport images found in general departmental sites (unexpected location). Recommendation: migrate all passport images to secure KYC repository; delete from general sites.

### Scanned Documents (OCR Pipeline)

| Document Type | Pages Scanned | PII Found | OCR Confidence |
|--------------|--------------|-----------|---------------|
| Passport scans | 3,247 | 3,247 (100%) | 96% avg |
| Medical certificates | 891 | 891 (100%) | 93% avg |
| Signed contracts | 8,421 | 7,893 (94%) | 95% avg |
| Utility bills (KYC) | 2,104 | 2,104 (100%) | 91% avg |
| Miscellaneous scans | 1,204 | 487 (40%) | 87% avg |

---

## 4. High-Priority Remediation Items

| # | Finding | Source | Risk | Action Required |
|---|---------|--------|------|----------------|
| 1 | 234 passport images in general SharePoint sites | SharePoint — Marketing, HR General, Finance | Critical — biometric data in uncontrolled location | Move to secure KYC repository; apply Restricted label; delete originals |
| 2 | 847 ICD-10 health codes in HR case management notes | SharePoint — HR Operations | Critical — Art. 9 special category in general HR files | Apply Restricted label; restrict access to OH team only |
| 3 | 1,247 NINOs sent via email without encryption | Exchange Online — Customer Service | High — sensitive identifier in transit | Implement DLP policy to block/warn; train agents on secure alternatives |
| 4 | Customer account numbers in application debug logs | Application Logs — payment-service | High — PII in developer-accessible logs | Implement log masking for VFS- pattern; purge historical logs |
| 5 | 3 credit card numbers in Teams chat (Customer Service channel) | Teams — CS General | High — payment card data in chat | Delete messages; remind staff of PCI DSS requirements |

---

## 5. Accuracy Verification (Monthly Sample)

| Metric | March 2026 |
|--------|-----------|
| **Sample size** | 200 detections reviewed |
| **True positives** | 184 |
| **False positives** | 12 |
| **True negatives** | 189 (200 non-PII items checked) |
| **False negatives** | 11 |
| **Precision** | 93.9% |
| **Recall** | 94.4% |
| **F1 Score** | 0.94 |

### False Positive Analysis

| False Positive Pattern | Count | Tuning Action |
|-----------------------|-------|--------------|
| Reference numbers matching NINO format | 4 | Add negative keyword "ref" within 20 chars |
| Dates matching DOB pattern in invoice headers | 5 | Add negative keyword "invoice date", "due date" |
| Internal phone extensions matching phone pattern | 3 | Require minimum 10 digits for phone detection |

---

*Report generated by Vanguard Privacy Engineering team using Microsoft Presidio v2.2. Next scan report: 2026-04-15.*
