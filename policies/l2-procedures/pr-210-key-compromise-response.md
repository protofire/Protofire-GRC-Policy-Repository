---
id: "PR-210"
title: "Key Compromise Response Procedure"
type: "Procedure"
level: "L2"
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

# PR-210 — Key Compromise Response Procedure

Key Compromise Response Procedure

# 0. Document Control

Attribute

Value

Document ID

PR-210

Title

Key Compromise Response Procedure

Hierarchy Level

L2 - Procedure

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-16

Review Cycle

Semi-annual

Owner

CISO / Technical Lead

Approver

Node Owner

Classification

Confidential - Internal

Supersedes

—

References

PR-203 Incident Response Procedure; STD-104 Cryptographic Controls Standard; POL-002 ISMS Policy; CL-PHASE-001; NIST SP 800-61 Rev.2

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

PR-210 defines the step-by-step response procedure when a cryptographic key compromise is suspected or confirmed. In blockchain/DeFi engineering, key compromise is the highest-severity incident class because it can result in immediate, irreversible financial loss. This procedure supplements PR-203 (general Incident Response) with key-specific actions, tighter SLAs, and mandatory break-glass provisions.

# 2. Scope

Applies to compromise or suspected compromise of any key under Protofire custody or co-custody:

Smart-contract admin keys (owner, proxy admin, upgrader, pauser)

Multi-signature signer keys (hardware wallets, HSM-held keys)

Treasury / fund management keys

Deployment keys (used for contract deployment and verification)

Service account keys, API tokens, and CI/CD signing credentials

TLS private keys and code-signing certificates

Encryption keys protecting client or Protofire data at rest

# 3. Severity Classification

Severity

Trigger

Response SLA

Escalation

KC-1 Critical

Confirmed compromise of mainnet admin/treasury key; active exploit in progress; funds at immediate risk

5 min acknowledge; 15 min contain

Immediate: CISO + NO + TL + client; PagerDuty P1

KC-2 High

Suspected compromise (anomalous signing activity, phishing confirmed, device theft); no active exploit yet

15 min acknowledge; 1 h contain

CISO + TL + client within 30 min

KC-3 Medium

Compromise of non-mainnet key (testnet, staging, CI/CD); or service account key with limited blast radius

30 min acknowledge; 4 h contain

CISO + TL; client if engagement-related

KC-4 Low

Expired or rotated key found exposed (e.g., in commit history); no current access risk

4 h acknowledge; 24 h remediate

GRC Manager; log in REG-509

# 4. Response Phases

## 4.1 Phase 1 - Detection &amp; Triage (0-5 min)

Goal: Confirm the alert, classify severity, activate the response team.

Step 1.1: Receive alert via monitoring (on-chain alert, SIEM, manual report, or signer self-report)

Step 1.2: Triage lead (on-call TL or CISO) classifies severity using section 3 matrix

