---
id: "POL-013"
title: "Business Continuity Policy"
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

# POL-013 — Business Continuity Policy

**Document ID**

POL-013

**Document Title**

Business Continuity Policy

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

Director of Engineering + CEO

**Classification**

Confidential — Internal

**Concordance**

Replaces P-005 (GRC-MASTER-001 v1.0) per GRC-CONC-001

**References**

GRC-PF-001; L0-1 GRC Charter; L1-BC-008; L2-TEST-204; L1-INFRA-009; POL-017; ISO 22301:2019; ISO/IEC 27001:2022 A.5.29–A.5.30; NIST CSF 2.0 RC; SOC 2 A1.2; DORA Art.11–12

**Subordinate Documents**

S-111 Business Continuity &amp; DR Standard; PR-210 BCM/DR Testing Procedure; CL-408 Business Continuity Test Checklist; PR-213 Backup &amp; Recovery Procedure

────────────────────────────────────────────────────────────

## 1. Purpose

This Policy establishes Protofire's commitment to maintaining the continuity of essential business functions and client-delivery services during and after disruptive events. It mandates business impact analysis, continuity planning, disaster recovery, and regular testing across all operations.

────────────────────────────────────────────────────────────

## 2. Scope

This Policy applies to: all Protofire corporate functions and IT systems; all client delivery engagements regardless of track or tier; all on-chain operations including deployed smart contracts, monitoring infrastructure, and key management systems; all third-party services critical to Protofire operations (cloud providers, RPC nodes, oracle services).

────────────────────────────────────────────────────────────

## 3. Business Continuity Principles

### 3.1 Proportionality

Continuity measures must be proportionate to the criticality of the service and the risk tier of the engagement. T3/T4 engagements with TVL &gt; $1M require dedicated continuity planning per engagement.

### 3.2 Essential functions

The following are classified as essential functions requiring continuity capability: production smart contract operations (where Protofire holds admin/upgrade keys); client delivery pipelines (CI/CD, source control, secrets management); key management and signing operations; incident response and communication channels; financial operations (billing, payment monitoring).

### 3.3 Recovery objectives

**Function**

**RTO (target)**

**RPO (target)**

Production smart contract monitoring

1 hour

0 (real-time)

Key management / signing capability

4 hours

0

CI/CD pipeline and source control

8 hours

1 hour

Corporate communications (email, Slack)

4 hours

1 hour

Financial systems (billing, invoicing)

24 hours

24 hours

Internal documentation (Google Workspace)

8 hours

4 hours

RTO/RPO targets must be validated through the Business Impact Analysis (§4) and updated annually.

────────────────────────────────────────────────────────────

## 4. Business Impact Analysis (BIA)

### 4.1 Requirement

A BIA must be conducted annually and whenever a material change occurs to Protofire's service portfolio, infrastructure, or client base. The BIA identifies critical business processes, their dependencies, acceptable downtime, and the financial and reputational impact of disruption.

### 4.2 Web3-specific considerations

The BIA must specifically address: loss of access to production multisig keys; failure of RPC node providers; oracle service outages; blockchain network congestion or chain halts; smart contract pause function availability; loss of monitoring and alerting capability.

### 4.3 Output

The BIA produces: a prioritised list of essential functions; validated RTO/RPO targets; identified single points of failure; and input to the Business Continuity Plan.

────────────────────────────────────────────────────────────

## 5. Business Continuity Plans (BCP)

### 5.1 Corporate BCP

A corporate BCP must be maintained covering all essential functions identified in the BIA. The BCP must include: activation criteria and escalation procedures; roles and responsibilities (aligned with RACI-001); communication plans (internal and external); recovery procedures for each essential function; alternative operating procedures for degraded service; supplier and third-party dependencies with fallback options.

### 5.2 Project-level continuity

For T3/T4 engagements and any engagement with TVL &gt; $1M, a project-specific continuity section must be included in the PSF (P4-PM-002) covering: emergency contract pause/unpause procedures; key recovery procedures; fallback monitoring configuration; client communication escalation path.

────────────────────────────────────────────────────────────

## 6. Disaster Recovery

### 6.1 IT disaster recovery plan

An IT disaster recovery plan must be maintained covering: backup and restoration of all critical systems; infrastructure failover procedures; data recovery verification; communication system recovery.

### 6.2 Backup requirements

All critical data must be backed up per PR-213 (Backup &amp; Recovery Procedure). Backups must be: encrypted at rest (S-103); stored in a geographically separate location; tested for recoverability at least quarterly; retained per POL-008 retention schedules.

### 6.3 On-chain recovery

For smart contracts deployed by Protofire with upgrade or admin capabilities: upgrade procedures must be documented in the deployment runbook; emergency pause/unpause procedures must be tested during Phase 8 (testnet); key recovery procedures must be documented in the Signing Ceremony Checklist (CL-411).

────────────────────────────────────────────────────────────

## 7. Testing and Exercise

### 7.1 Requirement

Business continuity plans must be tested at least annually per PR-210 and CL-408. Tests must include at a minimum: tabletop exercise for SEV-1 scenario; technical recovery test for at least one critical system; communication cascade test; backup restoration verification.

### 7.2 Test results

Test results must be documented, including: scenarios tested; participants; outcomes; identified gaps; and remediation actions with owners and deadlines. Test evidence is stored per L1-EVID-004.

────────────────────────────────────────────────────────────

## 8. Roles and Responsibilities

**Role**

**Responsibility**

CISO

BCM programme owner. Maintains BIA, BCP, and DR plans. Commissions annual tests.

Node Owner

Approves BCP activation for SEV-1 events. Authorises emergency expenditure for recovery.

DevOps

Maintains IT DR procedures. Executes backup restoration tests. Manages infrastructure failover.

TL

Maintains project-level continuity procedures. Documents smart contract emergency procedures.

PM

Executes client communication plan during disruptions. Coordinates recovery timeline with clients.

────────────────────────────────────────────────────────────

## 9. Exceptions

Deviations from this Policy are managed under POL-009. No exception may waive the annual BIA requirement or the annual test requirement.

────────────────────────────────────────────────────────────

## 10. Review

This Policy is reviewed annually by the CISO and upon any material change to Protofire's infrastructure, service portfolio, or applicable regulations (DORA, ISO 22301).

────────────────────────────────────────────────────────────

## 11. Approval

**Role**

**Name**

**Signature**

**Date**

CISO

Director of Engineering

CEO

────────────────────────────────────────────────────────────

Document end — POL-013 v1.0
