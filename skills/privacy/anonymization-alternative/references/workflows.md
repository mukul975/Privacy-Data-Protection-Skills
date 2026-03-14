# Anonymization as Retention Alternative Workflows

## Workflow 1: Anonymization Decision

```
[Data Approaching Retention Expiry]
         │
         ▼
[Is There a Legitimate Purpose for Anonymized Retention?]
   ├── Statistical analysis / reporting ──► Proceed
   ├── Research purposes (Art. 89) ──► Proceed
   ├── ML model training ──► Proceed (with separate legal basis review)
   ├── Historical archiving ──► Proceed
   └── No legitimate purpose ──► DELETE (do not anonymize without reason)
         │
         ▼
[Can the Purpose be Achieved with Anonymized Data?]
   ├── Yes ──► Proceed to anonymization
   └── No ──► Consider pseudonymization with extended retention (separate assessment)
         │
         ▼
[Select Anonymization Technique]
   - Based on data type and intended use
   - Document technique selection rationale
         │
         ▼
[Proceed to Anonymization Pipeline]
```

## Workflow 2: Anonymization Pipeline Execution

```
[Anonymization Approved]
         │
         ▼
[Step 1: Identifier Removal]
   - Remove all direct identifiers
   - Remove unique cross-referencing IDs
         │
         ▼
[Step 2: Quasi-Identifier Generalization]
   - Age → bands; Postcode → outward code
   - Dates → month-year; Job title → function
         │
         ▼
[Step 3: K-Anonymity]
   - Ensure each quasi-identifier combination appears in ≥ k records
   - Suppress records that cannot achieve k threshold
         │
         ▼
[Step 4: L-Diversity (if sensitive attributes)]
   - ≥ l distinct values per sensitive attribute per equivalence class
         │
         ▼
[Step 5: Noise Addition (numerical attributes)]
   - Calibrated noise (Laplace mechanism)
   - Epsilon ≤ 1.0 (standard) / ≤ 0.1 (sensitive)
         │
         ▼
[Step 6: Validation]
   ├── Singling out test ──► < 5% probability
   ├── Linkability test ──► No successful linkage in sample
   ├── Inference test ──► No attribute inferred > 80% confidence
   └── Motivated intruder test ──► Cannot identify with reasonable effort
         │
         ▼
[Validation Passed?]
   ├── Yes ──► Approve anonymized dataset
   └── No ──► Iterate with stronger parameters
         │
         ▼
[Delete Source Personal Data]
[Register Anonymized Dataset]
[Retain Anonymized Data Without Retention Constraint]
```

## Workflow 3: Annual Re-Identification Risk Review

```
[Annual Review Trigger]
         │
         ▼
[For Each Registered Anonymized Dataset]
   │
   ├── [New external data sources available that could enable linkage?]
   │     ├── Yes ──► Re-run linkability test
   │     └── No ──► Continue
   │
   ├── [Technology advances affecting re-identification risk?]
   │     ├── Yes ──► Re-run full validation suite
   │     └── No ──► Continue
   │
   └── [Population/context changes affecting uniqueness?]
         ├── Yes ──► Re-run singling out test
         └── No ──► Continue
         │
         ▼
[Re-Identification Risk Still Acceptable?]
   ├── Yes ──► Confirm — dataset remains anonymized
   └── No ──► Apply additional techniques OR treat as personal data
         │
         ▼
[Update Anonymization Register]
```
