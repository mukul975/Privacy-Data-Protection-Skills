# RoPA-DPIA Linkage Workflow Reference

## Linkage Establishment Workflow

### When Creating a New RoPA Entry

1. Complete all seven Art. 30(1) fields for the new processing activity.
2. Apply the DPIA necessity assessment checklist (9 WP29 criteria + Art. 35(3) triggers).
3. If two or more criteria are met, or any Art. 35(3) trigger applies:
   - Set `dpia_required = true` in the RoPA entry.
   - Initiate the DPIA process before processing commences.
   - Assign a DPIA reference ID following the naming convention.
   - Link the RoPA entry to the DPIA via the reference ID.
4. If DPIA is not required:
   - Set `dpia_required = false` in the RoPA entry.
   - Document the reasoning (which criteria were assessed and why they do not apply).
5. Document the lawful basis assessment reference in the RoPA entry.

### When Conducting a New DPIA

1. Identify the RoPA entry (or entries) that the DPIA covers.
2. Reference the RoPA entry ID(s) in the DPIA document.
3. Use the RoPA entry's Art. 30(1) fields as the foundation for the DPIA's processing description (Art. 35(7)(a)):
   - Purposes from Art. 30(1)(b)
   - Data categories from Art. 30(1)(c)
   - Recipients from Art. 30(1)(d)
   - Transfers from Art. 30(1)(e)
   - Retention from Art. 30(1)(f)
   - Current security measures from Art. 30(1)(g)
4. After DPIA approval, update the RoPA entry with the DPIA reference, approval date, and next review date.

## Change Cascade Workflow

### RoPA Change Triggers DPIA Review

```
RoPA Entry Updated
    │
    ├── Check: Is dpia_required = true?
    │   ├── Yes
    │   │   ├── Which field changed?
    │   │   │   ├── Purpose (Art. 30(1)(b)) → DPIA review: necessity and proportionality
    │   │   │   ├── Data categories (Art. 30(1)(c)) → DPIA review: risk assessment
    │   │   │   ├── Recipients (Art. 30(1)(d)) → DPIA review: data sharing risks
    │   │   │   ├── Transfers (Art. 30(1)(e)) → DPIA review: transfer risks
    │   │   │   ├── Retention (Art. 30(1)(f)) → DPIA review: proportionality
    │   │   │   └── Security (Art. 30(1)(g)) → DPIA review: risk mitigation measures
    │   │   │
    │   │   └── Create DPIA review task assigned to DPO
    │   │
    │   └── No
    │       └── Re-assess: Does the change now make the processing high-risk?
    │           ├── Yes → Set dpia_required = true, initiate DPIA
    │           └── No → No action
    │
    └── Check: Does change affect lawful basis?
        ├── Yes → Flag lawful basis assessment for review
        └── No → No action
```

### DPIA Outcome Triggers RoPA Update

```
DPIA Completed/Updated
    │
    ├── New risk mitigation measures recommended?
    │   └── Yes → Update RoPA Art. 30(1)(g) security measures
    │
    ├── Processing scope restricted?
    │   └── Yes → Update RoPA Art. 30(1)(b) purposes and/or Art. 30(1)(c) categories
    │
    ├── Retention reduced?
    │   └── Yes → Update RoPA Art. 30(1)(f) retention periods
    │
    ├── Additional transfer safeguards required?
    │   └── Yes → Update RoPA Art. 30(1)(e) transfer mechanisms
    │
    ├── Processing prohibited (residual risk too high)?
    │   └── Yes → Archive RoPA entry (processing must not proceed)
    │
    └── Prior consultation required (Art. 36)?
        └── Yes → Flag RoPA entry as "Pending prior consultation"
            └── Processing must not commence until SA response received
```

## Periodic Review Workflow

### Quarterly Linkage Integrity Check

1. Export RoPA register and DPIA register.
2. For each RoPA entry where `dpia_required = true`:
   - Verify DPIA reference exists in DPIA register.
   - Verify DPIA status is "Approved" (not "Draft," "Expired," or "Rejected").
   - Verify DPIA review date has not passed.
3. For each DPIA in the register:
   - Verify linked RoPA entry exists and is active.
   - Verify RoPA entry has not changed since DPIA was last reviewed.
4. Flag discrepancies for DPO resolution.

### Annual DPIA Necessity Re-Assessment

1. For each RoPA entry where `dpia_required = false`:
   - Re-apply the DPIA necessity checklist.
   - Check against updated SA blacklists (which may have been expanded).
   - If circumstances have changed (new technology, increased scale, new data categories), the assessment may now require a DPIA.
2. For each existing DPIA:
   - Conduct the Art. 35(11) review: is processing still performed in accordance with the DPIA?
   - Has the risk profile changed since the DPIA was approved?
   - Are the risk mitigation measures still in place and effective?

## RACI Matrix

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|----------|
| DPIA necessity assessment for new RoPA entry | Privacy analyst | DPO | Processing owner | Legal |
| DPIA conduct | DPO / Privacy team | DPO | Processing owner, IT, Legal | Senior management |
| Cross-reference creation | Privacy analyst | DPO | — | Processing owner |
| Cascade trigger detection | Automated + Privacy analyst | DPO | — | Processing owner |
| Cascade action execution | DPO + Privacy analyst | DPO | Processing owner | Legal |
| Quarterly integrity check | Privacy analyst | DPO | — | Steering committee |
| Annual re-assessment | DPO | DPO | Processing owners, Legal | Board |
