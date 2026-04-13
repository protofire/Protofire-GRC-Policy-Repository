---
id: "POL-010"
title: "Monitoring & Continuous Assurance Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 Cl.9.1-9.3; COBIT MEA01.04"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-010 — Monitoring & Continuous Assurance Policy

## Scope

Monitoring programme, KRIs, internal audit, and continuous improvement for the ISMS.

## Atomic Requirements

### §2 — Monitoring Cadence

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-010-R01 | Weekly Security 360 review: risk register, incidents, access anomalies. | IF week_end THEN execute(security_360) |
| POL-010-R02 | Annual internal audit covering full ISMS scope. CAPA plan required. | IF year_end THEN execute(internal_audit); produce(CAPA) |
| POL-010-R03 | Annual management review: ISMS performance, policy adequacy, resources. | IF year_end THEN execute(management_review) |

### §3 — KRI Dashboard

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-010-R04 | 8 KRIs with Green/Amber/Red thresholds reported monthly. | IF month_end THEN report(kri_dashboard) |
| POL-010-R05 | Red KRI triggers NO escalation within 48 hours. | IF kri.status = Red THEN escalate(NO, 48h) |

## Controls

[CTL-ASR-001](../../controls/control-catalogue.md) through [CTL-ASR-005](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L2-RISK-102](../l2-procedures/l2-risk-102-risk-operations.md), [L2-INC-201](../l2-procedures/l2-inc-201-incident-response.md)
