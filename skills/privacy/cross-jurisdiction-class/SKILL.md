---
name: cross-jurisdiction-class
description: >-
  Harmonises data classification across jurisdictions mapping GDPR special
  categories vs CCPA sensitive PI (1798.140(ae)) vs HIPAA PHI (160.103) vs
  LGPD sensitive data (Art. 5-II). Provides cross-regulation mapping matrix
  for multinational compliance. Keywords: cross-jurisdiction, GDPR, CCPA,
  HIPAA, LGPD, sensitive data, multinational, classification mapping.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-classification
  tags: "cross-jurisdiction, gdpr, ccpa, hipaa, lgpd, multinational, classification-mapping"
---

# Cross-Jurisdiction Data Classification Harmonisation

## Overview

Multinational organisations must classify data under multiple regulatory frameworks simultaneously. GDPR special categories (Art. 9), CCPA sensitive personal information (Cal. Civ. Code §1798.140(ae)), HIPAA protected health information (45 CFR §160.103), and LGPD sensitive personal data (Art. 5-II) each define sensitive data differently with distinct requirements. This skill provides a cross-regulation mapping matrix enabling unified classification that satisfies all applicable jurisdictions, supporting Vanguard Financial Services' operations across the UK/EU, United States, and Brazil.

## Jurisdictional Definitions Compared

### GDPR Art. 9 — Special Categories (EU/UK)

| Category | Definition Summary |
|----------|-------------------|
| Racial or ethnic origin | Data revealing racial or ethnic background |
| Political opinions | Political views, party membership, voting |
| Religious or philosophical beliefs | Faith, atheism, philosophical convictions |
| Trade union membership | Union membership status or activities |
| Genetic data | Inherited/acquired genetic characteristics (Art. 4(13)) |
| Biometric data | Physical/behavioural characteristics for unique identification (Art. 4(14)) |
| Health data | Physical/mental health, healthcare provision (Recital 35) |
| Sex life or sexual orientation | Sexual behaviour, preferences, orientation |

**Processing standard**: General prohibition with ten exceptions (Art. 9(2)(a)-(j))

### CCPA/CPRA — Sensitive Personal Information (California)

Cal. Civ. Code §1798.140(ae) defines sensitive personal information as:

| Category | Definition Summary |
|----------|-------------------|
| Social Security, driver's licence, state ID, passport | Government-issued identifiers |
| Account log-in with password/security credentials | Financial account access data |
| Debit/credit card combined with security code | Payment card data with authentication |
| Precise geolocation | Location within 1,850 feet (GPS-level) |
| Racial or ethnic origin | Same scope as GDPR |
| Religious or philosophical beliefs | Same scope as GDPR |
| Union membership | Same scope as GDPR |
| Personal communications (mail, email, text) | Content of non-public communications |
| Genetic data | DNA, genetic test results |
| Biometric data | Physiological, biological, behavioural characteristics for identification |
| Health information | Physical/mental health condition, diagnosis, treatment |
| Sex life or sexual orientation | Sexual activity, preferences |

**Consumer right**: Right to limit use and disclosure of sensitive PI (§1798.121)

### HIPAA — Protected Health Information (United States)

45 CFR §160.103 defines PHI as individually identifiable health information held or transmitted by a covered entity or business associate, in any form, that relates to:

| Element | Description |
|---------|-------------|
| Physical or mental health condition | Past, present, or future |
| Provision of health care | Treatment, services, payments |
| Payment for health care | Claims, billing, insurance |
| Identifiability | Information that identifies or could identify the individual |

**18 HIPAA Identifiers** (45 CFR §164.514(b)):
Names, geographic data (smaller than state), dates (except year), phone, fax, email, SSN, medical record number, health plan beneficiary number, account number, certificate/licence number, vehicle identifiers, device identifiers, web URLs, IP addresses, biometric identifiers, full-face photographs, any unique identifying number

**Standard**: Minimum necessary standard; use and disclosure limited to minimum necessary for purpose

### LGPD Art. 5-II — Sensitive Personal Data (Brazil)

| Category | Definition Summary |
|----------|-------------------|
| Racial or ethnic origin | Same scope as GDPR |
| Religious belief | Religious conviction or practice |
| Political opinion | Political views or affiliations |
| Trade union membership | Union affiliation |
| Religious, philosophical, or political organisation | Broader than GDPR — includes organisational membership |
| Health data | Physical/mental health |
| Sex life | Sexual activity |
| Genetic data | Genetic information |
| Biometric data | Biometric characteristics for identification |

**Processing standard**: Consent must be specific and highlighted; other bases available under Art. 11(II)

## Cross-Regulation Mapping Matrix

