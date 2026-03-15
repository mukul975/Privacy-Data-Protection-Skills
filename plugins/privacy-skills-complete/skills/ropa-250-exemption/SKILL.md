---
name: ropa-250-exemption
description: >-
  Assesses the GDPR Article 30(5) exemption for organisations under 250
  employees. Covers the three exception conditions that negate the exemption:
  non-occasional processing, risk to data subject rights, and special category
  data processing. Activate for Art. 30(5), 250 employee exemption, small
  business RoPA, SME exemption, occasional processing.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: records-of-processing
  tags: "gdpr, ropa, article-30-5, exemption, sme, small-business, 250-employees, occasional"
---

# Art. 30(5) Exemption Assessment

## Overview

GDPR Article 30(5) provides a limited exemption from the RoPA obligation for organisations with fewer than 250 employees. However, this exemption is narrowly constructed and rarely available in practice. The exemption does not apply when any of three exception conditions are met: (1) the processing is likely to result in a risk to data subjects' rights and freedoms, (2) the processing is not occasional, or (3) the processing includes special category data under Art. 9(1) or criminal conviction data under Art. 10. Since virtually all organisations with regular employee or customer processing engage in non-occasional processing, the EDPB has recommended that all organisations maintain RoPA regardless of size.

## Art. 30(5) Text

> The obligations referred to in paragraphs 1 and 2 shall not apply to an enterprise or an organisation employing fewer than 250 persons **unless** the processing it carries out is likely to result in a risk to the rights and freedoms of data subjects, the processing is not occasional, or the processing includes special categories of data as referred to in Article 9(1) or personal data relating to criminal convictions and offences referred to in Article 10.

## Three Exception Conditions

The exemption is negated (RoPA is required) if **any one** of the following three conditions is met. They are disjunctive (OR), not conjunctive (AND).

### Exception 1: Processing Likely to Result in a Risk

**Test**: Does the processing carried out by the organisation result in any risk (not just high risk) to the rights and freedoms of data subjects?

**EDPB interpretation**: The EDPB Position Paper on Art. 30 (2018) interpreted this condition broadly. Unlike Art. 35 (DPIA), which requires "high risk," Art. 30(5) refers to "a risk" — a lower threshold. The EDPB concluded that virtually all processing of personal data involves some risk to data subjects, making this condition almost always met.

**Examples of processing that creates risk:**

| Processing Activity | Risk to Rights/Freedoms | Exemption Applies? |
|--------------------|------------------------|-------------------|
| Employee payroll | Financial data exposure risk; employment impact | No — risk exists |
| Customer database | Identity theft risk; unwanted marketing | No — risk exists |
| Website with login | Account compromise risk; privacy intrusion | No — risk exists |
| Email marketing | Unsolicited communication; profiling | No — risk exists |
| CCTV at workplace | Privacy intrusion; chilling effect | No — risk exists |
| Manual paper-only visitor log retained < 24 hours | Minimal risk | Potentially yes |

**Practical outcome**: This condition alone makes the exemption unavailable for most organisations. Only processing that involves genuinely negligible risk (such as a one-time, paper-only process with immediate destruction) might satisfy this condition.

### Exception 2: Processing Is Not Occasional

**Test**: Is the processing carried out on a regular or systematic basis, rather than being a one-time or infrequent occurrence?

**"Occasional" means**: One-time, infrequent, or ad hoc processing that is not part of the organisation's regular business operations. Examples might include a one-time market research survey conducted for a specific project with no repetition planned.

**"Not occasional" (regular) processing includes:**

| Processing Activity | Occasional? | Reasoning |
|--------------------|-------------|-----------|
| Monthly payroll | No — recurring | Systematic, monthly processing |
| Customer order processing | No — ongoing | Core business activity, continuous |
| Employee email system | No — continuous | Always-on processing |
| Website analytics | No — continuous | Ongoing data collection |
| Annual customer satisfaction survey | No — regular | Annually recurring; planned and systematic |
| One-time data migration project | Possibly yes | Single occurrence, defined end point |
| Ad hoc legal hold for single litigation | Possibly yes | One-time, specific trigger |

**EDPB guidance**: The EDPB stated that any organisation processing employee or customer personal data as part of its ongoing operations is engaged in non-occasional processing. This includes virtually all businesses that employ staff or serve customers.

**Practical outcome**: Any organisation with employees, customers, suppliers, or a website is engaged in non-occasional processing, negating the exemption.

### Exception 3: Special Category or Criminal Data

**Test**: Does the processing include any special category data under Art. 9(1) or criminal conviction data under Art. 10?

**Art. 9(1) special categories:**
- Racial or ethnic origin
- Political opinions
- Religious or philosophical beliefs
- Trade union membership
- Genetic data
- Biometric data for identification purposes
- Health data
- Data concerning sex life or sexual orientation

**Art. 10**: Personal data relating to criminal convictions and offences or related security measures.

**Common special category processing in small organisations:**

| Processing Activity | Special Category Data | Exemption Applies? |
|--------------------|----------------------|-------------------|
| Employee sick leave records | Health data (Art. 9(1)) | No |
| Church tax processing (Germany) | Religious beliefs (Art. 9(1)) | No |
| Background checks | Criminal data (Art. 10) | No |
| Biometric access control (fingerprint) | Biometric data (Art. 9(1)) | No |
| Diversity monitoring | Racial/ethnic origin (Art. 9(1)) | No |
| Employee emergency contacts with medical needs | Health data (Art. 9(1)) | No |
| Trade union membership deductions | Trade union membership (Art. 9(1)) | No |
| Employee photos on ID badges | Not biometric unless used for identification | Depends on use |

