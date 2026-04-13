---
id: "L2-DEL-101"
title: "8-Stage Delivery Governance Procedure (Track A/B)"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "Head-of-Delivery"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-001; L1-SDLC-003; STD-101"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-DEL-101 — 8-Stage Delivery Governance Procedure (Track A/B)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| DEL-R01 | 8-stage gate process mandatory for all engagements. | `IF engagement THEN gates = [G1..G8]` |
| DEL-R02 | Track A: Protofire bears all risk. Track B: client risk with Protofire delivery. | `classify(track)` |
| DEL-R03 | Gate passage requires all mandatory signers and evidence. | `IF signer.absent OR evidence.missing THEN block(gate)` |
| DEL-R04 | This procedure uses the 8-stage gate model. Authoritative 12-step mapping: see lifecycle-model.md. | `reference(lifecycle-model.md)` |

## Dependencies

- **Explicit**: `STD-101`, `CL-PHASE-001`, `L1-SDLC-003`
