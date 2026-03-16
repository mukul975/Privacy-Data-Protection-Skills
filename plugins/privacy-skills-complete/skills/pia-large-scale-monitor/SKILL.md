---
name: pia-large-scale-monitor
description: >-
  Conducts Privacy Impact Assessment for large-scale systematic monitoring
  under GDPR Article 35(3)(c). Covers CCTV and video surveillance, employee
  monitoring, location tracking, internet monitoring, and behavioural analytics.
  Applies EDPB WP248rev.01 criteria for systematic monitoring of publicly
  accessible areas. Keywords: DPIA, large-scale monitoring, CCTV, employee
  monitoring, systematic monitoring, surveillance, location tracking.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "dpia, large-scale-monitoring, cctv, employee-monitoring, systematic-monitoring"
---

# Privacy Impact Assessment for Large-Scale Monitoring

## Overview

GDPR Article 35(3)(c) mandates a DPIA for systematic monitoring of a publicly accessible area on a large scale. The EDPB in WP248rev.01 identifies systematic monitoring as criterion C3, which often combines with other criteria (large scale C4, vulnerable data subjects C7, innovative technology C8) to trigger mandatory DPIA. This skill covers PIA methodology for CCTV/video surveillance, employee monitoring, location tracking, internet/communications monitoring, and behavioural analytics systems.

## Regulatory Framework

### GDPR Requirements

| Provision | Relevance to Large-Scale Monitoring |
|-----------|-------------------------------------|
| Art. 35(3)(c) | Mandatory DPIA for systematic monitoring of publicly accessible area on a large scale |
| Art. 35(1) | DPIA required when processing is likely to result in a high risk to rights and freedoms |
| Art. 6(1)(f) | Legitimate interests as typical lawful basis for monitoring; requires balancing test |
| Art. 5(1)(c) | Data minimisation: collect only what is necessary for the monitoring purpose |
| Art. 5(1)(e) | Storage limitation: retain monitoring data only as long as necessary |
| Art. 12-14 | Transparency obligations: informing data subjects about monitoring |
| Art. 21 | Right to object to processing based on legitimate interests |
| Art. 22 | Automated decision-making restrictions applicable to behavioural analytics |

### EDPB and National Authority Guidance

- **EDPB Guidelines 3/2019 on Video Devices**: Comprehensive guidance on CCTV use, including legal basis, transparency, retention, and access rights for video surveillance.
- **EDPB WP248rev.01 Annex**: National supervisory authority blacklists frequently include large-scale monitoring activities as mandatory DPIA triggers.
- **ICO Employment Practices Code**: UK guidance on workplace monitoring including CCTV, email, internet, and vehicle tracking.
- **CNIL Guidance on Employee Monitoring (2023)**: French DPA requirements for workplace surveillance including keystroke logging, screen capture, and video monitoring.

## Monitoring Scenarios

### 1. CCTV and Video Surveillance

**Scope**: Fixed and mobile cameras in public spaces, retail premises, transport hubs, workplaces.
**Key risks**: Mass surveillance of individuals in publicly accessible areas; facial recognition enabling biometric identification; disproportionate retention creating behavioural profiles; function creep from security to performance monitoring.
**EDPB Guidelines 3/2019 requirements**:
- Legitimate interest must be documented with a concrete, real, and present threat (not hypothetical security concerns).
- Signs must be placed at a reasonable distance indicating the area is under surveillance, the controller identity, the purpose, and where to find the full privacy notice.
- Retention should generally not exceed 72 hours unless justified by a specific incident.
- Facial recognition in public spaces requires explicit consent or substantial public interest legal basis.

### 2. Employee Monitoring

**Scope**: Email monitoring, internet usage logging, keystroke logging, screen recording, GPS tracking of company vehicles, badge access tracking.
**Key risks**: Chilling effect on employee behaviour and communications; disproportionate intrusion into private life at work; monitoring of protected activities (trade union, whistleblowing); covert monitoring without transparency.
**Legal constraints**:
- ECHR Article 8 (right to respect for private life) applies even in the workplace (Barbulescu v Romania, Grand Chamber, 2017).
- Employers must demonstrate monitoring is necessary, proportionate, and transparent.
- Works council or employee representative consultation may be required (varies by jurisdiction).
- Covert monitoring is permissible only in exceptional circumstances where there is reasonable suspicion of criminal activity or gross misconduct (Lopez Ribalda v Spain, Grand Chamber, 2019).

### 3. Location Tracking

