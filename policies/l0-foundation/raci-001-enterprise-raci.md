---
id: "RACI-001"
title: "Enterprise RACI Matrix"
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

# RACI-001 — Enterprise RACI Matrix

# Enterprise RACI (Roles, Accountability, Consult, Inform)

Field

Value

Document ID

RACI-001

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

CISO + CEO

Approver

Board

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

RACI-001 is the enterprise-level RACI that assigns named accountability across every phase, gate, and standing activity of the Protofire GRC lifecycle. It complements project-level RACI instances (e.g. the DApp/DeFi RACI spreadsheet) by establishing the upstream defaults. Where a project RACI is silent, this document governs.

# 2. Legend

R — Responsible: performs the work.

A — Accountable: single point of sign-off; cannot be delegated; co-sign indicated explicitly (e.g. Gate G4-A and G7-IRR require both vCISO and NO).

C — Consulted: two-way communication; provides input before sign-off.

I — Informed: one-way notification after the fact.

(2PR) — Two-person rule applies: TL and DevOps Deployer cannot be the same individual.

# 3. Roles (abbreviations)

Board / CEO — approves risk appetite and T3/T4 decisions.

vCISO / CISO / DPO — security strategy, G4-A and G7-IRR mandatory co-signer, GDPR DPO.

Node Owner (NO) — engagement-level sign-off, Hard Stop escalation.

CFO — financial feasibility, T2+ MSA co-sign, cold-wallet reconciliation.

PM — delivery and RACI population on the engagement.

TL — technical architecture, threat modelling, internal audit.

DevOps — infrastructure, CI/CD, deployments, monitoring.

QA — independent test execution, internal code-quality audit.

AM — pre-sales, client risk scoring, project brief.

FIN — billing, arrears monitoring (HS-05).

Legal — MSA review, DPA, regulatory notifications.

# 4. RACI matrix

Phase / Gate / Activity

Board / CEO

vCISO / CISO / DPO

Node Owner

CFO

PM

TL

DevOps

QA

AM

FIN

Legal

P1 Intake &amp; C/B/P scoring

I

C

A

C

I

I

I

I

R

I

C

G1-A Gate sign-off

I

C

A

I

I

I

I

I

R

I

C

P2 Proposal (security sections)

I

C

A

I

I

C

I

I

R

I

C

P3 MSA execution

I

C

A

C

I

I

I

I

R

I

R

G2-A Gate sign-off

I

C

A

C (T2+)

I

I

I

I

R

I

C

P3-FIN Billing setup

I

I

A

C

I

I

I

I

I

R

I

P4 Kickoff + PSF

I

C

A

R

C

C

I

I

I

I

I

G3-A Gate sign-off

I

C

A

R

I

I

I

I

I

I

I

P5 Threat modelling

I

A

C

I

R

R

C

C

I

I

I

G4-A Gate (MANDATORY vCISO)

I

A (vCISO)

A (NO)

I

C

C

I

C

I

I

I

P6–P7 Build, QA, demo

I

C

A

I

R (PM)

R

C

R

I

I

I

G5-A Code review + tests

I

C

A

I

C

R

C

A

I

I

I

P8 Testnet deploy

I

C

A

I

C

R

R

R

I

I

I

G6-A Pre-prod sign-off

I

C

A

I

C

A

C

R

I

I

I

P9 Mainnet deploy (Irrev.)

I

A (vCISO)

A (NO)

C (T2+)

C

A (2PR)

A (2PR)

R

I

I

I

G7-IRR Irreversibility Gate

I

A (vCISO)

A (NO)

I

C

C

C

C

I

I

C

P10–P11 Ops &amp; upgrades

I

C

A

I

C

R

R

R

I

I

I

G8-A Ops sign-off

I

C

A

I

C

C

C

C

I

I

I

P12 Close-out

I

C

A

C

R

C

C

C

C

C

I

Incident SEV-1 (declare + pause)

I

A

R

I

C

R

R

C

I

I

C

Incident SEV-1 regulator notify (GDPR 72h)

I

A (DPO)

C

I

I

I

I

I

I

I

R

Risk appetite change

A

R

C

C

I

I

I

I

I

I

C

Hard Stop escalation (HS-01–07)

A

R

R

C

C

I

I

I

I

C

C

Policy approval (L0/L1)

A

R

C

C

I

I

I

I

I

I

C

Internal audit finding &gt; High

I

A

R

C

I

I

I

I

I

I

C

# 5. Separation-of-Duty constraints

A single individual may not hold Accountable for both G4-A (security review) and G7-IRR (irreversibility) on the same engagement — vCISO co-signs both, NO may co-sign both only if a different deputy handles the technical sign-off.

DevOps Deployer ≠ TL Reviewer at deployment (two-person rule, per the 20 mandatory controls, two-person rule row).

QA auditor ≠ code author (independence per L3-TEST-204).

CISO auditing own controls is prohibited — use vCISO or external assessor.

Node Owner cannot approve their own Hard Stop override; escalation goes to CEO.

# 6. Maintenance

This RACI is reviewed annually by the GRC Committee and whenever a material role change occurs (leadership hire, SoD violation, role split). Changes are recorded in REG-511 with the ID of the approving Gate decision (typically GRC Committee minute).

# 7. Related documents

L0-2 GRC Programme Governance Charter

POL-001 Project Governance Policy

POL-004 Access Control and Segregation of Duties

Control Catalogue — sod-matrix

definitions/roles.md

REG-513 Node Configuration Register (NEW)
