---
id: "POL-004"
title: "Access Control & Segregation of Duties Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 Cl.5.15-5.18; NIST AC-5/AC-6; SOC 2 CC6.2"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-004 — Access Control & Segregation of Duties Policy

## Scope

All systems, keys, and privileged functions across all engagements and infrastructure.

## Atomic Requirements

### §2.1–2.2 — Provisioning

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-004-R01 | Least privilege: role-scoped, project-scoped, time-limited access. | IF access_scope > role_scope THEN deny() |
| POL-004-R02 | Provisioning within 1 business day. Production access requires separate approval. | IF production_access THEN require(separate_approval) |
| POL-004-R03 | Deprovisioning within 1 business day of role change or departure. | IF trigger(role_change OR departure) THEN deprovision(1_bday) |

### §2.3 — Credentials

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-004-R04 | Shared credentials prohibited. Exception requires CISO waiver + compensating monitor. | IF credential.shared THEN require(CISO_waiver, compensating_control) |

### §2.4 — SoD

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-004-R05 | 7 SoD conflict scenarios defined with compensating controls. | See [sod-matrix.md](../../controls/sod-matrix.md) |
| POL-004-R06 | No self-approval where also Responsible. | IF approver = responsible_party THEN block() |

### §2.5 — On-chain

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-004-R07 | Production on-chain admin requires ≥ 2-of-3 multisig. | IF admin_signers < 2 THEN block(G7) |

### §2.6 — Review

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-004-R08 | Quarterly access review for all privileged accounts. Remediation within 5 business days. | IF quarter_end THEN review(privileged); fix(5_bdays) |

## Controls

[CTL-ACC-001](../../controls/control-catalogue.md) through [CTL-ACC-006](../../controls/control-catalogue.md), [CTL-SEC-007](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L2-ACCESS-203](../l2-procedures/l2-access-203-jml.md), [L1-HR-010](../l1-standards/l1-hr-010-personnel-security.md), [sod-matrix.md](../../controls/sod-matrix.md)
