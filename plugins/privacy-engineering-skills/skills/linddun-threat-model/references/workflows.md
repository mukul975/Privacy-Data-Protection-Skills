# LINDDUN Privacy Threat Modeling — Workflows

## Workflow 1: Full LINDDUN Threat Modeling Session

### Prerequisites
- System architecture documentation
- Data flow diagrams (or create during session)
- Privacy requirements from stakeholders
- Threat modeling facilitator with LINDDUN expertise

### Steps
1. **System Scoping** (30 min): Define system boundaries and trust boundaries
2. **DFD Construction** (45 min): Create privacy-annotated data flow diagram
3. **Threat Mapping** (90 min): Walk through each LINDDUN category per DFD element
4. **Threat Tree Analysis** (60 min): Build threat trees for identified threats
5. **Risk Prioritization** (30 min): Score using likelihood x impact matrix
6. **Mitigation Selection** (45 min): Select controls for high/critical risks
7. **Documentation** (30 min): Record findings in threat register

### Outputs
- Privacy-annotated DFD
- LINDDUN threat register
- Risk-prioritized mitigation plan

## Workflow 2: LINDDUN GO (Lightweight)

### Steps
1. **System Description** (15 min): Brief overview and key data flows
2. **Category Cards** (45 min): Use LINDDUN GO cards to identify threats
3. **Quick Risk Assessment** (15 min): High/Medium/Low rating per threat
4. **Action Items** (15 min): Assign top-priority mitigations

### Outputs
- Lightweight threat list with risk ratings
- Prioritized action items

## Workflow 3: LINDDUN + STRIDE Integration

### Steps
1. **Shared DFD**: Build single DFD for both security and privacy analysis
2. **STRIDE Pass**: Identify security threats per DFD element
3. **LINDDUN Pass**: Identify privacy threats per DFD element
4. **Cross-Reference**: Map overlapping threats (e.g., Data Disclosure / Information Disclosure)
5. **Unified Mitigation**: Select controls addressing both security and privacy threats
6. **Combined Report**: Produce integrated threat model document
