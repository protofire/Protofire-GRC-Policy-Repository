---
id: "POL-007"
title: "Third-Party & Vendor Risk Policy"
type: "Policy"
level: "L1"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "Node-Owner"
approver: "NOC"
classification: "Confidential — Internal"
references: "GRC-PF-001; ISO 27001 A.5.19-5.22; NIST GV.SC; DORA Art.28"
last_change: "2026-04-08"
last_approval: "Pending"
parent: "GRC-PF-001"
---

# POL-007 — Third-Party & Vendor Risk Policy

## Scope

All third-party and vendor relationships: oracle providers, bridge operators, RPC providers, cloud infrastructure, audit firms, and tooling vendors.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| POL-007-R01 | All critical third parties assessed per S-115 before onboarding. | IF vendor.critical AND assessment = NULL THEN block(onboarding) |
| POL-007-R02 | Vendor risk classification: Critical (oracle/bridge/RPC), High (cloud/audit), Medium (tooling), Low (non-technical). | classify(vendor) |
| POL-007-R03 | Critical vendor re-assessment annually. High vendor re-assessment every 18 months. | IF assessment_age > threshold THEN flag(overdue) |
| POL-007-R04 | Vendor incidents reported to CISO within 24 hours. | IF vendor_incident THEN notify(CISO, 24h) |
| POL-007-R05 | Exit strategy documented for all Critical vendors. | IF vendor.critical AND exit_plan = NULL THEN flag(gap) |
| POL-007-R06 | For engagements involving exchange integrations or custodial flows: deposit address screening against known-malicious address databases (Chainalysis, TRM Labs, or equivalent) required before go-live. | IF custodial_integration AND address_screening = NULL THEN block(go_live) |
| POL-007-R07 | Ongoing AML transaction monitoring required for all live custodial and exchange-integrated engagements: automated screening of transaction flows for structuring, layering, and known-illicit address patterns. Monthly review results logged in REG-501. | IF custodial_live AND aml_monitoring = NULL THEN flag(P1) notify(CISO) |
| POL-007-R08 | Wallet tooling integrity verification: all hardware wallets and signing tool updates must be verified against official manufacturer checksums before deployment or use. Counterfeit or unverified devices are prohibited. | IF tooling_source != official_channel OR checksum_unverified THEN block(signing_authority) |

## Dependencies

- **Explicit**: [S-115](../l1-standards/s-115-vendor-security-assessment.md)
