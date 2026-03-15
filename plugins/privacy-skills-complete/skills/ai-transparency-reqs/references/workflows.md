# AI Transparency Workflows

## Workflow 1: AI Transparency Assessment

```
START: AI system is deployed or materially changed
│
├─ Step 1: Classify the AI system
│  ├─ AI Act classification: Unacceptable / High-risk / Limited / Minimal
│  ├─ GDPR automated decision-making: Art. 22 applicable? Yes / No
│  └─ Data subjects directly interacting with AI? Yes / No
│
├─ Step 2: Identify transparency obligations
│  ├─ GDPR Arts. 13-14: Privacy notice updated for AI processing?
│  ├─ GDPR Art. 13(2)(f)/14(2)(g): Meaningful logic information provided?
│  ├─ AI Act Art. 50(1): AI interaction notification required?
│  ├─ AI Act Art. 50(3): AI-generated content labelling required?
│  ├─ AI Act Art. 13: High-risk documentation for deployers?
│  ├─ AI Act Art. 86: Individual explanation right applicable?
│  └─ Document: applicable obligations checklist
│
├─ Step 3: Assess current transparency measures
│  ├─ Privacy notice: does it cover AI-specific processing? Review against checklist.
│  ├─ AI notification: are users informed about AI interaction?
│  ├─ Logic explanation: is meaningful information about decision logic provided?
│  ├─ Model card: is technical documentation maintained?
│  ├─ Individual explanation: can data subjects obtain per-decision explanations?
│  └─ Document: gap analysis
│
├─ Step 4: Implement remediation
│  ├─ Update privacy notice with AI-specific information
│  ├─ Deploy AI interaction notification
│  ├─ Create layered transparency documentation
│  ├─ Implement explainability tools for individual explanations
│  ├─ Generate and publish model card
│  └─ Document: implementation plan with deadlines
│
└─ Step 5: Ongoing monitoring
   ├─ Review transparency measures when AI system is updated
   ├─ Audit AI notifications for accuracy and completeness
   ├─ Test individual explanation mechanisms
   └─ Schedule periodic review (minimum annually)
```

## Workflow 2: Privacy Notice AI Section Development

```
START: Privacy notice requires AI processing section
│
├─ Step 1: Identify all AI processing activities
│  ├─ List all AI systems processing personal data
│  ├─ For each system: purpose, lawful basis, data categories, decision authority
│  └─ Group by data subject category (customers, employees, website visitors)
│
├─ Step 2: Draft Layer 1 — Initial notification
│  ├─ Short statement: "We use AI to [purpose]"
│  ├─ Link to full AI transparency information
│  ├─ Placement: at point of AI interaction (banner, tooltip, chat interface)
│  └─ Review: plain language, concise, under 50 words
│
├─ Step 3: Draft Layer 2 — Summary in privacy notice
│  For each AI system:
│  ├─ AI system description (what it does, in plain language)
│  ├─ Purpose of AI processing
│  ├─ Lawful basis (Art. 6(1) and Art. 9(2) if applicable)
│  ├─ Personal data categories processed (training and inference)
│  ├─ Decision authority (AI decision-support vs. automated decision)
│  ├─ Key factors influencing AI output (not proprietary details)
│  ├─ Data subject rights (including AI-specific: explanation, contestation, human review)
│  ├─ Retention periods (training data, inference logs, model lifecycle)
│  ├─ Recipients (AI infrastructure providers, model hosting)
│  └─ International transfers (training/inference jurisdictions)
│
├─ Step 4: Draft Layer 3 — Detailed AI documentation
│  ├─ Model card summary (architecture, training approach)
│  ├─ Training data categories and sources (not individual records)
│  ├─ Fairness and accuracy metrics
│  ├─ Known limitations and failure modes
│  ├─ Human oversight measures
│  ├─ Privacy safeguards (differential privacy, PII filtering)
│  └─ Publish as supplementary document linked from privacy notice
│
├─ Step 5: Review and approval
│  ├─ Legal review for compliance with Arts. 12-14 requirements
│  ├─ DPO review for completeness
│  ├─ Usability review: is it intelligible to the average data subject?
│  ├─ Translation for all applicable languages
│  └─ Approve and publish
│
└─ Step 6: Maintenance
   ├─ Update when AI systems change
   ├─ Update when new AI systems are deployed
   ├─ Version control privacy notice
   └─ Review at minimum annually
```

## Workflow 3: Art. 22 Explanation Process

