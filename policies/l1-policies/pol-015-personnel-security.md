---
id: "POL-015"
title: "Personnel Security Policy"
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

# POL-015 — Personnel Security Policy

**Document ID**

POL-015

**Document Title**

Personnel Security Policy

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

Replaces P-008 (GRC-MASTER-001 v1.0) per GRC-CONC-001

**References**

GRC-PF-001; L0-1 GRC Charter; L1-HR-010; L2-ACCESS-203; POL-004; POL-014; ISO/IEC 27001:2022 A.6.1–A.6.6; NIST CSF 2.0 GV.RR; SOC 2 CC1.4

**Subordinate Documents**

PR-206 Access Provisioning Procedure (JML); PR-212 Security Awareness &amp; Training Procedure; CL-412 New Employee Security Onboarding Checklist; CL-405 Access Review Checklist

────────────────────────────────────────────────────────────

## 1. Purpose

This Policy establishes Protofire's requirements for personnel security throughout the employment lifecycle — from pre-engagement screening through onboarding, ongoing employment, and termination. It ensures that individuals with access to Protofire systems and client data meet security and trustworthiness requirements.

────────────────────────────────────────────────────────────

## 2. Scope

This Policy applies to all Protofire employees, contractors, consultants, freelancers, and any third-party personnel granted access to Protofire systems, repositories, or client information.

────────────────────────────────────────────────────────────

## 3. Pre-Engagement Screening

### 3.1 Background verification

Background verification must be conducted for all new hires and contractors before granting access to Protofire systems. Verification scope is proportionate to the role's risk level: standard verification (identity, right to work, reference check) for all roles; enhanced verification (employment history, qualification verification) for roles with access to production signing keys, client funds, or T3/T4 engagement data.

### 3.2 Contractual obligations

All personnel must sign: a confidentiality and non-disclosure agreement before first access; acceptance of this Policy and the Information Security Policy (POL-002); acceptable use terms per POL-012 (when approved).

────────────────────────────────────────────────────────────

## 4. Security Onboarding

### 4.1 Onboarding checklist

All new personnel must complete the Security Onboarding Checklist (CL-412) within 5 business days of start date, covering: security awareness training (§5); MFA configuration on all Protofire systems; access provisioning per POL-004 (least privilege); acknowledgement of incident reporting obligations (POL-017); data protection awareness per POL-011 §14.

### 4.2 Access provisioning

Access is provisioned per the Joiner/Mover/Leaver procedure (PR-206 / L2-ACCESS-203). Access must be role-scoped, time-limited where appropriate, and documented in the access management system.

────────────────────────────────────────────────────────────

## 5. Security Awareness and Training

### 5.1 Mandatory training

All personnel must complete security awareness training within 30 days of joining and annually thereafter. Training content must cover: information security principles and this Policy; phishing and social engineering recognition; secure coding practices (for engineering roles); key management and handling of secrets; incident reporting obligations; data protection and privacy (POL-011); Web3-specific threats (private key phishing, governance attacks, front-end injection).

### 5.2 AI-Enabled Social Engineering Awareness

All personnel must receive specific training on AI-enabled attack vectors at onboarding and annually thereafter. Training must explicitly cover:

**Voice cloning / deepfake audio**: Attackers can synthesise the voice of a colleague, manager, or client to request urgent action (signing, fund transfer, credential sharing). Treat any unexpected voice-only request for security-sensitive actions as unverified until confirmed via an independent second channel.

**Video deepfake**: Real-time video calls may use deepfake technology to impersonate known individuals. A video call alone is not sufficient verification of identity for any signing or access-granting action.

**AI-generated phishing**: LLM-crafted messages are indistinguishable from genuine communication by grammar and tone alone. Apply out-of-band verification regardless of message quality or apparent sender authenticity.

**Verification protocol**: Any request for a signing action, credential change, fund movement, or access grant received via Slack, Telegram, email, voice, or video — regardless of apparent sender — must be verified via an independent channel before action is taken. This applies even if the requestor appears to be a named Protofire colleague.

**Challenge word programme**: Personnel with signing authority or privileged system access must maintain a shared challenge word with at least one trusted peer, rotated quarterly, for use when authenticity of a request is in doubt. Challenge words must not be transmitted via the same channel as the request being challenged.

Training completion is recorded per L1-EVID-004. Completion is a prerequisite for signing authority and privileged access provisioning.

### 5.3 Role-specific training

Personnel in security-sensitive roles (TL, DevOps, signers) must complete additional role-specific training on: signing ceremony procedures (CL-411); deployment runbook execution; monitoring and alerting configuration; incident response procedures for their role.

### 5.3 Evidence

Training completion is recorded per L1-EVID-004 and the Evidence Calendar. Training records are retained for the duration of employment plus 2 years.

────────────────────────────────────────────────────────────

## 6. During Employment

### 6.1 Access reviews

Access rights must be reviewed quarterly per CL-405 (Access Review Checklist). Access must be adjusted immediately upon role change (Mover procedure in PR-206). Dormant accounts (no login for 60 days) must be investigated and disabled if no longer required.

### 6.2 Security responsibilities

All personnel are responsible for: protecting credentials and not sharing them; reporting security incidents within 4 hours (POL-017); following secure development practices; complying with all applicable GRC policies.

────────────────────────────────────────────────────────────

## 7. Termination and Role Change

### 7.1 Offboarding

Upon termination or contract end, all access must be revoked within 1 business day per POL-004 §2.2 and PR-206. This includes: source code repositories; cloud infrastructure accounts; secrets vault access; signing key access (production keys must be rotated if the departing individual was a signer); ClickUp and Google Workspace access; VPN and remote access.

### 7.2 Exit obligations

Departing personnel must: return all Protofire equipment and media; confirm deletion of any Protofire data from personal devices; acknowledge ongoing confidentiality obligations.

────────────────────────────────────────────────────────────

## 8. Disciplinary Process

Violation of this Policy or any subordinate security policy may result in: mandatory remediation and re-training; formal warning; suspension of system access; termination of employment or contract; legal action for criminal conduct.

────────────────────────────────────────────────────────────

## 9. Exceptions

Deviations from this Policy are managed under POL-009. No exception may waive the pre-engagement screening requirement for roles with access to production signing keys.

────────────────────────────────────────────────────────────

## 10. Review

This Policy is reviewed annually by the CISO and upon any material change to employment law, Protofire's workforce model, or security requirements.

────────────────────────────────────────────────────────────

## 11. Approval

**Role**

**Name**

**Signature**

**Date**

CISO

Director of Engineering

Node Owner

────────────────────────────────────────────────────────────

Document end — POL-015 v1.0
