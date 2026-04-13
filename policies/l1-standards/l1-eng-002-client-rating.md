---
id: "L1-ENG-002"
title: "Client Rating & Commercial Guardrails Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "L0-1; L1-ERM-001"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-ENG-002 — Client Rating & Commercial Guardrails Standard

## Scope
Client rating methodology, commercial guardrails, MSA requirements, payment terms.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| ENG-R01 | Client rated using C-pillar (C1–C3) before engagement acceptance. | IF c_score = NULL THEN block(G1) |
| ENG-R02 | MSA must contain: liability cap, IP assignment, termination clause, data processing terms. | IF msa_clause_missing THEN flag(CISO_review) |
| ENG-R03 | Payment terms: net-30 standard. Net-60 requires CFO approval. | IF payment_terms > 30 THEN require(CFO_approval) |
| ENG-R04 | Stop-work clause: mandatory for all Track B engagements. | IF track = B AND stop_work_absent THEN block(MSA_signing) |

## Dependencies
- **Explicit**: [L1-ERM-001](l1-erm-001-risk-governance.md)