```
START: Data subject requests explanation of automated AI decision
│
├─ Step 1: Verify Art. 22 applicability
│  ├─ Was the decision solely automated? (No meaningful human intervention)
│  ├─ Does the decision produce legal or similarly significant effects?
│  ├─ If both YES → Art. 22 applies. Provide explanation.
│  └─ If NO to either → Voluntary explanation recommended. Provide if possible.
│
├─ Step 2: Retrieve decision information
│  ├─ Identify the specific decision (date, outcome, context)
│  ├─ Retrieve model inputs for this decision
│  ├─ Retrieve model output (score, classification, recommendation)
│  ├─ Retrieve any human review that occurred
│  └─ Log: explanation request details and decision record
│
├─ Step 3: Generate explanation
│  ├─ Run SHAP/LIME analysis on the specific prediction
│  ├─ Identify top contributing features
│  ├─ Generate counterfactual ("if X were Y, outcome would differ")
│  ├─ Translate technical output into plain language
│  └─ Include: decision outcome, key factors, what would change the outcome
│
├─ Step 4: Provide explanation
│  ├─ Deliver within Art. 12 timeframe (one month, extendable by two months)
│  ├─ Include:
│  │  ├─ The decision that was made
│  │  ├─ The key factors that influenced the decision
│  │  ├─ How those factors were weighted (general terms)
│  │  ├─ What the decision means for the data subject
│  │  ├─ What data the subject could change to obtain a different outcome
│  │  └─ How to request human review or contest the decision
│  └─ Record: explanation provided, date, content
│
├─ Step 5: Post-explanation rights
│  ├─ Right to human review: escalate to qualified reviewer
│  ├─ Right to express views: record data subject's perspective
│  ├─ Right to contest: process through complaint mechanism
│  └─ Document: post-explanation actions and outcomes
│
└─ END: File explanation record in data subject rights register.
```

## Workflow 4: AI Act Art. 50 Notification Implementation

```
START: AI system requires Art. 50 transparency
│
├─ Step 1: Determine applicable Art. 50 obligation
│  ├─ Art. 50(1): AI interacting with natural persons → Notify of AI interaction
│  ├─ Art. 50(2): Emotion recognition / biometric categorisation → Inform of operation
│  ├─ Art. 50(3): AI-generated/manipulated content → Label as AI-generated
│  ├─ Art. 50(4): AI-generated text on public interest → Disclose AI generation
│  └─ Multiple may apply simultaneously
│
├─ Step 2: Design notification mechanism
│  ├─ For AI interaction notification:
│  │  ├─ Chatbot/virtual assistant → "You are interacting with an AI system" before first response
│  │  ├─ AI customer service → Notification in call introduction or chat opening
│  │  ├─ AI-generated email → "[AI-generated]" label or disclosure in footer
│  │  └─ Recommendation system → "Recommendations are generated by AI" disclosure
│  │
│  ├─ For AI content labelling:
│  │  ├─ Images: machine-readable metadata (C2PA, IPTC) + visible label
│  │  ├─ Video: machine-readable metadata + visible watermark/label
│  │  ├─ Audio: machine-readable metadata + verbal disclosure at start
│  │  └─ Text: machine-readable marker + visible disclosure
│  │
│  └─ For emotion recognition:
│     ├─ Prominent notice before processing begins
│     ├─ Clear description of what is being detected
│     └─ GDPR consent requirements must also be met
│
├─ Step 3: Implement notification
│  ├─ Develop notification copy (plain language, accessible)
│  ├─ Integrate into user interface / content pipeline
│  ├─ Test accessibility (screen readers, colour contrast, language)
│  ├─ Test: notification appears before/at point of AI interaction
│  └─ Test: labels persist when content is shared or redistributed
│
├─ Step 4: Verify and audit
│  ├─ Verify notification displays correctly across platforms
│  ├─ Test edge cases (notification failure, API-only interaction)
│  ├─ Audit notification content for accuracy
│  └─ Document: notification implementation with screenshots/evidence
│
└─ Step 5: Ongoing compliance
   ├─ Monitor for new AI systems requiring notification
   ├─ Update notifications when AI system capabilities change
   ├─ Review notification effectiveness (user comprehension)
   └─ Track regulatory guidance on notification requirements
```

## Workflow 5: Model Card Generation and Maintenance

```
START: AI model deployed or updated
│
├─ Step 1: Gather model information
│  ├─ From ML engineer: architecture, training methodology, performance metrics
│  ├─ From data team: training data description, data quality assessment
│  ├─ From privacy team: privacy properties, DPIA findings, transparency requirements
│  ├─ From business owner: intended use, deployment context, success criteria
│  └─ From legal: regulatory classification, compliance requirements
│
├─ Step 2: Complete model card template
│  ├─ Model overview: name, version, type, date, developer
│  ├─ Intended use: specific purpose, target users, scope
│  ├─ Out-of-scope use: misuse scenarios, unsupported contexts
│  ├─ Training data: source categories, volume, temporal range, known biases
│  ├─ Performance: accuracy, precision, recall by subgroup
│  ├─ Fairness: demographic parity, equalized odds, calibration
│  ├─ Limitations: failure modes, edge cases, performance disparities
│  ├─ Privacy: DP epsilon, MI test results, extraction risk
│  ├─ Human oversight: required level, reviewer qualifications
│  └─ Ethical considerations: potential harms, mitigation measures
│
├─ Step 3: Review and approval
│  ├─ ML engineer reviews technical accuracy
│  ├─ DPO reviews privacy and transparency content
│  ├─ Legal reviews regulatory compliance content
│  ├─ Business owner reviews intended use accuracy
│  └─ Version and date the model card
│
├─ Step 4: Publication
│  ├─ Store in model registry alongside model artefacts
│  ├─ Link from privacy notice Layer 3 documentation
│  ├─ Make accessible to deployers (if model is provided to third parties)
│  └─ Archive previous versions
│
└─ Step 5: Maintenance triggers
   ├─ Model retraining → Update training data and performance sections
   ├─ New use case deployment → Update intended use and limitations
   ├─ Fairness issue discovered → Update limitations and ethical considerations
   ├─ Regulatory change → Update compliance requirements section
   └─ Annual review → Verify all sections remain current
```
