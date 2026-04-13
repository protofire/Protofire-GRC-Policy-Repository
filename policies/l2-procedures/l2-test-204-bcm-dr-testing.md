---
id: "L2-TEST-204"
title: "BCM/DR Testing Standard"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "L1-BC-008; ISO 27001 A.5.29-5.30"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-TEST-204 — BCM/DR Testing Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| TEST-R01 | Annual BCM/DR test covering all critical services. | `IF year_end THEN execute(bcm_dr_test)` |
| TEST-R02 | Test types: tabletop (minimum), simulation (T2+), full failover (T3+). | `IF tier >= T3 THEN test_type = full_failover` |
| TEST-R03 | Test results documented per L3-TEST-204. Findings tracked to closure. | `document(test_results); track(findings)` |

## Dependencies

- **Explicit**: `L1-BC-008`, `L3-TEST-204`
