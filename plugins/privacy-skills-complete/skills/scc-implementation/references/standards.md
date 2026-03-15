# Standards and Regulatory References

## Primary Legislation

### Commission Implementing Decision (EU) 2021/914
- **Date of adoption**: 4 June 2021
- **Effective date**: 27 June 2021
- **Transition deadline**: 27 December 2022 (all prior SCC sets must be replaced)
- **Legal basis**: Article 46(2)(c) of Regulation (EU) 2016/679
- **Structure**: Four modules covering C2C, C2P, P2P, P2C transfer relationships
- **Annexes**: Annex I (parties and transfer description), Annex II (technical and organisational measures), Annex III (sub-processor list)

### GDPR Article 46 — Transfers Subject to Appropriate Safeguards
- **Art. 46(1)**: In the absence of an adequacy decision under Art. 45, transfers may occur only if the controller or processor has provided appropriate safeguards and enforceable data subject rights and effective legal remedies are available.
- **Art. 46(2)(c)**: SCCs adopted by the Commission constitute appropriate safeguards within the meaning of paragraph 1.
- **Art. 46(5)**: Authorisations and SCCs adopted under Directive 95/46/EC remain valid until amended, replaced, or repealed.

### GDPR Article 28 — Processor
- **Art. 28(3)**: Processing by a processor shall be governed by a contract or other legal act setting out the subject-matter and duration of processing, nature and purpose, type of personal data, categories of data subjects, and obligations and rights of the controller. Module 2 SCCs incorporate these requirements.
- **Art. 28(4)**: Where a processor engages a sub-processor, the same data protection obligations as set out in the contract between controller and processor must be imposed. Module 3 SCCs serve this function.

### Schrems II — Court of Justice of the European Union, Case C-311/18
- **Date**: 16 July 2020
- **Key holdings**: (1) Privacy Shield adequacy decision invalidated; (2) SCCs remain valid in principle but require case-by-case assessment of whether the legal framework of the third country ensures adequate protection; (3) Supplementary measures may be needed to bridge protection gaps.
- **Impact on SCCs**: Clause 14 of the 2021 SCCs directly addresses the Schrems II requirement by obligating parties to conduct a Transfer Impact Assessment.

## Regulatory Guidance

### EDPB Recommendations 01/2020 on Supplementary Measures (Version 2.0, Adopted 18 June 2021)
- Six-step assessment methodology for determining whether supplementary measures are necessary and which measures are effective.
- Directly referenced by Clause 14(b) of the 2021 SCCs.
- Categories of supplementary measures: technical, contractual, and organisational.

### EDPB Recommendations 02/2020 on Essential Guarantees for Government Access (Adopted 10 November 2020)
- Four European Essential Guarantees: (1) clear, precise, accessible rules; (2) necessity and proportionality; (3) independent oversight; (4) effective remedies.
- Applied when assessing whether Clause 14/15 obligations can be satisfied in a given destination country.

### EDPB Guidelines 05/2021 on the Interplay Between Art. 3 and Chapter V (Adopted 18 November 2021)
- Clarifies when a data transfer occurs under the GDPR and Chapter V transfer rules apply.
- Relevant for determining whether SCCs are required for a given data flow.

### European Commission Q&A on the New SCCs (Published June 2021, Updated December 2021)
- Confirms that additional commercial clauses may be added in a separate annex but must not contradict the SCCs.
- Clarifies the docking clause (Clause 7) mechanism for adding new parties.
- Addresses multi-party SCC execution.

## Enforcement Precedents

### Austrian DPA (DSB) — Decision D550.738 (2022)
- Google Analytics transfer to the United States found non-compliant despite SCCs because supplementary measures were insufficient to address FISA Section 702 access.
- Significance: Demonstrates that SCCs alone do not guarantee lawful transfer; Clause 14 assessment must be substantive.

### French CNIL — Decision on Google Analytics (February 2022)
- Aligned with the Austrian DSB decision; found that Google's SCCs and supplementary measures did not sufficiently protect transferred data against US government access.
- Ordered the website operator to bring analytics processing into compliance within one month.

### Italian Garante — Decision on Google Analytics (June 2022)
- Third coordinated enforcement action on the same transfer mechanism gap.
- Reinforced that the Clause 14 Transfer Impact Assessment must produce a documented, substantive analysis rather than a formalistic check.

### Berlin DPA (BlnBDI) — Warning to Employer Regarding Third-Country HR Data Transfer (2023)
- Employer using a US-based HR platform relied on SCCs Module 2 but had not completed a documented TIA.
- BlnBDI issued a formal warning and required documented evidence of Clause 14 compliance within 60 days.

## ISO/IEC Standards

- **ISO/IEC 27701:2019**: Section 7.5 on data transfer controls aligns with SCC Annex II requirements for technical and organisational measures.
- **ISO/IEC 27001:2022**: Annex A Control 5.34 (Privacy and protection of PII) and Control 5.14 (Information transfer) support the security measures documentation required in SCC Annex II.
- **ISO/IEC 27018:2019**: Code of practice for protection of PII in public clouds, relevant to Module 2 and Module 3 SCCs involving cloud processor transfers.
