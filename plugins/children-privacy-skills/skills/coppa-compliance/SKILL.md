---
name: coppa-compliance
description: >-
  Implements Children's Online Privacy Protection Act (COPPA) compliance
  under 16 CFR Part 312. Covers verifiable parental consent methods
  including signed forms, credit card verification, government ID,
  knowledge-based authentication, and video call. Includes FTC safe
  harbor programs and enforcement actions. Keywords: COPPA, FTC,
  children, parental consent, safe harbor, verifiable consent.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "coppa, ftc, children-privacy, parental-consent, safe-harbor, verifiable-consent"
---

# COPPA Compliance — Children's Online Privacy Protection Act

## Overview

The Children's Online Privacy Protection Act (COPPA), codified at 15 U.S.C. Sections 6501-6506 and implemented through the FTC's COPPA Rule at 16 CFR Part 312, regulates the online collection, use, and disclosure of personal information from children under 13 years of age. COPPA applies to operators of commercial websites and online services (including mobile apps) directed to children under 13, or operators with actual knowledge that they are collecting personal information from a child under 13. The FTC's 2013 amendments significantly expanded the scope to cover persistent identifiers used for behavioural advertising, photos, videos, audio recordings, and geolocation data. The FTC issued a Notice of Proposed Rulemaking (NPRM) in December 2023 proposing further amendments including restrictions on push notifications to children and expanded consent requirements for targeted advertising.

## Statutory and Regulatory Framework

### COPPA Statute — 15 U.S.C. Section 6502

- **Section 6502(a)(1)**: Unlawful for an operator of a website or online service directed to children, or having actual knowledge of collecting from a child under 13, to collect personal information in a manner that violates the FTC's regulations.
- **Section 6502(b)(1)**: FTC must issue regulations requiring operators to: (A) provide notice of information practices; (B) obtain verifiable parental consent; (C) allow parents to review information collected; (D) allow parents to refuse further collection/use; (E) limit collection to what is necessary for the activity.
- **Section 6502(b)(2)**: FTC shall apply regulations considering competitive impact, costs, and benefits, and potential effect on existing safe harbor programs.

### COPPA Rule — 16 CFR Part 312

#### Section 312.2 — Key Definitions

- **Child**: An individual under the age of 13
- **Operator**: Any person who operates a website or online service and collects or maintains personal information from or about users, or on whose behalf such information is collected or maintained
- **Personal information**: Individually identifiable information including: first and last name; home or physical address; online contact information (email); telephone number; Social Security number; persistent identifier that can be used to recognise a user over time and across different websites; photograph, video, or audio file containing a child's image or voice; geolocation information sufficient to identify street name and city; information concerning the child or parents collected and combined with any of the above
- **Website or online service directed to children**: Determined by: subject matter, visual content, use of animated characters, child-oriented activities and incentives, music, age of models, presence of child celebrities, ads directed at children, competent evidence regarding the target audience
- **Support for internal operations**: Activities necessary to maintain or analyse the functioning of the website or online service, including one-time collection and non-contact use, frequency capping, legal compliance, security, contextual advertising, personalising content (not for advertising)

#### Section 312.3 — Obligations of Operators

1. **Direct notice to parents** (Section 312.4): Before collecting, using, or disclosing personal information from a child, the operator must provide clear and prominent notice on the website/service and directly to the parent
2. **Verifiable parental consent** (Section 312.5): Must obtain verifiable parental consent before any collection, use, or disclosure, except for narrow exceptions
3. **Parental access** (Section 312.6): Must provide parents with reasonable means to review the personal information collected from their child and to refuse to permit further collection or use
4. **Confidentiality, security, and integrity** (Section 312.8): Must establish and maintain reasonable procedures to protect the confidentiality, security, and integrity of personal information collected from children
5. **Data minimisation** (Section 312.7): Must not condition a child's participation in an activity on providing more personal information than is reasonably necessary
6. **Data retention** (Section 312.10): Must retain personal information collected from a child only as long as reasonably necessary to fulfil the purpose for which it was collected