Step 1.3: Open dedicated incident channel (Slack #key-compromise-[date] or equivalent)

Step 1.4: Page the Key Compromise Response Team (KCRT): CISO, TL, DevOps, affected signer(s)

Step 1.5: Log incident in REG-509 with timestamp, reporter, initial classification

## 4.2 Phase 2 - Immediate Containment (5-15 min for KC-1)

Goal: Prevent further unauthorised use of the compromised key. Every second matters for KC-1.

Step 2.1: EMERGENCY PAUSE - If the affected contract has a pause function, execute immediately via the fastest available signer quorum. Do NOT wait for full analysis.

Step 2.2: Revoke compromised key from all multi-sig signer sets where it participates

Step 2.3: Rotate all credentials that shared infrastructure with the compromised key (vault, CI/CD secrets, API tokens on same device)

Step 2.4: If funds are at risk and pause is not available, execute emergency fund rescue (pre-approved guardian transaction to safe multi-sig) per the engagement\&apos;s Emergency Recovery Plan

Step 2.5: Block compromised address in all internal allowlists and monitoring rules

Step 2.6: Preserve forensic state - snapshot logs, device state, on-chain transaction history from compromised address

## 4.3 Phase 3 - Investigation (15 min - 4 h)

Goal: Determine root cause, blast radius, and whether other keys are affected.

Step 3.1: Determine HOW the key was compromised: phishing, malware, physical theft, insider, supply chain, social engineering, operational error

Step 3.2: Assess blast radius - list all contracts, wallets, and systems the compromised key can/could access

Step 3.3: Check for lateral movement - were other signers or systems accessed from the compromised device?

Step 3.4: Review on-chain history of the compromised address for any unauthorised transactions

Step 3.5: If device compromise - quarantine the device; do NOT power off (preserve volatile memory)

Step 3.6: Timeline reconstruction - build minute-by-minute timeline from first compromise indicator to detection

## 4.4 Phase 4 - Remediation &amp; Key Rotation (1-24 h)

Goal: Replace compromised keys, restore secure operations.

Step 4.1: Generate new replacement key(s) per STD-104 section 5.1 (CSPRNG, hardware wallet, air-gapped)

Step 4.2: Execute key rotation ceremony per CL-411 Signing Ceremony Checklist with two-person rule

Step 4.3: Update all multi-sig signer sets to replace compromised signer with new key

Step 4.4: If contract upgrade is required to rotate admin key - follow POL-005 change classification (emergency C5)

Step 4.5: Update all dependent systems: vault, CI/CD, monitoring alerts, allowlists

Step 4.6: Verify new key works correctly in testnet or staging before mainnet operations resume

Step 4.7: Securely destroy the compromised key per STD-104 section 5.4 (witnessed, logged)

## 4.5 Phase 5 - Notification (parallel with Phases 2-4)

Goal: Fulfil all notification obligations.

Stakeholder

Timing

Content

Client

Within 1 h of confirmed KC-1/KC-2

Nature of compromise; containment actions taken; estimated remediation time; whether funds are affected

Node Owner

Immediately for KC-1; within 30 min for KC-2

Severity; financial exposure; containment status; resource needs

Regulatory (GDPR Art.33)

Within 72 h if personal data exposed

Standard breach notification per PR-203 section 6

Insurance

Within 24 h if financial loss likely

Incident summary; estimated exposure; claim details

Law enforcement

If criminal activity suspected; after CISO + NO + legal approval

Coordinated with CLO; preserve privilege

## 4.6 Phase 6 - Recovery &amp; Verification (24-72 h)

Step 6.1: Unpause contracts only after: new keys in place, monitoring validated, and TL + CISO co-sign

Step 6.2: Execute verification checklist: all signer sets correct, thresholds unchanged, timelocks active, monitoring firing correctly

Step 6.3: Conduct 24-hour enhanced monitoring period post-recovery (alert thresholds lowered)

Step 6.4: Client confirmation that operations are restored to satisfaction

## 4.7 Phase 7 - Post-Incident Review (within 5 business days)

Step 7.1: Blameless post-mortem with full KCRT and affected stakeholders

Step 7.2: Root-cause analysis with contributing factors and systemic weaknesses

Step 7.3: Action items with owners and deadlines - update GL-305, STD-104, STD-105 as needed

Step 7.4: Update REG-509 with full incident record; link to post-mortem document

Step 7.5: CISO report to NO with lessons learned and budget/resource requests

Step 7.6: If engagement-related - update client security posture document (SEC-POSTURE-001)

# 5. Break-Glass Procedure

For situations where normal approval chains cannot be followed due to urgency:

Provision

Detail

Authority

Any member of the KCRT may invoke break-glass for KC-1 without prior approval

Emergency pause

Single authorised signer may execute pause without full quorum if delay &gt; 5 min would result in fund loss; must document justification within 1 h

Emergency credential access

Sealed envelope / escrow key released by 2-of-3: CISO, NO, DoE; logged immediately

Emergency fund rescue

Pre-approved guardian transaction to safe multi-sig; requires 2 available signers from approved rescue set

Post-hoc approval

All break-glass actions must be ratified by NO within 24 h; failure to ratify triggers POL-009 E3 exception

# 6. Pre-Positioned Defences

The following must be configured BEFORE any mainnet deployment to enable rapid response:

Emergency pause function accessible to at least 2 independent signers

Guardian/rescue multi-sig pre-funded with gas and pre-approved for emergency fund movement

On-chain monitoring alerts for all admin key usage (Tenderly/OZ Defender) with PagerDuty integration

Break-glass credential envelopes sealed and stored in physically separate locations

Incident channel template pre-configured in Slack with auto-invite for KCRT members

Pre-drafted client notification template (FRM-806) ready for rapid customisation

# 7. Roles &amp; Responsibilities

Role

Responsibility

CISO

Incident commander; severity classification; notification decisions; post-mortem owner

TL

Technical analysis; key rotation execution; contract interaction; verification

DevOps

Infrastructure containment; credential rotation; monitoring; log preservation

Affected Signer

Immediate self-report; device quarantine; cooperation with investigation

PM

Client communication coordination; timeline tracking; documentation

NO

Break-glass ratification; resource allocation; escalation decisions; insurance notification

GRC Manager

REG-509 entry; regulatory notification coordination; evidence preservation

# 8. KRIs &amp; Metrics

Metric

Target

Measurement

Time to detect key compromise

&lt; 15 min (on-chain); &lt; 4 h (off-chain)

REG-509 timestamps

Time to contain (KC-1)

&lt; 15 min from detection

Incident channel timestamps

Time to full key rotation

&lt; 24 h from confirmation

Key ceremony log timestamps

Break-glass invocations per year

&lt; 2 (indicates strong preventive controls)

REG-509 annual review

Post-incident action item completion

100% within 30 days

PLAN-701 tracking

Annual tabletop exercise completion

1 per year minimum

Exercise report

# 9. Testing &amp; Exercises

Quarterly: tabletop walk-through of KC-1 scenario with KCRT (rotate scenarios: phishing, device theft, insider, supply chain)

Semi-annual: live drill - execute emergency pause on testnet; measure time-to-contain

Annual: full break-glass exercise including credential envelope access and key rotation ceremony

After every real incident: update procedure based on lessons learned within 15 business days

# 10. Control Mapping

Framework

Control

ISO 27001:2022

A.5.26 Response to information security incidents, A.8.24 Use of cryptography

NIST CSF 2.0

RS.MA-01 Incident management, RS.AN-03 Analysis performed, RS.MI-01 Incident contained

NIST SP 800-61 Rev.2

Incident handling: detection, analysis, containment, eradication, recovery

SOC 2

CC7.3 Evaluation of events, CC7.4 Response to incidents

NIST SP 800-57

Key compromise recovery procedures

# Review &amp; Maintenance

Reviewed on a Semi-annual cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

PR-203 Incident Response Procedure

STD-104 Cryptographic Controls Standard

STD-105 Transaction Verification &amp; Simulation Standard

GL-305 Signer OPSEC Guideline

CL-411 Signing Ceremony Checklist

REG-509 Incident Register
