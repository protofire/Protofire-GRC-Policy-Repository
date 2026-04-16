---
id: "REG-508"
title: "Access Review Register"
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

# REG-508 — Access Review Register

Access Review Register

# 0. Document Control

Attribute

Value

Document ID

REG-508

Title

Access Review Register

Hierarchy Level

L6 — Register

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Monthly (Tier-1 systems) / Quarterly (Tier-2) / Semi-annual (Tier-3)

Owner

CISO / IT Operations

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

POL-004 Access Control &amp; SoD Policy; ISO 27001:2022 A.5.15–A.5.18; NIST CSF 2.0 PR.AC; SOC 2 CC6.1–CC6.3

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-508 records every scheduled access-recertification exercise (quarterly / semi-annual / annual as applicable per asset tier), privileged-access reviews, joiner/mover/leaver reconciliations, and exception approvals. Primary evidence for SOC 2 CC6.1-CC6.3 testing and ISO 27001 A.5.18.

# 2. Scope

In scope: all production systems, privileged identities, break-glass accounts, shared accounts, service accounts, code-repository admin rights, SaaS admin panels, cloud-console access, key-management accesses. Out of scope: end-user access to self-service tools (covered by automated de-provisioning).

# 3. Register Schema

Field

Description / Domain

Review_ID

Format AR-{YYYY-Q}-{SYSTEM}-{NNN}

System / Asset

Asset_ID from REG-503

Review_Cycle

Monthly | Quarterly | Semi-annual | Annual

Scope

All users | Privileged only | Break-glass | Service accounts

Reviewer

Named system owner

Reviewer_Attestation_Date

ISO date

Users_In_Scope

Count

Users_Revoked

Count

Users_Retained_With_Justification

Count

Exceptions

Links to REG-506 entries

Evidence

Link to IdP export + attestation signature

Next_Review_Due

Per cadence

# 4. Roles &amp; Responsibilities

Role

Responsibility

CISO

Accountable for recertification programme.

IT Operations

Responsible for preparing IdP exports and tracking completion.

System Owner

Responsible for performing the review and recording the attestation.

Internal Audit

Samples reviews per quarter against CC6 testing plan.

Joiner/Mover/Leaver (JML)

Triggered events feed into this register (see L2-ACCESS-203).

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.5.15 Access control; A.5.16 Identity management; A.5.17 Authentication information; A.5.18 Access rights

NIST CSF 2.0

PR.AC-01..07 Identity Management &amp; Access Control

SOC 2

CC6.1 Logical access security; CC6.2 Before issuing credentials; CC6.3 Authorise, modify, revoke

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Reviews completed on schedule

100%

95% Amber / 90% Red

Privileged accounts reviewed monthly

100%

Any miss = Red

Dormant accounts (&gt; 90 days no login) still active

0

1–3 Amber / &gt;3 Red

Leaver offboarding complete within 24 h

100%

98% Amber / 95% Red

Break-glass account usage without incident ticket

0

Any occurrence = Red

# 7. Evidence &amp; Recordkeeping

IdP export per review with reviewer signature

Revocation tickets generated from review outcomes

JML (Joiner/Mover/Leaver) offboarding attestations

Break-glass-account activity logs with incident-ticket linkage

# 8. Exceptions

Any exception to the mandatory fields or review cadence of this register requires POL-009 classification E2+ with CISO co-sign. HS-01/HS-02 hard stops are non-exceptable.

# Review &amp; Maintenance

Reviewed on a Monthly (Tier-1 systems) / Quarterly (Tier-2) / Semi-annual (Tier-3) cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

L2-ACCESS-203 Access Management Procedure

REG-503 Asset Register

REG-506 Exception &amp; Waiver Register

REG-509 Incident Register
