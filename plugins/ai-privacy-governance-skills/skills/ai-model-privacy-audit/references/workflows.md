# AI Model Privacy Audit Workflows

## Workflow 1: Audit Initiation and Scoping

```
START: AI model requires privacy audit
│
├─ Step 1: Determine audit trigger
│  ├─ Pre-deployment audit (new model before production)
│  ├─ Periodic audit (annual or per DPIA schedule)
│  ├─ Post-retraining audit (model updated with new data)
│  ├─ Incident-triggered audit (suspected privacy breach)
│  └─ Regulatory request (DPA investigation or audit)
│
├─ Step 2: Define scope
│  ├─ Model(s) to audit
│  ├─ Threat model: black-box / grey-box / white-box
│  ├─ Attack categories: extraction / membership / inversion / attribute
│  ├─ Data sensitivity level: general / special category / highly sensitive
│  └─ Regulatory requirements driving the audit
│
├─ Step 3: Assemble audit team
│  ├─ ML security engineer (attack execution)
│  ├─ Privacy engineer (GDPR alignment)
│  ├─ Model owner (technical cooperation)
│  └─ DPO (oversight and reporting)
│
├─ Step 4: Obtain authorisation
│  ├─ Model owner approval for audit activities
│  ├─ Legal clearance for attack testing
│  ├─ Access credentials and infrastructure
│  └─ Data access for member/non-member datasets
│
└─ Step 5: Prepare audit plan
   ├─ Timeline and milestones
   ├─ Attack configurations and parameters
   ├─ Success/failure thresholds
   ├─ Reporting format and recipients
   └─ Remediation validation plan
```

## Workflow 2: Membership Inference Audit

```
START: Membership inference testing
│
├─ Step 1: Prepare datasets
│  ├─ Members: sample from training data (known members)
│  ├─ Non-members: sample from same distribution, not in training data
│  ├─ Balance: equal size member and non-member sets
│  ├─ Minimum size: 1,000 samples per set (larger for statistical power)
│  └─ Include samples from sensitive subgroups (for per-group analysis)
│
├─ Step 2: Select attack methods
│  ├─ Population metric attack (low cost, moderate accuracy)
│  │  └─ Compare target model loss on each sample against population loss
│  ├─ Reference model attack (medium cost, high accuracy)
│  │  └─ Train reference models to establish per-sample metrics
│  ├─ Shadow model attack (high cost, high accuracy)
│  │  └─ Train shadow models and binary classifier
│  ├─ LiRA attack (highest cost, best accuracy)
│  │  └─ Train IN/OUT models for likelihood ratio
│  └─ Select based on threat model and computational budget
│
├─ Step 3: Execute attacks
│  ├─ Query the target model for each sample (outputs, confidences, losses)
│  ├─ Run selected attack algorithms
│  ├─ Compute per-sample membership scores
│  └─ Log all queries and results
│
├─ Step 4: Analyse results
│  ├─ Compute ROC curve (TPR vs FPR)
│  ├─ Compute TPR at key FPR thresholds (0.1%, 1%, 5%)
│  ├─ Compute AUC (area under ROC curve)
│  ├─ Identify most vulnerable samples (highest membership scores)
│  ├─ Analyse per-subgroup vulnerability (demographic groups, data categories)
│  └─ Compare against thresholds:
│     ├─ TPR@1%FPR < 5% → Acceptable
│     ├─ TPR@1%FPR 5-15% → Elevated — mitigation recommended
│     └─ TPR@1%FPR > 15% → Unacceptable — mitigation required
│
└─ Step 5: Document results
   ├─ Attack methodology and configuration
   ├─ Results summary with ROC curves
   ├─ Most vulnerable sample characteristics
   ├─ Risk assessment aligned with DPIA
   └─ Recommended mitigations
```

## Workflow 3: Training Data Extraction Audit

