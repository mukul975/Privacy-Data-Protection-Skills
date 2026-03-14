#!/usr/bin/env python3
"""
Data Subject Breach Communication Manager

Generates Art. 34 data subject notifications based on breach type,
manages communication tracking, and validates notification content
against GDPR Art. 34(2) requirements.
"""

import json
import sys
from datetime import datetime, timezone
from enum import Enum
from typing import Optional


class BreachScenario(Enum):
    FINANCIAL_DATA = "financial_data"
    HEALTH_DATA = "health_data"
    CREDENTIAL_COMPROMISE = "credential_compromise"
    RANSOMWARE = "ransomware"
    INSIDER_THREAT = "insider_threat"


class CommunicationChannel(Enum):
    EMAIL = "email"
    POSTAL = "postal_mail"
    SMS = "sms"
    IN_APP = "in_app_notification"
    PUBLIC = "public_communication"


class ExemptionCheck:
    """Evaluate Art. 34(3) exemptions from data subject notification."""

    @staticmethod
    def check_encryption_exemption(
        encryption_applied: bool,
        encryption_standard: str,
        key_compromised: bool,
        all_data_encrypted: bool,
    ) -> dict:
        """Check Art. 34(3)(a) encryption exemption."""
        exempt = (
            encryption_applied
            and encryption_standard in ("AES-256", "AES-128", "ChaCha20-Poly1305")
            and not key_compromised
            and all_data_encrypted
        )

        reasons = []
        if not encryption_applied:
            reasons.append("Encryption was not applied to the affected data")
        if encryption_standard not in ("AES-256", "AES-128", "ChaCha20-Poly1305"):
            reasons.append(f"Encryption standard '{encryption_standard}' may not meet state-of-the-art requirement")
        if key_compromised:
            reasons.append("Encryption keys were compromised in the same breach — encryption provides no protection")
        if not all_data_encrypted:
            reasons.append("Not all affected data was encrypted — exemption requires protection of ALL affected data")

        return {
            "exemption": "Art. 34(3)(a) — Technical protection measures",
            "applicable": exempt,
            "assessment": "EXEMPT — Data rendered unintelligible" if exempt else "NOT EXEMPT",
            "reasons": reasons if not exempt else ["All conditions met: state-of-the-art encryption applied to all data, keys not compromised"],
        }

    @staticmethod
    def check_subsequent_measures_exemption(
        risk_eliminated: bool,
        data_accessed: bool,
        exposure_window_hours: float,
    ) -> dict:
        """Check Art. 34(3)(b) subsequent measures exemption."""
        exempt = risk_eliminated and not data_accessed and exposure_window_hours < 1.0

        reasons = []
        if not risk_eliminated:
            reasons.append("Controller cannot demonstrate that high risk is no longer likely to materialise")
        if data_accessed:
            reasons.append("Evidence indicates unauthorized access to the data occurred")
        if exposure_window_hours >= 1.0:
            reasons.append(f"Exposure window of {exposure_window_hours:.1f} hours exceeds the brief window required for this exemption")

        return {
            "exemption": "Art. 34(3)(b) — Subsequent measures eliminating risk",
            "applicable": exempt,
            "assessment": "EXEMPT — High risk no longer likely" if exempt else "NOT EXEMPT",
            "reasons": reasons if not exempt else ["Risk demonstrably eliminated, no access, brief exposure"],
        }

    @staticmethod
    def check_disproportionate_effort_exemption(
        total_affected: int,
        valid_contact_percentage: float,
    ) -> dict:
        """Check Art. 34(3)(c) disproportionate effort exemption."""
        exempt = valid_contact_percentage < 30.0 and total_affected > 10000

        reasons = []
        if valid_contact_percentage >= 30.0:
            reasons.append(f"Valid contact information available for {valid_contact_percentage:.0f}% of affected individuals — individual notification is feasible")
        if total_affected <= 10000:
            reasons.append(f"Only {total_affected} individuals affected — individual notification is proportionate")

        alternative_required = exempt
        return {
            "exemption": "Art. 34(3)(c) — Disproportionate effort",
            "applicable": exempt,
            "assessment": "EXEMPT — but public communication required" if exempt else "NOT EXEMPT",
            "reasons": reasons if not exempt else [f"Only {valid_contact_percentage:.0f}% valid contacts for {total_affected} individuals — disproportionate effort established"],
            "public_communication_required": alternative_required,
        }


