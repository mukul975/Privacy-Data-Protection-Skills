# Data Localization Implementation Workflow

## Assessment Workflow

1. **Jurisdiction mapping**: Identify all countries where the organisation collects or processes personal data of local residents.
2. **Localization requirement identification**: For each jurisdiction, determine whether a data localization law applies (storage mandate, processing mandate, or both).
3. **Scope assessment**: Determine which data categories are subject to localization (all personal data, payment data only, government data only, CIIO data only).
4. **Threshold assessment**: For China (PIPL), determine whether volume thresholds trigger the CAC security assessment requirement.
5. **Architecture review**: Assess current data architecture against localization requirements to identify gaps.
6. **Remediation planning**: Design infrastructure changes to meet localization obligations.

## Implementation Workflow (Per Jurisdiction)

### Russia

1. Identify all personal data collected from Russian citizens.
2. Provision or procure database infrastructure within Russian territory.
3. Configure all data collection points (web forms, APIs, manual entry) to write initially to the Russian database.
4. Implement replication to the central EU systems, encrypted via TLS 1.3.
5. Complete the Roskomnadzor notification of personal data processing (Form 1).
6. Verify cross-border transfer compliance for replicated data (adequate country or data subject consent).
7. Document the localization architecture and retain for regulatory inspection.

### China

1. Determine if the organisation is a CIIO or meets CAC volume thresholds.
2. If yes: initiate CAC security assessment process (file with provincial CAC).
3. If no: prepare and file the CAC Standard Contract with the provincial CAC within 10 working days of execution.
4. Complete the Personal Information Impact Assessment (PIIA) per PIPL Art. 55.
5. Provision domestic storage (Alibaba Cloud, Tencent Cloud, or licensed DC in mainland China).
6. Configure data processing to occur within domestic infrastructure.
7. Implement cross-border transfer controls per the approved mechanism.
8. Schedule the 2-year reassessment for security assessments.

### India

1. Monitor Central Government notifications for any blacklisted countries.
2. Comply with RBI payment data localization for payment system operators.
3. Provision cloud infrastructure in the Indian region (AWS Mumbai, Azure Central India).
4. Implement data residency policies in cloud configuration to prevent PD egress.
5. Maintain readiness for future DPDP Act Section 16 restrictions.
6. If designated as Significant Data Fiduciary: appoint DPO in India, conduct data protection audit.

## Monitoring Workflow

1. **Quarterly**: Review regulatory developments in each jurisdiction for new or amended localization requirements.
2. **Semi-annually**: Verify localization architecture compliance (confirm data residency controls are operative).
3. **Annually**: Full localization compliance audit across all jurisdictions.
4. **Upon legislative change**: Assess impact within 30 days; implement architectural changes within the compliance deadline.