| Data Category | GDPR Art. 9 | CCPA §1798.140(ae) | HIPAA PHI | LGPD Art. 5-II | Unified Tier |
|--------------|-------------|-------------------|-----------|---------------|-------------|
| **Racial/ethnic origin** | Special category | Sensitive PI | N/A (unless health-related) | Sensitive | RESTRICTED |
| **Political opinions** | Special category | N/A | N/A | Sensitive | RESTRICTED |
| **Religious beliefs** | Special category | Sensitive PI | N/A | Sensitive | RESTRICTED |
| **Trade union membership** | Special category | Sensitive PI | N/A | Sensitive | RESTRICTED |
| **Genetic data** | Special category | Sensitive PI | PHI (if health-related) | Sensitive | RESTRICTED |
| **Biometric data (for identification)** | Special category | Sensitive PI | PHI (identifier) | Sensitive | RESTRICTED |
| **Health data** | Special category | Sensitive PI | PHI | Sensitive | RESTRICTED |
| **Sex life/orientation** | Special category | Sensitive PI | N/A (unless health-related) | Sensitive | RESTRICTED |
| **Social Security Number** | Personal (direct identifier) | Sensitive PI | PHI (identifier) | Personal (direct) | RESTRICTED |
| **Precise geolocation** | Personal (may be special if reveals religion/health) | Sensitive PI | PHI (if health-related) | Personal | CONFIDENTIAL+ |
| **Financial account with credentials** | Personal (financial) | Sensitive PI | N/A | Personal | RESTRICTED |
| **Personal communications content** | Personal | Sensitive PI | N/A | Personal | CONFIDENTIAL |
| **Medical record number** | Personal (indirect) | N/A (separate HIPAA regime) | PHI (identifier) | Personal | RESTRICTED (in healthcare context) |
| **Health insurance ID** | Personal (indirect) | N/A | PHI (identifier) | Personal | RESTRICTED (in healthcare context) |

## Harmonised Classification Approach

### Principle: Apply the Highest Standard

When data falls under multiple jurisdictions, apply the most protective classification:

```
For each data element:
  1. Classify under GDPR (personal / special category / criminal)
  2. Classify under CCPA (personal information / sensitive PI)
  3. Classify under HIPAA (PHI / non-PHI) — if applicable
  4. Classify under LGPD (personal / sensitive) — if applicable
  5. Assign the unified tier = MAX(all jurisdictional classifications)
```

### Unified Tier Assignment Rules

| Jurisdictional Classification | Unified Tier |
|------------------------------|-------------|
| Any regulation classifies as most-sensitive | RESTRICTED |
| GDPR special category OR CCPA sensitive PI OR LGPD sensitive | RESTRICTED |
| HIPAA PHI (any) | RESTRICTED |
| GDPR personal data AND CCPA personal information (not sensitive) | CONFIDENTIAL |
| Non-personal under all applicable regulations | PUBLIC or INTERNAL |

## Implementation for Vanguard Financial Services

### Jurisdictional Scope

| Jurisdiction | Applicable Law | Vanguard Operations |
|-------------|---------------|-------------------|
| EU/EEA | GDPR | EU customer base, Frankfurt data centre |
| United Kingdom | UK GDPR + DPA 2018 | London headquarters, UK customer base |
| California, USA | CCPA/CPRA | US operations, California residents' data |
| Other US States | Various (VCDPA, CPA, CTDPA, etc.) | US operations |
| Brazil | LGPD | Brazilian customer base |

### Cross-Jurisdiction Handling Requirements

For data that falls under multiple jurisdictions:

| Scenario | Jurisdictions | Handling |
|----------|--------------|---------|
| UK customer health data | UK GDPR + potentially HIPAA if shared with US health insurer | RESTRICTED; Art. 9(2) condition + HIPAA BAA if shared with US covered entity |
| California employee biometric data (fingerprint) | CCPA + Illinois BIPA + GDPR (if EU data subject) | RESTRICTED; CCPA consent + BIPA written consent + GDPR Art. 9(2)(a) |
| Brazilian customer financial data | LGPD + GDPR (if transferred from EU) | CONFIDENTIAL; LGPD lawful basis + GDPR Chapter V transfer safeguards |
| Cross-border employee HR data | UK GDPR + CCPA + LGPD | CONFIDENTIAL (RESTRICTED if contains health/diversity data); satisfy all three frameworks simultaneously |

## Regulatory Precedents

- **Meta Platforms Ireland (EDPB Binding Decision 01/2023)**: EUR 1.2 billion fine for EU-US data transfers — underscores the importance of jurisdictional mapping when data crosses borders
- **Sephora (CCPA Enforcement, 2022)**: USD 1.2 million settlement with California AG for failure to honour opt-out of sale of personal information — demonstrated CCPA-specific classification obligations
- **ANPD Brazil (2023)**: First LGPD administrative sanctions for inadequate security measures on sensitive personal data — confirmed LGPD enforcement trajectory

## Integration Points

- **personal-data-test**: GDPR personal data test is the foundation; cross-jurisdiction classification layers additional requirements
- **special-category-data**: GDPR special categories map to sensitive data across other jurisdictions
- **classification-policy**: Unified tier from cross-jurisdiction mapping feeds the enterprise classification policy
- **data-inventory-mapping**: Data inventory must record applicable jurisdictions per data element
