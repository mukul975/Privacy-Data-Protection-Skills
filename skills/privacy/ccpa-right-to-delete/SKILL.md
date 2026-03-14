---
name: ccpa-right-to-delete
description: >-
  Implements CCPA Section 1798.105 right to delete and CPRA amendments including service
  provider obligations, statutory exceptions for legal, security, and internal uses,
  consumer identity verification procedures, and 45-day response timeline management.
  Activate for CCPA deletion, CPRA right to delete, California privacy, consumer deletion queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "ccpa-right-to-delete, cpra, california-privacy, consumer-deletion, service-provider-obligations"
---

# CCPA/CPRA Right to Delete

## Overview

The California Consumer Privacy Act (CCPA), as amended by the California Privacy Rights Act (CPRA), grants California consumers the right to request deletion of personal information collected about them. This right is codified in Cal. Civ. Code Section 1798.105. Unlike the GDPR right to erasure which requires establishing one of six grounds, the CCPA right to delete is a more direct right — the consumer simply requests deletion and the business must comply unless a specific exception applies. The CPRA amendments expanded the obligations and introduced the California Privacy Protection Agency (CPPA) as the dedicated enforcement body. This skill covers the complete operational framework for receiving, verifying, assessing, and fulfilling deletion requests under CCPA/CPRA.

## Legal Foundation

### CCPA Section 1798.105 — Consumer's Right to Delete Personal Information

**(a)** A consumer shall have the right to request that a business delete any personal information about the consumer which the business has collected from the consumer.

**(b)** A business that collects personal information about consumers shall disclose the consumer's right to request deletion of the consumer's personal information.

**(c)** A business that receives a verifiable consumer request to delete the consumer's personal information shall delete the consumer's personal information from its records, notify any service providers or contractors to delete the consumer's personal information from their records, and notify all third parties to whom the business has sold or shared the consumer's personal information to delete the consumer's personal information unless this proves impossible or involves disproportionate effort.

**(d)** A business, service provider, or contractor shall not be required to comply with a consumer's request to delete the consumer's personal information if it is reasonably necessary for the business, service provider, or contractor to maintain the consumer's personal information in order to: [see exceptions below].

### CPRA Amendments (Effective January 1, 2023)

Key CPRA changes affecting the right to delete:

1. **Extended to service providers and contractors**: Businesses must direct service providers and contractors to delete, not just notify them.
2. **Third-party notification**: Businesses must notify third parties to whom personal information was sold or shared to also delete.
3. **CPPA enforcement**: The California Privacy Protection Agency has rulemaking and enforcement authority.
4. **Expanded definitions**: "Sharing" (for cross-context behavioral advertising) added alongside "selling."

### CCPA Regulations (11 CCR Division 6)

The California Attorney General's CCPA regulations (subsequently updated by CPPA regulations) specify:
- Methods for submitting requests (Section 999.312)
- Verification procedures (Section 999.323-999.325)
- Response requirements (Section 999.313)
- Service provider obligations (Section 999.314)

## Exceptions to Deletion

### CCPA Section 1798.105(d) — Nine Exceptions

A business is not required to delete personal information if it is reasonably necessary to:

| Exception | Description | Example at Orion Data Vault Corp |
|-----------|-------------|----------------------------------|
| **(d)(1)** Complete the transaction | Complete the transaction for which the personal information was collected, fulfill the terms of a written warranty or product recall, provide a good or service requested by the consumer, or reasonably anticipated within the context of a business's ongoing business relationship with the consumer | Active subscription or service delivery |
| **(d)(2)** Detect security incidents | Detect security incidents, protect against malicious, deceptive, fraudulent, or illegal activity, or prosecute those responsible for that activity | Fraud investigation records, security incident logs |
| **(d)(3)** Debug | Debug to identify and repair errors that impair existing intended functionality | Error logs, crash reports tied to consumer account |
| **(d)(4)** Free speech | Exercise free speech, ensure the right of another consumer to exercise their free speech rights, or exercise another right provided for by law | User-generated content on public forums |
| **(d)(5)** CCPA research | Engage in public or peer-reviewed scientific, historical, or statistical research in the public interest that adheres to all other applicable ethics and privacy laws, when deletion is likely to render impossible or seriously impair the research | Anonymized research datasets (must meet CCPA research standards) |
| **(d)(6)** Internal use aligned with expectations | Enable solely internal uses that are reasonably aligned with the expectations of the consumer based on the consumer's relationship with the business | Service improvement analytics based on consumer's direct interactions |
| **(d)(7)** Legal obligation | Comply with a legal obligation | Tax records, AML records, employment records |
| **(d)(8)** Internal use — lawful and compatible | Otherwise use the consumer's personal information, internally, in a lawful manner that is compatible with the context in which the consumer provided the information | Business operations where consumer reasonably expects data use |
| **(d)(9)** Comply with other law | Comply with federal, state, or local laws | HIPAA, FCRA, GLBA requirements |

