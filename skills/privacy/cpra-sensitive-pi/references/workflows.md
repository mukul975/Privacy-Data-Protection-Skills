# Workflows — CPRA Sensitive Personal Information

## Workflow 1: Limit Request Processing

```
START: Consumer clicks "Limit the Use of My Sensitive Personal Information" link
  │
  ├─► Step 1: Request Receipt
  │     ├─ No identity verification required
  │     ├─ Log: timestamp, session ID, consumer ID (if authenticated)
  │     └─ If unauthenticated: apply limit to session/device
  │
  ├─► Step 2: Identify Sensitive PI Categories Processed for Consumer
  │     ├─ Query data inventory for consumer's sensitive PI records
  │     ├─ Categories found for Liberty Commerce Inc.:
  │     │     ├─ Precise geolocation (mobile app usage)
  │     │     ├─ Payment credentials (transaction processing)
  │     │     ├─ Government ID (marketplace seller tax reporting — if applicable)
  │     │     └─ Racial/ethnic origin (optional survey — if provided)
  │     └─ Categories not collected: genetic, biometric, union, religious, sex life
  │
  ├─► Step 3: Apply Purpose Restrictions
  │     ├─ For each sensitive PI category, restrict to permitted purposes only:
  │     │     ├─ Geolocation: BLOCK targeted ads, location-based marketing
  │     │     │     └─ PERMIT: delivery tracking, active store finder request
  │     │     ├─ Payment credentials: BLOCK profile enrichment, cross-referencing
  │     │     │     └─ PERMIT: transaction processing, fraud detection
  │     │     ├─ Government ID: BLOCK any non-original purpose
  │     │     │     └─ PERMIT: tax reporting (SSN), age verification (DL)
  │     │     └─ Racial/ethnic origin: BLOCK all processing
  │     │           └─ DELETE survey response data within 30 days
  │     │
  │     └─ Update data access controls in real time
  │
  ├─► Step 4: Downstream Propagation
  │     ├─ Notify service providers of limit status
  │     ├─ Update consent management platform
  │     └─ Adjust advertising tag configuration (suppress sensitive PI signals)
  │
  └─► Step 5: Confirmation
        ├─ Display confirmation to consumer
        ├─ Log limit application for compliance audit
        └─ Effective within 15 business days (typically immediate)
```

## Workflow 2: Sensitive PI Collection Assessment

```
TRIGGER: New data collection activity proposed by business unit
  │
  ├─► Step 1: Classify Data Elements
  │     ├─ Review proposed data elements against §1798.140(ae) categories
  │     ├─ For each element, determine:
  │     │     ├─ Is this sensitive PI? (Y/N)
  │     │     ├─ Which specific category? (1-11)
  │     │     └─ Is collection reasonably necessary and proportionate? (§1798.100(c))
  │     └─ Document classification decisions with reasoning
  │
  ├─► Step 2: Purpose Assessment
  │     ├─ For each sensitive PI element:
  │     │     ├─ What is the specific business purpose?
  │     │     ├─ Is this purpose one of the §1798.121(a) permitted purposes?
  │     │     ├─ Could the purpose be achieved without sensitive PI?
  │     │     └─ What is the retention period?
  │     └─ If purpose is not a permitted purpose under §1798.121(a):
  │           └─ Business must be prepared to cease this use upon limit request
  │
  ├─► Step 3: Privacy Notice Update
  │     ├─ Add new sensitive PI category to privacy notice
  │     ├─ Disclose specific purpose for each category
  │     ├─ State retention period
  │     └─ Confirm "Limit" link is functional for new category
  │
  ├─► Step 4: Technical Controls
  │     ├─ Implement purpose-based access controls
  │     ├─ Configure data segregation for sensitive PI
  │     ├─ Ensure limit-request workflow includes new category
  │     └─ Test: verify limit request properly restricts new category
  │
  └─► Step 5: Approval
        ├─ Privacy team sign-off
        ├─ Legal review of necessity and proportionality
        └─ Document approval in data processing register
```

## Workflow 3: Quarterly Sensitive PI Audit

```
TRIGGER: Quarterly audit schedule
  │
  ├─► Step 1: Inventory Verification
  │     ├─ Review all sensitive PI categories currently collected
  │     ├─ Verify against data inventory records
  │     └─ Identify any new or discontinued sensitive PI processing
  │
  ├─► Step 2: Purpose Compliance Check
  │     ├─ For each sensitive PI category:
  │     │     ├─ Verify current processing matches stated purpose
  │     │     ├─ Check for purpose creep (use beyond original scope)
  │     │     └─ Verify consumers with limit requests have restricted processing
  │     └─ Review system access logs for unauthorized sensitive PI access
  │
  ├─► Step 3: Limit Request Effectiveness
  │     ├─ Sample consumers who submitted limit requests
  │     ├─ Verify sensitive PI processing is restricted to permitted purposes
  │     ├─ Test: attempt to use limited consumer's sensitive PI for blocked purpose
  │     └─ Confirm downstream service providers are honoring limits
  │
  ├─► Step 4: Retention Compliance
  │     ├─ Verify sensitive PI is not retained beyond stated periods
  │     ├─ Check that deleted survey data (racial/ethnic) is purged for limit consumers
  │     └─ Confirm backup systems reflect deletion/restriction
  │
  └─► Step 5: Audit Report
        ├─ Document findings, gaps, and remediation actions
        ├─ Report to CPO and legal counsel
        └─ Update data processing register as needed
```
