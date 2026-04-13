---
id: "STD-101"
title: "Delivery Security Standard (8-Stage)"
type: "Standard"
level: "L2-STD"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-001; L1-SDLC-003; L2-DEL-101"
last_change: "2026-04-08"
last_approval: "Pending"
---

# STD-101 — Delivery Security Standard (8-Stage)

## Scope
Maps mandatory security controls to each of the 12 lifecycle steps / 8 gates. Defines evidence requirements, RACI, and Hard Stop checkpoints per gate.

## Atomic Requirements

See: [gate-evidence-map.md](../../mappings/gate-evidence-map.md) for the full gate × evidence matrix.
See: [lifecycle-model.md](../../definitions/lifecycle-model.md) for step ↔ gate mapping.
See: [control-catalogue.md](../../controls/control-catalogue.md) for control definitions.

| Req ID | Requirement | Enforcement |
|---|---|---|
| STD-R01 | Each gate has mandatory controls, signers, and evidence per the gate-evidence map. | IF evidence_missing THEN block(gate) |
| STD-R02 | Preventive controls applied before the gate; detective controls applied after. | control_timing(gate) |
| STD-R03 | All gate decisions produce a gate record with: decision, signers, timestamp, evidence links, conditions. | create(gate_record) |

## Dependencies
- **Explicit**: [POL-001](../l1-policies/pol-001-project-governance.md), [CL-PHASE-001](../l5-checklists/cl-phase-001-audit-checklists.md)
