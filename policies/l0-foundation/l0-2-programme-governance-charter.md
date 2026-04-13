---
id: "L0-2"
title: "GRC Programme Governance Charter"
type: "Charter"
level: "L0"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "GRC-Manager"
approver: "CEO + CISO"
classification: "Confidential — Internal"
references: "L0-1; ISO 27001:2022 Cl.5.1-5.3,6.1,9.3; NIST CSF 2.0"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L0-2 — GRC Programme Governance Charter

## Scope

Governs the GRC programme itself: committee structure, resource commitments, programme cadence, KPI/KRI dashboard, and gap remediation tracking.

## Definitions

See: [roles.md](../../definitions/roles.md), [terms.md](../../definitions/terms.md)

## Atomic Requirements

### §4 — Programme Roles

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-2-R01 | GRC Manager role is distinct from CISO. Min 0.5 FTE or contracted. | IF grc_manager = NULL THEN escalate(CEO, 5_bdays) |
| L0-2-R02 | vCISO commitment: 8–12h/week; 4-hour escalation response for P0/P1 events. | IF vciso_response_time > 4h AND severity IN [P0, P1] THEN flag(breach) |

### §5 — Decision Rights

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-2-R03 | L0 amendments: CEO + Board approve. | IF amendment.level = L0 THEN require(CEO_AND_Board) |
| L0-2-R04 | L1 Standards: CISO proposes; CEO approves. | IF amendment.level = L1 THEN require(CISO_propose, CEO_approve) |
| L0-2-R05 | L2 Procedures: CISO approves; CEO notified. | IF amendment.level = L2 THEN require(CISO_approve); notify(CEO) |

### §6 — Resource Commitments

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-2-R06 | GRC Manager shortfall: report to CEO at monthly review; coverage plan within 10 business days. | IF grc_mgr_fte < 0.5 THEN report(CEO, monthly); coverage_plan(10_bdays) |
| L0-2-R07 | vCISO shortfall: CEO notified within 5 business days if sustained. | IF vciso_hours < 8_per_week FOR 2_consecutive_weeks THEN notify(CEO) |

### §8 — KRI Dashboard

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-2-R08 | 8–10 KRIs with RAG thresholds reported monthly. Red triggers NO escalation within 48h. | IF kri.status = Red THEN escalate(NO, 48h) |

### §10 — Gap Remediation

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-2-R09 | S-109 (Data Classification Standard) required within 90 days. | IF s109_status = absent AND days_since_approval > 90 THEN flag(overdue) |
| L0-2-R10 | S-115 (Vendor Security Assessment Standard) required within 90 days. | IF s115_status = absent AND days_since_approval > 90 THEN flag(overdue) |
| L0-2-R11 | REG-505 (ROPA) required within 60 days. | IF reg505_status = absent AND days_since_approval > 60 THEN flag(overdue) |

## Controls

[CTL-GOV-003](../../controls/control-catalogue.md), [CTL-ASR-001](../../controls/control-catalogue.md), [CTL-ASR-004](../../controls/control-catalogue.md)

## Roles

| Role | Responsibility |
|---|---|
| GRC-MGR | Programme operations, register maintenance, evidence calendar |
| CISO | Programme direction, policy authority, KRI analysis |
| CEO | Programme sponsor, resource guarantor, escalation point |

## Exceptions

Governed by L0-1 amendment process. L0-2 cannot override L0-1.

## Dependencies

- **Explicit**: [L0-1](l0-1-grc-charter.md)
- **Implicit**: All programme operational activities
