# Workflows — State Law Applicability Assessment

## Workflow 1: Comprehensive Applicability Assessment

```
START: Organization needs to determine which state privacy laws apply
  │
  ├─► Step 1: Gather Organization Data
  │     ├─ Annual gross revenue
  │     ├─ NAICS code (for Texas SBA determination)
  │     ├─ Employee count
  │     ├─ Entity type (for-profit, nonprofit, government, financial, healthcare)
  │     ├─ Federal regulatory status (GLBA, HIPAA, FERPA coverage)
  │     └─ Consumer count per state (from data inventory)
  │
  ├─► Step 2: Entity Exemption Check (per state)
  │     ├─ Government entity? → Exempt in VA, CO, CT, TX, OR, MT, KY
  │     ├─ GLBA institution? → Entity exempt in VA, CO, CT, TX, OR, MT, KY; data exempt in CA
  │     ├─ HIPAA covered? → Entity exempt in VA, CO, CT, TX, OR, MT, KY; data exempt in CA
  │     ├─ Nonprofit? → Exempt in VA, CO, CT, TX, MT, KY; NOT exempt in OR, CA
  │     ├─ Higher ed? → Exempt in VA, CO, CT, TX, MT, KY
  │     └─ Air carrier? → Exempt only in MT
  │
  ├─► Step 3: Threshold Assessment (per state)
  │     ├─ California: Check revenue ($25M), consumer count (100K), revenue % (50%)
  │     ├─ Virginia: Check consumer count (100K) or (25K + 50% revenue)
  │     ├─ Colorado: Check consumer count (100K) or (25K + any revenue from sale)
  │     ├─ Connecticut: Check consumer count (100K excl. payment) or (25K + 25% revenue)
  │     ├─ Texas: Check SBA small business status (exempt if small)
  │     ├─ Oregon: Check consumer count (100K excl. payment) or (25K + 25% revenue)
  │     ├─ Montana: Check consumer count (50K excl. payment) or (25K + 25% revenue)
  │     └─ Kentucky: Check consumer count (100K) or (25K + 50% revenue)
  │
  ├─► Step 4: SBA Small Business Determination (Texas only)
  │     ├─ Identify NAICS code
  │     ├─ Look up SBA threshold in 13 CFR §121.201
  │     ├─ Compare annual receipts to threshold
  │     ├─ If small business: Most TDPSA exempt (sensitive data sale prohibition remains)
  │     └─ If not small business: Full TDPSA applies
  │
  ├─► Step 5: Data-Level Exemption Assessment
  │     ├─ Identify data categories governed by GLBA, HIPAA, FERPA, FCRA, DPPA, COPPA
  │     ├─ For California: Exempt data but entity remains subject for non-exempt data
  │     └─ For other states: Entity-level exemption covers all data if applicable
  │
  ├─► Step 6: Employee Data Assessment
  │     ├─ California: Employee data fully covered
  │     ├─ Oregon: Partial exemption (rights exempt, duties apply)
  │     └─ Other states: Consumer rights exempt, controller duties apply
  │
  └─► Step 7: Document and Report
        ├─ Generate applicability matrix
        ├─ Document basis for each determination
        ├─ Identify monitoring states (below threshold but growing)
        └─ Schedule annual re-assessment
```

## Workflow 2: Annual Re-Assessment

```
TRIGGER: January 1 each year (assess based on prior calendar year data)
  │
  ├─► Step 1: Update Consumer Counts
  │     ├─ Pull consumer counts per state from data inventory
  │     ├─ Note: Some states exclude payment-only (CT, OR, MT)
  │     └─ Identify states where counts have changed significantly
  │
  ├─► Step 2: Update Revenue Data
  │     ├─ Total annual gross revenue
  │     ├─ Revenue from sale/sharing of personal data
  │     ├─ Revenue percentage calculation
  │     └─ SBA threshold comparison (for Texas)
  │
  ├─► Step 3: Check for New Laws
  │     ├─ Review newly enacted state privacy laws
  │     ├─ Add new states to assessment matrix
  │     └─ Review amendments to existing laws
  │
  ├─► Step 4: Run Assessment Tool
  │     ├─ Input updated data into process.py assessment engine
  │     ├─ Generate updated applicability report
  │     └─ Compare with prior year's determination
  │
  └─► Step 5: Action Items
        ├─ If newly applicable: activate compliance program for that state
        ├─ If no longer applicable: maintain as best practice or deactivate
        └─ Update privacy notice and state-specific disclosures
```
