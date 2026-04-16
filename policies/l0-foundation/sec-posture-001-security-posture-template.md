---
id: "SEC-POSTURE-001"
title: "Security Posture Template"
type: "Template"
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

# SEC-POSTURE-001 — Security Posture Template

Security Posture Document Template

# 0. Document Control

Attribute

Value

Document ID

SEC-POSTURE-001

Title

Security Posture Document Template

Hierarchy Level

L5 - Template

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

CISO / vCISO

Approver

Node Owner

Classification

Confidential - Internal

Supersedes

—

References

CL-PHASE-001; GRC-MASTER-001; MAP-001; POL-002 ISMS Policy

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

SEC-POSTURE-001 is the template for Protofire\&apos;s Security Posture Document, a client-facing summary of security capabilities, controls, certifications, and engagement-specific security measures. It is produced per CL-PHASE-001 Phase 2 (proposal) and updated at engagement close (Phase 10). The vCISO co-authors and co-signs this document.

# 2. When to Use

RFP/proposal responses requiring security documentation

Client due diligence and vendor security assessments

Track B engagements (mandatory per CL-PHASE-001)

Annual refresh for ongoing client relationships

Insurance applications and renewal submissions

# 3. Template Sections

## 3.1 Executive Summary

[TEMPLATE] Protofire DAO LLC maintains a comprehensive security programme aligned with ISO 27001:2022, NIST CSF 2.0, and SOC 2 Trust Services Criteria. Our security posture is governed by [X] policies, [Y] standards, and [Z] procedures, with continuous monitoring and quarterly executive review. Current GRC maturity: ML-[N] per L0-6 assessment.

## 3.2 Organisational Security

[TEMPLATE] Dedicated CISO/vCISO with [X] years experience in blockchain/DeFi security

[TEMPLATE] GRC team of [N] personnel with defined RACI (RACI-001)

[TEMPLATE] Security governance via L0-3 GRC Charter with Node Owner oversight

[TEMPLATE] Annual security budget of [USD amount] covering tooling, training, and external audits

## 3.3 Technical Controls Summary

Control Domain

Implementation Summary

Access Control

RBAC + MFA enforced; quarterly access reviews (STD-101, REG-508)

Encryption

AES-256 at rest, TLS 1.3 in transit; HSM for mainnet keys (STD-104)

Secure Development

SAST, SCA, fuzz testing mandatory; 2-reviewer code review (STD-103)

Logging &amp; Monitoring

Centralised SIEM; on-chain monitoring; 12-month retention (STD-102)

Incident Response

15-min ack SLA; documented IR procedure; annual tabletop (PR-203)

Business Continuity

RTO 4h / RPO 1h; annual BCP/DR drill (PLAN-702/703)

Vendor Management

Risk-scored vendor register; annual reassessment (POL-007, REG-502)

Training

Mandatory security awareness; role-specific training; tracked (REG-507)

## 3.4 Engagement-Specific Security

[TEMPLATE - customise per engagement]

Aspect

Detail

Threat Model

[Reference engagement threat model document]

Key Management

[Multi-sig config: X-of-Y; hardware wallets; handover plan]

Deployment Controls

[Two-person rule; testnet validation; monitoring config]

Audit Coverage

[Internal audit complete / External audit by [firm] on [date]]

Residual Risks

[List accepted risks per POL-009 with mitigation]

## 3.5 Compliance &amp; Certifications

Framework

Status

Evidence

ISO 27001:2022

Aligned (certification planned Q1 2027)

MAP-001 control mapping

SOC 2 Type II

Readiness assessment Q4 2026

MAP-001; internal audit reports

GDPR

Compliant

POL-011; DPA-001; ROPA

NIST CSF 2.0

Aligned

MAP-001 mapping; maturity assessment

OWASP Top 10

Addressed in SDLC

STD-103; SAST/fuzz reports

## 3.6 Incident History (Last 12 Months)

[TEMPLATE] Summary of security incidents and their resolution, redacted to protect confidentiality. Reference REG-509 for full details (available under NDA/audit clause).

#

Severity

Summary

Resolution

[N/A or count]

[P1-P4]

[Brief description or &quot;No reportable incidents&quot;]

[Resolution summary]

## 3.7 Continuous Improvement

[TEMPLATE] Current maturity: ML-[N]; target: ML-[N+1] by [date]

[TEMPLATE] Active improvement plan: PLAN-701 with [X] initiatives

[TEMPLATE] Next external assessment: [type] scheduled [date]

# 4. Document Control

Version: updated per engagement or annually, whichever is sooner

Approval: CISO/vCISO co-sign required before external distribution

Classification: Confidential - Client; distribute only under NDA or MSA confidentiality clause

Retention: per POL-008; archived copies linked to engagement in REG-505

# Review &amp; Maintenance

Reviewed on a Annual cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

CL-PHASE-001 Client Engagement Lifecycle

MAP-001 Control Mapping Matrix

GRC-MASTER-001 Enterprise GRC Framework

All referenced POL, STD, PLAN documents