NOTIFICATION_TEMPLATES = {
    BreachScenario.FINANCIAL_DATA: {
        "subject": "Important Security Notice — Your Payment Information May Have Been Affected",
        "sender": "Stellar Payments Group",
        "recommended_channel": CommunicationChannel.EMAIL,
        "support_measures": [
            "12 months complimentary credit monitoring (Experian IdentityWorks)",
            "Dedicated breach response hotline: +49 30 7742 9000",
            "Online breach support portal: stellarpayments.eu/breach-support",
        ],
        "protective_actions": [
            "Contact your bank or card issuer and request a replacement card",
            "Review bank and card statements for unrecognized transactions",
            "Be cautious of unsolicited emails, calls, or texts claiming to be from Stellar Payments",
            "Consider placing a fraud alert with SCHUFA or your local credit agency",
            "Do not click links in emails claiming to be about this incident — go directly to stellarpayments.eu",
        ],
    },
    BreachScenario.HEALTH_DATA: {
        "subject": "Important Notice Regarding Your Health Information",
        "sender": "Stellar Payments Group — Data Protection Office",
        "recommended_channel": CommunicationChannel.POSTAL,
        "support_measures": [
            "Confidential counselling through Employee Assistance Programme: +49 800 100 0287",
            "Right to request access logs under Art. 15 GDPR",
            "DPO direct line: +49 30 7742 8001",
        ],
        "protective_actions": [
            "Contact the DPO if you have concerns about how your health information may be used",
            "Exercise your right of access (Art. 15) to obtain a copy of access logs for your records",
            "Report any adverse consequences you believe are related to this incident",
        ],
    },
    BreachScenario.CREDENTIAL_COMPROMISE: {
        "subject": "Action Required — Your Account Credentials May Be Compromised",
        "sender": "Stellar Payments Group — Security Team",
        "recommended_channel": CommunicationChannel.EMAIL,
        "support_measures": [
            "Forced password reset on all affected accounts",
            "Two-factor authentication enrollment guidance",
            "Breach support hotline: +49 30 7742 9000",
        ],
        "protective_actions": [
            "Create a new strong unique password when prompted at next login",
            "Enable two-factor authentication (Settings > Security > Enable 2FA)",
            "Change the same password on any other service where you reused it",
            "Be alert for phishing emails referencing this incident",
            "Use a password manager to generate unique passwords for every account",
        ],
    },
    BreachScenario.RANSOMWARE: {
        "subject": "Service Disruption Notice — Your Data Was Temporarily Unavailable",
        "sender": "Stellar Payments Group",
        "recommended_channel": CommunicationChannel.EMAIL,
        "support_measures": [
            "Systems restored from verified clean backups",
            "Customer support: +49 30 7742 5000",
            "Account verification portal: stellarpayments.eu/verify-account",
        ],
        "protective_actions": [
            "Log in and verify your recent transactions and account balance",
            "Report any discrepancies to customer support immediately",
            "Change your account password as a precaution",
        ],
    },
    BreachScenario.INSIDER_THREAT: {
        "subject": "Important Notice Regarding Your Personal Records",
        "sender": "Stellar Payments Group — Data Protection Office",
        "recommended_channel": CommunicationChannel.POSTAL,
        "support_measures": [
            "24 months identity theft protection (Experian IdentityWorks with EUR 25,000 insurance)",
            "Court-ordered data deletion confirmed with sworn declaration",
            "Law enforcement referral: LKA Berlin",
            "HR confidential line: +49 30 7742 7500",
        ],
        "protective_actions": [
            "Monitor bank accounts for unauthorized transactions",
            "Place a SCHUFA fraud alert (meineschufa.de or +49 611 9278 0)",
            "Be cautious of unsolicited contact referencing your employment details",
            "Report suspicious activity to security@stellarpayments.eu",
        ],
    },
}


