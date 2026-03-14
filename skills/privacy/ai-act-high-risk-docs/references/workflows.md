# EU AI Act High-Risk Documentation — Workflows

## Workflow 1: High-Risk Classification Assessment

### Trigger
- New AI system development initiated
- Existing AI system scope or use case changed
- Regulatory update to Annex III categories

### Steps
1. **System Description**: Document the AI system's intended purpose, target users, and deployment context
2. **Annex III Check**: Evaluate against each Annex III category (biometric, critical infrastructure, employment, essential services, law enforcement, migration, justice, democratic processes)
3. **Annex I Check**: Determine if the system is a safety component of a product under Union harmonisation legislation
4. **Art. 6(3) Exception**: Assess whether the narrow exception applies (profiling, preparatory tasks, pattern detection without human replacement)
5. **GPAI Assessment**: For foundation models, evaluate general-purpose AI obligations under Art. 51-52
6. **Classification Decision**: Document classification with legal reasoning
7. **Legal Review**: External legal counsel validates classification
8. **Board Notification**: Inform executive team of classification and compliance obligations

### Output
- AI System Classification Record
- Compliance obligation matrix
- Timeline to compliance (before 2 August 2026)

## Workflow 2: Technical Documentation Preparation (Annex IV)

### Steps
1. **General Description**: Draft system description, intended purpose, hardware/software requirements
2. **System Elements**: Document model architecture, training methodology, computational resources
3. **Training Data**: Document data sources, collection methods, quality measures, bias examination
4. **Validation and Testing**: Compile test metrics, validation datasets, performance benchmarks
5. **Risk Management**: Reference Art. 9 risk management system outputs
6. **Human Oversight**: Document Art. 14 compliance measures
7. **Monitoring Measures**: Document accuracy monitoring, drift detection, retraining triggers
8. **Cybersecurity**: Document Art. 15 robustness and security measures
9. **Internal Review**: Privacy Engineer + ML Engineer + Legal review cycle
10. **Version Control**: Store documentation with version history in compliance repository

### Output
- Complete Annex IV technical documentation package
- Document version register

## Workflow 3: Conformity Assessment

### Steps
1. **Quality Management System**: Verify Art. 17 QMS is established and documented
2. **Technical Documentation**: Confirm Annex IV documentation is complete and current
3. **Assessment Path**: Determine internal (Art. 43(2)) vs third-party (Art. 43(1)) assessment
4. **Internal Assessment**: For non-biometric Annex III systems, conduct internal verification against each Art. 8 requirement
5. **Third-Party Assessment**: For biometric systems in Annex III para. 1, engage notified body
6. **Declaration of Conformity**: Draft EU Declaration of Conformity per Art. 47
7. **CE Marking**: Affix CE marking per Art. 48
8. **EU Database Registration**: Register system in EU AI database per Art. 49
9. **Post-Market Setup**: Establish Art. 72 post-market monitoring system

### Output
- Conformity assessment report
- EU Declaration of Conformity
- EU database registration confirmation

## Workflow 4: Post-Market Monitoring (Art. 72)

### Steps
1. **Metric Collection**: Deploy continuous performance, bias, and accuracy monitoring
2. **Drift Detection**: Automated alerts for data drift and model performance degradation
3. **Incident Logging**: Record all incidents, near-misses, and user complaints
4. **Serious Incident Reporting**: Report to market surveillance authority within 15 days (Art. 73)
5. **Quarterly Review**: Update risk register and technical documentation
6. **Corrective Action**: Implement corrections for identified issues
7. **Documentation Update**: Maintain technical documentation current with system changes
