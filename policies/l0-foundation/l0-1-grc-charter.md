---
id: "L0-1"
title: "GRC Charter — Information Security Charter"
type: "Charter"
level: "L0"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "CEO + Board"
classification: "Confidential — Internal"
references: "ISO 27001:2022 Cl.5.1-5.3; NIST CSF 2.0 GV.OC/GV.RM"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L0-1 — GRC Charter — Information Security Charter

## Scope

Applies to: all Protofire nodes, all engagement types (Track A and Track B), all personnel (employees, contractors, agents).

Defines: governance structure, role model, committee composition, document hierarchy, risk acceptance framework, Hard Stop conditions.

## Definitions

See: [roles.md](../../definitions/roles.md), [terms.md](../../definitions/terms.md), [hard-stops.md](../../definitions/hard-stops.md)

## Atomic Requirements

### §4 — Role Model

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-1-R01 | Node Owner is the primary risk acceptance authority at node level. | IF risk_decision THEN require(NO_signature) |
| L0-1-R02 | CISO holds policy authority over the ISMS and is the mandatory co-signer for G4 and G7. | IF gate IN [G4, G7] THEN require(CISO_signature) |
| L0-1-R03 | GRC Manager is the operational backbone (min 0.5 FTE). Escalate shortfall to CEO within 5 business days. | IF grc_mgr_fte < 0.5 THEN escalate(CEO, 5_bdays) |
| L0-1-R04 | DPO function is held by CISO. Succession: CEO appoints interim within 5 business days if unavailable. | IF ciso_unavailable THEN ceo.appoint_interim_dpo(5_bdays) |

### §5 — Governance Committee

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-1-R05 | GRC Committee meets monthly (T1–T2) or bi-weekly (T3+). Quorum: NO + CISO + 1 additional. | IF tier >= T3 THEN meeting_cadence = biweekly |
| L0-1-R06 | CEO/Board co-approves all L0 and L1 document changes. | IF doc.level IN [L0, L1] THEN require(CEO_approval) |

### §6 — Document Hierarchy

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-1-R07 | Six-level hierarchy: L0 Foundation > L1 Policy/Standard > L2 Procedure > L3 Work Instruction > L4 Guideline > L5 Checklist > L6 Register. | IF conflict(doc_a, doc_b) THEN higher_level.prevails |
| L0-1-R08 | All documents follow consistent numbering (POL-xxx canonical) and metadata standards. | IF doc.numbering != POL_xxx AND doc.level = L1 THEN flag(ISS-001) |

### §7 — Risk Acceptance and Hard Stops

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-1-R09 | Risk acceptance authority: T1 = NO sole; T2 = NO + CFO; T3 = CEO/Board. Non-delegable. | See [risk-tiers.md](../../definitions/risk-tiers.md) |
| L0-1-R10 | Seven Hard Stops (HS-01 through HS-07) are mandatory blocking conditions. | See [hard-stops.md](../../definitions/hard-stops.md) |
| L0-1-R11 | HS-01 (OFAC) and HS-02 (no MSA) are absolute prohibitions — no exception permitted. | IF hs IN [HS-01, HS-02] THEN exception_permitted = FALSE |
| L0-1-R12 | Hard Stop table single source of truth is L1-ERM-001 §7.2. | IF hard_stop_definition_needed THEN reference(L1-ERM-001) |

## Controls

[CTL-GOV-001](../../controls/control-catalogue.md), [CTL-GOV-002](../../controls/control-catalogue.md), [CTL-GOV-003](../../controls/control-catalogue.md), [CTL-GOV-004](../../controls/control-catalogue.md), [CTL-GOV-007](../../controls/control-catalogue.md)

## Roles

| Role | Responsibility | Authority |
|---|---|---|
| CEO | Charter sponsor. T3+ risk acceptance. L0 amendments. | Approve |
| CISO | Policy authority. ISMS lead. Charter drafter. | Author, Co-approve |
| NO | Node-level governance. Risk acceptance (T1 sole). | Execute |
| GRC-MGR | Operational maintenance of charter artefacts. | Maintain |

## Exceptions

Amendments to this charter require CEO + Board approval. No exception process applies to L0 documents — changes must go through formal amendment.

## Dependencies

- **Explicit**: [L0-4](l0-4-isms-scope-statement.md), [L0-5](l0-5-risk-appetite-statement.md), [L1-ERM-001](../l1-standards/l1-erm-001-risk-governance.md)
- **Implicit**: All L1 policies derive authority from this charter.
