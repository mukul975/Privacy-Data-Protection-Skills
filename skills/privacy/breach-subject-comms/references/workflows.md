# Data Subject Breach Communication Workflow

## Phase 1: Notification Decision (Completed Before This Workflow Begins)

The Art. 34 communication workflow is initiated only after the breach risk assessment has determined that the breach is "likely to result in a high risk to the rights and freedoms of natural persons." The risk assessment workflow (conducting-breach-risk-assessment) must be completed first, with:
- Aggregate risk score of 13 or above (recommended) or 19 or above (mandatory)
- DPO recommendation for data subject notification
- Management approval to proceed with notification

## Phase 2: Preparation (Days 1-3 After Risk Assessment Confirmation)

### 2.1 Identify the Affected Population
1. Obtain the final list of affected data subjects from the investigation team, deduplicated by unique identifier.
2. Classify data subjects by category (customers, employees, business partners) as communication content may differ.
3. Determine the language requirements for each data subject based on their communication preferences or country of residence.
4. Verify current contact information for each data subject — email address, postal address, phone number.
5. Flag data subjects for whom no current contact information is available (candidates for Art. 34(3)(c) public communication).

### 2.2 Draft the Communication
1. Select the appropriate template based on breach scenario (financial data, health data, credential compromise, ransomware, insider threat).
2. Customize the template with breach-specific details:
   - Nature of the breach: what happened, when, how.
   - Specific data categories affected for this group of data subjects.
   - Specific consequences relevant to this data type.
   - Specific protective actions data subjects can take.
3. Review the draft against Art. 34(2) mandatory content checklist:
   - [ ] Nature of the breach described in clear and plain language
   - [ ] DPO or contact point name and contact details
   - [ ] Likely consequences described
   - [ ] Measures taken or proposed by the controller
   - [ ] Actionable steps data subjects can take to protect themselves
4. Remove all legal jargon, technical terminology, and acronyms. Apply the "would your non-technical relative understand this?" test.
5. Translate the communication into all required languages using professional human translators (not machine translation alone for legal notices).

### 2.3 Establish Support Infrastructure
1. Activate a dedicated breach response hotline with trained operators:
   - Phone: +49 30 7742 9000
   - Operating hours: Monday-Friday 08:00-20:00 CET, Saturday 09:00-17:00 CET
   - Staffing: minimum 8 operators per shift for breaches affecting over 10,000 individuals
2. Prepare a comprehensive FAQ document for hotline operators covering:
   - What happened and when
   - What data was involved
   - What the company is doing
   - What the individual should do
   - How to enroll in credit monitoring (if offered)
   - How to exercise data subject rights (access, erasure)
   - How to lodge a complaint with the supervisory authority
3. Set up a dedicated breach information web page at stellarpayments.eu/breach-support
4. Configure auto-acknowledgment for email responses to the breach notification

### 2.4 Legal Review
1. In-house legal counsel reviews the draft for accuracy, completeness, and potential liability exposure.
2. External counsel reviews if the breach involves litigation risk or regulatory proceedings.
3. Verify that the communication does not inadvertently waive legal privilege or make admissions that could prejudice the organization's position.
4. Confirm that the communication complies with the requirements of all applicable jurisdictions if data subjects span multiple countries.

## Phase 3: Distribution (Days 4-7)

### 3.1 Email Distribution
1. Send the notification from a recognizable sender address (breach-notification@stellarpayments.eu) that is not commonly used for marketing.
2. Use a clear, non-clickbait subject line: "Important Security Notice — Your [Stellar Payments] Account" or equivalent.
3. Include the full notification text in the email body — do not require the recipient to click a link to read the notification content.
4. Send in batches to manage delivery infrastructure load (10,000 per hour maximum for deliverability).
5. Monitor bounce rates and flag undeliverable addresses for postal fallback.

### 3.2 Postal Distribution
1. For data subjects without valid email addresses, or where emails bounced, dispatch postal notifications via registered mail.
2. Envelope must be clearly marked as an important security notice (not marketing).
3. Expected delivery timeline: 3-5 business days for domestic (Germany), 7-14 business days for international EU.

### 3.3 Supplementary Channels
1. In-app notification for users of the Stellar Payments mobile application and web portal.
2. SMS notification to data subjects with mobile numbers on file: "STELLAR PAYMENTS: Important security notice sent to your email regarding your account. Check your inbox or visit stellarpayments.eu/breach-support"
3. For Art. 34(3)(c) public communication (if applicable): prominent banner on stellarpayments.eu homepage, press release via PR Newswire, advertisement in Frankfurter Allgemeine Zeitung and Financial Times.

## Phase 4: Post-Communication Monitoring (Weeks 2-8)

1. Track hotline call volume and categorize inquiries by type (general concern, credit monitoring enrollment, rights exercise, complaint, media inquiry).
2. Monitor the breach support email inbox and ensure responses within 48 hours.
3. Track credit monitoring enrollment rates and follow up with data subjects who have not enrolled by week 4.
4. Monitor social media for public discussion of the breach and correct misinformation.
5. Provide weekly status reports to the DPO and CEO on data subject engagement metrics.
6. Maintain detailed records of all communications sent, channels used, and delivery confirmations for Art. 5(2) accountability documentation.

## Communication Timing Decision Matrix

| Factor | Notify Immediately | Notify Within 7 Days | Extended Timeline |
|--------|-------------------|---------------------|-------------------|
| Physical safety risk | Yes | — | — |
| Financial fraud imminent | Yes | — | — |
| Credential compromise | Yes (force reset) | — | — |
| Financial data exposed | — | Yes | — |
| Identity data exposed | — | Yes | — |
| Non-sensitive data only | — | — | Yes (14 days) |
| Law enforcement requests delay | Comply with request | — | Document request |
