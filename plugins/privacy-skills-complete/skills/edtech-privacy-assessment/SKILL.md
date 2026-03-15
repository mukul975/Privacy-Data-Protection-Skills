---
name: edtech-privacy-assessment
description: >-
  Assesses children's data protection in educational technology. Covers
  COPPA school exception under Section 312.5(c)(4), FERPA intersection,
  parental rights, teacher consent authority, data deletion at year-end,
  and Student Privacy Pledge compliance. Keywords: edtech, COPPA school
  exception, FERPA, student privacy, teacher consent, educational data.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: children-data-protection
  tags: "edtech, coppa-school-exception, ferpa, student-privacy, teacher-consent, educational-data"
---

# EdTech Privacy Assessment — Children's Data in Educational Technology

## Overview

Educational technology (EdTech) platforms that process children's personal data operate at the intersection of multiple privacy frameworks. In the United States, COPPA's school exception (16 CFR 312.5(c)(4)) allows schools to provide consent on behalf of parents for the collection of children's data in educational contexts, but only for school-authorised educational purposes. The Family Educational Rights and Privacy Act (FERPA, 20 U.S.C. Section 1232g) governs education records maintained by educational agencies or institutions receiving federal funding. In the EU, GDPR applies with the heightened protections of Art. 8 (parental consent for children) and Recital 38 (specific protection for children). The UK AADC applies to EdTech services likely to be accessed by children. This skill provides a framework for conducting privacy assessments of EdTech platforms that navigate these overlapping requirements.

## Regulatory Frameworks

### COPPA School Exception — 16 CFR 312.5(c)(4)

COPPA permits an operator to collect personal information from a child for the use and benefit of the school, and for no other commercial purpose, without obtaining verifiable parental consent directly, when:

1. The school has authorised the collection of personal information on behalf of the students
2. The collection is solely for the school's use and benefit in the educational context
3. The operator does not use the collected information for any commercial purpose unrelated to the educational context
4. The operator does not disclose the information to non-school third parties

**Critical Limitations**:
- The school acts as an agent of the parent; the school does not have unlimited authority
- The school can only consent to the collection of information necessary for the school-authorised educational activity
- If the operator wants to use the data for commercial purposes (including advertising), the operator must obtain verifiable parental consent directly from the parent
- The FTC has stated that schools "should not be able to consent on behalf of the parent to the collection of information that is not needed for the educational purpose" (FTC COPPA FAQ J.2)

### FERPA — 20 U.S.C. Section 1232g

FERPA protects education records maintained by educational agencies or institutions that receive federal funding. EdTech platforms may receive education records as "school officials" under the school official exception.

**Key Provisions**:
- **Education records**: Records, files, documents, and other materials directly related to a student that are maintained by an educational agency or institution or by a person acting for such agency or institution
- **School official exception** (34 CFR 99.31(a)(1)): An educational agency or institution may disclose education records to a contractor, consultant, volunteer, or other party to whom the agency has outsourced institutional services or functions, provided that: the party performs an institutional service or function; the party is under the direct control of the agency; the party uses the education records only for the purposes for which the disclosure was made; the party meets the criteria specified in the agency's FERPA annual notification
- **Legitimate educational interest**: The school official must have a legitimate educational interest in the education records — meaning the official needs to review the record to fulfil their professional responsibility
- **Directory information exception** (34 CFR 99.37): Schools may disclose directory information (name, address, telephone number, email, date and place of birth, honours, activities) without consent if parents have been notified and given the opportunity to opt out

### FERPA vs. COPPA Interaction

| Scenario | FERPA Applies? | COPPA Applies? | Result |
|----------|:---------:|:---------:|--------|
| School-directed use of EdTech platform | Yes | Yes (school exception available) | School consents under COPPA; FERPA school official exception governs data handling |
| Student independently uses EdTech at home | No (not maintained by school) | Yes (full COPPA applies) | Operator must obtain verifiable parental consent directly |
| EdTech vendor receives education records from school | Yes | Yes (school exception) | FERPA and COPPA both apply; vendor must comply with both |
| EdTech vendor uses data for advertising | FERPA violation (non-educational use) | COPPA violation (exceeds school exception) | Both laws violated; school exception does not apply |

