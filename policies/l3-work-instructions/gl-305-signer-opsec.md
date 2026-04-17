---
id: "GL-305"
title: "Signer OPSEC Guideline"
type: "Guideline"
level: "L3"
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

# GL-305 — Signer OPSEC Guideline

Signer Operational Security (OPSEC) Guideline

# 0. Document Control

Attribute

Value

Document ID

GL-305

Title

Signer Operational Security (OPSEC) Guideline

Hierarchy Level

L3 - Guideline

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

STD-104 Cryptographic Controls Standard; STD-105 Transaction Verification Standard; PR-208 Key Compromise Response Procedure; POL-003 Access Control Policy; NIST SP 800-63B

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

GL-305 provides operational security guidance for every individual who holds signing authority over on-chain assets or admin functions in Protofire engagements. The Drift Protocol breach and similar incidents demonstrated that well-audited contracts are compromised through the human and operational layer - phishing, social engineering, device compromise, and poor key hygiene. This guideline addresses that attack surface directly.

# 2. Audience

All multi-sig signers on client engagements

Technical Leads with deployment authority

DevOps engineers with deployer role

Any Protofire personnel holding keys to mainnet contracts or treasury wallets

Contractors and sub-processors with signing authority (must acknowledge this guideline in writing)

# 3. Device Security

## 3.1 Hardware Wallet Hygiene

Use only approved hardware wallets: Ledger Nano X/S Plus, Trezor Model T/Safe 3, or GridPlus Lattice1

Purchase hardware wallets only from official manufacturer channels - never second-hand, never from Amazon/eBay

Verify device authenticity upon receipt using manufacturer\&apos;s verification procedure before first use

Never connect a hardware wallet to a device you do not fully control

Store hardware wallet in a secure location when not in active use - not in an unlocked desk drawer

Report lost or stolen hardware wallets within 1 hour to CISO and TL (triggers PR-208 KC-2 assessment)

Do not use a signing hardware wallet for personal transactions or DeFi activity

## 3.2 Signing Device (Computer)

Use a dedicated device or user profile for signing operations - not your daily browsing/email machine if possible

Full-disk encryption enabled (FileVault, BitLocker, LUKS)

OS and browser auto-update enabled; defer no longer than 48 hours

Browser: use a dedicated browser profile for signing with minimal extensions (only wallet connector)

No browser extensions besides the wallet connector on the signing profile - especially no &quot;productivity&quot; or &quot;crypto&quot; extensions

Antivirus / EDR active and updating; no exceptions for signing device

Screen lock timeout: 5 minutes maximum; require password on wake

Never use public Wi-Fi for signing operations; use VPN or mobile hotspot if away from trusted network

## 3.3 Seed Phrase / Recovery Security

Write seed phrase on metal backup (Cryptosteel, Billfodl) - not paper, not digital file, not screenshot

Store seed backup in a physically secure location separate from the hardware wallet (different building or safe deposit box)

Never type, photograph, screenshot, or digitally store the seed phrase

Never share seed phrase with anyone, including Protofire colleagues, IT support, or hardware wallet manufacturer

If seed phrase may have been exposed: immediately rotate to new key per PR-208 Phase 4

# 4. Phishing &amp; Social Engineering Resistance

## 4.1 Common Attack Vectors

Fake Safe/multi-sig UI: attacker creates a lookalike Safe interface that presents a malicious transaction for signing

Urgent Slack/Telegram DM: &quot;we need to execute an emergency transaction NOW&quot; - urgency is the primary social engineering lever

Fake governance proposal: legitimate-looking proposal that includes a malicious embedded transaction

Compromised colleague: attacker gains access to a team member\&apos;s account and requests signing through normal channels

Supply chain: malicious dependency in a signing tool or SDK that modifies transaction parameters

Address poisoning: dust transactions from addresses visually similar to known addresses, hoping signer copies from history

**AI voice clone** (DPRK/nation-state pattern): attacker synthesises the voice of a TL, colleague, or client to request an urgent signing operation via phone call or voice message. The cloned voice is indistinguishable from genuine voice without a challenge word. Incident precedent: $100K Zerion employee funds lost to DPRK-linked AI voice attack (2025).

**AI video deepfake**: real-time deepfake video call impersonates a known individual to create false urgency for a signing action. A live video call is not sufficient proof of identity — require the challenge word.

**Fake hardware wallet / malicious firmware**: counterfeit Ledger or Trezor devices, or manipulated firmware updates distributed via unofficial channels, silently modify transaction parameters before hardware signing. Incident precedent: KuCoin fake Ledger app used to launder $9.5M+ (2025).

## 4.2 Defence Practices

ALWAYS access signing interfaces via bookmarked URLs - never via links in messages, emails, or search results

