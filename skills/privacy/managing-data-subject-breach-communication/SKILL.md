---
name: managing-data-subject-breach-communication
description: >-
  Manages direct communication to affected data subjects following a personal
  data breach under GDPR Article 34 when the breach is likely to result in a
  high risk to their rights and freedoms. Covers the high risk threshold,
  required notification content per Art. 34(2), exemptions under Art. 34(3),
  and breach notification letter templates for five scenarios. Keywords: data
  subject notification, Article 34, high risk, breach communication, GDPR.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-breach-response
  tags: "data-subject-notification, article-34, high-risk, breach-letter, gdpr, communication"
---

# Managing Data Subject Breach Communication

## Overview

Article 34 of the GDPR requires controllers to communicate a personal data breach to affected data subjects "without undue delay" when the breach is "likely to result in a high risk to the rights and freedoms of natural persons." This obligation is separate from and additional to the Art. 33 supervisory authority notification. The communication must be in clear and plain language, directly accessible to the affected individuals, and must contain specific information prescribed by Art. 34(2).

## High Risk Threshold — When Art. 34 Applies

Art. 34 notification is triggered when the breach risk assessment yields a "high risk" determination. Per EDPB Guidelines 9/2022, Section 3.2, high risk is present when:

1. The breach involves special category data (Art. 9) or criminal conviction data (Art. 10) in combination with direct identifiers.
2. The breach enables identity theft — the compromised data includes government identifiers (national ID, tax ID, social security number) combined with other identifying information.
3. The breach involves financial data (bank account numbers, payment card details) that could be used to commit fraud.
4. The breach involves data of vulnerable individuals (minors, patients, employees in dependent relationships) where the consequences are amplified.
5. The breach involves a large volume of personal data (more than 1,000 individuals) with direct identifiers, even if the data is not special category.
6. The breach could lead to physical harm, discrimination, or threat to the life or safety of individuals.

## Required Content — Art. 34(2)

The data subject communication must contain, at minimum, the information specified in Art. 33(3)(b), (c), and (d):

### (b) DPO or Contact Point Details
- Name and contact details of the DPO or other designated contact point where data subjects can obtain further information.
- At Stellar Payments Group: Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001.
- A dedicated breach response hotline should be established for breaches affecting more than 1,000 individuals.

### (c) Likely Consequences
- Description of the likely consequences of the breach written in plain language that a non-technical data subject can understand.
- Avoid legal jargon and technical terminology.
- Be specific about what could happen: "Your name, email address, and partial payment card number were exposed. This means someone could attempt to use this information to send you convincing phishing emails or attempt fraudulent transactions."

### (d) Measures Taken or Proposed
- What the controller has done to address the breach.
- What the controller is doing to mitigate adverse effects.
- What the data subject can do to protect themselves (specific, actionable steps).

### Additional Required Element: Nature of the Breach
- Although Art. 34(2) references only (b), (c), and (d) of Art. 33(3), the introductory text of Art. 34(1) requires the controller to "communicate the personal data breach to the data subject." This inherently requires describing the nature of the breach.

## Exemptions Under Art. 34(3)

A controller may be exempt from direct data subject notification in three circumstances:

### (a) Technical Protection Measures
The controller has applied appropriate technical and organisational protection measures that render the personal data unintelligible to any person who is not authorized to access it, such as encryption.

**Requirements for this exemption:**
- The encryption must be state-of-the-art (AES-256 or equivalent).
- The encryption keys must not have been compromised in the same breach.
- The encryption must have been applied to all affected data, not just a subset.
- The controller must be able to demonstrate that the encryption was in place before the breach occurred.

### (b) Subsequent Measures
The controller has taken subsequent measures which ensure that the high risk to the rights and freedoms of data subjects is no longer likely to materialise.

**Requirements for this exemption:**
- The measures must definitively eliminate the risk, not merely reduce it.
- The controller must have high confidence that the data has not been accessed or used by unauthorized persons.
- The window of exposure must have been very brief.

### (c) Disproportionate Effort
Individual notification would involve disproportionate effort, in which case a public communication or similar measure shall be made instead.

**Requirements for this exemption:**
- The controller must demonstrate why individual notification is disproportionate (e.g., outdated contact details for a large proportion of affected individuals).
- The public communication must be equally effective in reaching affected individuals.
- Channels: prominent website banner, national newspaper advertisements, coordinated social media announcements, broadcast media notification.

## Communication Channels and Timing

### Preferred Channels (in order of priority)
1. **Direct email** to the email address on file — fastest and most verifiable delivery.
2. **Postal letter** to the physical address on file — required fallback when email is unavailable or unreliable.
3. **SMS notification** with link to detailed information — supplementary channel for time-sensitive breaches.
4. **In-app notification** — for breaches affecting users of mobile or web applications.
5. **Public communication** — only when Art. 34(3)(c) disproportionate effort exemption applies.

