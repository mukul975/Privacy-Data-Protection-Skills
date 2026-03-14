---
name: processing-data-subject-access-requests
description: >-
  Guides AI agents through the complete GDPR Data Subject Access Request (DSAR)
  workflow under Article 15, including identity verification, 30-day deadline
  calculation with extensions, response formatting, exemptions, and fee provisions.
  Activate when handling DSAR, access request, subject access, Art. 15, or SAR queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "dsar, gdpr-article-15, access-request, subject-access-right, data-subject-rights"
---

# Processing Data Subject Access Requests

## Overview

A Data Subject Access Request (DSAR) is the right of an individual under GDPR Article 15 to obtain confirmation of whether their personal data is being processed, and if so, to access that data along with supplementary information. This skill provides a complete operational workflow for receiving, validating, processing, and responding to DSARs within the legally mandated timeframe.

## Legal Foundation

### GDPR Article 15 — Right of Access by the Data Subject

1. **Art. 15(1)** — The data subject has the right to obtain from the controller confirmation as to whether personal data concerning them is being processed, and where that is the case, access to the personal data and the following information:
   - (a) the purposes of the processing
   - (b) the categories of personal data concerned
   - (c) the recipients or categories of recipient to whom the personal data have been or will be disclosed, in particular recipients in third countries or international organisations
   - (d) where possible, the envisaged period for which the personal data will be stored, or if not possible, the criteria used to determine that period
   - (e) the existence of the right to request rectification, erasure, restriction, or to object to processing
   - (f) the right to lodge a complaint with a supervisory authority
   - (g) where the personal data are not collected from the data subject, any available information as to their source
   - (h) the existence of automated decision-making, including profiling, referred to in Art. 22(1) and (4), and meaningful information about the logic involved, significance, and envisaged consequences

2. **Art. 15(3)** — The controller shall provide a copy of the personal data undergoing processing. For additional copies, the controller may charge a reasonable fee based on administrative costs.

3. **Art. 15(4)** — The right to obtain a copy shall not adversely affect the rights and freedoms of others.

### GDPR Article 12 — Transparent Communication

- **Art. 12(3)** — Response deadline: without undue delay and in any event within one month of receipt. That period may be extended by two further months where necessary, taking into account the complexity and number of requests. The controller shall inform the data subject of any such extension within one month of receipt, together with the reasons for the delay.
- **Art. 12(5)** — Where requests are manifestly unfounded or excessive (particularly due to repetitive character), the controller may either charge a reasonable fee or refuse to act. The controller bears the burden of demonstrating the manifestly unfounded or excessive character.

## DSAR Processing Workflow

### Step 1: Receive and Log the Request

1. Record the request in the DSAR tracking register with a unique reference number (format: DSAR-YYYY-NNNN).
2. Capture the channel of receipt (email, web form, postal mail, telephone, in-person).
3. Timestamp the receipt to the minute using UTC.
4. Assign the request to the designated DSAR processing team member.
5. Send an acknowledgement to the data subject within 3 business days confirming receipt and reference number.

### Step 2: Verify the Identity of the Requester

1. **Low-risk verification** (request received from a verified account, e.g., logged-in customer portal): Confirm account ownership via existing authentication.
2. **Medium-risk verification** (request received via email matching records): Request two of the following — date of birth, account number, postal code associated with the account, last four digits of payment method.
3. **High-risk verification** (request from unrecognised channel or on behalf of another person): Require government-issued photo ID plus one additional identifier. For third-party requests (e.g., solicitor acting on behalf), require written authorisation signed by the data subject plus proof of identity for both the representative and the data subject.
4. If identity cannot be verified, inform the requester within 10 business days that additional proof is required. The 30-day response clock pauses until verification is complete per EDPB Guidelines 01/2022 paragraph 64.

### Step 3: Assess the Request Scope

1. Determine whether the request covers all personal data or a specific subset.
2. Identify all data processing systems where the subject's data may reside:
   - CRM systems (e.g., Salesforce, HubSpot)
   - HR/payroll systems (for employee DSARs)
   - Marketing automation platforms
   - Customer support ticket systems
   - Analytics and logging platforms
   - Backup and archival systems
   - Third-party processor systems
3. Document any data that falls under exemptions (see Step 5).
4. Where the controller processes a large quantity of data, request that the data subject specify the information or processing activities to which the request relates, per Recital 63.

### Step 4: Calculate the Response Deadline

