---
id: "PR-208"
title: "Personal Data Breach Notification Procedure"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO-DPO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-011 §8; GDPR Art.33-34"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# PR-208 — Personal Data Breach Notification Procedure

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| PR208-R01 | Breach discovered → internal report to CISO within 4 hours. | `IF breach THEN notify(CISO, 4h)` |
| PR208-R02 | CISO assesses: personal data involved? Risk to data subjects? | `assess(scope, severity, data_subjects_affected)` |
| PR208-R03 | Supervisory authority notification within 72 hours if risk to rights. | `IF risk_to_rights THEN notify(authority, 72h)` |
| PR208-R04 | Data subject notification without undue delay if high risk. | `IF high_risk THEN notify(data_subjects)` |
| PR208-R05 | Breach record maintained in incident log with: timeline, scope, actions, notifications. | `log(breach_record)` |

## Dependencies

- **Explicit**: `POL-011`, `L2-INC-201`
