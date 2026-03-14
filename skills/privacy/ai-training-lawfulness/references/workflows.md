# AI Training Data Lawfulness Workflows

## Workflow 1: Lawful Basis Selection Decision Tree

```
START: AI model training requires personal data
│
├─ Step 1: Is the AI training necessary to perform a contract with the data subject?
│  ├─ YES → Is the training for a personalised model serving the specific data subject?
│  │  ├─ YES → Art. 6(1)(b) may apply. Document necessity. Proceed to validation.
│  │  └─ NO → Art. 6(1)(b) does not apply. General model improvement is not contract necessity.
│  └─ NO → Continue.
│
├─ Step 2: Can valid consent be obtained from all data subjects?
│  ├─ Feasible (limited, identifiable population with direct relationship) →
│  │  ├─ Obtain specific consent for AI training purpose per Art. 7 requirements.
│  │  ├─ Document: consent language, collection mechanism, withdrawal process.
│  │  └─ Art. 6(1)(a) applies. Proceed to validation.
│  └─ Not feasible (large-scale, web-sourced, third-party data) → Continue.
│
├─ Step 3: Is the controller a public body/performing public interest task?
│  ├─ YES → Is there a legal basis in national/Union law authorising AI training?
│  │  ├─ YES → Art. 6(1)(e) applies. Document the legal basis. Proceed to validation.
│  │  └─ NO → Continue.
│  └─ NO → Continue.
│
├─ Step 4: Does the controller have a legitimate interest in AI training?
│  ├─ YES → Complete the three-part balancing test (Workflow 2).
│  │  ├─ Balancing favours controller → Art. 6(1)(f) applies with documented safeguards.
│  │  ├─ Balancing favours data subject → Art. 6(1)(f) does NOT apply. Seek alternative basis.
│  │  └─ Marginal → Implement maximum safeguards, consider alternative basis.
│  └─ NO → No lawful basis available. Do not proceed with training on personal data.
│
└─ END: Document selected lawful basis with supporting analysis.
```

## Workflow 2: Legitimate Interest Balancing Test for AI Training

### Part 1: Interest Identification

```
├─ 1.1 Articulate the specific interest
│  ├─ What is the precise interest? (Not "AI improvement" — specify the capability)
│  ├─ Example: "Training a fraud detection model to reduce unauthorized transactions for our payment processing customers"
│  └─ Document: interest statement, business case, beneficiaries
│
├─ 1.2 Verify legitimacy
│  ├─ Is the interest lawful? (Does not involve unlawful activities)
│  ├─ Is the interest real and present? (Not hypothetical future need)
│  ├─ Is the interest articulated clearly? (Specific enough for a regulator to evaluate)
│  └─ Document: legitimacy assessment
│
├─ 1.3 Identify beneficiaries
│  ├─ Who benefits? Controller / Third parties / Data subjects / Society
│  └─ Document: benefit distribution
```

### Part 2: Necessity Assessment

```
├─ 2.1 Is personal data necessary?
│  ├─ Could the model be trained on anonymised data? Test and document results.
│  ├─ Could synthetic data achieve adequate performance? Test and document.
│  ├─ Could federated learning avoid centralising personal data?
│  └─ Document: alternatives assessment with evidence
│
├─ 2.2 Is the volume proportionate?
│  ├─ Has the minimum effective training dataset been determined?
│  ├─ Can data be filtered to remove unnecessary personal data?
│  ├─ Has PII detection and removal been applied to training data?
│  └─ Document: data minimisation measures
│
├─ 2.3 Are all data elements necessary?
│  ├─ Review each personal data category: is it needed for model performance?
│  ├─ Can any categories be replaced with pseudonymised or generalised values?
│  └─ Document: per-element necessity justification
```

### Part 3: Balancing Test

