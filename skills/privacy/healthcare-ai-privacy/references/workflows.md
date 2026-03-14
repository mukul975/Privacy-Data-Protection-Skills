# Healthcare AI Privacy — Workflows

## Workflow 1: AI Training Data PHI Governance

```
AI Model Development — Training Data Request
│
├── Step 1: Purpose and Lawful Basis
│   ├── Is the AI model for treatment, payment, or healthcare operations?
│   │   ├── Treatment CDS → TPO basis (§164.506); minimum necessary applies
│   │   ├── Quality improvement → Healthcare operations (§164.501)
│   │   └── Research → IRB/Privacy Board waiver (§164.512(i)) or authorization
│   │
│   └── Document lawful basis for PHI use in AI training
│
├── Step 2: Data Minimization Assessment
│   ├── Can the model be trained on de-identified data?
│   │   ├── YES → Apply safe harbor or expert determination
│   │   │         If de-identified, HIPAA no longer applies to training data
│   │   │         BUT: assess model memorization risk (de-identification may be undermined)
│   │   └── NO → Justify why identifiable PHI is required
│   │
│   ├── Can synthetic data achieve acceptable model performance?
│   │   ├── YES → Use synthetic data to reduce PHI exposure
│   │   └── NO → Document synthetic data evaluation results
│   │
│   └── Minimum necessary: request only data elements essential for model performance
│
├── Step 3: Security Controls for AI Training Environment
│   ├── Encrypted storage for training data (AES-256)
│   ├── Access-controlled compute environment (role-based)
│   ├── Audit logging of all data access
│   ├── Network isolation of training infrastructure
│   ├── Data retention: delete training data copies within 90 days of model finalization
│   └── Differential privacy during training if applicable (calibrate epsilon)
│
├── Step 4: Pre-Deployment Privacy Testing
│   ├── Membership inference attack testing
│   ├── Training data extraction testing (especially for generative models)
│   ├── Model inversion attack testing
│   ├── Attribute inference testing
│   └── If leakage detected: retrain with privacy-preserving techniques or additional safeguards
│
└── Step 5: Approval and Documentation
    ├── AI Data Governance Committee approval
    ├── Privacy Officer sign-off
    ├── Model card created with privacy section
    └── Data provenance documentation retained
```

## Workflow 2: Healthcare AI Deployment Privacy Review

```
AI System Ready for Clinical Deployment
│
├── Step 1: Regulatory Classification
│   ├── Is this a medical device (SaMD)?
│   │   ├── Does it process medical images/signals? → Likely SaMD (FDA regulated)
│   │   ├── Does it make autonomous decisions? → Likely SaMD
│   │   ├── Does it meet all 4 Cures Act CDS exemption criteria? → May be exempt
│   │   └── Document classification determination
│   │
│   ├── Is this high-risk under AI Act?
│   │   ├── Is it an AI-based medical device? → High-risk (Annex III)
│   │   └── Document AI Act classification
│   │
│   └── Does it process EU patient data? → GDPR + AI Act apply
│
├── Step 2: Privacy Impact Assessment
│   ├── What PHI does the system process at inference time?
│   ├── Who has access to AI outputs? (care team, patient, insurer)
│   ├── Are AI outputs stored in the medical record?
│   ├── Does the system communicate with external services (cloud API)?
│   │   └── If yes: BAA required with AI service provider
│   ├── Can the system reveal sensitive information not provided as input?
│   └── Document all privacy risks and mitigations
│
├── Step 3: Transparency and Disclosure
│   ├── Update Notice of Privacy Practices if AI use not covered
│   ├── Label AI-generated content in the medical record
│   ├── Create patient-facing explanation of AI system
│   ├── Prepare clinician documentation (model card, limitations, failure modes)
│   └── Configure audit trail for all AI decisions
│
├── Step 4: Human Oversight Configuration
│   ├── Define which decisions require physician review
│   ├── Implement override capability
│   ├── Configure automation bias safeguards
│   └── Document human oversight protocol
│
└── Step 5: Go-Live Approval
    ├── Privacy Officer approval
    ├── CISO security clearance
    ├── Clinical leadership approval
    ├── AI Ethics Committee review complete
    └── Post-deployment monitoring plan in place
```

## Workflow 3: AI Bias Monitoring

```
Post-Deployment AI Bias Monitoring (Ongoing)
│
├── Monthly Automated Monitoring
│   ├── Extract model predictions disaggregated by:
│   │   age, sex, race/ethnicity, primary language, insurance type
│   ├── Calculate performance metrics per subgroup:
│   │   sensitivity, specificity, PPV, NPV, AUC, calibration
│   ├── Compare subgroup metrics to overall population
│   ├── Flag if any subgroup metric < 80% of best-performing group
│   └── Generate automated monitoring report
│
├── Quarterly Clinical Outcome Correlation
│   ├── Correlate AI recommendations with actual patient outcomes
│   ├── Analyze outcome disparities across demographic groups
│   ├── Review clinician override patterns by patient demographics
│   └── Report to AI Ethics Committee
│
├── Annual Comprehensive Audit
│   ├── Independent third-party bias audit
│   ├── Review training data representativeness vs current population
│   ├── Assess model drift and performance degradation
│   ├── Review fairness metrics against regulatory requirements
│   │   (ACA §1557, AI Act Art. 10 data governance)
│   └── Publish audit results (internal or external as required)
│
└── Triggered Reviews
    ├── Patient complaint about AI-assisted care
    ├── Clinician report of AI error or bias
    ├── Regulatory inquiry or guidance update
    └── Significant demographic shift in patient population
```
