# Hard Stop Definitions

> Source-of-Truth: L1-ERM-001 §7.2
> Referenced-By: L0-1 §7.3, POL-001 §5.3, POL-009 §3, CL-PHASE-001
> Last-Updated: 2026-04-08

## Rule

Hard Stops are absolute blocking conditions. When triggered, project progression halts until the condition is resolved or a formal E4 exception is granted (HS-01 and HS-02 cannot be excepted under any circumstance).

## Definitions

| ID | Condition | Trigger Gate | Action | Exception Permitted | Acceptance Authority |
|---|---|---|---|---|---|
| HS-01 | Jurisdiction appears on OFAC sanctions list | G1 | IMMEDIATE rejection. Legal notified within 24h. No work commences. | **NEVER** — absolute prohibition | N/A |
| HS-02 | No signed MSA before work commencement | G1 | Project blocked. Release only upon signed MSA with compliant terms. | **NEVER** — absolute prohibition | N/A |
| HS-03 | TVL > $1,000,000 USD with no external audit active or planned | G6 | P3 sub-score auto-set to 4. Escalate to CISO. Audit must be engaged before G6. | E4 (DoE + CISO + CEO written) | CEO |
| HS-04 | Single client > 60% of node revenue | G1 | C2 sub-score auto-set to 4. Full GRC Committee review required. Mandatory re-score. | E4 (DoE + CISO + CEO written) | CEO |
| HS-05 | Payment arrears > 60 calendar days | Any | Stop-work clause triggered. B2 auto-set to 4. Legal review within 48h. NO notified. | E4 (DoE + CISO + CEO written) | CEO |
| HS-06 | Irreversibility Gate (G7) criteria not met | G7 | Deployment blocked. CEO/Board escalation within 24h. NO incident report. | E4 (DoE + CISO + CEO written) | CEO/Board |
| HS-07 | Key ownership/custody status is disputed or unclear | G7 | Deployment blocked. CEO notified. Legal opinion required before release. | E4 (DoE + CISO + CEO written) | CEO |

## Enforcement Logic

```
IF jurisdiction IN OFAC_LIST THEN reject(HS-01); RETURN
IF signed_msa = FALSE THEN block(HS-02); RETURN
IF tvl > 1000000 AND audit_status NOT IN [active, planned] THEN trigger(HS-03); set(P3, 4)
IF client_revenue_share > 0.60 THEN trigger(HS-04); set(C2, 4)
IF payment_arrears_days > 60 THEN trigger(HS-05); set(B2, 4); stop_work()
IF g7_criteria_met = FALSE THEN trigger(HS-06); block_deployment()
IF key_custody_status IN [disputed, unclear] THEN trigger(HS-07); block_deployment()
```
