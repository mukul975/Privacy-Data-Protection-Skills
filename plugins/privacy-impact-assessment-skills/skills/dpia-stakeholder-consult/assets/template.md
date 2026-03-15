# DPIA Stakeholder Consultation Report

## Consultation Details

| Field | Value |
|-------|-------|
| DPIA Reference | DPIA-QLH-2026-012 |
| Processing Activity | Patient Genomic Profiling Platform |
| Controller | QuantumLeap Health Technologies |
| Consultation Period | 2026-04-01 to 2026-05-01 |
| Status | Completed |
| Lead Coordinator | Dr. Elena Vasquez, DPO |

---

## DPO Advice (Art. 35(2))

| Field | Value |
|-------|-------|
| DPO Advice Received | Yes |
| Date | 2026-03-20 |

**DPO Advice Summary:**
Dr. Elena Vasquez recommends patient focus groups and genetics society engagement given the sensitivity of genomic data. Enhanced transparency measures are required, including plain-language genomic data flow diagrams. The DPO advises that prior consultation with BfDI under Art. 36 is likely required given the inherent risk profile. Works council (Betriebsrat) consultation is mandatory under BetrVG Section 87 for any employee-related monitoring aspects of the platform.

---

## Stakeholder Map

| Stakeholder | Type | Method | Status |
|-------------|------|--------|--------|
| Patient Advisory Council (Charite Berlin) | Patient Advisory Group | Focus Group | Responded |
| Deutsche Gesellschaft fuer Humangenetik | Representative Body | Written Consultation | Responded |
| Verbraucherzentrale Bundesverband | Representative Body | Written Consultation | Responded |
| Patient Sample Group (n=200) | Data Subjects | Online Survey | Responded (n=187, 93.5% response rate) |
| Hospital IT Directors Group | Internal Stakeholder | Advisory Panel | Responded |
| CloudGenomics GmbH (Processor) | Processor Representative | Meeting | Responded |
| Betriebsrat QuantumLeap | Works Council | Meeting | Responded |
| Ethics Committee Charite | Representative Body | Written Consultation | No Response (follow-up sent) |

**Response Rate: 7/8 stakeholder groups (87.5%)**

---

## Consultation Responses and DPIA Integration

### Response 1: Patient Transparency Concerns

| Field | Value |
|-------|-------|
| From | Patient Advisory Council (Charite Berlin) |
| Date | 2026-04-10 |
| Theme | Transparency and informed consent |
| Risk Alignment | R1 (Loss of confidentiality) |
| Outcome | **Adopted -- DPIA updated** |

**Concern:** Patients want a clear, visual explanation of how genomic data flows through the platform, who can access their genetic information, and how treatment decisions are influenced by algorithmic outputs. Current consent forms are too technical and do not adequately explain downstream data sharing.

**Action Taken:**
- Created illustrated genomic data flow diagram in patient information leaflet (A4, multi-language)
- Redesigned consent mechanism with granular options: (1) treatment use only, (2) treatment + research, (3) treatment + insurance sharing
- Added real-time data access log viewable by patients through secure patient portal

---

### Response 2: Genetic Discrimination Risk

| Field | Value |
|-------|-------|
| From | Deutsche Gesellschaft fuer Humangenetik (German Society of Human Genetics) |
| Date | 2026-04-15 |
| Theme | Genetic discrimination by insurance partners |
| Risk Alignment | R3 (Loss of purpose limitation) |
| Outcome | **Adopted -- DPIA updated** |

**Concern:** The Gendiagnostikgesetz (GenDG) Section 18 prohibits insurers from requiring or using genetic test results for insurance decisions. Sharing genomic risk scores with insurance partners, even for "coverage assessment," creates a pathway for prohibited use. The society recommends no individual-level genomic data be shared with insurers under any circumstances.

**Action Taken:**
- Modified data sharing architecture: only aggregated risk category labels (e.g., "standard risk," "elevated monitoring recommended") shared with insurance partners -- no individual genomic scores or raw data
- Added contractual clause explicitly prohibiting insurance partners from using shared data for underwriting, premium calculation, or coverage exclusion decisions
- Implemented technical enforcement: insurance API endpoint only returns categorical risk levels, with no drill-down capability
- Added R3 mitigation measure reflecting GenDG Section 18 compliance

---

### Response 3: Data Retention Preferences

