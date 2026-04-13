---
id: "POL-002"
title: "Information Security Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001:2022; NIST SP 800-53; supersedes GL1-INFO-006"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-002 — Information Security Policy

## Scope

All information assets, systems, and processing activities within the ISMS scope ([L0-4](../l0-foundation/l0-4-isms-scope-statement.md)).

## Definitions

See: [terms.md](../../definitions/terms.md), [roles.md](../../definitions/roles.md)

## Atomic Requirements

### §3.1 — Development Security

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R01 | Peer code review with minimum 2 independent reviewers. TL mandatory for security-critical code. | IF security_critical AND tl_review = FALSE THEN block(merge) |
| POL-002-R02 | SAST enforced at CI/CD gate. Critical/High findings block merge. | IF sast_severity IN [Critical, High] THEN block(merge) |
| POL-002-R03 | Secret scanning enforced at CI/CD gate. Any finding blocks merge. | IF secret_scan.count > 0 THEN block(merge) |

### §3.2 — Access Security

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R04 | Principle of least privilege. Role-scoped, time-limited, project-scoped. | IF access > role_scope THEN deny() |

### §3.3 — Cryptographic Security

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R05 | No hard-coded credentials in source code. HSM/vault for production key material. | IF hardcoded_secret THEN block(merge); require(vault_integration) |

### §3.5 — Deployment Security

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R06 | Threat model covering 4 categories: technical, economic, governance, human failure. | IF threat_model.categories < 4 THEN block(G4) |
| POL-002-R07 | Two-person rule: deployer ≠ reviewer at testnet and mainnet. | IF deployer = reviewer THEN block(deployment) |
| POL-002-R08 | External audit mandatory for TVL > $1M or custody/bridge/cross-chain/lending. | IF (tvl > 1M OR custody OR bridge) AND no_audit THEN trigger(HS-03) |

### §3.6 — Incident Response

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R09 | GDPR Art.33 notification within 72 hours of awareness. Internal report to CISO within 4 hours per POL-011 §8.2. | IF personal_data_breach THEN notify(CISO, 4h); notify(authority, 72h) |

### §4 — Assurance

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-002-R10 | Monthly Security 360 reviews. Quarterly access reviews. Annual internal audit. | Cadence enforced via evidence calendar |
| POL-002-R11 | Non-compliance tracked in exception register per POL-009. | IF non_compliance THEN log(REG-506) |

## Controls

[CTL-SEC-001](../../controls/control-catalogue.md) through [CTL-SEC-010](../../controls/control-catalogue.md)

## Roles

| Role | R/A/C/I |
|---|---|
| CISO | Accountable for policy; maintains training programme |
| TL | Responsible for threat model, code review |
| DevOps | Responsible for CI/CD security gates, deployment |
| QA | Responsible for independent testing |

## Exceptions

Per [POL-009](pol-009-exception-deviation.md). Core controls (§3) are E3 class.

## Dependencies

- **Explicit**: [L1-SDLC-003](../l1-standards/l1-sdlc-003-secure-delivery.md), [L1-KEY-005](../l1-standards/l1-key-005-key-treasury.md), [L1-INFRA-009](../l1-standards/l1-infra-009-infrastructure-security.md)
- **Supersedes**: GL1-INFO-006
