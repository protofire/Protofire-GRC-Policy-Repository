---
id: "L1-ERM-001"
title: "Enterprise Risk Governance & Acceptance Authority Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "CEO + Board"
classification: "Confidential — Internal"
references: "L0-1; L0-5; ISO 27001 Cl.6.1.2; ISO 31000; NIST GV.RM"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-ERM-001 — Enterprise Risk Governance & Acceptance Authority Standard

## Scope
Enterprise-wide risk governance: scoring model, acceptance tiers, Hard Stop definitions (source of truth), KRI framework.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| ERM-R01 | C/B/P composite scoring model is mandatory for all engagements. | IF engagement AND cbp_score = NULL THEN block(G2) |
| ERM-R02 | Risk acceptance: T1=NO sole, T2=NO+CFO, T3=CEO/Board. Non-delegable. | authority_matrix(tier) |
| ERM-R03 | Hard Stops HS-01–HS-07 defined here. This section is the single source of truth. | See [hard-stops.md](../../definitions/hard-stops.md) |
| ERM-R04 | Risk register reviewed at tier-appropriate frequency. | See POL-003-R06 |
| ERM-R05 | Residual risk acceptance requires written sign-off at appropriate authority level. | IF residual_risk.accepted THEN require(written_signoff, authority_level) |

## Dependencies
- **Explicit**: [L0-5](../l0-foundation/l0-5-risk-appetite-statement.md), [OPS-001](ops-001-risk-scoring-framework.md), [REG-501](../l6-registers/reg-501-risk-register.md)
