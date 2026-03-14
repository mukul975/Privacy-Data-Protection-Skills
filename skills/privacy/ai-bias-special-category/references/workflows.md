# AI Bias Assessment Workflows

## Workflow 1: Bias Assessment Process

```
START: AI system processes or infers special category data
│
├─ Step 1: Identify protected attributes
│  ├─ Art. 9 special categories in training data or inference
│  ├─ Equality law characteristics (gender, age, disability)
│  ├─ Proxy features correlated with protected attributes
│  └─ Document: protected attribute inventory
│
├─ Step 2: Data audit
│  ├─ Profile training data demographics
│  ├─ Compare against target population distribution
│  ├─ Identify underrepresented groups
│  ├─ Check for label bias in training data
│  └─ Document: data representation report
│
├─ Step 3: Select fairness metrics
│  ├─ Based on decision context (hiring, credit, healthcare)
│  ├─ Document metric selection justification
│  ├─ Acknowledge impossibility trade-offs
│  └─ Set acceptable disparity thresholds
│
├─ Step 4: Model testing
│  ├─ Disaggregated performance by protected group
│  ├─ Compute fairness metrics per group pair
│  ├─ Run counterfactual tests
│  ├─ Test intersectional combinations
│  └─ Document: model fairness report
│
├─ Step 5: Mitigation (if bias detected)
│  ├─ Select mitigation strategy (pre/in/post-processing)
│  ├─ Apply mitigation and re-test
│  ├─ Document accuracy-fairness trade-off
│  └─ Verify mitigation effectiveness
│
├─ Step 6: Documentation and approval
│  ├─ Complete bias assessment report
│  ├─ DPO and AI ethics board review
│  ├─ Integrate findings into DPIA
│  └─ Set ongoing monitoring schedule
│
└─ END: Deploy with monitoring. Review at model update or annually.
```

## Workflow 2: Art. 10(5) Bias Detection Data Processing

```
START: Need to process special category data for bias detection
│
├─ Step 1: Verify Art. 10(5) conditions
│  ├─ Processing is strictly necessary for bias monitoring/detection/correction
│  ├─ Cannot achieve bias assessment without special category data
│  └─ Document: necessity justification
│
├─ Step 2: Implement safeguards
│  ├─ Pseudonymise special category data before analysis
│  ├─ Restrict access to authorised bias assessment team only
│  ├─ Ensure data is not used for any other purpose
│  ├─ Set retention limit: delete after bias assessment completion
│  └─ Document: safeguards implementation
│
├─ Step 3: Conduct bias analysis
│  ├─ Compute fairness metrics using protected attribute data
│  ├─ Identify disparate impact patterns
│  └─ Document findings
│
├─ Step 4: Post-analysis data management
│  ├─ Delete special category data used for bias analysis
│  ├─ Retain only aggregate bias metrics and findings
│  ├─ Exception: retain if needed for compliance documentation
│  └─ Document: deletion confirmation
│
└─ END: Bias assessment complete. Special category data deleted.
```

## Workflow 3: Ongoing Bias Monitoring

```
START: AI system deployed in production
│
├─ Monitor decision distributions across groups (weekly/monthly)
├─ Alert if fairness metric exceeds threshold
├─ Investigate drift in group-level performance
├─ Re-run bias assessment if:
│  ├─ Model retrained
│  ├─ Population shift detected
│  ├─ Complaint received about discriminatory outcome
│  └─ Scheduled review period reached
│
└─ Document: monitoring results and any corrective actions
```
