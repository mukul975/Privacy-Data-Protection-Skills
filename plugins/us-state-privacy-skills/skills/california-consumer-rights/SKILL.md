---
name: california-consumer-rights
description: >-
  California consumer privacy rights workflow implementation under CCPA/CPRA.
  Covers right to know, delete, opt-out of sale/sharing, correct, and limit
  sensitive PI processing. Includes 45-day response timelines, identity
  verification procedures, and authorized agent handling.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: us-state-privacy-laws
  tags: "california-rights, ccpa-rights, consumer-requests, dsr-workflow, opt-out"
---

# California Consumer Rights Workflow

## Overview

The CCPA/CPRA grants California consumers six categories of privacy rights enforceable against businesses that meet the applicability thresholds under Cal. Civ. Code §1798.140(d). These rights are modeled after but distinct from GDPR data subject rights, with California-specific verification requirements, response timelines, and scope limitations.

The California Privacy Protection Agency (CPPA) regulations (11 CCR §7001-7102) provide detailed implementation requirements for consumer request handling, including verification standards, response formats, and authorized agent procedures.

## Consumer Rights Matrix

| Right | Statute | Verification Level | Response Time | Extension | Frequency Limit |
|-------|---------|-------------------|---------------|-----------|-----------------|
| Right to Know (categories) | §1798.110 | 2 data points | 45 days | +45 days | 2 per 12 months |
| Right to Know (specific pieces) | §1798.110 | 3 data points + declaration | 45 days | +45 days | 2 per 12 months |
| Right to Delete | §1798.105 | 2 data points | 45 days | +45 days | No limit stated |
| Right to Correct | §1798.106 | 2 data points | 45 days | +45 days | No limit stated |
| Right to Opt-Out of Sale/Sharing | §1798.120 | Reasonable belief | 15 business days | None | Anytime |
| Right to Limit Sensitive PI | §1798.121 | Reasonable belief | 15 business days | None | Anytime |

## Right to Know (§1798.100, §1798.110, §1798.115)

### Categories Disclosure

Upon verified request, the business must disclose for the 12-month period preceding the request:

1. Categories of personal information collected
2. Categories of sources from which PI was collected
3. Business or commercial purpose for collecting, selling, or sharing PI
4. Categories of third parties to whom PI was disclosed
5. Categories of PI sold and, for each category, the categories of third parties to whom it was sold
6. Categories of PI disclosed for a business purpose and, for each category, the categories of recipients

### Specific Pieces Disclosure

Requires heightened verification (three data points plus a signed declaration under penalty of perjury). The business must provide the specific pieces of PI it has collected about the consumer in a portable, readily usable format (structured, commonly used, machine-readable).

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. provides a Know My Data portal that generates two report formats:
- **PDF report**: Human-readable summary with categories, sources, purposes, and recipients listed in plain language
- **JSON export**: Machine-readable structured data including all specific pieces of PI, organized by category with collection timestamps

The system enforces the 12-month lookback period automatically. Consumers may request data beyond 12 months, which Liberty Commerce Inc. provides where reasonably feasible per §1798.130(a)(2).

## Right to Delete (§1798.105)

### Processing Steps

1. **Receive request** through designated channels (web portal, email, toll-free number)
2. **Verify identity** — match at least two data points (name + email, email + account number, etc.)
3. **Confirm intent** — for requests submitted by means other than the designated portal, confirm the consumer's intent to delete
4. **Identify applicable exceptions** (§1798.105(d)):
   - Complete the transaction for which the PI was collected
   - Detect security incidents; protect against malicious, deceptive, fraudulent, or illegal activity
   - Debug to identify and repair functionality errors
   - Exercise free speech or ensure another consumer's right to exercise free speech
   - Comply with the California Electronic Communications Privacy Act (Cal. Penal Code §1546)
   - Engage in public or peer-reviewed scientific, historical, or statistical research in the public interest
   - Enable solely internal uses reasonably aligned with consumer expectations based on the consumer's relationship
   - Comply with a legal obligation (e.g., tax record retention per 26 U.S.C. §6001)
   - Otherwise use the PI internally in a lawful manner compatible with the context of collection
5. **Execute deletion** — delete PI from active systems and direct service providers and contractors to delete
6. **Handle deferred deletion** — for PI in backup/archival systems, mark for deletion at next scheduled maintenance cycle
7. **Notify consumer** — confirm deletion or explain partial denial with specific exception cited

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. executes a cascading deletion workflow:
- Active database records: Deleted within 10 business days
- Service provider systems (PaySecure Corp., SwiftShip Logistics): Deletion request forwarded with 30-day compliance deadline
- Backup systems: Marked for deletion at next 90-day rotation
- Retained data: Tax records (7 years per IRS requirements), fraud investigation records (duration of investigation plus 3 years)

## Right to Correct (§1798.106)

Added by CPRA, effective January 1, 2023. Consumers may request that a business correct inaccurate personal information, taking into account the nature of the PI and the purposes of processing.

### Business Obligations