def validate_notification_content(notification_text: str) -> dict:
    """
    Validate that a breach notification meets Art. 34(2) content requirements.

    Checks for the presence of mandatory elements referenced from Art. 33(3)(b)(c)(d).
    """
    checks = {
        "nature_of_breach": {
            "required": True,
            "description": "Description of the nature of the breach",
            "keywords": ["what happened", "security incident", "breach", "unauthorized", "compromised"],
        },
        "dpo_contact": {
            "required": True,
            "description": "DPO or contact point name and details — Art. 33(3)(b)",
            "keywords": ["data protection officer", "dpo", "contact", "email", "phone"],
        },
        "likely_consequences": {
            "required": True,
            "description": "Likely consequences of the breach — Art. 33(3)(c)",
            "keywords": ["consequences", "risk", "impact", "may", "could"],
        },
        "measures_taken": {
            "required": True,
            "description": "Measures taken or proposed — Art. 33(3)(d)",
            "keywords": ["we have", "we are", "measures", "steps", "action"],
        },
        "protective_actions": {
            "required": False,
            "description": "Steps data subjects can take (best practice, not strictly required)",
            "keywords": ["you can", "you should", "we recommend", "action required"],
        },
        "clear_language": {
            "required": True,
            "description": "Clear and plain language per Art. 34(2)",
            "keywords": [],
        },
    }

    text_lower = notification_text.lower()
    results = {}

    for check_name, check_def in checks.items():
        if check_name == "clear_language":
            technical_terms = ["sql injection", "tcp/ip", "siem", "cryptographic hash", "zero-day"]
            found_jargon = [t for t in technical_terms if t in text_lower]
            passed = len(found_jargon) == 0
            results[check_name] = {
                "passed": passed,
                "required": check_def["required"],
                "description": check_def["description"],
                "note": f"Technical jargon found: {', '.join(found_jargon)}" if found_jargon else "No technical jargon detected",
            }
        else:
            found = any(kw in text_lower for kw in check_def["keywords"])
            results[check_name] = {
                "passed": found,
                "required": check_def["required"],
                "description": check_def["description"],
            }

    all_required_passed = all(
        r["passed"] for r in results.values() if r["required"]
    )

    return {
        "compliant": all_required_passed,
        "checks": results,
        "summary": "Notification meets Art. 34(2) content requirements" if all_required_passed
        else "Notification is MISSING required Art. 34(2) content elements",
    }


