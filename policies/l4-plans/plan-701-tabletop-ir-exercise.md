---
id: "PLAN-701"
title: "Tabletop IR Exercise Plan"
type: "Plan"
level: "L4"
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

# PLAN-701 — Tabletop IR Exercise Plan

# Tabletop Incident Response Exercise Plan

Field

Value

Document ID

PLAN-701

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

CISO

Approver

CISO + CEO

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

This plan operationalises the Security Brief §7 requirement for bi-annual tabletop incident-response exercises and supports ISO 27001 Annex A.5.24 (incident-management planning and preparation), A.5.27 (learning), and A.5.30 (ICT readiness for business continuity).

# 2. Scope

The plan covers the Protofire Incident Response team composition defined in L2-INC-201 and the Security Team roster, plus observers from Board/CEO, Legal, HR, and external retainers (SEAL 911, MDR providers). Exercises are run against production-representative (not production) environments; simulated on-chain activity uses testnets.

# 3. Scenario library

Each scenario maps to a Hard Stop, a Web3-specific threat class, or a regulatory obligation. Facilitators rotate scenarios so that each high-impact category is exercised at least once every two years.

Scenario ID

Title

Threat category

Primary control under test

Target roles

Duration

SC-01

Smart contract exploit (re-entrancy) on live mainnet

Technical / Web3

Contract PAUSE, front-running, MDR engagement

CEO, CISO, TL, DevOps, Legal

90 min

SC-02

Key compromise — multisig signer phished

Human / Key management

L1-KEY-005; rotate signers; freeze multisig

CISO, NO, TL, IT

75 min

SC-03

Ransomware on developer workstations

Technical / Endpoint

Isolation, backup restore, L1-BC-008

CISO, IT, DevOps, HR

90 min

SC-04

GDPR breach — client PII exfiltrated

Privacy

PR-208 breach notification (72h), DPA

DPO, CEO, Legal, CISO

60 min

SC-05

Insider threat — TL commits backdoor

Human / Insider

Two-person rule, L2-ACCESS-203, audit

CISO, TL team, HR, Legal

90 min

SC-06

DeFi protocol oracle manipulation

Economic

Circuit breaker, economic simulation, TVL freeze

TL, DevOps, vCISO, NO

90 min

SC-07

Supply-chain compromise — dependency backdoor

Technical / Third-party

SBOM, SAST, POL-007 vendor audit

DevOps, CISO, Legal

75 min

SC-08

OFAC sanction of a client wallet mid-engagement (HS-01)

Regulatory / Hard Stop

HS-01 escalation, MSA termination, treasury isolation

AM, Legal, CEO, CISO

60 min

# 4. Exercise schedule

Two exercises per calendar year (H1 and H2), aligned with internal-audit cadence. Scenarios rotate through the library; real incidents in the preceding 12 months are re-run as tabletops to validate remediation.

Quarter

Scenario

Lead facilitator

Observer / scorer

Post-exercise review

2026-H2 (Q3)

SC-01 (contract exploit)

vCISO

External IR retainer (e.g. SEAL 911)

Within 7 days

2026-H2 (Q4)

SC-04 (GDPR breach)

DPO

Legal counsel

Within 7 days

2027-H1 (Q1)

SC-02 (key compromise)

CISO

vCISO

Within 7 days

2027-H1 (Q2)

SC-06 (oracle manipulation)

TL + vCISO

External economic auditor

Within 7 days

2027-H2 (Q3)

SC-03 (ransomware)

CISO

External MDR

Within 7 days

2027-H2 (Q4)

SC-08 (OFAC sanction)

CISO

Legal counsel

Within 7 days

2028-H1 (Q1)

SC-05 (insider threat)

vCISO

HR + Legal

Within 7 days

2028-H1 (Q2)

SC-07 (supply-chain)

CISO + DevOps Lead

External assessor

Within 7 days

# 5. Exercise flow

Facilitator briefs participants on scenario; observers are assigned.

Inject 1: initial detection signal. Participants declare or dismiss.

Inject 2: escalation trigger. Participants execute IR Phase 1 (0–15 min).

Inject 3: complication (e.g. key co-signer unavailable, media attention). Participants execute Phase 2 (containment).

Inject 4: recovery decision point. Participants execute Phase 3 (investigate &amp; recover).

Debrief: hot wash, observer scoring, blameless retrospective scheduled within seven days.

# 6. Scoring rubric

Dimension

Weight

Pass threshold

Detection time (actual vs target)

20%

Within Phase 1 (0–15 min)

Containment actions taken

25%

Correct action in Phase 2 (15–60 min)

Communication discipline

15%

Pre-defined notifications executed

Regulatory notification path (where relevant)

10%

Correct authority, within 72h for GDPR

Decision authority (correct RACI)

15%

Accountable role made call without escalation gap

Post-incident learning (blameless retro)

15%

Learning documented within 7 days

# 7. Deliverables

Exercise log (decisions, timestamps, injects).

Scoring sheet signed by facilitator and observers.

Action item list with owners and SLAs feeding REG-501 (Risk Register) and the Evidence Calendar.

Retrospective minutes (blameless) published to GRC Committee within seven days.

# 8. Related documents

POL-017 Incident Management Policy

L2-INC-201 Incident Response Procedure

L1-BC-008 Business Continuity Standard

L2-TEST-204 BCM/DR Testing Standard

PR-208 Breach Notification Procedure

RACI-001 (NEW) — Incident SEV-1 rows

REG-512 Evidence Calendar — EVD-H-02 row
