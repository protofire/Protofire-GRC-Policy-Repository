---
id: "REG-512"
title: "Evidence Calendar"
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

# REG-512 — Evidence Calendar

# Evidence Calendar

Field

Value

Document ID

REG-512

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

CISO

Approver

CISO (with Board notification)

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

The Evidence Calendar is Protofire's master schedule of recurring compliance evidence. It operationalises Section 7 of the GRC Framework (Compliance and Evidence Management) and satisfies the ISO 17021-1:2015 / ISO 19011 requirement to preserve evidence that confirms the operation of ISMS processes over time.

# 2. Scope

Every periodic control-attestation task, audit, test, and re-approval required anywhere in the Protofire GRC library is registered here. Ad-hoc evidence (e.g. one-off incident post-mortems) is recorded in the relevant procedure but is not part of this calendar.

# 3. Calendar structure

Tasks are grouped by cadence: Monthly, Quarterly, Bi-Annual, Annual, and Per-Deployment. Each task has a stable evidence ID (EVD-{cadence}-{NN}), a named owner, an evidence-location pointer, and a delivery SLA. Owners are responsible for producing the artefact, uploading it to the evidence location, and marking the task complete in the GRC ticketing system.

# 4. Monthly evidence

Task

Artefact ID

Owner

Evidence location

SLA

User access review

EVD-M-01

IT / HR

L2-ACCESS-203 review log

5 working days after month-end

Patch management report

EVD-M-02

DevOps + IT

L2-VULN-202 patch log

5 working days

Backup verification

EVD-M-03

DevOps

L1-BC-008 backup log

5 working days

Cold wallet balance reconciliation

EVD-M-04

CFO + Treasury

L1-KEY-005 treasury log

5 working days

Incident ticket triage review

EVD-M-05

CISO

Incident Registry

10 working days

# 5. Quarterly evidence

Task

Artefact ID

Owner

Evidence location

SLA

Vulnerability scan (internal + external)

EVD-Q-01

IT / vCISO

L2-VULN-202 scan reports

End of quarter + 15 days

Privileged access review

EVD-Q-02

IT / vCISO

L2-ACCESS-203 PAM review

End of quarter + 15 days

T3+ engagement acceptance review

EVD-Q-03

CEO + GRC Committee

OPS-001 decision log

End of quarter + 10 days

Risk register update

EVD-Q-04

CISO

REG-501

End of quarter + 10 days

KRI dashboard review

EVD-Q-05

CISO + Board

STD-110 KRI Dashboard

End of quarter + 5 days

# 6. Bi-annual evidence

Task

Artefact ID

Owner

Evidence location

SLA

Internal audit engagement

EVD-H-01

vCISO + Internal Audit

IAP-001 audit reports

Per IAP-001 schedule

Tabletop IR exercise

EVD-H-02

CISO + IR team

PLAN-701 exercise log

H1 and H2 of calendar year

BCM/DR test

EVD-H-03

vCISO

L2-TEST-204 test report

H1 and H2

Policy spot-check review

EVD-H-04

GRC Manager

REG-511 registry delta

Aligned to internal audit

# 7. Annual evidence

Task

Artefact ID

Owner

Evidence location

SLA

External penetration test

EVD-A-01

vCISO + External Assessor

L2-ASSURE-103 engagement report

Q4

Policy library review (all L0–L6)

EVD-A-02

CISO + GRC Manager

REG-511

Q4

SoA re-approval

EVD-A-03

CISO + CEO

SOA-001 updated

Q4

Risk appetite re-approval

EVD-A-04

CEO + Board

L0-5

Q1

Business Impact Analysis (BIA)

EVD-A-05

vCISO

L1-BC-008 BIA output

Q1

ISO 27001 management review (Clause 9.3)

EVD-A-06

CISO + Board

Management review minutes

Q4

Annex A mandatory controls self-assessment

EVD-A-07

CISO

Control Catalogue + SoA

Q4

DPO / supervisory-authority registration renewal

EVD-A-08

CISO-DPO + Legal

GAP-10 registration record

Calendar anniversary

# 8. Per-deployment evidence

Task

Artefact ID

Owner

Evidence location

SLA

Smart contract audit report

EVD-PD-01

Engineering + External Auditor

Gate G6-A / G7-IRR record

Before mainnet

Deployment runbook checklist

EVD-PD-02

TL + DevOps

CL-411 signing ceremony + deploy runbook

Before mainnet

Testnet fuzz/property test results

EVD-PD-03

QA

L3-TEST-204

Before G7-IRR

Two-person rule attestation

EVD-PD-04

TL + DevOps Deployer

Gate G7-IRR record

At deployment

Monitoring &amp; alert validation

EVD-PD-05

DevOps

Tenderly / Defender config snapshot

At deployment

# 9. Operating model

The GRC Manager (or delegate) runs a weekly calendar sweep: tasks due in the next seven days are pushed to the owner's queue; overdue tasks escalate to the CISO.

Agentic flow: where an artefact can be produced from machine-readable evidence (logs, tickets, scan outputs), an agent skill from the Protofire-GRC-Agent-Skill-Suite is invoked to produce the first draft; the human owner verifies and attests.

Each completed task writes a row to REG-511 (Document Registry) with document ID, owner, timestamp, and a pointer to the stored evidence.

Evidence is retained per L1-EVID-004 (minimum seven years for audit-relevant records; indefinite for Board-level decisions).

# 10. Related documents

L1-EVID-004 Evidence and Recordkeeping Standard

REG-511 Document Registry

IAP-001 Internal Audit Programme (NEW)

STD-110 KRI Dashboard Specification (NEW)

GRC Framework §7 Compliance and Evidence Management
