---
id: "REG-503"
title: "Asset Register / CMDB"
type: "Register"
level: "L6"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "CISO advisory"
classification: "Confidential — Internal"
last_change: "2026-04-16"
last_approval: "Pending"
source: "reference_policies (DOCX conversion)"
---

# REG-503 — Asset Register / CMDB

Asset Register (CMDB)

# 0. Document Control

Attribute

Value

Document ID

REG-503

Title

Asset Register (CMDB)

Hierarchy Level

L6 — Register

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Quarterly

Owner

CISO / IT Operations

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

ISO 27001:2022 A.5.9 Inventory of information &amp; other associated assets; A.5.10 Acceptable use; A.8.10 Information deletion; NIST CSF 2.0 ID.AM

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-503 is the authoritative inventory of information assets, physical assets, software assets, SaaS tenancies, code repositories, key material and data stores owned or used by Protofire. It is the foundation for access control (POL-004), vulnerability management, change management (POL-005), incident response (L2-INC-201) and data-classification (S-109) decisions.

# 2. Scope

In scope: all assets holding or processing Protofire or client data (production and non-production); all identity and credential stores; all code repositories; all SaaS tenancies; all secrets vaults and HSMs; all endpoints used for privileged access. Out of scope: personal devices under a BYOD policy that never access Protofire data (subject to L1-HR-010 controls).

# 3. Register Schema

Field

Description / Domain

Asset_ID

Format A-{TYPE}-{NNN}; immutable

Type

Info-Asset | SaaS | Server | Endpoint | Network | Repo | Key | HSM | Container | Database | Queue | BucketNode

Name

Human-readable identifier

Owner / Custodian

Named individual (role on contract)

Classification

Public | Internal | Confidential | Restricted — per S-109

Location / Region

Region, provider tenant, rack/zone where applicable

Criticality

Tier-1 | Tier-2 | Tier-3 — per BIA in L1-BC-008 / L1-BCM-012

Data_Categories

Personal | Special-category | Financial | Code | Secrets | Operational | None

Environment

Prod | Staging | Dev | Test | Archive

Dependencies

Upstream / downstream asset IDs

Created / Decommissioned

ISO dates

Review_Cycle

Quarterly (Tier-1), Semi-annual (Tier-2), Annual (Tier-3)

# 4. Roles &amp; Responsibilities

Role

Responsibility

CISO

Accountable for register completeness.

IT Operations

Responsible for day-to-day maintenance and automated discovery feeds.

Asset Owner

Named individual for each Tier-1/Tier-2 asset; responsible for classification accuracy.

Security Operations

Consulted on criticality and dependency entries.

Internal Audit

Reconciles register against procurement, cloud billing and identity-provider inventories at least annually.

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.5.9 Inventory; A.5.10 Acceptable use; A.5.12 Classification; A.5.13 Labelling; A.8.10 Information deletion

NIST CSF 2.0

ID.AM-01..08 Asset Management; PR.DS-03 Data-at-rest protection

SOC 2

CC6.1 Logical &amp; physical access; CC3.2 Risk identification

CIS Controls v8

CIS-1 Inventory &amp; control of enterprise assets; CIS-2 Inventory of software assets

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Tier-1 assets with complete metadata

100%

95% Amber / 90% Red

Register reconciliation gap vs. cloud billing (count diff)

0

1–3 Amber / &gt;3 Red

Assets without named Owner

0

1 Amber / 5 Red

Tier-1 review within 90 days

100%

95% Amber / 90% Red

# 7. Evidence &amp; Recordkeeping

Automated discovery feed logs (cloud provider inventory APIs, IdP exports)

Quarterly reconciliation minutes

Decommissioning records with data-deletion attestation per asset

Asset-owner attestations at annual review

# 8. Exceptions

Any exception to the mandatory fields or review cadence of this register requires POL-009 classification E2+ with CISO co-sign. HS-01/HS-02 hard stops are non-exceptable.

# Review &amp; Maintenance

Reviewed on a Quarterly cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

# Version History

Version

Date

Author

Change Summary

v1.0

2026-04-15

Owner (per Document Control)

Initial audit-ready publication — gap-fill per Drive Housekeeping Plan.

# Appendix — Cross-References

POL-004 Access Control &amp; SoD Policy

POL-005 Change Management Policy

S-109 Data Classification Standard

L1-BC-008 Business Continuity Standard (BIA source)

REG-513 Node Configuration Register (subset for Web3 nodes)
