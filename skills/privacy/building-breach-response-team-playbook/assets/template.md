# Breach Response Team Playbook — Quick Reference Card

## IMMEDIATE ACTIONS UPON BREACH DETECTION

### Step 1: CONFIRM
- Is personal data involved? If NO → standard security incident process.
- If YES → proceed to Step 2.

### Step 2: CLASSIFY
| If... | Then severity is... |
|-------|-------------------|
| 10,000+ subjects OR Art. 9 data OR ongoing exfiltration OR ransomware | SEV-1 (Critical) |
| 1,000-10,000 subjects OR financial data OR media coverage | SEV-2 (High) |
| 100-1,000 subjects OR non-sensitive data OR contained | SEV-3 (Medium) |
| Under 100 subjects OR low sensitivity OR no exfiltration | SEV-4 (Low) |

### Step 3: ACTIVATE
| SEV-1 | Call within 15 min: IC (+49 30 7742 8100), DPO (+49 30 7742 8001), CEO (+49 30 7742 8000), Legal (+49 30 7742 8200) |
| SEV-2 | Call within 30 min: IC, DPO, Legal, IT Forensics (+49 30 7742 8300) |
| SEV-3 | Notify within 2 hr: IC, DPO |
| SEV-4 | Notify within 4 hr: DPO |

### Step 4: PRESERVE
- Do NOT shut down or restart affected systems
- Capture RAM dump before any remediation
- Initiate forensic disk image
- Preserve all log files

### Step 5: CONTAIN
- Isolate compromised systems from network
- Revoke compromised credentials
- Block attacker IP addresses at perimeter
- Activate backup restoration if needed

### Step 6: ASSESS
- Art. 33 72-hour clock starts when controller has "reasonable certainty"
- Complete risk assessment using the 6-factor methodology
- Score 6-8: document only | Score 9-18: notify SA | Score 19-24: notify SA + data subjects

### Step 7: NOTIFY
- SA notification deadline: [Discovery timestamp + 72 hours]
- Lead SA: Berliner BfDI — datenschutz-berlin.de — +49 30 13889 0
- DPO prepares Art. 33(3) notification form

## EMERGENCY CONTACTS

| Role | Name | Phone |
|------|------|-------|
| Incident Commander | Thomas Brenner | +49 30 7742 8100 |
| DPO | Dr. Elena Vasquez | +49 30 7742 8001 |
| General Counsel | Sarah Chen | +49 30 7742 8200 |
| CEO | Marcus Lindqvist | +49 30 7742 8000 |
| Mandiant IR | Hotline | +1 703 935 1700 |
| Freshfields Legal | Dr. Klaus Fischer | +49 30 2028 39000 |
| Experian (credit monitoring) | Enterprise Team | +44 115 941 0888 |
| Allianz (cyber insurance) | Claims | +49 89 3800 0 |

**Playbook Version**: 3.1 | **Last Updated**: 1 March 2026 | **Next Review**: 1 September 2026
