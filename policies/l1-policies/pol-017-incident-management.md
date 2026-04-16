---
id: "POL-017"
title: "Incident Management Policy"
type: "Policy"
level: "L1"
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

# POL-017 — Incident Management Policy

**Document ID**

POL-017

**Document Title**

Incident Management Policy

**Document Type**

Policy (L1)

**Version**

1.0

**Status**

Draft — pending approval

**Effective Date**

Upon approval — [DD Month 2026]

**Review Cycle**

Annual (or upon material change)

**Owner**

CISO — Aleksey Lekontsev

**Approver**

Director of Engineering + Node Owners Council

**Classification**

Confidential — Internal

**Concordance**

Replaces P-010 (GRC-MASTER-001 v1.0) per GRC-CONC-001

**References**

GRC-PF-001; L0-1 GRC Charter; L2-INC-201; POL-011; POL-002; GDPR Art.33/34; ISO/IEC 27001:2022 A.5.24–A.5.28; NIST CSF 2.0 RS; SOC 2 CC7; DORA Art.17

**Subordinate Documents**

PR-203 Incident Response Procedure; PR-208 Data Breach Notification Procedure; CL-406 Incident Response Checklist; GL-306 Incident Classification Guideline; REG-503 Incident Registry

────────────────────────────────────────────────────────────

## 1. Purpose

This Policy establishes Protofire's mandatory requirements for detecting, reporting, triaging, containing, resolving, and learning from security incidents across all corporate operations, client delivery engagements, and Web3/DeFi platform interactions. It ensures compliance with GDPR 72-hour breach notification obligations, DORA ICT incident reporting requirements, and ISO 27001 incident management controls.

────────────────────────────────────────────────────────────

## 2. Scope

This Policy applies to all security and operational incidents affecting Protofire-managed or Protofire-delivered systems, including: smart contract exploits, front-end compromises, private key exposure, CI/CD pipeline breaches, infrastructure incidents, data breaches (personal and non-personal), denial-of-service events, insider threats, and vendor/third-party incidents that impact Protofire operations.

All Protofire personnel, contractors, Node Owners, and partner resources are subject to this Policy.

────────────────────────────────────────────────────────────

## 3. Incident Classification

### 3.1 Severity levels

**Severity**

**Definition**

**Response SLA**

**Escalation**

**SEV-1 — Critical**

Active exploitation with confirmed financial loss, private key compromise, or production smart contract exploit. Complete loss of essential service.

Immediate response. CISO notified within 15 minutes. War room activated within 30 minutes.

CISO + Node Owner + CEO (if TVL &gt; $1M)

**SEV-2 — High**

Confirmed security breach without active exploitation, significant service degradation, personal data breach affecting &gt;100 data subjects.

Response within 1 hour. CISO notified within 30 minutes.

CISO + Node Owner

**SEV-3 — Medium**

Suspected security event, minor service disruption, vulnerability being actively exploited in the wild (but not against Protofire), personal data breach affecting &lt;100 data subjects.

Response within 4 hours. CISO notified within 2 hours.

CISO

**SEV-4 — Low**

Security anomaly, near-miss, policy violation without breach, failed attack attempt.

Response within 1 business day.

Incident Manager

### 3.2 Web3-specific incident types

The following incident types receive mandatory SEV-1 or SEV-2 classification regardless of other factors: smart contract re-entrancy exploit (SEV-1); oracle manipulation with financial impact (SEV-1); private key compromise of any production signer (SEV-1); governance attack or malicious upgrade (SEV-1); front-end DNS hijack or UI injection (SEV-2); multisig signer compromise (SEV-2).

────────────────────────────────────────────────────────────

## 4. Incident Response Lifecycle

### 4.1 Phase 1 — Detection and reporting

All Protofire personnel must report suspected incidents to the CISO or the designated incident Slack channel immediately upon detection. Automated monitoring systems (on-chain monitors, SIEM, alerting platforms) must feed into the incident detection pipeline.

Internal reporting deadline: no later than 4 hours after discovery (aligned with POL-011 §8.2).

### 4.2 Phase 2 — Triage and activation

The Incident Manager (or CISO for SEV-1/SEV-2) conducts initial triage: confirms the event, classifies severity, determines scope, and activates the appropriate response team. For SEV-1 events, the CISO activates the war room within 30 minutes.

### 4.3 Phase 3 — Containment and eradication

