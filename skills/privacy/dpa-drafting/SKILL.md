---
name: dpa-drafting
description: >-
  GDPR-compliant Data Processing Agreement drafting per Article 28(3). Covers all
  8 mandatory provisions including subject matter, duration, nature and purpose,
  data types, categories of data subjects, controller and processor obligations,
  and sub-processor cascade requirements.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: vendor-privacy-management
  tags: "dpa-drafting, article-28, data-processing-agreement, processor-contract, gdpr-compliance"
---

# Data Processing Agreement Drafting

## Overview

GDPR Article 28(3) mandates that processing by a processor shall be governed by a contract or other legal act that is binding on the processor. This contract must set out specific mandatory provisions covering the subject-matter and duration of processing, the nature and purpose, the type of personal data, the categories of data subjects, and the obligations and rights of the controller. The EDPB has emphasized in Guidelines 07/2020 that these requirements are not optional and that failure to include any mandatory element renders the DPA non-compliant.

The European Commission adopted Standard Contractual Clauses for controller-to-processor arrangements in Implementing Decision (EU) 2021/915, providing a reference framework that organizations may adopt or adapt.

## Mandatory DPA Provisions Under Article 28(3)

### Provision 1: Subject-Matter and Duration

The DPA must specify what processing the vendor will perform and for how long.

**Required Elements:**

| Element | Description | Example |
|---------|-------------|---------|
| Subject-matter | The specific service being provided | "Cloud-hosted customer analytics platform" |
| Duration | Period of processing | "Duration of the Master Services Agreement plus 90-day data return/deletion period" |
| Commencement date | When processing begins | "Effective as of the MSA effective date" |
| Survival clauses | Obligations surviving termination | "Confidentiality, deletion certification, and audit rights survive for 3 years" |

### Provision 2: Nature and Purpose of Processing

**Required Elements:**

| Element | Description | Example |
|---------|-------------|---------|
| Nature of processing | Operations performed on personal data | "Collection via API ingestion, storage in encrypted database, automated analysis, aggregated reporting, deletion upon contract termination" |
| Purpose of processing | Why processing occurs | "To provide Summit Cloud Partners with customer behavior analytics enabling product improvement decisions" |
| Processing instructions scope | Boundaries of processing | "Processor shall process personal data only for the purposes specified in Annex 1 and only on documented instructions from the Controller" |

### Provision 3: Type of Personal Data

Enumerate all categories of personal data the processor will handle.

**Summit Cloud Partners — Example Annex:**

| Data Category | Description | Sensitivity Level |
|--------------|-------------|-------------------|
| Contact information | Name, email address, phone number | Standard |
| Account identifiers | User ID, account number, tenant ID | Standard |
| Usage data | Feature usage logs, session duration, click paths | Standard |
| Device information | IP address, browser type, OS version | Standard |
| Location data | City/region derived from IP address (not precise GPS) | Elevated |
| Payment metadata | Transaction dates, plan type (not card numbers) | Elevated |

### Provision 4: Categories of Data Subjects

| Category | Description | Approximate Volume |
|----------|-------------|-------------------|
| Enterprise customers | Named users of Summit Cloud Partners platform | 50,000 |
| Trial users | Users on free trial accounts | 15,000 |
| API consumers | Developers using Summit Cloud Partners API | 5,000 |

### Provision 5: Obligations and Rights of the Controller

The DPA must set out what the controller is entitled to do and what the controller must provide to the processor:

1. **Right to issue instructions**: The controller has the right to issue documented written instructions regarding processing
2. **Right to audit**: The controller may audit the processor's compliance (Article 28(3)(h))
3. **Obligation to determine lawful basis**: The controller confirms that processing is lawful under Article 6
4. **Obligation to respond to data subjects**: The controller is responsible for responding to data subject requests, with processor assistance
5. **Obligation to notify processor of relevant changes**: Changes to processing instructions, data categories, or regulatory requirements

### Provision 6: Processor Obligations (Article 28(3)(a)-(h))

The eight mandatory processor obligations under Article 28(3):

**(a) Process only on documented instructions**

> "The Processor shall process personal data only on documented instructions from the Controller, including with regard to transfers of personal data to a third country or an international organisation, unless required to do so by Union or Member State law to which the Processor is subject; in such a case, the Processor shall inform the Controller of that legal requirement before processing, unless that law prohibits such information on important grounds of public interest."

**(b) Confidentiality obligations**

> "The Processor shall ensure that persons authorised to process the personal data have committed themselves to confidentiality or are under an appropriate statutory obligation of confidentiality."

**(c) Security measures (Article 32)**

