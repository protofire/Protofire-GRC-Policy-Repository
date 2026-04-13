---
id: "GRC-CONC-001"
title: "Document Numbering Concordance Table"
type: "Reference"
level: "L0"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "GRC-Manager"
approver: "CISO"
classification: "Confidential — Internal"
references: "L0-1 §6; GRC-PF-001; GRC-MASTER-001"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# GRC-CONC-001 — Document Numbering Concordance Table

## Purpose

Resolves the dual-numbering collision between GRC-PF-001 v1.0 (P-xxx scheme) and GRC-MASTER-001 v1.1 (POL-xxx scheme). The POL-xxx scheme is **canonical**. All P-xxx references are deprecated.

## Concordance Table

| Deprecated ID (P-xxx) | Canonical ID (POL-xxx) | Title (Canonical) | Notes |
|---|---|---|---|
| P-001 | POL-002 | Information Security Policy | P-001 was "Info Security" in v1.0; POL-001 is now "Project Governance" |
| P-002 | POL-003 | Risk Management Policy | Direct rename |
| P-003 | POL-011 | Data Protection & Privacy Policy | Elevated to standalone; expanded scope |
| P-004 | POL-004 | Access Control & SoD Policy | Title change: was "Acceptable Use" |
| P-005 | POL-005 | Change Management Policy | Was "Business Continuity" in P-xxx; reassigned |
| P-006 | POL-007 | Third-Party & Vendor Risk Policy | Renumbered |
| P-007 | — | Cryptographic Controls Policy | Merged into L1-KEY-005; no standalone POL equivalent |
| P-008 | — | Personnel Security Policy | Merged into L1-HR-010; no standalone POL equivalent |
| P-009 | — | Physical & Environmental Security Policy | Deferred; not applicable to remote-first model |
| P-010 | — | Incident Management Policy | Elevated to L2-INC-201 under POL-010 governance |

## New Documents (no P-xxx predecessor)

| Canonical ID | Title | Origin |
|---|---|---|
| POL-001 | Project Governance Policy | New — gap fill |
| POL-006 | Testing & QA Policy | New — gap fill |
| POL-008 | Documentation & Records Retention Policy | New — gap fill |
| POL-009 | Exception & Deviation Management Policy | New — gap fill |
| POL-010 | Monitoring & Continuous Assurance Policy | New — gap fill |

## Rule

```
IF reference contains "P-001" through "P-010" THEN
  lookup(this_table)
  replace_with(canonical_POL_id)
  log(migration_event)
```
