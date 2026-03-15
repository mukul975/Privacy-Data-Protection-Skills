---
name: transparent-communication
description: >-
  Implements GDPR Article 12 transparent information and communication requirements,
  covering concise, intelligible, and plain language obligations, response timelines,
  fee and refusal provisions, and layered notice design. Activate for transparent
  communication, Art. 12, privacy notice, plain language, response timeline queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "transparent-communication, gdpr-article-12, privacy-notice, plain-language, response-timelines"
---

# Implementing Transparent Communication

## Overview

GDPR Article 12 establishes the overarching framework for how controllers must communicate with data subjects about data protection matters. All information under Articles 13-14 and all communications under Articles 15-22 and 34 must be provided in a concise, transparent, intelligible, and easily accessible form, using clear and plain language. This skill covers the operational requirements for achieving transparent communication.

## Legal Foundation

### GDPR Article 12 — Transparent Information, Communication and Modalities

1. **Art. 12(1)** — The controller shall take appropriate measures to provide any information referred to in Articles 13 and 14 and any communication under Articles 15 to 22 and 34 in a concise, transparent, intelligible and easily accessible form, using clear and plain language, in particular for any information addressed specifically to a child. The information shall be provided in writing, or by other means, including, where appropriate, by electronic means. When requested by the data subject, the information may be provided orally, provided that the identity of the data subject is proven by other means.

2. **Art. 12(2)** — The controller shall facilitate the exercise of data subject rights under Articles 15 to 22. The controller shall not refuse to act on the request of the data subject unless it demonstrates that it is not in a position to identify the data subject.

3. **Art. 12(3)** — Response timeline: without undue delay and in any event within one month of receipt. Extension by two further months where necessary. Notification of extension within one month with reasons.

4. **Art. 12(4)** — If the controller does not take action on the request, inform the data subject without delay and at the latest within one month: reasons for not taking action, possibility of lodging a complaint with a supervisory authority, and seeking a judicial remedy.

5. **Art. 12(5)** — Information under Articles 13 and 14 and any communication and actions under Articles 15 to 22 and 34 shall be provided free of charge. Where requests are manifestly unfounded or excessive, the controller may charge a reasonable fee or refuse to act.

6. **Art. 12(6)** — Where the controller has reasonable doubts about the identity of the natural person making the request, it may request the provision of additional information necessary to confirm identity.

7. **Art. 12(7)** — Information to be provided under Articles 13 and 14 may be provided in combination with standardised icons.

## Transparency Requirements

### Plain Language Standard

Per EDPB Guidelines on Transparency (WP260 rev.01):

1. **Concise**: Eliminate unnecessary detail. Separate essential from supplementary information using layered notices.
2. **Transparent**: No hidden information. All material processing details must be disclosed.
3. **Intelligible**: Written at a reading level accessible to the average member of the intended audience. For general public notices, target an 8th-grade reading level (Flesch-Kincaid Grade Level 8 or below).
4. **Easily accessible**: Available without the data subject having to search for it. Prominently placed, not buried in terms and conditions.
5. **Clear and plain language**: No legal jargon, no technical terminology without explanation, no double negatives, no ambiguous phrasing.

### Language Requirements

| Scenario | Language Obligation |
|----------|-------------------|
| Service offered in one EU/EEA Member State | Language of that Member State |
| Service offered across multiple Member States | Language of each Member State where the service is actively offered |
| Service specifically targeting a linguistic minority | Consider providing in that language |
| Children as intended audience | Language and vocabulary appropriate for the age group |

### Layered Notice Approach

The EDPB recommends a layered approach to provide transparency without overwhelming the data subject:

#### Layer 1: Short Notice (Immediate Point of Collection)

Displayed at the point of data collection. Contains the most critical information:
- Identity of the controller
- Purpose(s) of the processing
- Description of data subject rights
- Information about the most impactful processing (e.g., profiling, international transfers)
- Link to full privacy notice

**Format**: 150-300 words. Visible without scrolling. No click-through required.

#### Layer 2: Full Privacy Notice

The complete privacy notice containing all information required under Art. 13 or Art. 14. Accessible from Layer 1 via a clear link.

**Format**: Structured with clear headings, table of contents, expandable sections where appropriate. Written in plain language throughout.

#### Layer 3: Supplementary Detail

Detailed information for specific processing activities, available on request or through contextual links:
- Legitimate interest assessments
- International transfer mechanisms and safeguards
- Data retention schedule detail
- Automated decision-making logic explanations

### Response Timeline Management

| Action | Deadline | Extension | Notification |
|--------|----------|-----------|--------------|
| Acknowledge receipt of request | 3 business days (best practice) | N/A | Send acknowledgement with reference number |
| Respond to data subject right request | 30 calendar days from receipt | Up to 60 additional days | Notify within initial 30 days with reasons |
| Respond to identity verification request | 30 calendar days from verification completion | Up to 60 additional days | Notify within initial 30 days |
| Inform of refusal to act | 30 calendar days from receipt | N/A | Must include: reasons, right to complain, right to judicial remedy |

### Fee and Refusal Framework

#### When a Fee May Be Charged (Art. 12(5)(a))

A reasonable fee based on administrative costs may be charged where requests are:
- **Manifestly unfounded**: The requester has stated a disruptive intent, or there is no legitimate purpose for the request.
- **Excessive**: Due to repetitive character (e.g., the same request submitted repeatedly without any change in processing).

Meridian Analytics Ltd fee schedule: GBP 10.00 base fee + GBP 0.10 per page exceeding 500 pages.

#### When Refusal Is Permitted (Art. 12(5)(b))

The controller may refuse to act where the request is manifestly unfounded or excessive, but must:
1. Inform the data subject of the reasons for not taking action.
2. Inform of the possibility to lodge a complaint with the ICO.
3. Inform of the right to a judicial remedy.

The burden of proof for demonstrating that a request is manifestly unfounded or excessive lies with the controller.

## Communication Templates

### Acknowledgement Elements

Every acknowledgement must include:
1. The reference number assigned to the request
2. The date the request was received
3. The type of right being exercised
4. The expected response date (30 calendar days)
5. Contact details for the DPO for any queries
6. A statement that the request is being processed free of charge (unless fee/refusal applies)

### Refusal Elements

Every refusal must include:
1. The specific reason(s) for refusing to act
2. The evidence supporting the manifestly unfounded or excessive determination
3. The data subject's right to lodge a complaint with the Information Commissioner's Office (ICO), Wycliffe House, Water Lane, Wilmslow, Cheshire SK9 5AF, telephone 0303 123 1113
4. The data subject's right to seek a judicial remedy under Article 79

### Extension Notification Elements

1. Confirmation that the request is being processed
2. The specific reason(s) for the extension (complexity, volume, concurrent requests)
3. The extended deadline date
4. Contact details for queries about the delay
