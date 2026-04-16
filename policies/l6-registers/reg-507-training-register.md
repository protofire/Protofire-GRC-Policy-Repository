---
id: "REG-507"
title: "Training and Awareness Register"
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

# REG-507 — Training and Awareness Register

Training &amp; Awareness Register

# 0. Document Control

Attribute

Value

Document ID

REG-507

Title

Training &amp; Awareness Register

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

CISO / People Operations

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

ISO 27001:2022 A.6.3 Information security awareness, education &amp; training; A.6.4 Disciplinary process; NIST CSF 2.0 PR.AT; SOC 2 CC1.4

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-507 is the authoritative record of security-awareness training, role-based training, phishing-simulation results and completion status for every employee and contractor with access to Protofire or client data. It is the evidence base for ISO 27001 A.6.3 and SOC 2 CC1.4 audit testing.

# 2. Scope

In scope: all employees, contractors, interns, board members and privileged third parties. Tracks: mandatory onboarding security training, annual refresher, role-based training (developers, operators, DPO, finance, AMs), and phishing-simulation participation. Out of scope: unrelated professional-development training.

# 3. Register Schema

Field

Description / Domain

Record_ID

Format TR-{YYYY}-{NNNNN}

Subject

Individual name + role + employment status

Training_Type

Onboarding | Annual-Refresher | Role-Based | Incident-Driven | Phishing-Simulation

Course_Title / Vendor

Course identifier

Required_By_Role

Yes/No (from training matrix)

Assigned_Date / Due_Date

ISO dates

Completion_Date

ISO date or NULL

Score / Outcome

% pass | click / report for phishing

Evidence

Link to LMS certificate / record

Next_Required_By

Per policy cadence

# 4. Roles &amp; Responsibilities

Role

Responsibility

CISO

Accountable for awareness programme effectiveness.

People Operations

Responsible for LMS administration and onboarding enrolment.

Line Manager

Responsible for ensuring team completion within SLA.

All Personnel

Responsible for completing assigned training on time.

Internal Audit

Reconciles against HR active-employee list each quarter.

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.6.3 Awareness, education &amp; training; A.6.4 Disciplinary process

NIST CSF 2.0

PR.AT-01..05

SOC 2

CC1.4 Commitment to competence; CC2.2 Internal communication

GDPR

Art.32(4) staff awareness

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Onboarding training completed within 30 days of start

100%

98% Amber / 95% Red

Annual refresher completion across workforce

≥ 95%

90–95% Amber / &lt;90% Red

Role-based training completion (Dev/Ops/Finance/AM)

100%

95% Amber / 90% Red

Phishing-simulation click rate

&lt; 5%

5–10% Amber / &gt;10% Red

Phishing-simulation report rate (reported as suspicious)

&gt; 40%

30–40% Amber / &lt;30% Red

# 7. Evidence &amp; Recordkeeping

LMS completion certificates

Phishing-simulation campaign reports with per-user outcomes

Role-based training matrix (maintained in GRC repo)

Quarterly completion reconciliation with HR active list

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

L1-HR-010 Personnel Security Standard

POL-001 Project Governance Policy

POL-002 Information Security Policy

CL-PHASE-001 Lifecycle Checklist

REG-511 Document Registry