### GDPR Application to EdTech

In the EU, the COPPA school exception does not exist. Schools using EdTech platforms must comply with:

- **Art. 6 Lawful Basis**: Schools may rely on Art. 6(1)(e) (public task) for processing necessary for educational purposes, or Art. 6(1)(f) (legitimate interests) where public task does not apply
- **Art. 8 Parental Consent**: If the EdTech platform relies on consent as its lawful basis for processing children's data, parental consent is required for children below the applicable national threshold
- **Art. 28 Processor Agreement**: If the school is the data controller and the EdTech vendor is the processor, a compliant Art. 28 data processing agreement must be in place
- **Controller Determination**: The school is typically the controller for educational processing; the EdTech vendor is the processor. However, if the vendor processes data for its own purposes (product improvement, analytics, advertising), it becomes a controller or joint controller for those purposes

### Student Privacy Pledge (FPF/SIIA)

The Student Privacy Pledge, administered by the Future of Privacy Forum (FPF) and the Software and Information Industry Association (SIIA), is a voluntary industry commitment. Signatories commit to:

1. Not sell student personal information
2. Not behaviourally target advertising to students using data from the educational context
3. Not create advertising profiles of students
4. Not change privacy policies without notice and choice
5. Enforce strict limits on data retention and deletion
6. Support access to and correction of student information by authorised parties
7. Use student data only for authorised educational/school purposes or as directed by parent/student
8. Maintain a comprehensive data security program
9. Not disclose student information except for legitimate educational purposes
10. Require downstream recipients to comply with these commitments

Over 400 EdTech companies are signatories as of 2024.

## EdTech Privacy Assessment Framework

### Assessment Phase 1: Platform Classification

| Question | Significance |
|----------|-------------|
| Is the platform directed to children under 13? | COPPA applies fully; age gate and parental consent required |
| Is the platform used in a school context? | COPPA school exception may apply; FERPA may apply |
| Does the school direct students to use the platform? | Strengthens school exception applicability |
| Does the platform operate in the EU/UK? | GDPR/UK GDPR applies; AADC compliance required |
| Does the platform collect persistent identifiers? | COPPA personal information threshold met |
| Does the platform use collected data for non-educational purposes? | School exception does not apply to non-educational uses |

### Assessment Phase 2: Data Mapping

For each data element collected by the EdTech platform:

| Data Element | Collection Method | Educational Purpose | Non-Educational Use | Retention Period | Shared With |
|-------------|-------------------|--------------------|--------------------|-----------------|-------------|
| Student name | Account creation | Identify student in classroom | None | Academic year + 30 days | Teacher, parent |
| Email address | Login credential | Authentication | None | Account duration | None |
| Learning progress | Automated tracking | Adaptive content, grading | Product improvement (aggregated) | Academic year + 30 days | Teacher, parent |
| Assignment submissions | Student upload | Assessment, feedback | None | Academic year + 30 days | Teacher |
| Interaction logs | Automated | Feature usage analytics | Product improvement (aggregated) | 90 days | None (internal only) |
| Device identifiers | Automated | Session management | None | Session only | None |

### Assessment Phase 3: Legal Basis Evaluation

| Jurisdiction | Lawful Basis | Conditions | Documentation Required |
|-------------|-------------|-----------|----------------------|
| US (COPPA) | School exception consent | School has authorised use; data used only for educational purposes; operator does not use data commercially | Written agreement with school; operator's COPPA-compliant privacy policy |
| US (FERPA) | School official exception | Operator performs institutional service; under school's direct control; uses records only for authorised purposes | School's FERPA annual notification names operator as school official |
| EU (GDPR) | Art. 6(1)(e) Public task | School's educational mission qualifies as public task; processing necessary for that task | School's records of processing (Art. 30); DPA between school and vendor (Art. 28) |
| UK (GDPR + AADC) | Art. 6(1)(e) Public task or Art. 6(1)(f) Legitimate interests | Same as EU GDPR plus AADC compliance for all 15 standards | DPIA; AADC conformance assessment |

