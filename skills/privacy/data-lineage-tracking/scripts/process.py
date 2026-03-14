"""
Data Lineage Tracking - Lineage Graph Builder and Analyzer

Builds a directed acyclic graph of personal data flows between systems,
identifies compliance gaps, and generates lineage reports for GDPR Art. 30
RoPA integration.
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Set, Tuple


class LineageNode:
    """Represents a system or processing stage in the data lineage."""

    def __init__(
        self,
        node_id: str,
        name: str,
        node_type: str,
        data_categories: List[str],
        legal_basis: str,
        retention_days: int,
        storage_location: str,
        encryption: bool = True,
        special_category: bool = False,
    ):
        self.node_id = node_id
        self.name = name
        self.node_type = node_type  # collection, transformation, storage, output, deletion
        self.data_categories = data_categories
        self.legal_basis = legal_basis
        self.retention_days = retention_days
        self.storage_location = storage_location
        self.encryption = encryption
        self.special_category = special_category
        self.ropa_entry_id: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "node_id": self.node_id,
            "name": self.name,
            "type": self.node_type,
            "data_categories": self.data_categories,
            "legal_basis": self.legal_basis,
            "retention_days": self.retention_days,
            "storage_location": self.storage_location,
            "encryption": self.encryption,
            "special_category": self.special_category,
            "ropa_entry_id": self.ropa_entry_id,
        }


class LineageEdge:
    """Represents a data flow between two lineage nodes."""

    def __init__(
        self,
        source_id: str,
        target_id: str,
        transfer_mechanism: str,
        transformation: Optional[str] = None,
        cross_border: bool = False,
        transfer_safeguard: Optional[str] = None,
        frequency: str = "continuous",
    ):
        self.source_id = source_id
        self.target_id = target_id
        self.transfer_mechanism = transfer_mechanism
        self.transformation = transformation
        self.cross_border = cross_border
        self.transfer_safeguard = transfer_safeguard
        self.frequency = frequency

    def to_dict(self) -> Dict:
        return {
            "source": self.source_id,
            "target": self.target_id,
            "mechanism": self.transfer_mechanism,
            "transformation": self.transformation,
            "cross_border": self.cross_border,
            "transfer_safeguard": self.transfer_safeguard,
            "frequency": self.frequency,
        }


class DataLineageGraph:
    """Directed acyclic graph tracking personal data flows."""

    def __init__(self, organization: str):
        self.organization = organization
        self.nodes: Dict[str, LineageNode] = {}
        self.edges: List[LineageEdge] = []
        self.created_at = datetime.now()

    def add_node(self, node: LineageNode) -> None:
        self.nodes[node.node_id] = node

    def add_edge(self, edge: LineageEdge) -> None:
        if edge.source_id not in self.nodes:
            raise ValueError(f"Source node {edge.source_id} not found in graph")
        if edge.target_id not in self.nodes:
            raise ValueError(f"Target node {edge.target_id} not found in graph")
        self.edges.append(edge)

    def get_downstream_nodes(self, node_id: str) -> Set[str]:
        """Find all nodes downstream from a given node (for breach impact scoping)."""
        visited = set()
        queue = [node_id]
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            for edge in self.edges:
                if edge.source_id == current and edge.target_id not in visited:
                    queue.append(edge.target_id)
        visited.discard(node_id)
        return visited

    def get_upstream_nodes(self, node_id: str) -> Set[str]:
        """Find all nodes upstream from a given node (for source tracing)."""
        visited = set()
        queue = [node_id]
        while queue:
            current = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            for edge in self.edges:
                if edge.target_id == current and edge.source_id not in visited:
                    queue.append(edge.source_id)
        visited.discard(node_id)
        return visited

    def find_all_paths(self, source_id: str, target_id: str) -> List[List[str]]:
        """Find all paths between two nodes in the lineage graph."""
        paths = []
        adjacency = {}
        for edge in self.edges:
            adjacency.setdefault(edge.source_id, []).append(edge.target_id)

        def dfs(current: str, target: str, path: List[str]):
            if current == target:
                paths.append(list(path))
                return
            for neighbor in adjacency.get(current, []):
                if neighbor not in path:
                    path.append(neighbor)
                    dfs(neighbor, target, path)
                    path.pop()

        dfs(source_id, target_id, [source_id])
        return paths

    def get_cross_border_transfers(self) -> List[LineageEdge]:
        """Identify all cross-border transfers requiring Art. 44-49 safeguards."""
        return [e for e in self.edges if e.cross_border]

    def get_special_category_paths(self) -> List[Tuple[str, Set[str]]]:
        """Find all paths containing Art. 9 special category data."""
        results = []
        for node_id, node in self.nodes.items():
            if node.special_category:
                downstream = self.get_downstream_nodes(node_id)
                results.append((node_id, downstream))
        return results

    def compliance_gaps(self) -> List[Dict]:
        """Identify compliance gaps in the lineage."""
        gaps = []

        # Check for unencrypted nodes
        for node_id, node in self.nodes.items():
            if not node.encryption:
                gaps.append({
                    "type": "encryption_missing",
                    "severity": "high",
                    "node": node_id,
                    "description": f"Node '{node.name}' lacks encryption at rest",
                    "remediation": "Implement AES-256 encryption at rest per Art. 32(1)(a)",
                })

        # Check for cross-border transfers without safeguards
        for edge in self.edges:
            if edge.cross_border and not edge.transfer_safeguard:
                gaps.append({
                    "type": "transfer_safeguard_missing",
                    "severity": "critical",
                    "edge": f"{edge.source_id} -> {edge.target_id}",
                    "description": "Cross-border transfer without Art. 44-49 safeguard",
                    "remediation": "Implement SCCs (Art. 46(2)(c)), BCRs (Art. 47), or identify applicable derogation (Art. 49)",
                })

        # Check for nodes without legal basis
        for node_id, node in self.nodes.items():
            if not node.legal_basis:
                gaps.append({
                    "type": "legal_basis_missing",
                    "severity": "critical",
                    "node": node_id,
                    "description": f"Node '{node.name}' has no documented legal basis",
                    "remediation": "Document Art. 6(1) legal basis for this processing activity",
                })

        # Check for nodes without RoPA linkage
        for node_id, node in self.nodes.items():
            if not node.ropa_entry_id:
                gaps.append({
                    "type": "ropa_linkage_missing",
                    "severity": "medium",
                    "node": node_id,
                    "description": f"Node '{node.name}' not linked to Art. 30 RoPA entry",
                    "remediation": "Create or link to existing RoPA entry covering this processing",
                })

        # Check for special category data without Art. 9(2) basis
        for node_id, node in self.nodes.items():
            if node.special_category and node.legal_basis and "Art. 9" not in node.legal_basis:
                gaps.append({
                    "type": "special_category_basis_missing",
                    "severity": "critical",
                    "node": node_id,
                    "description": f"Node '{node.name}' processes special category data without Art. 9(2) condition",
                    "remediation": "Document applicable Art. 9(2) condition (explicit consent, employment law, vital interests, etc.)",
                })

        # Check for excessive retention
        for node_id, node in self.nodes.items():
            if node.retention_days > 2555:  # ~7 years
                gaps.append({
                    "type": "excessive_retention",
                    "severity": "medium",
                    "node": node_id,
                    "description": f"Node '{node.name}' has retention of {node.retention_days} days ({node.retention_days // 365} years)",
                    "remediation": "Review whether retention period is necessary and proportionate per Art. 5(1)(e)",
                })

        return sorted(gaps, key=lambda g: {"critical": 0, "high": 1, "medium": 2, "low": 3}[g["severity"]])

    def generate_dsar_scope(self, data_subject_id: str) -> Dict:
        """Generate the list of systems to query for a DSAR response."""
        collection_nodes = [
            n for n in self.nodes.values() if n.node_type == "collection"
        ]
        all_systems = set()
        for cn in collection_nodes:
            all_systems.add(cn.node_id)
            downstream = self.get_downstream_nodes(cn.node_id)
            all_systems.update(downstream)

        systems_by_type = {
            "access_scope": [],
            "erasure_scope": [],
            "portability_scope": [],
        }

        for node_id in all_systems:
            node = self.nodes[node_id]
            systems_by_type["access_scope"].append({
                "system": node.name,
                "node_id": node_id,
                "data_categories": node.data_categories,
                "storage_location": node.storage_location,
            })
            if node.node_type != "deletion":
                systems_by_type["erasure_scope"].append({
                    "system": node.name,
                    "node_id": node_id,
                    "includes_backups": "backup" in node.name.lower(),
                })
            if node.node_type == "collection" and node.legal_basis in [
                "Art. 6(1)(a) consent",
                "Art. 6(1)(b) contract",
            ]:
                systems_by_type["portability_scope"].append({
                    "system": node.name,
                    "node_id": node_id,
                    "data_categories": node.data_categories,
                })

        return {
            "data_subject_id": data_subject_id,
            "generated_at": datetime.now().isoformat(),
            "total_systems": len(all_systems),
            "scopes": systems_by_type,
        }

    def generate_breach_impact(self, compromised_node_id: str) -> Dict:
        """Assess breach impact by tracing data flows from compromised node."""
        downstream = self.get_downstream_nodes(compromised_node_id)
        upstream = self.get_upstream_nodes(compromised_node_id)
        affected_nodes = downstream | upstream | {compromised_node_id}

        affected_categories = set()
        has_special_category = False
        has_cross_border = False
        affected_locations = set()

        for node_id in affected_nodes:
            node = self.nodes[node_id]
            affected_categories.update(node.data_categories)
            if node.special_category:
                has_special_category = True
            affected_locations.add(node.storage_location)

        for edge in self.edges:
            if edge.source_id in affected_nodes or edge.target_id in affected_nodes:
                if edge.cross_border:
                    has_cross_border = True

        risk_level = "low"
        if has_special_category:
            risk_level = "high"
        elif has_cross_border or len(affected_categories) > 3:
            risk_level = "medium"

        return {
            "compromised_system": self.nodes[compromised_node_id].name,
            "assessed_at": datetime.now().isoformat(),
            "affected_systems_count": len(affected_nodes),
            "affected_data_categories": sorted(affected_categories),
            "special_category_involved": has_special_category,
            "cross_border_involved": has_cross_border,
            "affected_locations": sorted(affected_locations),
            "risk_level": risk_level,
            "notification_required": risk_level in ["medium", "high"],
            "dpa_notification_deadline": (
                datetime.now() + timedelta(hours=72)
            ).isoformat() if risk_level in ["medium", "high"] else None,
        }

    def to_json(self) -> str:
        return json.dumps({
            "organization": self.organization,
            "created_at": self.created_at.isoformat(),
            "nodes": [n.to_dict() for n in self.nodes.values()],
            "edges": [e.to_dict() for e in self.edges],
            "statistics": {
                "total_nodes": len(self.nodes),
                "total_edges": len(self.edges),
                "collection_points": sum(1 for n in self.nodes.values() if n.node_type == "collection"),
                "storage_locations": sum(1 for n in self.nodes.values() if n.node_type == "storage"),
                "cross_border_flows": sum(1 for e in self.edges if e.cross_border),
                "special_category_nodes": sum(1 for n in self.nodes.values() if n.special_category),
            },
        }, indent=2)


def build_sample_lineage() -> DataLineageGraph:
    """Build a sample lineage graph for Meridian Analytics Ltd."""
    graph = DataLineageGraph("Meridian Analytics Ltd")

    # Collection points
    web_form = LineageNode(
        "col-web-form", "Customer Registration Form", "collection",
        ["name", "email", "phone", "address"],
        "Art. 6(1)(b) contract", 1095, "EU-West (Dublin)", True
    )
    web_form.ropa_entry_id = "ROPA-001"

    mobile_app = LineageNode(
        "col-mobile-app", "Mobile App Analytics", "collection",
        ["device_id", "usage_data", "location_data"],
        "Art. 6(1)(a) consent", 365, "EU-West (Dublin)", True
    )
    mobile_app.ropa_entry_id = "ROPA-002"

    hr_system = LineageNode(
        "col-hr-system", "HR Information System", "collection",
        ["employee_name", "payroll_data", "health_data", "performance_data"],
        "Art. 6(1)(b) contract / Art. 9(2)(b) employment law", 2555,
        "EU-West (Dublin)", True, True
    )
    hr_system.ropa_entry_id = "ROPA-003"

    # Transformation nodes
    etl_pipeline = LineageNode(
        "txn-etl-customer", "Customer Data ETL Pipeline", "transformation",
        ["name", "email", "usage_data", "customer_segment"],
        "Art. 6(1)(f) legitimate interest", 730, "EU-West (Dublin)", True
    )
    etl_pipeline.ropa_entry_id = "ROPA-004"

    pseudonymizer = LineageNode(
        "txn-pseudonymize", "Pseudonymization Service", "transformation",
        ["pseudonymized_id", "usage_patterns"],
        "Art. 6(1)(f) legitimate interest", 365, "EU-West (Dublin)", True
    )
    pseudonymizer.ropa_entry_id = "ROPA-005"

    # Storage nodes
    prod_db = LineageNode(
        "str-prod-db", "Production PostgreSQL Database", "storage",
        ["name", "email", "phone", "address", "usage_data"],
        "Art. 6(1)(b) contract", 1095, "EU-West (Dublin)", True
    )
    prod_db.ropa_entry_id = "ROPA-001"

    analytics_dw = LineageNode(
        "str-analytics-dw", "Analytics Data Warehouse", "storage",
        ["pseudonymized_id", "usage_patterns", "customer_segment"],
        "Art. 6(1)(f) legitimate interest", 730, "EU-Central (Frankfurt)", True
    )
    analytics_dw.ropa_entry_id = "ROPA-005"

    backup_sys = LineageNode(
        "str-backup", "Encrypted Backup Storage", "storage",
        ["name", "email", "phone", "address", "usage_data"],
        "Art. 6(1)(b) contract", 1460, "EU-West (Dublin)", True
    )
    backup_sys.ropa_entry_id = "ROPA-001"

    # Output nodes
    crm_export = LineageNode(
        "out-crm-export", "CRM Integration Export", "output",
        ["name", "email", "customer_segment"],
        "Art. 6(1)(b) contract", 1095, "US-East (Virginia)", True
    )
    crm_export.ropa_entry_id = "ROPA-006"

    # Add all nodes
    for node in [web_form, mobile_app, hr_system, etl_pipeline, pseudonymizer,
                 prod_db, analytics_dw, backup_sys, crm_export]:
        graph.add_node(node)

    # Add edges
    graph.add_edge(LineageEdge("col-web-form", "str-prod-db", "PostgreSQL INSERT", frequency="continuous"))
    graph.add_edge(LineageEdge("col-mobile-app", "str-prod-db", "REST API", frequency="continuous"))
    graph.add_edge(LineageEdge("str-prod-db", "txn-etl-customer", "SQL SELECT / Airflow DAG",
                               transformation="Join customer and usage data, derive segments", frequency="daily"))
    graph.add_edge(LineageEdge("txn-etl-customer", "txn-pseudonymize", "Internal API",
                               transformation="Replace identifiers with HMAC-SHA256 tokens", frequency="daily"))
    graph.add_edge(LineageEdge("txn-pseudonymize", "str-analytics-dw", "BigQuery LOAD", frequency="daily"))
    graph.add_edge(LineageEdge("str-prod-db", "str-backup", "pg_dump encrypted backup", frequency="daily"))
    graph.add_edge(LineageEdge("txn-etl-customer", "out-crm-export", "REST API",
                               cross_border=True, transfer_safeguard="EU SCCs (2021/914) Module 1",
                               frequency="weekly"))

    return graph


if __name__ == "__main__":
    graph = build_sample_lineage()

    print("=" * 70)
    print("DATA LINEAGE REPORT - Meridian Analytics Ltd")
    print("=" * 70)

    print(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"Nodes: {len(graph.nodes)}")
    print(f"Edges: {len(graph.edges)}")

    print("\n--- Cross-Border Transfers ---")
    for edge in graph.get_cross_border_transfers():
        src = graph.nodes[edge.source_id].name
        tgt = graph.nodes[edge.target_id].name
        print(f"  {src} -> {tgt}")
        print(f"    Safeguard: {edge.transfer_safeguard or 'NONE - COMPLIANCE GAP'}")

    print("\n--- Special Category Data Paths ---")
    for node_id, downstream in graph.get_special_category_paths():
        node = graph.nodes[node_id]
        print(f"  Source: {node.name}")
        if downstream:
            print(f"    Downstream systems: {', '.join(graph.nodes[d].name for d in downstream)}")
        else:
            print("    No downstream systems")

    print("\n--- Compliance Gaps ---")
    gaps = graph.compliance_gaps()
    if gaps:
        for gap in gaps:
            print(f"  [{gap['severity'].upper()}] {gap['type']}")
            print(f"    {gap['description']}")
            print(f"    Remediation: {gap['remediation']}")
    else:
        print("  No compliance gaps identified")

    print("\n--- DSAR Scope (Sample) ---")
    scope = graph.generate_dsar_scope("DS-12345")
    print(f"  Total systems to query: {scope['total_systems']}")
    print(f"  Access scope: {len(scope['scopes']['access_scope'])} systems")
    print(f"  Erasure scope: {len(scope['scopes']['erasure_scope'])} systems")
    print(f"  Portability scope: {len(scope['scopes']['portability_scope'])} systems")

    print("\n--- Breach Impact Assessment (Production DB Compromise) ---")
    impact = graph.generate_breach_impact("str-prod-db")
    print(f"  Affected systems: {impact['affected_systems_count']}")
    print(f"  Data categories: {', '.join(impact['affected_data_categories'])}")
    print(f"  Special category involved: {impact['special_category_involved']}")
    print(f"  Risk level: {impact['risk_level']}")
    print(f"  DPA notification required: {impact['notification_required']}")
    if impact['dpa_notification_deadline']:
        print(f"  72-hour deadline: {impact['dpa_notification_deadline']}")
