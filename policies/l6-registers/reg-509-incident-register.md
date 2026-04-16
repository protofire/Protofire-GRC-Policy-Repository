---
id: "REG-509"
title: "Incident Register"
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

# REG-509 — Incident Register

Incident Register

# 0. Document Control

Attribute

Value

Document ID

REG-509

Title

Incident Register

Hierarchy Level

L6 — Register

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Continuous (per incident) + Quarterly trend review

Owner

CISO / Incident Response Lead

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

L2-INC-201 Incident Response Procedure; PR-208 Breach Notification Procedure; POL-010 Monitoring &amp; Continuous Assurance; ISO 27001:2022 A.5.24–A.5.27; NIST CSF 2.0 RS/RC; SOC 2 CC7.3–CC7.5

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-509 is the authoritative chronological record of every declared security or privacy incident, near-miss treated as incident, and post-incident review. It is the primary input to trend analysis (POL-010), breach-notification audit trail (PR-208, GDPR Art.33/34), and the Internal Audit Programme (IAP-001) non-conformance workflow.

# 2. Scope

In scope: every confirmed security incident, confirmed privacy breach, near-miss reclassified as incident, vulnerability-exploitation attempt with material impact, and tabletop exercises (logged for traceability, flagged &quot;EXERCISE&quot;). Out of scope: purely operational outages without security impact (handled in ops incident log separately).

# 3. Register Schema

Field

Description / Domain

Incident_ID

Format INC-{YYYY}-{NNNN}

Severity

SEV-1 | SEV-2 | SEV-3 | SEV-4 — per L2-INC-201 §4

Category

Confidentiality | Integrity | Availability | Privacy | Supply-chain | Insider | Web3-specific

Detection_Source

SIEM alert | Monitoring | User report | External notification | Audit finding

Detection_Time / Declaration_Time / Containment_Time / Resolution_Time

ISO-8601 UTC

Commander / Scribe

Named IRT members

Affected_Assets

Asset_IDs from REG-503

Affected_Subjects_Count

For privacy incidents

Lawful_Basis_Impact

For privacy incidents (POL-011)

External_Notifications

Regulator | Data subjects | Clients | Partners — with dates

Root_Cause

Assigned after PIR

Corrective_Actions

Links to change tickets (REG-504) and remediation in REG-511

Post_Incident_Review_Date

Scheduled + completed

Linked_Risks

REG-501 Risk_IDs

# 4. Roles &amp; Responsibilities

Role

Responsibility

CISO

Accountable for incident register integrity.

Incident Response Lead

Responsible for per-incident record and PIR scheduling.

DPO

Consulted / Informed for all privacy-impacting incidents; co-drives PR-208.

Legal / Commercial

Consulted on notification obligations and client-contract triggers.

Internal Audit

Reviews trend analysis quarterly; samples PIRs for completeness.

Node Owner

Informed on SEV-1; approves public notifications on SEV-1 if customer-facing.

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.5.24 Incident planning; A.5.25 Assessment &amp; decision; A.5.26 Response; A.5.27 Learning

NIST CSF 2.0

RS.AN, RS.MI, RS.RP, RS.CO; RC.RP, RC.IM, RC.CO

SOC 2

CC7.3 Evaluate security events; CC7.4 Respond; CC7.5 Recovery

GDPR

Art.33 Notification of data breach to supervisory authority; Art.34 Communication to data subject

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Mean Time to Detect (MTTD) — SEV-1/2

&lt; 1 h

1–4 h Amber / &gt;4 h Red

Mean Time to Contain (MTTC) — SEV-1

&lt; 4 h

4–24 h Amber / &gt;24 h Red

Supervisory Authority notification within 72 h (reportable events)

100%

Any miss = Red

PIR completion within 14 days of resolution

100%

90% Amber / &lt;90% Red

Repeat root-cause incidents / quarter

0

1 Amber / 3 Red

# 7. Evidence &amp; Recordkeeping

Incident timeline per record (immutable append-only log)

Commander / Scribe notes and decision log

Post-Incident Review minutes with corrective-action tickets

External-notification correspondence (regulator / client / data-subject)

Forensic artefacts preserved per evidence-handling procedure

# 8. Exceptions

Any exception to the mandatory fields or review cadence of this register requires POL-009 classification E2+ with CISO co-sign. HS-01/HS-02 hard stops are non-exceptable.

# Review &amp; Maintenance

Reviewed on a Continuous (per incident) + Quarterly trend review cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

L2-INC-201 Incident Response Procedure

PR-208 Breach Notification Procedure

POL-010 Monitoring &amp; Continuous Assurance Policy

REG-501 Enterprise Risk Register

REG-504 Change &amp; Release Register

REG-510 DPIA Register

PLAN-701 Tabletop IR Exercise Plan
