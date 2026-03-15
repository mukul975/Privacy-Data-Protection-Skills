# AI Data Subject Rights Workflows

## Workflow 1: AI Rights Request Processing

```
START: Rights request received involving AI processing
│
├─ Step 1: Identify and classify request
│  ├─ Access (Art. 15) — training data, inference records, or logic explanation
│  ├─ Rectification (Art. 16) — training data or output correction
│  ├─ Erasure (Art. 17) — training data deletion, model unlearning
│  ├─ Restriction (Art. 18) — quarantine from AI pipeline
│  ├─ Portability (Art. 20) — training data or profile in machine-readable format
│  ├─ Objection (Art. 21) — cease AI training or profiling
│  ├─ Automated decision (Art. 22) — human review, contestation, explanation
│  └─ Explanation (Art. 86 AI Act) — role of AI in specific decision
│
├─ Step 2: Verify identity and locate data
│  ├─ Verify data subject identity
│  ├─ Search training data catalogue for data subject records
│  ├─ Search inference logs for AI decisions affecting data subject
│  └─ Identify all AI systems that processed data subject's data
│
├─ Step 3: Process request
│  ├─ Access: compile training data contribution, inference records, generate explanation
│  ├─ Rectification: correct data, assess retraining need, correct outputs
│  ├─ Erasure: remove from training data, assess model unlearning, purge logs
│  ├─ Objection: cease training on data, remove from pipeline
│  ├─ Explanation: generate SHAP/LIME analysis or system-level explanation
│  └─ Contestation: assign to independent reviewer (see ai-automated-decisions)
│
├─ Step 4: ML engineering action (if needed)
│  ├─ Rectification requiring retraining → schedule retraining
│  ├─ Erasure requiring unlearning → execute machine unlearning or flag for retraining
│  ├─ Objection → exclude from training pipeline
│  └─ Document technical actions and timeline
│
├─ Step 5: Respond to data subject
│  ├─ Within Art. 12 timeframe (one month, extendable by two with notice)
│  ├─ Provide: action taken, data if access, explanation if requested
│  ├─ If unable to fully comply: explain reasons and data subject's further options
│  └─ Record in rights exercise register
│
└─ END: Close request. Monitor for follow-up.
```

## Workflow 2: AI Erasure and Machine Unlearning

```
START: Erasure request for data in AI training set
│
├─ Step 1: Remove data from training dataset
│  ├─ Locate and delete records from training data store
│  ├─ Verify deletion from all copies and backups
│  └─ Update training data catalogue
│
├─ Step 2: Assess model impact
│  ├─ Was the data subject's data a significant portion of training data?
│  ├─ Is the current model likely to reproduce/memorize the deleted data?
│  └─ Run membership inference test on the data subject's records
│
├─ Step 3: Model remediation
│  ├─ If low impact: document assessment, monitor for leakage
│  ├─ If moderate impact: apply machine unlearning technique
│  │  ├─ SISA (Sharded, Isolated, Sliced, Aggregated) training
│  │  ├─ Gradient-based unlearning
│  │  └─ Fine-tuning with gradient ascent on deleted data
│  ├─ If high impact or unlearning not feasible: schedule full model retraining
│  └─ Document: remediation approach and timeline
│
├─ Step 4: Verify erasure effectiveness
│  ├─ Re-run membership inference on deleted records
│  ├─ Test for extraction of deleted data
│  ├─ Confirm data subject's records are no longer reproducible
│  └─ Document: verification results
│
└─ Step 5: Respond to data subject
   ├─ Confirm deletion from training data
   ├─ Explain model remediation approach and timeline
   ├─ If full erasure from model not immediately possible: communicate timeline
   └─ Record in rights register
```
