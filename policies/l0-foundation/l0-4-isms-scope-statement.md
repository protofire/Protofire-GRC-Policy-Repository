---
id: "L0-4"
title: "ISMS Scope Statement"
type: "Scope"
level: "L0"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "Board"
classification: "Confidential — Internal"
references: "ISO 27001:2022 Cl.4.3"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L0-4 — ISMS Scope Statement

## Scope

Defines the boundaries of the Protofire ISMS: organizational units, services, information assets, locations, and technologies in scope.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| L0-4-R01 | ISMS covers all Protofire nodes and their engagements (Track A and Track B). | IF node_active THEN isms_in_scope = TRUE |
| L0-4-R02 | Scope includes: smart contract development, DeFi protocol integration, blockchain infrastructure, key management, monitoring services. | Enumerated services list |
| L0-4-R03 | Personnel in scope: all employees, contractors, and AI agents involved in delivery. | IF personnel.role IN delivery_roles THEN isms_applies = TRUE |
| L0-4-R04 | Locations: primarily remote; any location where Protofire information is processed. | Geographic independence |
| L0-4-R05 | Exclusions: none currently. All services are in scope. | IF exclusion_requested THEN require(CISO_justification, Board_approval) |

## Controls

[CTL-GOV-007](../../controls/control-catalogue.md)

## Dependencies

- **Explicit**: [L0-1](l0-1-grc-charter.md)
