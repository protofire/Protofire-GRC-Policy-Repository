---
id: "L2-ASSURE-103"
title: "External Assurance Procedure (Audit/Bug Bounty)"
type: "Procedure"
level: "L2"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-006; L1-SDLC-003"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L2-ASSURE-103 — External Assurance Procedure (Audit/Bug Bounty)

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| ASSURE-R01 | External audit mandatory if: custody=YES OR TVL>$1M USD OR architecture IN [bridge,cross-chain,lending,leverage]. | `IF trigger_met THEN audit = MANDATORY` |
| ASSURE-R02 | Audit firm selected from approved vendor list per S-115. | `IF audit_firm NOT IN approved_list THEN flag(CISO)` |
| ASSURE-R03 | All Critical/High findings resolved before G7. Medium findings tracked. | `IF crit_high_open THEN block(G7)` |
| ASSURE-R04 | Bug bounty programme recommended for all mainnet deployments with TVL. | `IF mainnet AND tvl > 0 THEN recommend(bug_bounty)` |

## Dependencies

- **Explicit**: `L1-SDLC-003`, `S-115`
