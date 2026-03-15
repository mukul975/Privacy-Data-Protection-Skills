---
name: new-tech-pia
description: >-
  Guides privacy impact assessment for emerging technologies including IoT,
  blockchain, AR/VR, quantum computing, and digital twins. Covers risk
  identification methodology, proportionality assessment, and technology-specific
  privacy challenges. Activate when evaluating new technology adoption,
  innovation projects, or emerging tech procurement. Keywords: PIA, emerging
  technology, IoT, blockchain, AR/VR, quantum computing, digital twins,
  innovation privacy.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: privacy-impact-assessment
  tags: "pia, emerging-technology, iot, blockchain, ar-vr, quantum-computing"
---

# Assessing New Technology Privacy Impact

## Overview

Article 35(1) of the GDPR explicitly references new technologies as a factor increasing the likelihood of high risk to data subjects' rights and freedoms. The EDPB in WP248rev.01 identifies innovative use of technology as one of nine criteria triggering a DPIA. This skill provides a structured PIA methodology for emerging technologies where the privacy implications are not yet fully understood, including Internet of Things (IoT), blockchain and distributed ledger technologies, augmented and virtual reality (AR/VR), quantum computing, digital twins, brain-computer interfaces, and ambient computing.

## Technology-Specific Privacy Risk Profiles

### Internet of Things (IoT)

| Risk Area | Description | Privacy Impact |
|-----------|-------------|---------------|
| Pervasive data collection | IoT devices continuously collect environmental and behavioural data, often without visible indicators | Data subjects may be unaware of the scope of data collection; transparency obligations under Art. 13-14 are difficult to fulfil on devices without screens |
| Data minimisation challenges | Sensors often collect more data than needed for the immediate purpose to enable future analytics | Violation of Art. 5(1)(c) data minimisation; purpose creep through accumulated data |
| Device-to-device communication | IoT ecosystems share data between devices without user awareness | Unexpected recipients; difficulty identifying all processors and sub-processors |
| Insecure by default | Many IoT devices ship with default credentials, unencrypted communications, and no update mechanism | Art. 25 data protection by design and Art. 32 security of processing obligations not met |
| Location and behavioural tracking | Connected devices reveal location patterns, daily routines, and behavioural habits | Systematic monitoring (WP248 C3); profiling risk (WP248 C1) |
| Cross-device correlation | Data from multiple IoT devices can be combined to create comprehensive behavioural profiles | Matching or combining datasets (WP248 C6); disproportionate surveillance |

**EDPB Guidelines 02/2023 on IoT and Wearable Devices**: Emphasized that IoT devices must implement data protection by design, provide clear privacy notices (adapted to device constraints), and enable genuine consent mechanisms.

### Blockchain and Distributed Ledger Technology

| Risk Area | Description | Privacy Impact |
|-----------|-------------|---------------|
| Immutability vs right to erasure | Blockchain's append-only nature conflicts with Art. 17 right to erasure | Technical inability to delete personal data recorded on-chain |
| Transparency of transactions | Public blockchains expose transaction data to all participants | Personal data potentially accessible to unlimited recipients |
| Pseudonymity not anonymity | Blockchain addresses are pseudonymous but can be linked to real identities through transaction analysis | Re-identification risk; Art. 4(5) pseudonymisation does not equal anonymisation |
| Controller identification | Decentralised governance makes it difficult to identify the data controller | Art. 26 joint controller arrangements may be needed; accountability unclear |
| Cross-border by design | Distributed ledger nodes are typically located across multiple jurisdictions | Chapter V international transfer obligations triggered |
| Smart contract automation | Smart contracts execute automatically without human intervention | Art. 22 automated decision-making implications when smart contracts affect individuals |

**CNIL Blockchain Guidance (2018)**: Recommended storing personal data off-chain with only hashes on-chain; using commitment schemes; designating participants who decide to use blockchain as controllers.

### Augmented and Virtual Reality (AR/VR)

| Risk Area | Description | Privacy Impact |
|-----------|-------------|---------------|
| Biometric data collection | Eye tracking, facial expressions, body movements, voice patterns | Art. 9 special category data (biometric data for identification); Art. 35(3)(b) trigger |
| Spatial mapping | AR/VR devices scan and map physical environments including private spaces | Collection of data about third parties present in the environment without their consent |
| Behavioural profiling | Gaze tracking reveals interests, attention patterns, and cognitive state | Highly personal data; evaluation and scoring (WP248 C1) |
| Immersive manipulation | VR environments can influence behaviour through environmental design | Art. 5(1)(a) fairness; potential for subliminal manipulation |
| Persistent identity | Avatar and behavioural biometrics create persistent identifiable profiles | Long-term tracking across virtual environments |
| Child safety | Minors using VR platforms face enhanced risks | Vulnerable data subjects (WP248 C7); Art. 8 child consent requirements |

### Quantum Computing

| Risk Area | Description | Privacy Impact |
|-----------|-------------|---------------|
| Cryptographic vulnerability | Quantum computers may break current encryption standards (RSA, ECC) | Art. 32 security measures based on current encryption become insufficient |
| Retroactive decryption | Encrypted data harvested today can be decrypted when quantum computers mature (harvest now, decrypt later) | Data currently protected may become exposed; long-term confidentiality compromised |
| Enhanced data analytics | Quantum machine learning can process data at scales impossible for classical computers | New forms of profiling and inference; privacy-preserving techniques may be defeated |
| Post-quantum migration | Transitioning to quantum-resistant cryptography requires significant infrastructure changes | Interim vulnerability period during migration |

**ENISA Post-Quantum Cryptography Report (2024)**: Recommended organisations begin quantum risk assessment and plan migration to NIST-standardised post-quantum algorithms (ML-KEM, ML-DSA, SLH-DSA).

