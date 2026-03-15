# Automated Decision-Making and Profiling Rights Workflows

## Workflow 1: Art. 22 Applicability Assessment

```
[Automated Processing Activity Identified]
         │
         ▼
[Is the decision solely automated?]
   │
   ├── No meaningful human intervention ──► SOLELY AUTOMATED
   │     (Human involvement is a rubber stamp,
   │      reviewer lacks authority/competence,
   │      or reviewer routinely endorses without review)
   │
   └── Genuine human intervention exists ──► NOT SOLELY AUTOMATED
         (Reviewer has authority, competence,         Art. 22 does NOT apply
          and genuinely considers the output)         (but Art. 5/6 still apply)
         │
         ▼ (if solely automated)
[Does the decision produce legal effects?]
   │
   ├── Affects legal rights (contract denial, benefit refusal) ──► LEGAL EFFECT
   │
   └── No legal effect ──► [Similarly significant effect?]
         │
         ├── Material impact on circumstances, behaviour, or choices
         │   (job rejection, significant price differential, service denial)
         │   ──► SIMILARLY SIGNIFICANT EFFECT
         │
         └── Minimal or no impact ──► Art. 22 does NOT apply
         │
         ▼
[Art. 22(1) APPLIES — Prohibition on solely automated decisions]
         │
         ▼
[Does an exception under Art. 22(2) apply?]
   ├── (a) Necessary for contract? ──► Exception applies + safeguards required
   ├── (b) Authorised by law? ──► Exception applies + statutory safeguards
   └── (c) Explicit consent? ──► Exception applies + safeguards required
         │
         ▼
[No exception?] ──► Decision CANNOT be made solely by automated means
                     Human intervention is MANDATORY in the decision process
```

## Workflow 2: Contestation Process

```
[Data Subject Contests Automated Decision]
         │
         ▼
[Log Contestation: ADM-YYYY-NNNN]
   - Record the decision contested
   - Record the data subject's grounds
   - Record any additional evidence provided
         │
         ▼
[Assign Independent Human Reviewer]
   - Must NOT have been involved in original decision
   - Must have authority to override
   - Must have relevant domain expertise
         │
         ▼
[Reviewer Conducts Assessment]
   - Review the automated decision and its basis
   - Review the data subject's contestation
   - Consider the specific circumstances
   - Analyse model inputs and outputs for the specific case
         │
         ▼
[Reviewer Decision]
   │
   ├── UPHOLD original decision
   │     - Document reasoning
   │     - Notify subject: decision upheld + reasons
   │     - Inform: right to complain (Art. 77) + judicial remedy (Art. 79)
   │
   ├── MODIFY decision
   │     - Document reasoning and new outcome
   │     - Notify subject: decision modified + new outcome + next steps
   │
   └── OVERTURN decision
         - Document reasoning and new outcome
         - Notify subject: decision overturned + new outcome + next steps
         │
         ▼
[Log outcome for model monitoring]
   - Update contestation register
   - Feed into quarterly model review
```

## Workflow 3: Logic Explanation Process

```
[Data Subject Requests Art. 22 Explanation]
         │
         ▼
[Identify the Automated Decision]
         │
         ▼
[Compile Explanation Components]
   │
   ├── [1. Existence confirmation]
   │     "We confirm automated decision-making is used for [purpose]"
   │
   ├── [2. Input factors]
   │     List all data inputs used by the model
   │     Describe general weighting/importance of each factor
   │
   ├── [3. Decision logic]
   │     Functional description of how inputs are combined
   │     Thresholds or rules that determine outcomes
   │     (NOT source code or algorithm weights)
   │
   ├── [4. Accuracy information]
   │     Overall accuracy rate
   │     False positive and false negative rates
   │     Last validation date
   │
   └── [5. Significance and consequences]
         What the decision means in practical terms
         Possible outcomes and their impact
         │
         ▼
[Review by DPO for clarity and completeness]
         │
         ▼
[Deliver explanation to data subject]
   - Plain language, no technical jargon
   - Within 30-day response deadline
```

## Workflow 4: Human Oversight Audit

```
[Quarterly Review Trigger]
         │
         ▼
[For Each Art. 22 Decision Type]
   │
   ├── [Review Metrics]
   │     - Total automated decisions in period
   │     - Number reviewed by human within SLA (48 hours)
   │     - Override rate (target: indicates genuine review, not rubber-stamping)
   │     - Average review time per decision
   │     - Contestation rate
   │     - Contestation overturn rate
   │
   ├── [Compliance Check]
   │     - All designated reviewers still employed and trained?
   │     - Review dashboard providing adequate information?
   │     - Override documentation complete?
   │
   └── [Risk Indicators]
         - Contestation rate > 10%? ──► Trigger model review
         - Overturn rate > 15%? ──► Escalate to DPO for potential model decommissioning
         - Override rate < 2%? ──► Investigate whether human review is genuine
         - Review time < 30 seconds average? ──► Investigate rubber-stamping
         │
         ▼
[Generate Quarterly Art. 22 Compliance Report]
   - Findings
   - Recommendations
   - Action items with owners and deadlines
```
