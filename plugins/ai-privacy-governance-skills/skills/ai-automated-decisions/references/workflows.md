# AI Automated Decision-Making Workflows

## Workflow 1: Art. 22 Applicability Assessment

```
START: AI system produces outputs that influence decisions about individuals
│
├─ Step 1: Is there a "decision"?
│  ├─ Does the AI output directly determine an outcome for the individual?
│  │  ├─ YES (e.g., auto-approval/denial, score-based routing) → Decision exists.
│  │  └─ NO (e.g., AI provides input, human decides independently) → Art. 22 likely not triggered.
│  └─ Note: "decision" is broadly interpreted — includes automated categorisation that determines treatment.
│
├─ Step 2: Is the decision "solely" automated?
│  ├─ Is there human involvement in the decision chain?
│  │  ├─ NO → Solely automated. Continue to Step 3.
│  │  └─ YES → Assess if human involvement is "meaningful":
│  │     ├─ Does reviewer have authority to change the decision? → If NO → Solely automated.
│  │     ├─ Does reviewer have competence to evaluate? → If NO → Solely automated.
│  │     ├─ Does reviewer have access to all relevant information? → If NO → Solely automated.
│  │     ├─ Is sufficient time allocated for review? → If NO → Solely automated.
│  │     ├─ Does reviewer actually exercise discretion? (Check override rates) → If < 5% → Red flag.
│  │     └─ All criteria met → NOT solely automated. Art. 22 likely not triggered.
│
├─ Step 3: Does the decision produce "legal or similarly significant effects"?
│  ├─ Legal effects? (Contract, legal status, legal obligation) → YES → Art. 22 triggered.
│  ├─ Access to services? (Credit, insurance, housing, education, employment) → YES → Art. 22 triggered.
│  ├─ Significant financial impact? (Pricing, payments, benefits) → YES → Art. 22 triggered.
│  ├─ Health/safety impact? → YES → Art. 22 triggered.
│  ├─ Freedom/autonomy impact? → YES → Art. 22 triggered.
│  └─ None of the above → Art. 22 likely not triggered. Document assessment.
│
├─ Step 4: Art. 22 triggered — identify applicable exception
│  ├─ Art. 22(2)(a) — Contract necessity?
│  │  └─ Is the automated decision necessary for entering into or performing a contract?
│  ├─ Art. 22(2)(b) — Legal authorisation?
│  │  └─ Is there Union or Member State law authorising the automated decision with safeguards?
│  ├─ Art. 22(2)(c) — Explicit consent?
│  │  └─ Has the data subject given explicit consent to automated decision-making?
│  └─ No exception → Data subject has right not to be subject to the decision.
│
├─ Step 5: Implement Art. 22(3) safeguards (if exception relied upon)
│  ├─ Right to human intervention → Implement qualified reviewer process
│  ├─ Right to express point of view → Enable data subject submissions
│  ├─ Right to contest → Implement contestation mechanism (Workflow 3)
│  └─ Special category data check → If Art. 9 data used, verify Art. 22(4) conditions
│
└─ END: Document Art. 22 assessment with conclusion and safeguards.
```

## Workflow 2: Human Oversight Implementation

```
START: AI system requires human oversight (Art. 22/AI Act Art. 14)
│
├─ Step 1: Determine appropriate oversight level
│  ├─ High-stakes individual decisions (hiring, credit, medical, judicial)
│  │  └─ Human-in-the-loop (HITL): Review every decision
│  ├─ Medium-risk decisions with volume
│  │  └─ Human-on-the-loop (HOTL): Monitor and intervene on exceptions
│  ├─ Low-risk decisions with high volume
│  │  └─ Human-in-command (HIC): Set parameters, review samples and outcomes
│  └─ Document: selected level with justification
│
├─ Step 2: Design the oversight process
│  ├─ Define reviewer role and qualifications
│  │  ├─ Domain expertise requirements
│  │  ├─ Training on AI system capabilities and limitations
│  │  ├─ Training on automation bias awareness
│  │  └─ Authority to override AI decisions
│  ├─ Define information provided to reviewer
│  │  ├─ AI input data
│  │  ├─ AI output (score, classification, recommendation)
│  │  ├─ AI explanation (key factors, confidence level)
│  │  ├─ Contextual information beyond AI input
│  │  └─ Data subject's submitted information (if Art. 22(3))
│  ├─ Define time allocation
│  │  ├─ Minimum review time per decision
│  │  ├─ Maximum daily decision volume per reviewer
│  │  └─ Escalation for complex cases
│  └─ Define override process
│     ├─ How reviewer records a decision different from AI recommendation
│     ├─ Justification documentation for overrides
│     └─ Feedback loop to AI system improvement
│
├─ Step 3: Implement automation bias countermeasures
│  ├─ Present AI recommendation after reviewer forms initial assessment (delayed reveal)
│  ├─ Require reviewer to document their assessment before seeing AI output
│  ├─ Regularly present test cases with known incorrect AI outputs
│  ├─ Monitor override rates — very low rates trigger investigation
│  ├─ Rotate reviewers to prevent habituation
│  └─ Train reviewers on known AI failure modes
│
├─ Step 4: Deploy monitoring
│  ├─ Track override rate by reviewer and time period
│  ├─ Track decision accuracy (where ground truth is available)
│  ├─ Track time spent per review
│  ├─ Track data subject contestation outcomes
│  └─ Alert when metrics indicate oversight may not be meaningful
│
└─ Step 5: Periodic review
   ├─ Monthly: review override rates and decision quality
   ├─ Quarterly: assess reviewer effectiveness and training needs
   ├─ Annually: full oversight design review
   └─ On incident: investigate any case where oversight failed
```