### Assessment Phase 4: Contractual Requirements

The agreement between the school and the EdTech vendor must address:

1. **Scope of data processing**: Specific data elements, purposes, and retention periods
2. **Prohibition on commercial use**: Vendor may not use student data for advertising, marketing, or non-educational product development
3. **Sub-processor restrictions**: Vendor must disclose all sub-processors and ensure they comply with equivalent restrictions
4. **Data deletion obligations**: Vendor must delete all student data at the school's request and at the end of the contract period
5. **End-of-year deletion**: Vendor must delete or return all student data at the end of each academic year unless the school specifically authorises retention
6. **Security requirements**: Specific technical and organisational security measures
7. **Breach notification**: Vendor must notify the school within 24-72 hours of a data breach affecting student data
8. **Audit rights**: School has the right to audit the vendor's compliance with the agreement
9. **FERPA compliance** (US): Vendor acknowledged as school official; data used only for legitimate educational interests
10. **COPPA compliance** (US): Vendor acknowledges school exception limitations; does not use data for non-educational commercial purposes

### Assessment Phase 5: End-of-Year Data Lifecycle

The end of the academic year is a critical data lifecycle event for EdTech platforms. The following protocol must be implemented:

**60 Days Before Year End**:
1. Notify school administrators that the end-of-year data lifecycle process will begin
2. Provide data export options: school can download all student data in standard formats (CSV, JSON, SIF)
3. Confirm whether the school authorises retention of any data for the next academic year

**30 Days Before Year End**:
1. Notify teachers that student data will be archived
2. Generate end-of-year student progress reports for school records
3. Export any student-created content (assignments, projects) to the school's designated storage

**Year End (Last Day of Academic Year)**:
1. Deactivate all student accounts associated with the ending year
2. Archive student data to a deletion queue (not immediately deleted, to allow for last-minute school requests)

**30 Days After Year End**:
1. Execute deletion of all student data in the deletion queue unless the school has authorised retention
2. Deletion scope: primary database, search indices, analytics databases, caches, logs
3. Generate deletion certificates for the school

**60 Days After Year End**:
1. Purge archived backups containing deleted student data
2. Provide final deletion confirmation to the school
3. Retain only the deletion certificate and the school agreement (no student personal data)

## BrightPath Learning Inc. — EdTech Privacy Assessment

### Platform Profile

BrightPath Learning Inc. operates an educational gaming platform deployed in schools and available for home use across the US, UK, and EU. The platform serves children aged 5-15.

### Assessment Results

**Classification**:
- Directed to children under 13: YES
- Used in school context: YES (deployed in 2,400 schools)
- Also available for home (non-school) use: YES
- Operates in US, UK, EU: YES

**Dual-Track Compliance**:
- **School deployments**: COPPA school exception applies for school-directed use; FERPA school official exception applies; GDPR Art. 6(1)(e) public task in EU
- **Home use**: Full COPPA applies (verifiable parental consent via credit card); GDPR Art. 8 parental consent required in EU

**Data Practices Assessment**:

| Practice | Status | Notes |
|----------|--------|-------|
| Data used only for educational purposes | PASS | No advertising, no behavioural profiling, no commercial use |
| Student data not sold | PASS | Written policy prohibition; contractual commitment with schools |
| Behavioural advertising to students | N/A | Platform is ad-free; no advertising infrastructure |
| Data retention limited to academic year | PASS | Automatic deletion 30 days after year end; school can request earlier |
| Sub-processor list disclosed to schools | PASS | AWS (hosting), SendGrid (parent notifications); both under DPA |
| School agreement includes all required terms | PASS | Annual review; covers COPPA, FERPA, GDPR, security, deletion |
| Breach notification procedure | PASS | 24-hour notification to school; 72-hour to DPA (GDPR) |
| Parental access mechanism (home use) | PASS | Parental dashboard with data view, download, and deletion |
| Student Privacy Pledge signatory | YES | Signed 2024; annual compliance certification |