Execute pre-defined containment measures per L2-INC-201. For smart contract incidents: activate pause functions (if available), revoke compromised keys, deploy monitoring on affected contracts. Root cause analysis (RCA) is initiated during containment using 5-Whys or Ishikawa methodology.

### 4.4 Phase 4 — Recovery and validation

Restore normal operations with verified system integrity. No service restoration is announced until the CISO confirms containment is complete and residual risks are documented. For on-chain incidents: verify contract state consistency before re-enabling operations.

### 4.5 Phase 5 — Post-incident review (PIR)

A formal PIR is mandatory for all SEV-1 and SEV-2 incidents and recommended for SEV-3. The PIR must document: root cause, timeline, effectiveness of response, lessons learned, and Corrective and Preventive Actions (CAPA). PIR must be completed within 10 business days of incident closure. CAPA items are tracked in REG-503 with named owners and deadlines.

────────────────────────────────────────────────────────────

## 5. Personal Data Breach Notification

### 5.1 Supervisory authority notification (GDPR Art.33)

Where an incident involves a personal data breach, the CISO (DPO function) must notify the relevant supervisory authority within 72 hours of becoming aware of the breach, unless the breach is unlikely to result in a risk to data subjects' rights and freedoms. The detailed procedure is PR-208.

### 5.2 Data subject notification (GDPR Art.34)

Where the breach is likely to result in a high risk to data subjects, affected individuals must be notified without undue delay per POL-011 §8.3.

### 5.3 DORA ICT incident reporting (Art.17)

Where applicable, major ICT-related incidents must be reported to the relevant financial supervisory authority in accordance with DORA Article 17 timelines and templates.

────────────────────────────────────────────────────────────

## 6. Roles and Responsibilities

**Role**

**Responsibility**

CISO

Incident response lead for SEV-1/SEV-2. Approves PIR. Owns PR-208 (breach notification). Maintains REG-503.

Node Owner

Receives escalation for SEV-1/SEV-2. Approves client-facing communications. Authorises emergency changes.

Incident Manager

Leads response for SEV-3/SEV-4. Coordinates triage and containment. Initiates PIR.

TL

Executes technical containment and eradication. Leads RCA for smart contract and infrastructure incidents.

DevOps

Executes infrastructure containment (network isolation, key rotation). Provides monitoring data to RCA.

PM

Manages client communication during incidents (Track B). Documents timeline.

All personnel

Report suspected incidents within 4 hours. Preserve evidence. Follow CISO instructions.

────────────────────────────────────────────────────────────

## 7. Evidence and Record-Keeping

All incidents must be recorded in REG-503 (Incident Registry) with: incident ID, date/time of detection, date/time of reporting, severity classification, description, affected systems, response actions, root cause, CAPA items, and closure date. Evidence must be preserved per L1-EVID-004 and GL-307 (Evidence Collection Guideline).

────────────────────────────────────────────────────────────

## 8. Key Performance Indicators

**KPI**

**Target**

**Measurement**

Mean Time to Detect (MTTD)

&lt; 1 hour (SEV-1/2)

Time from incident occurrence to detection

Mean Time to Respond (MTTR)

&lt; 4 hours (SEV-1)

Time from detection to containment

PIR completion rate

100% for SEV-1/SEV-2

PIR completed within 10 business days

GDPR notification compliance

100% within 72 hours

Supervisory authority notified on time

CAPA closure rate

90% within 30 days

CAPA items closed within deadline

────────────────────────────────────────────────────────────

## 9. Integration with CL-PHASE-001 Lifecycle

Incident response readiness is established at Phase 4 (IRP draft in PSF) and validated at Gate G4. On-chain monitoring is configured at Phase 8 (DevOps agent) and validated at Phase 9 (Irreversibility Gate). Post-deployment incidents during Phase 10 are handled under this Policy.

────────────────────────────────────────────────────────────

## 10. Exceptions

Deviations from this Policy are managed under POL-009. No exception may extend the 72-hour GDPR notification deadline or waive the mandatory PIR requirement for SEV-1/SEV-2 incidents.

────────────────────────────────────────────────────────────

## 11. Review

This Policy is reviewed annually by the CISO and upon any material change to GDPR, DORA, or the Protofire incident response capability.

────────────────────────────────────────────────────────────

## 12. Approval

**Role**

**Name**

**Signature**

**Date**

CISO

Director of Engineering

Node Owner

────────────────────────────────────────────────────────────

Document end — POL-017 v1.0
