#!/usr/bin/env python3
"""HIPAA Security Rule technical safeguards assessment and audit log analysis processor."""

import json
import os
from datetime import datetime, timedelta
from typing import Any


# --- Security Rule Standards Registry ---

TECHNICAL_SAFEGUARDS = {
    "access_control": {
        "standard": "§164.312(a)(1)",
        "description": "Access Control",
        "specifications": {
            "unique_user_id": {
                "type": "required",
                "ref": "§164.312(a)(2)(i)",
                "description": "Unique User Identification",
            },
            "emergency_access": {
                "type": "required",
                "ref": "§164.312(a)(2)(ii)",
                "description": "Emergency Access Procedure",
            },
            "automatic_logoff": {
                "type": "addressable",
                "ref": "§164.312(a)(2)(iii)",
                "description": "Automatic Logoff",
            },
            "encryption_decryption": {
                "type": "addressable",
                "ref": "§164.312(a)(2)(iv)",
                "description": "Encryption and Decryption",
            },
        },
    },
    "audit_controls": {
        "standard": "§164.312(b)",
        "description": "Audit Controls",
        "specifications": {},
    },
    "integrity": {
        "standard": "§164.312(c)(1)",
        "description": "Integrity",
        "specifications": {
            "authenticate_ephi": {
                "type": "addressable",
                "ref": "§164.312(c)(2)",
                "description": "Mechanism to Authenticate ePHI",
            },
        },
    },
    "person_entity_auth": {
        "standard": "§164.312(d)",
        "description": "Person or Entity Authentication",
        "specifications": {},
    },
    "transmission_security": {
        "standard": "§164.312(e)(1)",
        "description": "Transmission Security",
        "specifications": {
            "integrity_controls": {
                "type": "addressable",
                "ref": "§164.312(e)(2)(i)",
                "description": "Integrity Controls",
            },
            "encryption": {
                "type": "addressable",
                "ref": "§164.312(e)(2)(ii)",
                "description": "Encryption",
            },
        },
    },
}

ADMINISTRATIVE_SAFEGUARDS = {
    "security_management": {
        "standard": "§164.308(a)(1)",
        "specifications": {
            "risk_analysis": {"type": "required", "ref": "§164.308(a)(1)(ii)(A)"},
            "risk_management": {"type": "required", "ref": "§164.308(a)(1)(ii)(B)"},
            "sanction_policy": {"type": "required", "ref": "§164.308(a)(1)(ii)(C)"},
            "activity_review": {"type": "required", "ref": "§164.308(a)(1)(ii)(D)"},
        },
    },
    "workforce_security": {
        "standard": "§164.308(a)(3)",
        "specifications": {
            "authorization_supervision": {"type": "addressable", "ref": "§164.308(a)(3)(ii)(A)"},
            "clearance_procedure": {"type": "addressable", "ref": "§164.308(a)(3)(ii)(B)"},
            "termination_procedures": {"type": "addressable", "ref": "§164.308(a)(3)(ii)(C)"},
        },
    },
    "security_awareness": {
        "standard": "§164.308(a)(5)",
        "specifications": {
            "security_reminders": {"type": "addressable", "ref": "§164.308(a)(5)(ii)(A)"},
            "malicious_software": {"type": "addressable", "ref": "§164.308(a)(5)(ii)(B)"},
            "login_monitoring": {"type": "addressable", "ref": "§164.308(a)(5)(ii)(C)"},
            "password_management": {"type": "addressable", "ref": "§164.308(a)(5)(ii)(D)"},
        },
    },
    "contingency_plan": {
        "standard": "§164.308(a)(7)",
        "specifications": {
            "data_backup": {"type": "required", "ref": "§164.308(a)(7)(ii)(A)"},
            "disaster_recovery": {"type": "required", "ref": "§164.308(a)(7)(ii)(B)"},
            "emergency_mode": {"type": "required", "ref": "§164.308(a)(7)(ii)(C)"},
            "testing_revision": {"type": "addressable", "ref": "§164.308(a)(7)(ii)(D)"},
            "criticality_analysis": {"type": "addressable", "ref": "§164.308(a)(7)(ii)(E)"},
        },
    },
}

AUDIT_ALERT_THRESHOLDS = {
    "failed_logins_lockout": {"count": 5, "window_minutes": 10},
    "bulk_record_access": {"count": 50, "window_minutes": 60},
    "after_hours_access": {"start_hour": 22, "end_hour": 6},
    "break_the_glass_review": {"review_hours": 24},
    "vip_record_access": {"immediate_alert": True},
    "privilege_escalation": {"immediate_alert": True},
}


