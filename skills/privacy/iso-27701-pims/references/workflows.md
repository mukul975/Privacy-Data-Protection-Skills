# ISO 27701 PIMS Implementation Workflows

## Workflow 1: Gap Assessment Execution

### Prerequisites
- ISO 27001:2022 ISMS in place (certified or fully implemented)
- PIMS implementation team formed (DPO, IT Security, Legal, Privacy Ops)
- Management commitment secured

### Steps

1. **Prerequisite Verification** (Week 1)
   - Confirm ISO 27001 certification status or ISMS maturity
   - Verify ISMS scope documentation is current
   - Inventory existing ISMS documentation

2. **Clause 5 Gap Analysis** (Weeks 2-4)
   - Review each sub-clause of Clause 5 against current ISMS
   - Assess privacy-specific extensions required for each ISO 27001 clause
   - Document gap findings with current state and target state
   - Rate each gap: Fully Implemented / Partially Implemented / Not Implemented / Not Applicable

3. **Annex A Control Gap Analysis (Controllers)** (Weeks 4-6)
   - Assess all 31 Annex A controls (A.7.2 through A.7.5)
   - For each control: document current implementation, identify gaps, assess remediation effort
   - Prioritize gaps by regulatory risk and implementation complexity

4. **Annex B Control Gap Analysis (Processors)** (Weeks 4-6, parallel with Annex A)
   - Assess all 18 Annex B controls (B.8.2 through B.8.5)
   - For each control: document current implementation, identify gaps, assess remediation effort

5. **Clause 6 Gap Analysis** (Weeks 6-8)
   - Review 34 privacy-specific extensions to ISO 27002 controls
   - Assess current ISO 27002 implementation against privacy extensions
   - Document additional measures required

6. **Gap Report and Remediation Roadmap** (Week 8)
   - Compile all gaps into a consolidated report
   - Prioritize remediation actions by risk and effort
   - Develop phased remediation roadmap with milestones
   - Present to management for approval and resource allocation

## Workflow 2: Statement of Applicability Extension

### Steps

1. **Retrieve Current ISO 27001 SoA**
   - Obtain the current Statement of Applicability covering ISO 27001 Annex A controls

2. **Add Annex A Controls (Controllers)**
   - For each of the 31 Annex A controls, determine applicability
   - If applicable: describe implementation and link to evidence
   - If not applicable: document justification for exclusion

3. **Add Annex B Controls (Processors)**
   - For each of the 18 Annex B controls, determine applicability
   - If applicable: describe implementation and link to evidence
   - If not applicable: document justification for exclusion

4. **Update Clause 6 Extensions**
   - For each of the 34 Clause 6 privacy extensions, document implementation status

5. **Management Review and Approval**
   - Present extended SoA to management for review
   - Obtain formal approval and sign-off
   - Version and date the updated SoA

6. **Certification Body Communication**
   - Submit updated SoA to certification body for Stage 1 review
   - Address any feedback or clarification requests

## Workflow 3: Certification Audit Preparation

### Timeline: 10-12 Weeks Before Stage 1

1. **Stage 1 Preparation** (Weeks 1-4)
   - Compile all PIMS documentation into audit-ready format
   - Ensure SoA is complete and approved
   - Prepare privacy risk assessment documentation
   - Organize evidence portfolio by clause and control
   - Confirm audit logistics (dates, rooms, interviewees)

2. **Internal Audit** (Weeks 4-6)
   - Conduct PIMS-specific internal audit covering Clauses 5-8
   - Document nonconformities and observations
   - Issue corrective action requests for any findings

3. **Management Review** (Week 6-7)
   - Conduct management review with PIMS-specific agenda
   - Review privacy risk assessment results
   - Review privacy KPIs and objectives
   - Document management review outputs and decisions

4. **Corrective Action Closure** (Weeks 7-9)
   - Close all major nonconformities from internal audit
   - Document corrective actions with evidence of effectiveness

5. **Pre-Audit Readiness Check** (Week 9-10)
   - Conduct final document completeness review
   - Brief all interviewees on audit process and expectations
   - Prepare audit room with documentation and refreshments
   - Confirm auditor logistics and schedule

6. **Stage 1 Audit** (Week 10-11)
   - Support auditor documentation review
   - Address any immediate queries
   - Receive Stage 1 findings and plan Stage 2

7. **Stage 2 Preparation** (Weeks 11-12+)
   - Address any Stage 1 findings
   - Final preparation for implementation verification
   - Ensure all evidence is current and accessible

## Workflow 4: Privacy Risk Assessment (5.4.1.2)

### Steps

1. **Scope Definition**
   - Identify processing activities in scope
   - Identify categories of PII and PII principals affected

2. **Threat Identification**
   - Identify threats to PII principals from each processing activity
   - Categories: unauthorized access, unauthorized modification, unauthorized disclosure, unlawful processing, excessive collection, failure to honor rights, cross-border transfer without safeguards

3. **Impact Assessment**
   - For each threat, assess impact on PII principals (not organizational impact)
   - Impact levels: Negligible, Limited, Significant, Maximum
   - Consider physical, material, non-material, and social harm

4. **Likelihood Assessment**
   - For each threat, assess likelihood of occurrence
   - Likelihood levels: Remote, Possible, Likely, Almost Certain
   - Consider existing controls, threat landscape, processing complexity

5. **Risk Level Determination**
   - Calculate risk level: Likelihood × Impact
   - Risk levels: Low, Medium, High, Very High

6. **Risk Treatment**
   - For High and Very High risks: identify specific mitigation measures
   - Select controls from ISO 27001 Annex A, ISO 27701 Annex A/B, or additional sources
   - Document expected risk reduction

7. **Residual Risk Assessment**
   - Calculate residual risk after mitigation
   - If residual risk remains High/Very High: escalate to Art. 36 prior consultation

8. **Documentation and Approval**
   - Document all risk assessments in the privacy risk register
   - Present to management for review and risk acceptance decisions
   - Schedule next review date
