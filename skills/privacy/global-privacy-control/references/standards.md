# Regulatory Standards — Implementing Global Privacy Control

## Primary Regulations

### California Privacy Rights Act (CPRA) — California Civil Code Section 1798.100 et seq.

- **Section 1798.135(e)**: "A business that collects consumers' personal information shall allow consumers, or a person authorized by the consumer, to opt out of the sale or sharing of their personal information... A business shall treat the use of an opt-out preference signal by the consumer as a valid request submitted pursuant to Section 1798.120 for that browser or device, and, if known, for the consumer."
- **Section 1798.120**: Establishes the consumer's right to opt out of the sale or sharing of personal information.
- **Section 1798.185(a)(19)**: Directs the California Privacy Protection Agency (CPPA) to establish technical specifications for opt-out preference signals.
- **AG Regulation 11 CCR 7025(a)**: A business must treat an opt-out preference signal as a valid request to opt out of sale/sharing.
- **AG Regulation 11 CCR 7025(b)**: The opt-out applies to the browser or device and any consumer profile associated with that browser or device.
- **AG Regulation 11 CCR 7025(c)**: Conflict resolution when opt-out preference signal conflicts with consumer's financial incentive program participation.

### Colorado Privacy Act (CPA) — C.R.S. Section 6-1-1301 et seq.

- **Section 6-1-1306(1)(a)(IV)(A)**: Controllers must recognize universal opt-out mechanisms, effective July 1, 2024.
- **CPA Rules 4.6**: Details on technical requirements for universal opt-out mechanism recognition.

### Connecticut Data Privacy Act (CTDPA) — Public Act No. 22-15

- **Section 42-520(b)(5)**: Controllers must recognize universal opt-out mechanisms for sale and targeted advertising, effective January 1, 2025.

### Montana Consumer Data Privacy Act (MCDPA) — MCA Section 30-14-2801 et seq.

- **Section 30-14-2807**: Controllers must recognize opt-out preference signals for sale of personal data and targeted advertising, effective October 1, 2024.

### Texas Data Privacy and Security Act (TDPSA) — Texas Business and Commerce Code Chapter 541

- **Section 541.055**: Universal opt-out mechanism recognition required beginning January 1, 2025.

### Oregon Consumer Privacy Act (OCPA) — ORS Section 646A.570 et seq.

- **Section 646A.578**: Controllers shall recognize opt-out preference signals, effective July 1, 2024.

## Technical Standards

### Global Privacy Control Specification

Published at globalprivacycontrol.org, the GPC specification defines:
- **Sec-GPC HTTP Header**: A request header with value "1" indicating opt-out preference.
- **navigator.globalPrivacyControl JavaScript API**: A DOM property returning `true` when GPC is enabled.
- **Scope**: GPC communicates a general request to opt out of selling or sharing personal information. The legal effect depends on applicable jurisdiction.

## Enforcement Actions

### California AG v. Sephora (August 24, 2022)

First public enforcement action involving GPC signals. Sephora agreed to:
- Pay $1.2 million in penalties
- Implement GPC signal detection and honoring
- Provide clear opt-out mechanisms
- Conform data processing agreements with service providers

Key finding: Sephora failed to detect and honor GPC signals as valid opt-out requests under CCPA (predecessor to CPRA), constituting a violation of Section 1798.135.

### CPPA Enforcement Advisory (February 2024)

The California Privacy Protection Agency issued enforcement advisories confirming that failure to honor GPC signals constitutes a violation of the CPRA, and that businesses should implement detection of both the HTTP header and JavaScript API.
