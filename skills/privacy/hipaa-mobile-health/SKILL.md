---
name: hipaa-mobile-health
description: >-
  Addresses HIPAA compliance for mobile health (mHealth) applications,
  wearable devices, and remote patient monitoring. Covers OCR guidance on
  mobile device PHI, FDA-regulated mobile medical applications, FTC Health
  Breach Notification Rule for non-HIPAA apps, BYOD policies, and
  encryption requirements for ePHI on mobile platforms. Keywords: mHealth,
  mobile health, HIPAA mobile, wearable, remote monitoring, BYOD, mobile
  device management, app privacy.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: healthcare-privacy
  tags: "hipaa, mobile-health, mhealth, wearable, remote-monitoring, byod, mobile-device, app-privacy"
---

# HIPAA Mobile Health — mHealth Privacy and Security

## Overview

Mobile health (mHealth) encompasses the use of mobile devices, applications, wearable sensors, and remote patient monitoring systems to deliver healthcare services and manage health information. OCR has issued specific guidance on HIPAA compliance for mobile devices, recognizing that the proliferation of smartphones, tablets, and wearable health technology creates significant risks to the confidentiality, integrity, and availability of ePHI. The regulatory landscape intersects HIPAA (for covered entities and business associates), FDA regulation (for mobile medical devices/software as a medical device), and FTC jurisdiction (for consumer health apps not covered by HIPAA).

## Regulatory Framework

### HIPAA Security Rule — Mobile-Relevant Provisions

- **§164.310(b)**: Workstation use — policies specifying the proper functions to be performed and the physical attributes of surroundings for workstations accessing ePHI (includes mobile devices)
- **§164.310(c)**: Workstation security — physical safeguards for workstations accessing ePHI to restrict access to authorized users
- **§164.310(d)**: Device and media controls — policies for receipt, removal, disposal, and re-use of hardware and electronic media containing ePHI
- **§164.312(a)(1)**: Access control — unique user identification, emergency access procedure, automatic logoff, encryption and decryption
- **§164.312(a)(2)(iv)**: Encryption and decryption (addressable) — encrypt ePHI stored on mobile devices
- **§164.312(d)**: Person or entity authentication — verify identity of persons seeking access via mobile
- **§164.312(e)(1)**: Transmission security — protect ePHI transmitted over wireless and cellular networks

### OCR Mobile Device Guidance

OCR guidance emphasizes that the Security Rule applies to ePHI on all electronic media, including mobile devices. Key OCR positions:

1. Mobile devices used to access, receive, transmit, or store ePHI must comply with Security Rule safeguards
2. Lost or stolen unencrypted mobile devices containing ePHI constitute presumed breaches under the Breach Notification Rule
3. The use of personal mobile devices (BYOD) does not exempt the entity from HIPAA compliance

### FTC Health Breach Notification Rule (16 CFR Part 318)

For health apps and connected devices NOT covered by HIPAA:

- Applies to vendors of personal health records and related entities
- Expanded by FTC in 2023 to cover health apps, fitness trackers, and consumer wearables
- Requires breach notification to consumers, FTC, and (for 500+ individuals) media
- Violations subject to FTC enforcement (up to $50,120 per violation per day as of 2024)

### FDA Mobile Medical Applications

- FDA exercises enforcement discretion for most general wellness and health management apps
- Software as a Medical Device (SaMD): FDA regulates apps that perform clinical decision support, diagnostic functions, or meet the definition of a medical device
- FDA does NOT enforce HIPAA but PHI handling in FDA-regulated devices must still comply with HIPAA

## Mobile Device Security Requirements

| Requirement | Regulation | Implementation |
|------------|-----------|----------------|
| Device encryption | §164.312(a)(2)(iv) | Full-disk encryption (AES-256) on all mobile devices accessing ePHI |
| Screen lock / auto-logoff | §164.312(a)(2)(iii) | Maximum 2-minute inactivity timeout; biometric or 6-digit PIN |
| Remote wipe capability | §164.310(d)(2)(iii) | MDM-enabled remote wipe for lost/stolen devices |
| Transmission encryption | §164.312(e)(1) | TLS 1.2+ for all data in transit; VPN for network access |
| App-level authentication | §164.312(d) | Per-app authentication for mHealth applications accessing ePHI |
| Malware protection | §164.308(a)(5)(ii)(B) | Mobile threat defense software; app vetting for sideloading |
| Audit logging | §164.312(b) | MDM audit trails for device access, app usage, data transfers |
| Data backup | §164.308(a)(7) | Automated backup of ePHI on mobile; exclude from consumer cloud backup |

## BYOD Policy Requirements

For organizations permitting personal device use:

1. **Acceptable use policy**: Define permitted PHI activities on personal devices
2. **MDM enrollment**: Require mobile device management enrollment with containerization
3. **Separation of personal and work data**: Use app-level containers or work profiles
4. **Minimum device standards**: OS version requirements, jailbreak/root detection, encryption verification
5. **Offboarding**: Remote wipe of organizational data upon termination; leave personal data intact
6. **Risk acceptance**: Document that BYOD risk has been evaluated per §164.308(a)(1) risk analysis

## Wearable and Remote Patient Monitoring

| Device Category | HIPAA Applicability | Key Privacy Considerations |
|----------------|--------------------|-----------------------------|
| Prescribed RPM devices (e.g., cardiac monitors) | Yes — CE or BA processes PHI | Encryption at rest and in transit; BAA with device vendor; patient consent for continuous monitoring |
| Provider-issued wearables (e.g., glucose monitors) | Yes — CE or BA processes PHI | Data minimization; defined retention; secure transmission to EHR |
| Consumer wearables (e.g., Fitbit, Apple Watch) | Only if data flows to CE/BA | FTC Health Breach Notification Rule applies if non-HIPAA; HIPAA applies once data enters CE/BA systems |
| Clinical trial wearables | Yes — research use of PHI | IRB oversight; authorization or waiver; de-identification at earliest opportunity |

## Enforcement Examples

- **Lifespan Health System (2020)**: $1.04 million — unencrypted stolen laptop; OCR found systemic failure to encrypt ePHI on mobile devices despite multiple prior incidents
- **Children's Medical Center of Dallas (2017)**: $3.2 million — unencrypted BlackBerry lost in 2009 and unencrypted laptop stolen in 2013; OCR cited failure to implement encryption after risk analysis identified the risk
- **CardioNet (2017)**: $2.5 million — stolen unencrypted laptop containing ePHI; OCR found insufficient risk analysis and device/media controls for mobile devices

## Integration Points

- **hipaa-security-rule**: Mobile device requirements are a subset of Security Rule technical and physical safeguards
- **hipaa-risk-analysis**: Mobile devices must be included in enterprise risk analysis scope
- **hipaa-breach-notification**: Lost/stolen unencrypted mobile devices trigger breach assessment
- **hipaa-employee-training**: Workforce training must cover mobile device PHI handling
- **hipaa-baa-management**: BAAs required with MDM vendors, mHealth app vendors, and RPM device manufacturers that access PHI
