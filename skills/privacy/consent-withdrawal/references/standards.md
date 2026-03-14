# Regulatory Standards — Implementing Consent Withdrawal

## Primary Regulations

### GDPR — Regulation (EU) 2016/679

- **Article 7(3)**: "The data subject shall have the right to withdraw his or her consent at any time. The withdrawal of consent shall not affect the lawfulness of processing based on consent before its withdrawal. Prior to giving consent, the data subject shall be informed thereof. It shall be as easy to withdraw consent as to give it."
- **Article 7(1)**: The controller must be able to demonstrate that consent was validly given — and by extension, must be able to demonstrate the withdrawal was properly processed.
- **Recital 42**: Consent is not freely given if the data subject is unable to refuse or withdraw consent without detriment. This means services must not degrade or threaten service termination upon consent withdrawal for optional processing.
- **Recital 66**: "To strengthen the right to be forgotten in the online environment, the right to erasure should also be extended in such a way that a controller who has made the personal data public should be obliged to inform the controllers which are processing such personal data to erase any links to, or copies or replications of those personal data." While this applies to erasure, the principle of downstream notification applies equally to consent withdrawal.

### ePrivacy Directive 2002/58/EC

- **Article 5(3)**: Consent for cookies and similar technologies must be withdrawable. Withdrawal should be possible through the same interface where consent was given (cookie consent banner or preference center).

## Supervisory Authority Guidance

### EDPB Guidelines 05/2020 on Consent

- **Paragraph 108**: Controllers should ensure that consent can be withdrawn easily. Where consent is obtained through electronic means, the data subject should be able to withdraw consent through the same electronic means.
- **Paragraph 112**: "Where consent was obtained via an electronic user interface (for example, through a website, an app, a log-in page, an email interface or similar), a data subject must be able to withdraw consent via the same type of electronic user interface."
- **Paragraph 113**: If consent is obtained through a service-specific user interface, withdrawal should be possible within that same user interface (e.g., through account settings), not through a different channel.
- **Paragraph 116**: A confirmation dialogue to prevent accidental withdrawal is acceptable and does not violate the equal ease requirement.
- **Paragraph 118**: The controller must be able to demonstrate that processing has ceased following withdrawal. This requires monitoring and audit capability.

## Enforcement Actions

### CNIL v. Google LLC (January 6, 2022) — EUR 150,000,000

The French supervisory authority fined Google partly because rejecting cookies on google.fr required multiple clicks while accepting required only one click. The CNIL held this violated the equal ease principle, as users had to click "Personnaliser" and then "Confirmer" to reject, while a single "Tout accepter" button was available.

### CNIL v. Meta Platforms Ireland Ltd. (January 6, 2022) — EUR 60,000,000

Similar finding for facebook.com: the "Accept Cookies" button was prominently displayed on the first layer while refusing required navigating to a secondary page.

### AEPD v. CaixaBank (January 2021) — EUR 6,000,000

The Spanish supervisory authority fined CaixaBank for, among other things, inadequate consent withdrawal mechanisms. Users could not easily withdraw consent given during the banking relationship, and withdrawal requests were not properly propagated to all processing systems.

### Hamburg DPA v. H&M (October 2020) — EUR 35,258,707.95

While primarily about excessive employee data processing, the Hamburg DPA noted deficiencies in H&M's consent withdrawal mechanisms for employee data, reinforcing that withdrawal must be technically effective across all processing systems.
