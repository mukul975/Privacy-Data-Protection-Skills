# New Technology Privacy Impact Assessment Report

## Reference: PIA-QLH-2026-0005

| Field | Value |
|-------|-------|
| Organisation | QuantumLeap Health Technologies |
| Technology | Smart Building Environmental Monitoring System (IoT) |
| Version | 1.0 |
| Date | 2026-03-01 |
| Next Review | 2026-09-01 (6 months — accelerated for new technology) |
| DPO | Dr. Elena Vasquez, CIPP/E, CIPM |
| Technology Owner | David Mueller, Head of Facilities Management |

---

## 1. Technology Description

QuantumLeap Health Technologies is deploying an IoT-based smart building system across its London, Berlin, and Dublin offices comprising:

| Component | Quantity | Function | Data Collected |
|-----------|---------|----------|---------------|
| Environmental sensors (Siemens BT-E200) | 450 | Temperature, humidity monitoring | Temperature (celsius), relative humidity (%), timestamp, sensor location ID |
| CO2 and air quality monitors (Siemens AQM-500) | 12 | Indoor air quality measurement | CO2 (ppm), PM2.5, PM10, VOC levels, timestamp, zone ID |
| Occupancy sensors (Steinel HPD2) | 85 | Room-level occupancy detection | Occupancy count (integer), timestamp, room ID. No individual identification capability. |
| Building management gateway | 3 | Data aggregation and cloud transmission | Aggregated sensor data per building |

All sensor data is transmitted via building LAN (wired Ethernet, not wireless) to building management gateways, then via TLS 1.3 encrypted connection to Siemens Navigator platform hosted in AWS eu-central-1 (Frankfurt).

---

## 2. DPIA Screening

### WP248rev.01 Criteria Assessment

| Criterion | Met? | Justification |
|-----------|------|---------------|
| C1: Evaluation or scoring | No | System monitors environmental conditions, not individual performance or behaviour |
| C2: Automated decision-making | No | System controls HVAC and lighting; does not make decisions about individuals |
| C3: Systematic monitoring | Yes | Continuous monitoring of office spaces including occupancy detection |
| C4: Sensitive data | No | No special category data processed |
| C5: Large-scale processing | No | 450 sensors across 3 buildings; not large-scale relative to the data type |
| C6: Matching datasets | No | Sensor data not combined with employee data |
| C7: Vulnerable data subjects | No | Employees in standard office environment; no enhanced vulnerability |
| C8: Innovative technology | Yes | IoT sensor network with cloud-based analytics is innovative technology |
| C9: Preventing exercise of rights | No | System does not affect data subject rights |

**Criteria met: 2 (C3, C8)**
**Determination: DPIA required** (innovative technology + systematic monitoring)

---

## 3. Proportionality Assessment

### 3.1 Necessity

Environmental monitoring is necessary for:
- EU Energy Efficiency Directive 2023/1791 compliance (energy performance monitoring and optimisation)
- Workplace health and safety regulations (Workplace (Health, Safety and Welfare) Regulations 1992 in UK; Arbeitstattenverordnung in Germany; Safety, Health and Welfare at Work Act 2005 in Ireland)
- Indoor air quality management for employee health (WHO indoor air quality guidelines)

### 3.2 Data Minimisation

| Measure | Implementation |
|---------|---------------|
| Occupancy detection without identification | Passive infrared sensors count bodies without identifying individuals. No cameras, no badge integration, no Wi-Fi tracking. |
| Room-level aggregation | Occupancy data is aggregated to room level. Individual desk-level occupancy is not recorded. |
| No employee data linkage | Sensor data is not linked to any employee database, access control system, or HR system. |
| Short retention | Raw sensor data: 30 days. Aggregated daily summaries: 12 months (energy reporting). |

### 3.3 Less Invasive Alternatives Considered

