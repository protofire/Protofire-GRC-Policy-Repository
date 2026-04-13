---
id: "PR-209"
title: "Data Subject Request Handling Procedure"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO-DPO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-011 §7; GDPR Art.12-23"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# PR-209 — Data Subject Request Handling Procedure

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| PR209-R01 | DSR received → acknowledged to data subject within 3 business days. | `IF dsr THEN ack(3_bdays)` |
| PR209-R02 | Identity verification before fulfillment. | `verify(identity)` |
| PR209-R03 | Fulfillment within 30 calendar days. Complex: extend 60d with written notification. | `IF complex THEN extend(60d, notify)` |
| PR209-R04 | Rights supported: access, rectification, erasure, restriction, portability, objection. | `support(all_gdpr_rights)` |
| PR209-R05 | DSR log maintained in REG-510 (or equivalent). | `log(dsr_record)` |

## Dependencies

- **Explicit**: `POL-011`
