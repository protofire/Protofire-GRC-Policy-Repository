---
id: "PLAN-703"
title: "Disaster Recovery Plan"
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

# PLAN-703 — Disaster Recovery Plan

Disaster Recovery Plan

# 0. Document Control

Attribute

Value

Document ID

PLAN-703

Title

Disaster Recovery Plan (DRP)

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

DevOps Lead / CISO

Approver

Node Owner / DoE

Classification

Confidential -- Internal

Supersedes

—

References

PLAN-702 Business Continuity Plan; POL-006 Network &amp; Infrastructure Security; ISO 27001:2022 A.8.13-A.8.14; NIST CSF 2.0 RC.RP

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

PLAN-703 provides the technical recovery procedures for restoring Protofire&apos;s IT infrastructure, data and services following a disaster or major outage. It is a technical companion to PLAN-702 (BCP) and focuses on system-level recovery rather than business-level continuity.

# 2. Scope

Covers: cloud infrastructure (AWS, GCP, Azure as applicable), CI/CD pipelines, monitoring systems, repositories, databases, communication platforms, on-chain monitoring infrastructure, and all systems classified as Critical or High in REG-503 (Asset Register).

# 3. Recovery Objectives

System / Service

RTO

RPO

Recovery Method

On-chain monitoring (Tenderly, OZ Defender)

1 h

0

Failover to secondary provider; pre-configured templates

CI/CD pipeline (GitHub Actions)

4 h

1 h

Rebuild from IaC; secrets from vault backup

SIEM / log aggregation

4 h

4 h

Restore from snapshot; replay from log archive if needed

Internal communication (Slack, email)

4 h

N/A

Provider SLA; backup channel: Matrix self-hosted

Repositories (GitHub)

2 h

0

Git mirrors updated every 15 min; clone from mirror

Database / state stores

4 h

1 h

Point-in-time restore from automated snapshots

VPN / network access

2 h

N/A

Rebuild from IaC; distribute new configs

Client-facing APIs

2 h

0

Multi-region deployment; DNS failover

# 4. Backup Strategy

## 4.1 Backup Schedule

Data Class

Frequency

Retention

Storage

Databases (production)

Continuous (point-in-time)

30 days hot, 90 days cold, 7 years archive

Cloud-native + cross-region replica

Repositories

15-min mirror sync

Indefinite (git history)

Secondary cloud provider

Configuration / IaC

On every commit

Indefinite (git history)

GitHub + encrypted backup

Secrets / vault

Daily encrypted export

90 days

Air-gapped storage + HSM-encrypted

Logs / SIEM

Continuous ingest

12 months hot, 24 months cold, 7 years archive

WORM-compliant storage

Documents (Drive, policies)

Provider-managed

7 years

Google Workspace + quarterly encrypted export

## 4.2 Backup Verification

Monthly: automated restore test of one production database to isolated environment

Quarterly: full infrastructure rebuild from IaC in clean environment; measure time to operational

Annual: complete DR drill with actual failover (coordinated with PLAN-702 BCP drill)

Each test: document results, RTO/RPO achieved, and gaps found in REG-504

# 5. Recovery Procedures

## 5.1 Invocation

DR Plan activated by CISO or DevOps Lead when a disaster is declared per PLAN-702 §4

DR Lead (DevOps Lead or delegate) coordinates all technical recovery activities

Recovery actions are logged in real-time in a dedicated incident channel

## 5.2 Recovery Sequence

Phase 1 -- Assess (0-30 min): determine scope; identify affected systems; declare severity

Phase 2 -- Contain (30-60 min): isolate affected components; prevent further damage; preserve evidence

Phase 3 -- Restore Infrastructure (1-4 h): deploy core infrastructure from IaC; restore network, auth, secrets

Phase 4 -- Restore Services (2-8 h): deploy applications; restore data from backups; validate functionality

Phase 5 -- Validate (8-12 h): run smoke tests; verify monitoring active; confirm data integrity; client notification

Phase 6 -- Normalise (12-48 h): return to standard operations; deactivate emergency procedures; schedule post-mortem

# 6. Roles &amp; Responsibilities

Role

DR Responsibility

DR Lead (DevOps Lead)

Coordinate all technical recovery; communicate status to CISO

CISO

Authorise DR activation; oversee security during recovery; approve return-to-normal

TL

Validate application integrity; verify smart-contract monitoring restored

GRC Manager

Document timeline for post-mortem; verify compliance with notification obligations

Node Owner

Authorise emergency spend; approve client communications; final return-to-normal sign-off

# 7. Post-Disaster Review

Blameless post-mortem within 5 business days of return to normal operations

Root-cause analysis documented; timeline reconstruction from recovery logs

DR Plan and PLAN-702 BCP updated with lessons learned within 15 business days

Client debrief for affected engagements within 10 business days

Insurance notification if financial loss exceeds policy threshold

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

PLAN-702 Business Continuity Plan

POL-006 Network &amp; Infrastructure Security

PR-203 Incident Response Procedure

REG-503 Asset Register (CMDB)

REG-504 Change &amp; Release Register
