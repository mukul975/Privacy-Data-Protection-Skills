# UK International Data Transfer — Implementation Template

## Transfer Identification

| Field | Value |
|-------|-------|
| UK Transfer Reference | UK-TRF-2025-HK-001 |
| Assessment Date | 14 March 2025 |
| UK Data Protection Manager | David Morrison, Athena Logistics (UK) Ltd |

## Adequacy Check

| Question | Answer |
|----------|--------|
| Does the destination country have UK adequacy regulations? | No — Hong Kong SAR is not on the UK adequacy list |
| Transfer mechanism required | IDTA or UK Addendum to EU SCCs |
| Selected instrument | UK Addendum to EU SCCs (EU SCCs already executed with this importer) |

## UK Addendum — Table Completion

### Table 1: Parties

| Field | Value |
|-------|-------|
| EU SCC Reference | SCC-2025-APAC-001 |
| Exporter | Athena Logistics (UK) Ltd, 30 Fenchurch Street, London EC3M 3BD |
| Importer | TransPacific Freight Solutions Ltd, 88 Harbour Road, Wan Chai, Hong Kong SAR |

### Table 2: Selected SCCs

| Field | Value |
|-------|-------|
| EU SCC Version | Commission Implementing Decision (EU) 2021/914 |
| Module | Module 2: Controller to Processor |
| Execution Date | 15 March 2025 |

### Table 3: Appendix Information

Appendix information is as set out in the EU SCC Annexes I-III (no UK-specific variations required).

### Table 4: Ending the Addendum

Selected approach: If the ICO issues a revised Approved Addendum, the parties will review the changes within 30 days. Either party may end the Addendum by providing 30 days' written notice if the revised Addendum materially reduces the protections for personal data.

## ICO Transfer Risk Assessment

| TRA Reference | TRA-2025-HK-001 |
|---------------|-----------------|
| Assessment Date | 14 March 2025 |
| Destination Country | Hong Kong SAR |

### Risk Factor Scores (0-5 scale: 5 = equivalent to UK)

| Factor | Score | Notes |
|--------|-------|-------|
| Rule of law and human rights | 4 | Independent judiciary; concerns about NSL impact on judicial independence |
| Data protection legislation | 3 | PDPO (Cap. 486) provides baseline but lacks comprehensive individual rights equivalent to UK GDPR |
| Government access to data | 2 | NSL provides broad powers; Cap. 589 has judicial oversight but NSL oversight is limited |
| Enforcement and redress | 3 | PCPD handles complaints; judicial review available but limited for NSL matters |
| Data sensitivity | 4 | Commercial freight data; low sensitivity |
| Transfer volume | 3 | Ongoing operational transfer; medium volume |
| Importer profile | 4 | Logistics company; not in high-risk sector for government access |
| Technical measures | 4 | TLS 1.3, AES-256, RBAC, ISO 27001 |

### TRA Conclusion

| Field | Value |
|-------|-------|
| Overall Risk Level | Medium |
| Extra Protection Clauses Required | Yes |
| Measures | Encryption with UK-held keys (archived data), challenge obligation, transparency notification, audit rights, access restriction |

## Execution Record

| Field | Value |
|-------|-------|
| Addendum Execution Date | 15 March 2025 |
| Exporter Signatory | David Morrison, UK Data Protection Manager |
| Importer Signatory | James Leung, Chief Privacy Officer |
| Filed In | UK Transfer Register, entry UK-TRF-2025-HK-001 |
| Next Review Date | 15 March 2026 |

## Comparison: EU TIA vs UK TRA for Same Transfer

| Element | EU TIA (TIA-2025-HK-001) | UK TRA (TRA-2025-HK-001) |
|---------|--------------------------|--------------------------|
| Legal standard | GDPR + EDPB EEG framework | UK GDPR + ICO TRA methodology |
| Conclusion | Amber (supplementary measures) | Medium risk (Extra Protection Clauses) |
| Measures aligned | Yes — same supplementary measures package applied |
| Separate documentation | Yes — separate TIA and TRA on file |