| Alternative | Assessment | Decision |
|-------------|-----------|----------|
| Manual environmental monitoring | Insufficient granularity; cannot respond to real-time changes; high labour cost | Rejected |
| Scheduled HVAC without sensors | Energy waste from heating/cooling unoccupied spaces; does not meet energy efficiency targets | Rejected |
| Camera-based occupancy detection | More privacy-invasive than PIR sensors; captures identifiable images | Rejected |
| Wi-Fi device counting | Links to personal devices; creates individual tracking capability | Rejected |
| **PIR-based occupancy with environmental sensors (selected)** | Least invasive automated option; no individual identification; room-level only | **Selected** |

---

## 4. Risk Assessment

| Risk ID | Risk | Likelihood | Severity | Level | Mitigation | Residual Level |
|---------|------|-----------|----------|-------|------------|---------------|
| IOT-R1 | Scope creep: occupancy data used for employee monitoring or attendance tracking | Possible | Significant | High | Technical: occupancy sensors physically incapable of identification (PIR only). Organisational: policy prohibiting use of building data for employee monitoring, audited annually. | Low |
| IOT-R2 | Insecure sensor communications intercepted, revealing building occupancy patterns | Possible | Limited | Medium | Technical: wired Ethernet connections (not wireless); TLS 1.3 for gateway-to-cloud; network segmentation for IoT VLAN. | Low |
| IOT-R3 | Visitor or contractor data incidentally collected by occupancy sensors | Possible | Limited | Medium | Organisational: visitors informed via lobby signage and visitor privacy notice. Technical: occupancy count only (not identification). | Low |
| IOT-R4 | Combination of occupancy, schedule, and access data enabling individual tracking | Remote | Significant | Medium | Technical: no integration between building management system and access control/HR systems. Policy: integration prohibited without new DPIA. | Low |

---

## 5. Technical and Organisational Measures

| Measure | Type | Detail |
|---------|------|--------|
| PIR-only occupancy detection | Technical (DPbD) | Passive infrared sensors detect heat signatures for counting only; no image capture, no individual identification capability |
| Room-level aggregation | Technical (DPbD) | Occupancy data aggregated to room level in the building gateway before cloud transmission |
| Network segmentation | Technical (Security) | IoT sensors on dedicated VLAN isolated from corporate network; no direct internet access for sensors |
| Wired connections | Technical (Security) | Environmental and occupancy sensors connected via wired Ethernet; no wireless attack surface |
| TLS 1.3 encryption | Technical (Security) | All gateway-to-cloud communications encrypted with TLS 1.3 |
| 30-day raw data retention | Technical (Storage limitation) | Raw sensor data automatically deleted after 30 days; daily aggregated summaries retained 12 months |
| No-integration policy | Organisational | Building management data prohibited from integration with HR, access control, or employee monitoring systems without a new DPIA |
| Lobby privacy signage | Organisational (Transparency) | Visitors informed of occupancy monitoring via lobby signage at each entrance |
| Annual audit | Organisational | Annual audit verifying that building data has not been used for employee monitoring or integrated with employee data |

---

## 6. Conclusion

| Assessment Area | Finding |
|-----------------|---------|
| DPIA Required | Yes (innovative technology + systematic monitoring) |
| Highest Residual Risk | Low (after mitigation) |
| Prior Consultation Required | No |
| Deployment Approved | Yes — subject to conditions |

**Conditions for Deployment**:
1. Occupancy sensors must remain PIR-only (no cameras, no Wi-Fi tracking).
2. No integration with employee data systems without new DPIA.
3. Annual audit of building data usage.
4. 6-month DPIA review (September 2026).

### Approvals

| Role | Name | Date |
|------|------|------|
| DPO | Dr. Elena Vasquez | 2026-03-01 |
| Head of Facilities | David Mueller | 2026-03-01 |
| CISO | Dr. James Okonkwo | 2026-03-02 |
| COO | Dr. Priya Sharma | 2026-03-03 |
