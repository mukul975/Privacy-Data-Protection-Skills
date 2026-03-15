# Group Structure RoPA Workflow Reference

## Entity-Level RoPA Creation Workflow

### For Each Entity in the Group

1. **Determine entity role**: Is this entity a controller, processor, or both for each processing activity?
2. **Create entity-level RoPA**: Using the group standard template, populate all fields for processing activities where this entity is controller.
3. **Create processor records**: For activities where this entity processes on behalf of other group entities, create Art. 30(2) records.
4. **Document intra-group relationships**: Record all intra-group data flows as recipients (Art. 30(1)(d)) and transfers (Art. 30(1)(e) if cross-border).
5. **Reference intra-group agreements**: Link to Art. 28 intra-group DPAs and Art. 26 joint controller arrangements.

## Consolidated View Assembly Workflow

### Quarterly Aggregation

1. **Collect entity exports**: Each entity privacy lead exports their RoPA in the group standard JSON/CSV format.
2. **Merge into consolidated view**: Group privacy analyst aggregates all entity exports, tagging each entry with the source entity.
3. **Intra-group flow validation**: Verify that intra-group transfers appear in both the disclosing and receiving entity's records.
4. **Consistency check**: Ensure joint controller arrangements are recorded consistently by all participating entities.
5. **Gap analysis**: Identify entities with incomplete records, missing DPAs, or undocumented transfers.
6. **Publish consolidated view**: Make available to group DPO and entity privacy leads.

## Post-Acquisition Integration Workflow

### Timeline for Integrating Acquired Entity

| Milestone | Timeline | Activities |
|-----------|----------|-----------|
| Day 1 | Immediate | Obtain existing RoPA from acquired entity. Assess format and completeness. |
| Week 1-2 | First 14 days | Map acquired entity's processing activities. Identify personal data flows. |
| Week 3-4 | Days 15-30 | Conduct gap analysis against group RoPA template. Identify missing fields. |
| Month 2 | Days 31-60 | Migrate RoPA to group template format. Establish intra-group DPAs. |
| Month 3 | Days 61-90 | Document new intra-group transfers. Update both entities' RoPAs. |
| Month 4-6 | Days 91-180 | Full integration into consolidated view. Align with group governance cycle. |

### Day 1 Due Diligence Checklist

- [ ] Does the acquired entity have an existing RoPA?
- [ ] In what format (spreadsheet, tool, document)?
- [ ] How many processing activities are recorded?
- [ ] Does it include processor records (Art. 30(2))?
- [ ] Who is the current DPO or privacy contact?
- [ ] What privacy management tools are in use?
- [ ] Are there existing DPAs with processors?
- [ ] Are there international transfers?
- [ ] What supervisory authority has jurisdiction?
- [ ] Are there any pending SA investigations or complaints?

## Intra-Group Transfer Documentation Workflow

### Step 1: Map All Intra-Group Data Flows

1. Identify all systems shared across group entities.
2. Map which entities can access which systems and what data.
3. Identify shared service arrangements (IT, HR, Finance).
4. Map any centralised databases or data warehouses.
5. Identify global systems (e.g., group-wide CRM, ERP, HRIS).

### Step 2: Classify Each Flow

| Classification | Example | Legal Requirement |
|---------------|---------|-------------------|
| Controller-to-controller (intra-group) | Employee directory sharing | Art. 6 lawful basis + Chapter V transfer mechanism (if cross-border EEA/non-EEA) |
| Controller-to-processor (intra-group) | Shared service centre | Art. 28 DPA + Chapter V transfer mechanism |
| Joint controllers | Multi-country clinical trial | Art. 26 arrangement + Chapter V transfer mechanism |
| Processor-to-sub-processor (intra-group) | Shared services engaging group IT | Art. 28(4) sub-processor DPA + Chapter V |

### Step 3: Document in Both Entities' RoPAs

For each intra-group flow, ensure:

1. The disclosing entity records the receiving entity as a recipient in Art. 30(1)(d).
2. If the receiving entity is outside the EEA, the disclosing entity records the transfer in Art. 30(1)(e) with the transfer mechanism.
3. If the receiving entity is a processor, it records the relationship in its Art. 30(2)(a).
4. All intra-group DPAs, joint controller arrangements, and BCR references are cross-linked.

## RACI Matrix for Group RoPA

| Activity | Group DPO | Entity Privacy Lead | Shared Services | Group Privacy Analyst |
|----------|-----------|--------------------|-----------------|-----------------------|
| Entity-level RoPA creation | A | R | R (for processor records) | C |
| Intra-group DPA negotiation | A | R | R | C |
| Consolidated view assembly | A | C | C | R |
| Cross-entity gap analysis | A | I | I | R |
| Board reporting | R | I | I | C |
| Post-acquisition integration | A | R (acquiring entity) | C | R |
| BCR maintenance | R | C | C | C |

(R = Responsible, A = Accountable, C = Consulted, I = Informed)
