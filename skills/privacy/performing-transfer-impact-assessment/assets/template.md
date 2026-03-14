# Transfer Impact Assessment Report

## TIA Reference: TIA-QLH-2026-0003

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| TIA Version | 1.0 |
| Date | 2026-02-15 |
| Next Review | 2027-02-15 |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |
| Assessor | Maximilian Berger, Senior Privacy Counsel |

---

## Step 1: Transfer Mapping

| Attribute | Detail |
|-----------|--------|
| Data Exporter | QuantumLeap Health Technologies GmbH, Friedrichstrasse 112, 10117 Berlin, Germany |
| Data Importer | QuantumLeap Health Technologies India Pvt. Ltd., Tower B, Manyata Embassy Business Park, Outer Ring Road, Bangalore 560045, Karnataka, India |
| Destination Country | India |
| Data Categories | Employee identifiers (name, employee ID, email address); IT support ticket data (device information, error logs, user actions); application usage metadata (timestamps, feature usage counts) |
| Special Categories | None |
| Data Subjects | QuantumLeap Health Technologies employees in EU/EEA (2,847 employees) |
| Transfer Purpose | IT helpdesk support services and application monitoring provided by the Bangalore-based IT support team during extended business hours (IST timezone coverage for after-hours EU support) |
| Transfer Frequency | Continuous during IST business hours (09:30-18:30 IST / 05:00-14:00 CET) |
| Onward Transfers | None — data processed only in Bangalore office |
| Data Format | Clear text in IT service management platform (ServiceNow instance hosted in AWS eu-west-1, accessed remotely by Bangalore team) |

---

## Step 2: Transfer Mechanism

**Mechanism**: Standard Contractual Clauses (Commission Implementing Decision 2021/914), Module 2 (Controller-to-Processor)

**SCC Execution Details**:
- Executed: 2025-10-01
- SCC Reference: SCC-QLH-2025-0019
- Module: Module 2 (Controller to Processor)
- Annexes completed: Annex I (list of parties, description of transfer, competent SA), Annex II (technical and organisational measures), Annex III (list of sub-processors)
- Governing law: German law (Clause 17)
- Competent supervisory authority: Berliner Beauftragte fur Datenschutz und Informationsfreiheit (BlnBDI)

---

## Step 3: Third Country Legal Framework Assessment — India

### 3.1 Data Protection Legislation

India enacted the Digital Personal Data Protection Act (DPDP Act) on 11 August 2023. The DPDP Act establishes a framework for personal data processing with consent as the primary basis, data fiduciary obligations, and a Data Protection Board of India as the enforcement authority. However, the implementing rules under the DPDP Act have not yet been finalised, and the Data Protection Board has not yet been operationally established.

### 3.2 Government Access Legislation

| Legislation | Access Powers | Assessment |
|-------------|--------------|------------|
| Information Technology Act 2000, Section 69 | Central or state government may direct any agency to intercept, monitor, or decrypt any information through any computer resource. Orders can be issued on grounds of sovereignty, integrity, defence, security of state, friendly relations with foreign states, public order, or investigation of cognizable offence. | Broad access powers with limited proportionality requirements. No independent judicial authorisation required — orders issued by the executive. |
| Indian Telegraph Act 1885, Section 5(2) | Government may order interception of messages on grounds of public safety, sovereignty, or investigation. | Colonial-era legislation with very broad discretionary scope. |
| DPDP Act 2023, Section 17(2) | Central government may exempt any government instrumentality from the entire Act on grounds of sovereignty, security of state, public order, or prevention of offences. | Blanket exemption power for government agencies — no independent oversight of exemption decisions. |
| IT (Procedure and Safeguards for Interception, Monitoring and Decryption of Information) Rules, 2009 | Procedural rules for Section 69 orders. Secretary-level approval required. Review committee must review every 2 months. | Review committee is not independent — comprises government officials. No judicial oversight. |

### 3.3 European Essential Guarantees Assessment

| Guarantee | Score | Assessment |
|-----------|-------|------------|
| EG1: Clear, precise, accessible rules | 3/5 | IT Act Section 69 and DPDP Act Section 17(2) are publicly available but grant broad discretionary powers. The conditions for exercising surveillance powers are defined in general terms (sovereignty, security, public order) without specificity. |
| EG2: Necessity and proportionality | 4/5 | No statutory requirement for proportionality assessment. Section 69 orders can be issued on broad grounds without a necessity test. The DPDP Act Section 17(2) exemption is blanket with no proportionality limitation. |
| EG3: Independent oversight | 4/5 | No judicial authorisation required for Section 69 orders. Review committee under IT Rules 2009 consists of government officials and is not independent. No independent data protection authority operational yet. |
| EG4: Effective remedies | 4/5 | No specific remedy mechanism for foreign nationals to challenge surveillance. The Data Protection Board (once operational) may address complaints but has no jurisdiction over government surveillance. Judicial review is theoretically available but practically inaccessible for foreign nationals. |

**Overall Essential Guarantees Score: 3.75 / 5.00**
**Assessment: Does not meet European Essential Guarantees. Supplementary measures required.**

### 3.4 Government Access Risk Score

