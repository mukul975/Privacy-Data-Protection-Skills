# Biometric Processing Privacy Assessment Workflows

## Workflow 1: Biometric Processing Classification

```
START: Biometric processing identified
│
├─ Step 1: Is this biometric data under Art. 4(14)?
│  ├─ Data results from specific technical processing relating to physical,
│  │  physiological, or behavioural characteristics?
│  │  ├─ YES → Continue.
│  │  └─ NO → Not biometric data under GDPR. Standard assessment applies.
│  └─ Does the processing allow or confirm unique identification?
│     ├─ YES → Art. 9 special category data. Continue to Step 2.
│     └─ NO → Not Art. 9 data, but may still be high-risk. Assess under standard DPIA criteria.
│
├─ Step 2: Determine processing mode
│  ├─ Verification (1:1) — comparing live sample to claimed identity template?
│  ├─ Identification (1:N) — searching live sample against database?
│  └─ Categorisation — classifying without identifying?
│
├─ Step 3: Determine scale
│  ├─ Number of enrolled data subjects
│  ├─ Number of persons in capture area (for identification)
│  ├─ Geographic scope
│  └─ Duration of processing
│
├─ Step 4: DPIA trigger assessment
│  ├─ Art. 35(3)(b) — Large-scale special category processing?
│  │  ├─ YES → Mandatory DPIA.
│  │  └─ NO → Continue assessment.
│  ├─ Art. 35(3)(c) — Systematic monitoring of public area?
│  │  ├─ YES → Mandatory DPIA.
│  │  └─ NO → Continue EDPB criteria assessment.
│  └─ EDPB WP248 criteria met?
│     ├─ C4 (sensitive data) — always met for biometric processing
│     ├─ + any other criterion → DPIA required
│     └─ Document screening outcome.
│
└─ Proceed to full biometric DPIA (Workflow 2).
```

## Workflow 2: Biometric DPIA Execution

### Phase 1: Necessity and Proportionality (Critical Phase)
1. Document the specific purpose requiring biometric identification.
2. Evaluate non-biometric alternatives:
   - Card/badge access control
   - PIN/password authentication
   - Multi-factor authentication without biometrics
   - Security guard visual identification
3. For each alternative, assess:
   - Whether it achieves the same security level as biometric
   - Cost differential
   - User experience impact
4. If a non-biometric alternative achieves the purpose adequately, biometric processing is not proportionate and should not proceed.
5. If biometric processing is necessary, evaluate the least intrusive biometric option:
   - Verification (1:1) over identification (1:N)
   - On-device template over centralised database
   - Fingerprint over facial recognition (less ambient capture)
   - Voluntary enrollment over mandatory enrollment

### Phase 2: Art. 9(2) Exemption Identification
1. Identify the applicable Art. 9(2) exemption.
2. If relying on consent (Art. 9(2)(a)):
   - Must be explicit (not implied, not bundled)
   - Must be freely given (genuine alternative must be available)
   - In employment context: consent is presumptively not free (WP29 Opinion 2/2017)
   - Non-biometric alternative must be offered without penalty
3. If relying on employment law (Art. 9(2)(b)):
   - Identify the specific Member State law provision
   - Verify the law provides suitable safeguards
4. Document the exemption analysis.

### Phase 3: Technical Risk Assessment
1. Assess accuracy metrics:
   - FAR (False Acceptance Rate)
   - FRR (False Rejection Rate)
   - Demographic accuracy differential (NIST FRVT benchmarks for facial recognition)
2. Assess security:
   - Template protection method
   - Liveness detection capability
   - System penetration test results
3. Assess data minimisation:
   - Template vs raw biometric data storage
   - Retention periods
   - Deletion mechanisms

### Phase 4: Mitigation and Approval
1. Implement mitigation measures.
2. Assess residual risk.
3. DPO advice.
4. If residual risk remains high (biometric breach risk, discriminatory accuracy), Art. 36 prior consultation may be needed.

## Workflow 3: Biometric Data Breach Response

```
Biometric data breach detected
│
├─ Step 1: Contain the breach
│  ├─ Isolate affected biometric system.
│  ├─ Revoke compromised templates.
│  ├─ If centralised database compromised: assume all enrolled templates affected.
│  └─ Activate non-biometric fallback access mechanisms.
│
├─ Step 2: Assess severity (heightened for biometric data)
│  ├─ Biometric data is irreplaceable — breach severity is inherently high.
│  ├─ Were raw biometric images or only templates exposed?
│  ├─ Are templates protected (cancellable biometrics, encryption)?
│  ├─ Can exposed templates be used to reconstruct biometric characteristics?
│  └─ Number of affected data subjects.
│
├─ Step 3: Notification
│  ├─ Art. 33 supervisory authority notification: likely required (high risk to rights and freedoms).
│  ├─ Art. 34 data subject notification: likely required (biometric breach is high risk).
│  └─ Notify data subjects of:
│     ├─ What biometric data was compromised
│     ├─ That biometric data cannot be changed (unlike passwords)
│     ├─ Steps taken to mitigate
│     └─ Recommendations (monitor for identity fraud)
│
├─ Step 4: Remediation
│  ├─ If cancellable biometrics: generate new templates using different transformation parameters.
│  ├─ If standard templates: re-enrollment required with enhanced security.
│  ├─ If raw biometric images: permanent compromise — consider transitioning to different biometric modality.
│  └─ Update DPIA with breach findings.
│
└─ Step 5: DPIA Review
   └─ Mandatory DPIA review following biometric data breach.
```
