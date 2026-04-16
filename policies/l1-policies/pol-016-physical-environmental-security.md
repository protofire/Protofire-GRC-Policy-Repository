---
id: "POL-016"
title: "Physical and Environmental Security Policy"
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

# POL-016 — Physical and Environmental Security Policy

**Document ID**

POL-016

**Document Title**

Physical &amp; Environmental Security Policy

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

Replaces P-009 (GRC-MASTER-001 v1.0) per GRC-CONC-001

**References**

GRC-PF-001; L1-INFRA-009; POL-002; POL-014; ISO/IEC 27001:2022 A.7.1–A.7.14; NIST CSF 2.0 PR.AC/PR.IP; SOC 2 CC6.4

────────────────────────────────────────────────────────────

## 1. Purpose

This Policy establishes Protofire's requirements for the physical protection of information assets, equipment, and personnel. Given Protofire's distributed workforce model, this Policy focuses on the protection of hardware security devices, secure storage of cryptographic media, and environmental controls for any Protofire-controlled infrastructure.

────────────────────────────────────────────────────────────

## 2. Scope

This Policy applies to: all Protofire office locations (if any); home office environments used by personnel with access to production signing keys or sensitive data; any data centre or co-location facility hosting Protofire-managed infrastructure; storage locations for hardware wallets, HSMs, and cryptographic backup media.

────────────────────────────────────────────────────────────

## 3. Secure Areas

### 3.1 Office facilities

Where Protofire maintains office facilities, physical access controls must include: controlled entry (key card, lock, or biometric); visitor registration and escort requirement; separate secure area for hardware wallet storage and signing ceremonies; clean desk policy for all workstations.

### 3.2 Home office — key holders

Personnel who hold hardware wallets, HSM tokens, or backup seed material at home must: store cryptographic media in a locked safe or security container when not in active use; ensure the home environment is not accessible to unauthorised individuals during signing operations; use a private, secured workspace for all signing ceremonies (video-verified per CL-411 if remote).

────────────────────────────────────────────────────────────

## 4. Equipment Protection

### 4.1 Hardware wallets and HSMs

Hardware security devices must be: inventoried in the Asset Register (REG-502); stored in tamper-evident packaging when not in use; tracked with chain-of-custody records for any transfer between individuals; destroyed or securely wiped before disposal.

### 4.2 Endpoint protection

All Protofire-issued or approved devices must have: disk encryption (FileVault, BitLocker, or LUKS); current operating system with automatic security updates; endpoint detection and response (EDR) software where available; screen lock after maximum 5 minutes of inactivity.

### 4.3 Media disposal

Cryptographic media, hard drives, and any storage containing Protofire or client data must be securely destroyed before disposal per POL-008 retention schedules. Methods: physical destruction for hardware wallets and backup media; secure erase (NIST SP 800-88) for hard drives and SSDs; certificate of destruction for outsourced disposal.

────────────────────────────────────────────────────────────

## 5. Environmental Controls

For any Protofire-controlled data centre or server infrastructure: appropriate fire detection and suppression; UPS and backup power; temperature and humidity monitoring; water leak detection. For fully cloud-hosted operations (Protofire's current model): the CISO must verify that cloud providers maintain equivalent environmental controls as part of the vendor risk assessment under POL-007.

────────────────────────────────────────────────────────────

## 6. Roles and Responsibilities

**Role**

**Responsibility**

CISO

Policy owner. Audits physical security compliance annually. Approves secure area designations.

Node Owner

Ensures key holders comply with home office security requirements. Authorises hardware wallet issuance.

DevOps

Maintains asset inventory for hardware security devices. Executes secure disposal.

All key holders

Comply with cryptographic media storage and handling requirements. Report loss or tampering immediately.

────────────────────────────────────────────────────────────

## 7. Exceptions

Deviations from this Policy are managed under POL-009. No exception may waive the locked storage requirement for production hardware wallets.

────────────────────────────────────────────────────────────

## 8. Review

This Policy is reviewed annually by the CISO and upon any material change to Protofire's office arrangements, infrastructure model, or key management architecture.

────────────────────────────────────────────────────────────

## 9. Approval

**Role**

**Name**

**Signature**

**Date**

CISO

Director of Engineering

CEO

────────────────────────────────────────────────────────────

Document end — POL-016 v1.0