### Exception Assessment Procedure

```
[Deletion Request Received]
         │
         ▼
[For Each Category of Personal Information Held]
   │
   ├── [Does any exception under §1798.105(d) apply?]
   │     │
   │     ├── No exception ──► DELETE this category
   │     │
   │     ├── Exception (d)(1) — Active transaction/relationship?
   │     │     └── [Is the consumer's transaction/service still active?]
   │     │           ├── Yes ──► RETAIN (document: active relationship)
   │     │           └── No ──► DELETE (transaction complete)
   │     │
   │     ├── Exception (d)(2) — Security?
   │     │     └── [Is data part of active security investigation?]
   │     │           ├── Yes ──► RETAIN (document: investigation ref)
   │     │           └── No ──► DELETE
   │     │
   │     ├── Exception (d)(7) — Legal obligation?
   │     │     └── [Is there a specific statutory retention requirement?]
   │     │           ├── Yes ──► RETAIN (document: cite statute + period)
   │     │           └── No ──► DELETE
   │     │
   │     └── [Other exceptions: assess per criteria above]
   │
   ▼
[Partial Deletion Decision]
   - Delete all categories where no exception applies
   - Retain categories where valid exception applies
   - Document each retained category with exception citation
   - Inform consumer of partial deletion with explanation
```

## Verification Procedures

### Consumer Identity Verification Requirements

CCPA requires that businesses verify the identity of the consumer making the request. The level of verification depends on the type of request and the sensitivity of the data:

| Verification Level | When Required | Methods |
|-------------------|---------------|---------|
| **Reasonable degree of certainty** | Deletion requests (standard) | Match at least 2 data points provided by consumer against information already maintained |
| **Reasonably high degree of certainty** | Deletion requests involving sensitive personal information or where deletion could cause significant harm to the consumer if incorrect | Match at least 3 data points + signed declaration under penalty of perjury |

### Verification Methods

| Method | Description | Data Points Matched |
|--------|-------------|-------------------|
| **Account-based verification** | Consumer logs into their verified account | Account credentials constitute verification |
| **Email verification** | Send verification link to email address on file | Email address + 1 additional data point |
| **Knowledge-based verification** | Ask consumer to confirm information only they would know | 2-3 data points (name, address, transaction history, phone) |
| **Government ID** | Request government-issued identification | Use only when other methods insufficient; destroy copy after verification |
| **Signed declaration** | Request signed declaration under penalty of perjury | Required for high-certainty verification; supplements other methods |

### Verification Workflow

```
[Deletion Request Received]
         │
         ▼
[Does consumer have an account?]
   │
   ├── Yes ──► [Is consumer logged in?]
   │             ├── Yes ──► Verified (account-based)
   │             └── No ──► Request login; if unable, proceed to non-account verification
   │
   └── No ──► [Non-account verification]
               │
               ├── [Request 2 data points for standard verification]
               │     ├── Match ──► Verified
               │     └── No match ──► Request additional data or deny (document reason)
               │
               └── [If sensitive data or high-risk deletion]
                     ├── [Request 3 data points + signed declaration]
                     ├── Match ──► Verified
                     └── No match ──► Deny with right to appeal
```

### Authorized Agents

Consumers may designate an authorized agent to submit deletion requests on their behalf:

1. **Proof of authorization**: The agent must provide signed written permission from the consumer, or a power of attorney under California Probate Code sections 4000-4465.
2. **Consumer verification still required**: Even with an authorized agent, the business may require the consumer to directly verify their identity.
3. **Agent registration**: California-registered agents must provide proof of registration with the California Secretary of State.

## Response Timeline

### 45-Day Response Period

| Milestone | Deadline | Action |
|-----------|----------|--------|
| **Acknowledgement** | 10 business days from request receipt | Confirm receipt; provide expected completion date |
| **Verification completion** | As soon as practicable | Complete identity verification; if unable to verify, notify consumer |
| **Response** | 45 calendar days from verifiable request receipt | Complete deletion and notify consumer; OR invoke extension |
| **Extension (if needed)** | Additional 45 calendar days (90 total) | Notify consumer of extension within initial 45 days; explain reason |
| **Deletion completion** | Within response deadline | Delete from business systems; direct service providers/contractors to delete; notify third parties |

### Response Content Requirements

The response to a deletion request must include:

