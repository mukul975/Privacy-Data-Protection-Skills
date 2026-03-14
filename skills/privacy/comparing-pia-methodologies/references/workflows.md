# PIA Methodology Comparison Workflows

## Workflow 1: Methodology Selection
1. Identify all jurisdictions where the processing operates or where data subjects reside.
2. Check whether any applicable supervisory authority mandates or recommends a specific methodology.
3. If mandated methodology exists → adopt it (e.g., CNIL PIA for France-regulated processing).
4. If no mandate → assess organisational maturity (low → ICO, medium → CNIL, high → ISO 29134).
5. If multi-jurisdictional → default to ISO 29134 for international acceptability.
6. If US-based with existing NIST CSF → layer NIST PF as framework, supplement with CNIL or ICO for individual assessments.
7. Document methodology selection rationale in DPIA introduction section.

## Workflow 2: Cross-Methodology Mapping
1. Identify the primary methodology being used for the assessment.
2. Map each step of the primary methodology to Art. 35(7)(a)-(d) minimum content requirements.
3. Identify any gaps where the primary methodology does not address a requirement covered by another methodology.
4. Supplement the primary methodology with elements from other methodologies to fill gaps.
5. Document the combined approach and justify each supplementary element.

## Workflow 3: Methodology Compliance Verification
1. Complete the DPIA using the selected methodology.
2. Verify against Art. 35(7) minimum content checklist:
   - (a) Systematic description of processing operations and purposes: present?
   - (b) Necessity and proportionality assessment in relation to purposes: present?
   - (c) Risk assessment to rights and freedoms of data subjects: present?
   - (d) Measures to address risks including safeguards, security measures, and mechanisms: present?
3. Verify against CNIL Deliberation 2018-327 ten criteria:
   - Criterion 1: Description of processing operations assessed.
   - Criterion 2: Assessment of compliance with fundamental principles.
   - Criterion 3: Assessment of risks to data subjects.
   - Criterion 4: Risk treatment measures.
   - Criterion 5: Linkage between principles, risks, and measures.
   - Criterion 6: Review by relevant stakeholders.
   - Criterion 7: Consistent risk scale.
   - Criterion 8: Sources of risk identified.
   - Criterion 9: Data subjects' perspective considered.
   - Criterion 10: Documented and revisable.
4. If any criterion not met → supplement assessment before finalisation.

## Workflow 4: Multi-Methodology Harmonisation
1. For organisations operating across jurisdictions requiring different methodologies:
   - Create a master DPIA using ISO 29134 as the base (internationally recognised).
   - Add CNIL-specific sections (feared events analysis) for French processing.
   - Add ICO-specific sections (data subject consultation record) for UK processing.
   - Add NIST PF profile for US operations.
2. Maintain a single risk register that maps to all methodology risk scales.
3. Produce jurisdiction-specific extracts from the master DPIA for supervisory authority submissions.
