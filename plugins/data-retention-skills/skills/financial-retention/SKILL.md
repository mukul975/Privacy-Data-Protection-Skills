---
name: financial-retention
description: >-
  Implements financial records retention requirements across EU directives (5-7 years),
  SOX Section 802 (7 years), MiFID II (5-7 years), tax records, payment data, and AML
  obligations under AMLD. Maps financial data categories to statutory retention periods
  with cross-jurisdictional reconciliation. Activate for financial retention, SOX records,
  MiFID retention, AML retention, tax record keeping queries.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: data-retention-deletion
  tags: "financial-retention, sox-compliance, mifid-ii, aml-retention, tax-records"
---

# Financial Records Retention

## Overview

Financial records are subject to a complex matrix of statutory retention requirements across multiple regulatory frameworks. Unlike many other data categories where the GDPR storage limitation principle drives the retention period, financial records frequently have mandatory minimum retention periods that override the general principle of minimizing retention. Organizations operating across jurisdictions must reconcile overlapping and sometimes conflicting requirements — retaining long enough to satisfy the strictest applicable requirement while not retaining longer than necessary. This skill maps financial data categories to their statutory retention periods across EU, UK, and US frameworks.

## Regulatory Framework Matrix

### EU/UK Financial Record Retention Requirements

| Regulation/Statute | Scope | Retention Period | Data Categories | Legal Reference |
|-------------------|-------|-----------------|-----------------|-----------------|
| **Companies Act 2006 (UK)** | All UK companies | 6 years from end of financial year | Accounting records, financial statements, directors' reports | s.388(4) |
| **HMRC — Income Tax** | UK taxpayers | 6 years from end of tax year (5 years for individuals and unincorporated businesses meeting specific conditions) | Tax returns, P60s, P11Ds, payroll records, expense records | TMA 1970 s.12B; ITEPA 2003 |
| **HMRC — VAT** | UK VAT-registered businesses | 6 years from end of VAT period | VAT returns, invoices (sales and purchase), credit/debit notes | VAT Regulations 1995 reg.31 |
| **HMRC — Corporation Tax** | UK companies | 6 years from end of accounting period | Corporation tax returns, computations, supporting records | TMA 1970 s.34 |
| **EU Accounting Directive 2013/34/EU** | EU member state companies | 5-10 years (varies by member state) | Annual accounts, management reports, audit reports | Art. 30 (member state transposition) |
| **MiFID II / MiFIR** | Investment firms | 5 years (extendable to 7 years by competent authority) | Client orders, transactions, communications (including telephone and electronic), suitability assessments | MiFID II Art. 16(6)-(7); Commission Delegated Regulation 2017/565 Art. 72-76 |
| **EMIR** | Derivatives counterparties | 5 years following termination of contract | OTC derivative contracts, cleared derivative records, trade reports | EMIR Art. 9(2) |
| **AMLD 5 (EU)** / **MLR 2017 (UK)** | Obliged entities | 5 years from end of business relationship or transaction completion | Customer due diligence records, transaction records, risk assessments, SARs | AMLD5 Art. 40; MLR 2017 reg.40 |
| **Payment Services Directive (PSD2)** | Payment service providers | 5 years | Payment transaction records, authentication records | PSD2 Art. 99 (enforcement provisions) |
| **GDPR** | All controllers processing personal data | Storage limitation — no longer than necessary | All personal data within financial records | Art. 5(1)(e) |

### US Financial Record Retention Requirements

| Regulation/Statute | Scope | Retention Period | Data Categories | Legal Reference |
|-------------------|-------|-----------------|-----------------|-----------------|
| **SOX Section 802** | Public companies, auditors | 7 years | Audit workpapers, review workpapers, documents forming the basis of audit/review | 18 U.S.C. §1520; SEC Rule 2-06 |
| **SOX Section 802 — Destruction prohibition** | Public companies | Penalty: up to 20 years imprisonment | Prohibition on knowingly altering, destroying, or concealing documents with intent to impede investigation | 18 U.S.C. §1519 |
| **SEC Rule 17a-4** | Broker-dealers | 6 years (first 2 years readily accessible) | Transaction records, customer account records, communications | 17 CFR §240.17a-4 |
| **IRS Requirements** | US taxpayers | 3-7 years depending on type | Tax returns (3 years from filing or 2 years from payment); employment records (4 years); property records (until disposition + 3 years) | IRC §6501 (statute of limitations) |
| **Bank Secrecy Act (BSA)** | Financial institutions | 5 years | CTRs, SARs, CDD records, CIP records | 31 CFR §1010.430 |
| **FCPA** | Companies with US nexus | Minimum 5 years (recommended 10) | Books and records, internal controls documentation, payment records | 15 U.S.C. §78m |
| **Dodd-Frank** | Swap dealers, security-based swap dealers | 5 years | Swap transaction records, daily trading records | 17 CFR §23.203 |

