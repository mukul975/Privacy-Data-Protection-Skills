# Workflows — Evaluating Consent Management Platforms

## Workflow 1: CMP Selection Process

```
START: Organization decides to implement or replace CMP
  │
  ├─► Step 1: Requirements gathering (Week 1)
  │     ├─ Interview stakeholders: DPO, Legal, Engineering, Marketing
  │     ├─ Document: jurisdictions, domains, mobile apps, ad tech needs
  │     ├─ Define mandatory requirements (must-have)
  │     ├─ Define desirable requirements (nice-to-have)
  │     └─ Establish budget range
  │
  ├─► Step 2: Market research and shortlisting (Week 2)
  │     ├─ Research CMP vendors against requirements
  │     ├─ Check TCF v2.2 certification (IAB Europe registered CMP list)
  │     ├─ Check references and case studies
  │     ├─ Request pricing proposals
  │     └─ Shortlist 3-4 vendors for POC
  │
  ├─► Step 3: Proof of Concept (Weeks 3-6, 2 weeks per vendor)
  │     ├─ Implement on staging environment
  │     ├─ Test matrix:
  │     │   ├─ Consent collection flows (accept, refuse, manage)
  │     │   ├─ Withdrawal mechanism
  │     │   ├─ GPC detection
  │     │   ├─ Multi-jurisdiction logic
  │     │   ├─ API integration with backend
  │     │   ├─ Mobile SDK integration
  │     │   ├─ Page load performance measurement
  │     │   ├─ Consent record completeness (Art. 7(1))
  │     │   └─ A/B testing capabilities (within CNIL limits)
  │     └─ Document findings per vendor
  │
  ├─► Step 4: Scoring (Week 7)
  │     ├─ Score each vendor against weighted criteria
  │     ├─ Calculate weighted totals
  │     ├─ Present comparison to stakeholders
  │     └─ Select preferred vendor
  │
  ├─► Step 5: Procurement (Weeks 8-9)
  │     ├─ Negotiate contract terms
  │     ├─ Execute DPA (GDPR Article 28)
  │     ├─ Review sub-processor list
  │     ├─ Confirm data residency requirements
  │     └─ Finalize SLA terms
  │
  └─► Step 6: Implementation (Weeks 10-14)
        ├─ Technical implementation
        ├─ Cookie inventory and classification
        ├─ Banner design and configuration
        ├─ Integration testing
        ├─ DPO review and sign-off
        └─ Production deployment
```

## Workflow 2: CMP Proof of Concept Testing

```
TRIGGER: Shortlisted CMP vendor ready for POC evaluation
  │
  ├─► Day 1-2: Setup
  │     ├─ Create staging environment account
  │     ├─ Install CMP script on staging site
  │     ├─ Configure basic cookie categories
  │     └─ Set up for primary jurisdiction (e.g., EU/GDPR)
  │
  ├─► Day 3-5: Functional Testing
  │     ├─ Test 1: Accept All flow
  │     │   ├─ Verify all cookies load after acceptance
  │     │   ├─ Verify consent record created with all required fields
  │     │   └─ Verify TC String generated (if TCF enabled)
  │     │
  │     ├─ Test 2: Refuse All flow
  │     │   ├─ Verify no non-essential cookies loaded
  │     │   ├─ Verify consent record reflects refusal
  │     │   └─ Verify site remains fully functional
  │     │
  │     ├─ Test 3: Granular consent (manage preferences)
  │     │   ├─ Accept some categories, refuse others
  │     │   ├─ Verify only accepted categories load
  │     │   └─ Verify per-category consent records
  │     │
  │     ├─ Test 4: Withdrawal
  │     │   ├─ Accept all, then withdraw one category
  │     │   ├─ Verify withdrawal takes effect
  │     │   └─ Verify withdrawal record created
  │     │
  │     └─ Test 5: GPC detection
  │           ├─ Enable GPC in browser
  │           ├─ Verify CMP detects signal
  │           └─ Verify opt-out applied
  │
  ├─► Day 6-8: Integration Testing
  │     ├─ API: query consent state from backend
  │     ├─ Tag Manager: verify conditional tag firing
  │     ├─ Mobile SDK: test in iOS and Android apps
  │     └─ Server-side: verify consent propagation
  │
  ├─► Day 9-10: Performance and Reporting
  │     ├─ Measure page load impact (Lighthouse, WebPageTest)
  │     ├─ Review reporting dashboard
  │     ├─ Test consent record export
  │     └─ Document findings
  │
  └─► Day 10: POC Report
        ├─ Functional test results
        ├─ Performance measurements
        ├─ Integration compatibility
        ├─ Consent record quality
        └─ Overall recommendation
```
