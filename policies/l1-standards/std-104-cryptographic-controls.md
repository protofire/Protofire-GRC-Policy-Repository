---
id: "STD-104"
title: "Cryptographic Controls Standard"
type: "Standard"
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

# STD-104 — Cryptographic Controls Standard

Cryptographic Controls Standard

# 0. Document Control

Attribute

Value

Document ID

STD-104

Title

Cryptographic Controls Standard

Hierarchy Level

L2 -- Standard

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

CISO / Technical Lead

Approver

Node Owner

Classification

Confidential -- Internal

Supersedes

—

References

POL-002 Information Security Policy; L1-KEY-005 Cryptographic Controls Policy; ISO 27001:2022 A.8.24; NIST SP 800-57; FIPS 140-3

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

STD-104 defines the mandatory cryptographic algorithms, key lengths, key management practices and implementation requirements for all Protofire systems and client engagements. In blockchain engineering, cryptographic controls are foundational -- a single key compromise can result in immediate, irreversible financial loss.

# 2. Scope

Applies to: all encryption at rest and in transit, digital signatures, hashing, key generation, key storage, key rotation, certificate management, smart-contract signing keys, multi-sig configurations, and any system where cryptographic operations protect Protofire or client assets.

# 3. Approved Algorithms

Use Case

Approved Algorithm(s)

Minimum Key Length / Parameters

Symmetric encryption

AES-256-GCM, ChaCha20-Poly1305

256-bit key; 96-bit nonce (GCM), 256-bit key (ChaCha20)

Asymmetric encryption

RSA-OAEP, ECIES (secp256k1, P-256)

RSA ≥ 3072-bit; ECC ≥ 256-bit

Digital signatures

ECDSA (secp256k1), EdDSA (Ed25519), RSA-PSS

ECC ≥ 256-bit; RSA ≥ 3072-bit

Hashing

SHA-256, SHA-3-256, Keccak-256 (Ethereum)

256-bit output minimum

Password hashing

Argon2id, bcrypt, scrypt

Argon2id: memory ≥ 64 MB, iterations ≥ 3, parallelism ≥ 4

Key derivation

HKDF-SHA256, PBKDF2-SHA256

PBKDF2: ≥ 600,000 iterations

TLS

TLS 1.2+ (prefer 1.3)

Forward-secrecy cipher suites only (ECDHE)

Smart-contract signing

ECDSA secp256k1 (Ethereum standard)

256-bit; hardware wallet or HSM required for mainnet

# 4. Prohibited Algorithms

MD5, SHA-1 -- deprecated; collision-vulnerable

DES, 3DES, RC4, Blowfish -- insufficient key length or known weaknesses

RSA &lt; 2048-bit -- factorable with current hardware

CBC mode without authenticated encryption (HMAC) -- padding oracle vulnerable

TLS 1.0, TLS 1.1, SSLv3 -- deprecated protocols

Custom/proprietary cryptographic algorithms -- not permitted under any circumstances

# 5. Key Management

## 5.1 Key Generation

Keys must be generated using CSPRNG (cryptographically secure pseudo-random number generator)

Hardware entropy source required for mainnet signing keys (HSM, hardware wallet, or secure enclave)

Key generation for production must occur on air-gapped or hardened systems

## 5.2 Key Storage

Mainnet private keys: hardware wallet (Ledger, Trezor) or HSM -- never in plaintext on disk or in environment variables

Service account keys: encrypted at rest using envelope encryption (KMS-wrapped)

API keys and tokens: secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager) -- never in source code

Backup keys: encrypted, stored in physically separate location; access requires dual-control

## 5.3 Key Rotation

Key Type

Rotation Cadence

Procedure

TLS certificates

Annual or on compromise

Automated via ACME/Let&apos;s Encrypt or PKI; 30-day advance renewal

Service account keys

90 days

Automated rotation via secrets manager; old key valid for 48 h overlap

API tokens

90 days or on compromise

Regenerate and update all consumers; log in REG-508

Smart-contract admin keys

Per engagement lifecycle

Key ceremony documented; handover at project close (Phase 10-11)

Encryption keys (at rest)

Annual

Re-encryption with new key; old key retained for decryption only

## 5.4 Key Destruction

Retired keys must be securely destroyed using NIST SP 800-88 equivalent (cryptographic erase for HSM, secure wipe for software keys)

Destruction must be witnessed (two-person rule) and logged in REG-508

Backup copies must be destroyed simultaneously

# 6. Multi-Signature Requirements

For smart contracts managing client or treasury funds:

Minimum 3-of-5 multi-sig for treasury operations above $10,000 equivalent

Minimum 2-of-3 multi-sig for admin operations (upgrades, parameter changes)

Signers must be on separate devices, in separate physical locations where feasible

Signer set composition and thresholds documented in engagement security posture document

Changes to signer set require timelock (minimum 48 h) with on-chain announcement

# 7. Control Mapping

Framework

Control

ISO 27001:2022

A.8.24 Use of cryptography

NIST SP 800-57

Key management lifecycle

NIST CSF 2.0

PR.DS-01 Data-at-rest, PR.DS-02 Data-in-transit

SOC 2

CC6.1 Logical access, CC6.7 Encryption

FIPS 140-3

Cryptographic module validation (where applicable)

PCI DSS v4.0

Req 3.5 Key management, Req 4.2 Strong cryptography in transit

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

L1-KEY-005 Cryptographic Controls Policy

POL-002 Information Security Policy

STD-101 Identity &amp; Access Management Standard

REG-508 Access Review Register
