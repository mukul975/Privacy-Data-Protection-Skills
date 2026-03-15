# BYOD Privacy Policy Workflows

## Workflow 1: BYOD Programme Privacy Assessment

```
START: Proposal to implement or review BYOD programme
│
├─ Step 1: Voluntariness check
│  ├─ Is BYOD genuinely voluntary? [Must be Yes]
│  ├─ Is a corporate-provided device available as an alternative? [Must be Yes]
│  └─ Is there ANY consequence for declining BYOD? [Must be No]
│
├─ Step 2: Data separation architecture
│  ├─ Is containerisation / work profile implemented? [Must be Yes]
│  ├─ Can employer access personal data outside the container? [Must be No]
│  ├─ Is corporate data encrypted within the container? [Must be Yes]
│  └─ Can corporate and personal data be independently managed? [Must be Yes]
│
├─ Step 3: MDM capabilities review
│  ├─ Permitted capabilities:
│  │  [ ] Enforce device passcode
│  │  [ ] Encrypt corporate container
│  │  [ ] Selective wipe (corporate data only)
│  │  [ ] Push corporate apps to container
│  │  [ ] Enforce minimum OS version
│  │  [ ] VPN configuration
│  ├─ Prohibited capabilities — MUST be disabled:
│  │  [ ] Full device remote wipe
│  │  [ ] Personal app inventory
│  │  [ ] Personal browsing history
│  │  [ ] Personal location tracking
│  │  [ ] Personal email access
│  │  [ ] Personal photo/media access
│  │  [ ] Microphone/camera activation
│  │  [ ] Personal call log access
│  │  [ ] Keylogging
│  └─ Any prohibited capability enabled → FAIL → Reconfigure before proceeding
│
├─ Step 4: Privacy notice and agreement
│  ├─ Privacy notice covers what is and is not collected? [Must be Yes]
│  ├─ BYOD agreement separate from employment contract? [Must be Yes]
│  ├─ Remote wipe scope clearly stated (corporate only)? [Must be Yes]
│  └─ Withdrawal/un-enrolment procedure documented? [Must be Yes]
│
├─ Step 5: DPIA
│  ├─ Has a DPIA been conducted for the BYOD programme? [Must be Yes if monitoring]
│  └─ DPIA approved by DPO? [Must be Yes]
│
└─ END: BYOD programme may proceed. Schedule annual review.
```

## Workflow 2: BYOD Selective Wipe Procedure

```
START: Trigger event for selective wipe
│
├─ Trigger identification:
│  [ ] Employee leaves organisation
│  [ ] Employee reports device lost/stolen
│  [ ] Employee un-enrols from BYOD
│  [ ] Device found non-compliant (jailbroken, below OS minimum)
│
├─ Step 1: Authorisation
│  ├─ IT helpdesk receives trigger
│  ├─ Verify employee identity / trigger legitimacy
│  └─ Authorise selective wipe (NOT full device wipe)
│
├─ Step 2: Execute selective wipe
│  ├─ Remove corporate container and managed apps
│  ├─ Revoke corporate access credentials
│  ├─ Verify personal data is NOT affected
│  └─ Timeline: within 4 hours for lost/stolen; within 24 hours for termination
│
├─ Step 3: Documentation
│  ├─ Record wipe in incident register
│  ├─ Confirm selective (not full) wipe completed
│  └─ Notify employee of actions taken
│
├─ Step 4: Follow-up
│  ├─ If device lost/stolen and selective wipe unconfirmed (device offline):
│  │  ├─ Revoke all corporate credentials immediately
│  │  ├─ Queue selective wipe for when device reconnects
│  │  └─ Offer temporary corporate device
│  └─ Personal data recovery is employee's responsibility
│
└─ END: Corporate data secured. Personal data preserved.
```

## Workflow 3: BYOD Enrolment Process

```
START: Employee requests BYOD enrolment
│
├─ Step 1: Provide BYOD privacy notice and agreement
│  ├─ Employee reads privacy notice detailing:
│  │  - What data is collected from the device
│  │  - What data is NOT collected
│  │  - Remote wipe scope (corporate only)
│  │  - How to un-enrol
│  ├─ Employee signs BYOD agreement
│  └─ Confirm employee understands BYOD is voluntary
│
├─ Step 2: Technical enrolment
│  ├─ Install containerisation / work profile
│  ├─ Configure corporate apps within container
│  ├─ Enforce device passcode requirement
│  ├─ Verify prohibited MDM capabilities are disabled
│  └─ Test: confirm personal data not visible to MDM console
│
├─ Step 3: Activation
│  ├─ Corporate email, messaging, file access active within container
│  ├─ Employee confirms everything working
│  └─ IT helpdesk records enrolment
│
└─ END: BYOD active. Employee uses corporate apps within container.
```