def assess_technical_safeguards(controls: dict[str, Any]) -> dict[str, Any]:
    """Assess technical safeguards implementation status.

    Args:
        controls: Dictionary mapping control keys to implementation status and details.

    Returns:
        Assessment results with compliance status per standard and specification.
    """
    results = {
        "assessment_date": datetime.now().isoformat(),
        "standards": {},
        "summary": {
            "total_specifications": 0,
            "required_total": 0,
            "required_compliant": 0,
            "addressable_total": 0,
            "addressable_implemented": 0,
            "addressable_alternative": 0,
            "addressable_not_applicable": 0,
            "non_compliant": 0,
        },
    }

    for std_key, std_info in TECHNICAL_SAFEGUARDS.items():
        std_result = {
            "standard": std_info["standard"],
            "description": std_info["description"],
            "standard_status": controls.get(std_key, {}).get("status", "not_assessed"),
            "specifications": {},
        }

        for spec_key, spec_info in std_info["specifications"].items():
            spec_status = controls.get(std_key, {}).get(spec_key, {})
            implementation_status = spec_status.get("status", "not_assessed")
            results["summary"]["total_specifications"] += 1

            spec_result = {
                "type": spec_info["type"],
                "reference": spec_info["ref"],
                "description": spec_info["description"],
                "status": implementation_status,
            }

            if spec_info["type"] == "required":
                results["summary"]["required_total"] += 1
                if implementation_status == "implemented":
                    results["summary"]["required_compliant"] += 1
                else:
                    results["summary"]["non_compliant"] += 1
            elif spec_info["type"] == "addressable":
                results["summary"]["addressable_total"] += 1
                if implementation_status == "implemented":
                    results["summary"]["addressable_implemented"] += 1
                elif implementation_status == "alternative":
                    results["summary"]["addressable_alternative"] += 1
                    spec_result["alternative_measure"] = spec_status.get(
                        "alternative_measure", ""
                    )
                    spec_result["justification"] = spec_status.get("justification", "")
                elif implementation_status == "not_applicable":
                    results["summary"]["addressable_not_applicable"] += 1
                    spec_result["justification"] = spec_status.get("justification", "")
                else:
                    results["summary"]["non_compliant"] += 1

            std_result["specifications"][spec_key] = spec_result
        results["standards"][std_key] = std_result

    return results


