---
id: "GL-304"
title: "Privacy by Design Guideline"
type: "Guideline"
level: "L4"
version: "1.0"
status: "Generated"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO-DPO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-011 §5; GDPR Art.25"
last_change: "2026-04-08"
last_approval: "Pending"
---
<!-- GENERATED: true -->

# GL-304 — Privacy by Design Guideline

## Scope
Guidance for incorporating privacy principles into system architecture and development.

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| GL304-R01 | Data minimization: collect only personal data necessary for stated purpose. | IF no_purpose THEN reject(collection) |
| GL304-R02 | Pseudonymization/anonymization preferred where feasible. | IF identifiable AND anonymization_feasible THEN apply() |
| GL304-R03 | Privacy impact considered at architecture phase (G4). | IF g4 AND personal_data THEN review(privacy_impact) |
| GL304-R04 | Default settings: most privacy-protective option. | IF configurable THEN default = most_private |
| GL304-R05 | Data lifecycle: define collection, processing, storage, deletion for each data category. | document(data_lifecycle_per_category) |

## Dependencies
- **Explicit**: `POL-011`, `CL-409`