The business must use commercially reasonable efforts to correct the PI. If the business contests the correction, it must:
- Notify the consumer of the decision
- Provide instructions for the consumer to submit documentation supporting the correction
- Consider the documentation and correct the PI if warranted
- If maintaining its decision, allow the consumer to submit a written addendum to the record

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. allows self-service correction for profile fields (name, address, email, phone number). For non-self-service data (transaction records, loyalty tier, inferred preferences), consumers submit correction requests through the privacy portal with supporting documentation. The privacy team reviews within 15 business days and either corrects or responds with reasoning.

## Right to Opt-Out of Sale and Sharing (§1798.120)

### Two Distinct Operations (Post-CPRA)

1. **Sale** (§1798.140(ad)): Disclosure of PI to a third party for monetary or other valuable consideration
2. **Sharing** (§1798.140(ah)): Disclosure of PI to a third party for cross-context behavioral advertising, regardless of monetary exchange

Both must be subject to the opt-out right. The business must provide a "Do Not Sell or Share My Personal Information" link on its homepage.

### Opt-Out Signal Requirements (CPPA Regulations §7025)

- Businesses must process opt-out preference signals (including GPC) as valid opt-out requests
- No identity verification required — the signal itself constitutes a valid request
- Must apply opt-out within 15 business days of receiving the signal
- Must not display a pop-up or interstitial asking the consumer to validate the signal
- Must not require the consumer to provide additional information to process the signal
- If the consumer is not identifiable, apply the opt-out to the browser/device

### Minor-Specific Requirements (§1798.120(c))

- Children under 13: Business must not sell or share PI without affirmative authorization from parent or guardian
- Children 13-15: Business must not sell or share PI without the child's affirmative authorization (opt-in)
- No re-solicitation for at least 12 months after a minor's parent/guardian or the minor themselves opts out

**Liberty Commerce Inc. Implementation:**
Liberty Commerce Inc. processes opt-out requests through three channels:
1. **Homepage link**: "Do Not Sell or Share My Personal Information" in page footer
2. **GPC signal**: Automatic detection and honoring of `Sec-GPC: 1` header
3. **Privacy portal**: Authenticated opt-out with account-level persistence

Upon opt-out, the system:
- Suppresses third-party advertising pixels (AdReach Network, TargetAds)
- Disables cross-context behavioral advertising data transmission
- Maintains first-party analytics (not a sale/sharing when processed under service provider agreement)
- Updates consent management platform state within 15 minutes

## Right to Limit Use of Sensitive PI (§1798.121)

### Permitted Uses After Limitation

When a consumer exercises this right, the business may only use or disclose sensitive PI for:
1. Performing services or providing goods reasonably expected by the consumer
2. Preventing, detecting, and investigating security incidents
3. Resisting malicious, deceptive, fraudulent, or illegal actions
4. Ensuring the physical safety of natural persons
5. Short-term, transient use (including non-personalized advertising)
6. Performing services on behalf of the business (verification, maintenance, customer service)
7. Verifying or maintaining the quality or safety of a service or device
8. Upgrading, enhancing, or improving services

**Liberty Commerce Inc. Sensitive PI Categories Processed:**
- Precise geolocation (store finder, delivery tracking)
- Payment card details (transaction processing)
- Racial/ethnic origin (optional diversity survey — discontinued upon any limitation request)
- Account credentials (authentication)

## Identity Verification Framework (CPPA Regulations §7060-7062)

### Verification Methods

| Method | Data Points | Applicable To |
|--------|------------|---------------|
| Knowledge-based | Account email + last 4 SSN | Know, Delete, Correct |
| Account verification | Authenticated session | Know, Delete, Correct |
| Document-based | Government ID scan | Know (specific), high-value requests |
| Declaration | Signed under penalty of perjury | Know (specific pieces) — required |
| Agent authorization | Signed permission or POA | All rights via authorized agent |

### Authorized Agent Handling (§1798.130(a)(1), CPPA Regs §7063)

When a request is submitted by an authorized agent:
1. Verify the agent's authorization: signed written permission from the consumer or valid power of attorney under Cal. Prob. Code §§4000-4465
2. If signed written permission (not POA): may also verify the consumer's identity directly
3. If POA: no additional consumer verification required
4. Deny request if authorization cannot be verified

## Response Delivery Standards

### Format Requirements
- **Categories disclosure**: May be in any readily understandable format
- **Specific pieces**: Must be in a portable, readily usable format that allows the consumer to transmit the information to another entity without hindrance (machine-readable: JSON, CSV, or XML)
- **Deletion confirmation**: Written confirmation specifying what was deleted and what was retained (with legal basis)
- **Opt-out**: Confirmation of opt-out status; must be effective within 15 business days

### Delivery Method
- Deliver via the same channel through which the request was received (or more secure alternative)
- For specific pieces of PI: use a secure, password-protected delivery mechanism
- Do not deliver sensitive PI (SSN, financial account numbers) in response to a right-to-know request — confirm existence only

## Key Regulatory References

- Cal. Civ. Code §1798.100-199 (CCPA/CPRA)
- CPPA Regulations 11 CCR §7001-7102
- CPPA Regulations §7025 — Opt-out preference signals
- CPPA Regulations §7060-7063 — Consumer request verification
- CPPA Enforcement Advisory No. 2024-01 — Dark patterns
- AG Opinion No. 21-303 — Authorized agent verification standards
