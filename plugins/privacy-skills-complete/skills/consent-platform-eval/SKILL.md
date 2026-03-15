---
name: consent-platform-eval
description: >-
  Framework for evaluating and selecting Consent Management Platforms (CMPs). Covers
  TCF v2.2 certification requirements, Global Privacy Control support, multi-regulation
  compliance (GDPR, CCPA, LGPD), A/B testing capabilities, API integration options,
  reporting features, and a structured vendor comparison methodology.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "consent-management-platform, cmp-evaluation, tcf-certification, vendor-selection, cmp-comparison"
---

# Evaluating Consent Management Platforms

## Overview

A Consent Management Platform (CMP) is the technology layer that handles cookie consent collection, preference management, consent record storage, and signal propagation to downstream systems. Selecting the right CMP is critical for compliance with GDPR, ePrivacy, CCPA/CPRA, LGPD, and other regulations. The IAB Transparency and Consent Framework (TCF) v2.2 certification is a key differentiator for CMPs operating in the EU advertising ecosystem.

## Evaluation Criteria

### Category 1: Regulatory Compliance (Weight: 30%)

| Criterion | Description | Scoring |
|-----------|-------------|---------|
| TCF v2.2 Certification | CMP is registered with IAB Europe and passes compliance audits | Required for EU advertising |
| GDPR Compliance | Supports Art. 7 consent requirements, Art. 7(3) withdrawal, Art. 7(1) records | Mandatory for EU operations |
| CCPA/CPRA Support | Supports "Do Not Sell" opt-out, GPC signal detection, CPRA requirements | Required for US operations |
| LGPD Support | Brazilian data protection law consent requirements | Required for Brazil operations |
| GPC Support | Detects and honors Global Privacy Control (Sec-GPC: 1) signal | Required for CA, CO, CT, MT, TX, OR |
| CNIL Compliance | Equal prominence accept/reject, 6-month reconsent, no cookie walls | Required for French operations |
| Multi-Jurisdiction | Ability to apply different consent rules based on user location | Critical for global operations |
| Cookie Scanning | Automated scanning to detect and classify all cookies on the site | Important for completeness |

### Category 2: Technical Capabilities (Weight: 25%)

| Criterion | Description | Scoring |
|-----------|-------------|---------|
| API Integration | RESTful API for consent state queries from backend systems | Critical for server-side enforcement |
| Tag Manager Integration | Native integration with Google Tag Manager, Tealium, Segment | Reduces implementation effort |
| SDK Availability | Mobile SDKs (iOS, Android) and server-side SDKs | Required for mobile apps |
| Performance | Page load impact (target: <100ms additional latency) | Critical for UX |
| Customization | UI customization (colors, layout, language, button text) | Important for brand consistency |
| A/B Testing | Built-in consent banner experimentation (within compliance boundaries) | Important for optimization |
| Geolocation | Accurate user location detection for jurisdiction-specific rules | Critical for multi-region |
| TC String Generation | Generates IAB TC String for ad tech ecosystem integration | Required for advertising |

### Category 3: Consent Record Management (Weight: 20%)

| Criterion | Description | Scoring |
|-----------|-------------|---------|
| Consent Receipts | Generates audit-ready consent receipts per Art. 7(1) | Critical for compliance |
| Version Control | Tracks consent text versions with change history | Important for audit trail |
| Consent History | Full history per user (grants, withdrawals, re-consents) | Critical for DSAR support |
| Data Export | Export consent records in standard formats (JSON, CSV) | Important for portability |
| Retention Controls | Configurable consent record retention periods | Important for data minimization |
| Search and Query | Search consent records by user, purpose, date range | Important for DPA inquiries |
| Proof of Consent | Can generate evidence packages for regulatory inquiries | Critical for enforcement defense |

### Category 4: Reporting and Analytics (Weight: 15%)

| Criterion | Description | Scoring |
|-----------|-------------|---------|
| Consent Rate Dashboard | Real-time consent/opt-out rates by purpose and region | Important for monitoring |
| Trend Analysis | Historical consent rate trends over time | Important for strategy |
| Compliance Reporting | Pre-built reports aligned with GDPR, CCPA requirements | Important for DPO |
| Custom Reports | Ability to create custom reports and dashboards | Nice to have |
| Alerting | Alerts for anomalous consent patterns (sudden drops, spikes) | Important for incident detection |
| GPC Reporting | Reports on GPC signal detection rates and actions taken | Required for CPRA compliance |

### Category 5: Vendor and Support (Weight: 10%)

