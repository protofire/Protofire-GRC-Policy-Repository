---
id: "OPS-001"
title: "Project Risk Scoring Framework (Annex A to L1-ERM-001)"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "GRC-Committee"
approver: "NOC"
classification: "Confidential — Internal"
references: "L1-ERM-001; ISO 27001 Cl.6.1.2"
last_change: "2026-04-08"
last_approval: "Pending"
---

# OPS-001 — Project Risk Scoring Framework (Annex A to L1-ERM-001)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| OPS-R01 | 9 sub-scores: C1-C3, B1-B3, P1-P3. Each scored 1–4. | `IF sub_score NOT IN [1,2,3,4] THEN reject()` |
| OPS-R02 | Composite = weighted average of pillar averages. | `composite = w_c*avg(C) + w_b*avg(B) + w_p*avg(P)` |
| OPS-R03 | Tier classification: T1(1.0-2.9), T2(3.0-3.5), T3(3.6-4.0), T4(escalated). | `tier = classify(composite)` |
| OPS-R04 | Hard Stop auto-scoring: HS triggers override individual sub-scores to 4. | `IF hs_triggered(HS-03) THEN set(P3, 4)` |