def generate_communication_plan(
    scenario: str,
    affected_count: int,
    valid_email_percentage: float,
    languages_required: list,
    breach_reference: str,
) -> dict:
    """
    Generate a data subject communication plan with timeline and channels.
    """
    scenario_enum = BreachScenario(scenario)
    template = NOTIFICATION_TEMPLATES[scenario_enum]

    channels = []

    email_count = int(affected_count * (valid_email_percentage / 100))
    postal_count = affected_count - email_count

    if valid_email_percentage > 0:
        channels.append({
            "channel": CommunicationChannel.EMAIL.value,
            "recipients": email_count,
            "send_rate": "10,000 per hour",
            "estimated_completion_hours": max(1, email_count / 10000),
            "priority": 1,
        })

    if postal_count > 0:
        channels.append({
            "channel": CommunicationChannel.POSTAL.value,
            "recipients": postal_count,
            "estimated_delivery_days": "3-5 domestic, 7-14 international",
            "priority": 2,
        })

    channels.append({
        "channel": CommunicationChannel.IN_APP.value,
        "recipients": email_count,
        "priority": 3,
        "note": "Supplementary — triggers on next login",
    })

    if affected_count > 5000:
        channels.append({
            "channel": CommunicationChannel.SMS.value,
            "recipients": int(affected_count * 0.7),
            "priority": 3,
            "note": "Supplementary SMS alerting to check email/post",
        })

    batches_needed = max(1, email_count // 10000)
    send_hours = max(1, email_count / 10000)

    return {
        "breach_reference": breach_reference,
        "scenario": scenario,
        "template_subject": template["subject"],
        "sender": template["sender"],
        "total_affected": affected_count,
        "languages": languages_required,
        "channels": channels,
        "support_infrastructure": {
            "hotline": "+49 30 7742 9000",
            "hotline_hours": "Monday-Friday 08:00-20:00 CET, Saturday 09:00-17:00 CET",
            "operators_required": max(4, affected_count // 2000),
            "web_portal": "stellarpayments.eu/breach-support",
            "email_inbox": "breach-support@stellarpayments.eu",
        },
        "support_measures": template["support_measures"],
        "protective_actions": template["protective_actions"],
        "timeline": {
            "day_1_2": "Finalize notification text, legal review, translation, set up support infrastructure",
            "day_3": "Internal testing — send to test group, verify rendering across email clients",
            "day_4_5": "Begin email distribution in batches, dispatch postal notifications, activate in-app alerts",
            "day_6_7": "Complete email distribution, send SMS alerts, activate public communication if applicable",
            "week_2_4": "Monitor hotline, process responses, track credit monitoring enrollment",
            "week_4_8": "Follow-up communication to non-enrolled credit monitoring recipients, close hotline",
        },
        "email_distribution": {
            "total_emails": email_count,
            "batches": batches_needed,
            "hours_to_complete": round(send_hours, 1),
            "bounce_handling": "Bounced addresses flagged for postal fallback within 48 hours",
        },
    }


def main():
    print("=" * 70)
    print("ART. 34(3) EXEMPTION ANALYSIS")
    print("=" * 70)

    print("\n--- Encryption Exemption Check ---")
    enc_check = ExemptionCheck.check_encryption_exemption(
        encryption_applied=True,
        encryption_standard="AES-256",
        key_compromised=True,
        all_data_encrypted=True,
    )
    print(json.dumps(enc_check, indent=2))

    print("\n--- Subsequent Measures Exemption Check ---")
    sub_check = ExemptionCheck.check_subsequent_measures_exemption(
        risk_eliminated=False,
        data_accessed=True,
        exposure_window_hours=48.0,
    )
    print(json.dumps(sub_check, indent=2))

    print("\n--- Disproportionate Effort Exemption Check ---")
    effort_check = ExemptionCheck.check_disproportionate_effort_exemption(
        total_affected=15230,
        valid_contact_percentage=92.0,
    )
    print(json.dumps(effort_check, indent=2))

    print("\n" + "=" * 70)
    print("COMMUNICATION PLAN — Financial Data Breach")
    print("=" * 70)

    plan = generate_communication_plan(
        scenario="financial_data",
        affected_count=15230,
        valid_email_percentage=92.0,
        languages_required=["de", "en", "fr", "nl"],
        breach_reference="SPG-BREACH-2026-003",
    )
    print(json.dumps(plan, indent=2))

    print("\n" + "=" * 70)
    print("NOTIFICATION CONTENT VALIDATION")
    print("=" * 70)

    sample_notification = """
    Dear Customer,

    We are writing to inform you of a security incident that may have affected
    your personal and payment information held by Stellar Payments Group.

    What happened: On 13 March 2026, we detected unauthorized access to our
    payment processing database. An external attacker gained access to customer
    payment records between 10 March and 13 March 2026.

    What we have done: We immediately isolated the affected system and engaged
    Mandiant to conduct a full forensic investigation. We have notified the
    supervisory authority.

    The consequences of this breach may include risk of financial fraud and
    targeted phishing using your personal information.

    You can protect yourself by contacting your bank and reviewing your statements.

    Our Data Protection Officer, Dr. Elena Vasquez, can be reached at
    dpo@stellarpayments.eu or +49 30 7742 8001.
    """

    validation = validate_notification_content(sample_notification)
    print(json.dumps(validation, indent=2))


if __name__ == "__main__":
    main()
