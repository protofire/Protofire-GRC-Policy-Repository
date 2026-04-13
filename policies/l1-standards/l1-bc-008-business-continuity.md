---
id: "L1-BC-008"
title: "Business Continuity Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-002; ISO 22301; ISO 27001 A.5.29-5.30"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-BC-008 — Business Continuity Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| BC-R01 | BIA (Business Impact Analysis) for all critical services. Updated annually. | `IF bia_age > 365d THEN flag(overdue)` |
| BC-R02 | DR plan documented and tested annually per L2-TEST-204. | `IF dr_test_age > 365d THEN flag(overdue)` |
| BC-R03 | RTO and RPO defined per service tier. | `IF rto = NULL OR rpo = NULL THEN flag(gap)` |
| BC-R04 | On-chain pause/circuit-breaker mechanism for DeFi protocols. | `IF defi AND pause_mechanism = FALSE THEN flag(critical)` |