## State Student Privacy Laws

Several US states have enacted student privacy laws that impose additional requirements on EdTech vendors:

| State | Law | Key Requirements |
|-------|-----|-----------------|
| **California** | Student Online Personal Information Protection Act (SOPIPA, 2014) | Prohibits using student data for non-educational advertising; prohibits selling student data; requires deletion when no longer needed |
| **New York** | Education Law Section 2-d (2014, amended 2020) | Requires data privacy and security plans; parental notification of third-party access; breach notification; data encryption |
| **Colorado** | Student Data Transparency and Security Act (2016) | Requires school contracts to specify data elements, purposes, and security; prohibits targeted advertising to students |
| **Connecticut** | Student Data Privacy Act (PA 16-189, 2016) | Prohibits using student data for targeted advertising; requires operator to delete data within 30 days of request |
| **Illinois** | Student Online Personal Protection Act (SOPPA, 2021) | Requires parental notification; prohibits targeted advertising, creating commercial profiles, selling student data; mandates data breach notification |
| **Virginia** | Student Data Governance Plan (2015) | Requires schools to adopt data governance plans; vendors must comply with school data governance policies |
| **Texas** | SCOPE Act (2017) | Prohibits using covered information for non-educational purposes; requires security standards; mandates deletion |
| **Maryland** | Student Data Privacy Act (2015) | Prohibits using student data for advertising; requires data security; mandates deletion at end of contract |

## Common Compliance Failures

1. **Exceeding the school exception**: Using data collected under the COPPA school exception for product improvement, advertising, or other commercial purposes without separate parental consent
2. **No end-of-year deletion**: Retaining student data indefinitely after the educational purpose has expired
3. **Inadequate school agreements**: Missing key contractual terms such as sub-processor disclosure, deletion obligations, audit rights, or breach notification timelines
4. **Treating all collection as school-authorised**: When a student uses the EdTech platform at home for non-school purposes, the school exception does not apply — the operator must obtain direct parental consent
5. **FERPA non-compliance**: Failing to ensure the vendor is designated as a school official or using education records for purposes beyond legitimate educational interest
6. **No separate consent for non-educational features**: Bundling consent for educational features with optional features (gamification rewards, social features) that require separate consent

## Enforcement Precedents

- **Edmodo (FTC, 2023)**: USD 6 million penalty for collecting and using children's personal information for advertising purposes while operating as a school-directed EdTech platform, exceeding the scope of the COPPA school exception.
- **Google/YouTube (FTC, 2019)**: USD 170 million included channels used in educational contexts where persistent identifiers were collected for advertising.
- **InBloom (State enforcement, 2014)**: Data aggregation platform for student records shut down after New York, Louisiana, and other states raised FERPA and privacy concerns about centralised storage of student data with inadequate security and access controls.
- **Chegg (FTC, 2023)**: FTC ordered Chegg to implement comprehensive data security program after four breaches exposed personal information of millions of students and employees.

## Integration Points

- **COPPA Compliance**: The school exception is a narrow carve-out from COPPA's general requirements; all other COPPA requirements (notice, security, data minimisation) still apply
- **Children's Data Minimisation**: EdTech platforms must collect only data necessary for the educational purpose; data minimisation is both a COPPA and GDPR requirement
- **Children's Deletion Requests**: Parents retain the right to request deletion of their child's data even in school-directed contexts; schools can also request deletion under FERPA
- **GDPR Parental Consent**: In the EU, the school exception does not exist; schools must rely on Art. 6(1)(e) public task or obtain parental consent under Art. 8
- **Children's Privacy Notice**: EdTech platforms must provide privacy notices to both the school (as decision-maker) and parents (as rights holders)