### Timing Requirements
- "Without undue delay" under Art. 34(1) means as quickly as possible.
- EDPB guidance suggests data subject notification should occur within days, not weeks, of the breach determination.
- Stellar Payments Group internal standard: data subject notifications dispatched within 7 calendar days of the risk assessment confirming high risk.

## Language and Accessibility Requirements

1. **Clear and plain language**: Art. 34(2) explicitly requires the communication to describe the breach "in clear and plain language." Avoid legal terminology, technical jargon, and acronyms.
2. **Language of the data subject**: Notifications must be in the language in which the controller normally communicates with the data subject. For a controller operating across Europe, this means multilingual notifications.
3. **Accessibility**: Notifications must be accessible to individuals with disabilities (WCAG 2.1 AA compliance for digital channels; large print or audio alternatives for postal communications upon request).
4. **Separate communication**: The breach notification should not be bundled with marketing communications, invoices, or other routine correspondence. It must be clearly identifiable as a data breach notification.

## Scenario-Specific Communication Templates

### Scenario 1: Financial Data Breach — Payment Card Compromise

**Subject: Important Security Notice — Your Payment Information May Have Been Affected**

Dear [Data Subject Name],

We are writing to inform you of a security incident that may have affected your personal and payment information held by Stellar Payments Group.

**What happened:** On 13 March 2026, we detected unauthorized access to our payment processing database. Our investigation determined that an external attacker gained access to a subset of customer payment records between 10 March and 13 March 2026.

**What information was involved:** Your name, email address, billing address, and payment card details (card number, expiry date, and CVV) associated with your Stellar Payments account were among the records accessed.

**What we are doing:**
- We immediately isolated the affected system and engaged Mandiant, a leading cybersecurity firm, to conduct a full forensic investigation.
- We have notified the relevant payment card networks (Visa and Mastercard) and they are monitoring for fraudulent activity on affected card numbers.
- We have reported this incident to the Berliner Beauftragte für Datenschutz und Informationsfreiheit as required by law.

**What you can do:**
- Contact your bank or card issuer immediately and request a replacement card. Do not wait for signs of fraud.
- Review your bank and card statements for any transactions you do not recognize.
- Be cautious of unsolicited emails, calls, or texts claiming to be from Stellar Payments or your bank — we will never ask for your password or full card number.
- Consider placing a fraud alert with a credit reference agency (SCHUFA in Germany, Experian/Equifax in other jurisdictions).

**Free credit monitoring:** We are offering all affected customers 12 months of complimentary credit monitoring through Experian IdentityWorks. To enroll, visit stellarpayments.eu/breach-support and use activation code SPG-2026-PROTECT. Enrollment is available until 30 June 2026.

**Contact us:** If you have questions, our dedicated breach response team is available at:
- Email: breach-support@stellarpayments.eu
- Phone: +49 30 7742 9000 (Monday-Friday, 08:00-20:00 CET; Saturday 09:00-17:00 CET)
- Post: Stellar Payments Group, Data Breach Response Team, Friedrichstraße 191, 10117 Berlin, Germany

Our Data Protection Officer, Dr. Elena Vasquez, can be reached at dpo@stellarpayments.eu or +49 30 7742 8001.

We sincerely regret this incident and are committed to preventing any recurrence.

Regards,
Marcus Lindqvist
Chief Executive Officer
Stellar Payments Group

---

### Scenario 2: Health Data Breach — Unauthorized Access to Medical Records

**Subject: Important Notice Regarding Your Health Information**

Dear [Data Subject Name],

We are contacting you to inform you of a security incident involving your health information held by Stellar Payments Group's employee wellness programme.

**What happened:** On 5 March 2026, we discovered that an employee in our IT department accessed the occupational health database without authorization between 1 February and 4 March 2026. This database contains health screening results and sick leave records for employees enrolled in our wellness programme.

**What information was involved:** Your name, employee number, date of birth, health screening results (including blood pressure, cholesterol, and BMI readings), and sick leave history for 2025-2026.

**What we are doing:**
- The employee responsible has been suspended pending a disciplinary investigation. Their system access has been revoked.
- We have implemented additional access controls on the occupational health database, including role-based access with multi-factor authentication.
- An audit of all database access logs for the past 12 months has been completed.
- We have notified the Berliner Beauftragte für Datenschutz und Informationsfreiheit.

**What you can do:**
- If you have concerns about how your health information may be used, contact our DPO for advice.
- You have the right to request a copy of the access logs relating to your health records under your right of access (Art. 15 GDPR).
- If you experience any adverse consequences that you believe are related to this incident, please contact us immediately.

**Counselling support:** We have arranged confidential counselling support through our Employee Assistance Programme (EAP) provider, Workplace Options, available 24/7 at +49 800 100 0287 (reference: SPG-Health-2026).

**Contact us:**
- DPO: Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001
- HR Confidential Line: hr-confidential@stellarpayments.eu, +49 30 7742 7500

Regards,
Dr. Elena Vasquez
Data Protection Officer
Stellar Payments Group

---

### Scenario 3: Credential Breach — Username and Password Exposure

