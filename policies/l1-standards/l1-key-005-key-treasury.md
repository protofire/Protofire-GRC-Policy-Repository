---
id: "L1-KEY-005"
title: "Key/Treasury & Signing Ceremonies Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-002; ISO 27001 A.8.24; NIST PR.DS"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-KEY-005 — Key/Treasury & Signing Ceremonies Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| KEY-R01 | Production keys generated in signing ceremony per CL-411. | `IF production_keys THEN require(CL-411)` |
| KEY-R02 | HSM or MPC/vault for all production key material. | `IF key_storage != HSM_OR_VAULT THEN block(G7)` |
| KEY-R03 | Multisig 2-of-3 minimum for production admin. | `IF admin_signers < 2 THEN block()` |
| KEY-R04 | Key rotation schedule: annually or upon personnel change. | `IF key_age > 365d OR personnel_change THEN rotate()` |