## Workflow 3: Contestation Process

```
START: Data subject contests an automated AI decision
│
├─ Step 1: Receive contestation
│  ├─ Record: data subject identity, decision contested, date of decision
│  ├─ Record: grounds for contestation (data subject's reasons)
│  ├─ Record: any supporting evidence submitted
│  ├─ Acknowledge receipt within 5 business days
│  └─ Assign case reference number
│
├─ Step 2: Retrieve decision record
│  ├─ Identify the specific AI decision (inputs, output, date, context)
│  ├─ Retrieve AI explanation (SHAP/LIME output or equivalent)
│  ├─ Retrieve any human review that occurred
│  ├─ Retrieve applicable model version and configuration
│  └─ Document: complete decision record
│
├─ Step 3: Assign qualified reviewer
│  ├─ Reviewer must be different from original decision oversight (if any)
│  ├─ Reviewer must have authority to overturn the decision
│  ├─ Reviewer must have domain expertise
│  └─ Reviewer must have no conflict of interest
│
├─ Step 4: Review
│  ├─ Reviewer examines:
│  │  ├─ AI inputs — were they accurate and complete?
│  │  ├─ AI output — was the model functioning correctly?
│  │  ├─ AI explanation — do the key factors make sense in context?
│  │  ├─ Data subject's arguments — do they identify valid concerns?
│  │  ├─ Supporting evidence — does it change the assessment?
│  │  └─ Applicable policies — was the decision consistent with policy?
│  ├─ Reviewer may request additional information from data subject
│  └─ Reviewer makes independent determination
│
├─ Step 5: Decision
│  ├─ Uphold: Original decision confirmed
│  │  ├─ Provide reasons for upholding
│  │  ├─ Inform data subject of right to complain to DPA
│  │  └─ Inform data subject of right to judicial remedy
│  ├─ Modify: Decision adjusted based on review
│  │  ├─ Document modification and reasons
│  │  ├─ Implement modified decision
│  │  └─ Inform data subject of modification
│  └─ Overturn: Original decision reversed
│     ├─ Document reversal and reasons
│     ├─ Implement reversed decision
│     ├─ Assess if AI model requires correction
│     └─ Inform data subject of reversal
│
├─ Step 6: Communication
│  ├─ Notify data subject within 30 days (Art. 12 timeframe)
│  ├─ Provide: outcome, reasons, next steps
│  ├─ If complex: extend by up to 60 days with notification
│  └─ Record: full contestation record in rights register
│
└─ Step 7: Learning
   ├─ Analyse contestation outcomes for patterns
   ├─ If systematic issues found → trigger AI system review
   ├─ Feed outcomes into model improvement pipeline
   └─ Report contestation statistics to AI governance board
```

## Workflow 4: Profiling Assessment

```
START: AI system evaluates personal aspects of individuals
│
├─ Step 1: Confirm profiling exists
│  ├─ Does the AI evaluate or predict personal aspects?
│  │  ├─ Work performance → Profiling
│  │  ├─ Economic situation → Profiling
│  │  ├─ Health → Profiling
│  │  ├─ Personal preferences → Profiling
│  │  ├─ Reliability → Profiling
│  │  ├─ Behaviour → Profiling
│  │  ├─ Location/movements → Profiling
│  │  └─ None of the above → Not profiling under Art. 4(4)
│  └─ Document: profiling determination
│
├─ Step 2: Assess profiling impact
│  ├─ Does profiling feed into a decision with legal/significant effects?
│  │  ├─ YES → Art. 22 assessment required (Workflow 1)
│  │  └─ NO → Art. 22 not triggered, but other GDPR obligations apply
│  ├─ Does profiling use special category data?
│  │  ├─ YES → Art. 22(4) applies; Art. 9(2)(a) or (g) required
│  │  └─ NO → Standard assessment
│  └─ Does profiling affect vulnerable data subjects?
│     ├─ YES → Enhanced safeguards required
│     └─ NO → Standard safeguards
│
├─ Step 3: Implement profiling safeguards
│  ├─ Transparency: inform data subjects about profiling (Arts. 13-14)
│  ├─ Right to object: Art. 21 objection mechanism for profiling
│  ├─ Data minimisation: limit data used for profiling to what is necessary
│  ├─ Accuracy: ensure profiling inputs are accurate and current
│  ├─ Fairness: assess profiling for discriminatory outcomes
│  └─ DPIA: conduct DPIA for systematic profiling (Art. 35(3)(a))
│
└─ END: Document profiling assessment and safeguards.
```
