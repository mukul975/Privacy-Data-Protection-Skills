---
name: managing-consent-for-children
description: >-
  Guide for managing consent for children's personal data under GDPR Article 8 and
  COPPA. Covers parental consent mechanisms, age verification methods, country-specific
  age thresholds (ranging from 13 to 16), parental authorization workflows, and
  age-appropriate design per the UK ICO Children's Code.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: consent-management
  tags: "children-consent, article-8, coppa, age-verification, parental-consent"
---

# Managing Consent for Children

## Overview

GDPR Article 8 establishes special rules for processing children's personal data in the context of information society services offered directly to a child. Where processing is based on consent under Article 6(1)(a), the controller must make reasonable efforts to verify that consent is given or authorized by the holder of parental responsibility over the child. Member States may set the age threshold between 13 and 16 years.

In the United States, the Children's Online Privacy Protection Act (COPPA, 15 U.S.C. Section 6501-6506) requires verifiable parental consent before collecting personal information from children under 13.

## Country-Specific Age Thresholds under GDPR Article 8(1)

Member States may provide by law for a lower age threshold, provided it is not below 13 years:

| Country | Age Threshold | Legal Basis |
|---------|--------------|-------------|
| Austria | 14 | Austrian Data Protection Act (DSG) Section 4(4) |
| Belgium | 13 | Law of 30 July 2018, Art. 7 |
| Croatia | 16 | GDPR default (no national derogation) |
| Czech Republic | 15 | Act No. 110/2019, Section 7 |
| Denmark | 13 | Danish Data Protection Act Section 12 |
| Estonia | 13 | Personal Data Protection Act Section 8 |
| Finland | 13 | Data Protection Act 1050/2018, Section 5 |
| France | 15 | Law No. 2018-493 (Loi Informatique et Libertés), Art. 45 |
| Germany | 16 | GDPR default (no national derogation) |
| Greece | 15 | Law 4624/2019, Art. 21 |
| Hungary | 16 | GDPR default (no national derogation) |
| Ireland | 16 | Data Protection Act 2018, Section 31 |
| Italy | 14 | Legislative Decree 101/2018, Art. 2-quinquies |
| Latvia | 13 | Personal Data Processing Law, Section 9 |
| Lithuania | 14 | Law on Legal Protection of Personal Data, Art. 5 |
| Luxembourg | 16 | GDPR default (no national derogation) |
| Netherlands | 16 | GDPR default (no national derogation) |
| Poland | 16 | GDPR default (no national derogation) |
| Portugal | 13 | Law 58/2019, Art. 16 |
| Romania | 16 | GDPR default (no national derogation) |
| Slovakia | 16 | GDPR default (no national derogation) |
| Slovenia | 16 | GDPR default (no national derogation) |
| Spain | 14 | Organic Law 3/2018, Art. 7 |
| Sweden | 13 | Data Protection Act (2018:218), Chapter 2 Section 4 |
| United Kingdom | 13 | Data Protection Act 2018, Section 9 (UK GDPR retained) |

## Age Verification Methods

Article 8(2) requires "reasonable efforts" to verify parental consent, "taking into consideration available technology." The EDPB and national supervisory authorities have identified the following methods ranked by assurance level:

### High Assurance Methods

1. **Credit Card Verification**: Parent provides credit card details with a micro-transaction (refundable) to verify adult status. Used widely under COPPA in the US.
2. **Government ID Verification**: Parent uploads government-issued ID (passport, national ID). Must comply with data minimization — ID should be verified and immediately deleted per EDPB guidance.
3. **Video Call Verification**: Live video call with parent presenting ID. Highest assurance but lowest scalability.
4. **Digital Identity Systems**: eIDAS-compliant electronic identification (e.g., BankID in Nordic countries, SPID in Italy).

### Medium Assurance Methods

5. **Knowledge-Based Verification**: Parent answers questions only an adult would know (e.g., financial questions from credit bureaus).
6. **Signed Consent Form**: Parent downloads, signs, and uploads a consent form. Can be combined with electronic signatures (eIDAS Regulation).
7. **Email-Plus Verification**: Email to parent followed by a secondary verification step (phone callback, reply with code).

### Low Assurance Methods (May Not Be Sufficient Alone)

8. **Self-Declaration**: User states their age via a date-of-birth input. Insufficient as the sole mechanism for high-risk processing, per CNIL guidance on age verification (June 2022).
9. **Checkbox Confirmation**: "I am over [age] years old" checkbox. EDPB considers this inadequate for children's consent.

### CloudVault SaaS Inc. Implementation

CloudVault SaaS Inc. implements a tiered verification approach:

