---
id: "L2-RISK-102"
title: "Delivery Risk Operations Procedure"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "Head-of-Risk"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-003; L1-ERM-001"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-RISK-102 — Delivery Risk Operations Procedure

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| RISK-R01 | Risk register maintained per engagement. Updated at each gate. | `IF gate_passed THEN update(risk_register)` |
| RISK-R02 | New risks logged within 24h of identification. | `IF risk_identified THEN log(REG-501, 24h)` |
| RISK-R03 | Risk escalation: Amber to NO within 5 bdays; Red within 48h. | `IF risk.rag = Red THEN escalate(NO, 48h)` |

## Dependencies

- **Explicit**: `REG-501`, `L1-ERM-001`