| Field | Value |
|-------|-------|
| From | Patient Survey Group (n=187 respondents) |
| Date | 2026-04-28 |
| Theme | Data retention and deletion rights |
| Risk Alignment | New risk identified (added as R6) |
| Outcome | **Partially adopted with modifications** |

**Concern:** 67% of survey respondents want the ability to request deletion of their genomic data after treatment completion. 23% want indefinite retention for future research benefit. 10% were unsure. Respondents highlighted that genomic data is uniquely permanent and expressed concern about long-term storage risks.

**Action Taken:**
- Implemented tiered retention model:
  - Clinical genomic records: retained for duration of active treatment + 10 years (German medical records retention requirement under MBO Section 10)
  - Research datasets: separate explicit consent required; patients can withdraw research consent and request deletion at any time
  - Insurance-shared categorical data: deleted within 12 months of coverage decision
- Added new DPIA risk R6: "Long-term genomic data retention increasing cumulative breach exposure"
- Residual risk managed through scheduled re-encryption with rotating keys every 24 months

---

### Response 4: Algorithmic Transparency

| Field | Value |
|-------|-------|
| From | Verbraucherzentrale Bundesverband (Federation of German Consumer Organisations) |
| Date | 2026-04-20 |
| Theme | AI model transparency and bias accountability |
| Risk Alignment | R2 (Discrimination) |
| Outcome | **Partially adopted with modifications** |

**Concern:** Consumer federation requests full public documentation of AI model decision criteria, training data composition, and bias testing results. They argue that health-related algorithmic decisions require maximum transparency under the AI Act high-risk system requirements.

**Action Taken:**
- Published model cards for each genomic analysis algorithm on the QuantumLeap transparency portal, including: intended use, training data demographics, performance metrics by ethnic group, known limitations
- Bias audit executive summaries published quarterly
- Full model architecture and proprietary variant classification algorithms withheld as trade secrets per Art. 35(9) commercial interests exception -- documented justification in DPIA
- Committed to independent third-party algorithmic audit annually (first audit by AlgorithmWatch, scheduled Q4 2026)

---

### Response 5: Employee Data Concerns

| Field | Value |
|-------|-------|
| From | Betriebsrat QuantumLeap (Works Council) |
| Date | 2026-04-12 |
| Theme | Employee monitoring via platform usage logs |
| Risk Alignment | New risk identified (added as R7) |
| Outcome | **Adopted -- DPIA updated** |

**Concern:** Works council raised that platform usage logs (clinician access patterns, query volumes, response times) could be repurposed for employee performance monitoring in violation of BetrVG Section 87(1)(6).

**Action Taken:**
- Negotiated supplementary works agreement (Betriebsvereinbarung) specifying that platform usage logs shall not be used for individual employee performance evaluation
- Technical controls: employee-identifiable usage logs accessible only to DPO and IT security team; HR department excluded from access
- Aggregated, anonymised usage statistics permitted for system optimisation
- Added DPIA risk R7: "Employee monitoring via platform usage analytics"
- Works council granted audit rights over log access records

---

## Completeness Assessment

| Criterion | Status |
|-----------|--------|
| Art. 35(2) DPO advice received | Compliant |
| Art. 35(9) data subject views sought | Compliant |
| Representative body engagement | Compliant (3 bodies consulted) |
| Works council consultation (BetrVG) | Compliant |
| Response rate adequate | Yes (87.5%) |
| Feedback documented | Yes (5 formal responses recorded) |
| Feedback integrated into DPIA | Yes (2 adopted, 2 partially adopted, 1 adopted) |
| Non-adoption justified | Yes (partial adoption of Verbraucherzentrale request justified under Art. 35(9) commercial interests) |
| Feedback loop closed | In progress -- outcome notification to consultees scheduled for 2026-05-15 |

**Overall Completeness Score: 90/100**

---

## Sign-Off

| Role | Name | Date | Decision |
|------|------|------|----------|
| DPO | Dr. Elena Vasquez | 2026-05-05 | Consultation process compliant; 2 new risks added to DPIA |
| Head of Patient Relations | Dr. Tobias Keller | 2026-05-05 | Patient engagement materials approved |
| Works Council Chair | Sandra Hoffmann | 2026-05-03 | Betriebsvereinbarung signed; consultation adequate |
| Legal Counsel | Dr. Katrin Neumann | 2026-05-05 | GenDG compliance measures validated |
