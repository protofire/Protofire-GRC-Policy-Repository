---
id: "REG-504"
title: "Change and Release Register"
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

# REG-504 — Change and Release Register

Change &amp; Release Register

# 0. Document Control

Attribute

Value

Document ID

REG-504

Title

Change &amp; Release Register

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

CISO / DevOps Lead

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

POL-005 Change Management Policy; ISO 27001:2022 A.8.32; NIST CSF 2.0 PR.IP-03; SOC 2 CC8.1

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-504 is the authoritative log of every classified change (C1–C5) across Protofire-operated systems and client engagements where Protofire is the deployer. It is the evidence base for POL-005 compliance, the two-person-rule attestation for Web3 deployments, and SOC 2 CC8.1 change-management audit testing.

# 2. Scope

In scope: every change to production systems, client production systems where Protofire deploys, smart-contract deployments, key-rotation events, IaC changes with production impact, SaaS admin-configuration changes affecting security posture, and emergency changes. Out of scope: non-production sandbox work, documentation-only changes classified C1.

# 3. Register Schema

Field

Description / Domain

Change_ID

Format CHG-{YYYY}-{NNNN}; immutable

Class

C1 (doc-only) | C2 (low) | C3 (standard) | C4 (major) | C5 (emergency) — per POL-005

Title

Short description

System / Asset

Asset_ID from REG-503

Requester / Implementer / Approver

Named individuals (must differ where POL-004 SoD applies)

Two-Person_Deployer

For mainnet / production deployments — Deployer + Verifier named

Risk_Assessment

Residual risk rating + link to threat-model update if applicable

Test_Evidence

Link to QA sign-off / automated test result / staging verification

Rollback_Plan

Documented; verified if C4/C5

CAB_Decision

Approved | Rejected | Deferred — with timestamp

Deployment_Window

Planned + actual start/end

Post-Change_Verification

Pass | Fail + link to evidence

Related_Incident

If change caused or fixed an incident

# 4. Roles &amp; Responsibilities

Role

Responsibility

CISO

Accountable for register integrity and change governance.

DevOps Lead

Responsible for tooling integration (CI/CD, ticket system) and log completeness.

CAB (Change Advisory Board)

Decision authority for C4/C5 changes.

Implementer

Records each change; produces test evidence.

Internal Audit

Samples changes per quarter against CC8.1 testing plan.

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.8.32 Change management

NIST CSF 2.0

PR.IP-03 Configuration change control processes

SOC 2

CC8.1 Change management

Protofire

POL-005 C1–C5 classification; CL-411 Signing Ceremony for smart-contract changes

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Changes with complete test evidence

100%

97% Amber / 95% Red

Emergency changes (C5) as % of monthly total

&lt; 5%

5–10% Amber / &gt;10% Red

Failed change rollback &gt; 15 min

0

1 Amber / 3 Red

Two-person-rule attestation on smart-contract deploys

100%

Any miss = Red

CAB backlog &gt; 14 days

0

1 Amber / 3 Red

# 7. Evidence &amp; Recordkeeping

CI/CD pipeline records linked per change

CAB meeting minutes (weekly + emergency)

Signing-ceremony attestations (CL-411) for on-chain changes

Post-deployment verification screenshots / monitoring dashboards

Rollback evidence where invoked

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

POL-005 Change Management Policy

CL-411 Signing Ceremony Checklist

REG-503 Asset Register

REG-509 Incident Register

L2-CHANGE-205 Change Management Procedure