ALWAYS verify the transaction on your hardware wallet display matches the decoded parameters (STD-105 DBS)

NEVER sign under time pressure alone - invoke the 30-minute cooling period (STD-105 section 6) if pressured

VERIFY out-of-band: if a colleague requests an urgent signature, confirm via a separate channel (phone call, in-person, different app)

CHECK contract addresses against the authoritative Address Registry - not from the requesting message

REPORT all suspected phishing to CISO within 30 minutes, even if you did not click/sign

**USE the challenge word**: any signing request received via voice call, voice message, or video call must be authenticated with the pre-agreed challenge word before action is taken — a recognised voice or face is not sufficient

**REJECT signing requests via voice alone**: always require written confirmation in an authorised channel (ClickUp task or signed Slack message from the requesting party) before signing based on a voice/video request

**VERIFY hardware wallet firmware** before any signing session if the device has been out of your direct custody; check firmware version against official manufacturer release notes; if in doubt, factory-reset and re-provision

# 5. Operational Practices

## 5.1 Before Every Signing Session

Verify you are on the correct URL (bookmark, not link)

Verify the multi-sig address matches the engagement\&apos;s known safe address

Complete the full Decode-Before-Sign protocol per STD-105

Confirm the transaction was proposed through an authorised channel (not a surprise)

Check that the expected number of other signers have already verified (for sequential signing flows)

## 5.2 During Signing

Read every field on the hardware wallet display - do not just click &quot;confirm&quot;

Verify: target address, function name (if displayed), value, chain ID

If the hardware wallet shows a raw hex data hash that you cannot verify against decoded parameters: DO NOT SIGN

One transaction at a time - do not batch-approve without individual verification

## 5.3 After Signing

Confirm the transaction landed on-chain with expected parameters (block explorer verification)

Record your TVL entry per STD-105 section 3.4

Monitor for expected state changes (Tenderly alerts)

Disconnect hardware wallet from device

# 6. Travel &amp; Remote Signing

Notify TL and CISO before international travel if you are an active signer on a live engagement

Do not carry hardware wallet through airport security X-ray if avoidable - hand inspection is preferred

Do not sign from hotel business centre computers or shared devices under any circumstances

If signing authority is needed while travelling, consider temporary delegation to a deputy signer (requires TL + CISO approval and key ceremony)

Border crossing: be aware that devices may be inspected; ensure full-disk encryption is active and device is powered off

# 7. Signer Rotation Triggers

A signer must be rotated from the multi-sig set when any of the following occurs:

Personnel departure from Protofire or removal from engagement - rotate within 24 h

Hardware wallet loss or theft - immediate rotation (PR-208 KC-2)

Confirmed phishing click or malware exposure on signing device - immediate rotation

Extended unavailability (&gt; 2 weeks) with no deputy signer arrangement

Role change removing signing responsibility

Failure to complete quarterly OPSEC refresher training

Any violation of section 6 (Prohibited Practices in STD-105) or this guideline\&apos;s requirements

# 8. Fund Movement Monitoring

All signers should have personal notification alerts configured for the multi-sigs they participate in

Recommended: Tenderly alerts to personal email + mobile push for any transaction from monitored addresses

Any unexpected transaction notification - report to TL and CISO immediately (triggers PR-208 triage)

Weekly: review on-chain activity for all multi-sigs you participate in; flag any transaction you did not verify

# 9. Training &amp; Compliance

Requirement

Frequency

Verification

OPSEC onboarding briefing

Before first signing authority

TL-delivered briefing; signed acknowledgement

DBS protocol hands-on training

Before first signing authority

Supervised testnet exercise; pass/fail

Phishing simulation exercise

Quarterly

GRC-managed; results tracked in REG-507

OPSEC refresher

Semi-annual

Updated scenarios; signed re-acknowledgement

Incident response tabletop

Annual

KC-1 scenario participation; PR-208 familiarity

# 10. Acknowledgement

Every individual granted signing authority must sign the following acknowledgement before receiving key material:

&quot;I have read, understood, and agree to comply with GL-305 Signer OPSEC Guideline v1.0. I understand that violation of these guidelines may result in immediate revocation of signing authority, incident investigation per PR-208, and disciplinary action per L1-HR-010. I will report any suspected compromise, phishing attempt, or guideline violation to the CISO within 30 minutes.&quot;

Signed: ____________________  Name: ____________________  Date: ____________________  Engagement: ____________________

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

STD-104 Cryptographic Controls Standard

STD-105 Transaction Verification &amp; Simulation Standard

PR-208 Key Compromise Response Procedure

POL-003 Access Control Policy

CL-411 Signing Ceremony Checklist

REG-507 Training &amp; Awareness Register