### Cross-Jurisdictional Reconciliation for Orion Data Vault Corp

When multiple requirements apply to the same data, the longest applicable period governs:

| Financial Data Category | UK Requirement | EU Requirement | US Requirement (if applicable) | Governing Period |
|------------------------|----------------|----------------|-------------------------------|-----------------|
| General accounting records | 6 years (Companies Act) | 5-10 years (Accounting Directive) | 7 years (SOX, if US-listed) | **7 years** (if US-listed) / **6 years** (UK only) |
| Tax records (corporate) | 6 years (HMRC) | Per member state (typically 5-10 years) | 3-7 years (IRS) | **6 years** (UK) |
| VAT records | 6 years (HMRC) | Per member state | N/A | **6 years** (UK) |
| Payroll records | 6 years (PAYE Regulations) | Per member state | 4 years (IRS employment) | **6 years** (UK) |
| AML/CDD records | 5 years (MLR 2017) | 5 years (AMLD5) | 5 years (BSA) | **5 years** |
| Investment client records | 5-7 years (MiFID II) | 5-7 years (MiFID II) | 6 years (SEC 17a-4) | **7 years** (if FCA extends) |
| Payment transaction records | 6 years (Limitation Act) | 5 years (PSD2) | N/A | **6 years** (UK) |
| Audit workpapers | 6 years (Companies Act) | Per member state | 7 years (SOX) | **7 years** (if US-listed) |
| Client communications (investment) | 5 years (MiFID II baseline) | 5 years (MiFID II) | 6 years (SEC 17a-4) | **5-7 years** (MiFID II; competent authority may extend) |

## Data Category Retention Schedule — Financial Records

### Detailed Schedule for Orion Data Vault Corp

| Cat ID | Data Category | Specific Records | Retention Period | Trigger Event | Legal Basis | Review Frequency |
|--------|--------------|-----------------|-----------------|---------------|-------------|-----------------|
| FIN-001 | General Ledger | Journal entries, trial balances, chart of accounts | 6 years from end of financial year | Financial year end | Companies Act 2006 s.388 | Annual |
| FIN-002 | Accounts Payable | Purchase invoices, supplier statements, payment records | 6 years from end of financial year | Financial year end | Companies Act 2006; HMRC VAT | Annual |
| FIN-003 | Accounts Receivable | Sales invoices, credit notes, debit notes, statements | 6 years from end of financial year | Financial year end | Companies Act 2006; HMRC VAT | Annual |
| FIN-004 | Bank Records | Bank statements, reconciliations, cheque stubs | 6 years from end of financial year | Financial year end | Companies Act 2006; Limitation Act 1980 | Annual |
| FIN-005 | Payroll | Pay slips, P45s, P60s, P11Ds, NI records, pension contributions | 6 years from end of tax year | Tax year end (5 April) | Income Tax (PAYE) Regulations 2003; Pensions Act 2004 | Annual |
| FIN-006 | Tax Returns (CT) | Corporation tax returns, computations, supporting schedules | 6 years from end of accounting period | Accounting period end | TMA 1970 s.34 | Annual |
| FIN-007 | VAT Returns | VAT returns, quarterly summaries, MTD records | 6 years from end of VAT period | VAT period end | VAT Regulations 1995 reg.31 | Annual |
| FIN-008 | Expense Claims | Expense reports, receipts, approvals, mileage records | 6 years from end of tax year | Tax year end | HMRC; Companies Act 2006 | Annual |
| FIN-009 | AML Records | CDD documentation, EDD records, risk assessments, transaction monitoring alerts, SAR filings | 5 years from end of business relationship or transaction | Relationship end / transaction date | MLR 2017 reg.40; AMLD5 Art. 40 | Annual |
| FIN-010 | Audit Files | External audit workpapers, internal audit reports, management letters | 7 years from audit date (SOX) / 6 years (UK only) | Audit completion date | SOX s.802; Companies Act 2006 | Annual |
| FIN-011 | Investment Records | Client orders, execution reports, suitability assessments, best execution records | 5 years (extendable to 7 by FCA) from date of record | Record creation date | MiFID II Art. 16(6); FCA COBS 9.5 | Annual |
| FIN-012 | Communications (Investment) | Recorded telephone conversations, electronic communications relating to client orders and transactions | 5 years from date of recording | Recording date | MiFID II Art. 16(7); Commission Delegated Reg. 2017/565 Art. 76 | Annual |
| FIN-013 | Payment Records | Card transaction records, direct debit records, BACS/CHAPS records | 6 years from transaction date | Transaction date | Limitation Act 1980 s.5; PSD2 | Annual |
| FIN-014 | Insurance Records | Policy documents, claims records, premium records | Duration of policy + 6 years (or 3 years for personal injury limitation) | Policy expiry / claim settlement | Limitation Act 1980 s.5 / s.11 | Annual |
| FIN-015 | Contracts (Financial) | Loan agreements, facility letters, guarantees, security documents | Duration + 12 years (deed) / 6 years (simple contract) | Contract termination | Limitation Act 1980 s.5 (6 years) / s.8 (12 years for deeds) | Annual |

