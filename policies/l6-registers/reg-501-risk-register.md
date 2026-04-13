---
id: "REG-501"
title: "Enterprise Risk Register"
type: "Register"
level: "L6"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Quarterly"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "L1-ERM-001; POL-003; OPS-001"
last_change: "2026-04-08"
last_approval: "Pending"
---

# REG-501 — Enterprise Risk Register

## Purpose

Register of all identified risks with C/B/P scoring, tier classification, treatment plans, and gate linkages.

## Schema

| Field | Description |
|---|---|
| Risk_ID | Unique identifier: RR-{category}-{seq} |
| Category | Operational / Web2-Infra / Web3 / Legal-Regulatory / Business |
| Description | Risk statement |
| C1_Jurisdiction | Score 1–4 |
| C2_Concentration | Score 1–4 |
| C3_Credibility | Score 1–4 |
| B1_Payment_Terms | Score 1–4 |
| B2_Payment_Discipline | Score 1–4 |
| B3_Diversification | Score 1–4 |
| P1_Tech_Complexity | Score 1–4 |
| P2_TVL_Custody | Score 1–4 |
| P3_Audit_Status | Score 1–4 |
| Composite_Score | Weighted average |
| Tier | T1/T2/T3/T4 |
| Hard_Stop_Flag | HS-01..HS-07 or NONE |
| Gate_Trigger | Gate where risk is assessed |
| Gate_Accept | Gate where risk is accepted |
| Owner | Named individual |
| Acceptance_Authority | NO/CFO/CEO per tier |
| Treatment_Type | Mitigate/Accept/Transfer/Avoid |
| Compensating_Controls | Control IDs from catalogue |
| Residual_Risk_Score | Post-treatment composite |
| KRI_Reference | KRI-01..KRI-10 |
| Last_Review | Date |
| Next_Review | Date |
| Review_Cadence | Per tier |

