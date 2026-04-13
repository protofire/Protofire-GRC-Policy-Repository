---
id: "POL-005"
title: "Change Management Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "Node-Owner"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 Cl.8.32"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-005 — Change Management Policy

## Scope

All changes to code, infrastructure, and operational upgrades across all engagements.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-005-R01 | 5-class change model (C1–C5) with approval chains, documentation, and rollback per class. | IF change_request THEN classify(C1_C5) |
| POL-005-R02 | C1 (Trivial): TL approval. C2 (Minor): TL + PM. C3 (Standard): TL + PM + NO. C4 (Major): TL + PM + NO + CISO. C5 (Emergency): NO + CISO; post-hoc documentation within 24h. | route_approval(change_class) |
| POL-005-R03 | On-chain change for TVL > $1M requires mini-cycle: threat model update, testnet validation, two-person deployment. | IF tvl > 1M AND on_chain THEN require(mini_cycle) |
| POL-005-R04 | Rollback plan required for C3+ changes. | IF change_class >= C3 THEN require(rollback_plan) |
| POL-005-R05 | All changes logged with: requestor, class, approvers, timestamp, rollback status. | log(change_record) |

## Controls

[CTL-CHG-001](../../controls/control-catalogue.md), [CTL-CHG-002](../../controls/control-catalogue.md), [CTL-CHG-003](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L2-CHANGE-205](../l2-procedures/l2-change-205-change-management.md)
