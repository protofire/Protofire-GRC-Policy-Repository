---
id: "POL-014"
title: "Cryptographic Controls Policy"
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

# POL-014 — Cryptographic Controls Policy

**Document ID**

POL-014

**Document Title**

Cryptographic Controls Policy

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

Replaces P-007 (GRC-MASTER-001 v1.0) per GRC-CONC-001

**References**

GRC-PF-001; L0-1 GRC Charter; L1-KEY-005; S-103; POL-004; ISO/IEC 27001:2022 A.8.24; NIST CSF 2.0 PR.DS-1/PR.DS-2; SOC 2 CC6.1/CC6.7

**Subordinate Documents**

S-103 Encryption &amp; Key Management Standard; PR-211 Signing Ceremony Procedure; CL-411 Signing Ceremony Checklist

────────────────────────────────────────────────────────────

## 1. Purpose

This Policy establishes Protofire's requirements for the use of cryptographic controls to protect the confidentiality, integrity, and authenticity of information. It addresses both traditional IT cryptography and Web3-specific key management for blockchain operations, treasury custody, and smart contract administration.

────────────────────────────────────────────────────────────

## 2. Scope

This Policy applies to: all encryption of data at rest and in transit across Protofire systems; all private key material used for blockchain signing, multisig operations, and smart contract administration; all API keys, tokens, and credentials used in development and production environments; all certificate management for TLS/SSL and code signing.

────────────────────────────────────────────────────────────

## 3. Cryptographic Standards

### 3.1 Encryption at rest

All sensitive data at rest must be encrypted using AES-256 or equivalent. Database encryption, disk encryption, and backup encryption are mandatory for all systems processing client or personal data.

### 3.2 Encryption in transit

All data in transit must be encrypted using TLS 1.2 or higher. TLS 1.0 and 1.1 are prohibited. Certificate pinning is recommended for API integrations with critical third-party services.

### 3.3 Hashing

Password hashing must use bcrypt, scrypt, or Argon2id with appropriate work factors. SHA-256 or SHA-3 are the minimum acceptable hash functions for integrity verification. MD5 and SHA-1 are prohibited for any security purpose.

────────────────────────────────────────────────────────────

## 4. Key Management

### 4.1 Key lifecycle

All cryptographic keys must follow a managed lifecycle: generation, distribution, storage, rotation, revocation, and destruction. Key lifecycle procedures are defined in S-103 and L1-KEY-005.

### 4.2 Private key protection

Private keys used for blockchain signing must be stored in hardware security modules (HSMs), hardware wallets, or MPC (multi-party computation) wallet solutions. Software-only key storage is prohibited for production signing keys. This requirement is enforced at Gate G4 (admin/control matrix) and the Irreversibility Gate (Phase 9).

### 4.3 Multisig and timelock requirements

All production smart contract admin functions must be protected by multisig (minimum M-of-N where M ≥ 2 and N ≥ 3) with timelock (minimum 24 hours for non-emergency operations). Single-key admin access to production contracts is classified as ADMIN-01 risk and requires explicit risk acceptance per POL-009.

### 4.4 Key rotation

Infrastructure credentials and API keys must be rotated at least every 90 days. Blockchain signing keys are rotated when: a signer leaves the organisation; a key compromise is suspected; or the annual review identifies rotation as necessary.

### 4.5 Secrets management

All secrets (API keys, credentials, tokens) must be stored in a secrets vault (HashiCorp Vault, AWS Secrets Manager, or equivalent). Hard-coded secrets in source code are prohibited. .env files must be git-ignored. Secret scanning must be active in all repositories (per P4-TL-001 security baseline).

────────────────────────────────────────────────────────────

## 5. Signing Ceremonies

### 5.1 Requirement

All production multisig key generation, key replacement, and critical on-chain transactions (initial deployment, upgrade execution, emergency pause) must follow the Signing Ceremony Procedure (PR-211) using the Signing Ceremony Checklist (CL-411).

### 5.2 Two-person rule

All production signing operations require the two-person rule: TL (Approver) and DevOps (Deployer) as defined in the CL-PHASE-001 deployment runbook. No single individual may both approve and execute a production signing operation.

### 5.3 Key custody transfer

At project close-out (Phase 10/12), key custody must be formally transferred to the client with documented acceptance. Protofire must revoke all signing access within 1 business day of handover per POL-004 §2.2.

────────────────────────────────────────────────────────────

## 6. Certificate Management

TLS/SSL certificates must be tracked in an inventory, renewed before expiry (minimum 30 days advance), and provisioned from trusted Certificate Authorities. Wildcard certificates are permitted but must be stored with the same protections as private keys.

────────────────────────────────────────────────────────────

## 7. Roles and Responsibilities

**Role**

**Responsibility**

CISO

Policy owner. Approves cryptographic standards. Reviews key management compliance.

TL

Implements cryptographic controls in delivery. Leads signing ceremonies (Approver role).

DevOps

Manages secrets vault, certificate inventory, and CI/CD secret scanning. Executes signing ceremonies (Deployer role).

Node Owner

Approves key custody transfer at project close-out. Co-signs Irreversibility Gate.

────────────────────────────────────────────────────────────

## 8. Exceptions

Deviations from this Policy are managed under POL-009. No exception may permit single-key admin access to production contracts without CISO + Node Owner written risk acceptance (E3 classification).

────────────────────────────────────────────────────────────

## 9. Review

This Policy is reviewed annually by the CISO and upon any material change to cryptographic standards, blockchain protocols, or Protofire's key management infrastructure.

────────────────────────────────────────────────────────────

## 10. Approval

**Role**

**Name**

**Signature**

**Date**

CISO

Director of Engineering

Node Owner

────────────────────────────────────────────────────────────

Document end — POL-014 v1.0
