---
name: managing-joint-controller-arrangements
description: >-
  Guides the establishment and management of joint controller arrangements under
  GDPR Article 26, including determination of joint controllership, allocation of
  responsibilities, and transparency obligations. Activate when two or more
  controllers jointly determine purposes and means of processing, or when
  evaluating shared data platforms. Keywords: joint controller, Article 26,
  shared responsibility, arrangement, joint determination.
license: Apache-2.0
metadata:
  author: mukul975
  version: "1.0"
  domain: privacy
  subdomain: gdpr-compliance
  tags: "gdpr, joint-controller, article-26, shared-processing, arrangement, responsibility"
---

# Managing Joint Controller Arrangements

## Overview

Article 26 applies when two or more controllers jointly determine the purposes and means of processing. Joint controllers must enter into an arrangement that transparently determines their respective responsibilities for compliance, particularly regarding data subject rights and transparency obligations. The essence of the arrangement must be made available to data subjects.

## Determining Joint Controllership

Joint controllership exists when two or more entities:
1. **Jointly determine the purposes** — both entities influence why data is processed.
2. **Jointly determine the means** — both entities influence how data is processed (essential means, not just technical implementation details).

### Key Indicators

| Indicator | Points to Joint Controllership | Points Away |
|-----------|-------------------------------|-------------|
| Shared decision on purpose | Both parties decide why data is processed | One party decides purpose; other merely executes |
| Shared platform | Both parties upload/access data on a common platform | One party hosts; other merely provides input |
| Shared dataset | Both parties contribute to and benefit from a combined dataset | One party processes only for the other's purpose |
| Mutual benefit | Both parties derive independent benefit from the processing | Only one party benefits; other is purely a service provider |
| Influence on means | Both parties have a say in essential aspects (what data, how long, who accesses) | One party determines all essential means; other party only implements |

### CJEU Case Law Guidance

- **Wirtschaftsakademie Schleswig-Holstein (C-210/16)**: A Facebook fan page admin is a joint controller with Facebook because the admin's creation of the page enables Facebook's processing and the admin benefits from visitor statistics.
- **Jehovah's Witnesses (C-25/17)**: A religious community that organises door-to-door preaching and coordinates personal data collection by its members is a joint controller with those members.
- **Fashion ID (C-40/17)**: A website embedding a Facebook Like button is a joint controller with Facebook for the collection and transmission of data triggered by the plugin.

## Art. 26 Arrangement Requirements

The arrangement between joint controllers must determine in a transparent manner:

### 1. Respective Responsibilities

| Responsibility Area | Allocation Options |
|---------------------|-------------------|
| Lawful basis determination | Which controller is responsible for establishing and documenting the lawful basis |
| Privacy notices (Art. 13-14) | Which controller provides transparency information to data subjects |
| Data subject rights (Art. 15-22) | Which controller serves as the contact point and handles requests |
| Data security (Art. 32) | Which controller implements and maintains security measures |
| Breach notification (Art. 33-34) | Which controller notifies the supervisory authority and data subjects |
| DPIA (Art. 35) | Which controller conducts the DPIA |
| Records of processing (Art. 30) | How both controllers maintain their respective RoPA entries |

### 2. Contact Point for Data Subjects

The arrangement must designate a contact point for data subjects. Regardless of the arrangement, data subjects may exercise their rights against any of the joint controllers (Art. 26(3)).

### 3. Transparency

The essence of the arrangement must be made available to data subjects. This does not require publishing the full commercial agreement, but must cover:
- The identity of both joint controllers
- How responsibilities are divided
- How data subjects can exercise their rights
- The designated contact point

## Arrangement Template Structure

A compliant Art. 26 arrangement should include:

1. **Parties and definitions**: Legal entity names, registered addresses, roles.
2. **Scope of joint processing**: Specific processing activities covered, personal data categories, data subject categories.
3. **Purpose determination**: How purposes are jointly determined and what each party's interest is.
4. **Means determination**: Which essential means each party determines (data elements, retention, access, security standards).
5. **Responsibilities allocation**: Detailed allocation per the table above.
6. **Data subject rights**: Designated contact point, handling procedures, cooperation obligations.
7. **Transparency**: How the essence of the arrangement is communicated to data subjects.
8. **Security obligations**: Minimum security standards each party commits to.
9. **Breach management**: Notification obligations between the parties and to authorities/data subjects.
10. **Liability**: Internal allocation of liability (note: external liability to data subjects is joint and several per Art. 82(4)-(5)).
11. **Term and termination**: Duration, exit provisions, and data handling upon termination.

## Practical Considerations

### Joint and Several Liability

Under Art. 82(4), each joint controller is liable for the entire damage caused by processing that infringes the GDPR. A joint controller may be exempted from liability under Art. 82(3) only if it proves it is not responsible for the event giving rise to the damage. Internal liability allocation in the arrangement does not affect the data subject's right to claim against either controller.

### Supervisory Authority Actions

Under Art. 26(3), data subjects can exercise their rights against each and any of the joint controllers regardless of the arrangement. The supervisory authority may also investigate any joint controller for the full scope of joint processing.

### Relationship with Art. 28

Joint controllership and the controller-processor relationship are mutually exclusive for a given processing activity. If Entity A determines purposes and means and Entity B merely processes on A's instructions, the relationship is controller-processor (Art. 28). If both determine purposes and means, the relationship is joint controllership (Art. 26).
