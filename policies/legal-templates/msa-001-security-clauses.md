---
id: "MSA-001"
title: "Master Service Agreement Security Clauses Template"
type: "Legal Template"
level: "L2"
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

# MSA-001 — Master Service Agreement Security Clauses Template

MSA Security Clauses Template

# 0. Document Control

Attribute

Value

Document ID

MSA-001

Title

MSA Security Clauses Template

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

CISO / Account Manager

Approver

Node Owner / CLO

Classification

Confidential - Internal

Supersedes

—

References

CL-PHASE-001 Phase 2-3; POL-002 ISMS Policy; POL-007 Vendor &amp; Third-Party Risk; LEGAL-02 MSA review step; ISO 27001:2022 A.5.20

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

MSA-001 provides the mandatory security clauses that must be incorporated into every Master Service Agreement (MSA) or equivalent client contract. These clauses ensure Protofire\&apos;s security obligations are contractually defined, auditable, and aligned with the GRC framework. Per CL-PHASE-001 Phase 3, no MSA may be executed without LEGAL-02 review confirming inclusion of all mandatory clauses.

# 2. Applicability

All new client MSAs, SOWs, and engagement letters

Renewals and amendments of existing agreements

Sub-processor agreements where Protofire acts as data controller or processor

Track A (standard) and Track B (high-risk) engagements per CL-PHASE-001

# 3. Mandatory Security Clauses

## 3.1 Information Security Obligations

[CLAUSE MSA-SEC-01] Provider (Protofire) shall implement and maintain an information security management system aligned with ISO 27001:2022 and shall comply with its published security policies, including but not limited to POL-002 (Information Security), POL-003 (Access Control), and POL-004 (Secure SDLC). Provider shall notify Client within [72/48/24] hours of any Security Incident affecting Client Data.

## 3.2 Data Protection

[CLAUSE MSA-SEC-02] Provider shall process Client Data only as instructed by Client and in accordance with the Data Processing Agreement (DPA-001). Provider shall implement encryption at rest (AES-256 minimum) and in transit (TLS 1.2+) for all Client Data. Provider shall not transfer Client Data to sub-processors without prior written consent.

## 3.3 Access Control

[CLAUSE MSA-SEC-03] Provider shall implement role-based access control (RBAC) ensuring least-privilege access to Client systems, code repositories, and data. Multi-factor authentication (MFA) shall be required for all personnel accessing Client environments. Access shall be reviewed quarterly and revoked within 24 hours of personnel role change or departure.

## 3.4 Secure Development

[CLAUSE MSA-SEC-04] All smart contracts and code delivered under this Agreement shall be developed in accordance with Provider\&apos;s Secure Development Standard (STD-103), including: static analysis (zero Critical/High findings), dependency scanning, fuzz testing (minimum 10,000 runs per critical function), and independent code review by minimum 2 reviewers. All mainnet deployments require Provider\&apos;s Technical Lead sign-off.

## 3.5 Audit Rights

[CLAUSE MSA-SEC-05] Client shall have the right to audit Provider\&apos;s security controls relevant to the engagement, with [30] days prior written notice, not more than [once/twice] per calendar year. Provider shall make available security documentation, audit reports, and relevant personnel. Provider shall remediate Critical and High findings within [30] days of audit report delivery.

## 3.6 Incident Response

[CLAUSE MSA-SEC-06] Provider shall maintain an incident response capability per PR-203, including: 15-minute acknowledgement SLA for Critical severity, 4-hour containment for confirmed breaches. Provider shall preserve forensic evidence for minimum 12 months. Provider shall cooperate with Client\&apos;s incident investigation and provide a root-cause analysis within [10] business days.

## 3.7 Key Management

[CLAUSE MSA-SEC-07] All cryptographic keys used in Client engagements shall be managed per STD-104. Mainnet signing keys shall be stored in hardware wallets or HSM. Multi-signature configurations shall meet minimum thresholds defined in the engagement security posture document. Key handover procedure at engagement close shall be documented and executed per CL-PHASE-001 Phase 10-11.

## 3.8 Business Continuity

[CLAUSE MSA-SEC-08] Provider shall maintain a Business Continuity Plan (PLAN-702) and Disaster Recovery Plan (PLAN-703). Provider shall achieve the following minimum recovery objectives for Client-related services: RTO [4 hours], RPO [1 hour]. Provider shall conduct annual BCP/DR testing and provide Client with test summary upon request.

## 3.9 Personnel Security

[CLAUSE MSA-SEC-09] All Provider personnel assigned to Client engagement shall complete security awareness training within 30 days of assignment and annually thereafter. Provider shall conduct background checks where legally permitted. Provider shall enforce acceptable use policies per L1-HR-010.

## 3.10 Termination &amp; Data Return

[CLAUSE MSA-SEC-10] Upon termination or expiration, Provider shall: (a) return or securely destroy all Client Data within [30] days, (b) execute key handover per STD-104 section 5.4, (c) revoke all Provider personnel access to Client systems within 24 hours, (d) provide written certification of data destruction. Surviving obligations: confidentiality, data protection, and audit rights shall survive for [3] years.

# 4. Track B Additional Clauses

For engagements classified as Track B (high-risk) per CL-PHASE-001, the following additional clauses are mandatory:

[MSA-SEC-11] External security audit by independent firm before mainnet deployment

[MSA-SEC-12] Client written acknowledgement of residual risks per POL-009

[MSA-SEC-13] Enhanced monitoring SLA: 24/7 on-chain monitoring for minimum 90 days post-deployment

[MSA-SEC-14] Insurance: Provider shall maintain professional liability insurance of not less than [USD amount] per occurrence

# 5. Negotiation Guidance

Clause

Non-Negotiable Elements

Negotiable Parameters

MSA-SEC-01

ISMS requirement; incident notification

Notification timeframe: 24-72 h

MSA-SEC-02

Encryption standards; sub-processor consent

Transfer mechanism specifics

MSA-SEC-03

MFA; quarterly review; 24h revocation

Specific RBAC implementation

MSA-SEC-04

SAST zero Critical/High; 2 reviewers

Fuzz run count (min 5,000)

MSA-SEC-05

Audit right existence

Frequency; notice period; scope limits

MSA-SEC-06

15-min ack; evidence preservation

Containment SLA; RCA timeline

MSA-SEC-07

Hardware wallet for mainnet; handover

Multi-sig threshold specifics

MSA-SEC-08

BCP/DR existence; annual testing

Specific RTO/RPO values

MSA-SEC-09

Training; acceptable use

Background check scope

MSA-SEC-10

Data return/destroy; access revocation

Timeline: 14-60 days; survival period

# 6. Integration with Engagement Lifecycle

Phase 2 (AM): Include all mandatory clauses in proposal security section

Phase 3 (AM/CLO): LEGAL-02 review confirms all clauses present; negotiate parameters

Gate G2: MSA with security clauses fully executed is a prerequisite

Phase 10-11: Execute termination clauses (MSA-SEC-10)

REG-511: Log MSA execution with clause version reference

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

DPA-001 Data Processing Agreement Template

POL-002 ISMS Policy

STD-103 Secure Development Standard

STD-104 Cryptographic Controls Standard