## Verifiable Parental Consent Methods — Section 312.5(b)

The FTC recognizes the following methods for obtaining verifiable parental consent. Controllers must select the appropriate method based on the sensitivity of data collected and how it will be used.

### Method 1: Signed Consent Form

- Parent prints, signs, and returns a consent form to the operator via postal mail, fax, or electronic scan
- Form must identify the operator, list all information to be collected, describe uses and disclosures, and state that the parent can revoke consent
- Suitable for initial high-assurance verification
- **Limitation**: Slow turnaround, accessibility barriers for parents without printing capability

### Method 2: Credit Card or Other Online Payment Transaction

- Parent uses a credit card, debit card, or other online payment system that provides notification of each discrete transaction to the primary account holder
- The transaction must be a bona fide purchase or donation, or a micro-transaction (e.g., USD 0.50) disclosed to the parent
- Credit card verification alone (without a transaction) is insufficient; there must be an actual monetary transaction
- **Limitation**: Excludes unbanked families; may deter participation

### Method 3: Toll-Free Telephone Number or Video Conference

- Parent calls a toll-free number staffed by trained personnel who verify the parent's identity through knowledge-based questions
- Alternatively, parent connects through a video conference call where identity is confirmed visually
- Operator must train staff on COPPA requirements and verification protocols
- **Limitation**: Resource-intensive; staffing requirements for multi-language support

### Method 4: Government-Issued ID with Comparison to Database

