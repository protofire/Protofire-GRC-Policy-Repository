---
id: "POL-006"
title: "Testing & Quality Assurance Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "TL"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 Cl.8.29"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-006 — Testing & Quality Assurance Policy

## Scope

All QA activities: internal review, testnet validation, and external audit requirements.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-006-R01 | Minimum 2 independent code reviews before G5. QA ≠ code author. | IF reviews < 2 OR qa = author THEN block(G5) |
| POL-006-R02 | Test evidence documented per L3-TEST-204. | IF test_evidence = NULL THEN block(G5) |
| POL-006-R03 | SAST and secret scanning mandatory at CI/CD gate. | IF sast_not_run THEN block(merge) |
| POL-006-R04 | Fuzz testing (Echidna) and property testing for DeFi protocols. | IF protocol_type = DeFi THEN require(fuzz_testing) |
| POL-006-R05 | External audit decision at G6 per L2-ASSURE-103 criteria. | See HS-03 triggers |

## Controls

[CTL-SEC-001](../../controls/control-catalogue.md), [CTL-SEC-002](../../controls/control-catalogue.md), [CTL-ASR-005](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L2-ASSURE-103](../l2-procedures/l2-assure-103-external-assurance.md), [L3-TEST-204](../l3-work-instructions/l3-test-204-test-evidence.md)
