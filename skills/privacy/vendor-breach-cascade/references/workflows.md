# Workflows — Vendor Breach Cascade

## Workflow 1: Vendor Breach Notification Cascade Response

```
TRIGGER: Summit Cloud Partners receives breach notification from a vendor (processor)
  │
  ├─► Phase 1: Initial Response (T+0 to T+2 hours)
  │     ├─ Step 1.1: On-call Privacy Team member logs notification:
  │     │     ├─ Vendor name and contact person
  │     │     ├─ Date/time vendor became aware
  │     │     ├─ Date/time of notification to Summit
  │     │     ├─ Initial breach description
  │     │     └─ Assign breach case ID (BREACH-YYYY-NNN)
  │     │
  │     ├─ Step 1.2: Verify notification authenticity
  │     │     ├─ Confirm sender is authorized DPA contact
  │     │     └─ If uncertain: call vendor DPO on registered number
  │     │
  │     ├─ Step 1.3: Acknowledge receipt to vendor (within 30 minutes)
  │     │     └─ "Summit Cloud Partners acknowledges receipt of breach notification
  │     │         [BREACH-YYYY-NNN]. We will revert with information requests."
  │     │
  │     ├─ Step 1.4: Alert Breach Response Team
  │     │     ├─ DPO: Dr. Maria Santos
  │     │     ├─ InfoSec Lead: designated on-call
  │     │     ├─ Legal Counsel: designated contact
  │     │     └─ Business Unit Owner: for affected services
  │     │
  │     └─ Step 1.5: Initial severity classification
  │           ├─ Critical / High / Medium / Low
  │           └─ Activate appropriate response level
  │
  ├─► Phase 2: Assessment (T+2 to T+24 hours)
  │     ├─ Step 2.1: Send detailed information request to vendor:
  │     │     ├─ Root cause (known or suspected)
  │     │     ├─ Exact data categories compromised
  │     │     ├─ Exact or estimated data subject count
  │     │     ├─ Breach timeline (occurrence, detection, containment)
  │     │     ├─ Evidence of data exfiltration
  │     │     ├─ Current containment status
  │     │     ├─ Forensic investigation status
  │     │     └─ Impact on other clients
  │     │
  │     ├─ Step 2.2: Internal impact analysis
  │     │     ├─ Cross-reference vendor's data access with DPA Annex I
  │     │     ├─ Identify specific Summit data subjects affected
  │     │     ├─ Assess data sensitivity level
  │     │     └─ Determine if breach involves cross-border elements
  │     │
  │     ├─ Step 2.3: Risk assessment (DPO)
  │     │     ├─ Apply EDPB risk assessment criteria:
  │     │     │     ├─ Type of breach (confidentiality, integrity, availability)
  │     │     │     ├─ Nature, sensitivity, volume of data
  │     │     │     ├─ Ease of identification of data subjects
  │     │     │     ├─ Severity of consequences for data subjects
  │     │     │     ├─ Number of data subjects
  │     │     │     └─ Special characteristics (children, vulnerable persons)
  │     │     ├─ Determine: risk / no risk / high risk
  │     │     └─ Document assessment rationale
  │     │
  │     └─ Step 2.4: Determine notification obligations
  │           ├─ Supervisory authority notification required? (Art. 33)
  │           ├─ Data subject notification required? (Art. 34)
  │           ├─ Other controller notifications (if shared processor)?
  │           └─ Law enforcement notification (if criminal activity)?
  │
  ├─► Phase 3: Notifications (T+24 to T+72 hours from awareness)
  │     ├─ Step 3.1: Supervisory authority notification (if required)
  │     │     ├─ Complete notification form per local SA requirements
  │     │     ├─ Include all Art. 33(3) required elements
  │     │     ├─ File via SA online portal (preferred) or encrypted email
  │     │     ├─ Mark if phased notification (Art. 33(4))
  │     │     └─ Record filing timestamp and confirmation
  │     │
  │     ├─ Step 3.2: Data subject notification (if high risk — Art. 34)
  │     │     ├─ Draft notification in clear, plain language
  │     │     ├─ Include: breach description, DPO contact, likely consequences, measures
  │     │     ├─ Include recommended protective actions for data subjects
  │     │     ├─ Delivery method: direct email to affected individuals
  │     │     └─ If disproportionate effort: public communication
  │     │
  │     └─ Step 3.3: Internal notifications
  │           ├─ Notify affected business units
  │           ├─ Brief senior management
  │           └─ Prepare external communications (press, customers) if needed
  │
  ├─► Phase 4: Coordinated Response (T+72 hours onwards)
  │     ├─ Step 4.1: Monitor vendor investigation progress
  │     │     ├─ Scheduled update calls (daily for Critical, every 48 hours for High)
  │     │     └─ Track investigation milestones
  │     │
  │     ├─ Step 4.2: Receive and review root cause analysis
  │     ├─ Step 4.3: Review vendor remediation plan
  │     ├─ Step 4.4: Verify remediation implementation
  │     │
  │     ├─ Step 4.5: File supplementary SA notification (if phased)
  │     │     └─ Provide additional details as they become available
  │     │
  │     └─ Step 4.6: Update data subjects (if new information material to their risk)
  │
  └─► Phase 5: Post-Incident (within 90 days)
        ├─ Step 5.1: Complete breach register entry with full details
        ├─ Step 5.2: Update vendor risk score (per risk scoring model)
        ├─ Step 5.3: Evaluate contractual remedies with Legal
        ├─ Step 5.4: Conduct lessons-learned review
        ├─ Step 5.5: Update breach response procedures based on lessons learned
        └─ Step 5.6: Schedule vendor verification audit (within 6 months)
```

## Workflow 2: Multi-Party Vendor Breach Coordination

```
TRIGGER: Vendor notifies that breach affects multiple controllers
  │
  ├─► Step 1: Assess Summit-Specific Impact
  │     ├─ Determine which Summit data and data subjects are affected
  │     ├─ Request Summit-specific forensic results
  │     └─ Do NOT rely on vendor's generic assessment for Summit notification decisions
  │
  ├─► Step 2: Independent Notification Decision
  │     ├─ Summit makes its own SA notification decision
  │     ├─ Summit makes its own data subject notification decision
  │     └─ Summit coordinates timing with vendor (but does not delay for vendor)
  │
  ├─► Step 3: Coordination with Other Controllers (if appropriate)
  │     ├─ Where vendor facilitates joint communication among affected controllers
  │     ├─ Share lessons learned (without disclosing proprietary information)
  │     └─ Coordinate with lead supervisory authority if cross-border
  │
  └─► Step 4: Joint Remediation Oversight
        ├─ Participate in vendor-organized multi-party remediation planning
        └─ Ensure Summit-specific remediation requirements are addressed
```
