# Special Category Data Processing Register

## Organisation: Vanguard Financial Services
## Register Reference: SCD-REG-2026-001
## Date: 2026-03-14
## Maintained By: Dr. James Whitfield, Data Protection Officer

---

## Processing Activity 1: Employee Diversity Monitoring

| Field | Detail |
|-------|--------|
| **Processing Activity ID** | SCD-HR-001 |
| **System** | HR Platform (Workday) |
| **Special Categories Processed** | Racial/ethnic origin, sexual orientation |
| **Data Elements** | `employee_ethnicity`, `sexual_orientation`, `gender_identity` |
| **Data Subjects** | Vanguard employees (12,000 globally) |
| **Purpose** | Workforce diversity reporting, equal opportunity compliance, pay equity analysis |
| **Art. 9(2) Condition** | Art. 9(2)(a) — Explicit consent (voluntary diversity survey) and Art. 9(2)(b) — Employment law obligation (UK Equality Act 2010 s.158-159 positive action provisions) |
| **Art. 6 Lawful Basis** | Art. 6(1)(c) — Legal obligation (equality monitoring) and Art. 6(1)(a) — Consent (voluntary additional categories) |
| **Explicit Consent Mechanism** | Online survey form with separate explicit consent checkbox per category: "I explicitly consent to Vanguard processing my [ethnicity/sexual orientation/gender identity] for the purpose of diversity monitoring. I understand this data will be aggregated for statistical reporting and will not be used in any individual employment decision." Consent is refreshed annually. |
| **Data Minimisation** | Data collected only to the level of detail required for regulatory reporting. Free-text responses not permitted. Predefined categories aligned with national census categories. |
| **Access Controls** | Restricted to Diversity & Inclusion team (4 persons) and DPO. Individual-level data not accessible to line managers or HR business partners. |
| **Retention** | Individual responses retained for 3 years. Aggregated statistics retained indefinitely. |
| **DPIA Reference** | DPIA-HR-DIV-2025-001 (completed 2025-09-15, next review 2026-09-15) |
| **International Transfer** | UK-collected data processed in Workday EU instance (Ireland). No transfers outside EEA for this processing. |

---

## Processing Activity 2: Biometric Building Access Control

| Field | Detail |
|-------|--------|
| **Processing Activity ID** | SCD-SEC-001 |
| **System** | Physical Security Access Control (HID Global) |
| **Special Categories Processed** | Biometric data (fingerprint templates) |
| **Data Elements** | `fingerprint_template` (ISO 19795 format), `facial_recognition_embedding` (secure area only) |
| **Data Subjects** | Employees and authorised contractors accessing Vanguard offices (8,500 enrolled users) |
| **Purpose** | Physical access control for office buildings and secure areas (trading floor, data centre) |
| **Art. 9(2) Condition** | Art. 9(2)(a) — Explicit consent (employees may opt for RFID card-only access as alternative) |
| **Art. 6 Lawful Basis** | Art. 6(1)(f) — Legitimate interests (security of financial services premises) |
| **Explicit Consent Mechanism** | During onboarding, employees are presented with access control options: (1) Biometric fingerprint + RFID card, (2) RFID card only. Employees choosing option (1) sign a dedicated biometric consent form: "I explicitly consent to Vanguard collecting and processing my fingerprint biometric template solely for the purpose of physical building access control. I understand I may withdraw consent at any time and switch to card-only access without detriment." |
| **Alternative Available** | RFID card-only access available for all standard areas. Biometric required only for highest-security areas (data centre) — these are staffed by volunteers who have freely consented. |
| **Template Storage** | Biometric templates stored on-premise in encrypted hardware security module (HSM). No cloud storage. Templates are mathematical representations, not raw fingerprint images. |
| **Retention** | Templates deleted within 7 days of employment termination or consent withdrawal. |
| **DPIA Reference** | DPIA-SEC-BIO-2025-001 (completed 2025-06-20, next review 2026-06-20) |

