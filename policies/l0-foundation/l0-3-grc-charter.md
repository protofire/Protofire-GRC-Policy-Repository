---
id: "L0-3"
title: "GRC Charter"
type: "Charter"
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

# L0-3 — GRC Charter

GRC Charter

# 0. Document Control

Attribute

Value

Document ID

L0-3

Title

GRC Charter

Hierarchy Level

L0 -- Foundation

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

CISO / GRC Manager

Approver

Director of Engineering (DoE) / Node Owner

Classification

Confidential -- Internal

Supersedes

—

References

GRC-MASTER-001; POL-001 ISMS Policy; ISO 27001:2022 §5.1-5.3; NIST CSF 2.0 GV.OC

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

The GRC Charter establishes the mandate, authority, scope, objectives and governance structure of the Governance, Risk and Compliance (GRC) function within Protofire DAO LLC. It serves as the foundational authority document from which all lower-tier policies, standards, procedures and guidelines derive their legitimacy.

# 2. Mission Statement

To protect Protofire&apos;s stakeholders -- clients, team members, and the broader ecosystem -- by maintaining a risk-aware culture, ensuring compliance with applicable legal and regulatory obligations, and enabling secure delivery of blockchain infrastructure and smart-contract engineering services.

# 3. Scope

This Charter applies to all Protofire personnel (employees, contractors, sub-processors), all information systems, all client engagements, and all jurisdictions in which Protofire operates. It covers:

Information Security -- confidentiality, integrity and availability of data and systems

Operational Risk -- business continuity, incident management, change control

Compliance -- GDPR, CCPA/CPRA, LGPD, MiCA, SOC 2 Type II readiness, ISO 27001:2022 alignment

Third-Party Risk -- vendor assessments, sub-processor governance, SLA management

Smart-Contract &amp; Protocol Security -- audit lifecycle, deployment controls, key management

# 4. Authority &amp; Mandate

The GRC function operates under direct authority of the Node Owner (NO) and is executed by the CISO, with delegation to the GRC Manager for day-to-day operations. This mandate includes:

Right of access to any system, log, repository, or personnel record necessary to assess risk or compliance

Authority to issue binding directives (policies, standards) requiring compliance by all personnel

Power to invoke hard stops (HS-01 through HS-07) halting engagement or deployment activity

Budget authority for GRC tooling, training, external audits and insurance premiums

Escalation path directly to the Node Owner, bypassing operational management where risk warrants

# 5. GRC Organisational Structure

The GRC function is structured as follows:

Role

Primary Responsibility

Reports To

Node Owner (NO)

Ultimate accountability; gate signatory

Board / DAO Governance

CISO / vCISO

Security strategy; risk appetite; policy approval

Node Owner

GRC Manager

Policy lifecycle; register maintenance; audit coordination

CISO

DPO (Data Protection Officer)

Privacy compliance; DPIA reviews; DSR processing

CISO (functional), NO (independence)

Technical Lead (TL)

Threat modelling; security baselines; deployment sign-off

CISO (security), DoE (technical)

Project Manager (PM)

RACI population; PSF initiation; SoD checks

GRC Manager

Account Manager (AM)

Client risk scoring; Hard Stop verification; proposal GRC sections

GRC Manager

QA Engineer

Independent audit 2nd reviewer; fuzz/property testing

TL (technical), GRC Manager (audit)

DevOps Engineer

CI/CD security gates; monitoring; deployment execution

TL (technical), GRC Manager (compliance)

Finance/Billing

Payment schedule; arrears monitoring; HS-05 enforcement

NO (financial), GRC Manager (compliance)

# 6. Objectives

The GRC function shall pursue the following measurable objectives on an annual cycle:

#

Objective

Metric / Target

O1

Maintain zero Critical / High unresolved findings for &gt; 30 days

REG-501 aging report; target: 0

O2

Complete all mandatory policy reviews within cadence

REG-511 compliance; target: 100%

O3

Achieve SOC 2 Type II readiness by Q4 2026

External readiness assessment score ≥ 85%

O4

Reduce mean-time-to-detect (MTTD) for security incidents

REG-509; target: &lt; 4 hours

O5

Ensure 100% personnel security-awareness training completion

REG-507; target: 100% within 30 days of onboarding

O6

All client engagements pass Gate G1-A risk scoring before SOW signature

REG-505 / CL-PHASE-001; target: 100%

O7

Vendor risk assessments completed for all Critical/High vendors

REG-502; target: 100% within 90 days of onboarding

# 7. Risk Appetite Statement

Protofire operates in the Web3/DeFi space where smart-contract vulnerabilities can result in immediate, irreversible financial loss. Accordingly:

Zero tolerance for deployment of unaudited smart contracts to mainnet (HS-03)

Zero tolerance for OFAC-sanctioned counterparties (HS-01)

Low appetite for residual risk rated Critical after mitigation -- must escalate to NO within 24 h

Moderate appetite for operational risk where compensating controls exist and are documented

Risk acceptance requires formal sign-off per POL-009 Exception Management Policy, with CISO + NO co-sign for E3+ exceptions

# 8. Policy Hierarchy

The GRC document hierarchy is governed by GRC-MASTER-001 and follows six levels:

Level

Type

Examples

L0

Foundation

GRC Charter (this document), Concordance Log, Enterprise Framework

L1

Policy

POL-001 through POL-011 -- &quot;what must be done&quot;

L2

Standard / Procedure

STD-101 through STD-104; PR-201 through PR-207 -- &quot;how it must be done&quot;

L3

Guideline

GL-301 through GL-304 -- &quot;recommended approaches&quot;

L4

Plan

PLAN-701 through PLAN-703 -- time-bound execution roadmaps

L5

Template / Form

FRM-801 through FRM-805 -- reusable artefacts

L6

Register / Record

REG-501 through REG-511 -- evidence of compliance

# 9. Reporting &amp; Accountability

The GRC function reports to the Node Owner through the following cadences:

Weekly: CISO → NO security posture summary (KRI dashboard, open incidents, gate status)

Monthly: GRC Manager → CISO policy compliance scorecard; register health metrics

Quarterly: CISO → NO + DoE formal risk review; updated risk register (REG-501); training compliance (REG-507)

Annual: GRC Manager → NO comprehensive GRC maturity assessment; Charter review; budget request

Ad-hoc: Immediate escalation for any HS trigger, Critical-severity incident, or regulatory inquiry

# 10. Amendment Process

This Charter may be amended only by the Node Owner upon recommendation of the CISO. Amendments are versioned in REG-511 and require a 14-day review period for stakeholder comment before effective date. Material changes (scope expansion, authority modification, risk appetite shift) require DoE co-approval.

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

GRC-MASTER-001 Enterprise GRC Framework

POL-001 ISMS Policy

GRC-CONC-001 Concordance Log

REG-511 Document Control Register

CL-PHASE-001 Client Engagement Lifecycle
