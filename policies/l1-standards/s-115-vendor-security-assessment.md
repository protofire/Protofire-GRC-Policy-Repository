---
id: "S-115"
title: "Vendor Security Assessment Standard"
type: "Standard"
level: "L2-STD"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-007; ISO 27001 A.5.19-5.22; DORA Art.28"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# S-115 — Vendor Security Assessment Standard

## Scope
Assessment methodology for all third-party vendors per POL-007.

## Assessment Framework

| Vendor Class | Assessment Depth | Frequency | Assessor | Evidence |
|---|---|---|---|---|
| Critical (oracle, bridge, RPC) | Full security questionnaire + on-chain monitoring review + incident history | Annual | CISO + TL | Completed questionnaire, monitoring dashboard, SLA metrics |
| High (cloud, audit firm) | Security questionnaire + SOC 2 / ISO 27001 cert review | 18 months | CISO | Cert copies, questionnaire |
| Medium (tooling) | Self-assessment questionnaire | 2 years | GRC-MGR | Self-assessment form |
| Low (non-technical) | NDA + basic due diligence | At onboarding only | AM | NDA signed |

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| S115-R01 | Critical vendors assessed before onboarding. | IF critical AND assessment = NULL THEN block(onboard) |
| S115-R02 | Exit strategy documented for all Critical vendors. | IF critical AND exit_plan = NULL THEN flag(gap) |
| S115-R03 | Vendor incidents reported to CISO within 24h. | IF vendor_incident THEN notify(CISO, 24h) |
| S115-R04 | Sub-processor chain documented for all vendors handling DC-3+ data. | IF vendor.data_tier >= DC3 THEN document(sub_processors) |
