---
id: "L1-HR-010"
title: "Personnel Security Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-004; ISO 27001 A.6.1-6.8; NIST PR.AT"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-HR-010 — Personnel Security Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| HR-R01 | Background verification for all personnel with access to production systems. | `IF production_access AND background_check = FALSE THEN block(access)` |
| HR-R02 | Security awareness training annually. Completion tracked. | `IF training_age > 365d THEN block(system_access_renewal)` |
| HR-R03 | NDA signed before access to confidential information. | `IF nda = FALSE THEN block(access)` |
| HR-R04 | Exit procedure: access revoked within 1 business day per POL-004. | `IF departure THEN deprovision(1_bday)` |

