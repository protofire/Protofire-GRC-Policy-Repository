---
id: "POL-009"
title: "Exception & Deviation Management Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "DoE"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 Cl.6.1.3; NIST PM-6; SOC 2 CC3.4"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-009 — Exception & Deviation Management Policy

## Scope

All deviations from GRC-PF-001 and component policies.

## Definitions

See: [exception-classes.md](../../definitions/exception-classes.md)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-009-R01 | 4-class exception model (E1–E4). | See [exception-classes.md](../../definitions/exception-classes.md) |
| POL-009-R02 | HS-01 (OFAC) and HS-02 (no MSA) cannot be excepted under any circumstance. | IF exception_target IN [HS-01, HS-02] THEN reject(exception) |
| POL-009-R03 | All exceptions recorded in REG-506 with documentation. | IF exception_approved THEN log(REG-506) |
| POL-009-R04 | Automatic lapse at expiry. Re-application required for renewal. | IF exception.expired THEN policy.reapplies |
| POL-009-R05 | E4 (Critical): one-time only. No renewal without full re-approval. | IF E4.renewal_requested THEN require(full_reapproval) |
| POL-009-R06 | Exception register reviewed monthly by CISO. | IF month_end THEN CISO.review(REG-506) |

## Dependencies

- **Explicit**: [REG-506](../l6-registers/reg-506-exception-register.md)