**Subject: Action Required — Your Stellar Payments Account Credentials May Be Compromised**

Dear [Data Subject Name],

We are writing to inform you that your Stellar Payments account login credentials may have been exposed in a security incident.

**What happened:** On 20 March 2026, our security monitoring systems detected that a database backup file containing customer account credentials was inadvertently stored on an unsecured cloud storage instance between 15 March and 20 March 2026.

**What information was involved:** Your email address, username, and hashed password for your Stellar Payments account. While passwords were stored in a hashed format (bcrypt with a cost factor of 12), we are treating this as a high-risk breach because sophisticated attackers may attempt to reverse the hashes.

**What we are doing:**
- We have secured the cloud storage instance and deleted the exposed backup file.
- All affected account passwords have been force-reset as a precaution.
- We are implementing automated scanning to prevent sensitive data from being stored in unsecured cloud environments.

**What you must do immediately:**
1. You will be prompted to create a new password when you next log in to stellarpayments.eu. Choose a strong, unique password that you do not use for any other service.
2. Enable two-factor authentication (2FA) on your account by going to Settings > Security > Enable 2FA.
3. If you used the same password on any other website or service, change those passwords immediately.
4. Be alert for phishing emails that may reference this incident and attempt to trick you into providing information.

**Contact us:**
- Email: breach-support@stellarpayments.eu
- Phone: +49 30 7742 9000
- DPO: Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001

Regards,
Thomas Brenner
Chief Information Security Officer
Stellar Payments Group

---

### Scenario 4: Ransomware — Temporary Data Unavailability

**Subject: Service Disruption Notice — Your Data Was Temporarily Unavailable**

Dear [Data Subject Name],

We are writing to inform you of a security incident that temporarily affected access to your account data.

**What happened:** On 13 March 2026, Stellar Payments Group experienced a ransomware attack that encrypted portions of our customer database. This made your account data temporarily unavailable for approximately 36 hours while we restored systems from secure backups.

**What information was affected:** Your account data (name, contact details, transaction history, and account balance) was rendered inaccessible during the incident. Our forensic investigation has confirmed that no data was exfiltrated (copied or stolen) during the attack. The data was encrypted in place and has been fully restored.

**What we are doing:**
- We restored all affected data from verified clean backups taken before the attack.
- We have engaged Mandiant to conduct a comprehensive forensic investigation.
- We are implementing enhanced network segmentation and endpoint protection.
- We have reported this incident to the supervisory authority.

**What you should do:**
- Verify that your recent transactions and account balance are correct by logging into your account at stellarpayments.eu.
- If you notice any discrepancies, contact our support team immediately.
- As a precaution, we recommend changing your account password.

**Contact us:**
- Customer Support: support@stellarpayments.eu, +49 30 7742 5000
- DPO: Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001

Regards,
Marcus Lindqvist
Chief Executive Officer
Stellar Payments Group

---

### Scenario 5: Insider Threat — Employee Data Exfiltration

**Subject: Important Notice Regarding Your Employment Records**

Dear [Data Subject Name],

We are writing to inform you of a security incident involving your employment records held by Stellar Payments Group.

**What happened:** On 1 March 2026, our data loss prevention system detected that a departing employee in the People Operations department transferred a file containing employee records to a personal cloud storage account on 27 February 2026. We immediately launched an investigation and recovered the data.

**What information was involved:** Your name, employee number, home address, personal email address, date of birth, salary information, bank account details for payroll, and national insurance/social security number.

**What we are doing:**
- We obtained a court order requiring the former employee to delete all copies of the data and provide a sworn declaration of deletion.
- Forensic examination of the former employee's personal devices confirmed deletion of all copies.
- We have implemented enhanced DLP controls preventing bulk export of employee records.
- We have added behavioral analytics monitoring for all users with access to HR systems.
- We have reported this incident to the Berliner Beauftragte für Datenschutz und Informationsfreiheit and notified law enforcement (Landeskriminalamt Berlin, case reference LKA-2026-04872).

**What you can do:**
- Monitor your bank account for any unauthorized transactions.
- Consider placing a SCHUFA fraud alert by contacting SCHUFA at +49 611 9278 0 or visiting meineschufa.de.
- Be cautious of unsolicited contact from recruiters or other organizations that reference specific details of your employment at Stellar Payments.
- Report any suspicious activity to our security team at security@stellarpayments.eu.

**Free identity protection:** We are providing all affected employees with 24 months of complimentary identity theft protection through Experian IdentityWorks, including dark web monitoring, credit monitoring, and EUR 25,000 identity theft insurance. Enrollment details are available on the HR portal under Benefits > Breach Support, or contact hr-confidential@stellarpayments.eu.

**Contact us:**
- HR Confidential: hr-confidential@stellarpayments.eu, +49 30 7742 7500
- DPO: Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001
- Employee Assistance Programme: +49 800 100 0287 (24/7)

Regards,
Dr. Elena Vasquez
Data Protection Officer
Stellar Payments Group