```
DELETION REQUEST RESPONSE — Orion Data Vault Corp
---------------------------------------------------
Consumer Reference: DEL-CA-2026-0089
Request Date: [YYYY-MM-DD]
Verification Date: [YYYY-MM-DD]
Response Date: [YYYY-MM-DD]

STATUS: [Completed / Partially Completed / Denied]

PERSONAL INFORMATION DELETED:
- Category 1: [Description] — DELETED from business systems
- Category 2: [Description] — DELETED from business systems
- Category 3: [Description] — DELETED from business systems

SERVICE PROVIDERS/CONTRACTORS DIRECTED TO DELETE:
- [Service Provider Name] — Directed [date], confirmed [date]
- [Contractor Name] — Directed [date], confirmed [date]

THIRD PARTIES NOTIFIED (if PI was sold or shared):
- [Third Party Name] — Notified [date]

EXCEPTIONS APPLIED (if any):
- Category [X]: Retained under §1798.105(d)(7) — legal obligation
  (Specific statute: [cite statute and retention period])
- Category [Y]: Retained under §1798.105(d)(1) — active transaction
  (Transaction expected to complete: [date])

CONSUMER RIGHTS:
- You may appeal this decision by contacting [contact information]
- You may file a complaint with the California Privacy Protection Agency
  at [CPPA contact information]
- This deletion does not prevent you from exercising other rights under
  the CCPA, including the right to know and the right to opt-out
```

## Service Provider and Contractor Obligations

### Flow-Down Deletion Requirements

Under CCPA/CPRA, when a business receives a deletion request:

1. **Business** deletes personal information from its own records.
2. **Business directs service providers** to delete personal information from their records.
3. **Business directs contractors** to delete personal information from their records.
4. **Service providers and contractors must**:
   - Delete the consumer's personal information from their records.
   - Notify any sub-service providers or sub-contractors to delete.
   - Confirm deletion to the business.
5. **Business notifies third parties** (to whom PI was sold or shared) to delete.

### Service Provider Agreement Requirements

Orion Data Vault Corp includes the following provisions in all service provider agreements:

```
CCPA SERVICE PROVIDER ADDENDUM — Key Clauses
----------------------------------------------

1. DELETION OBLIGATIONS
   Service Provider shall, upon receipt of direction from Business to
   delete a consumer's personal information:
   (a) Delete the personal information from its systems within [15]
       business days of receiving the direction;
   (b) Direct any sub-service providers to delete the personal information;
   (c) Confirm deletion to Business in writing within [20] business days;
   (d) Retain no copies of the deleted personal information except as
       permitted by an applicable exception under Cal. Civ. Code §1798.105(d).

2. EXCEPTION NOTIFICATION
   If Service Provider determines that an exception under §1798.105(d)
   applies to any portion of the personal information, Service Provider
   shall notify Business within [5] business days, specifying the exception
   relied upon, the categories of personal information affected, and the
   expected retention period.

3. AUDIT RIGHTS
   Business shall have the right to audit Service Provider's deletion
   processes and verify that deletion has been completed as directed.
```

## Differences from GDPR Right to Erasure

| Aspect | CCPA Right to Delete | GDPR Right to Erasure |
|--------|---------------------|----------------------|
| **Grounds required** | No — consumer simply requests deletion | Yes — must establish one of six grounds under Art. 17(1) |
| **Scope** | Personal information collected FROM the consumer | Personal data concerning the data subject (broader — includes data obtained from other sources) |
| **Response timeline** | 45 calendar days (extendable to 90) | 30 calendar days (extendable to 90) |
| **Verification** | Explicit verification requirements with defined certainty levels | Identity verification required but method at controller's discretion |
| **Service provider obligations** | Explicit — must direct service providers/contractors to delete | Implicit — controller must ensure processors delete under Art. 28 |
| **Third-party notification** | Must notify third parties to whom PI was sold/shared | Must inform other controllers to whom data was disclosed (Art. 17(2) + Art. 19) |
| **Exceptions** | 9 enumerated exceptions under §1798.105(d) | 5 exceptions under Art. 17(3) |
| **Enforcement** | CPPA and California AG; private right of action limited to data breaches | Supervisory authorities; broader private right of action |

## Monitoring and Compliance Reporting

### CCPA Deletion Request Metrics

| Metric | Target | Reporting |
|--------|--------|-----------|
| Requests received (quarterly) | Track volume and trend | Quarterly to CPPA (if required) |
| Median response time | ≤ 30 calendar days | Quarterly |
| Requests completed within 45 days | ≥ 95% | Quarterly |
| Requests requiring extension | ≤ 10% | Quarterly |
| Requests denied (with exception) | Track percentage and exception type breakdown | Quarterly |
| Service provider deletion confirmation rate | 100% within 20 business days | Per request |
| Consumer appeals filed | Track volume and outcome | Quarterly |

### Annual CCPA Privacy Metrics Disclosure

If required to provide annual metrics (businesses receiving ≥10 million consumer requests), disclose:
1. Number of deletion requests received
2. Number of deletion requests complied with (whole or part)
3. Number of deletion requests denied
4. Median number of days to substantive response