```
├─ 3.1 Assess data subject impact
│  ├─ What are the consequences for data subjects?
│  │  ├─ Positive: improved service, fraud protection, personalisation
│  │  ├─ Neutral: no direct effect on most data subjects
│  │  └─ Negative: privacy intrusion, discrimination risk, loss of control
│  ├─ Are special categories involved? (Tips balance toward data subject)
│  ├─ Are vulnerable data subjects involved? (Children, employees, patients)
│  └─ Document: impact assessment
│
├─ 3.2 Assess reasonable expectations
│  ├─ Would data subjects expect their data to be used for AI training?
│  │  ├─ First-party data with AI training disclosure: expectations may be met
│  │  ├─ Publicly posted data: EDPB position is that AI training is not expected
│  │  ├─ Third-party purchased data: data subjects likely unaware
│  │  └─ Web-scraped data: data subjects did not intend AI training use
│  └─ Document: expectations analysis
│
├─ 3.3 Assess safeguards
│  ├─ Technical safeguards:
│  │  ├─ Differential privacy applied to training? (Specify epsilon)
│  │  ├─ PII detection and removal before training?
│  │  ├─ Access controls on training data and models?
│  │  ├─ Training data encryption at rest and in transit?
│  │  └─ Model privacy testing (membership inference, extraction)?
│  ├─ Organisational safeguards:
│  │  ├─ Privacy notice updated to cover AI training?
│  │  ├─ Opt-out mechanism available and accessible?
│  │  ├─ DPO oversight of AI training activities?
│  │  └─ Regular review and update of balancing test?
│  └─ Document: safeguards inventory
│
├─ 3.4 Weigh the balance
│  ├─ Controller interest strength: Strong / Moderate / Weak
│  ├─ Data subject impact: High / Medium / Low
│  ├─ Expectations alignment: Met / Partially met / Not met
│  ├─ Safeguards adequacy: Comprehensive / Adequate / Insufficient
│  │
│  ├─ OUTCOME: Controller interest overrides
│  │  → Document balancing with evidence. Implement safeguards. Proceed.
│  ├─ OUTCOME: Data subject rights override
│  │  → Do not proceed. Consider consent or anonymisation alternatives.
│  └─ OUTCOME: Marginal
│     → Implement maximum safeguards. Consult DPO. Consider alternative basis.
│
└─ Document: complete balancing test with dated sign-off.
```

## Workflow 3: Training Data Source Assessment

```
FOR EACH DATA SOURCE IN TRAINING PIPELINE:
│
├─ Step 1: Data source classification
│  ├─ First-party collected
│  ├─ Third-party purchased/licensed
│  ├─ Public dataset (academic/government)
│  ├─ Open-source dataset (with license)
│  ├─ Web-scraped
│  └─ User-contributed
│
├─ Step 2: Personal data identification
│  ├─ Run PII detection scan on dataset sample
│  ├─ Identify categories: names, emails, addresses, photos, IDs, health, financial
│  ├─ Assess indirect identifiability: can individuals be identified through combination?
│  ├─ Assess inferability: does the data enable inference of sensitive attributes?
│  └─ Document: data categories and identifiability assessment
│
├─ Step 3: Original purpose and compatibility
│  ├─ What was the original collection purpose?
│  ├─ Was AI training disclosed as a purpose at collection?
│  ├─ If repurposed: conduct Art. 6(4) compatibility assessment
│  │  ├─ Link between original and AI training purpose
│  │  ├─ Context of collection
│  │  ├─ Nature of the data (sensitive = less compatible)
│  │  ├─ Consequences of AI training for data subjects
│  │  └─ Existence of safeguards (pseudonymisation, encryption)
│  └─ Document: compatibility assessment
│
├─ Step 4: Lawful basis identification
│  ├─ Apply Workflow 1 for this specific source
│  ├─ Document the selected basis with justification
│  └─ If no valid basis → EXCLUDE from training pipeline
│
├─ Step 5: Special category check
│  ├─ Does the source contain Art. 9 data?
│  │  ├─ YES → Identify Art. 9(2) condition
│  │  │  ├─ Condition available → Document and proceed
│  │  │  └─ No condition → EXCLUDE Art. 9 data or entire source
│  │  └─ NO → Continue
│  └─ Can Art. 9 data be inferred from non-sensitive data?
│     └─ YES → Treat as special category processing
│
├─ Step 6: Upstream chain verification (third-party sources)
│  ├─ Has the provider documented their lawful basis for collection?
│  ├─ Does the licence/agreement permit AI training use?
│  ├─ Has the provider warranted consent scope or legitimate interest assessment?
│  ├─ Has due diligence been conducted on the provider's practices?
│  └─ Document: chain of lawfulness verification
│
├─ Step 7: Safeguards implementation
│  ├─ PII filtering/removal applied?
│  ├─ Pseudonymisation applied?
│  ├─ Data subject opt-out mechanism operational?
│  ├─ Training data access controls in place?
│  └─ Document: safeguards for this source
│
└─ Step 8: Register in training data catalogue
   ├─ Source identifier and metadata
   ├─ Lawful basis with reference to assessment
   ├─ Safeguards applied
   ├─ Retention period
   └─ Next review date
```

