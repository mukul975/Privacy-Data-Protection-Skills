---
name: gdpr-dpa-art28
description: >-
  Guides the creation and review of data processing agreements under GDPR Article
  28(3), covering all eight mandatory clauses. References the 2021 Standard
  Contractual Clauses and provides a compliance checklist for processor contracts.
  Activate when onboarding processors, reviewing DPAs, or auditing processor
  compliance. Keywords: DPA, data processing agreement, Article 28, processor,
  mandatory clauses, standard contractual clauses.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "gdpr, dpa, article-28, processor, data-processing-agreement, scc"
---

# Establishing Data Processing Agreements

## Overview

Article 28(3) requires that processing by a processor is governed by a contract or other legal act that is binding on the processor and sets out specific mandatory elements. This skill details all eight mandatory clauses, provides a compliance checklist, and references the 2021 EU Standard Contractual Clauses for controller-to-processor transfers.

## Art. 28(3) Mandatory Elements

### Element 1: Subject-Matter and Duration
The DPA must specify the subject-matter of the processing (what processing is being carried out), the duration (aligned with the service contract term), the nature of the processing (collection, storage, analysis, deletion), and the purpose of the processing.

### Element 2: Type of Personal Data
The DPA must list the specific categories of personal data being processed (names, email addresses, financial data, health data, etc.).

### Element 3: Categories of Data Subjects
The DPA must identify which data subjects are affected (employees, customers, website visitors, patients, etc.).

### Element 4: Obligations and Rights of the Controller
The DPA must set out the controller's documented instructions to the processor, covering what the processor is authorised to do with the data.

### Element 5: Processor Obligations (Art. 28(3)(a)-(h))

**(a) Documented instructions**: The processor shall process personal data only on documented instructions from the controller, including with regard to transfers to third countries, unless required to do so by EU or Member State law — in which case the processor must inform the controller before processing (unless the law prohibits such notification).

**(b) Confidentiality**: The processor shall ensure that persons authorised to process the personal data have committed to confidentiality or are under an appropriate statutory obligation of confidentiality.

**(c) Security measures**: The processor shall take all measures required pursuant to Article 32 (security of processing).

**(d) Sub-processors**: The processor shall not engage another processor without prior specific or general written authorisation of the controller. In the case of general written authorisation, the processor must inform the controller of any intended changes concerning the addition or replacement of sub-processors, giving the controller the opportunity to object (Art. 28(2) and (4)).

**(e) Assistance with data subject rights**: The processor shall assist the controller by appropriate technical and organisational measures, insofar as this is possible, for the fulfilment of the controller's obligation to respond to data subject requests (Art. 15-22).

**(f) Assistance with GDPR obligations**: The processor shall assist the controller in ensuring compliance with Articles 32-36 (security, breach notification, DPIAs, prior consultation), taking into account the nature of processing and the information available to the processor.

**(g) Data return or deletion**: At the choice of the controller, the processor shall delete or return all personal data after the end of the provision of processing services, and delete existing copies unless EU or Member State law requires storage.

**(h) Audit and inspection**: The processor shall make available to the controller all information necessary to demonstrate compliance with Art. 28 obligations, and allow for and contribute to audits, including inspections, conducted by the controller or another auditor mandated by the controller.

### Element 6: International Transfers
If the processor or any sub-processor transfers personal data outside the EEA, appropriate safeguards must be in place (SCCs, BCRs, adequacy decision, or derogation).

### Element 7: Sub-Processor Chain
The processor must impose the same data protection obligations in the sub-processing contract. The initial processor remains fully liable to the controller for the sub-processor's performance (Art. 28(4)).

### Element 8: Written Form
The contract must be in writing, including in electronic form (Art. 28(9)).

## DPA Compliance Checklist

| # | Requirement | Art. Reference | Present? |
|---|------------|---------------|----------|
| 1 | Subject-matter and duration specified | Art. 28(3) | |
| 2 | Nature and purpose of processing defined | Art. 28(3) | |
| 3 | Types of personal data listed | Art. 28(3) | |
| 4 | Categories of data subjects identified | Art. 28(3) | |
| 5 | Processor acts only on documented instructions | Art. 28(3)(a) | |
| 6 | Notification if law requires processing beyond instructions | Art. 28(3)(a) | |
| 7 | Confidentiality commitment for authorised personnel | Art. 28(3)(b) | |
| 8 | Art. 32 security measures implemented | Art. 28(3)(c) | |
| 9 | Sub-processor authorisation mechanism specified | Art. 28(3)(d), 28(2) | |
| 10 | Sub-processor change notification procedure | Art. 28(4) | |
| 11 | Controller objection right to new sub-processors | Art. 28(2) | |
| 12 | Same obligations imposed on sub-processors | Art. 28(4) | |
| 13 | Assistance with data subject rights requests | Art. 28(3)(e) | |
| 14 | Assistance with Art. 32-36 obligations | Art. 28(3)(f) | |
| 15 | Data return or deletion upon contract end | Art. 28(3)(g) | |
| 16 | Audit and inspection rights for controller | Art. 28(3)(h) | |
| 17 | Information to demonstrate compliance | Art. 28(3)(h) | |
| 18 | International transfer safeguards (if applicable) | Art. 28(3), Ch. V | |
| 19 | Written form (including electronic) | Art. 28(9) | |
| 20 | Processor breach notification to controller | Art. 33(2) | |

## 2021 Standard Contractual Clauses Reference

Commission Implementing Decision (EU) 2021/914 of 4 June 2021 established new SCCs that include a Module Two (Controller to Processor) and Module Three (Processor to Processor) set. These SCCs can serve as the DPA or can supplement an existing DPA for international transfers. Key clauses in the controller-to-processor module:

- Clause 7: Docking clause (additional parties can accede)
- Clause 8: Data protection safeguards including Art. 28(3) requirements
- Clause 9: Sub-processor provisions with specific or general authorisation
- Clause 10: Data subject rights
- Clause 13: Supervision by supervisory authority
- Clause 14: Transfer impact assessment obligations
- Clause 15: Obligations in case of government access requests

## Practical Considerations

### Negotiation Priorities
1. **Audit rights**: Ensure meaningful audit rights, not just acceptance of SOC 2 reports as a substitute for on-site audits.
2. **Sub-processor transparency**: Require a current list of sub-processors and timely notification (at least 30 days) before changes.
3. **Breach notification timeline**: Art. 33(2) requires "without undue delay" — specify a concrete timeline (e.g., 24-48 hours).
4. **Data deletion evidence**: Require written certification of deletion with a specific format and timeline.
5. **Liability**: Art. 82(2) establishes processor liability for damage caused by non-compliance with processor-specific obligations or acting outside/against controller instructions.
