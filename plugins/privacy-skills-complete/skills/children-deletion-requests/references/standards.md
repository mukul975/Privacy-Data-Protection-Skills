# Standards and Regulatory References — Children's Deletion Requests

## Primary Legislation

### GDPR Article 17 — Right to Erasure ('Right to Be Forgotten')

- **Art. 17(1)**: "The data subject shall have the right to obtain from the controller the erasure of personal data concerning him or her without undue delay and the controller shall have the obligation to erase personal data without undue delay where one of the following grounds applies:"
  - **(a)**: The personal data are no longer necessary for the purposes for which they were collected or otherwise processed.
  - **(b)**: The data subject withdraws consent on which the processing is based and there is no other legal ground for the processing.
  - **(c)**: The data subject objects to the processing pursuant to Art. 21(1) and there are no overriding legitimate grounds for the processing, or the data subject objects to processing pursuant to Art. 21(2).
  - **(d)**: The personal data have been unlawfully processed.
  - **(e)**: The personal data have to be erased for compliance with a legal obligation.
  - **(f)**: The personal data have been collected in relation to the offer of information society services directly to a child referred to in Article 8(1).

- **Art. 17(2)**: "Where the controller has made the personal data public, the controller shall, taking account of available technology and the cost of implementation, take reasonable steps, including technical measures, to inform controllers which are processing the personal data that the data subject has requested the erasure by such controller of any links to, or copy or replication of, those personal data."

- **Art. 17(3)**: Exceptions where erasure does not apply: (a) freedom of expression and information; (b) compliance with legal obligation; (c) public health; (d) archiving in public interest, scientific/historical research, statistical purposes; (e) establishment, exercise or defence of legal claims.

### GDPR Article 12(3) — Response Timeline

"The controller shall provide information on action taken on a request under Articles 15 to 22 to the data subject without undue delay and in any event within one month of receipt of the request. That period may be extended by two further months where necessary, taking into account the complexity and number of the requests."

### GDPR Article 19 — Notification Obligation Regarding Erasure

"The controller shall communicate any erasure of personal data [...] to each recipient to whom the personal data have been disclosed, unless this proves impossible or involves disproportionate effort. The controller shall inform the data subject about those recipients if the data subject requests it."

### GDPR Recital 65 — Right to Rectification and Erasure

"A data subject should have the right to have his or her personal data erased and no longer processed where the personal data are no longer necessary in relation to the purposes for which they are collected or otherwise processed, where a data subject has withdrawn his or her consent [...]. That right is relevant in particular where the data subject has given his or her consent as a child and is not fully aware of the risks involved by the processing, and later wants to remove such personal data, especially on the internet. The data subject should be able to exercise that right notwithstanding the fact that he or she is no longer a child."

### COPPA Section 312.6 — Parental Access and Deletion

- **312.6(a)**: Operator must provide a parent, upon request, with the opportunity to direct the operator to delete the personal information collected from the child.
- **312.6(b)**: Operator must delete the child's personal information within a reasonable time.
- **312.6(c)**: Operator must employ reasonable procedures to verify the identity of the parent making the request.

### UK AADC Standard 15 — Online Tools

"Provide prominent and accessible tools to help children exercise their data protection rights and report concerns."

ICO guidance:
- Deletion tools must be child-accessible (one-click or equivalent)
- Children should not need to navigate adult-oriented settings to request deletion
- Reporting tools should not require additional personal data
- Tools should empower children to manage their own privacy as they mature

## Regulatory Guidance

### EDPB Guidelines on the Right to Erasure (Under Development, 2024)

Draft guidelines address:
- Scope of erasure obligation across systems (production, backups, third parties)
- Timeline expectations (without undue delay, maximum one month)
- Technical implementation of erasure (deletion vs. anonymisation)
- Verification of erasure across complex data architectures

### EDPB Guidelines 05/2020 on Consent — Section on Children

- Parental consent can be withdrawn at any time per Art. 7(3)
- Withdrawal triggers the right to erasure of data collected under that consent
- The process for withdrawal must be as easy as the process for giving consent

### ICO Right to Erasure Guidance (2023)

- Controllers must respond to erasure requests within one month
- If more time is needed, the controller must inform the data subject within the first month and provide a reason
- Erasure must be from all systems including backups (within a reasonable backup cycle)
- Third parties must be notified per Art. 17(2) and Art. 19
- For children's data: the ICO expects controllers to prioritise erasure requests and process them faster than adult requests where possible

### CJEU Case Law

- **C-131/12 Google Spain (2014)**: Established the right to erasure in the search engine context. The Court noted that the right to erasure is particularly important when data was published during the data subject's minority.
- **C-507/17 Google v CNIL (2019)**: Clarified the territorial scope of the right to erasure (EU-wide but not necessarily global).
- **C-460/20 TU and RE (2022)**: Confirmed that the right to erasure extends to inaccurate data and that controllers must take reasonable steps to verify accuracy before refusing erasure.

## Enforcement Decisions

- **TikTok (ICO, 2023)**: GBP 12.7 million fine. ICO found that TikTok did not provide adequate mechanisms for parents and children to exercise their data protection rights, including deletion.
- **Musical.ly/TikTok (FTC, 2019)**: USD 5.7 million settlement. FTC required TikTok to delete all personal information collected from children under 13 and to provide a mechanism for parents to request deletion of their children's information going forward.
- **Edmodo (FTC, 2023)**: USD 6 million. FTC order required Edmodo to delete children's personal information collected in violation of COPPA and to establish a deletion program.
- **Google (CNIL, 2022)**: EUR 150 million for making it difficult for users to exercise opt-out rights, with the large child user base as an aggravating factor.
- **Instagram/Meta (DPC Ireland, 2022)**: EUR 405 million. Included findings on inadequate tools for children to exercise their data protection rights.

## Technical Standards

### NIST SP 800-88 Rev. 1 — Guidelines for Media Sanitization (2014)

- Provides guidance on media sanitization methods to ensure data is irrecoverable.
- Clear: overwriting data with non-sensitive data using standard read/write commands.
- Purge: rendering data irrecoverable using dedicated sanitization equipment or techniques.
- Destroy: physical destruction of the storage media.
- Applicable to backup media containing children's data that must be sanitized.

### ISO/IEC 27001:2022 — Annex A Control A.8.10

- Requirement for information deletion: "Information stored in information systems, devices or in any other storage media shall be deleted when no longer required."
- Supports systematic deletion processes for children's data.

### ISO/IEC 27701:2019 — Section 7.4.5

- "The organization shall have procedures in place for permanent de-identification or disposal of PII at the end of its retention period or when it is no longer necessary for the identified purpose."
