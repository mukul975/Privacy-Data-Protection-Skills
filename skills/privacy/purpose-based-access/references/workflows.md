# Purpose-Based Access Control — Workflows

## Workflow 1: Purpose Ontology Development
1. Inventory all processing purposes from ROPA
2. Build hierarchical purpose taxonomy
3. Map legal bases to each purpose
4. Define data category allowlists per purpose
5. Set retention periods per purpose
6. Review with legal and business stakeholders
7. Publish purpose registry

## Workflow 2: PBAC Policy Engine Deployment
1. Define access policies linking roles, purposes, and data categories
2. Implement purpose validation middleware
3. Integrate consent store for consent-dependent purposes
4. Configure audit logging for all access decisions
5. Deploy SQL proxy with purpose enforcement
6. Test with representative access scenarios
7. Enable monitoring and alerting

## Workflow 3: Purpose Verification at Query Time
1. Requester submits query with purpose declaration
2. System validates purpose exists and is active
3. System checks data category alignment
4. System verifies consent (if required)
5. ABAC policies evaluated
6. Decision issued (PERMIT/DENY) with obligations
7. Full audit trail recorded
