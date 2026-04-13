---
id: "POL-011"
title: "Data Protection & Privacy Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO-DPO"
approver: "DoE + NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; GDPR Art.5-49; ISO 27001 A.5.34; NIST PR.DS"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-011 — Data Protection & Privacy Policy

## Scope

All personal data processing by Protofire as controller or processor. Covers GDPR, CCPA, LGPD, and sector-specific requirements.

## Definitions

See: [terms.md](../../definitions/terms.md) (DSR, DPIA, ROPA, DPO)

## Atomic Requirements

### §3–4 — Principles and Lawful Basis

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R01 | Data minimization: only collect personal data with identified lawful basis. | IF lawful_basis = NULL THEN reject(collection) |
| POL-011-R02 | Purpose limitation: data used only for stated purpose. | IF purpose_change THEN require(new_lawful_basis) |

### §5 — Privacy by Design

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R03 | Privacy impact considered at architecture phase (G4). | IF g4_review AND personal_data THEN require(privacy_assessment) |

### §6 — DPIA

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R04 | DPIA mandatory for T2+ engagements processing EU personal data. | IF tier >= T2 AND eu_data THEN require(DPIA_before_G4) |
| POL-011-R05 | Unresolved high-residual DPIA blocks G4. | IF dpia.residual_risk = HIGH AND unresolved THEN block(G4) |

### §7 — Data Subject Rights

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R06 | DSR acknowledged within 3 business days. | IF dsr_received THEN ack(3_bdays) |
| POL-011-R07 | DSR fulfilled within 30 calendar days. Extendable by 60d for complex requests with written notification. | IF dsr_complex THEN extend(60d, notify_subject) |

### §8 — Breach Notification

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R08 | Internal breach report to CISO within 4 hours of discovery. | IF breach_discovered THEN notify(CISO, 4h) |
| POL-011-R09 | Supervisory authority notification within 72 hours of awareness. | IF personal_data_breach THEN notify(authority, 72h) |
| POL-011-R10 | Data subjects notified without undue delay if high risk to rights. | IF risk_to_rights = HIGH THEN notify(data_subjects, without_undue_delay) |

### §9 — International Transfers

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R11 | Transfers outside EEA require safeguard mechanism (SCCs, adequacy, BCRs). | IF transfer_outside_eea AND safeguard = NULL THEN block(transfer) |

### §10 — Processor Obligations

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R12 | DPA (Data Processing Agreement) required with all sub-processors. | IF sub_processor AND dpa = NULL THEN block(engagement) |

### §12 — ROPA

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R13 | ROPA maintained and current for all processing activities. | IF new_processing THEN update(REG-505) |

### §13 — DPO

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-011-R14 | DPO function held by CISO. Succession: CEO appoints interim within 5 business days. | IF dpo_unavailable THEN ceo.appoint_interim(5_bdays) |

## Controls

[CTL-PRI-001](../../controls/control-catalogue.md) through [CTL-PRI-005](../../controls/control-catalogue.md), [CTL-SEC-008](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [PR-208](../l2-procedures/pr-208-breach-notification.md), [PR-209](../l2-procedures/pr-209-dsr-handling.md), [GL-304](../l3-work-instructions/gl-304-privacy-by-design.md), [CL-409](../l5-checklists/cl-409-dpia-screening.md), [REG-505](../l6-registers/reg-505-ropa.md), [REG-510](../l6-registers/reg-510-dpia-register.md)