## GDPR Interaction with Financial Retention

### Balancing Storage Limitation with Statutory Retention

The GDPR storage limitation principle (Art. 5(1)(e)) does not override statutory retention requirements. Art. 17(3)(b) explicitly provides that the right to erasure does not apply where processing is necessary for compliance with a legal obligation under Union or Member State law.

However, the following GDPR obligations still apply to financially retained data:

1. **Purpose limitation (Art. 5(1)(b))**: Data retained for statutory compliance may only be processed for that purpose — not repurposed for marketing, profiling, or other purposes without a separate legal basis.
2. **Data minimization (Art. 5(1)(c))**: Only the personal data fields necessary for the statutory obligation should be retained. Non-essential fields should be deleted or anonymized when the primary processing purpose expires.
3. **Access restrictions**: Data retained solely for legal obligation should be restricted to authorized personnel (legal, finance, compliance) — not accessible to general staff.
4. **Transparency (Art. 13/14)**: Data subjects must be informed of the retention periods and the legal obligations that mandate them.

### Handling Art. 17 Erasure Requests for Financial Data

```
[Art. 17 Erasure Request Received — Financial Records]
         │
         ▼
[Identify Financial Data Categories Held]
         │
         ▼
[For Each Category]
   │
   ├── [Statutory retention period still active?]
   │     ├── Yes ──► [Exception applies: Art. 17(3)(b)]
   │     │           [Inform data subject: statutory retention obligation
   │     │            prevents erasure until [date]. Cite specific statute.]
   │     │           [Apply data minimization: delete non-essential fields]
   │     │           [Restrict access to compliance-only]
   │     │
   │     └── No ──► [Statutory period expired]
   │                 [Delete financial records per normal erasure workflow]
   │
   └── [Data subject requests access to retained financial records?]
         └── Yes ──► [Provide access under Art. 15 — financial data
                       retention does NOT suspend access rights]
```

## Implementation Guidance

### Retention Calendar

Orion Data Vault Corp operates the following annual retention calendar for financial records:

| Month | Activity |
|-------|----------|
| April | Tax year end — trigger retention countdown for payroll records (FIN-005), expense claims (FIN-008) |
| May | Annual financial statement preparation — trigger retention countdown for prior year general ledger (FIN-001) |
| June | Annual external audit completion — trigger retention countdown for audit files (FIN-010) |
| September | Companies House filing deadline — file and archive annual accounts |
| October | Annual retention review — review all active financial retention periods against current statutory requirements |
| December/January | Financial year end (if December year-end) — trigger retention countdown for accounting records |
| Quarterly | VAT return filing — archive returns and supporting records (FIN-007) |
| Monthly | AML transaction monitoring — archive alerts and dispositions (FIN-009) |

### Technical Controls

1. **Immutable storage**: Financial records subject to statutory retention must be stored on immutable (WORM) storage or with appropriate integrity controls to prevent unauthorized modification.
2. **Audit trail**: All access to retained financial records must be logged (who accessed, when, what was accessed, for what purpose).
3. **Encryption at rest**: All financial records must be encrypted at rest using AES-256 or equivalent.
4. **Automated deletion scheduling**: When a statutory retention period expires, the record enters the automated deletion queue with a 30-day review period before permanent deletion.
5. **Legal hold override**: Financial records subject to an active litigation hold are excluded from scheduled deletion regardless of retention period expiry.
