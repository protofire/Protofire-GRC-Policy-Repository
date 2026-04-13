# Protofire GRC Policy Repository

> Version: 2026-04-08 | Owner: CISO | Classification: Confidential — Internal

## Structure

```
├── policies/
│   ├── l0-foundation/     # Charters, scope, appetite, master frameworks
│   ├── l1-policies/       # POL-001 through POL-011
│   ├── l1-standards/      # L1-ERM-001, L1-SDLC-003, OPS-001, STD-101, etc.
│   ├── l2-procedures/     # Operational procedures (DEL, RISK, ASSURE, INC, etc.)
│   ├── l3-work-instructions/  # Test evidence, privacy by design
│   ├── l5-checklists/     # CL-PHASE-001, CL-409, CL-411
│   └── l6-registers/      # REG-501, REG-505, REG-506, REG-510, REG-511
├── controls/
│   ├── control-catalogue.md   # All controls with enforcement logic
│   └── sod-matrix.md          # Separation of duties conflict table
├── definitions/
│   ├── roles.md               # Canonical role definitions
│   ├── terms.md               # Glossary
│   ├── hard-stops.md          # HS-01 through HS-07
│   ├── exception-classes.md   # E1–E4 classification
│   ├── risk-tiers.md          # T1–T4 with scoring
│   └── lifecycle-model.md     # 12-step ↔ 8-stage ↔ 5-phase
├── mappings/
│   ├── standards-mapping.md           # ISO 27001, NIST, GDPR, SOC 2, COBIT
│   ├── policy-control-map.json        # Policy → Control cross-reference
│   ├── policy-dependency-map.json     # Parent/child document graph
│   └── gate-evidence-map.md           # Gate × Evidence requirements
└── meta/
    ├── index.json                     # Master document registry
    ├── repo-config.yaml               # Repository configuration
    └── supersession-log.json          # Document supersession chain
```

## Conventions

- **Naming**: kebab-case, deterministic
- **Format**: Markdown with YAML frontmatter
- **Numbering**: POL-xxx canonical (P-xxx deprecated per GRC-CONC-001)
- **Generated docs**: Marked with `<!-- GENERATED: true -->` in frontmatter
- **Hierarchy precedence**: L0 > L1 > L2 > L3 > L4 > L5 > L6
- **Currency**: USD (standardized)
- **Lifecycle model**: 12-step authoritative

## AI Agent Usage

All files use:
- YAML frontmatter for metadata parsing
- Atomic requirement tables with `Req ID | Requirement | Enforcement` columns
- Enforcement logic in pseudo-code (`IF/THEN` blocks)
- Explicit cross-references via relative Markdown links
- JSON files for machine-parseable mappings

## Generated Documents

Documents with `status: "Generated"` were created to fill identified gaps.
They require review and approval before becoming operative.

| Doc ID | Title | Gap Filled |
|---|---|---|
| GRC-CONC-001 | Concordance Table | Dual numbering collision |
| S-109 | Data Classification Standard | No classification tiers |
| S-115 | Vendor Security Assessment | No vendor assessment |
| PR-208 | Breach Notification Procedure | GDPR Art.33 operationalization |
| PR-209 | DSR Handling Procedure | GDPR Art.12-23 operationalization |
| GL-304 | Privacy by Design Guideline | GDPR Art.25 operationalization |
| CL-409 | DPIA Screening Checklist | GDPR Art.35 operationalization |
| CL-411 | Signing Ceremony Checklist | Key custody procedure gap |
| REG-505 | ROPA | GDPR Art.30 mandatory |
| REG-506 | Exception Register | POL-009 operationalization |
| REG-510 | DPIA Register | POL-011 §6 operationalization |
| REG-511 | Document Registry | Document control gap |
