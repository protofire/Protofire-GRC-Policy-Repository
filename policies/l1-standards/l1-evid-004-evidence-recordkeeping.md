---
id: "L1-EVID-004"
title: "Evidence & Recordkeeping Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "CEO/Board"
classification: "Confidential — Internal"
references: "POL-008; ISO 27001 Cl.7.5"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-EVID-004 — Evidence & Recordkeeping Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| EVID-R01 | All gate records retain: timestamp, signers, evidence links, decision. | `IF gate_passed THEN create(gate_record)` |
| EVID-R02 | Security logs retained minimum 365 days. Immutable logging required. | `IF log_age < 365d THEN retention = active` |
| EVID-R03 | MSA and legal docs retained 7 years. | `IF doc_type = legal THEN retention = 7y` |
| EVID-R04 | Evidence calendar: 23 activities mapped month-by-month. | `See GRC-MASTER-001 Part III` |

