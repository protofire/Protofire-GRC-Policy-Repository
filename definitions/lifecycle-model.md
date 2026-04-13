# Lifecycle Model Reconciliation

> Source-of-Truth: GRC-PF-001 §Lifecycle Model Reconciliation
> Authoritative Model: 12-Step
> Last-Updated: 2026-04-08

| Step | 12-Step (Authoritative) | 8-Stage Gate | 5-Phase Group | Classification |
|---|---|---|---|---|
| 1 | Assessment | G1 — Intake & Rating | Phase 1 — Project Assessment | PRE-SALES |
| 2 | Proposal | G1 — Intake & Rating | Phase 1 — Project Assessment | PRE-SALES |
| 3 | MSA & Onboarding | G2 — Commercial Structuring | Phase 2 — Commercial & Legal | PRE-SALES |
| 4 | Discovery & Architecture | G3 — Scope + Kickoff | Phase 3 — Planning & Architecture | DELIVERY |
| 5 | Threat Model & Security Design | G4 — Security Review | Phase 3 — Planning & Architecture | DELIVERY |
| 6 | Internal QA | G5 — Internal QA | Phase 4 — Build & Assure | DELIVERY |
| 7 | Assurance Decision | G6 — Assurance Decision | Phase 4 — Build & Assure | DELIVERY |
| 8 | Testnet Deployment | G7 — Irreversibility Gate | Phase 4 — Build & Assure | DELIVERY |
| 9 | Mainnet Deployment | G7 — Irreversibility Gate | Phase 4 — Build & Assure | DELIVERY |
| 10 | Operate & Monitor | G8 — Operate / Closeout | Phase 5 — Operate & Close | POST-DELIVERY |
| 11 | Upgrade / Change | G8 — Operate / Closeout | Phase 5 — Operate & Close | POST-DELIVERY |
| 12 | Close-Out | G8 — Operate / Closeout | Phase 5 — Operate & Close | POST-DELIVERY |

## Gate → Signer Matrix

| Gate | Mandatory Signers | Hard Stop Checks | Key Evidence |
|---|---|---|---|
| G1-A | AM, NO | HS-01, HS-02, HS-04 | C/B/P score, OFAC check |
| G2-A | AM, NO, CFO (if T2+) | HS-02 | MSA signed, retainer confirmed |
| G3-A | PM, NO | — | RACI-001, PSF, kickoff minutes |
| G4-A | TL, **CISO (mandatory)**, NO | — | Threat model (4 cat), admin matrix, DPIA (if T2+ EU) |
| G5-A | TL, QA, CISO | — | 2 independent reviews, test evidence, SAST clean |
| G6-A | AM, CISO, NO | HS-03 | External audit decision, bug bounty decision |
| G7-IRR | NO, **CISO (mandatory)**, TL | HS-06, HS-07 | Signing ceremony, deployment runbook, monitoring, all Crit/High resolved |
| G8-A | NO, TL | — | Monitoring handover, upgrade workflow documented |
