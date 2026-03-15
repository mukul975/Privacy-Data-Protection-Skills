# Workflow -- DPIA Risk Scoring

## Phase 1: Risk Identification

### Step 1.1: Enumerate Privacy Risks
- Review processing activity description and data flows
- Identify potential threat scenarios using ENISA taxonomy
- Map each threat to affected rights and freedoms (Recital 75)
- Catalogue risk sources: internal actors, external attackers, processors, system failures

### Step 1.2: Categorise Risks
- Assign each risk to a rights/freedoms impact category
- Distinguish between compliance risks and data subject harm risks
- Group related risks for consolidated assessment where appropriate

## Phase 2: Inherent Risk Assessment

### Step 2.1: Assess Severity
- Evaluate the worst-case impact on data subjects if the risk materialises
- Consider: reversibility, number of affected data subjects, nature of data, vulnerability of data subjects
- Assign severity score (1-4) with documented rationale

### Step 2.2: Assess Likelihood
- Evaluate probability of the risk materialising in the absence of specific mitigation measures
- Consider: threat landscape, attack surface, historical incidents, processing complexity
- Assign likelihood score (1-4) with documented rationale

### Step 2.3: Calculate Inherent Risk Score
- Inherent Risk = Severity x Likelihood
- Map to risk level: Low (1-3), Medium (4-6), High (7-9), Very High (10-16)
- Record in risk register

## Phase 3: Mitigation Assessment

### Step 3.1: Identify Existing Controls
- Document technical measures (encryption, access controls, pseudonymisation)
- Document organisational measures (policies, training, audits)
- Assess effectiveness of each control against the identified risks

### Step 3.2: Identify Additional Mitigation Measures
- For each High or Very High inherent risk, identify feasible additional controls
- Evaluate cost-benefit of each proposed measure
- Determine expected risk reduction per measure

## Phase 4: Residual Risk Calculation

### Step 4.1: Re-Assess After Mitigation
- Re-evaluate likelihood considering all planned mitigation measures
- Severity typically remains unchanged (worst-case impact)
- Calculate Residual Risk = Severity x Adjusted Likelihood

### Step 4.2: Compare Against Risk Appetite
- Compare residual risk levels against organisational risk appetite thresholds
- Identify any risks that remain High or Very High after mitigation

## Phase 5: Decision and Escalation

### Step 5.1: Risk Acceptance or Escalation
- Risks within appetite: Accept with documented rationale and monitoring plan
- Risks above appetite but below prior consultation threshold: Escalate to senior management
- Risks at High/Very High after all feasible mitigation: Trigger Art. 36 prior consultation

### Step 5.2: Document Risk Register
- Complete risk register with all inherent scores, controls, residual scores
- Record risk owners and review dates
- Link to DPIA report section 7(c) and 7(d)
