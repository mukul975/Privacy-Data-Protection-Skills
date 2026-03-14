# Regulatory Standards — Vendor Termination Data

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 28(3)(g)**: "At the choice of the controller, [the processor shall] delete or return all the personal data to the controller after the end of the provision of services relating to processing, and delete existing copies unless Union or Member State law requires storage of the personal data."

- **Article 5(1)(e)**: Storage limitation — personal data must be kept in a form which permits identification of data subjects for no longer than is necessary. At termination, the processing purpose has ceased, triggering the deletion obligation.

- **Article 17(1)**: Right to erasure. While primarily a data subject right, it reinforces the principle that personal data should not be retained beyond its necessary purpose.

### EDPB Guidelines 07/2020

- **Paragraph 108**: The deletion/return obligation covers all personal data, including copies, backups, and data held by sub-processors.
- **Paragraph 109**: The controller should specify the return format and deletion method in the DPA.
- **Paragraph 110**: Processors must be able to demonstrate that deletion has been carried out — deletion certification is best practice.

### NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization

Provides three levels of media sanitization:
- **Clear**: Overwriting data with non-sensitive values. Suitable for media that will be reused within the organization.
- **Purge**: Physical or logical techniques rendering data recovery infeasible. Suitable for media leaving organizational control.
- **Destroy**: Physical destruction of media. Suitable for highest-sensitivity data.

For cloud and virtual environments, cryptographic erasure (destroying encryption keys so encrypted data becomes unrecoverable) is recognized as an effective purge-equivalent method.

### ISO/IEC 27040:2015 — Storage Security

Provides guidance on secure storage management including:
- Data sanitization requirements for different storage types
- Verification of sanitization effectiveness
- Chain of custody for media destruction
- Cloud-specific storage security considerations

## Supervisory Authority Guidance

### Hamburg DPA — Data Deletion Verification (2023)

The Hamburg DPA emphasized that controllers must verify processor deletion, not merely accept self-certification. Recommended verification methods include:
- Independent audit of deletion procedures
- Review of deletion logs and technical evidence
- Sample verification where feasible
- Sub-processor deletion chain verification

### Danish DPA — Processor Termination Guidance (2022)

Datatilsynet published guidance recommending:
- Written deletion certification requirement in all DPAs
- Specific timeline for deletion (maximum 90 days post-termination)
- Coverage of backup and archive copies
- Sub-processor deletion coordination responsibility on the processor