## Workflow 4: Consent Management for AI Training

```
START: Consent selected as lawful basis for AI training
│
├─ Step 1: Draft consent language
│  ├─ Specify the AI training purpose clearly
│  ├─ Identify what personal data will be used
│  ├─ Explain how long data will be retained for training
│  ├─ Disclose model memorization risks
│  ├─ Explain limitations on erasure from trained models
│  └─ Legal review of consent language
│
├─ Step 2: Implement consent collection
│  ├─ Separate AI training consent from other consents
│  ├─ Use affirmative opt-in mechanism (no pre-ticked boxes)
│  ├─ Record: identity, timestamp, version of consent text, mechanism
│  └─ Do not condition service access on AI training consent (unless necessary)
│
├─ Step 3: Implement withdrawal mechanism
│  ├─ Provide easy withdrawal (equivalent ease to providing consent)
│  ├─ Define process for data removal from training pipeline
│  ├─ Define process for model update/retraining following withdrawal
│  ├─ Document technical limitations on removing data from trained models
│  └─ Communicate withdrawal consequences transparently
│
├─ Step 4: Ongoing management
│  ├─ Monitor consent rates and withdrawal rates
│  ├─ Review consent language when training purpose changes
│  ├─ Re-consent when expanding to new training purposes
│  └─ Audit consent records periodically
│
└─ END: Maintain consent register linked to training data catalogue.
```

## Workflow 5: Web Scraping Lawfulness Assessment

```
START: Considering web-scraped data for AI training
│
├─ Step 1: Assess personal data presence
│  ├─ Scan sample for PII
│  ├─ Assess identifiability of scraped content
│  ├─ If no personal data → Copyright/TDM rules apply, but GDPR obligations reduced
│  └─ If personal data present → Continue full assessment
│
├─ Step 2: Assess lawful basis availability
│  ├─ Consent → Not feasible at scale. Cannot identify and contact all data subjects.
│  ├─ Contract → No contractual relationship with scraped data subjects. Not available.
│  ├─ Legitimate interest → Complete Workflow 2 with heightened scrutiny.
│  └─ If no basis available → Do not use scraped data containing personal data.
│
├─ Step 3: EDPB heightened scrutiny factors
│  ├─ Were data subjects aware their data would be scraped? (Typically no)
│  ├─ Did data subjects implement privacy settings? (Respect settings as expression of objection)
│  ├─ Is robots.txt respected? (Necessary but not sufficient for GDPR)
│  ├─ Does the source website's terms prohibit scraping? (Indicates expectations)
│  ├─ What categories of personal data are being scraped? (Sensitive = higher bar)
│  ├─ Are children's data likely present? (Heightened protection required)
│  └─ Document: heightened scrutiny assessment
│
├─ Step 4: Implement maximum safeguards
│  ├─ Apply PII detection and removal before training
│  ├─ Implement opt-out mechanism (web form, API, robots.txt extension)
│  ├─ Honour opt-out requests within defined timeframe
│  ├─ Apply differential privacy during training
│  ├─ Publish transparency information about scraping and AI training
│  └─ Document: safeguards implementation
│
├─ Step 5: Document decision
│  ├─ Record complete assessment with legal counsel review
│  ├─ Accept risk or implement alternatives
│  └─ Schedule review when regulatory guidance evolves
│
└─ END: If proceeding, register in training data catalogue with "web-scraped" flag.
```
