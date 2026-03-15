---
name: cpra-sensitive-pi
description: >-
  CPRA §1798.121 sensitive personal information restrictions and compliance.
  Covers all 9 sensitive PI categories including SSN, precise geolocation,
  racial/ethnic origin, biometric, genetic, health, and sex life data.
  Right to limit use/disclosure, permitted purposes, and implementation.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "cpra-sensitive-pi, sensitive-data, limit-use, geolocation, biometric"
---

# CPRA Sensitive Personal Information

## Overview

The California Privacy Rights Act (CPRA) introduced the concept of "sensitive personal information" (sensitive PI) as a distinct category under Cal. Civ. Code §1798.140(ae), effective January 1, 2023. This category parallels but is not identical to the GDPR's "special categories of data" under Article 9. The CPRA grants consumers the right to limit a business's use and disclosure of their sensitive PI to specific enumerated purposes under §1798.121.

Unlike the GDPR, which generally prohibits processing of special categories unless an exception applies, the CPRA permits businesses to collect and use sensitive PI but gives consumers the right to restrict that processing after collection through the "limit use" mechanism.

## Sensitive PI Categories (§1798.140(ae))

### Category 1: Government Identifiers

Social Security number, driver's license number, state identification card number, or passport number.

**Liberty Commerce Inc. Processing:**
Liberty Commerce Inc. collects Social Security numbers for tax reporting (1099-K forms) from marketplace sellers exceeding $600 in annual sales per IRS reporting thresholds. Driver's license numbers are collected for age verification on restricted product purchases. These are stored in a segregated, encrypted database with access limited to the tax compliance and fraud prevention teams.

### Category 2: Account Credentials

Account log-in, financial account, debit card, or credit card number in combination with any required security or access code, password, or credentials allowing access to an account.

**Liberty Commerce Inc. Processing:**
Payment card data is processed via PCI DSS-compliant service provider PaySecure Corp. and is not stored in Liberty Commerce Inc.'s systems in cleartext. Account credentials (hashed passwords, MFA tokens) are stored in the identity management system with bcrypt hashing and per-account salt.

### Category 3: Precise Geolocation

Any data that is derived from a device and that is used or intended to be used to locate a consumer within a geographic area that is equal to or less than the area of a circle with a radius of 1,850 feet (approximately 564 meters).

**Liberty Commerce Inc. Processing:**
The mobile app collects precise geolocation for store finder, delivery tracking, and local inventory search. Geolocation data is processed in real time and retained for 30 days. Upon a consumer's limit request, geolocation processing is restricted to delivery tracking only (a permitted service fulfillment purpose).

### Category 4: Racial or Ethnic Origin

Racial or ethnic origin of the consumer.

**Liberty Commerce Inc. Processing:**
Liberty Commerce Inc. collects racial/ethnic origin data through an optional workforce diversity survey for employees and an optional customer demographic survey. Customer survey data is aggregated and anonymized within 90 days. Upon a limit request, survey data collection ceases for that consumer and existing data is deleted.

### Category 5: Religious or Philosophical Beliefs

Religious or philosophical beliefs of the consumer.

**Liberty Commerce Inc. Processing:**
Not actively collected. May be inferred from product purchase patterns (religious texts, dietary products). Liberty Commerce Inc. does not create inferences about religious beliefs for advertising purposes. Product recommendation algorithms are configured to exclude religion-indicative categories from profile building.

### Category 6: Union Membership

Union membership of the consumer.

**Liberty Commerce Inc. Processing:**
Collected only for employees where required for payroll processing (union dues deduction). Not collected from consumers. Stored in HR system with access restricted to payroll administrators.

### Category 7: Private Communications Content

Contents of a consumer's mail, email, and text messages unless the business is the intended recipient of the communication.

**Liberty Commerce Inc. Processing:**
Customer service email and chat communications are retained for quality assurance and dispute resolution. Liberty Commerce Inc. is the intended recipient of these communications, so they fall outside the sensitive PI definition for purposes of the limit right. Third-party message content is not collected.

### Category 8: Genetic Data

A consumer's genetic data.

**Liberty Commerce Inc. Processing:**
Not collected. Liberty Commerce Inc. does not process genetic data for any business purpose.

### Category 9: Biometric Information

Processing of biometric information for the purpose of uniquely identifying a consumer.

**Liberty Commerce Inc. Processing:**
Face ID and fingerprint authentication are processed locally on the consumer's device via platform APIs (Apple Face ID, Android BiometricPrompt). Liberty Commerce Inc. does not receive, store, or process raw biometric templates. Device-side biometric results are used only to unlock the app and authorize transactions.

### Category 10: Health Information

A consumer's health information.

**Liberty Commerce Inc. Processing:**
Health-related product purchases (vitamins, supplements, medical devices) are recorded as transaction data. Liberty Commerce Inc. does not infer health conditions from purchase patterns for advertising. Health product purchase data is excluded from behavioral advertising profiles.

### Category 11: Sex Life or Sexual Orientation

Information concerning a consumer's sex life or sexual orientation.

**Liberty Commerce Inc. Processing:**
Not actively collected. May be inferred from product purchases. Liberty Commerce Inc. does not create or use inferences about sex life or sexual orientation for any business purpose.

## Right to Limit Use and Disclosure (§1798.121)

### Consumer Exercise Mechanism