### Digital Twins

| Risk Area | Description | Privacy Impact |
|-----------|-------------|---------------|
| Comprehensive data aggregation | Digital twins aggregate data from multiple sources to create a virtual replica | Matching or combining datasets (WP248 C6); comprehensive profiling |
| Predictive modelling of individuals | Digital twins of patients or employees predict future states and behaviours | Evaluation and scoring (WP248 C1); Art. 22 implications for predictions affecting individuals |
| Continuous synchronisation | Real-time data feeds maintain the digital twin's accuracy | Systematic monitoring (WP248 C3); proportionality concerns |
| Blurred anonymisation boundary | Even without direct identifiers, a sufficiently detailed digital twin may be re-identifiable | Pseudonymisation vs anonymisation assessment required |

## PIA Methodology for Emerging Technologies

### Phase 1: Technology Understanding (Week 1)

1. Document the technology's data processing characteristics:
   - What data is collected (categories, volume, frequency)
   - How data flows through the technology stack
   - Where data is stored and processed (geographic locations)
   - Who has access to data at each stage
   - How long data is retained
   - What security measures protect data at each stage
2. Identify the technology's novel risk characteristics that distinguish it from established technologies.
3. Map the technology against the EDPB WP248rev.01 nine criteria.
4. Consult published regulatory guidance specific to the technology (EDPB, CNIL, ICO, ENISA).

### Phase 2: Stakeholder Impact Mapping (Week 2)

1. Identify all affected data subjects:
   - Direct users of the technology
   - Third parties whose data may be incidentally collected
   - Bystanders (particularly relevant for IoT, AR/VR, spatial computing)
2. Identify vulnerable data subjects (children, employees, patients, elderly).
3. Map potential impacts on each stakeholder group:
   - Privacy impacts (loss of control, unexpected processing)
   - Autonomy impacts (manipulation, reduced choice)
   - Equality impacts (discriminatory outcomes, digital exclusion)
   - Safety impacts (physical harm from decisions based on technology)
4. Document data subject expectations versus actual processing.

### Phase 3: Proportionality Assessment (Week 3)

For each data processing element of the technology:

| Assessment Question | Analysis Required |
|--------------------|-------------------|
| Is this processing necessary for the stated purpose? | Document why the technology cannot achieve its purpose without this data |
| Could the purpose be achieved with less data? | Evaluate data minimisation alternatives (aggregation, sampling, synthetic data) |
| Could the purpose be achieved with less identifying data? | Evaluate anonymisation, pseudonymisation, and differential privacy options |
| Could the purpose be achieved with a less invasive technology? | Compare the proposed technology against established alternatives |
| Are the benefits proportionate to the privacy intrusion? | Balancing test: public interest vs individual privacy impact |
| Have data subjects been consulted on the acceptability of the intrusion? | Art. 35(9) data subject views; user acceptance research |

### Phase 4: Risk Assessment and Mitigation (Week 4-5)

1. For each identified risk, assess likelihood and severity using the standard DPIA risk matrix.
2. Identify technology-specific mitigation measures:
   - Privacy-enhancing technologies (PETs): differential privacy, homomorphic encryption, secure multi-party computation, federated learning
   - Data protection by design: privacy-preserving defaults, granular consent, purpose-bound processing
   - Transparency mechanisms adapted to technology constraints (audio notices for screenless IoT, visual indicators for AR/VR)
3. Assess residual risk after mitigation.
4. If residual risk remains high, consider whether the technology should be deployed at all, not just how to mitigate risks.

### Phase 5: Ongoing Monitoring Framework (Week 5-6)

1. Define monitoring metrics specific to the technology:
   - Data collection volumes (detect scope creep)
   - Access patterns (detect unauthorised use)
   - Accuracy and reliability of technology outputs
   - User complaints and feedback
2. Establish review triggers:
   - Technology update or version change
   - New use case or feature added
   - Security vulnerability discovered
   - Regulatory guidance issued for the technology
   - Peer data breach involving similar technology
3. Define a sunset plan: how will personal data be handled if the technology is decommissioned?

## Privacy-by-Design Requirements for Emerging Technologies

| Principle | Implementation for Emerging Tech |
|-----------|--------------------------------|
| Proactive not reactive | Conduct PIA before technology deployment, not after incidents |
| Privacy as default | Technology must ship with privacy-protective defaults; opt-in for additional data collection |
| Privacy embedded in design | Privacy requirements must be part of the technology specification, not bolt-on |
| Full functionality | Privacy protections should not degrade the technology's core functionality |
| End-to-end security | Data protection from collection through deletion, including inter-device communication |
| Visibility and transparency | Clear indicators when technology is collecting data; accessible privacy notices |
| Respect for user privacy | User-centric design; genuine choice and control over personal data |

## Enforcement Precedents

- **Spanish AEPD vs CaixaBank (2021)**: EUR 6 million fine for deploying new profiling technology (behavioural analytics for targeted financial products) without adequate DPIA for innovative technology use.
- **ICO vs Clearview AI (2022)**: GBP 7.5 million fine for novel facial recognition technology scraping public images without lawful basis or DPIA.
- **CNIL vs Amazon Europe (2020)**: EUR 35 million fine for deploying cookie tracking technology without valid consent on the Amazon.fr website.
- **Italian Garante vs Foodinho/Glovo (2021)**: EUR 2.5 million fine for deploying algorithmic management technology (AI-driven shift allocation for riders) without DPIA.
- **Belgian DPA vs IAB Europe (2022)**: EUR 250,000 fine for the Transparency and Consent Framework (TCF) used in programmatic advertising technology; found that TCF constituted processing of personal data without adequate controller designation.
