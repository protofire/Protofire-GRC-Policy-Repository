---
id: "L3-TEST-204"
title: "Test Evidence Standard"
type: "Work Instruction"
level: "L3"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "TL"
approver: "NOC"
classification: "Confidential — Internal"
references: "L2-TEST-204; L2-DEL-101"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L3-TEST-204 — Test Evidence Standard

## Scope
Defines the format, content, and retention requirements for all test evidence artefacts.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| L3T-R01 | Test evidence report includes: test ID, description, input, expected result, actual result, pass/fail, tester, date. | IF field_missing THEN reject(report) |
| L3T-R02 | SAST results: tool name, version, scan date, findings (severity, location, description). | format(sast_report) |
| L3T-R03 | Fuzz test results: tool, seed, corpus size, coverage %, crashes found. | format(fuzz_report) |
| L3T-R04 | External audit results: firm, scope, findings (severity, status, remediation). | format(audit_report) |

## Dependencies
- **Explicit**: `L2-TEST-204`, `L2-DEL-101`
