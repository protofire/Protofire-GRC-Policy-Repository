---
id: "STD-105"
title: "Transaction Verification and Simulation Standard"
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

# STD-105 — Transaction Verification and Simulation Standard

Transaction Verification &amp; Simulation Standard

# 0. Document Control

Attribute

Value

Document ID

STD-105

Title

Transaction Verification &amp; Simulation Standard

Hierarchy Level

L2 - Standard

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-16

Review Cycle

Annual

Owner

Technical Lead / CISO

Approver

Node Owner

Classification

Confidential - Internal

Supersedes

—

References

STD-103 Secure Development Standard; STD-104 Cryptographic Controls Standard; POL-005 Change Management Policy; CL-PHASE-001; OWASP Smart Contract Top 10

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

STD-105 mandates that every on-chain transaction signed by Protofire personnel must be decoded, verified, and simulated before signing. The Drift Protocol breach demonstrated that well-audited smart contracts can still be exploited through access and execution layer weaknesses. This standard ensures signers understand exactly what they are signing and confirms the expected outcome before broadcast.

# 2. Scope

Applies to every on-chain transaction where Protofire holds signing authority:

Contract deployments (create transactions)

Multi-sig proposal submissions and confirmations

Admin function calls (pause, upgrade, parameter change, role grant)

Treasury and fund movements

Proxy upgrades and implementation changes

Timelock queue and execute operations

Any transaction requiring a Protofire-held private key on mainnet

Testnet transactions are exempt from full simulation but must still be decoded and reviewed.

# 3. Decode-Before-Sign Protocol

No signer shall approve a transaction without completing all steps of the Decode-Before-Sign (DBS) protocol:

## 3.1 Step 1 - Transaction Decoding

Decode the raw transaction calldata against the verified contract ABI

Produce a human-readable summary showing: target contract address, function name, all parameter values with labels

For proxy contracts: decode against the implementation ABI, not the proxy ABI

Tool requirement: use a verified decoder (Tenderly, Etherscan, Safe Transaction Service, or internal tooling) - never rely solely on the proposer\&apos;s description

If calldata cannot be decoded against a verified ABI, the transaction MUST NOT be signed (HS-08 equivalent)

## 3.2 Step 2 - Parameter Verification

Compare every decoded parameter against the expected values documented in the change request (REG-504)

For address parameters: verify against known address registry (not just visual inspection - full address match)

For numeric parameters: verify units, decimals, and magnitude (e.g., confirm whether value is in wei or ether)

For role/access parameters: verify the target identity and confirm the permission change is authorised

For upgrade parameters: verify the new implementation address matches the audited deployment

Any parameter mismatch: STOP. Do not sign. Escalate to TL.

## 3.3 Step 3 - Transaction Simulation

Simulate the transaction against a mainnet fork using Tenderly, Foundry fork, or equivalent

Simulation must show: state changes, token transfers, event emissions, gas consumption

Compare simulation output against expected outcomes documented in the change request

Check for unexpected state changes: balance changes in unrelated contracts, unexpected event emissions, excessive gas

For multi-step operations (e.g., timelock queue then execute): simulate the full sequence, not just individual steps

## 3.4 Step 4 - Signer Attestation

Each signer records their verification in the Transaction Verification Log (TVL):

TVL fields: Transaction hash/nonce, Contract address, Function called, Parameters (decoded), Simulation link (Tenderly URL or equivalent), Expected vs. actual outcome, Signer identity, Timestamp, Approval decision (SIGN / REJECT / ESCALATE).

The TVL entry must be created BEFORE the signer submits their signature

For multi-sig: each signer independently completes DBS - no signer may rely on another signer\&apos;s verification

# 4. Simulation Requirements by Transaction Type

Transaction Type

Minimum Simulation

Additional Checks

Contract deployment

Full deployment simulation; verify bytecode matches compiled artifact

Verify constructor parameters; check initial state; confirm verification on explorer

Proxy upgrade

Simulate upgrade + one critical function call post-upgrade

Storage layout compatibility check; verify no storage collisions; confirm proxy admin unchanged

Treasury movement

Simulate full transfer; verify destination and amount

Confirm destination is in approved address registry; verify no intermediate routing

Parameter change

Simulate with new parameter; verify system behaviour within expected bounds

