---
name: providing-indirect-collection-information
description: >-
  Provides GDPR Article 14 information for personal data obtained from sources
  other than the data subject, covering timing requirements (within reasonable
  period, max one month), source disclosure, all required elements, and
  exemptions under Art. 14(5). Activate for Art. 14, indirect collection,
  third-party data source, indirect data notice queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "indirect-collection, gdpr-article-14, third-party-data, source-disclosure, privacy-notice"
---

# Providing Indirect Collection Information

## Overview

GDPR Article 14 applies when a controller obtains personal data from a source other than the data subject — such as from third-party data brokers, publicly available sources, other controllers, or through automated observation by third parties. The controller must still provide the data subject with comprehensive information about the processing, but the timing and content requirements differ from Art. 13.

## Legal Foundation

### GDPR Article 14 — Information Where Personal Data Have Not Been Obtained from the Data Subject

#### Required Information (Art. 14(1)-(2))

All elements required under Art. 13(1)(a)-(f) and Art. 13(2)(a)-(g) PLUS:

| Element | Article | Description |
|---------|---------|-------------|
| Categories of personal data | Art. 14(1)(d) | The categories of personal data concerned (not required under Art. 13 because the subject already knows what they provided) |
| Source of data | Art. 14(2)(f) | From which source the personal data originate, and if applicable, whether it came from publicly accessible sources |

#### Timing Requirements (Art. 14(3))

The controller must provide the information:

1. **Art. 14(3)(a) — Default**: Within a **reasonable period** after obtaining the personal data, but at the latest **within one month**, having regard to the specific circumstances in which the personal data are processed.
2. **Art. 14(3)(b) — Communication with data subject**: If the personal data are to be used for communication with the data subject, at the latest at the time of the **first communication** to that data subject.
3. **Art. 14(3)(c) — Disclosure to another recipient**: If a disclosure to another recipient is envisaged, at the latest when the personal data are **first disclosed**.

The earliest applicable deadline governs.

#### Exemptions Under Art. 14(5)

Art. 14(1)-(4) shall not apply where and insofar as:

1. **Art. 14(5)(a) — Data subject already has the information**: The data subject already has the information.
2. **Art. 14(5)(b) — Impossible or disproportionate effort**: The provision of such information proves impossible or would involve a disproportionate effort, in particular for processing for archiving purposes in the public interest, scientific or historical research, or statistical purposes under Art. 89(1). In such cases, the controller must take appropriate measures to protect the data subject's rights and freedoms, including making the information publicly available.
3. **Art. 14(5)(c) — Union or Member State law**: Obtaining or disclosure is expressly laid down by Union or Member State law which provides appropriate measures to protect the data subject's legitimate interests.
4. **Art. 14(5)(d) — Professional secrecy**: The personal data must remain confidential subject to an obligation of professional secrecy regulated by Union or Member State law, including a statutory obligation of secrecy.

## Common Indirect Collection Scenarios at Meridian Analytics Ltd

| Scenario | Data Source | Categories | Timing Obligation |
|----------|-----------|------------|-------------------|
| Client employee data received from employer client | Employer (another controller) | Name, email, job title, access permissions | Within 1 month of receipt, or at first communication |
| Companies House / public registry data | Publicly accessible source | Director names, registered address, filing history | Within 1 month; note public source in notice |
| Credit reference agency data | Credit reference agency (Experian, Equifax) | Credit score, payment history, financial indicators | At first communication or within 1 month |
| Referral from existing client | Existing client | Name, email, company | At first communication with referred person |
| Data enrichment from third-party provider | Data enrichment provider | Firmographic data, industry classification | Within 1 month of enrichment |

## Indirect Collection Information Workflow

### Step 1: Identify Indirect Data Acquisition

1. Map all sources of personal data that are not the data subjects themselves.
2. For each source, document:
   - Source identity and type (controller, publicly accessible, data broker)
   - Categories of personal data received
   - Legal basis for receiving the data
   - Date of receipt
   - Purpose of processing

### Step 2: Determine the Timing Obligation

Apply the earliest applicable deadline from Art. 14(3)(a)-(c):

```
[Data Received from Third Party]
         │
         ▼
[Will data be used to contact the subject?]
   ├── Yes ──► Notify at or before first communication
   └── No ──► [Will data be disclosed to another recipient?]
               ├── Yes ──► Notify before or at disclosure
               └── No ──► Notify within reasonable period (max 1 month)
```

### Step 3: Prepare the Art. 14 Notice

The notice must contain all elements specified in Art. 14(1) and (2). Use the following structure:

1. **Controller identity**: Meridian Analytics Ltd, 47 Canary Wharf Tower, London E14 5AB
2. **DPO contact**: Dr Sarah Chen, dpo@meridiananalytics.co.uk
3. **Purposes and legal basis**: State each purpose and its legal basis
4. **Categories of personal data**: List the categories obtained (since the subject did not provide them directly)
5. **Recipients**: Identify recipients or categories
6. **International transfers**: Describe any transfers and safeguards
7. **Retention period**: State period or criteria
8. **Data subject rights**: List all applicable rights
9. **Right to withdraw consent**: If applicable
10. **Right to complain**: ICO details
11. **Source of data**: Identify the source and whether it is publicly accessible
12. **Automated decision-making**: If applicable
13. **Further processing**: If applicable

### Step 4: Assess Exemptions

Before deciding not to provide Art. 14 information, assess each exemption strictly:

| Exemption | Assessment | Documentation Required |
|-----------|------------|----------------------|
| Art. 14(5)(a) — Already has info | Verify the subject has received materially equivalent information from another source | Record the source and date of prior information |
| Art. 14(5)(b) — Impossible/disproportionate effort | Conduct and document proportionality assessment considering: number of data subjects, age of data, compensatory measures available | Written proportionality assessment, approved by DPO, with compensatory measures (e.g., publish information on website) |
| Art. 14(5)(c) — Law requires acquisition | Identify the specific legal provision | Citation of the provision |
| Art. 14(5)(d) — Professional secrecy | Identify the statutory obligation of secrecy | Citation of the provision |

The EDPB Guidelines on Transparency (WP260 rev.01) state that the Art. 14(5)(b) exemption should be interpreted restrictively and that the mere inconvenience or cost of providing information is not sufficient to constitute "disproportionate effort."

### Step 5: Deliver the Notice

1. **Email**: If the subject's email address is available, send the Art. 14 notice by email.
2. **Postal mail**: If only a postal address is available, send by first-class post.
3. **Combined with first communication**: Where the first communication is an email or letter, include the Art. 14 information in or with that communication.
4. **Published notice**: Where the Art. 14(5)(b) exemption applies and compensatory measures are required, publish the information on the controller's website.

### Step 6: Document and Record

1. Record the date of each Art. 14 notification.
2. Record the method of delivery.
3. Record any exemption relied upon and its justification.
4. Retain the record for 3 years.
