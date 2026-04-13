---
id: "L2-CHANGE-205"
title: "Change Management Procedure"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-005; L1-INFRA-009"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-CHANGE-205 — Change Management Procedure

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| CHG-R01 | All changes logged in change register with: requestor, class, approvers, timestamp. | `log(change_register)` |
| CHG-R02 | C3+ changes require documented rollback plan and test evidence. | `IF class >= C3 THEN require(rollback_plan, test_evidence)` |
| CHG-R03 | Emergency changes (C5): NO+CISO approval; post-hoc documentation within 24h. | `IF C5 THEN approve(NO, CISO); document(24h)` |
| CHG-R04 | Change freeze periods during critical deployment windows. | `IF deployment_window THEN freeze(non_critical_changes)` |

## Dependencies

- **Explicit**: `POL-005`, `L1-INFRA-009`
