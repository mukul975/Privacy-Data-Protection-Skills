# Workflows — Managing Consent for Research

## Workflow 1: Research Consent Collection

```
START: User encounters research consent option in CloudVault SaaS Inc.
  │
  ├─► Displayed in Preference Center under "Research Participation":
  │     ├─ Toggle: "Participate in CloudVault Research Program"
  │     ├─ Short description: "Allow your pseudonymized usage data to be
  │     │   used for scientific research into cloud storage optimization."
  │     └─ "Learn More" expander with full details:
  │           ├─ Research areas covered
  │           ├─ What data is used (and what is NOT used)
  │           ├─ Pseudonymization method
  │           ├─ Who conducts the research
  │           ├─ Where results are published
  │           ├─ Ethics committee oversight
  │           └─ Withdrawal rights and implications
  │
  ├─► User toggles ON → Record broad consent:
  │     ├─ Purpose: "scientific_research_cloud_storage"
  │     ├─ Scope: "Cloud storage optimization, file system design, data management"
  │     ├─ Consent type: "broad_consent_recital_33"
  │     ├─ Standard consent record fields (timestamp, version, mechanism, etc.)
  │     └─ Research-specific fields:
  │           ├─ Ethics committee reference: "CREC-2025-001"
  │           ├─ Pseudonymization confirmed: true
  │           └─ Research partner: "Trinity College Dublin"
  │
  └─► Confirmation: "Thank you for supporting research. Your data will be
        pseudonymized before any research use. You can withdraw at any time."
```

## Workflow 2: New Research Project Review

```
TRIGGER: Researcher proposes new study using CloudVault user data
  │
  ├─► Step 1: Check if study falls within broad consent scope
  │     ├─ Original consent area: "cloud storage optimization, file system design,
  │     │   data management"
  │     │
  │     ├─► Assessment:
  │     │     ├─ Study: "Impact of file deduplication algorithms on user storage efficiency"
  │     │     ├─ Area: Cloud storage optimization ✓
  │     │     ├─ Data needed: File metadata, storage patterns (subset of consented categories) ✓
  │     │     └─ Determination: WITHIN SCOPE of broad consent
  │     │
  │     └─► If outside scope: Route to new consent collection workflow
  │
  ├─► Step 2: Ethics committee review
  │     ├─ Submit: research proposal, data requirements, methodology
  │     ├─ Committee reviews per Recital 33 ethical standards
  │     ├─ Decision: APPROVED (ref: CREC-2026-007)
  │     └─ Conditions: Must use k-anonymity with k>=10 for any published statistics
  │
  ├─► Step 3: DPO review and DPIA
  │     ├─ Lawful basis: Broad consent (Recital 33) + Art. 89(1) safeguards
  │     ├─ DPIA: Required (large-scale processing, pseudonymized data)
  │     ├─ Risk assessment: LOW (pseudonymized, internal research team)
  │     └─ DPO sign-off: APPROVED
  │
  ├─► Step 4: Data preparation
  │     ├─ Extract relevant data from production database
  │     ├─ Apply pseudonymization (replace user IDs with research pseudonyms)
  │     ├─ Remove unnecessary fields (data minimization)
  │     ├─ Transfer to isolated research environment
  │     └─ Log data extraction in audit trail
  │
  └─► Step 5: Ongoing monitoring
        ├─ Quarterly access audit
        ├─ Annual ethics committee re-review
        └─ Publication review for re-identification risk before submission
```

## Workflow 3: Consent Withdrawal for Research

```
TRIGGER: User withdraws research consent via Preference Center
  │
  ├─► Step 1: Record withdrawal in consent system
  │     └─ Standard withdrawal process (see implementing-consent-withdrawal skill)
  │
  ├─► Step 2: Determine impact on active research
  │     ├─ Query active research projects using this user's data
  │     ├─ For each active project:
  │     │   ├─ Can the user's data be identified in the research dataset?
  │     │   │   (if fully anonymized/aggregated, may not be identifiable)
  │     │   ├─ Has the research already produced results using this data?
  │     │   └─ What is the impact of removing this user's data?
  │     │
  │     └─ Note: Article 17(3)(d) provides an exemption from erasure for
  │           research where erasure would render impossible or seriously
  │           impair the research objectives
  │
  ├─► Step 3: Apply withdrawal
  │     ├─ Exclude user's data from all FUTURE research processing
  │     ├─ For ongoing studies where data has not yet been analyzed:
  │     │   └─ Remove user's pseudonymized data from research dataset
  │     ├─ For completed studies where results are published:
  │     │   └─ Data cannot be retroactively removed from aggregated/anonymized results
  │     │       (Art. 89(2) derogation may apply per Member State law)
  │     └─ Log all actions in audit trail
  │
  └─► Step 4: Confirm to user
        "Your research participation has ended. Your data will be excluded
         from future research. Research already completed using aggregated
         data is not affected per GDPR Article 89(2) and Recital 33."
```
