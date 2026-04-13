---
id: "L1-SDLC-003"
title: "Secure Delivery Baseline for Web3/DeFi"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-002; ISO 27001 A.8.25-8.33; NIST PR.DS"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-SDLC-003 — Secure Delivery Baseline for Web3/DeFi

## Scope
Security baseline for all smart contract and Web3 delivery: coding standards, review gates, testing requirements, deployment controls.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| SDLC-R01 | Solidity/Vyper/Rust coding standards enforced via linter at CI. | IF lint_errors > 0 THEN block(merge) |
| SDLC-R02 | Static analysis (Slither, Mythril, or equivalent) mandatory. | IF sast_not_run THEN block(G5) |
| SDLC-R03 | Fuzz testing (Echidna, Foundry) for all DeFi protocols. | IF defi AND fuzz_testing = FALSE THEN flag(G5) |
| SDLC-R04 | Formal verification encouraged for TVL > $10M. | IF tvl > 10M THEN recommend(formal_verification) |
| SDLC-R05 | Testnet deployment mandatory before mainnet. No exceptions. | IF testnet_deployment = FALSE THEN block(G7) |
| SDLC-R06 | Deployment runbook documented and reviewed before G7. | IF runbook = NULL THEN block(G7) |

## Dependencies
- **Explicit**: [L2-DEL-101](../l2-procedures/l2-del-101-delivery-governance.md), [L2-ASSURE-103](../l2-procedures/l2-assure-103-external-assurance.md), [CL-PHASE-001](../l5-checklists/cl-phase-001-audit-checklists.md)
