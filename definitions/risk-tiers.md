# Risk Tier Definitions

> Source-of-Truth: L1-ERM-001 §5, OPS-001 §3
> Last-Updated: 2026-04-08

| Tier | Score Range | Label | Acceptance Authority | Review Cadence | Budget Floor | Gate Requirements |
|---|---|---|---|---|---|---|
| T1 | 1.0 – 2.9 | Low/Medium | NO sole | 6 months | Standard | Standard gates |
| T2 | 3.0 – 3.5 | High | NO + CFO | 3 months | ≥10% EL | Enhanced gates + DPIA if EU data |
| T3 | 3.6 – 4.0 | Critical | CEO / Board | Monthly | 20–37% EL (Gordon-Loeb) | Full gates + external audit + CEO briefing |
| T4 | Escalated | Enterprise | Board minute | Continuous | Board-approved | Board oversight + regulatory notification |

## Scoring Model

```
Composite = weighted_avg(
  C_pillar: avg(C1_jurisdiction, C2_concentration, C3_credibility),
  B_pillar: avg(B1_payment_terms, B2_payment_discipline, B3_diversification),
  P_pillar: avg(P1_tech_complexity, P2_tvl_custody, P3_audit_status)
)
```

Each sub-score: integer 1–4.

## RAG Mapping

| RAG | Score | Meaning |
|---|---|---|
| Green | 1.0 – 2.0 | Acceptable risk. Standard governance. |
| Amber | 2.1 – 2.9 | Elevated risk. Enhanced monitoring. |
| Red | 3.0 – 3.5 | High risk. T2 governance applies. |
| Critical | 3.6 – 4.0 | Critical risk. T3/T4 governance. CEO involvement. |