**Scope**: GPS vehicle tracking, mobile device tracking, Wi-Fi positioning, Bluetooth beacons.
**Key risks**: Continuous tracking creating comprehensive movement profiles; tracking extending beyond working hours; combination with other data revealing private activities; disproportionate monitoring intensity.
**Mitigation**: Disable tracking outside working hours; use geofencing rather than continuous tracking; inform employees and obtain consent where required; provide option for personal use of vehicles with tracking disabled.

### 4. Internet and Communications Monitoring

**Scope**: Web browsing logs, email content scanning, instant messaging monitoring, social media monitoring.
**Key risks**: Interception of private communications; monitoring of legally privileged communications; chilling effect on freedom of expression; access to special category data through content analysis.
**Legal constraints**: ePrivacy Directive Article 5 (confidentiality of communications); national interception laws (e.g., UK Regulation of Investigatory Powers Act 2000, Investigatory Powers Act 2016).

### 5. Behavioural Analytics

**Scope**: Customer behaviour tracking in retail (heat mapping, dwell time), website analytics, social media sentiment analysis, predictive analytics for security.
**Key risks**: Profiling without awareness; automated decision-making affecting individuals; combining data from multiple sources to create comprehensive profiles; targeting vulnerable individuals.

## DPIA Methodology for Large-Scale Monitoring

### Phase 1: Monitoring Scope Definition (Week 1)

1. Document the monitoring system: technology used, coverage area, data collected, retention period.
2. Define the monitoring purpose precisely (security, safety, performance management, compliance, loss prevention).
3. Identify all data subjects affected: employees, customers, visitors, bystanders, delivery personnel.
4. Quantify the scale: number of individuals monitored, geographic coverage, hours of operation, data volume.
5. Map data flows from collection through storage, access, analysis, and deletion.

### Phase 2: Necessity and Proportionality Assessment (Week 2)

1. Document the specific threat or business need justifying monitoring.
2. Assess whether the purpose can be achieved without monitoring or with less intrusive monitoring.
3. Evaluate alternative measures: physical security, access controls, procedural safeguards.
4. Apply the EDPB balancing test: controller's legitimate interests vs data subject's rights, freedoms, and reasonable expectations.
5. Consider temporal proportionality: is 24/7 monitoring necessary or would specific hours suffice?
6. Consider spatial proportionality: can monitoring be limited to specific high-risk areas?

### Phase 3: Data Subject Impact Assessment (Week 3)

1. Assess impact on each data subject category (employees vs public vs visitors).
2. Evaluate the reasonable expectations of data subjects in the monitored environment.
3. Identify vulnerable groups affected (children, patients, job applicants).
4. Assess the chilling effect on behaviour, communication, and freedom of movement.
5. Document ECHR Article 8 balancing analysis for employee monitoring.

### Phase 4: Technical and Organisational Safeguards (Week 4)

1. Define access controls: who can view monitoring data, under what circumstances, with what authorisation.
2. Set retention periods: default deletion schedule, exception process for incident-related retention.
3. Implement transparency measures: signage, privacy notices, employee policies.
4. Configure data protection by design: privacy masking, resolution reduction, automated deletion, purpose-bound access.
5. Establish oversight: DPO review, audit schedule, complaint mechanism.

### Phase 5: Documentation and Approval (Week 5)

1. Document the DPIA per Art. 35(7) requirements.
2. Record the DPO advice and whether it was followed.
3. Obtain management sign-off with clear accountability for proportionality decisions.
4. If residual risk remains high, initiate Art. 36 prior consultation with supervisory authority.
5. Schedule periodic review (minimum annually; sooner if monitoring scope or technology changes).

## Enforcement Precedents

- **Greek DPA vs Municipality of Thessaloniki (2020)**: EUR 15,000 fine for CCTV monitoring in public spaces without DPIA and without adequate transparency measures (signage inadequate, no privacy notice accessible).
- **Spanish AEPD vs Mercadona (2021)**: EUR 2.52 million fine for deploying facial recognition technology in supermarkets without adequate DPIA, proportionality assessment, or lawful basis.
- **Belgian DPA vs Brussels Airport (2020)**: Reprimand for thermal camera surveillance during COVID-19 without DPIA for the new processing purpose.
- **ICO vs Clearview AI (2022)**: GBP 7.5 million fine for processing biometric data of UK residents through facial recognition surveillance technology without lawful basis, transparency, or DPIA.
- **CNIL vs Amazon France Logistique (2024)**: EUR 32 million fine for excessively intrusive employee monitoring system (scanner-based activity tracking with multiple indicators) violating proportionality and data minimisation principles.
- **Romanian DPA vs Raiffeisen Bank (2020)**: EUR 150,000 fine for GPS tracking of employee vehicles without DPIA and extending beyond working hours.
