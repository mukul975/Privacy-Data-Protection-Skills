# Transfer Impact Assessment Workflows

## Workflow 1: TIA Initiation and Transfer Mapping

### Trigger Events
- New international transfer of personal data identified
- New processor or sub-processor located in a third country
- Change of data hosting location to a third country
- Acquisition of SaaS tool with third-country data processing
- Expiry or invalidation of existing transfer mechanism (e.g., adequacy decision withdrawal)
- Periodic re-evaluation schedule reached (annual minimum)

### Process
1. Data exporter identifies the transfer and notifies the DPO.
2. DPO opens a TIA case in the transfer register (reference: TIA-[ORG]-[YEAR]-[SEQ]).
3. Data exporter completes the transfer mapping form documenting all transfer attributes.
4. DPO validates the mapping against actual data flows (verified with IT and procurement).
5. DPO identifies the Chapter V transfer mechanism in use or to be used.

## Workflow 2: Third Country Legal Framework Assessment

### Information Gathering
1. Review the destination country's constitution for privacy and data protection provisions.
2. Review the destination country's data protection legislation and implementing regulations.
3. Review the destination country's surveillance and law enforcement access legislation.
4. Consult EDPB Recommendations 02/2020 European Essential Guarantees checklist.
5. Review published transparency reports from the data importer and comparable entities in the destination country.
6. Consult external legal opinions on the destination country's legal framework (law firm memoranda, academic analyses).
7. Check CoE Convention 108+ ratification status for the destination country.
8. Review any existing EDPB or Commission assessments of the destination country.

### European Essential Guarantees Assessment

```
For each of the four essential guarantees, assess the third country:

1. CLEAR, PRECISE, AND ACCESSIBLE RULES
   ├─ Are surveillance powers defined by publicly available law?
   ├─ Are the conditions for exercising powers clearly defined?
   ├─ Is the scope of surveillance clearly limited (targeted vs bulk)?
   └─ Score: [1-5]

2. NECESSITY AND PROPORTIONALITY
   ├─ Is access limited to what is strictly necessary?
   ├─ Are there safeguards against bulk/indiscriminate access?
   ├─ Is there a requirement to use least intrusive means?
   └─ Score: [1-5]

3. INDEPENDENT OVERSIGHT
   ├─ Is prior authorisation required from an independent body?
   ├─ Is the oversight body independent from the executive?
   ├─ Does the oversight body have power to halt or restrict surveillance?
   └─ Score: [1-5]

4. EFFECTIVE REMEDIES
   ├─ Can data subjects (including foreign nationals) challenge surveillance?
   ├─ Is the remedy body independent from the executive?
   ├─ Can the body provide binding relief (e.g., order deletion)?
   └─ Score: [1-5]
```

## Workflow 3: Supplementary Measures Selection

### Decision Tree

```
START: Third country assessment completed
│
├─ Overall TIA risk level: Low (score 1.0-2.0)?
│  └─ Standard transfer tool sufficient. Document and proceed.
│
├─ Overall TIA risk level: Medium (score 2.1-3.0)?
│  ├─ Can contractual supplementary measures address identified gaps?
│  │  ├─ YES → Implement contractual measures. Proceed.
│  │  └─ NO → Add technical supplementary measures. Proceed.
│  └─ Document supplementary measures and proceed.
│
├─ Overall TIA risk level: High (score 3.1-4.0)?
│  ├─ Can end-to-end encryption with exporter-held key be implemented?
│  │  ├─ YES → Implement. Proceed with monitoring.
│  │  └─ NO → Can pseudonymisation with exporter-held mapping be implemented?
│  │     ├─ YES → Implement. Proceed with monitoring.
│  │     └─ NO → Can split processing across jurisdictions be implemented?
│  │        ├─ YES → Implement. Proceed with monitoring.
│  │        └─ NO → Transfer cannot proceed. Explore alternatives.
│  └─ Document all measures and proceed with enhanced monitoring.
│
├─ Overall TIA risk level: Very High (score 4.1-5.0)?
│  ├─ Can the transfer be avoided entirely (EEA-only processing)?
│  │  ├─ YES → Process data within EEA. No transfer required.
│  │  └─ NO → Can end-to-end encryption with exporter-held key be implemented
│  │     AND importer has no access to clear text data?
│  │     ├─ YES → Implement. Proceed with enhanced monitoring.
│  │     └─ NO → Transfer must not proceed. No supplementary measures
│  │        can ensure essentially equivalent protection.
│  └─ Document decision and escalate to senior management.
│
└─ END: Document the supplementary measures decision and rationale.
```

## Workflow 4: TIA Documentation and Approval

1. DPO compiles the TIA report including:
   - Transfer mapping (Step 1)
   - Transfer mechanism identification (Step 2)
   - Third country legal framework assessment (Step 3)
   - Supplementary measures (Step 4)
   - Implementation plan (Step 5)
   - Re-evaluation schedule (Step 6)
2. Legal counsel reviews the TIA for legal accuracy.
3. IT security reviews the technical supplementary measures for feasibility.
4. DPO approves or rejects the transfer.
5. If approved, transfer proceeds with documented supplementary measures and monitoring schedule.
6. TIA is registered in the central TIA register.
7. SCC Clause 14 assessment is documented and available for supervisory authority request.

## Workflow 5: Ongoing Monitoring and Re-evaluation

### Monitoring Activities
1. Subscribe to legislative monitoring service for destination country surveillance law changes.
2. Review quarterly transparency reports from data importers.
3. Monitor EDPB and national SA guidance and enforcement decisions.
4. Track adequacy decision developments (adoptions, reviews, invalidations).

### Re-evaluation Triggers
- New surveillance legislation enacted in destination country
- Court decision affecting government access powers
- Adequacy decision adopted, reviewed, or withdrawn
- Data importer received government access request affecting transferred data
- Breach involving transferred data
- Material change in processing scope, data categories, or importer operations
- Annual re-evaluation date reached

### Re-evaluation Process
1. Update the third country legal framework assessment.
2. Reassess whether existing supplementary measures remain effective.
3. If supplementary measures are no longer sufficient, implement additional measures or suspend transfers.
4. Document the re-evaluation outcome and update the TIA register.
5. If transfers are suspended, notify affected business units and identify EEA alternatives.