```
START: Training data extraction testing
│
├─ Step 1: Canary insertion (if pre-training audit)
│  ├─ Generate unique canary strings (format: "CANARY-[UUID]-[DATA]")
│  ├─ Insert canaries at varying frequencies (1x, 5x, 10x, 50x)
│  ├─ Include canaries resembling real PII formats (email, phone, SSN patterns)
│  ├─ Document canary locations and frequencies
│  └─ Train model with canaries included
│
├─ Step 2: Extraction attempts
│  ├─ Prompt-based extraction (for language models):
│  │  ├─ Context-based prompting: provide partial training data, observe completion
│  │  ├─ Template prompting: "The email address of [name] is..."
│  │  ├─ Repetition prompting: repeat tokens to trigger memorized content
│  │  └─ High-temperature sampling: generate many outputs, check for training data
│  ├─ Gradient-based extraction (white-box):
│  │  ├─ Optimise input to maximise model output for target content
│  │  └─ Use gradient information to reconstruct training samples
│  └─ Generative reconstruction (for generative models):
│     ├─ Sample extensively from the model
│     └─ Compare generated outputs against training data
│
├─ Step 3: Measure extraction success
│  ├─ Canary extraction rate: percentage of canaries successfully extracted
│  ├─ Verbatim match rate: percentage of generated content matching training data
│  ├─ Near-verbatim rate: cosine similarity > 0.9 with training data
│  ├─ PII extraction rate: extractable PII types and quantities
│  └─ Compare against thresholds:
│     ├─ Extraction rate < 0.1% → Acceptable
│     ├─ Extraction rate 0.1-1% → Elevated
│     └─ Extraction rate > 1% → Unacceptable
│
├─ Step 4: PII-specific testing
│  ├─ Attempt to extract names, email addresses, phone numbers
│  ├─ Attempt to extract addresses, identification numbers
│  ├─ Attempt to extract health information, financial data
│  ├─ Test with known training data subjects as targets
│  └─ Document: types and volume of extractable PII
│
└─ Step 5: Document and report
   ├─ Extraction methodology
   ├─ Results with examples (redacted for report)
   ├─ PII-specific findings
   ├─ Risk assessment
   └─ Recommended mitigations (deduplication, DP, output filtering)
```

## Workflow 4: Model Inversion Audit

```
START: Model inversion testing
│
├─ Step 1: Select targets
│  ├─ Identify target classes or individuals in the model
│  ├─ Obtain ground truth for comparison (with consent, for audit purposes)
│  └─ Select diverse targets across demographic groups
│
├─ Step 2: Execute inversion attacks
│  ├─ Confidence-based inversion:
│  │  ├─ Initialise random input
│  │  ├─ Optimise to maximise model confidence for target class
│  │  ├─ Use multiple random initialisations
│  │  └─ Collect best reconstructions
│  ├─ GAN-based inversion (if applicable):
│  │  ├─ Train generator to produce inputs matching target model outputs
│  │  └─ Collect generated reconstructions
│  └─ White-box gradient inversion (if accessible):
│     ├─ Use gradient information to directly optimise reconstruction
│     └─ Apply regularisation to prevent artefacts
│
├─ Step 3: Evaluate reconstruction quality
│  ├─ Quantitative metrics:
│  │  ├─ SSIM (Structural Similarity Index) — 0 to 1 scale
│  │  ├─ PSNR (Peak Signal-to-Noise Ratio) — higher is more similar
│  │  ├─ Cosine similarity for embedding-based comparison
│  │  └─ FID (Frechet Inception Distance) for generative reconstruction quality
│  ├─ Re-identification assessment:
│  │  ├─ Can reconstructed data identify specific individuals?
│  │  ├─ Would a human recognise the original from the reconstruction?
│  │  └─ Can auxiliary information combined with reconstruction enable identification?
│  └─ Compare against thresholds:
│     ├─ SSIM < 0.3 → Acceptable
│     ├─ SSIM 0.3-0.6 → Elevated
│     └─ SSIM > 0.6 → Unacceptable
│
└─ Step 4: Document and report
   ├─ Attack methodology and parameters
   ├─ Reconstruction quality metrics
   ├─ Re-identification risk assessment
   └─ Recommended mitigations (output perturbation, confidence rounding)
```

## Workflow 5: Audit Report and Remediation

```
START: All audit attacks completed
│
├─ Step 1: Aggregate results
│  ├─ Compile results across all attack categories
│  ├─ Calculate overall privacy risk score
│  ├─ Identify highest-risk attack vectors
│  └─ Map findings to DPIA risk register entries
│
├─ Step 2: Generate audit report
│  ├─ Executive summary: overall privacy posture, key findings, recommendations
│  ├─ Per-attack results: methodology, metrics, pass/fail determination
│  ├─ Risk assessment: GDPR-aligned risk scoring (Low/Medium/High/Very High)
│  ├─ Mitigation recommendations: prioritised by risk and feasibility
│  ├─ Comparison with previous audits (if available)
│  └─ Appendices: detailed technical results, tools and configurations used
│
├─ Step 3: Remediation planning
│  ├─ For each failed threshold: identify applicable mitigation
│  ├─ Estimate mitigation impact on model performance
│  ├─ Prioritise mitigations by risk reduction and feasibility
│  ├─ Assign implementation owners and timelines
│  └─ Schedule validation audit post-remediation
│
├─ Step 4: Remediation validation
│  ├─ Apply mitigations (DP, deduplication, output perturbation, etc.)
│  ├─ Re-run failed attack categories
│  ├─ Verify metrics now meet acceptable thresholds
│  ├─ Document residual risk
│  └─ Issue audit certificate or note remaining deficiencies
│
└─ Step 5: Ongoing monitoring
   ├─ Schedule next periodic audit (12 months or at model retraining)
   ├─ Implement continuous monitoring for anomalous query patterns
   ├─ Track model updates that may affect privacy properties
   └─ Update DPIA with audit findings
```