| Criterion | Description | Scoring |
|-----------|-------------|---------|
| Data Processing Agreement | GDPR-compliant DPA available | Mandatory |
| Data Residency | EU data hosting available (for consent records) | Required for EU operations |
| Sub-Processors | Transparent sub-processor list | Required per Art. 28 |
| SLA | Uptime SLA (target: 99.9%+) | Critical for availability |
| Support | Dedicated support, privacy expertise, implementation guidance | Important |
| Pricing Model | Transparent pricing (per pageview, per domain, flat rate) | Important for budgeting |

## Vendor Comparison Matrix

| Feature | OneTrust | Cookiebot | Usercentrics | Didomi | Quantcast Choice |
|---------|----------|-----------|-------------|--------|-----------------|
| **TCF v2.2 Certified** | Yes | Yes | Yes | Yes | Yes |
| **GDPR Compliance** | Full | Full | Full | Full | Full |
| **CCPA/CPRA Support** | Yes | Yes | Yes | Yes | Yes |
| **GPC Detection** | Yes | Yes | Yes | Yes | Yes |
| **LGPD Support** | Yes | Limited | Yes | Yes | Limited |
| **CNIL Compliance** | Yes | Yes | Yes | Yes | Yes |
| **Multi-Jurisdiction** | 100+ countries | 50+ countries | 50+ countries | 40+ countries | 30+ countries |
| **Cookie Scanner** | Automated | Automated | Automated | Automated | Automated |
| **API** | REST + GraphQL | REST | REST | REST + GraphQL | REST |
| **Mobile SDKs** | iOS + Android | Limited | iOS + Android | iOS + Android | Limited |
| **GTM Integration** | Native | Native | Native | Native | Native |
| **A/B Testing** | Built-in | Via API | Built-in | Built-in | Limited |
| **Performance** | ~80ms | ~60ms | ~70ms | ~75ms | ~50ms |
| **Consent Receipts** | Kantara-aligned | Basic | Detailed | Detailed | Basic |
| **Version Control** | Yes | Yes | Yes | Yes | Yes |
| **Data Export** | JSON, CSV, API | CSV | JSON, CSV, API | JSON, CSV | CSV |
| **Consent Dashboard** | Advanced | Basic | Advanced | Advanced | Basic |
| **EU Data Hosting** | Yes (Frankfurt) | Yes (Copenhagen) | Yes (Munich) | Yes (Paris) | Yes (Amsterdam) |
| **DPA Available** | Standard | Standard | Standard | Standard | Standard |
| **SLA** | 99.99% | 99.9% | 99.95% | 99.9% | 99.9% |
| **Pricing Model** | Per session | Per domain | Per session | Per pageview | Free (basic) |
| **Starting Price** | ~EUR 300/month | ~EUR 9/month | ~EUR 50/month | ~EUR 50/month | Free tier |

## Selection Process

### Step 1: Requirements Gathering

Identify must-have requirements based on:
- Jurisdictions where your organization operates
- Number of domains and mobile apps
- Advertising ecosystem participation (need TCF v2.2?)
- Backend integration needs (API requirements)
- Budget constraints

### Step 2: Shortlist (3-4 Vendors)

Apply mandatory criteria as filters:
- TCF v2.2 certification (if operating in EU ad tech)
- GPC support (if serving US consumers)
- EU data hosting (if required by data residency policy)

### Step 3: Proof of Concept (2 Weeks per Vendor)

For each shortlisted vendor:
- Implement on a staging environment
- Test all consent flows (accept, refuse, manage, withdraw)
- Measure page load impact
- Test API integration with backend systems
- Verify consent records meet Art. 7(1) requirements
- Test multi-jurisdiction logic (EU vs US vs Brazil)

### Step 4: Scoring and Selection

Score each vendor against the weighted criteria. Calculate weighted total score. Select the vendor with the highest score that meets all mandatory requirements.

## CloudVault SaaS Inc. Selection

After evaluating five vendors, CloudVault SaaS Inc. selected **Usercentrics** based on:
- Full TCF v2.2 certification
- Native iOS and Android SDKs (critical for CloudVault mobile app)
- Built-in A/B testing within CNIL compliance boundaries
- Strong API for server-side consent state queries
- EU data hosting in Munich (same jurisdiction as key customers)
- Competitive pricing for the pageview volume

## Key Regulatory References

- IAB TCF v2.2 Specification — CMP certification and requirements
- GDPR Article 7 — Conditions for consent (CMP must support)
- GDPR Article 28 — Processor requirements (CMP as processor)
- CPRA Section 1798.135(e) — GPC signal recognition
- CNIL Deliberation 2020-091 — Cookie consent technical requirements
- LGPD (Lei 13.709/2018) — Brazilian consent requirements
- ePrivacy Directive Article 5(3) — Cookie consent basis
