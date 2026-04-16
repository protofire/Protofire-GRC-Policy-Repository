---
id: "RACI-002"
title: "Track B RACI Matrix"
type: "RACI"
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

# RACI-002 — Track B RACI Matrix

Track B Engagement RACI Matrix

# 0. Document Control

Attribute

Value

Document ID

RACI-002

Title

Track B Engagement RACI Matrix

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

PM / GRC Manager

Approver

CISO / Node Owner

Classification

Confidential - Internal

Supersedes

—

References

RACI-001 Standard RACI; CL-PHASE-001; POL-009 Exception Management

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

RACI-002 extends RACI-001 (standard engagement RACI) with additional accountability assignments required for Track B (high-risk) engagements. Track B engagements involve elevated risk factors such as: DeFi protocol with TVL &gt; $10M, upgradeability patterns, novel cryptographic mechanisms, cross-chain bridges, or regulatory-sensitive jurisdictions.

# 2. Scope

Applies to all engagements classified as Track B per CL-PHASE-001 risk scoring. RACI-002 supplements (does not replace) RACI-001. Where RACI-002 specifies a different assignment than RACI-001, RACI-002 takes precedence for Track B engagements.

# 3. Track B Classification Criteria

Criterion

Threshold

TVL (Total Value Locked)

&gt; $10M equivalent at deployment or within 90-day forecast

Upgradeability

Proxy pattern with admin key control over user funds

Cross-chain

Bridge or cross-chain messaging with value transfer

Novel crypto

Custom cryptographic primitives; zero-knowledge circuits

Regulatory exposure

MiCA-regulated, SEC-scrutinised, or OFAC-adjacent jurisdiction

Client risk score

C/B/P composite score &gt;= 7 (per CL-PHASE-001 scoring)

# 4. RACI Matrix - Track B Activities

R = Responsible (does the work), A = Accountable (owns the outcome), C = Consulted, I = Informed. Roles: NO = Node Owner, CISO = CISO/vCISO, TL = Technical Lead, PM = Project Manager, AM = Account Manager, QA = QA Engineer, DevOps = DevOps Engineer, FIN = Finance.

Activity

NO

CISO

TL

PM

AM

QA

DevOps

FIN

Track B classification decision

A

R

C

C

R

I

I

I

Enhanced threat model (4 categories)

I

A

R

C

I

C

C

--

External audit firm selection

A

R

C

I

C

--

--

C

External audit management

I

A

C

R

I

--

--

C

Client risk acknowledgement

I

C

I

R

A

--

--

--

Enhanced monitoring config (24/7)

I

A

C

I

--

--

R

--

Economic simulation (DeFi)

I

C

R

C

I

A

--

--

Multi-sig ceremony

A

R

R

C

I

C

C

--

Formal key handover

A

R

R

C

C

--

C

--

Insurance verification

A

C

--

I

R

--

--

R

Track B gate review (G4 enhanced)

A

R

R

C

C

C

C

I

Post-deployment 90-day monitoring

I

A

C

R

I

--

R

--

Client security debrief (Phase 10)

I

R

C

R

A

--

--

--

Engagement close audit (Phase 12)

A

R

C

R

I

C

--

R

# 5. Additional Track B Requirements

## 5.1 Enhanced Gate G4 (Go/No-Go)

Standard G4 signatories: NO + CISO + TL (per RACI-001)

Track B additional: external audit report must be received and reviewed

Track B additional: client written risk acknowledgement must be on file

Track B additional: insurance coverage confirmed by FIN

## 5.2 Irreversibility Gate (Pre-Mainnet)

All RACI-001 Irreversibility Gate requirements apply

Track B additional: vCISO co-sign mandatory (cannot delegate)

Track B additional: economic simulation results reviewed and accepted by TL + CISO

Track B additional: 24/7 monitoring validated on testnet for minimum 72 hours

## 5.3 Post-Deployment Obligations

90-day enhanced monitoring period with weekly status reports to client

Monthly security review calls with client during monitoring period

Incident response SLA tightened: P1 acknowledgement within 10 minutes (vs. standard 15)

At 90-day mark: formal security handover document to client

# 6. Separation of Duties (SoD) - Track B Specific

SoD Requirement

Rationale

Code author != Code reviewer (standard)

Independence of review

TL (authoriser) != DevOps (deployer)

Two-person deployment rule

AM (risk scorer) != NO (gate signer)

Independence of risk assessment from approval

External auditor != Protofire personnel

Independence of external assurance

QA (tester) != TL (test approver) for Track B

Enhanced testing independence

FIN (insurance verifier) != AM (client relationship)

Independence of financial verification

# 7. Escalation Path

Any Track B engagement where a required RACI assignment cannot be filled (e.g., insufficient personnel for SoD) must be escalated to NO for resolution. Options: (a) staff the gap, (b) engage external resource, (c) reclassify to Track A with POL-009 E3 exception and CISO + NO co-sign. Track B cannot proceed through Gate G4 with unfilled RACI assignments.

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

RACI-001 Standard Engagement RACI

CL-PHASE-001 Client Engagement Lifecycle

POL-009 Exception Management Policy

MSA-001 Security Clauses Template
