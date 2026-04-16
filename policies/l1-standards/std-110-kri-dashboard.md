---
id: "STD-110"
title: "KRI Dashboard Specification"
type: "Specification"
level: "L1-STD"
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

# STD-110 — KRI Dashboard Specification

# KRI Dashboard Specification

Field

Value

Document ID

STD-110

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

CISO

Approver

CEO + Board

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

This specification defines the Key Risk Indicators (KRIs) that Protofire monitors to provide early warning of control failures, Hard Stop breaches, and emerging exposures. The KRI dashboard feeds the quarterly Board reporting, the Evidence Calendar, the Internal Audit Programme, and the CISO's Security 360 weekly review.

# 2. Design principles

Each KRI is computable from a machine-readable source (ticketing system, scan output, ledger, IdP) without manual aggregation.

Each KRI has two thresholds: Amber (investigate) and Red (escalate).

A Red threshold that equates to a Hard Stop condition is annotated with the HS-xx reference and requires immediate escalation to CEO or CISO regardless of cadence.

KRIs are ordered from most time-sensitive (daily/per-deploy) to least (quarterly).

The dashboard renders RAG (Red-Amber-Green) tiles plus a 13-week sparkline per KRI.

# 3. KRI catalogue

KRI ID

Name

Formula / Source

Amber threshold

Red threshold

Owner

Cadence

KRI-001

Open Critical findings &gt; 30 days

count(findings where severity=Critical and age_days&gt;30)

≥ 1

≥ 3

CISO

Weekly

KRI-002

Engagements in T3/T4 without current audit

count(engagements where tier in (T3,T4) and last_audit_days&gt;90)

≥ 1

≥ 2

CISO

Monthly

KRI-003

MFA coverage on admin accounts

100 * mfa_enrolled_admins / total_admins

&lt; 98%

&lt; 95%

IT

Weekly

KRI-004

Cold-storage ratio of corporate assets

100 * cold_wallet_value / total_treasury_value

&lt; 85%

&lt; 80%

CFO + Treasury

Daily

KRI-005

Open vulnerabilities rated High+

count(vulns where cvss&gt;=7 and status!=Closed)

≥ 5

≥ 15

vCISO

Weekly

KRI-006

Mean time to patch (MTTP) — Critical

avg_days(close_date - detect_date) where cvss&gt;=9

&gt; 7d

&gt; 14d

DevOps + IT

Monthly

KRI-007

Payment arrears &gt; 30 days

count(invoices where age_days&gt;30 and paid=false)

≥ 1

≥ 3 (HS-05 at 60d)

FIN + NO

Weekly

KRI-008

Client concentration

max_client_revenue_pct(trailing_12mo)

&gt; 50%

&gt; 60% (HS-04)

CFO + CEO

Monthly

KRI-009

Incidents SEV-1 or SEV-2 trailing 90 days

count(incidents where sev in (1,2))

≥ 1

≥ 3

CISO + IR team

Weekly

KRI-010

Smart-contract deployments without 3rd-party audit

count(mainnet_deploys where external_audit=none)

≥ 1 (any)

≥ 2 (HS-03)

TL + vCISO

Per deploy

KRI-011

Access reviews overdue

count(nodes where monthly_access_review_overdue)

≥ 1

≥ 3

IT + HR

Monthly

KRI-012

DPIA screenings overdue

count(T2+ EU-PII engagements without CL-409 complete)

≥ 1

≥ 2

DPO

Monthly

KRI-013

Two-person rule violations (deploy)

count(prod_deploys where deployer_id = reviewer_id)

≥ 1

≥ 1 (zero-tolerance)

CISO

Per deploy

KRI-014

Policy spot-check non-conformance rate

non_conformant / total_sampled

&gt; 5%

&gt; 15%

GRC Manager

Quarterly

KRI-015

On-chain circuit-breaker (PAUSE) readiness

count(prod_contracts where pause_role_assigned=false)

≥ 1

≥ 1 (zero-tolerance for DeFi)

TL

Monthly

# 4. Data sources

Ticketing system: GRC work items, audit findings, incident tickets.

IdP (MFA, privileged access): directory export.

Vulnerability management tool: scan results.

Billing system: invoice age and paid status.

Treasury: multisig balances, cold/hot ratio.

CI/CD: deployment metadata including deployer identity.

Monitoring endpoints: Tenderly / OpenZeppelin Defender alerts.

# 5. Governance

The CISO is the KRI owner. The GRC Manager operates the dashboard. Amber breaches are reviewed at the weekly Security 360; Red breaches are escalated within one business day to the relevant Accountable role per RACI-001. A KRI that remains Red for two consecutive reporting cycles triggers a formal finding in the risk register (REG-501) with a remediation plan.

# 6. Change control

Adding, removing, or re-thresholding a KRI is a C2 change (POL-005): CISO-approved, Board-informed. Changing the data source or formula is a C3 change (requires independent validation against prior baseline).

# 7. Related documents

POL-010 Monitoring and Assurance Policy

REG-501 Risk Register

REG-512 Evidence Calendar

IAP-001 Internal Audit Programme

Control Catalogue (Assurance Controls — KRI dashboards row)