- Business must display a "Limit the Use of My Sensitive Personal Information" link on its homepage
- The link may be combined with the opt-out link as a single "Your Privacy Choices" link per CPPA Regulations §7026(b)
- The CPPA-approved opt-out icon may be used in conjunction with the link
- No identity verification is required — the consumer's direction itself is sufficient

### Permitted Purposes After Limitation (§1798.121(a))

After a consumer exercises the limit right, the business may only use or disclose sensitive PI for:

| # | Permitted Purpose | Statute | Liberty Commerce Inc. Application |
|---|------------------|---------|----------------------------------|
| 1 | Perform services or provide goods reasonably expected by average consumer | §1798.121(a)(1) | Process transactions, fulfill orders, deliver products |
| 2 | Prevent, detect, investigate security incidents | §1798.121(a)(2) | Fraud detection using account credentials and geolocation anomalies |
| 3 | Resist malicious, deceptive, fraudulent, or illegal actions | §1798.121(a)(3) | Chargeback investigation, account takeover prevention |
| 4 | Ensure physical safety of natural persons | §1798.121(a)(4) | Product recall notifications using health product purchase data |
| 5 | Short-term, transient use including non-personalized advertising | §1798.121(a)(5) | Contextual (non-targeted) advertising based on current page content |
| 6 | Perform services on behalf of the business | §1798.121(a)(6) | Customer service, account maintenance, warranty processing |
| 7 | Verify or maintain quality or safety of a service or device | §1798.121(a)(7) | App functionality testing, payment processing verification |
| 8 | Upgrade, enhance, or improve services | §1798.121(a)(8) | Aggregate analytics for service improvement (no individual targeting) |

### Processing Restrictions After Limitation

After a limit request, Liberty Commerce Inc. implements the following restrictions:

| Sensitive PI Category | Prohibited Uses | Permitted Uses |
|----------------------|-----------------|----------------|
| Precise geolocation | Targeted advertising, location-based marketing, sale to data brokers | Delivery tracking, store finder (if actively requested) |
| Payment credentials | Cross-referencing for marketing profiles, sharing with ad networks | Transaction processing, fraud detection |
| Racial/ethnic origin | Any marketing or profiling | Aggregate diversity reporting (anonymized) |
| Government IDs | Any use beyond original collection purpose | Tax reporting (SSN), age verification (DL) |

## Privacy Notice Disclosure Requirements

### Notice at Collection (§1798.100(a))

When collecting sensitive PI, the business must disclose:
- The categories of sensitive PI to be collected
- The purposes for which each category will be used
- Whether each category is sold or shared
- The retention period or criteria for each category

### Privacy Policy (§1798.130(a)(5))

The privacy policy must separately identify:
- Categories of sensitive PI collected in the preceding 12 months
- Categories of sensitive PI sold or shared
- Purposes for using each sensitive PI category
- Whether consumers can limit use via the "Limit" link

**Liberty Commerce Inc. Privacy Notice Excerpt:**

> **Sensitive Personal Information We Collect:**
> We collect the following categories of sensitive personal information: (1) Social Security numbers from marketplace sellers for tax reporting; (2) payment card details for transaction processing; (3) precise geolocation through our mobile app for delivery and store finder services. We do not sell or share your sensitive personal information. You may limit our use of your sensitive personal information by clicking "Limit the Use of My Sensitive Personal Information" in the footer of any page or by contacting us at privacy@libertycommerce.com.

## Comparison with GDPR Special Categories

| Aspect | CPRA Sensitive PI | GDPR Special Categories (Art. 9) |
|--------|------------------|----------------------------------|
| Default rule | Permitted, with consumer right to limit | Prohibited, unless exception applies |
| Legal basis | No separate legal basis needed for collection | Explicit consent or specific exceptions required |
| Government IDs | Included as sensitive PI | Not a special category (but may be restricted by Member State law) |
| Financial data | Account credentials included | Not a special category |
| Precise geolocation | Included as sensitive PI | Not a special category (but may be covered under ePrivacy) |
| Enforcement | CPPA administrative fines; $7,500 for violations involving minors | DPA fines up to 4% annual turnover or EUR 20M |

## Implementation Checklist

| # | Item | Status | Owner |
|---|------|--------|-------|
| 1 | Inventory all sensitive PI categories collected | Complete | Privacy Team |
| 2 | Map purposes for each sensitive PI category | Complete | Privacy Team |
| 3 | Deploy "Limit the Use of My Sensitive Personal Information" link | Complete | Engineering |
| 4 | Implement limit-request processing workflow | Complete | Engineering |
| 5 | Configure purpose-based access controls for sensitive PI | Complete | Security Team |
| 6 | Update privacy notice with sensitive PI disclosures | Complete | Legal |
| 7 | Train customer service on limit requests | Complete | Operations |
| 8 | Configure data processing agreements with sensitive PI restrictions | Complete | Legal |
| 9 | Test GPC signal interaction with limit mechanism | Complete | QA |
| 10 | Quarterly audit of sensitive PI processing against permitted purposes | Ongoing | Privacy Team |

## Key Regulatory References

- Cal. Civ. Code §1798.121 — Right to limit use and disclosure of sensitive PI
- Cal. Civ. Code §1798.140(ae) — Definition of sensitive personal information
- Cal. Civ. Code §1798.135(a)(2) — "Limit" link requirement
- CPPA Regulations §7026 — Requests to limit sensitive PI
- CPPA Regulations §7027 — Combined opt-out/limit link option
- GDPR Article 9 — Processing of special categories of personal data (comparative reference)