---

## Processing Activity 3: Occupational Health Surveillance

| Field | Detail |
|-------|--------|
| **Processing Activity ID** | SCD-OH-001 |
| **System** | Occupational Health Management (Cority) |
| **Special Categories Processed** | Health data |
| **Data Elements** | `diagnosis_code` (ICD-10), `fitness_for_duty_assessment`, `workplace_adjustment_recommendation`, `sick_leave_duration`, `return_to_work_plan` |
| **Data Subjects** | Employees referred for occupational health assessment (~800 annually) |
| **Purpose** | Assessment of fitness for duty, workplace adjustment recommendations, management of long-term sickness absence, compliance with Health and Safety at Work Act 1974 |
| **Art. 9(2) Condition** | Art. 9(2)(h) — Processing necessary for assessment of working capacity under occupational medicine, processed under responsibility of occupational health physician bound by professional secrecy |
| **Art. 6 Lawful Basis** | Art. 6(1)(c) — Legal obligation (employer duty of care under health and safety law) |
| **Professional Secrecy** | All occupational health assessments conducted by qualified occupational health physicians registered with the General Medical Council (GMC). Line managers receive only fitness/adjustment recommendations, not diagnosis details. |
| **Data Minimisation** | HR receives: fit/unfit/fit with adjustments. HR does NOT receive: diagnosis, treatment details, prognosis. Employee may voluntarily share additional information. |
| **Access Controls** | Clinical data: occupational health team only (3 physicians, 2 nurses). Fitness recommendations: HR case manager and line manager. |
| **Retention** | 40 years from last entry per occupational health records guidance (in line with Control of Substances Hazardous to Health Regulations 2002 for exposure records, applied as default for all OH records). |
| **DPIA Reference** | DPIA-OH-2025-001 (completed 2025-08-10, next review 2026-08-10) |

---

## Processing Activity 4: Trade Union Dues Deduction

| Field | Detail |
|-------|--------|
| **Processing Activity ID** | SCD-HR-002 |
| **System** | Payroll System (ADP GlobalView) |
| **Special Categories Processed** | Trade union membership |
| **Data Elements** | `union_membership_status`, `union_name`, `monthly_dues_amount` |
| **Data Subjects** | Unionised employees (~1,200 in UK operations) |
| **Purpose** | Deduction of trade union dues from payroll at employee request, in accordance with collective agreement |
| **Art. 9(2) Condition** | Art. 9(2)(b) — Processing necessary for obligations under employment law and collective agreement, authorised by Trade Union and Labour Relations (Consolidation) Act 1992 s.68 (check-off arrangements) |
| **Art. 6 Lawful Basis** | Art. 6(1)(c) — Legal obligation (statutory check-off requirement upon employee request) |
| **Data Minimisation** | Only membership status, union name, and deduction amount processed. No details of union activities, meeting attendance, or union role. |
| **Retention** | Duration of employment + 6 years (payroll records retention per HMRC requirements). Union membership status deleted upon termination; financial records retained for statutory period. |
| **DPIA Reference** | Included in payroll processing DPIA (DPIA-PAY-2025-001) |

---

## Summary Statistics

| Category | Fields | Records Affected | DPIA Completed |
|----------|--------|-----------------|----------------|
| Racial/ethnic origin | 1 | 12,000 | Yes |
| Sexual orientation | 1 | 3,200 (survey respondents) | Yes |
| Biometric (fingerprint) | 1 | 8,500 | Yes |
| Biometric (facial) | 1 | 350 (secure area) | Yes |
| Health data | 5 | 800/year | Yes |
| Trade union membership | 3 | 1,200 | Yes |
| **Total** | **12** | — | **All completed** |

---

*Register maintained in accordance with Art. 30 GDPR and Vanguard Data Classification Policy DCP-2025-v3.1. Reviewed quarterly by the DPO. Next scheduled review: 2026-06-14.*
