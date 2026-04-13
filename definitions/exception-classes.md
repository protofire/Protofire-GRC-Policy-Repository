# Exception Classification

> Source-of-Truth: POL-009 §2
> Last-Updated: 2026-04-08

| Class | Trigger | Approval Required | Max Duration | Review Frequency | Register |
|---|---|---|---|---|---|
| E1 — Low | Deviation from Guideline (L4) or Standard (L2) operational detail | PM + TL | 90 days | At next gate | REG-506 |
| E2 — Medium | Deviation from Policy (L1) other than Hard Stop | NO + CISO | 60 days | Monthly | REG-506 |
| E3 — High | Deviation from core policy control (POL-001 §5, POL-002 §3, POL-004 §2.4) | NO + DoE + CISO | 30 days | Bi-weekly | REG-506 |
| E4 — Critical | Hard Stop override (HS-03 through HS-07 only) | DoE + CISO + CEO (written, timestamped) | One-time; no renewal without full re-approval | Immediate re-assessment at each gate | REG-506 |

## Absolute Prohibitions

HS-01 (OFAC) and HS-02 (no MSA) **cannot be excepted** under any circumstance. These are legal prohibitions, not policy requirements.

## Process

```
1. Requestor → CISO: written request (requirement, justification, compensating control, duration)
2. CISO → classify exception (E1–E4)
3. IF E3 OR E4 THEN CISO → prepare risk opinion brief for DoE/NO
4. Approval obtained per authority table (written, timestamped)
5. Record in REG-506 with all documentation
6. Implement compensating control
7. Review at specified frequency
8. At expiry: lapse (policy re-applies) OR new request submitted
```
