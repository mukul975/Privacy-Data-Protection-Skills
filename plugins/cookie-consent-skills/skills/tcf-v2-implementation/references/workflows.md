# TCF v2.2 Implementation Workflows

## CMP Registration Workflow

1. Review IAB Europe CMP requirements and policies
2. Develop CMP software meeting TCF v2.2 Technical Specification
3. Implement __tcfapi stub and full API
4. Submit CMP for IAB Europe review and testing
5. Pass CMP validation tests
6. Receive CMP ID assignment
7. Deploy CMP with assigned CMP ID

## GVL Integration Workflow

1. Fetch latest GVL from vendor-list.consensu.org
2. Cache GVL locally (max staleness: 24 hours)
3. Filter vendor list to only vendors used by the publisher
4. Map vendor purposes to consent UI categories
5. Display vendor information in consent detail layer
6. Update GVL cache weekly via automated job

## TC String Generation Workflow

1. User interacts with CMP consent interface
2. CMP records per-purpose consent decisions
3. CMP records per-vendor consent decisions
4. CMP applies publisher restrictions
5. CMP encodes all decisions into TC String binary format
6. TC String is base64url-encoded
7. TC String stored in first-party cookie (euconsent-v2)
8. TC String made available via __tcfapi('getTCData')
9. Vendor scripts read TC String and act accordingly

## Publisher Restriction Configuration Workflow

1. Review vendor-declared legal bases in GVL
2. Identify vendors claiming legitimate interest where publisher requires consent
3. Configure publisher restrictions (restrictionType: 1 = require consent)
4. Encode restrictions in TC String publisher restrictions segment
5. Test that restricted vendors receive correct signals
6. Document restriction rationale for compliance records

## TCF Compliance Validation Workflow

1. Load page and verify __tcfapi is available before vendor scripts
2. Call __tcfapi('ping') to verify CMP status
3. Interact with consent UI (accept/reject)
4. Call __tcfapi('getTCData') to read TC String
5. Decode TC String and verify purpose consent matches UI selections
6. Verify vendor consent matches UI selections
7. Check publisher restrictions are correctly encoded
8. Verify TC String is transmitted in ad bid requests (OpenRTB consent field)
9. Monitor for vendor compliance with consent signals
