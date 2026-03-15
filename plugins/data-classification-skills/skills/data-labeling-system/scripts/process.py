"""
Data Classification Labelling System
Manages sensitivity labels, auto-labelling rules, and label lifecycle.
"""

import json
from dataclasses import dataclass, field
from enum import Enum
from datetime import date, datetime


class LabelTier(Enum):
    PUBLIC = "Public"
    INTERNAL = "Internal"
    CONFIDENTIAL = "Confidential"
    RESTRICTED = "Restricted"


class LabelAction(Enum):
    APPLIED = "label_applied"
    UPGRADED = "label_upgraded"
    DOWNGRADED = "label_downgraded"
    REMOVED = "label_removed"
    AUTO_APPLIED = "auto_label_applied"
    INHERITED = "label_inherited"


TIER_RANK = {
    LabelTier.PUBLIC: 0,
    LabelTier.INTERNAL: 1,
    LabelTier.CONFIDENTIAL: 2,
    LabelTier.RESTRICTED: 3,
}


@dataclass
class SensitivityLabel:
    """A sensitivity label definition."""
    label_id: str
    name: str
    tier: LabelTier
    sub_label: str = ""
    colour: str = ""
    visual_marking_header: str = ""
    visual_marking_footer: str = ""
    encryption_enabled: bool = False
    encryption_type: str = ""
    dlp_policy: str = ""
    auto_apply_conditions: list[str] = field(default_factory=list)
    auto_apply_confidence: float = 0.85


@dataclass
class LabelEvent:
    """An audit event for label application or change."""
    event_id: str
    document_id: str
    document_name: str
    previous_label: str
    new_label: str
    action: LabelAction
    applied_by: str
    method: str
    justification: str
    timestamp: str


@dataclass
class LabelPolicy:
    """A label policy governing label behaviour."""
    policy_id: str
    name: str
    mandatory_labelling: bool
    default_label: str
    require_justification_downgrade: bool
    require_justification_removal: bool
    scope: list[str]


