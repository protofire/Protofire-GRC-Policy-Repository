---
id: "CL-411"
title: "Signing Ceremony Checklist"
type: "Checklist"
level: "L5"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Quarterly"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "L1-KEY-005; POL-004 §2.5"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# CL-411 — Signing Ceremony Checklist

## Scope
Checklist for production multisig key generation/transfer ceremonies.

## Pre-Ceremony

| # | Item | Responsible | Verified |
|---|---|---|---|
| 1 | Participants identified (minimum 3 for 2-of-3). No single point of failure. | CISO | ☐ |
| 2 | Clean hardware devices prepared and verified. | TL | ☐ |
| 3 | Ceremony location secured (physical or verified virtual). | CISO | ☐ |
| 4 | Witness designated (independent from signers). | NO | ☐ |

## Ceremony

| # | Item | Responsible | Verified |
|---|---|---|---|
| 5 | Key generation on air-gapped or HSM device. | TL | ☐ |
| 6 | Each signer generates their key independently. | Signers | ☐ |
| 7 | Public keys collected and multisig wallet configured (≥ 2-of-3). | TL | ☐ |
| 8 | Test transaction executed and verified. | DevOps | ☐ |
| 9 | Backup seeds/recovery stored in separate secure locations. | Signers | ☐ |

## Post-Ceremony

| # | Item | Responsible | Verified |
|---|---|---|---|
| 10 | Ceremony record completed: date, participants, wallet address, threshold, witness statement. | CISO | ☐ |
| 11 | Record stored in evidence vault per L1-EVID-004. | GRC-MGR | ☐ |
| 12 | Key rotation schedule set (annual or personnel change). | CISO | ☐ |