- Parent submits a government-issued identification (driver's license, passport) which the operator checks against a database
- The ID must be deleted promptly from the operator's records after verification is complete
- Must comply with Section 312.5(b)(4) requirements for deletion of ID after verification
- **Limitation**: Privacy concerns about collecting sensitive identity documents; storage risk

### Method 5: Knowledge-Based Authentication

- Operator uses a series of challenge questions drawn from a third-party database (e.g., TransUnion, Experian, LexisNexis) that only the parent would likely be able to answer
- Questions must be dynamically generated and different for each verification attempt
- Must meet threshold of difficulty that prevents a child from successfully answering
- **Limitation**: Dependent on third-party data accuracy; may fail for parents with thin credit files

### Method 6: Facial Recognition Technology (FTC-Approved Method, 2013)

- Parent submits a photograph that is compared against a previously verified government-issued photo ID
- The photograph and ID image must be deleted promptly after the comparison is complete
- Currently an approved method under the FTC's COPPA Rule but raises significant privacy concerns
- **Limitation**: Biometric data collection concerns; accuracy disparities across demographics

### Method 7: Email Plus (Limited Use)

- Parent receives an email from the operator containing a notice and a link or response mechanism
- The operator sends a confirmatory email to the parent after a reasonable delay
- This method is approved ONLY for internal uses of collected information — NOT when the operator will disclose personal information to third parties or make it publicly available
- **Limitation**: Lowest assurance; child may access parent's email

### Consent Method Selection Matrix

| Data Use Scenario | Minimum Consent Method | FTC Expectation |
|-------------------|----------------------|-----------------|
| Internal use only (no disclosure) | Email Plus (Method 7) | Acceptable minimum |
| Sharing with third parties | Method 1, 2, 3, 4, or 5 | Higher assurance required |
| Public posting of child's information | Method 1, 2, 3, 4, or 5 | Highest assurance recommended |
| Behavioural advertising | Method 1, 2, 3, 4, or 5 | FTC scrutinises closely |
| Collection of photos/videos/audio | Method 1, 2, 3, 4, or 5 | Must verify before publication |

## Direct Notice Requirements — Section 312.4

### Notice on the Website or Online Service — Section 312.4(b)

The operator must post a clear and prominent link to an online notice of its information practices with respect to children on the home page and each area where personal information is collected from children. The notice must state:

1. Name, physical address, email address, and telephone number of all operators collecting or maintaining personal information through the site/service (or one designated operator with hyperlink to list of all)
2. Description of what information is collected and whether collected actively or passively
3. How the operator uses (and may use) the information
4. Whether personal information is disclosed to third parties; if so, the types of businesses, their general purposes, and whether they have agreed to maintain the confidentiality and security of the information
5. That the parent can review and have deleted the child's personal information, and can refuse to permit further collection
6. Procedures for the parent to exercise rights

### Direct Notice to Parent — Section 312.4(c)

Before collecting personal information from a child, the operator must send a direct notice to the parent that includes:

1. Statement that the operator has collected the parent's online contact information for the purpose of obtaining parental consent
2. The information practices of the operator
3. That if the parent does not respond within a reasonable time, the parent's online contact information will be deleted
4. A link to the online notice
5. The means by which the parent can provide consent

## FTC Safe Harbor Programs — Section 312.11

Industry groups or other persons may apply to the FTC for approval of self-regulatory guidelines (safe harbor programs) that implement the protections of the COPPA Rule. Operators subject to an approved safe harbor program are deemed to be in compliance with Section 312.

### Currently Approved Safe Harbor Programs

| Program | Administering Organisation | Focus Area |
|---------|--------------------------|------------|
| CARU (Children's Advertising Review Unit) | BBB National Programs | Advertising and marketing directed to children |
| kidSAFE Seal Program | kidSAFE, LLC | Websites and apps with child audiences |
| ESRB Privacy Certified | Entertainment Software Rating Board | Video games and interactive entertainment |
| Aristotle Integrity (formerly iKeepSafe COPPA Safe Harbor) | Aristotle Inc. | Cross-sector COPPA compliance |
| PRIVO (Privacy Vaults Online) | PRIVO, Inc. | Identity and consent management technology |
| TrustArc (formerly TRUSTe COPPA/Children's Privacy Program) | TrustArc Inc. | Cross-sector privacy certification |

### Safe Harbor Benefits

- FTC will not bring enforcement action against an operator that is in compliance with an approved safe harbor program's guidelines
- Safe harbor programs provide independent compliance review and monitoring
- Programs offer dispute resolution mechanisms and consumer complaint handling
- Membership signals compliance commitment to parents and regulators

### Safe Harbor Obligations

- Submit annual reports to the FTC on compliance activities
- Provide effective enforcement mechanisms including consumer redress
- Perform random, comprehensive compliance audits of members at least annually
- Maintain publicly available list of members and compliance status

## BrightPath Learning Inc. — COPPA Implementation

BrightPath Learning Inc. operates an educational gaming platform available to children in the United States. The platform includes interactive learning games, progress tracking, and parent communication features.

### COPPA Compliance Architecture

**Pre-Registration Flow:**
1. Landing page prominently links to the Children's Privacy Policy
2. Registration form asks "Are you 13 or older?" with neutral yes/no options (no age pre-fill)
3. User selecting "No" is routed to the parental consent flow
4. User selecting "Yes" proceeds with standard registration (with age verification at Step 5)

**Parental Consent Flow:**
1. Child enters parent's email address
2. BrightPath sends direct notice to parent per Section 312.4(c) including full information practices disclosure
3. Parent clicks the consent link within 72 hours (contact information deleted if no response)
4. Parent completes credit card verification via USD 0.50 micro-transaction (refunded within 48 hours)
5. Parent reviews and provides granular consent for each data use:
   - Account creation and educational content delivery (required for service)
   - Learning progress reports sent to parent (optional)
   - Anonymized aggregate analytics for platform improvement (optional)
6. Confirmation email sent to parent with link to parental dashboard

**Parental Dashboard Features:**
- View all personal information collected from the child
- Download collected information in machine-readable format (JSON/CSV)
- Delete specific data elements or the entire account
- Modify consent preferences for each data use
- Set usage time limits and content restrictions
- Receive weekly activity summary reports

**Data Minimisation Measures:**
- No persistent identifiers collected for advertising purposes
- No geolocation data collected (GPS disabled; IP address truncated to /24)
- No photographs, videos, or audio recordings stored beyond session
- Profile avatar selected from pre-set options (no photo upload for children under 13)
- Chat functionality disabled for accounts under 13; moderated text communication only through pre-approved messages

### Annual COPPA Audit Checklist

| # | Audit Item | Regulatory Reference | Status |
|---|-----------|---------------------|--------|
| 1 | Privacy policy posted and current | 312.4(b) | Review quarterly |
| 2 | Direct notice sent before collection | 312.4(c) | Automated system verified |
| 3 | Verifiable parental consent obtained | 312.5 | Credit card method validated |
| 4 | Parental access mechanism functional | 312.6 | Dashboard tested monthly |
| 5 | No excess data collection | 312.7 | Quarterly data mapping review |
| 6 | Security measures adequate | 312.8 | Annual penetration test |
| 7 | Retention limits enforced | 312.10 | Automated deletion verified |
| 8 | Third-party disclosures documented | 312.4(b)(4) | Vendor list updated quarterly |
| 9 | Safe harbor membership current | 312.11 | kidSAFE renewal date tracked |
| 10 | Staff training completed | Internal policy | Annual COPPA training for all staff |

## FTC Enforcement Actions

- **Epic Games/Fortnite (FTC, 2022)**: USD 275 million penalty for collecting personal information from children under 13 without parental consent, enabling voice and text communications with strangers by default, and using dark patterns to induce purchases. Largest COPPA penalty in history.
- **Google/YouTube (FTC, 2019)**: USD 170 million settlement (USD 136 million FTC, USD 34 million New York AG) for collecting persistent identifiers from viewers of child-directed YouTube channels to serve targeted advertising without obtaining verifiable parental consent.
- **Musical.ly/TikTok (FTC, 2019)**: USD 5.7 million settlement for collecting names, email addresses, and other personal information from children under 13 without parental consent while knowing that a significant portion of users were children.
- **VTech Electronics (FTC, 2018)**: USD 650,000 settlement for collecting personal information from children including photos, chat logs, and audio recordings without parental consent, and failing to secure the data leading to a breach exposing 6.4 million children's records.
- **Unixiz Inc./Explore Talent (FTC, 2020)**: USD 2 million judgment for collecting personal information from children on a talent scouting website without posting a privacy policy, obtaining parental consent, or maintaining reasonable security.

## Proposed 2024 COPPA Rule Amendments

The FTC's December 2023 Notice of Proposed Rulemaking proposes significant changes:

1. **Separate consent for targeted advertising**: Operators must obtain separate, opt-in parental consent specifically for targeted advertising directed at children — consent for the service itself cannot be bundled with advertising consent
2. **Prohibition on push notification consent**: Operators cannot condition access to the service on the parent's consent to send push notifications to the child
3. **Enhanced data security requirements**: Operators must implement a written information security program with specific technical safeguards
4. **Expanded definition of personal information**: Biometric identifiers added explicitly to the definition
5. **Limits on data retention**: Operators must retain children's personal information only for as long as reasonably necessary for the specific purpose for which it was collected
6. **Safe harbor accountability**: Enhanced FTC oversight of safe harbor programs including more detailed annual reporting requirements

## Integration Points

- **GDPR Parental Consent**: For services operating in both the US and EU, COPPA requirements (under-13 bright line) and GDPR Art. 8 requirements (13-16 depending on Member State) must both be satisfied
- **Age Verification Methods**: COPPA requires age screening; the method must not incentivise false age claims
- **Children's Data Minimisation**: COPPA Section 312.7 aligns with GDPR Art. 5(1)(c) data minimisation principle
- **EdTech Privacy Assessment**: COPPA's school exception (Section 312.5(c)(4)) allows schools to consent on behalf of parents for educational technology used in the classroom
- **Children's Deletion Requests**: COPPA Section 312.6 requires operators to delete children's information upon parental request