| Factor | Weight | Score | Weighted |
|--------|--------|-------|----------|
| GA1: Surveillance legislation scope | 25% | 3 | 0.75 |
| GA2: Independent prior authorisation | 20% | 4 | 0.80 |
| GA3: Effective remedies | 20% | 4 | 0.80 |
| GA4: Transparency and notification | 15% | 3 | 0.45 |
| GA5: Rule of law and judicial independence | 20% | 3 | 0.60 |
| **Overall** | **100%** | | **3.40** |

**TIA Risk Level: High (3.1-4.0)**

---

## Step 4: Supplementary Measures

Given the High risk level and the requirement for the Bangalore team to access data in clear text (to perform IT support and troubleshooting), end-to-end encryption with exporter-held key is not feasible. The following supplementary measures are implemented:

### Technical Measures

| Measure | Description | Status |
|---------|-------------|--------|
| TM-01: Data remains in EEA infrastructure | All data remains stored in AWS eu-west-1 (Ireland). Bangalore team accesses data via secure remote desktop gateway — no data is copied to or stored in India. | Implemented |
| TM-02: Privileged access management | Bangalore team accesses ServiceNow via CyberArk Privileged Access Manager with session recording, MFA, and time-limited access tokens. | Implemented |
| TM-03: Data minimisation at access layer | Bangalore team access is restricted to active tickets only. No bulk export capability. Personally identifying data fields are masked where not required for resolution. | Implemented |
| TM-04: Network segmentation and monitoring | Dedicated VPN tunnel (IPsec/IKEv2) from Bangalore office to AWS eu-west-1. All traffic monitored by Berlin SOC. Data loss prevention rules block any data extraction. | Implemented |

### Contractual Measures

| Measure | Description | Status |
|---------|-------------|--------|
| CM-01: Government access challenge obligation | SCC Clause 15.1 supplemented by additional obligation to immediately notify Berlin HQ of any government access request, use all available legal remedies to challenge the request, and not disclose data unless legally compelled after exhausting remedies. | Executed in SCC supplementary agreement (dated 2025-10-01) |
| CM-02: Transparency reporting | Quarterly transparency report from India entity to Berlin DPO on government access requests received (including nil reports). | Executed |
| CM-03: Audit rights | Annual on-site audit right for Berlin DPO or appointed auditor to verify India entity's handling of government access requests and compliance with supplementary measures. | Executed |

### Organisational Measures

| Measure | Description | Status |
|---------|-------------|--------|
| OM-01: Government access response procedure | Documented procedure for India IT team: upon receiving any government access request, immediately notify India legal counsel and Berlin DPO. Do not disclose data without legal counsel approval. Escalation to German legal counsel within 4 hours. | Implemented |
| OM-02: Staff training | Semi-annual training for Bangalore IT support team on government access request procedures, SCC obligations, and data protection principles. Last training: 2025-12-15. | Implemented |

---

## Step 5: Implementation Verification

| Measure | Verification Method | Last Verified |
|---------|-------------------|---------------|
| TM-01: Data remains in EEA | AWS CloudTrail and VPC Flow Logs audit | 2026-01-30 |
| TM-02: PAM implementation | CyberArk session recording review | 2026-01-30 |
| TM-03: Data minimisation | ServiceNow role configuration audit | 2026-01-30 |
| TM-04: Network segmentation | Penetration test by external firm (Cobalt Strike engagement) | 2025-11-15 |
| CM-01 to CM-03 | Legal review of executed supplementary agreement | 2025-10-01 |
| OM-01 to OM-02 | Training completion records and procedure walkthrough | 2025-12-15 |

---

## Step 6: Re-evaluation Schedule

**Next scheduled review**: 2027-02-15

### Monitoring Triggers for Interim Re-evaluation
- Indian DPDP Act implementing rules published
- Data Protection Board of India becomes operational
- Any government access request received by India entity
- Change in IT Act Section 69 powers or surveillance legislation
- Data breach involving transferred data
- EDPB or Commission guidance on India transfers
- Change in scope of data transferred or processing activities

---

## Conclusion

| Assessment Area | Finding |
|-----------------|---------|
| TIA Risk Level | High (3.40/5.00) |
| Essential Guarantees Met | No |
| Supplementary Measures Sufficient | Yes — with conditions |
| Transfer Permitted | Yes — subject to conditions |

**Determination**: The transfer may proceed subject to strict maintenance of all documented supplementary measures, particularly:

1. **Data must remain stored in EEA infrastructure** — the Bangalore team must access data remotely only; no data storage or copying in India.
2. **Privileged access management** must remain operational with session recording and time-limited access.
3. **Government access response procedure** must be followed for any request, with immediate notification to Berlin DPO.
4. **Annual on-site audit** of India entity's compliance with supplementary measures.

If any supplementary measure is compromised or cannot be maintained, transfers must be suspended immediately pending resolution.

### Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-02-15 |
| Senior Privacy Counsel | Maximilian Berger | 2026-02-15 |
| CTO | Dr. Rajesh Krishnamurthy | 2026-02-16 |
| COO | Dr. Priya Sharma | 2026-02-17 |
