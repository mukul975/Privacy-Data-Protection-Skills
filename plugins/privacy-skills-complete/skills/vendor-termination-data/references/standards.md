# Regulatory Standards — Vendor Termination Data

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 28(3)(g)**: "At the choice of the controller, [the processor shall] delete or return all the personal data to the controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data." This is the foundational termination data obligation.

- **Article 5(1)(e)**: Storage limitation — personal data shall be "kept in a form which permits identification of data subjects for no longer than is necessary for the purposes for which the personal data are processed." Once the processing relationship ends, the purpose ceases.

- **Article 17**: Right to erasure — while directed at controller-data subject obligations, it establishes the standard for what constitutes adequate data deletion.

### EDPB Guidelines 07/2020 on Controller and Processor Concepts

- **Paragraph 108**: "The obligation to delete or return data after the end of the provision of services extends to all copies of personal data, including backup copies. The controller should verify that all data has been deleted or returned."

- **Paragraph 109**: "Where the processor is required by Union or Member State law to retain certain personal data, it should inform the controller and limit the processing to that required by law."

### NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization

Provides the technical standard for data sanitization:
- **Clear**: Logical techniques to sanitize data (overwrite, block erase)
- **Purge**: Physical or logical techniques rendering data recovery infeasible (crypto-erase, degauss)
- **Destroy**: Physical destruction rendering media unusable (disintegrate, incinerate, shred)

### ISO/IEC 27001:2022

- **A.8.10 — Information deletion**: "Information stored in information systems, devices or in any other storage media shall be deleted when no longer required."

## Supervisory Authority Guidance

### Bavarian DPA (BayLDA) — Data Deletion Guidance

The BayLDA has provided practical guidance on processor data deletion:
- Deletion must cover all copies including backups and caches
- The controller should obtain written confirmation of deletion
- Spot checks or audits of deletion may be appropriate for high-risk data
- Backup deletion may occur on a rolling basis as backup tapes expire

### Danish DPA (Datatilsynet) — Data Deletion Enforcement

The Datatilsynet found a controller non-compliant for failing to verify processor data deletion after contract termination. The controller assumed deletion occurred but had no written confirmation — this was deemed insufficient accountability.

### French DPA (CNIL) — Data Retention and Deletion

CNIL emphasizes:
- Controllers must actively verify processor deletion, not assume it
- Deletion certification should be stored as an accountability artifact
- Where backup deletion is technically delayed (e.g., tape rotation), this must be documented with a maximum timeline
