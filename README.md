# Protofire GRC Policy Repository

> Version: 2026-04-16 | Owner: CISO | Classification: Confidential — Internal

## Structure

```
├── policies/
│   ├── l0-foundation/       # Charters, scope, appetite, master frameworks, RACI, SOA, IAP
│   ├── l1-policies/         # POL-001 through POL-017, DAO-001 template
│   ├── l1-standards/        # L1-ERM-001, L1-SDLC-003, OPS-001, STD-101–105, STD-110, S-109, S-115
│   ├── l2-procedures/       # Operational procedures (DEL, RISK, ASSURE, INC, VULN, ACCESS, etc.)
│   ├── l3-work-instructions/ # GL-304, GL-305, L3-TEST-204
│   ├── l4-plans/            # PLAN-701 (Tabletop IR), PLAN-702 (BCP), PLAN-703 (DR)
│   ├── l5-checklists/       # CL-PHASE-001, CL-409, CL-411
│   ├── l6-registers/        # REG-501 through REG-513
│   └── legal-templates/     # DPA-001, MSA-001
├── controls/
│   ├── control-catalogue.md     # All controls with enforcement logic
│   └── sod-matrix.md            # Separation of duties conflict table
├── definitions/
│   ├── roles.md                 # Canonical role definitions
│   ├── terms.md                 # Glossary
│   ├── hard-stops.md            # HS-01 through HS-07
│   ├── exception-classes.md     # E1–E4 classification
│   ├── risk-tiers.md            # T1–T4 with scoring
│   └── lifecycle-model.md       # 12-step ↔ 8-stage ↔ 5-phase
├── mappings/
│   ├── standards-mapping.md           # ISO 27001, NIST, GDPR, SOC 2, COBIT
│   ├── map-001-control-mapping-matrix.md  # Control mapping matrix (MAP-001)
│   ├── policy-control-map.json        # Policy → Control cross-reference
│   ├── policy-dependency-map.json     # Parent/child document graph
│   └── gate-evidence-map.md           # Gate × Evidence requirements
├── meta/
│   ├── index.json                     # Master document registry
│   ├── repo-config.yaml               # Repository configuration
│   ├── gap-tracker.md                 # Open and resolved gaps
│   └── supersession-log.json          # Document supersession chain
├── reference_policies/      # Source DOCX originals (canonical reference copies)
│   ├── POL-xxx_*.docx       # Active policy documents
│   ├── Retire_*.docx        # Superseded / non-policy files (do not use)
│   └── Bak_*.docx           # Pre-patch backups
└── repository_update_log.txt  # Last actualization run log (2026-04-16)
```

## Document Hierarchy

| Level | Prefix(es) | Folder | Description |
|---|---|---|---|
| L0 | L0-x, GRC-*, SOA, IAP, RACI | `l0-foundation/` | Charters, frameworks, scope, governance |
| L1-Policy | POL-xxx, DAO-xxx | `l1-policies/` | Enterprise policies |
| L1-Standard | L1-xxx, STD-xxx, S-xxx, OPS-xxx | `l1-standards/` | Technical and operational standards |
| L2 | L2-xxx, PR-xxx | `l2-procedures/` | Operational procedures |
| L3 | GL-xxx, L3-xxx | `l3-work-instructions/` | Guidelines and work instructions |
| L4 | PLAN-xxx | `l4-plans/` | BCM, DR and exercise plans |
| L5 | CL-xxx | `l5-checklists/` | Operational checklists |
| L6 | REG-xxx | `l6-registers/` | Registers and operational records |
| — | DPA-xxx, MSA-xxx | `legal-templates/` | Contract and legal templates |

## Conventions

- **Naming**: kebab-case, deterministic
- **Format**: Markdown with YAML frontmatter
- **Numbering**: POL-xxx canonical (P-xxx deprecated per GRC-CONC-001)
- **Generated docs**: Marked with `status: "Generated"` in frontmatter
- **Hierarchy precedence**: L0 > L1 > L2 > L3 > L4 > L5 > L6
- **Currency**: USD (standardized)
- **Lifecycle model**: 12-step authoritative
- **ID collision resolved**: PR-208 = Breach Notification; PR-210 = Key Compromise Response

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
| S-115 | Vendor Security Assessment Standard | No vendor assessment standard |
| PR-208 | Breach Notification Procedure | GDPR Art.33 operationalization |
| PR-209 | DSR Handling Procedure | GDPR Art.12-23 operationalization |
| GL-304 | Privacy by Design Guideline | GDPR Art.25 operationalization |
| CL-409 | DPIA Screening Checklist | GDPR Art.35 operationalization |
| CL-411 | Signing Ceremony Checklist | Key custody procedure gap |
| REG-505 | ROPA | GDPR Art.30 mandatory |
| REG-506 | Exception Register | POL-009 operationalization |
| REG-510 | DPIA Register | POL-011 §6 operationalization |
| REG-511 | Document Registry | Document control gap |

## Open Gaps (from meta/gap-tracker.md)

| Gap ID | Severity | Description | Target |
|---|---|---|---|
| GAP-10 | MEDIUM | DPO supervisory authority registration | 60 days |
| GAP-16 | LOW | Statement of Applicability not formalized (SOA-001 added; pending approval) | 90 days |
| GAP-17 | LOW | Internal Audit Programme (IAP-001 added; pending approval) | 90 days |
| GAP-18 | LOW | Node configuration register (REG-513 added; pending approval) | 90 days |

## Pending Manual Review

The following 50 documents exist in both `reference_policies/` (DOCX) and `policies/` (MD stub).
The DOCX versions are significantly more detailed. Content merge is required before these stubs become operative:

`L0-1`, `L0-2`, `L0-4`, `L0-5`, `GRC-MASTER-001`, `GRC-PF-001`, `GRC-CONC-001`,
`POL-001` through `POL-011`,
`L1-ERM-001`, `L1-ENG-002`, `L1-SDLC-003`, `L1-EVID-004`, `L1-KEY-005`, `L1-BC-008`, `L1-INFRA-009`, `L1-HR-010`,
`OPS-001`, `S-109`, `S-115`, `STD-101`,
`L2-DEL-101`, `L2-RISK-102`, `L2-ASSURE-103`, `L2-INC-201`, `L2-VULN-202`, `L2-ACCESS-203`, `L2-TEST-204`, `L2-CHANGE-205`,
`PR-208`, `PR-209`,
`GL-304`, `L3-TEST-204`,
`CL-PHASE-001`, `CL-409`, `CL-411`,
`REG-501`, `REG-505`, `REG-506`, `REG-510`, `REG-511`

See `repository_update_log.txt` for full word-count delta per document.
