---
id: "L2-ACCESS-203"
title: "Access Management Procedure (Joiner/Mover/Leaver)"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-004; L1-HR-010"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-ACCESS-203 — Access Management Procedure (Joiner/Mover/Leaver)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| ACC-R01 | Joiner: access provisioned within 1 bday based on role template. | `IF joiner THEN provision(role_template, 1_bday)` |
| ACC-R02 | Mover: access adjusted within 1 bday. Old access revoked; new access granted. | `IF mover THEN adjust(1_bday)` |
| ACC-R03 | Leaver: all access revoked within 1 bday. Keys rotated if applicable. | `IF leaver THEN revoke_all(1_bday); rotate_keys_if_applicable()` |
| ACC-R04 | Quarterly access certification: all privileged accounts reviewed. | `IF quarter_end THEN certify(privileged_accounts)` |

## Dependencies

- **Explicit**: `POL-004`, `L1-HR-010`