> "The Processor shall implement all measures required pursuant to Article 32, including as appropriate: (i) pseudonymisation and encryption of personal data; (ii) the ability to ensure ongoing confidentiality, integrity, availability and resilience of processing systems; (iii) the ability to restore availability and access to personal data in a timely manner in the event of a physical or technical incident; (iv) a process for regularly testing, assessing, and evaluating the effectiveness of technical and organisational measures."

**(d) Sub-processor conditions**

> "The Processor shall not engage another processor without prior specific or general written authorisation of the Controller. In the case of general written authorisation, the Processor shall inform the Controller of any intended changes concerning the addition or replacement of other processors, thereby giving the Controller the opportunity to object to such changes."

**(e) Assist with data subject rights**

> "Taking into account the nature of the processing, the Processor shall assist the Controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the Controller's obligation to respond to requests for exercising the data subject's rights laid down in Chapter III."

**(f) Assist with compliance obligations**

> "The Processor shall assist the Controller in ensuring compliance with Articles 32 to 36, taking into account the nature of processing and the information available to the Processor."

**(g) Deletion or return after termination**

> "At the choice of the Controller, the Processor shall delete or return all personal data to the Controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data."

**(h) Audit rights**

> "The Processor shall make available to the Controller all information necessary to demonstrate compliance with the obligations laid down in Article 28, and allow for and contribute to audits, including inspections, conducted by the Controller or another auditor mandated by the Controller."

### Provision 7: Sub-Processor Cascade

When the processor engages sub-processors, Article 28(4) requires the same data protection obligations as in the controller-processor DPA to be imposed on the sub-processor by way of a contract. The sub-processor DPA must contain materially equivalent terms.

**Sub-processor management provisions:**

| Provision | Description |
|-----------|-------------|
| Authorization mechanism | General written authorization with notification of changes |
| Notification period | Minimum 30 calendar days before engaging new sub-processor |
| Objection right | Controller may object within the notification period |
| Objection consequence | If objection not resolved, either party may terminate affected services |
| Flow-down obligations | Sub-processor contract must impose equivalent Article 28(3) obligations |
| Liability | Processor remains fully liable for sub-processor compliance |

### Provision 8: International Transfers

If personal data will be transferred outside the EEA, the DPA must address the transfer mechanism:

| Transfer Scenario | Required Mechanism |
|------------------|-------------------|
| EEA to Adequacy country (per Art. 45) | Reference adequacy decision |
| EEA to non-adequate country | Standard Contractual Clauses (Commission Decision 2021/914) |
| EEA to non-adequate country with supplementary measures | SCCs plus technical/organizational/contractual supplementary measures per EDPB Recommendations 01/2020 |

## DPA Drafting Checklist

| # | Requirement | Article | Status |
|---|-------------|---------|--------|
| 1 | Subject-matter and duration specified | 28(3) | [ ] |
| 2 | Nature and purpose of processing defined | 28(3) | [ ] |
| 3 | Types of personal data listed | 28(3) | [ ] |
| 4 | Categories of data subjects listed | 28(3) | [ ] |
| 5 | Controller obligations and rights defined | 28(3) | [ ] |
| 6 | Processor processes only on documented instructions | 28(3)(a) | [ ] |
| 7 | Confidentiality obligations for authorized personnel | 28(3)(b) | [ ] |
| 8 | Article 32 security measures implemented | 28(3)(c) | [ ] |
| 9 | Sub-processor conditions and authorization | 28(3)(d) | [ ] |
| 10 | Assistance with data subject rights | 28(3)(e) | [ ] |
| 11 | Assistance with Articles 32-36 compliance | 28(3)(f) | [ ] |
| 12 | Deletion or return upon termination | 28(3)(g) | [ ] |
| 13 | Audit rights and information access | 28(3)(h) | [ ] |
| 14 | Sub-processor flow-down obligations per Art. 28(4) | 28(4) | [ ] |
| 15 | International transfer mechanism (if applicable) | 28(3), Ch. V | [ ] |
| 16 | Breach notification obligations per Art. 33(2) | 33(2) | [ ] |
| 17 | DPA is in writing (including electronic form) | 28(9) | [ ] |

## Key Regulatory References

- GDPR Article 28(3) — Mandatory DPA provisions
- GDPR Article 28(4) — Sub-processor flow-down obligations
- GDPR Article 28(9) — Written form requirement
- GDPR Article 32 — Security of processing
- GDPR Article 33(2) — Processor breach notification to controller
- Commission Implementing Decision (EU) 2021/915 — Standard Contractual Clauses for controller-to-processor
- EDPB Guidelines 07/2020 — Controller and processor concepts
- EDPB Recommendations 01/2020 — Supplementary measures for international transfers