class LabellingEngine:
    """Manages sensitivity label application, inheritance, and audit."""

    def __init__(self):
        self.labels: dict[str, SensitivityLabel] = {}
        self.events: list[LabelEvent] = []
        self.event_counter = 0
        self._init_vanguard_labels()

    def _init_vanguard_labels(self):
        """Initialize Vanguard Financial Services label taxonomy."""
        labels = [
            SensitivityLabel("LBL-PUB", "Public", LabelTier.PUBLIC, colour="green",
                             visual_marking_footer="Vanguard Financial Services — Public"),
            SensitivityLabel("LBL-INT", "Internal", LabelTier.INTERNAL, colour="blue",
                             visual_marking_footer="Vanguard Financial Services — Internal Use Only"),
            SensitivityLabel("LBL-CONF-CUST", "Confidential - Customer Data", LabelTier.CONFIDENTIAL,
                             sub_label="Customer Data", colour="amber",
                             visual_marking_header="CONFIDENTIAL",
                             visual_marking_footer="CONFIDENTIAL — Vanguard Financial Services",
                             encryption_enabled=True, encryption_type="Azure RMS (AES-256)",
                             dlp_policy="VFS-DLP-Confidential",
                             auto_apply_conditions=["UK_NINO_HIGH", "IBAN_HIGH", "VFS_ACCOUNT_HIGH"],
                             auto_apply_confidence=0.85),
            SensitivityLabel("LBL-CONF-EMP", "Confidential - Employee Data", LabelTier.CONFIDENTIAL,
                             sub_label="Employee Data", colour="amber",
                             visual_marking_header="CONFIDENTIAL",
                             encryption_enabled=True, encryption_type="Azure RMS (AES-256)",
                             dlp_policy="VFS-DLP-Confidential"),
            SensitivityLabel("LBL-REST-SC", "Restricted - Special Category", LabelTier.RESTRICTED,
                             sub_label="Special Category (Art. 9)", colour="red",
                             visual_marking_header="RESTRICTED",
                             visual_marking_footer="RESTRICTED — Art. 9 Special Category Data",
                             encryption_enabled=True, encryption_type="Azure RMS (DKE)",
                             dlp_policy="VFS-DLP-Restricted",
                             auto_apply_conditions=["ICD10_MEDIUM", "HEALTH_CLASSIFIER_HIGH", "BIOMETRIC_HIGH"],
                             auto_apply_confidence=0.70),
            SensitivityLabel("LBL-REST-CRIM", "Restricted - Criminal Data", LabelTier.RESTRICTED,
                             sub_label="Criminal Data (Art. 10)", colour="red",
                             visual_marking_header="RESTRICTED",
                             encryption_enabled=True, encryption_type="Azure RMS (DKE)",
                             dlp_policy="VFS-DLP-Restricted",
                             auto_apply_conditions=["DBS_PATTERN", "CRIMINAL_TERMINOLOGY"],
                             auto_apply_confidence=0.80),
        ]
        for label in labels:
            self.labels[label.label_id] = label

    def apply_label(
        self,
        document_id: str,
        document_name: str,
        label_id: str,
        applied_by: str,
        method: str = "user",
        current_label_id: str = "",
        justification: str = "",
    ) -> LabelEvent:
        """Apply or change a label on a document."""
        new_label = self.labels.get(label_id)
        if not new_label:
            raise ValueError(f"Label {label_id} not found")

        current = self.labels.get(current_label_id)
        if current and TIER_RANK[new_label.tier] < TIER_RANK[current.tier]:
            action = LabelAction.DOWNGRADED
            if not justification:
                raise ValueError("Justification required for label downgrade")
        elif current and TIER_RANK[new_label.tier] > TIER_RANK[current.tier]:
            action = LabelAction.UPGRADED
        elif method == "auto":
            action = LabelAction.AUTO_APPLIED
        elif method == "inheritance":
            action = LabelAction.INHERITED
        else:
            action = LabelAction.APPLIED

        self.event_counter += 1
        event = LabelEvent(
            event_id=f"EVT-{self.event_counter:06d}",
            document_id=document_id,
            document_name=document_name,
            previous_label=current.name if current else "None",
            new_label=new_label.name,
            action=action,
            applied_by=applied_by,
            method=method,
            justification=justification,
            timestamp=datetime.now().isoformat(),
        )
        self.events.append(event)
        return event

    def apply_inheritance(
        self,
        parent_label_id: str,
        child_document_id: str,
        child_document_name: str,
        child_current_label_id: str = "",
    ) -> LabelEvent | None:
        """Apply label inheritance — child inherits parent label if parent is higher."""
        parent = self.labels.get(parent_label_id)
        child_current = self.labels.get(child_current_label_id)

        if not parent:
            return None

        if child_current and TIER_RANK[child_current.tier] >= TIER_RANK[parent.tier]:
            return None

        return self.apply_label(
            document_id=child_document_id,
            document_name=child_document_name,
            label_id=parent_label_id,
            applied_by="system",
            method="inheritance",
            current_label_id=child_current_label_id or "",
        )

    def generate_audit_report(self) -> dict:
        """Generate label activity audit report."""
        action_counts: dict[str, int] = {}
        label_counts: dict[str, int] = {}
        downgrades = []

        for event in self.events:
            action = event.action.value
            action_counts[action] = action_counts.get(action, 0) + 1
            label_counts[event.new_label] = label_counts.get(event.new_label, 0) + 1

            if event.action == LabelAction.DOWNGRADED:
                downgrades.append({
                    "document": event.document_name,
                    "from": event.previous_label,
                    "to": event.new_label,
                    "by": event.applied_by,
                    "justification": event.justification,
                    "timestamp": event.timestamp,
                })

        return {
            "report_date": date.today().isoformat(),
            "total_events": len(self.events),
            "by_action": action_counts,
            "by_label": label_counts,
            "downgrades_requiring_review": downgrades,
        }


def run_vanguard_example():
    """Demonstrate labelling system for Vanguard Financial Services."""
    engine = LabellingEngine()

    print("=" * 70)
    print("VANGUARD FINANCIAL SERVICES — DATA LABELLING SYSTEM")
    print("=" * 70)

    print("\nConfigured Labels:")
    for label in engine.labels.values():
        auto = f" [AUTO: {', '.join(label.auto_apply_conditions)}]" if label.auto_apply_conditions else ""
        print(f"  {label.name} ({label.tier.value}){auto}")

    events = []
    events.append(engine.apply_label("DOC-001", "customer_report.xlsx", "LBL-CONF-CUST",
                                     "Sarah Mitchell", "user"))
    events.append(engine.apply_label("DOC-002", "health_assessment.pdf", "LBL-REST-SC",
                                     "system", "auto"))
    events.append(engine.apply_label("DOC-003", "dbs_result_thompson.pdf", "LBL-REST-CRIM",
                                     "system", "auto"))
    events.append(engine.apply_label("DOC-004", "internal_memo.docx", "LBL-INT",
                                     "John Smith", "user"))

    inheritance = engine.apply_inheritance("LBL-CONF-CUST", "DOC-005", "new_file_in_customer_folder.xlsx")
    if inheritance:
        events.append(inheritance)

    events.append(engine.apply_label("DOC-004", "internal_memo.docx", "LBL-PUB",
                                     "John Smith", "user",
                                     current_label_id="LBL-INT",
                                     justification="Content approved for public release by Communications team"))

    print("\nLabel Events:")
    for e in events:
        print(f"  [{e.action.value:20s}] {e.document_name}: {e.previous_label} → {e.new_label} (by: {e.applied_by})")

    report = engine.generate_audit_report()
    print(f"\n{'='*70}")
    print("AUDIT REPORT")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    run_vanguard_example()
