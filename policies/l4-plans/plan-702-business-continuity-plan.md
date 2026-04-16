---
id: "PLAN-702"
title: "Business Continuity Plan"
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

# PLAN-702 — Business Continuity Plan

Business Continuity Plan

# 0. Document Control

Attribute

Value

Document ID

PLAN-702

Title

Business Continuity Plan (BCP)

Hierarchy Level

L4 -- Plan

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

Node Owner / DoE

Classification

Confidential -- Internal

Supersedes

—

References

L1-BC-008 Business Continuity Policy; ISO 22301:2019; ISO 27001:2022 A.5.29-A.5.30; NIST CSF 2.0 RC

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

PLAN-702 provides the operational plan for maintaining critical business functions during and after a disruptive event. It translates L1-BC-008 policy requirements into actionable procedures with specific RPO/RTO targets, communication plans and recovery steps.

# 2. Scope

Covers all Protofire business functions including: client engagement delivery, smart-contract deployment and monitoring, internal IT infrastructure, financial operations, and personnel safety. Applies to disruptions including: cyber incidents, cloud provider outages, key-person loss, natural disasters affecting remote workers, regulatory enforcement actions, and third-party failures.

# 3. Business Impact Analysis Summary

Critical Function

RTO

RPO

MTPD

Dependencies

Client smart-contract monitoring

1 h

0 (real-time)

4 h

Tenderly, OZ Defender, cloud infra

Active client engagement delivery

4 h

1 h

24 h

GitHub, CI/CD, communication tools

Incident response capability

30 min

N/A

2 h

PagerDuty, SIEM, communication tools

Internal IT / collaboration

8 h

4 h

48 h

Google Workspace, Slack, VPN

Financial operations / billing

24 h

24 h

72 h

ERP, banking, invoicing platform

HR / people operations

48 h

24 h

1 week

HRIS, payroll

GRC register &amp; policy maintenance

72 h

24 h

2 weeks

Google Drive, GitHub

RTO = Recovery Time Objective; RPO = Recovery Point Objective; MTPD = Maximum Tolerable Period of Disruption.

# 4. Activation Criteria

Level 1 (Business As Usual): single-system outage &lt; 1 h; handled by on-call team

Level 2 (BCP Activation): disruption affecting one or more critical functions beyond RTO or RPO

Level 3 (Crisis Management): organisation-wide disruption; regulatory action; confirmed data breach; key-person incapacitation

Activation authority: CISO (Level 2), Node Owner (Level 3). Any team member can request activation.

# 5. Communication Plan

Audience

Channel

Timing &amp; Content

Crisis team

PagerDuty + Slack #crisis-ops

Immediate: situation summary, role assignments, first actions

All personnel

Slack #general + email

Within 1 h: what happened, what we&apos;re doing, expected duration

Affected clients

Email + scheduled call

Within 4 h: impact assessment, mitigation steps, next update ETA

Regulatory (if required)

Formal notification per GDPR Art.33

Within 72 h of awareness for personal data breach

Node Owner / Board

Direct call + written brief

Within 30 min (Level 3); within 2 h (Level 2)

# 6. Recovery Procedures

## 6.1 Cyber Incident (ransomware, breach, smart-contract exploit)

Invoke PR-203 Incident Response Procedure -- contain, eradicate, recover

Isolate affected systems; preserve forensic evidence

For smart-contract exploit: invoke emergency pause if available; notify client; engage external audit firm

Restore from verified backups; validate integrity before reconnection

## 6.2 Cloud Provider Outage

Activate redundant infrastructure in secondary region (if provisioned)

Failover monitoring to backup provider (Tenderly ↔ OZ Defender)

Communicate to clients with estimated recovery based on provider status page

## 6.3 Key-Person Unavailability

Deputy assignments: CISO → GRC Manager; NO → DoE; TL → Senior Developer per RACI-001

Emergency credential access via break-glass procedure (sealed envelope + dual-control)

Knowledge base and runbooks must be current to enable handover (verify quarterly)

## 6.4 Third-Party / Supply-Chain Failure

Invoke vendor BCP verification per REG-502 contractual requirements

Activate identified alternative vendors per vendor risk assessment

Assess client impact and communicate per §5 communication plan

# 7. Testing &amp; Exercising

Exercise Type

Frequency

Description

Tabletop exercise

Quarterly

Walk-through of BCP scenario with crisis team; identify gaps

Backup restoration test

Quarterly

Full restore of critical systems from backup; validate RPO/RTO

Communication test

Semi-annual

Invoke communication plan (non-crisis); verify all channels operational

Full BCP drill

Annual

Simulated disruption; measure actual RTO/RPO against targets

Post-incident review

After every BCP activation

Lessons learned; BCP updates per findings

# 8. Plan Maintenance

BCP reviewed annually and after any activation, significant organisational change, or infrastructure change

Contact lists verified quarterly (personnel, clients, vendors, regulatory contacts)

Dependencies and RTO/RPO targets reassessed annually during BIA refresh

Updates logged in REG-511 Document Control Register

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

L1-BC-008 Business Continuity Policy

PR-203 Incident Response Procedure

REG-502 Vendor &amp; Third-Party Register

RACI-001 Responsibility Assignment Matrix
