# AI Data Retention Workflows

## Workflow 1: Training Data Retention Review

```
START: Training complete or retention review date reached
│
├─ For each training data category:
│  ├─ Is retraining planned within retention period? → Retain with justification
│  ├─ Is data needed for ongoing validation? → Pseudonymise and retain
│  ├─ Is data needed for rights exercise? → Retain with controls
│  ├─ Legal retention obligation? → Retain per requirement
│  └─ None of the above → DELETE and verify deletion
│
├─ Document retention decisions in data register
├─ Set next review date (maximum 12 months)
└─ END
```

## Workflow 2: Machine Unlearning Process

```
START: Data deletion request affecting trained model
│
├─ Step 1: Delete from training dataset → Verify deletion
├─ Step 2: Assess model impact
│  ├─ Low impact + low sensitivity → Document, monitor
│  ├─ Moderate impact → Apply approximate unlearning (gradient-based)
│  └─ High impact or high sensitivity → Schedule full retraining
├─ Step 3: Verify unlearning effectiveness
│  ├─ Membership inference test on deleted records
│  ├─ Extraction test for deleted content
│  └─ Statistical comparison with retrained model
├─ Step 4: Document in model version history
└─ END: Respond to data subject with actions taken
```

## Workflow 3: Model Decommission

```
START: Model retired from production
│
├─ Step 1: Remove model from all deployment endpoints
├─ Step 2: Delete model artefacts (weights, checkpoints, embeddings)
├─ Step 3: Delete remaining training data (if not already deleted)
├─ Step 4: Delete inference logs beyond legal retention period
├─ Step 5: Retain compliance documentation (DPIA, audit reports, model cards)
├─ Step 6: Update AI system register
└─ END: Model fully decommissioned
```