def analyze_audit_logs(
    log_entries: list[dict[str, Any]],
    analysis_period_hours: int = 24,
) -> dict[str, Any]:
    """Analyze audit log entries for security incidents and compliance.

    Args:
        log_entries: List of log entry dictionaries.
        analysis_period_hours: Hours of log data to analyze.

    Returns:
        Analysis results with alerts, statistics, and compliance indicators.
    """
    now = datetime.now()
    period_start = now - timedelta(hours=analysis_period_hours)

    results = {
        "analysis_period": {
            "start": period_start.isoformat(),
            "end": now.isoformat(),
            "hours": analysis_period_hours,
        },
        "statistics": {
            "total_events": 0,
            "authentication_events": 0,
            "access_events": 0,
            "administrative_events": 0,
            "failed_logins": 0,
            "break_the_glass_events": 0,
        },
        "alerts": [],
        "compliance_indicators": {},
    }

    failed_login_tracker: dict[str, list[datetime]] = {}
    user_access_tracker: dict[str, int] = {}

    for entry in log_entries:
        entry_time_str = entry.get("timestamp", "")
        try:
            entry_time = datetime.fromisoformat(entry_time_str)
        except (ValueError, TypeError):
            continue

        if entry_time < period_start:
            continue

        results["statistics"]["total_events"] += 1
        event_type = entry.get("event_type", "")
        user_id = entry.get("user_id", "unknown")

        if event_type in ("login_success", "login_failure", "logout", "lockout"):
            results["statistics"]["authentication_events"] += 1
            if event_type == "login_failure":
                results["statistics"]["failed_logins"] += 1
                if user_id not in failed_login_tracker:
                    failed_login_tracker[user_id] = []
                failed_login_tracker[user_id].append(entry_time)

        elif event_type in ("record_access", "record_modify", "record_delete"):
            results["statistics"]["access_events"] += 1
            user_access_tracker[user_id] = user_access_tracker.get(user_id, 0) + 1

        elif event_type in ("user_created", "privilege_change", "config_change"):
            results["statistics"]["administrative_events"] += 1
            if event_type == "privilege_change":
                results["alerts"].append({
                    "type": "privilege_escalation",
                    "severity": "high",
                    "timestamp": entry_time.isoformat(),
                    "user_id": user_id,
                    "details": entry.get("details", ""),
                    "action_required": "Verify change ticket authorization",
                })

        elif event_type == "break_the_glass":
            results["statistics"]["break_the_glass_events"] += 1
            results["alerts"].append({
                "type": "break_the_glass",
                "severity": "medium",
                "timestamp": entry_time.isoformat(),
                "user_id": user_id,
                "patient_id": entry.get("patient_id", ""),
                "action_required": f"Review justification within {AUDIT_ALERT_THRESHOLDS['break_the_glass_review']['review_hours']} hours",
            })

        if entry.get("vip_record"):
            results["alerts"].append({
                "type": "vip_record_access",
                "severity": "high",
                "timestamp": entry_time.isoformat(),
                "user_id": user_id,
                "patient_id": entry.get("patient_id", ""),
                "action_required": "Privacy Office review required",
            })

        hour = entry_time.hour
        if (
            hour >= AUDIT_ALERT_THRESHOLDS["after_hours_access"]["start_hour"]
            or hour < AUDIT_ALERT_THRESHOLDS["after_hours_access"]["end_hour"]
        ):
            if event_type == "record_access" and not entry.get("expected_after_hours"):
                results["alerts"].append({
                    "type": "after_hours_access",
                    "severity": "low",
                    "timestamp": entry_time.isoformat(),
                    "user_id": user_id,
                    "action_required": "Review by SOC next business day",
                })

    threshold = AUDIT_ALERT_THRESHOLDS["failed_logins_lockout"]
    window = timedelta(minutes=threshold["window_minutes"])
    for uid, times in failed_login_tracker.items():
        times.sort()
        for i in range(len(times)):
            count_in_window = sum(
                1 for t in times[i:] if t - times[i] <= window
            )
            if count_in_window >= threshold["count"]:
                results["alerts"].append({
                    "type": "brute_force_attempt",
                    "severity": "critical",
                    "user_id": uid,
                    "failed_attempts": count_in_window,
                    "window_minutes": threshold["window_minutes"],
                    "action_required": "Account lockout and SOC investigation",
                })
                break

    bulk_threshold = AUDIT_ALERT_THRESHOLDS["bulk_record_access"]["count"]
    for uid, count in user_access_tracker.items():
        if count >= bulk_threshold:
            results["alerts"].append({
                "type": "bulk_record_access",
                "severity": "high",
                "user_id": uid,
                "records_accessed": count,
                "action_required": "SOC review — possible unauthorized data access",
            })

    results["compliance_indicators"] = {
        "audit_logging_active": results["statistics"]["total_events"] > 0,
        "authentication_events_captured": results["statistics"]["authentication_events"] > 0,
        "access_events_captured": results["statistics"]["access_events"] > 0,
        "administrative_events_captured": results["statistics"]["administrative_events"] > 0,
        "alerts_generated": len(results["alerts"]),
        "critical_alerts": sum(1 for a in results["alerts"] if a["severity"] == "critical"),
        "high_alerts": sum(1 for a in results["alerts"] if a["severity"] == "high"),
    }

    return results