1. **Standard deadline**: 30 calendar days from the day after receipt of the request (or from the day after identity verification is completed, if verification was required).
2. **Extension**: Where the request is complex or where there are numerous requests, extend by up to two additional months (total maximum: 90 calendar days). Notify the data subject of the extension and reasons within the initial 30-day period.
3. **Weekend/holiday rule**: If the deadline falls on a weekend or public holiday in the controller's jurisdiction, the deadline moves to the next business day per Regulation (EEC, Euratom) No 1182/71.

### Step 5: Apply Exemptions Under Art. 15(4)

Review whether any of the following exemptions apply:

1. **Rights and freedoms of others** — Art. 15(4): Redact or withhold data where disclosure would adversely affect the rights and freedoms of other individuals (e.g., third-party personal data, trade secrets of third parties).
2. **Legal privilege** — Data protected by legal professional privilege or litigation privilege.
3. **Confidential references** — References given in confidence for education, training, or employment purposes (applicable under UK GDPR supplementary provisions).
4. **Management forecasting** — Data processed for management forecasting or planning where disclosure would prejudice the business (applicable under certain Member State derogations).
5. **Negotiations** — Data consisting of records of intentions in relation to negotiations with the data subject where disclosure would prejudice those negotiations.

Document each exemption applied with specific justification.

### Step 6: Compile the Response

1. Gather all personal data from identified systems.
2. Organise data by category:
   - Identity data (name, date of birth, contact details)
   - Financial data (transaction records, payment methods)
   - Technical data (IP addresses, device identifiers, cookies)
   - Usage data (service interaction records, preferences)
   - Communications data (support tickets, correspondence)
   - Profiling data (segments, scores, automated decisions)
3. Prepare the supplementary information required under Art. 15(1)(a)-(h).
4. Apply redactions for exempted data with clear notation that redactions have been made and the legal basis for each.
5. Format the response in a commonly used electronic format (PDF for the cover letter, structured data in CSV/JSON where applicable).

### Step 7: Quality Assurance Review

1. Verify completeness: all identified systems have been queried and results compiled.
2. Verify accuracy: spot-check data against source systems.
3. Verify redactions: confirm each redaction is legally justified and documented.
4. Verify the response addresses all elements of Art. 15(1)(a)-(h).
5. Obtain sign-off from the Data Protection Officer or designated privacy lead.

### Step 8: Deliver the Response

1. Transmit the response via a secure channel:
   - Encrypted email (TLS 1.2+ in transit, AES-256 encrypted attachment)
   - Secure download portal with time-limited access link (72-hour expiry)
   - Registered postal mail with delivery confirmation (for non-electronic requests)
2. Record the delivery date, method, and confirmation of receipt.
3. Update the DSAR register with the closure date and outcome.

### Step 9: Post-Response Actions

1. Retain the DSAR processing record (request, internal notes, redaction justifications, copy of response) for a minimum of 3 years to demonstrate compliance.
2. If the data subject is dissatisfied, inform them of their right to lodge a complaint with the relevant supervisory authority under Art. 77.
3. Feed any systemic issues identified during the DSAR process into the organisation's data governance improvement programme.

## Fee and Refusal Provisions

### Reasonable Fee (Art. 12(5)(a))

A controller may charge a reasonable fee taking into account the administrative costs of providing the information or communication or taking the action requested where:
- The request is **manifestly unfounded** (e.g., the requester has explicitly stated they intend to cause disruption), or
- The request is **excessive** (e.g., the same individual submits a fourth identical DSAR within a 12-month period without any change in processing activities).

The fee at Meridian Analytics Ltd is calculated as: GBP 10.00 base fee + GBP 0.10 per page exceeding 500 pages of output.

### Refusal to Act (Art. 12(5)(b))

The controller may refuse to act on the request where it is manifestly unfounded or excessive, but must:
1. Inform the data subject of the reasons for refusal.
2. Inform the data subject of their right to lodge a complaint with the supervisory authority.
3. Inform the data subject of their right to seek a judicial remedy.
4. Document the refusal decision and its justification.

## EDPB Guidance References

- **EDPB Guidelines 01/2022 on data subject rights — Right of access**: Clarifies scope, means of access, third-party data handling, and relationship with other GDPR rights.
- **EDPB Guidelines on Transparency (WP260 rev.01)**: Provides guidance on the Art. 12 requirements for concise, transparent, intelligible, and easily accessible communication.
