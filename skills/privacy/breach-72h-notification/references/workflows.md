# GDPR 72-Hour Breach Notification Workflow

## Phase 1: Breach Discovery and Initial Triage (Hour 0-4)

1. **Incident detection**: Security Operations Center (SOC) analyst identifies a potential data breach through SIEM alert, DLP trigger, user report, or third-party notification.
2. **Initial classification**: SOC lead determines within 30 minutes whether the incident involves personal data. If no personal data is involved, route to standard incident response — breach notification procedures do not apply.
3. **Breach confirmation**: Technical investigation team confirms whether personal data has been compromised (unauthorized access, disclosure, alteration, or destruction).
4. **Clock activation**: Record the exact UTC timestamp when the controller has reasonable certainty that a personal data breach has occurred. This is T=0 for the 72-hour deadline.
5. **Immediate escalation**: Notify the DPO (Dr. Elena Vasquez, dpo@stellarpayments.eu, +49 30 7742 8001) and the Incident Commander within 1 hour of clock activation.

## Phase 2: Rapid Assessment (Hour 4-12)

1. **Scope determination**: Identify affected systems, databases, and data repositories.
2. **Data subject count estimation**: Query affected systems to determine the approximate number of data subjects impacted. Document the methodology used for estimation.
3. **Data category identification**: Classify the personal data involved — names, email addresses, financial data, health data, government identifiers, authentication credentials, location data.
4. **Special category check**: Determine if Art. 9 special category data (racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic data, biometric data, health data, sex life/orientation) or Art. 10 criminal conviction data is involved.
5. **Recipient/accessor identification**: Determine who accessed the data — external attacker, insider, authorized but inappropriate recipient, public exposure.
6. **Containment status**: Confirm whether the breach is contained or ongoing. Document containment measures taken.

## Phase 3: Risk Assessment and Notification Decision (Hour 12-24)

1. **Apply the EDPB risk assessment matrix**: Score each factor (data sensitivity, volume, identifiability, consequences, vulnerable subjects, controller-specific factors) on the 1-4 scale.
2. **Calculate aggregate risk score**: Sum all factor scores. If 6 or below — document in breach register, no supervisory authority notification required. If 7 or above — proceed to notification preparation.
3. **Art. 34 assessment**: If aggregate score is 16 or above, or if the breach clearly meets the "high risk" threshold, initiate parallel data subject notification planning.
4. **DPO sign-off**: DPO reviews the risk assessment and notification decision. The DPO's recommendation is documented even if management decides differently (in which case, the divergence is also recorded).
5. **Legal review**: In-house legal counsel reviews the notification for accuracy, legal privilege considerations, and potential law enforcement coordination needs.

## Phase 4: Notification Preparation (Hour 24-48)

1. **Complete the supervisory authority notification form**: Populate all Art. 33(3)(a)-(d) fields using the information gathered in Phases 2-3.
2. **Identify the competent supervisory authority**: Determine the lead supervisory authority based on the controller's main establishment under Art. 55/56. For Stellar Payments Group with main establishment in Germany, the lead authority is BfDI or the relevant Landesdatenschutzbehörde (Berliner Beauftragte für Datenschutz und Informationsfreiheit).
3. **Multi-jurisdiction assessment**: If the breach affects data subjects in multiple EU member states, determine if notifications to additional supervisory authorities are needed under the one-stop-shop mechanism or if direct notification is required.
4. **Prepare supporting documentation**: Compile the breach timeline, forensic evidence summary, containment actions log, and risk assessment worksheet.
5. **Draft phased notification language** (if applicable): If investigation is ongoing and not all information is available, prepare Art. 33(4) phased notification language explaining what information will follow and why.

## Phase 5: Submission (Hour 48-72)

1. **Final review**: DPO and legal counsel conduct final review of notification content.
2. **Submit notification**: File the notification through the appropriate supervisory authority channel (online portal, PEC email, or postal submission depending on the authority's requirements).
3. **Confirmation receipt**: Obtain and archive the submission confirmation, reference number, and timestamp.
4. **Internal distribution**: Distribute a copy of the submitted notification to the Incident Commander, Chief Information Security Officer, General Counsel, and Chief Executive Officer.
5. **Breach register entry**: Create or update the Art. 33(5) breach register entry with notification details, submission timestamp, and authority reference number.

## Phase 6: Post-Notification Follow-Up (Hour 72+)

1. **Supplementary notifications**: Submit any outstanding information identified in the initial phased notification within 14 calendar days or as soon as available.
2. **Authority engagement**: Monitor for and respond promptly to any inquiries from the supervisory authority. Assign a single point of contact (DPO or delegate) for all authority communications.
3. **Data subject notification**: If Art. 34 notification is required, execute the data subject communication plan within 7 calendar days of supervisory authority notification.
4. **Remediation tracking**: Monitor implementation of all corrective measures committed to in the notification.
5. **Lessons learned**: Conduct a post-incident review within 30 calendar days and update the breach response procedure as needed.
6. **Board reporting**: Include the breach and response in the next scheduled DPO report to the board.

## Escalation Matrix

| Condition | Escalation Target | Response Time |
|-----------|------------------|---------------|
| Breach confirmed involving personal data | DPO + Incident Commander | Within 1 hour |
| Special category data (Art. 9) involved | DPO + General Counsel + CEO | Within 2 hours |
| More than 10,000 data subjects affected | DPO + CEO + Board Chair | Within 4 hours |
| Law enforcement involvement needed | General Counsel + CISO + External Counsel | Within 4 hours |
| Media inquiry received before notification | Communications Director + CEO + DPO | Immediately |
| 72-hour deadline at risk of being missed | DPO + General Counsel + CEO | 12 hours before deadline |

## Documentation Checklist

- [ ] Breach discovery timestamp (UTC)
- [ ] Clock activation timestamp (UTC)
- [ ] 72-hour deadline timestamp (UTC)
- [ ] Breach type classification (confidentiality/integrity/availability)
- [ ] Affected systems inventory
- [ ] Data subject count and categories
- [ ] Personal data categories compromised
- [ ] Special category data flag (yes/no)
- [ ] Risk assessment score and worksheet
- [ ] Notification decision and DPO recommendation
- [ ] Containment measures implemented
- [ ] Supervisory authority notification submission timestamp
- [ ] Authority reference number
- [ ] Phased notification schedule (if applicable)
- [ ] Art. 34 data subject notification decision
- [ ] Remediation action plan
