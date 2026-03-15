# Cloud Migration Privacy Assessment Workflows

## Workflow 1: Cloud Processing Data Mapping

1. Inventory all personal data categories to be migrated.
2. For each data category, identify: data subjects, volume, sensitivity classification, retention requirements.
3. Map current on-premises data flows.
4. Map proposed cloud data flows (collection to deletion).
5. Identify all CSP services in scope.
6. For each service, determine: processing location(s), sub-processors, encryption capabilities.
7. Document the complete data lifecycle in cloud.

## Workflow 2: CSP DPA Review Checklist

Verify the CSP DPA includes all Art. 28(3) mandatory elements:

| Element | Art. 28(3) Reference | Status |
|---------|---------------------|--------|
| Processing only on documented instructions | Art. 28(3)(a) | |
| Confidentiality obligations for authorised persons | Art. 28(3)(b) | |
| Appropriate security measures per Art. 32 | Art. 28(3)(c) | |
| Sub-processor conditions (prior authorisation, flow-down of obligations) | Art. 28(3)(d) | |
| Assistance with data subject rights | Art. 28(3)(e) | |
| Assistance with security, breach notification, DPIA, prior consultation | Art. 28(3)(f) | |
| Deletion or return of data on termination | Art. 28(3)(g) | |
| Audit and inspection rights | Art. 28(3)(h) | |

## Workflow 3: Cloud International Transfer Assessment

```
START: CSP data processing locations identified
│
├─ For each processing location outside EEA:
│  ├─ Is there an adequacy decision for this country?
│  │  ├─ YES → Document. Transfer mechanism: Art. 45.
│  │  └─ NO → Continue.
│  │
│  ├─ Are SCCs in place with the CSP?
│  │  ├─ YES → Conduct TIA per EDPB Recommendations 01/2020.
│  │  └─ NO → SCCs must be executed before migration.
│  │
│  ├─ Can customer-managed encryption keys prevent CSP clear-text access?
│  │  ├─ YES → Strong supplementary measure for TIA.
│  │  └─ NO → Assess CSP access to clear-text data under local law.
│  │
│  └─ Document transfer mechanism and supplementary measures.
│
└─ END: Complete transfer mapping for all non-EEA locations.
```

## Workflow 4: Cloud Exit Strategy

1. Define data portability requirements (formats, APIs, completeness).
2. Negotiate data return clause in DPA (timeline, format, verification).
3. Define data deletion verification mechanism (certification of destruction).
4. Identify alternative CSPs or on-premises options for contingency.
5. Test data export process before migration (dry run).
6. Document the exit strategy and include in DPIA.
