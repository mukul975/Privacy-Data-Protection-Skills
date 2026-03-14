---
name: ccpa-consumer-requests
description: >-
  Manages California Consumer Privacy Act (CCPA) consumer rights requests under
  Civil Code sections 1798.100-125, covering the right to know, right to delete,
  right to opt-out of sale, and non-discrimination. Includes 45-day response
  window and identity verification requirements. Activate for CCPA, California
  privacy, right to know, right to delete, opt-out of sale queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-subject-rights
  tags: "ccpa, california-privacy, right-to-know, right-to-delete, opt-out-sale"
---

# Managing CCPA Consumer Requests

## Overview

The California Consumer Privacy Act (CCPA), as amended by the California Privacy Rights Act (CPRA), grants California consumers specific rights regarding their personal information. This skill provides the operational workflow for handling CCPA consumer requests, including the right to know, right to delete, right to correct, right to opt-out of sale/sharing, and the right to limit use of sensitive personal information.

## Legal Foundation

### CCPA / CPRA Core Provisions

#### Right to Know (Cal. Civ. Code Section 1798.100, 1798.110, 1798.115)

Consumers have the right to request that a business disclose:
- The categories of personal information collected (Section 1798.110(a)(1))
- The categories of sources from which personal information is collected (Section 1798.110(a)(2))
- The business or commercial purpose for collecting, selling, or sharing personal information (Section 1798.110(a)(3))
- The categories of third parties to whom personal information is disclosed (Section 1798.110(a)(4))
- The specific pieces of personal information the business has collected about the consumer (Section 1798.110(a)(5))

#### Right to Delete (Cal. Civ. Code Section 1798.105)

Consumers have the right to request that a business delete any personal information about the consumer which the business has collected. The business must delete the consumer's personal information from its records, notify service providers and contractors to delete, and notify third parties who purchased or received the information to delete.

Exceptions to deletion (Section 1798.105(d)):
1. Complete a transaction or provide a requested service
2. Detect security incidents or protect against fraud
3. Debug to identify and repair errors
4. Exercise free speech or another legal right
5. Comply with the California Electronic Communications Privacy Act
6. Engage in research in the public interest (with consumer consent)
7. Enable solely internal uses reasonably aligned with consumer expectations
8. Comply with a legal obligation
9. Otherwise use the information internally in a lawful manner compatible with collection context

#### Right to Opt-Out of Sale/Sharing (Cal. Civ. Code Section 1798.120, 1798.135)

Consumers have the right to direct a business that sells or shares their personal information to third parties to stop selling or sharing that personal information. A business must provide a clear and conspicuous "Do Not Sell or Share My Personal Information" link on its website.

#### Right to Non-Discrimination (Cal. Civ. Code Section 1798.125)

A business shall not discriminate against a consumer because the consumer exercised any of their CCPA rights, including by:
- Denying goods or services
- Charging different prices or rates
- Providing a different level or quality of goods or services
- Suggesting the consumer will receive different treatment

#### Right to Correct (Cal. Civ. Code Section 1798.106)

Added by CPRA: consumers have the right to request correction of inaccurate personal information.

#### Right to Limit Use of Sensitive Personal Information (Cal. Civ. Code Section 1798.121)

Added by CPRA: consumers have the right to limit a business's use of their sensitive personal information to purposes necessary to perform the services or provide the goods requested.

## CCPA Consumer Request Workflow

### Step 1: Receive the Request

CCPA requires at least two methods for submitting requests:
- Toll-free telephone number
- Website form or email address
- If the business operates exclusively online, only the email method is required

1. Log with reference CCPA-YYYY-NNNN.
2. Record the request type (know, delete, correct, opt-out, limit).
3. Record the channel of receipt.
4. Acknowledge receipt within 10 business days.

### Step 2: Verify the Consumer's Identity

CCPA regulations (11 CCR Section 7060-7064) require verification proportional to the type of request:

| Request Type | Verification Standard | Method |
|-------------|----------------------|--------|
| Right to know — categories | Reasonable degree of certainty | Match at least 2 data points (name + email, name + account number) |
| Right to know — specific pieces | Reasonably high degree of certainty | Match at least 3 data points + signed declaration under penalty of perjury |
| Right to delete | Reasonable degree of certainty | Match at least 2 data points |
| Right to correct | Reasonable degree of certainty | Match at least 2 data points |
| Right to opt-out of sale | No verification required (unless fraudulent) | Confirm association with the business |

If the consumer has a password-protected account, the business may verify through the existing authentication process.

### Step 3: Process the Request

#### Right to Know

1. Identify all personal information collected in the preceding 12 months.
2. Compile response organised by CCPA categories:
   - Identifiers (name, address, email, SSN, driver's licence, passport, IP address, account name)
   - Customer records (financial information, insurance, education, employment)
   - Protected classification characteristics (age, race, sex, religion, disability)
   - Commercial information (purchase history, consumption tendencies)
   - Biometric information
   - Internet or other electronic network activity (browsing history, search history, interaction with website/app)
   - Geolocation data
   - Audio, electronic, visual, thermal, olfactory, or similar information
   - Professional or employment-related information
   - Education information (non-FERPA)
   - Inferences drawn from the above to create a consumer profile
   - Sensitive personal information (SSN, financial account, precise geolocation, racial/ethnic origin, religious beliefs, health data, sex life/orientation)
3. Disclose the categories of sources, business purposes, and third parties for each category.

#### Right to Delete

1. Verify the request per Step 2.
2. Assess whether any exceptions under Section 1798.105(d) apply.
3. If no exception, delete personal information from all systems.
4. Notify service providers and contractors to delete.
5. Notify third parties who purchased or received the information to delete.

#### Right to Opt-Out of Sale/Sharing

1. No identity verification required (process immediately).
2. Cease selling and sharing the consumer's personal information within 15 business days.
3. Do not sell/share for at least 12 months unless consumer provides subsequent authorization.
4. Apply to all future sale/sharing activities.

### Step 4: Respond to the Consumer

| Request Type | Response Deadline | Format |
|-------------|-------------------|--------|
| Right to know | 45 calendar days (extendable by 45 additional days with notice) | Written (email or postal), in a portable and readily useable format |
| Right to delete | 45 calendar days (extendable by 45 additional days) | Written confirmation |
| Right to correct | 45 calendar days (extendable by 45 additional days) | Written confirmation |
| Right to opt-out | 15 business days | Written confirmation |
| Right to limit sensitive PI | 15 business days | Written confirmation |

### Step 5: Document and Retain

1. Record the request, verification process, response, and outcome.
2. Retain records for 24 months per CCPA regulations (11 CCR Section 7101).
3. If the business receives 10 million or more consumer records annually, compile and publish annual metrics (number of requests received, complied with, denied, median response time).

## Non-Discrimination Requirements

When a consumer exercises any CCPA right, the business must not:
- Deny goods or services
- Charge different prices (unless reasonably related to the value provided by the consumer's data)
- Provide a different level or quality of goods or services
- Suggest the consumer will receive a different price or quality

Financial incentive programmes (e.g., loyalty programmes) must be disclosed in the privacy notice and require consumer opt-in consent. The incentive must be reasonably related to the value of the consumer's data.
