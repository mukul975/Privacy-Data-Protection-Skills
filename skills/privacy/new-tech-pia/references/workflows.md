# New Technology Privacy Impact Assessment Workflows

## Workflow 1: Technology Screening and Classification

```
START: New technology identified for deployment or procurement
│
├─ Step 1: Does the technology process personal data?
│  ├─ NO → No PIA required. Document screening outcome.
│  └─ YES → Continue.
│
├─ Step 2: Is the technology novel or innovative?
│  (Novel means: not yet widely deployed, uses new data collection methods,
│  applies existing technology in a new context, or combines technologies
│  in a new way)
│  ├─ YES → Innovative technology criterion (WP248 C8) met.
│  └─ NO → Standard DPIA screening applies.
│
├─ Step 3: Count additional WP248 criteria met:
│  □ C1: Evaluation or scoring
│  □ C2: Automated decision-making with significant effect
│  □ C3: Systematic monitoring
│  □ C4: Sensitive or highly personal data
│  □ C5: Large-scale processing
│  □ C6: Matching or combining datasets
│  □ C7: Vulnerable data subjects
│  □ C9: Processing preventing exercise of rights
│
├─ If C8 (innovative technology) + any one other criterion → DPIA required.
│
└─ Proceed to full new technology PIA (Workflow 2).
```

## Workflow 2: Full New Technology PIA Process

### Phase 1: Technology Deep Dive (Days 1-7)
1. Obtain technical documentation from the vendor or development team.
2. Map all personal data processing across the technology lifecycle:
   - What data is collected (all sensors, inputs, metadata)
   - How data travels (device to cloud, device to device, cloud to cloud)
   - Where data is stored (geographies, infrastructure)
   - Who accesses data (vendor, controller, processors, third parties)
   - How long data is retained
   - How data is protected at each stage
3. Identify technology-specific privacy risks (see risk profiles above).
4. Check for applicable regulatory guidance specific to this technology.

### Phase 2: Stakeholder and Impact Analysis (Days 8-14)
1. Map all affected stakeholder groups.
2. For each group, assess:
   - Awareness of data collection
   - Ability to exercise data subject rights
   - Power imbalance with the controller
   - Potential for physical, material, or non-material harm
3. Assess disproportionate impact on vulnerable groups.
4. Seek data subject views where appropriate per Art. 35(9).

### Phase 3: Proportionality and Alternatives (Days 15-21)
1. Document necessity of each data processing element.
2. Evaluate less invasive alternatives:
   - Can the purpose be achieved without this technology?
   - Can the technology function with less personal data?
   - Can privacy-enhancing technologies reduce the privacy impact?
3. Conduct proportionality balancing test.

### Phase 4: Risk Assessment (Days 22-28)
1. For each technology-specific risk, assess likelihood and severity.
2. Identify mitigation measures.
3. Calculate residual risk.
4. If residual risk remains high, assess whether deployment should proceed.

### Phase 5: Approval and Monitoring (Days 29-35)
1. DPO review and advice.
2. Senior management approval.
3. Establish monitoring framework.
4. Schedule review (minimum 6 months for new technology, accelerated from standard annual review).

## Workflow 3: Technology-Specific Risk Assessment Decision Trees

### IoT Risk Assessment
```
IoT Device Deployment
├─ Does the device have a user interface?
│  ├─ YES → Standard privacy notice and consent mechanisms.
│  └─ NO → Alternative transparency measures required (audio, LED indicator, companion app).
│
├─ Does the device communicate with cloud services?
│  ├─ YES → Assess cloud processor under Art. 28. Assess international transfers.
│  └─ NO → Local processing only — reduced risk.
│
├─ Does the device collect data about non-users?
│  ├─ YES → Art. 14 obligation for data not obtained from data subject. May require DPIA.
│  └─ NO → Continue standard assessment.
│
├─ Can the device be updated remotely?
│  ├─ YES → Assess firmware update security.
│  └─ NO → Increased long-term vulnerability risk. Flag for enhanced security review.
│
└─ Does the device process biometric or health data?
   ├─ YES → Art. 9 special category processing. Art. 35(3)(b) DPIA trigger.
   └─ NO → Standard risk assessment.
```

### Blockchain Risk Assessment
```
Blockchain Implementation
├─ Is personal data stored on-chain?
│  ├─ YES → Assess Art. 17 right to erasure compliance. Likely requires redesign.
│  └─ NO → Off-chain storage with on-chain hash is preferred.
│
├─ Is the blockchain public or permissioned?
│  ├─ PUBLIC → All transaction data visible to all participants.
│  │  Assess: Can transaction patterns reveal personal information?
│  └─ PERMISSIONED → Access controls possible. Reduced transparency risk.
│
├─ Are smart contracts making decisions about individuals?
│  ├─ YES → Assess Art. 22 automated decision-making.
│  └─ NO → Continue standard assessment.
│
└─ Are nodes located in multiple countries?
   ├─ YES → Chapter V international transfer assessment for each jurisdiction.
   └─ NO → Single jurisdiction — standard transfer assessment if outside EEA.
```
