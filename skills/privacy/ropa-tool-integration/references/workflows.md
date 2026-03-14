# RoPA Tool Integration Workflow Reference

## Platform Selection Workflow

### Step 1: Requirements Gathering

1. Define organisational requirements based on current RoPA size and complexity:
   - Number of processing activities (current and projected)
   - Number of entities (for multi-entity groups)
   - Number of processing owners who need platform access
   - Integration requirements with existing IT systems
   - Supervisory authority template requirements (which jurisdictions)
   - Budget constraints

2. Score platforms against requirements using weighted criteria:

| Criterion | Weight | OneTrust | TrustArc | Collibra | DataGrail |
|-----------|--------|----------|----------|----------|-----------|
| Art. 30 field coverage | 20% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| API capability | 15% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Automated discovery | 15% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Workflow automation | 15% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Regulatory reporting | 10% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Integration ecosystem | 10% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Ease of use | 10% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |
| Cost | 5% | Score 1-5 | Score 1-5 | Score 1-5 | Score 1-5 |

### Step 2: Security and Privacy Assessment

Before contracting with any platform provider:

1. Conduct a vendor security assessment per the organisation's third-party risk management process.
2. Review the provider's ISO 27001 certificate scope and SOC 2 Type II report.
3. Negotiate and execute an Art. 28 data processing agreement.
4. Verify EU data residency for hosted RoPA data.
5. Assess sub-processor list and third-country transfer implications.
6. Conduct a DPIA if the platform will process special category data metadata.

### Step 3: Proof of Concept

1. Request a 4-week trial environment.
2. Import 10-15 representative RoPA entries.
3. Test API integration with a non-production Active Directory or CMDB.
4. Verify export formats meet supervisory authority requirements.
5. Test approval workflows with actual processing owners.
6. Evaluate reporting capabilities against executive dashboard requirements.

## Integration Implementation Workflow

### Active Directory / Identity Provider Integration

**Purpose**: Auto-populate organisational structure, department hierarchy, and processing owner assignments.

1. Configure SCIM provisioning or LDAP sync between the identity provider and the privacy platform.
2. Map AD groups to privacy platform roles (DPO, Privacy Analyst, Processing Owner, Viewer).
3. Enable SSO via SAML 2.0 or OIDC.
4. Schedule daily sync to reflect organisational changes (new hires, role changes, departures).
5. Configure automated notifications when a processing owner's account is disabled (triggers RoPA ownership reassignment).

### IT Service Management Integration

**Purpose**: Trigger RoPA updates from IT change requests.

1. Configure a webhook from ServiceNow/Jira to the privacy platform.
2. When a change request is filed with the privacy impact flag set to "Yes" or "Unsure," the webhook creates a task in the privacy platform for DPO review.
3. The DPO assesses whether a RoPA update is required and either creates the update directly in the platform or confirms no change is needed.
4. The change request is updated with the privacy review outcome (DPO sign-off reference).

### Vendor Management Integration

**Purpose**: Sync processor information and DPA status with RoPA recipient fields.

1. If using OneTrust Vendorpedia, link vendor assessments to processing activities.
2. When a new vendor is onboarded and a DPA is executed, the platform auto-creates a recipient entry in the relevant RoPA entries.
3. When a vendor is terminated, the platform flags affected RoPA entries for update.
4. DPA expiry dates trigger automated renewal reminders and flag affected RoPA entries.

## Data Migration Workflow

### From Spreadsheet to Platform

1. **Audit the existing spreadsheet**: Count records, identify field inconsistencies, flag incomplete entries.
2. **Standardise column headers**: Map spreadsheet columns to the platform's import schema.
3. **Clean data**: Resolve inconsistencies, fill obvious gaps, standardise date formats and terminology.
4. **Export to CSV**: Produce a clean CSV file matching the platform's import template.
5. **Test import**: Import into a staging environment and validate 100% of records.
6. **Production import**: Import into the production platform after validation.
7. **Post-import QA**: Run the platform's completeness check and resolve any flagged issues.
8. **Establish relationships**: Link imported records to organisational entities, vendors, systems, and DPIAs within the platform.
9. **Decommission spreadsheet**: Archive the spreadsheet (do not delete — retain for historical reference) and communicate the cutover to all stakeholders.

## Ongoing Sync and Monitoring

### Daily Operations

- Identity sync runs at 02:00 UTC, updating organisational structure.
- Vendor management sync runs at 03:00 UTC, updating DPA status and vendor details.
- Automated completeness check runs at 06:00 UTC, generating alerts for any newly detected gaps.

### Weekly Operations

- IT change request review: DPO reviews accumulated change requests flagged for privacy impact.
- Platform health check: Verify API integrations are functioning (no failed sync jobs).

### Monthly Operations

- Generate maintenance status report from the platform.
- Review and resolve any long-standing alerts.
- Update platform configuration for any new regulatory templates released by supervisory authorities.

### Annual Operations

- Full RoPA review cycle managed through the platform's workflow engine.
- Platform vendor re-assessment (security, DPA compliance).
- License review and capacity planning for the coming year.
