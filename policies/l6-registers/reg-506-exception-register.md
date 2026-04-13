---
id: "REG-506"
title: "Exception & Waiver Register"
type: "Register"
level: "L6"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Quarterly"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-009"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# REG-506 — Exception & Waiver Register

## Purpose

Register of all active, expired, and rejected policy exceptions.

## Schema

| Field | Description |
|---|---|
| Exception_ID | Unique identifier: EXC-{year}-{seq} |
| Exception_Class | E1/E2/E3/E4 |
| Policy_Requirement | Specific requirement being deviated from |
| Requestor | Named individual and role |
| Business_Justification | Written justification |
| Compensating_Control | Description and control ID |
| Approval_Authority | Per exception class table |
| Approval_Date | Date and timestamp |
| Expiry_Date | Calculated from class duration |
| Status | Active/Expired/Rejected/Renewed |
| Review_Frequency | Per class: gate/monthly/biweekly/immediate |
| Last_Review | Date |
| Notes | Additional context |

