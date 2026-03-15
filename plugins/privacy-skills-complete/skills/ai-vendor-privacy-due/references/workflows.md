# AI Vendor Privacy Due Diligence Workflows

## Workflow 1: Controller-Processor Determination

```
START: Engaging AI vendor for processing personal data
│
├─ Does the vendor determine why data is processed (purpose)?
│  ├─ YES → Vendor is likely a controller or joint controller
│  └─ NO → Continue assessment
│
├─ Does the vendor use data for its own purposes (model training, analytics)?
│  ├─ YES → Vendor is controller for those purposes
│  │  ├─ Both parties determine purposes → Art. 26 joint controllers
│  │  └─ Vendor has independent purpose → Separate controllers
│  └─ NO → Continue assessment
│
├─ Does the vendor retain data beyond service delivery?
│  ├─ YES for own purposes → Controller for retained data
│  ├─ YES on customer instruction → Processor with documented retention
│  └─ NO → Continue assessment
│
├─ Does the vendor make independent processing decisions?
│  ├─ YES → At minimum joint controller for those decisions
│  └─ NO → Vendor acts solely on instructions → Processor
│
└─ DETERMINATION:
   ├─ Processor → Execute Art. 28 DPA
   ├─ Joint Controller → Execute Art. 26 JCA
   └─ Independent Controller → Separate controller transparency + legal basis
```

## Workflow 2: AI Vendor Due Diligence

```
START: AI vendor evaluation
│
├─ Step 1: Information gathering
│  ├─ Request vendor AI processing documentation
│  ├─ Complete vendor privacy questionnaire
│  ├─ Review vendor privacy notice, DPA terms, sub-processor list
│  └─ Assess vendor certifications (ISO 27001, SOC 2)
│
├─ Step 2: AI-specific assessment
│  ├─ Does vendor train on customer data? → Document scope and opt-out
│  ├─ What are vendor's data retention practices? → Compare against policy
│  ├─ Where is AI processing performed? → International transfer assessment
│  ├─ What sub-processors are used? → Review sub-processor chain
│  ├─ Does vendor conduct model privacy testing? → Request evidence
│  └─ Does vendor conduct bias assessment? → Request evidence for high-risk
│
├─ Step 3: Risk scoring
│  ├─ Data sensitivity × vendor risk factors = overall risk
│  ├─ High risk → Enhanced due diligence, audit rights, annual review
│  ├─ Medium risk → Standard due diligence, periodic review
│  └─ Low risk → Standard controls
│
├─ Step 4: Contractual negotiation
│  ├─ Insert AI-specific clauses (training restrictions, accuracy, bias)
│  ├─ Ensure audit rights and breach notification
│  ├─ Document data deletion on termination
│  └─ Execute Art. 28 DPA or Art. 26 JCA
│
└─ Step 5: Ongoing management
   ├─ Annual vendor review
   ├─ Monitor sub-processor changes
   ├─ Review vendor incident reports
   └─ Re-assess on material change
```