**Practical outcome**: Almost all organisations process at least health data (sick leave) or religious data (in countries with church tax), making this condition met for most employers.

## Exemption Assessment Flowchart

```
Does the organisation employ fewer than 250 persons?
│
├── No → Art. 30(5) exemption does NOT apply. Full RoPA required.
│
└── Yes → Assess three exception conditions:
    │
    ├── Condition 1: Is processing likely to result in a risk
    │   to data subjects' rights and freedoms?
    │   ├── Yes → Exemption does NOT apply for this processing.
    │   └── No → Continue to Condition 2
    │
    ├── Condition 2: Is the processing NOT occasional?
    │   (i.e., is it regular, recurring, or systematic?)
    │   ├── Yes (not occasional) → Exemption does NOT apply.
    │   └── No (truly occasional) → Continue to Condition 3
    │
    └── Condition 3: Does the processing include special
        category data (Art. 9(1)) or criminal data (Art. 10)?
        ├── Yes → Exemption does NOT apply.
        └── No → Exemption APPLIES for this specific processing
            activity. No RoPA entry required for this activity.
```

**Critical point**: The assessment is per processing activity, not per organisation. An organisation might have some processing activities that qualify for exemption and others that do not. In practice, the non-exempt activities (payroll, customer management, employee records) require a RoPA, and once you have a RoPA, you should document all processing for accountability purposes.

## Assessment for Helix Biotech Solutions (Hypothetical Small Entity Scenario)

Assume Helix Biotech Diagnostics S.A.S. (recently acquired French subsidiary) has only 45 employees. Can it claim the Art. 30(5) exemption?

### Employee Count Check

- Helix Biotech Diagnostics S.A.S.: 45 employees
- Threshold: fewer than 250 employees
- **Result**: Passes the employee count threshold.

### Exception Condition Assessment

| Processing Activity | Condition 1: Risk? | Condition 2: Not Occasional? | Condition 3: Special Category? | Exempt? |
|--------------------|--------------------|-----------------------------|-------------------------------|---------|
| Employee payroll | Yes — financial data risk | Yes — monthly | Yes — mutuelle health (health data) | **No** |
| Customer diagnostic orders | Yes — health data risk | Yes — daily operations | Yes — diagnostic results (health data) | **No** |
| Supplier management | Yes — financial data risk | Yes — ongoing | No | **No** (fails Conditions 1 and 2) |
| Website (informational only, no analytics) | Minimal risk | Yes — continuous | No | **No** (fails Condition 2) |
| Annual team photo | Minimal risk | Arguably occasional (annual) | No (photos not biometric unless used for ID) | **Possibly exempt** |
| One-time office furniture procurement | Minimal risk | Yes — occasional (one-time) | No | **Possibly exempt** |

**Conclusion for Helix Biotech Diagnostics S.A.S.**: Despite having only 45 employees, the entity must maintain a RoPA because:
1. It processes health data (diagnostic results, employee health insurance) — Exception 3 is met.
2. Its core business processing (customer orders, employee management) is non-occasional — Exception 2 is met.
3. Processing of customer health data creates risk to data subjects — Exception 1 is met.

Only truly one-off, non-sensitive, low-risk activities (like a single furniture procurement) might technically qualify for the exemption, but documenting them in the RoPA anyway costs minimal effort and demonstrates accountability.

## EDPB and Supervisory Authority Positions

### EDPB Position Paper on Art. 30 (2018)

The EDPB formally recommended that **all organisations maintain RoPA regardless of size**:

> "The EDPB considers that most processing operations carried out by employers or service providers can, in most cases, not be considered as 'occasional'. The EDPB therefore recommends that controllers and processors, including small and medium-sized enterprises, use and maintain records of their processing activities on a voluntary basis, even where they are not obliged to do so."

### CNIL (France)

The CNIL provides a simplified RoPA template for small organisations and explicitly states that the Art. 30(5) exemption is "very limited in practice." The CNIL's Facilita RGPD tool is designed for organisations of all sizes, implicitly recommending that small organisations maintain records.

### ICO (United Kingdom)

The ICO guidance states: "In practice, it is very likely that you will need to maintain records even if you employ fewer than 250 people because it is unlikely that all of your processing is only occasional."

### BfDI (Germany)

The BfDI guidance explicitly states that the exemption "hardly ever applies in practice" (kommt in der Praxis kaum zur Anwendung) because virtually all organisations engage in non-occasional processing of employee and customer data.

### AEPD (Spain)

The AEPD recommends that all organisations maintain RoPA as a matter of best practice and accountability, regardless of the Art. 30(5) exemption.

## Practical Recommendation

**For organisations under 250 employees: maintain a RoPA regardless of the Art. 30(5) exemption.**

Reasons:

1. **The exemption almost never applies**: Meeting any one of the three exception conditions negates it, and virtually all organisations meet at least one.

2. **Accountability obligation remains**: Art. 5(2) and Art. 24 require the controller to demonstrate compliance regardless of size. A RoPA is the primary demonstration tool.

3. **Supervisory authority expectation**: All major SAs recommend maintaining RoPA regardless of size.

4. **Minimal burden for small organisations**: A small organisation may have 5-15 processing activities. Documenting these in a simple template requires minimal effort compared to the compliance risk of not maintaining records.

5. **Investigation readiness**: If a supervisory authority investigates (e.g., following a data breach or complaint), the first request will be for processing records. Not having them significantly worsens the organisation's position.

6. **Foundation for other obligations**: The RoPA feeds into DPIA assessments, privacy notices, data subject rights responses, and breach impact assessments. Without it, these processes are also impaired.
