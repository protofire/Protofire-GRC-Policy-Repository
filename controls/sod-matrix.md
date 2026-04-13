# Separation of Duties Matrix

> Source: POL-004 §2.4
> Last-Updated: 2026-04-08

## Conflict Scenarios

| # | Role A (Responsible) | Role B (Approver) | Conflict | Compensating Control |
|---|---|---|---|---|
| SoD-1 | Developer (code author) | QA (code reviewer) | Same person writes and reviews code | Mandatory 2nd reviewer; QA ≠ author enforced in CI |
| SoD-2 | DevOps (deployer) | TL (deployment approver) | Same person deploys and approves | Two-person rule: deployer ≠ approver at G7 |
| SoD-3 | AM (risk scorer) | NO (risk acceptor) | Same person scores and accepts risk | IF AM = NO THEN require(CISO co-sign on acceptance) |
| SoD-4 | CISO (policy author) | NO (policy approver) | Same person writes and approves policy | DoE co-approval required for all L1 policies |
| SoD-5 | NO (gate signer) | NO (PM role) | Same person manages project and signs gate | IF NO = PM AND tier >= T2 THEN require(DoE co-sign) |
| SoD-6 | FIN (invoice issuer) | NO (payment approver) | Same person issues and approves payment | Segregated in billing system; FIN cannot self-approve |
| SoD-7 | TL (key generator) | TL (key custodian) | Same person generates and holds production keys | Multisig 2-of-3 minimum; no single-key holder |

## Enforcement Logic

```
FOR EACH gate_decision:
  IF signer.role IN responsible_roles_for_artifact THEN
    IF compensating_control_available THEN
      apply(compensating_control)
      log(SoD_exception, REG-506)
    ELSE
      block(gate_decision)
      escalate(CISO)
```
