# Automated RoPA Generation Workflow Reference

## End-to-End Automated Generation Process

### Phase 1: Source System Configuration

1. **Azure AD / Okta connection**: Configure read-only API access to the identity provider to extract enterprise application registrations, security groups, and conditional access policies.
2. **Cloud catalog connection**: Configure read-only access to AWS Organizations, Azure Subscriptions, or GCP Projects to enumerate services, regions, and resource tags.
3. **API gateway connection**: Configure log export from API Gateway (AWS API Gateway, Azure API Management, Kong, Apigee) to the analysis engine.
4. **Database connection**: Configure read-only schema access (no data access) to databases identified in the cloud catalog.

**Principle of least privilege**: The automated system requires only metadata access, never access to the personal data itself. Schema-only database connections, log analysis (not payload inspection), and read-only API access.

### Phase 2: Discovery Scan

#### Step 2.1: Application Discovery (Azure AD)

1. Query Microsoft Graph API for all enterprise applications and service principals.
2. For each application, extract: application name, description, publisher, sign-on URL, assigned users/groups.
3. Map applications to departments based on assigned security groups.
4. Identify applications with personal data indicators (HR systems, CRM, clinical systems, analytics).

#### Step 2.2: Cloud Service Enumeration

1. List all cloud services in use across all regions and accounts.
2. For each service instance, extract: service type, region, encryption configuration, access policies, resource tags.
3. Flag services in non-EEA regions as potential international transfers.
4. Identify services with data classification tags indicating personal data.

#### Step 2.3: API Data Flow Analysis

1. Parse API gateway access logs to identify all API endpoints processing personal data.
2. For each endpoint, determine: request/response data fields, upstream source, downstream destination, request volume, external vs internal callers.
3. Build a data flow graph showing how personal data moves between systems.
4. Identify external API calls (third-party integrations) as potential recipient disclosures.

#### Step 2.4: Database Schema Scanning

1. Connect to each database with read-only schema access.
2. Extract all table and column definitions.
3. Apply PII detection patterns to column names and data types.
4. Flag tables containing personal data indicators.
5. Analyze foreign key relationships to understand data flows between tables.

### Phase 3: Draft RoPA Entry Generation

For each discovered processing activity:

1. **Create entry skeleton**: Generate a unique record ID and populate the processing activity name from the source system name.
2. **Populate controller identity**: Auto-fill from organisation configuration (standard across all entries).
3. **Draft purpose**: Extract from application description. Mark as "DRAFT — DPO review required."
4. **Populate data categories**: From database schema PII detection results.
5. **Populate data subject categories**: Infer from table names and context (e.g., "employees" table suggests employee data subjects).
6. **Populate recipients**: Internal recipients from AD security groups, external recipients from API gateway external calls.
7. **Flag transfers**: Any non-EEA cloud region or API call to non-EEA endpoints.
8. **Detect retention**: Analyze oldest records in database tables to determine actual data age.
9. **Extract security measures**: From cloud encryption settings, AD conditional access, API gateway WAF configuration.

### Phase 4: Human Review and Enrichment

**Mandatory human review items:**

- Purpose articulation (automated draft is always insufficient for Art. 5(1)(b))
- Lawful basis determination (cannot be automated)
- Retention period policy (actual retention observed vs intended retention policy)
- DPA references for identified processors
- DPIA assessment (whether a DPIA is required)
- Processing owner assignment
- Art. 9(2) condition identification for special category data

### Phase 5: Validation and Registration

1. Run the RoPA validation script against all generated entries.
2. DPO reviews all entries flagged with "DRAFT" fields.
3. Processing owners confirm accuracy of their entries.
4. Approved entries are imported into the RoPA management platform.
5. Review dates are set (12 months for standard, 6 months for high-risk).

## Scan Scheduling

| Scan Type | Frequency | Purpose |
|-----------|-----------|---------|
| Full discovery scan | Quarterly | Identify new processing activities |
| Delta scan (AD changes) | Daily | Detect new applications, group changes |
| API gateway analysis | Weekly | Detect new data flows and integrations |
| Database schema scan | Monthly | Detect new tables and columns |
| Transfer detection | Daily | Flag any new non-EEA service deployments |

## RACI for Automated RoPA

| Activity | Responsible | Accountable | Consulted | Informed |
|----------|------------|-------------|-----------|----------|
| Source system configuration | IT / DevOps | CISO | DPO | — |
| Discovery scan execution | Automated (scheduled) | DPO | IT | — |
| Draft entry generation | Automated | DPO | — | Processing owners |
| Purpose articulation | Processing owner | DPO | Legal | — |
| Lawful basis determination | DPO | DPO | Legal | Processing owner |
| Final approval | DPO | DPO | Processing owner | Senior management |