def generate_encryption_status_report(
    systems: list[dict[str, Any]],
) -> dict[str, Any]:
    """Generate an encryption status report across all ePHI systems.

    Args:
        systems: List of system dictionaries with encryption information.

    Returns:
        Encryption compliance report.
    """
    report = {
        "report_date": datetime.now().isoformat(),
        "systems": [],
        "summary": {
            "total_systems": 0,
            "encrypted_at_rest": 0,
            "encrypted_in_transit": 0,
            "fully_encrypted": 0,
            "partially_encrypted": 0,
            "not_encrypted": 0,
            "exceptions_documented": 0,
        },
    }

    for system in systems:
        report["summary"]["total_systems"] += 1
        sys_result = {
            "name": system.get("name", "Unknown"),
            "type": system.get("type", ""),
            "contains_ephi": system.get("contains_ephi", True),
            "encryption_at_rest": {
                "status": system.get("encryption_at_rest", "unknown"),
                "algorithm": system.get("rest_algorithm", ""),
                "key_length": system.get("rest_key_length", ""),
            },
            "encryption_in_transit": {
                "status": system.get("encryption_in_transit", "unknown"),
                "protocol": system.get("transit_protocol", ""),
                "minimum_version": system.get("transit_min_version", ""),
            },
        }

        at_rest = system.get("encryption_at_rest") == "enabled"
        in_transit = system.get("encryption_in_transit") == "enabled"

        if at_rest:
            report["summary"]["encrypted_at_rest"] += 1
        if in_transit:
            report["summary"]["encrypted_in_transit"] += 1
        if at_rest and in_transit:
            report["summary"]["fully_encrypted"] += 1
        elif at_rest or in_transit:
            report["summary"]["partially_encrypted"] += 1
        else:
            report["summary"]["not_encrypted"] += 1
            if system.get("exception_documented"):
                report["summary"]["exceptions_documented"] += 1
                sys_result["exception"] = {
                    "documented": True,
                    "reason": system.get("exception_reason", ""),
                    "compensating_controls": system.get("compensating_controls", ""),
                }

        report["systems"].append(sys_result)

    total = report["summary"]["total_systems"]
    fully = report["summary"]["fully_encrypted"]
    report["summary"]["encryption_compliance_rate"] = (
        round(fully / total * 100, 1) if total > 0 else 0
    )

    return report


def export_report(report: dict[str, Any], output_path: str) -> str:
    """Export a report to JSON file."""
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    return output_path


if __name__ == "__main__":
    print("=== HIPAA Security Rule Technical Safeguards Assessment ===\n")

    controls = {
        "access_control": {
            "status": "implemented",
            "unique_user_id": {"status": "implemented"},
            "emergency_access": {"status": "implemented"},
            "automatic_logoff": {"status": "implemented"},
            "encryption_decryption": {"status": "implemented"},
        },
        "audit_controls": {"status": "implemented"},
        "integrity": {
            "status": "implemented",
            "authenticate_ephi": {"status": "implemented"},
        },
        "person_entity_auth": {"status": "implemented"},
        "transmission_security": {
            "status": "implemented",
            "integrity_controls": {"status": "implemented"},
            "encryption": {"status": "implemented"},
        },
    }

    assessment = assess_technical_safeguards(controls)
    print(f"Technical Safeguards Assessment:")
    print(f"  Required specifications compliant: {assessment['summary']['required_compliant']}/{assessment['summary']['required_total']}")
    print(f"  Addressable implemented: {assessment['summary']['addressable_implemented']}/{assessment['summary']['addressable_total']}")
    print(f"  Non-compliant: {assessment['summary']['non_compliant']}\n")

    sample_logs = [
        {"timestamp": datetime.now().isoformat(), "event_type": "login_success", "user_id": "jsmith4821"},
        {"timestamp": datetime.now().isoformat(), "event_type": "record_access", "user_id": "jsmith4821", "patient_id": "P-100234"},
        {"timestamp": (datetime.now() - timedelta(minutes=5)).isoformat(), "event_type": "login_failure", "user_id": "attacker1"},
        {"timestamp": (datetime.now() - timedelta(minutes=4)).isoformat(), "event_type": "login_failure", "user_id": "attacker1"},
        {"timestamp": (datetime.now() - timedelta(minutes=3)).isoformat(), "event_type": "login_failure", "user_id": "attacker1"},
        {"timestamp": (datetime.now() - timedelta(minutes=2)).isoformat(), "event_type": "login_failure", "user_id": "attacker1"},
        {"timestamp": (datetime.now() - timedelta(minutes=1)).isoformat(), "event_type": "login_failure", "user_id": "attacker1"},
        {"timestamp": datetime.now().isoformat(), "event_type": "break_the_glass", "user_id": "enurse_5521", "patient_id": "P-VIP-001"},
        {"timestamp": datetime.now().isoformat(), "event_type": "privilege_change", "user_id": "adm-jdoe", "details": "Elevated to admin role"},
    ]

    audit_results = analyze_audit_logs(sample_logs)
    print(f"Audit Log Analysis:")
    print(f"  Total events: {audit_results['statistics']['total_events']}")
    print(f"  Failed logins: {audit_results['statistics']['failed_logins']}")
    print(f"  Alerts generated: {len(audit_results['alerts'])}")
    for alert in audit_results["alerts"]:
        print(f"    [{alert['severity'].upper()}] {alert['type']}: {alert.get('action_required', '')}")
