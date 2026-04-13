---
id: "POL-001"
title: "Project Governance Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "Node-Owner"
approver: "CISO advisory"
classification: "Confidential — Internal"
references: "GRC-PF-001; L0-1; L1-ERM-001; STD-101"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-001 — Project Governance Policy

## Scope

All Protofire project engagements (Track A and Track B). Governs lifecycle compliance, Hard Stop enforcement, governance tiers, and role assignments.

## Definitions

See: [terms.md](../../definitions/terms.md), [hard-stops.md](../../definitions/hard-stops.md), [lifecycle-model.md](../../definitions/lifecycle-model.md)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-001-R01 | All engagements follow the mandatory 12-step lifecycle. No step may be skipped. | IF step_skipped THEN block(next_gate) |
| POL-001-R02 | Each gate requires designated signers per [lifecycle-model.md](../../definitions/lifecycle-model.md). | IF required_signer.absent THEN gate_invalid |
| POL-001-R03 | Hard Stop conditions HS-01 through HS-07 are enforced at designated gates. | See [hard-stops.md](../../definitions/hard-stops.md) |
| POL-001-R04 | Governance tier (T1–T4) is determined by Composite Risk Score before G2. | IF cbp_score = NULL at G2 THEN block(G2) |
| POL-001-R05 | Tier determines: approval authority, review cadence, budget floor, gate intensity. | See [risk-tiers.md](../../definitions/risk-tiers.md) |
| POL-001-R06 | Node Owner acting as PM and AM must obtain DoE or fCTO co-sign at T2+. | IF NO.roles INCLUDES [PM, AM] AND tier >= T2 THEN require(DoE_co_sign) |
| POL-001-R07 | Track B engagements require client written acknowledgement for all risk waivers. | IF track = B AND waiver_requested THEN require(client_signature) |
| POL-001-R08 | All gate decisions recorded in gate record with timestamp, signers, and evidence references. | IF gate_passed THEN create(gate_record) |

## Controls

[CTL-GOV-001](../../controls/control-catalogue.md), [CTL-GOV-002](../../controls/control-catalogue.md), [CTL-GOV-003](../../controls/control-catalogue.md), [CTL-GOV-004](../../controls/control-catalogue.md)

## Roles

| Role | R/A/C/I |
|---|---|
| NO | Accountable for all gate decisions |
| CISO | Consulted on all gates; Accountable for G4, G7 |
| PM | Responsible for lifecycle execution |
| AM | Responsible for pre-sales gates (G1–G2) |

## Exceptions

Per [POL-009](pol-009-exception-deviation.md). Hard Stop exceptions: E4 class only (HS-01 and HS-02 cannot be excepted).

## Dependencies

- **Explicit**: [STD-101](../l1-standards/std-101-delivery-security.md), [L1-ERM-001](../l1-standards/l1-erm-001-risk-governance.md), [CL-PHASE-001](../l5-checklists/cl-phase-001-audit-checklists.md)
- **Implicit**: All L2 delivery procedures
