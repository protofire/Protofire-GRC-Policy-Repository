---
id: "L2-INC-201"
title: "Incident Response Procedure"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-010; ISO 27001 A.5.24-5.28; GDPR Art.33-34"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-INC-201 — Incident Response Procedure

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| INC-R01 | Incident severity: P0 (Critical), P1 (High), P2 (Medium), P3 (Low). | `classify(severity)` |
| INC-R02 | P0/P1: CISO notified within 1 hour. War room within 2 hours. | `IF severity IN [P0,P1] THEN notify(CISO, 1h); war_room(2h)` |
| INC-R03 | Post-incident review within 5 business days for P0/P1. | `IF severity IN [P0,P1] THEN post_mortem(5_bdays)` |
| INC-R04 | Personal data breaches follow POL-011 §8 timelines (4h internal, 72h authority). | `IF personal_data_involved THEN follow(POL-011-R08, POL-011-R09)` |

## Dependencies

- **Explicit**: `POL-011`, `PR-208`
