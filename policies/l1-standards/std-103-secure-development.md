---
id: "STD-103"
title: "Secure Development Standard"
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

# STD-103 — Secure Development Standard

Secure Development Standard

# 0. Document Control

Attribute

Value

Document ID

STD-103

Title

Secure Development Standard

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

Node Owner / DoE

Classification

Confidential -- Internal

Supersedes

—

References

POL-004 Secure SDLC Policy; POL-005 Change Management Policy; ISO 27001:2022 A.8.25-A.8.33; NIST CSF 2.0 PR.DS; OWASP Top 10 2021; OWASP Smart Contract Top 10

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

STD-103 establishes the mandatory security controls for all software and smart-contract development activities at Protofire. It translates POL-004 (Secure SDLC) policy requirements into actionable technical standards that developers, auditors and reviewers must follow.

# 2. Scope

Applies to all code produced by or for Protofire: client project smart contracts, internal tooling, CI/CD scripts, infrastructure-as-code, and contributions to open-source projects under Protofire&apos;s name. Covers Solidity, Rust, TypeScript, Go and any other language used in production.

# 3. Secure Coding Requirements

## 3.1 General

All code must pass SAST (static analysis) in CI before merge -- zero Critical/High findings permitted

Secret detection scanning enabled on all repositories (pre-commit hook + CI)

Dependency scanning (SCA) on every build; known Critical CVEs block merge

No hardcoded secrets, private keys, or credentials in source code (HS-02 equivalent)

Input validation on all external interfaces; output encoding on all rendered content

## 3.2 Smart Contract Specific

Solidity: use latest stable compiler; enable all warnings; pragma locked to specific version

Reentrancy guards (checks-effects-interactions pattern or OpenZeppelin ReentrancyGuard) on all external calls

Access control: OpenZeppelin AccessControl or Ownable2Step; no unprotected admin functions

Upgradeability: UUPS or Transparent Proxy only; initializer protection; storage gap reserved

Integer arithmetic: Solidity 0.8+ built-in overflow checks; explicit SafeMath for assembly blocks

Flash-loan resistance: time-weighted oracle prices; multi-block confirmation for critical operations

Gas optimisation must not compromise security (documented trade-off required for any security-affecting gas optimisation)

## 3.3 Code Review

All production code requires minimum 2 reviewers, at least 1 with security competency

Smart contracts: TL must be one reviewer; threat model review tag required

Review checklist: OWASP Top 10 + OWASP Smart Contract Top 10 + project-specific threat model

Force pushes and branch protection bypass require CISO notification within 24 h

# 4. Testing Requirements

## 4.1 Minimum Coverage

Test Type

Threshold

Tool Examples

Unit tests

≥ 90% line coverage

Hardhat, Foundry, Jest

Integration tests

All cross-contract interactions

Hardhat mainnet fork, Tenderly

Fuzz testing

≥ 10,000 runs per critical function

Echidna, Foundry fuzz

Property / Invariant tests

All protocol invariants documented in threat model

Echidna, Certora (if licensed)

Slither (SAST)

Zero Critical/High; Medium documented

Slither v0.10+

Secret scanning

Zero findings

Gitleaks, TruffleHog

Dependency scan

Zero Critical CVE

Snyk, npm audit, cargo audit

## 4.2 Pre-Deployment Testing

Testnet deployment mandatory before mainnet (per CL-PHASE-001 Phase 7)

Monitoring validation on testnet: all alerts must fire correctly before mainnet (per STD-102)

Economic simulation for DeFi protocols: edge cases for liquidity, oracle failure, flash loan

# 5. Deployment Controls

Two-person rule: TL authorises, DevOps executes (per CL-PHASE-001 Phase 8)

Deployment runbook required for every mainnet deployment; signed by TL + DevOps

Change classification per POL-005: C1-C5; C4/C5 require NO approval

Rollback plan documented and tested before deployment execution

Post-deployment verification checklist: contract verification on explorer, monitoring active, admin keys secured

# 6. Control Mapping

Framework

Control

ISO 27001:2022

A.8.25 Secure development lifecycle, A.8.26 Application security requirements, A.8.28 Secure coding, A.8.29 Security testing, A.8.31 Separation of environments, A.8.32 Change management, A.8.33 Test information

NIST CSF 2.0

PR.DS-01 Data-at-rest protected, PR.DS-02 Data-in-transit protected, ID.AM-08 Software inventory

SOC 2

CC8.1 Change management, CC7.1 Intrusion detection

OWASP

Top 10 2021; Smart Contract Top 10 2025

CIS Controls v8

16.1 Secure software development, 16.2 Software development lifecycle

# 7. Exceptions

Deviation from any mandatory requirement (e.g., reduced fuzz runs for time-critical hotfix) requires POL-009 E2+ exception with TL + CISO co-sign. Hotfix exceptions are valid for 7 days, after which full compliance must be restored or a permanent exception raised to E3.

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

POL-004 Secure SDLC Policy

POL-005 Change Management Policy

CL-PHASE-001 Client Engagement Lifecycle

STD-102 Logging &amp; Monitoring Standard

REG-504 Change &amp; Release Register
