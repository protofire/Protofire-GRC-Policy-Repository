---
id: "S-109"
title: "Data Classification Standard"
type: "Standard"
level: "L2-STD"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-004; POL-011; ISO 27001 A.5.12-5.13"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# S-109 — Data Classification Standard

## Scope
Defines data classification tiers and maps each to access, encryption, retention, and handling requirements.

## Classification Tiers

| Tier | Label | Examples | Access | Encryption at Rest | Encryption in Transit | Retention |
|---|---|---|---|---|---|---|
| DC-1 | Public | Marketing material, blog posts | Unrestricted | Optional | HTTPS | Per content policy |
| DC-2 | Internal | Internal comms, process docs | Employees + authorized contractors | Recommended | HTTPS | 3 years |
| DC-3 | Confidential | Client data, source code, risk registers | Role-based + project-scoped | Required (AES-256) | TLS 1.2+ | 7 years (legal) / 365d (ops) |
| DC-4 | Restricted | Private keys, credentials, PII under GDPR | Named individuals + MFA + audit log | Required (AES-256 + HSM) | TLS 1.3 | Life of use + 5 years |

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| S109-R01 | All data assets classified at creation or ingestion. | IF data.classification = NULL THEN block(storage) |
| S109-R02 | Classification determines minimum access, encryption, and retention controls. | apply_controls(classification_tier) |
| S109-R03 | Reclassification requires data owner approval. Upgrade immediate; downgrade requires CISO. | IF downgrade THEN require(CISO_approval) |
| S109-R04 | DC-4 data: access logged, quarterly review, destruction certified. | IF dc4 THEN log(access); review(quarterly); certify(destruction) |
