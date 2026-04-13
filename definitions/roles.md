# Role Definitions

> Source: L0-1 §4, L0-2 §4.2, CL-PHASE-001
> Last-Updated: 2026-04-08
> Canonical: true

## Governance Roles

| ID | Canonical Name | Abbreviation | Authority | Non-Delegable Functions | Source |
|---|---|---|---|---|---|
| ROLE-01 | Node Owner | NO | Primary risk acceptance (T1 sole, T2 co-approve). Gate signer G1–G8. | T1 risk acceptance; Gate G7 Irreversibility sign-off | L0-1 §4 |
| ROLE-02 | Chief Information Security Officer | CISO | Policy authority. ISMS lead. Gate G4–G7 sign-off. DPO function. | G4 mandatory co-sign; Irreversibility Gate co-sign; E4 exception co-sign | L0-1 §4 |
| ROLE-03 | GRC Manager | GRC-MGR | Operational backbone. Registers, evidence calendar, ClickUp admin. | — | L0-2 §4.2 |
| ROLE-04 | Account Manager | AM | Default Project Risk Owner. C/B/P scoring. G1–G2 owner. | — | L1-ERM-001 §5.6 |
| ROLE-05 | Technical Lead | TL | Threat model owner. Admin matrix. Two-person Reviewer. G4–G6 co-sign. | Threat model (4 categories) at G4 | L0-1 §4 |
| ROLE-06 | Project Manager | PM | RACI-001, PSF, kickoff, demo minutes, G3 co-sign. | — | CL-PHASE-001 |
| ROLE-07 | DevOps Engineer | DevOps | CI/CD security. Monitoring. Two-person Deployer. G6 co-sign. | — | CL-PHASE-001 |
| ROLE-08 | QA Engineer | QA | 2nd independent reviewer. Fuzz/property testing. Audit report sign-off. | Independence: QA ≠ code author | CL-PHASE-001 |
| ROLE-09 | Finance/Billing | FIN | Payment schedules. Arrears monitoring. HS-05 alerts. | — | CL-PHASE-001 |
| ROLE-10 | Chief Financial Officer | CFO | T2 co-approval. Budget sign-off. Commercial exceptions. | — | L0-1 §4 |
| ROLE-11 | Chief Executive Officer | CEO | T3 risk acceptance. L0 amendments. Emergency override. | T3/T4 risk acceptance | L0-1 §4 |
| ROLE-12 | Director of Engineering | DoE | E3/E4 co-approver. SoD compensating authority when NO multi-roles. | — | L0-1 §4 |
| ROLE-13 | Data Protection Officer | DPO | GDPR compliance. ROPA. DPIA. Breach notification. DSR. | Breach notification to supervisory authority | POL-011 §13 |
| ROLE-14 | Head of Delivery | HoD | L2-DEL-101 owner. Delivery programme oversight. | — | L2-DEL-101 |
| ROLE-15 | Head of Risk | HoR | L2-RISK-102 owner. Risk register operations. | — | L2-RISK-102 |
| ROLE-16 | Kaizen Meta-Agent | KAIZEN | Post-session skill refinement. Continuous improvement cycle. | — | Agent Skill Suite |

## Deprecated Names

| Deprecated Name | Maps To | Reason |
|---|---|---|
| fCTO Extended | AM or DoE (context-dependent) | Ambiguous; split into AM and DoE per RACI-001 |
| GRC [CISO track] | CISO | Merged into single CISO definition per ISS-003 resolution |
| Head of Security | CISO | Legacy title; normalized |
| Security Officer | CISO | Legacy title; normalized |

## Functional Assignments

| Function | Current Holder | Backup | Source |
|---|---|---|---|
| DPO | CISO (Aleksey Lekontsev) | CEO appoints interim within 5 business days | POL-011 §13 |
| vCISO | Aleksey Lekontsev | Non-substitutable for gate G4 and Irreversibility Gate | L0-1 §4 |
| GRC Manager | TBD — requires 0.5 FTE | Report to CEO if shortfall sustained | L0-2 §6.2 |
