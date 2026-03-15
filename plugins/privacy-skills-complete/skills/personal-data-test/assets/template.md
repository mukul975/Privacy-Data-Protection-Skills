# Personal Data Classification Assessment Record

## Organisation: Vanguard Financial Services
## Assessment Reference: DC-2026-CRM-001
## Assessment Date: 2026-03-14
## Assessor: Sarah Mitchell, Senior Privacy Analyst
## Reviewer: Dr. James Whitfield, Data Protection Officer

---

## 1. Data Element Details

| Field | Value |
|-------|-------|
| **Element Name** | Customer Full Name |
| **System** | CRM Platform (Salesforce instance) |
| **Database/Table** | `customer_master.contact_details` |
| **Field Name** | `full_name` |
| **Data Type** | VARCHAR(255) |
| **Source** | Collected directly from data subject during account onboarding |
| **Volume** | 2.4 million records |
| **Retention Period** | Duration of customer relationship + 7 years (regulatory requirement) |

---

## 2. Art. 4(1) Four-Element Test

### Element 1: Any Information

| Criterion | Assessment |
|-----------|-----------|
| Is this information in any form? | YES — textual data representing a person's legal name |
| Format restrictions? | No format restriction under Art. 4(1); all formats qualify |

**Result**: SATISFIED

### Element 2: Relating to a Natural Person

| Link Type | Assessment | Satisfied? |
|-----------|-----------|-----------|
| **Content link** | The full name is biographical information directly about the customer as a natural person | YES |
| **Purpose link** | The name is used to identify and communicate with the customer, to manage their financial accounts, and to fulfil regulatory KYC obligations | YES |
| **Result link** | Processing of the name enables financial services delivery and affects the customer's legal relationship with Vanguard | YES |

**Reasoning**: The customer full name satisfies all three sub-elements of the "relating to" test established in WP29 Opinion 4/2007 (WP136). Any one would suffice under the Opinion's framework.

**Result**: SATISFIED

### Element 3: Identified or Identifiable Natural Person

| Criterion | Assessment |
|-----------|-----------|
| **Direct identification** | YES — a full name directly identifies the individual in combination with the account context |
| **Uniqueness consideration** | While full names are not globally unique, within the Vanguard CRM context each name is associated with a specific customer record containing corroborating identifiers (address, account number) |
| **Recital 26 assessment** | Not required — direct identification established |
| **Breyer test** | Not applicable — direct identifier |

**Result**: SATISFIED — Direct identification

### Element 4: Natural Person

| Criterion | Assessment |
|-----------|-----------|
| Living human being? | YES — customer records represent living individuals. Deceased customer records are flagged and subject to separate retention policy |
| Legal entity exclusion? | Confirmed — corporate client names are stored in a separate `corporate_master` table |

**Result**: SATISFIED

---

## 3. Classification Decision

| Assessment Step | Outcome |
|----------------|---------|
| All four elements satisfied? | YES |
| Direct or indirect identification? | Direct |
| Special category indicators (Art. 9)? | NO — full name alone is not special category data |
| Criminal data indicators (Art. 10)? | NO |

### Classification: `PERSONAL_DIRECT`

---

## 4. Legal Basis and Compliance Requirements

| Requirement | Detail |
|-------------|--------|
| **Art. 6 Lawful Basis** | Art. 6(1)(b) — necessary for performance of contract (financial services agreement); Art. 6(1)(c) — necessary for compliance with KYC/AML legal obligations |
| **Art. 13/14 Privacy Notice** | Customer privacy notice Section 2.1 covers collection and use of identity data |
| **Art. 15 Access Rights** | Included in DSAR response scope; automated retrieval configured |
| **Art. 17 Erasure Rights** | Subject to regulatory retention override (7-year financial records requirement) |
| **Art. 20 Portability** | Available — collected on basis of contract, processed by automated means |
| **Art. 30 RoPA Entry** | Processing Activity PA-CRM-001, Category: Customer Identity Data |
| **Art. 32 Security** | Encrypted at rest (AES-256), access restricted to authorised CRM users via RBAC, audit logged |

---

## 5. Handling Requirements per Classification

| Control | Requirement |
|---------|-------------|
| **Access Control** | Role-based access; minimum Customer Service Representative role required |
| **Encryption** | AES-256 at rest, TLS 1.3 in transit |
| **Logging** | All access and modifications audit-logged with user ID and timestamp |
| **Retention** | Active customer relationship + 7 years post-termination |
| **Cross-border Transfer** | Subject to Chapter V safeguards; current SCCs in place for Salesforce US processing |
| **Breach Notification** | Art. 33 notification required if confidentiality or integrity compromised |
| **DPIA Required** | Not solely for name processing; included in CRM platform DPIA (DPIA-CRM-2025-001) |

---

## 6. Borderline Assessment (Not Applicable for This Element)

This section is completed only for elements classified as `BORDERLINE_REVIEW`. For reference, the Breyer assessment template is:

| Breyer Criterion | Assessment |
|-----------------|-----------|
| Complementary data holders identified | [List third parties holding linking data] |
| Legal means to access complementary data | [Describe contractual, legal, or regulatory basis] |
| Cost of identification | [Low / Medium / High — with justification] |
| Time required for identification | [Duration relative to retention period] |
| Technology required | [Standard / Specialist — with description] |
| Proportionate effort? | [YES/NO — with reasoning] |
| Motivation for identification | [Describe realistic identification scenarios] |
| **Conclusion** | [Personal data / Not personal data — with citation to Breyer para] |

---

## 7. Review Schedule

| Review Type | Date | Trigger |
|-------------|------|---------|
| **Next scheduled review** | 2028-03-14 | Biennial review for clear classifications |
| **Trigger-based review** | As needed | New data sharing agreement, technology change, regulatory guidance, or data breach |

---

## 8. Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| **Privacy Analyst** | Sarah Mitchell | 2026-03-14 | S. Mitchell |
| **DPO Review** | Dr. James Whitfield | 2026-03-14 | J. Whitfield |
| **System Owner** | Mark Thompson, CRM Manager | 2026-03-14 | M. Thompson |

---

*Classification conducted in accordance with Vanguard Financial Services Data Classification Policy DCP-2025-v3.1, applying GDPR Art. 4(1), Recital 26, CJEU C-582/14 (Breyer), and WP29 Opinion 4/2007 (WP136).*