- **Tier 1 (Account Creation)**: Date-of-birth collection during registration. If age is below the applicable threshold for the user's country, the sign-up flow routes to the parental consent workflow.
- **Tier 2 (Parental Email Verification)**: An email is sent to the parent's email address with a unique verification link. The link expires after 48 hours.
- **Tier 3 (Credit Card Micro-Transaction)**: For processing activities classified as high-risk (profiling, data sharing), the parent must complete a $0.50 refundable credit card transaction to verify adult status.

## Parental Authorization Workflow

```
START: Child enters date of birth during CloudVault SaaS Inc. sign-up
  │
  ├─► Calculate age based on date of birth
  │
  ├─► Determine applicable age threshold based on country
  │     (e.g., 16 for Ireland/Germany, 13 for UK/Denmark/Belgium)
  │
  ├─► IF age >= threshold:
  │     └─ Proceed with standard consent flow (child can consent independently)
  │
  └─► IF age < threshold:
        │
        ├─► Step 1: Inform child that parental consent is required
        │     "Because you're under [threshold] in [country], we need your
        │      parent or guardian's permission before you can use CloudVault."
        │
        ├─► Step 2: Collect parent/guardian email address
        │     ├─ Validate email format
        │     └─ Ensure parent email differs from child's email
        │
        ├─► Step 3: Send verification email to parent
        │     ├─ Subject: "CloudVault SaaS Inc. — Parental Consent Required"
        │     ├─ Body includes:
        │     │   ├─ What service the child wants to use
        │     │   ├─ What personal data will be collected
        │     │   ├─ Processing purposes (with per-purpose consent options)
        │     │   ├─ Data retention periods
        │     │   ├─ Child's rights under GDPR Article 8
        │     │   ├─ Parent's right to withdraw consent at any time
        │     │   └─ Link to consent form (expires in 48 hours)
        │     └─ Verification link contains: child_id, timestamp, HMAC signature
        │
        ├─► Step 4: Parent clicks verification link
        │     ├─ Display full consent form with per-purpose options
        │     ├─ For high-risk purposes: require credit card micro-transaction
        │     └─ Parent reviews and grants/denies consent per purpose
        │
        ├─► Step 5: Record parental consent
        │     ├─ Parent subject_id (derived from email verification)
        │     ├─ Child subject_id
        │     ├─ Relationship: "parent_guardian"
        │     ├─ Consent decisions per purpose
        │     ├─ Verification method used
        │     ├─ Timestamp, IP address, user agent
        │     └─ Consent text version hash
        │
        ├─► Step 6: Activate child's account
        │     ├─ Enable only purposes for which parental consent was granted
        │     └─ Apply age-appropriate default settings
        │
        └─► Step 7: Ongoing monitoring
              ├─ Age re-verification at appropriate intervals
              ├─ Parent can manage child's consent via parent dashboard
              └─ When child reaches age threshold, transition to self-consent
```

## Age-Appropriate Design Considerations

The UK ICO Age Appropriate Design Code (Children's Code, effective September 2, 2021) establishes 15 standards for online services likely to be accessed by children:

1. **Best Interests of the Child**: Processing must be in the child's best interest.
2. **Data Protection Impact Assessments**: Required for services likely accessed by children.
3. **Age-Appropriate Application**: Risk-assess and apply age-appropriate standards.
4. **Transparency**: Provide privacy information in age-appropriate language.
5. **Detrimental Use**: Do not use children's data in ways detrimental to their wellbeing.
6. **Default Settings**: Settings must be "high privacy" by default.
7. **Data Minimization**: Collect only the minimum data necessary.
8. **Data Sharing**: Do not disclose children's data unless there is a compelling reason.
9. **Geolocation**: Switch off geolocation by default.
10. **Parental Controls**: If provided, give the child age-appropriate information about them.
11. **Profiling**: Switch off profiling by default (unless there is a compelling reason).
12. **Nudge Techniques**: Do not use nudge techniques to lead children to weaken privacy settings.
13. **Connected Toys and Devices**: Apply all standards to connected devices/toys.
14. **Online Tools**: Provide prominent accessible tools for children to exercise their rights.
15. **Policies and Community Standards**: Uphold published policies and community standards.

## Key Regulatory References

- GDPR Article 8 — Conditions applicable to child's consent in relation to information society services
- GDPR Article 8(1) — Age threshold (16 years, Member States may lower to 13)
- GDPR Article 8(2) — Reasonable efforts to verify parental consent
- COPPA (15 U.S.C. Section 6501-6506) — US children's privacy requirements
- FTC COPPA Rule (16 CFR Part 312) — Implementing regulations for COPPA
- UK ICO Age Appropriate Design Code — 15 standards for children's online services
- CNIL Guidance on Age Verification (June 2022) — Methods and adequacy assessment
- EDPB Guidelines 05/2020 on Consent — Section on children's consent
- eIDAS Regulation (EU) No 910/2014 — Electronic identification for parental verification
