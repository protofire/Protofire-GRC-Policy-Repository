---
id: "MAP-001"
title: "Control Mapping Matrix"
type: "Mapping"
level: "L0"
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

# MAP-001 — Control Mapping Matrix

Control Mapping Matrix

# 0. Document Control

Attribute

Value

Document ID

MAP-001

Title

Control Mapping Matrix

Hierarchy Level

L0 - Foundation

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Semi-annual

Owner

GRC Manager / CISO

Approver

Node Owner

Classification

Confidential - Internal

Supersedes

—

References

GRC-MASTER-001; ISO 27001:2022; NIST CSF 2.0; SOC 2 TSC; NIST SP 800-53 Rev.5; CIS Controls v8

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

MAP-001 provides a unified cross-reference between Protofire\&apos;s internal GRC controls (policies, standards, procedures) and external framework requirements. It serves three critical functions: (1) demonstrate compliance coverage during audits, (2) identify gaps where controls do not yet satisfy a framework requirement, (3) prevent duplicated effort by showing which internal control satisfies multiple framework requirements.

# 2. Scope

Covers the following frameworks mapped against Protofire internal controls:

ISO 27001:2022 - Annex A controls (93 controls across 4 themes)

NIST CSF 2.0 - 6 functions, 22 categories

SOC 2 Type II - Trust Services Criteria (CC, A, PI, P, C)

NIST SP 800-53 Rev.5 - selected control families

CIS Controls v8 - 18 control groups

# 3. Control Mapping

## 3.1 Governance &amp; Risk (GV)

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.5.1 Policies

GV.OC-01

CC1.1

POL-001 ISMS; GRC-MASTER-001

REG-511 approval records

A.5.2 Roles

GV.RR-01

CC1.3

RACI-001; L0-3 Charter

RACI matrix; org chart

A.5.3 SoD

GV.RR-02

CC1.3

CL-PHASE-001 SoD checks

Gate records; RACI-001

A.5.4 Mgmt resp.

GV.RR-01

CC1.2

L0-3 Charter section 4

NO approval records

A.5.5 Contact w/ auth

GV.OC-04

CC1.1

PR-203 section 6

Notification templates

A.5.6 Threat intel

ID.RA-02

CC3.2

STD-102 section 4

SIEM alerts; threat feeds

A.5.7 Project security

GV.RM-01

CC3.1

CL-PHASE-001 PSF

Gate G3 records

A.5.8 Asset mgmt

ID.AM-01

CC6.1

POL-005; REG-503

CMDB export

A.5.9-5.11 Acceptable use

PR.AA-06

CC6.1

L1-HR-010

Signed AUP records

## 3.2 Access Control (AC)

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.5.15 Access policy

PR.AA-01

CC6.1

POL-003; STD-101

Policy document; IAM config

A.5.16 Identity mgmt

PR.AA-01

CC6.2

STD-101 section 3

IdP configuration

A.5.17 Authentication

PR.AA-02

CC6.1

STD-101 section 4

MFA enforcement logs

A.5.18 Access rights

PR.AA-03

CC6.2

STD-101; REG-508

Quarterly review records

A.8.2 Privileged access

PR.AA-05

CC6.3

STD-101 section 5

PAM logs; JIT access records

A.8.3 Info access restrict

PR.AA-04

CC6.1

POL-003 section 4.3

RBAC matrix

A.8.5 Secure auth

PR.AA-02

CC6.1

STD-101 section 4

Password policy; MFA config

## 3.3 Cryptography &amp; Key Management

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.8.24 Cryptography

PR.DS-01

CC6.1

L1-KEY-005; STD-104

Crypto inventory; config

A.8.24 Key mgmt

PR.DS-01

CC6.7

STD-104 section 5

Key lifecycle records

--

PR.DS-02

CC6.7

STD-104 section 3 (TLS)

TLS scan reports

## 3.4 Development &amp; Change

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.8.25-8.26 Secure dev

PR.DS-01

CC8.1

POL-004; STD-103

SAST reports; review logs

A.8.28 Secure coding

PR.DS-01

CC8.1

STD-103 section 3

Code review records

A.8.29 Security testing

DE.CM-09

CC7.1

STD-103 section 4

Test reports; fuzz logs

A.8.31 Env separation

PR.DS-01

CC8.1

STD-103 section 5

Env config; access lists

A.8.32 Change mgmt

PR.DS-10

CC8.1

POL-005; REG-504

Change records; approvals

A.8.33 Test information

PR.DS-01

CC8.1

STD-103 section 4.2

Test data policy

## 3.5 Incident &amp; Continuity

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.5.24-5.28 Incident

RS.MA-01

CC7.3

PR-203; REG-509

Incident records; post-mortems

A.5.29 ICT continuity

RC.RP-01

A1.2

PLAN-702; PLAN-703

BCP/DR test records

A.5.30 ICT readiness

RC.RP-03

A1.2

PLAN-703 section 4

Backup verification logs

## 3.6 Monitoring &amp; Logging

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.8.15 Logging

DE.CM-01

CC7.2

STD-102 section 3

Log configuration; samples

A.8.16 Monitoring

DE.CM-06

CC7.2

STD-102 section 4

Alert rules; dashboards

A.8.17 Clock sync

DE.CM-01

CC7.2

STD-102 section 3.3

NTP config

## 3.7 Third-Party &amp; Vendor

ISO 27001:2022

NIST CSF 2.0

SOC 2

Protofire Control

Evidence

A.5.19-5.23 Supplier

GV.SC-01

CC9.2

POL-007; S-115; REG-502

Vendor assessments; register

A.5.20 Addressing security

GV.SC-07

CC9.2

MSA-001 clauses

Signed MSAs; DPAs

A.5.21 ICT supply chain

GV.SC-04

CC9.2

POL-007 section 4.5

SCA reports; SBOM

# 4. Gap Summary

The following gaps are identified as of the effective date and tracked for remediation in PLAN-701:

Gap ID

Description

Remediation Target

GAP-01

SOC 2 Type II audit not yet conducted

Q4 2026 - readiness assessment

GAP-02

Formal internal audit programme not yet established

Q3 2026 - first cycle

GAP-03

Physical security controls deferred (remote-first)

Accepted risk per POL-009

GAP-04

Automated vulnerability scanning not yet continuous

Q3 2026 - tool deployment

GAP-05

Business continuity tabletop exercise not yet conducted

Q2 2026 - first exercise

# Review &amp; Maintenance

Reviewed on a Semi-annual cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

GRC-MASTER-001 Enterprise GRC Framework

PLAN-701 Security Improvement Plan

All referenced POL, STD, PR, REG documents
