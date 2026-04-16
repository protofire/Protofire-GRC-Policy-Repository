---
id: "REG-513"
title: "Node Configuration Register"
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

# REG-513 — Node Configuration Register

# Node Configuration Register

Field

Value

Document ID

REG-513

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

Node Owner + CISO (jointly)

Approver

CEO

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

The Node Configuration Register (NCR) is the single source of truth for every Protofire Node / SubDAO that holds operational authority over an engagement, a platform, or a treasury pool. It records the named Node Owner, delegation scope, active engagements, signing wallet configuration, and review history. The register is required by GAP-18 (NO + CISO) to satisfy ISO 27001 Annex A.5.2 (roles and responsibilities) and A.5.9 (asset inventory).

# 2. Scope

All Nodes that (a) sign any Gate decision, (b) hold custody of corporate or client keys, or (c) are RACI-001 Accountable for an active engagement must have an NCR entry. Retired nodes are archived, not deleted, with a supersession marker and retention per L1-EVID-004.

# 3. Entry schema

Each node entry follows the schema below. All fields are mandatory unless marked optional. Changes are tracked with author and timestamp and logged in REG-511.

Field

Meaning

Node ID

Short stable identifier, e.g. NODE-DEFI-01

Node name

Human-readable SubDAO / Node name

Node Owner

Named individual accountable for engagement decisions and Hard Stop escalation

Deputy NO

Named backup (SoD: cannot also be PM or TL on same engagement)

Active engagements

Pointers to Project Security Frameworks (PSF) currently open

Risk appetite override

Any node-level tightening of corporate risk appetite (see L0-5)

Delegated authorities

Which gates the NO is pre-authorised to sign (typically G1-A, G2-A, G3-A, G5-A, G6-A, G8-A)

Excluded authorities

Gates requiring escalation regardless of delegation (always G4-A, G7-IRR)

Signing wallet(s)

Multisig address, M-of-N config, co-signer roster

Monitoring endpoints

Tenderly / Defender / Grafana dashboards for this node's assets

Last review date

Per POL-001 review cadence (T2+: quarterly)

Notes

Free-text for audit trail

# 4. Governance rules

Every engagement in the GRC lifecycle (P1–P12) must reference its governing Node by Node ID at Phase 1.

A Node Owner cannot simultaneously hold the TL or DevOps Deployer role on an engagement they own (two-person rule).

Any change to signing wallet configuration is a C3+ change (POL-005) and requires Gate G4-A sign-off.

Review cadence by tier follows OPS-001: T1 every 6 months, T2 quarterly, T3 monthly, T4 continuous.

Node Owner departures trigger immediate re-assignment; the HR Joiner/Mover/Leaver workflow (L2-ACCESS-203) must include NCR handover as a checklist item.

# 5. Seed register

The table below seeds the register with the Nodes implied by the current Security Team and project portfolio. Names and wallet addresses are redacted pending CISO+NO completion.

Node ID

Name

Owner

Deputy

Tier

Active

Signing wallet

Last review

NODE-DEFI-01

DeFi Core

[NO_NAME]

[DEPUTY]

T3

3

0x… (3-of-5)

2026-03-15

NODE-INFRA-02

Infrastructure

[NO_NAME]

[DEPUTY]

T2

2

0x… (2-of-3)

2026-02-28

NODE-PLATFORM-03

Platform (Track A)

[NO_NAME]

[DEPUTY]

T2

1

0x… (3-of-5)

2026-03-20

NODE-CLIENT-04

Client Delivery (Track B)

[NO_NAME]

[DEPUTY]

T1

5

N/A (client custody)

2026-03-10

# 6. Change log

Every amendment to the NCR is recorded with: timestamp, author, prior value, new value, reason, and reference to the approving Gate decision. The change log is an audit-grade record per L1-EVID-004 and is exportable to the Evidence Calendar.

# 7. Related documents

L0-2 Programme Governance Charter

POL-001 Project Governance Policy

POL-004 Access Control and SoD

L1-KEY-005 Key/Treasury &amp; Signing Ceremonies Standard

RACI-001 Enterprise RACI (NEW)

OPS-001 Project Risk Scoring Framework
