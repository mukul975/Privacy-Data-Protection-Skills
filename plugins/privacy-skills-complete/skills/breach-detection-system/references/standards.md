# Standards and Regulatory References — Breach Detection System

## Primary Legislation

### GDPR Article 32 — Security of Processing
- **Art. 32(1)**: The controller and the processor shall implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk, including: (a) pseudonymisation and encryption; (b) ongoing confidentiality, integrity, availability and resilience; (c) ability to restore availability and access to personal data in a timely manner; (d) a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures.
- **Art. 32(2)**: In assessing the appropriate level of security, account shall be taken in particular of the risks that are presented by processing, in particular from accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data.

### GDPR Article 33(1) — Implicit Detection Obligation
- While Art. 33 does not explicitly mandate breach detection technology, the 72-hour notification window creates a de facto obligation to detect breaches promptly. A controller that takes months to discover a breach faces enforcement action both for the late notification and for the inadequate security measures that failed to detect the breach.

### GDPR Recital 87 — Timely Detection
- "It should be ascertained whether all appropriate technological protection and organisational measures have been implemented to establish immediately whether a personal data breach has taken place."

## Regulatory Guidance

### EDPB Guidelines 9/2022 — Detection and Awareness
- Section 2.3: Controllers should implement measures to detect breaches rapidly, including monitoring systems, staff training, and clear reporting channels.
- The EDPB expects controllers to have "appropriate measures in place to detect a breach in a timely manner."

### ENISA — Guidelines on Breach Notification (2023)
- Recommends implementing SIEM, IDS/IPS, DLP, and behavioral analytics as minimum detection capabilities for organizations processing personal data at scale.
- Provides a maturity model for breach detection ranging from Level 1 (manual, reactive) to Level 5 (automated, predictive).

### NIST Cybersecurity Framework 2.0 (February 2024)
- **DE.CM (Detect — Continuous Monitoring)**: Networks and network services are monitored to find potentially adverse events.
- **DE.AE (Detect — Adverse Event Analysis)**: Anomalies, indicators of compromise, and other potentially adverse events are analyzed.

### NIST SP 800-61r3 — Computer Security Incident Handling Guide (2024)
- Provides incident detection and analysis methodology including: signs of an incident (precursors and indicators), sources of precursors and indicators, and incident analysis guidelines.

## Enforcement Precedents

- **ICO (UK) — British Airways (2020)**: GBP 20 million fine. The ICO specifically cited inadequate monitoring and detection capabilities: "BA ought to have identified weaknesses in its security arrangements and resolved them with measures that were available at the time."
- **ICO (UK) — Marriott International (2020)**: GBP 18.4 million fine. The breach went undetected for approximately four years (2014-2018). The ICO found that Marriott "failed to put appropriate technical and organisational measures in place to protect the personal data being processed on its systems."
- **CNIL (France) — Criteo (2023)**: EUR 40 million fine. Among other violations, inadequate monitoring of data access and processing activities.

## Industry Standards

- **PCI DSS v4.0** — Requirement 10: Log and Monitor All Access to System Components and Cardholder Data. Requirement 11: Test Security of Systems and Networks Regularly. Directly applicable to Stellar Payments Group as a payment processor.
- **ISO/IEC 27001:2022** — Annex A Control 8.15 (Logging), 8.16 (Monitoring activities). Requires that networks, systems, and applications are monitored for anomalous behavior and appropriate actions taken.
- **ISO/IEC 27701:2019** — Section 6.9.4.1: Requires logging and monitoring of events that could affect the security of personal data.
- **SOC 2 Type II** — CC7.2 (Monitoring): The entity monitors system components and the operation of those components for anomalies that are indicative of malicious acts, natural disasters, and errors affecting the entity's ability to meet its objectives.
