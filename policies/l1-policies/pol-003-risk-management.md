---
id: "POL-003"
title: "Risk Management Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NO + DoE"
classification: "Confidential — Internal"
references: "GRC-PF-001; L1-ERM-001; ISO 27001:2022 Cl.6.1.2; ISO 31000; OPS-001"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-003 — Risk Management Policy

## Scope

All Protofire engagements. Extends L1-ERM-001 with delivery-specific risk management.

## Definitions

See: [risk-tiers.md](../../definitions/risk-tiers.md), [terms.md](../../definitions/terms.md)

## Atomic Requirements

### §2 — C/B/P Scoring

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-003-R01 | All projects scored using C/B/P model before Step 3 (MSA execution). | IF cbp_score = NULL AND step >= 3 THEN block(G2) |
| POL-003-R02 | Score determines governance tier (T1–T4) for entire engagement. | tier = classify(composite_score) |
| POL-003-R03 | Full scoring methodology defined in OPS-001. In conflict, OPS-001 prevails. | reference(OPS-001) |

### §3 — Risk Register

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-003-R04 | Phase-specific risk register maintained per engagement. 18 risk categories mapped to lifecycle. | IF engagement_active THEN risk_register.exists = TRUE |
| POL-003-R05 | Each risk has: owner, C/B/P score, tier, treatment plan, gate linkage, KRI reference. | IF risk.fields_incomplete THEN flag(non_compliant) |

### §4 — Review Governance

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-003-R06 | Review frequency scales with tier: T1=6mo, T2=3mo, T3=monthly, T4=continuous. | IF tier = T3 AND last_review > 30d THEN flag(overdue) |

## Controls

[CTL-GOV-005](../../controls/control-catalogue.md), [CTL-GOV-006](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L1-ERM-001](../l1-standards/l1-erm-001-risk-governance.md), [OPS-001](../l1-standards/ops-001-risk-scoring-framework.md), [REG-501](../l6-registers/reg-501-risk-register.md)
