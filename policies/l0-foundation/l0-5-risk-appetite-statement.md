---
id: "L0-5"
title: "Risk Appetite Statement"
type: "Appetite"
level: "L0"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "Board"
classification: "Confidential — Internal"
references: "ISO 27001:2022 Cl.6.1; ISO 31000:2018"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L0-5 — Risk Appetite Statement

## Scope

Defines Protofire's tolerance for risk across all categories: operational, compliance, financial, reputational, and technical.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-5-R01 | Zero appetite for sanctions violations (OFAC, EU). | HS-01: absolute rejection |
| L0-5-R02 | Zero appetite for operating without signed contractual framework. | HS-02: absolute block |
| L0-5-R03 | Low appetite for unaudited high-TVL deployments. | HS-03: P3=4 auto-escalation |
| L0-5-R04 | Low appetite for client concentration risk. | HS-04: C2=4 + GRC Committee review |
| L0-5-R05 | Low appetite for unpaid work beyond 60 days. | HS-05: stop-work trigger |
| L0-5-R06 | Zero appetite for irreversible deployment without gate clearance. | HS-06: deployment block |
| L0-5-R07 | Zero appetite for ambiguous key custody at deployment. | HS-07: deployment block |
| L0-5-R08 | Moderate appetite for T1 operational risks with standard controls. | T1: NO sole acceptance; 6-month review |
| L0-5-R09 | Low appetite for T2+ risks; requires enhanced governance. | T2+: enhanced gates, DPIA if EU data, budget floors |
| L0-5-R10 | Security budget floor per Gordon-Loeb: 37% of Expected Loss maximum for T3. | IF tier = T3 THEN budget_floor = 0.20 * expected_loss |

## Dependencies

- **Explicit**: [L0-1](l0-1-grc-charter.md), [L1-ERM-001](../l1-standards/l1-erm-001-risk-governance.md)
