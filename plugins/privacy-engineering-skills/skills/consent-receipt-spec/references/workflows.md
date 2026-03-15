# Consent Receipt Specification — Workflows

## Workflow 1: Receipt Issuance
1. Data subject provides consent via form/API/verbal
2. System captures consent details (purposes, data categories, timestamp)
3. Receipt payload assembled per Kantara specification
4. Receipt signed as JWT using organization's private key
5. Receipt ID and JWT returned to data subject
6. Receipt stored in consent management database
7. Receipt activated for ongoing processing

## Workflow 2: Receipt Verification
1. Data subject or auditor presents receipt JWT
2. System extracts issuer from JWT header
3. System retrieves issuer's public key from registry
4. JWT signature verified cryptographically
5. Required Kantara fields validated
6. Consent status checked (active, withdrawn, expired)
7. Verification result returned

## Workflow 3: Receipt Lifecycle Management
1. Consent receipt issued (ISSUED state)
2. Receipt activated after verification (ACTIVE state)
3. If consent scope changes, new receipt issued (old marked UPDATED)
4. If consent withdrawn, receipt marked WITHDRAWN
5. Expired receipts archived (ARCHIVED state)
6. Full receipt history maintained for audit trail