Check boundary conditions; simulate with extreme values to confirm no overflow/underflow

Pause / Unpause

Simulate; verify correct functions are paused/unpaused

Confirm pause scope matches intent (full pause vs. selective)

Role grant / revoke

Simulate; verify role membership before and after

Confirm no privilege escalation path created; verify SoD maintained

Timelock operations

Simulate queue + execute; verify delay and target match

Confirm timelock delay meets STD-104 minimums; verify no bypass

# 5. Tooling Requirements

## 5.1 Approved Simulation Tools

Tool

Use Case

Configuration Requirement

Tenderly

Primary simulation and monitoring platform

Mainnet fork; project-specific alerts; team access configured

Foundry (cast/forge)

Developer-level simulation and testing

Mainnet fork via --fork-url; script-based verification

Safe Transaction Service

Multi-sig transaction decoding and simulation

Connected to Tenderly for simulation; all signers have UI access

OpenZeppelin Defender

Automated transaction proposals and monitoring

Relayer configured; approval workflow matches RACI

Etherscan/Blockscout

Contract verification and calldata decoding

Verified source code for all deployed contracts

## 5.2 Internal Tooling

Transaction Verification Log (TVL) - spreadsheet or database tracking all verified transactions

Address Registry - authoritative list of known contract addresses, EOAs, and multi-sigs with labels

ABI Repository - version-controlled collection of verified ABIs for all deployed contracts

Automated pre-sign checks (CI integration or Safe module) that block signing without simulation link

# 6. Prohibited Practices

Blind signing - signing a transaction based solely on the proposer\&apos;s description without independent decoding

Screenshot verification - using screenshots of decoded data instead of live decoding

Single-signer verification - in a multi-sig, relying on one signer\&apos;s DBS instead of independent verification per signer

Stale simulation - using simulation results older than 1 hour for mainnet transactions (state may have changed)

Unverified contracts - signing transactions targeting contracts without verified source code on a block explorer

Signing under pressure - any signer may invoke a 30-minute cooling period without justification; urgency does not override verification

# 7. Exception: Emergency Transactions

During a confirmed KC-1 (key compromise) incident per PR-208:

Emergency pause may bypass full simulation if delay &gt; 5 min would result in fund loss

The pause transaction must still be decoded (Step 1 of DBS) - only simulation (Step 3) may be deferred

Post-hoc simulation and TVL entry must be completed within 1 hour

All other emergency transactions (fund rescue, key rotation) require full DBS protocol

# 8. Roles &amp; Responsibilities

Role

Responsibility

TL

Maintain ABI repository and address registry; train signers on DBS; review TVL weekly; define simulation scripts

Each Signer

Complete full DBS independently for every transaction; record TVL entry; REJECT if any step fails

DevOps

Maintain simulation infrastructure (Tenderly project, fork nodes); automate pre-sign checks

CISO

Audit TVL monthly; investigate any gaps or anomalies; enforce prohibited practices

GRC Manager

Include TVL completeness in quarterly compliance review; report to CISO

# 9. KRIs &amp; Metrics

Metric

Target

Measurement

DBS completion rate

100% of mainnet transactions

TVL records vs. on-chain transactions

Rejected transactions (DBS failures)

Track trend; no target (rejections are healthy)

TVL REJECT entries

Mean DBS completion time

&lt; 30 min for standard transactions

TVL timestamps

Simulation tool uptime

&gt; 99.5%

Tenderly/tool availability logs

Address registry currency

Updated within 24 h of new deployment

Registry audit vs. deployment records

# 10. Control Mapping

Framework

Control

ISO 27001:2022

A.8.24 Use of cryptography, A.8.25 Secure development lifecycle, A.8.32 Change management

NIST CSF 2.0

PR.DS-01 Data-at-rest protected, PR.DS-02 Data-in-transit protected, ID.RA-01 Vulnerabilities identified

SOC 2

CC8.1 Change management, CC6.1 Logical access

OWASP Smart Contract Top 10

SC01 Reentrancy, SC04 Access Control, SC09 Gas Limit

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

STD-103 Secure Development Standard

STD-104 Cryptographic Controls Standard

PR-208 Key Compromise Response Procedure

POL-005 Change Management Policy

REG-504 Change &amp; Release Register
