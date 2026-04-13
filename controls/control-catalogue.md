# Control Catalogue

> Last-Updated: 2026-04-08
> Source: Consolidated from POL-001 through POL-011, STD-101, L1 Standards

## Governance Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-GOV-001 | Mandatory 12-step lifecycle compliance for all engagements | Preventive | PM + TL | POL-001 §5.1 | All | IF engagement_active THEN lifecycle_steps = 12 |
| CTL-GOV-002 | Hard Stop conditions enforced at designated gates | Preventive | NO + CISO | POL-001 §5.3 | G1,G6,G7 | See [hard-stops.md](../definitions/hard-stops.md) |
| CTL-GOV-003 | Risk-proportionate governance tiers (T1–T4) | Preventive | NO + CISO | POL-001 §5.5 | All | IF tier >= T2 THEN enhanced_governance = TRUE |
| CTL-GOV-004 | Node Owner SoD requirement when multi-role | Compensating | NO + DoE | POL-001 §5.4 | All | IF NO.roles.count > 1 AND tier >= T2 THEN require(DoE_co_sign) |
| CTL-GOV-005 | C/B/P risk scoring before MSA execution | Preventive | AM + NO | POL-003 §2 | G1 | IF step < 3 AND cbp_score = NULL THEN block(G2) |
| CTL-GOV-006 | Exception classification and approval per E1–E4 | Detective | CISO | POL-009 §2 | All | See [exception-classes.md](../definitions/exception-classes.md) |
| CTL-GOV-007 | Document hierarchy precedence (L0 > L1 > L2 > L3+) | Directive | CISO | L0-1 §6 | All | IF conflict(doc_a, doc_b) THEN doc_higher_level.prevails |

## Security Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-SEC-001 | Peer code review (≥2 reviewers) | Preventive | TL + QA | POL-002 §3.1 | G5 | IF security_critical THEN require(TL_review) |
| CTL-SEC-002 | SAST at CI/CD gate — Critical/High block merge | Preventive | DevOps | POL-002 §3.1 | G5 | IF sast_findings.severity IN [Critical, High] THEN block(merge) |
| CTL-SEC-003 | No hard-coded credentials in source | Preventive | TL + Dev | POL-002 §3.3 | G5 | IF secret_scan.findings > 0 THEN block(merge) |
| CTL-SEC-004 | Threat model (4 categories: technical, economic, governance, human) | Preventive | TL + CISO | POL-002 §3.5 | G4 | IF threat_model.categories < 4 THEN block(G4) |
| CTL-SEC-005 | Two-person rule for production deployment | Preventive | TL + DevOps | POL-002 §3.5 | G7 | IF deployer = reviewer THEN block(deployment) |
| CTL-SEC-006 | External audit for TVL > $1M or custody/bridge/lending | Preventive | NO + TL | POL-002 §3.5 | G6 | See HS-03 |
| CTL-SEC-007 | Multisig ≥ 2-of-3 for production on-chain admin | Preventive | TL + NO | POL-004 §2.5 | G7 | IF admin_signers < 2 THEN block(G7) |
| CTL-SEC-008 | GDPR breach notification within 72h | Reactive | CISO (DPO) | POL-011 §8.1 | Post-G8 | IF personal_data_breach THEN notify(authority, 72h); notify(CISO, 4h) |
| CTL-SEC-009 | Signing ceremony documented per CL-411 | Preventive | CISO + TL | L1-KEY-005 | G7 | IF production_keys_generated THEN require(CL-411_completed) |
| CTL-SEC-010 | Evidence retention ≥ 365 days | Detective | CISO | L1-EVID-004 | All | IF evidence_age > 365d AND type != legal THEN archive_review() |

## Access Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-ACC-001 | Principle of least privilege | Preventive | CISO | POL-004 §2.1 | G4, G8 | IF access_scope > role_scope THEN deny() |
| CTL-ACC-002 | Access provisioning within 1 business day | Directive | CISO + NO | POL-004 §2.2 | G4 | IF new_access_request THEN provision(1_bday); production = separate_approval |
| CTL-ACC-003 | Access deprovisioning within 1 business day of trigger | Reactive | CISO | POL-004 §2.2 | G8 | IF role_change OR departure THEN deprovision(1_bday) |
| CTL-ACC-004 | Shared credentials prohibited | Preventive | CISO | POL-004 §2.3 | All | IF credential.shared = TRUE THEN violation(); require(CISO_waiver + compensating_monitor) |
| CTL-ACC-005 | SoD rules table (7 conflict scenarios) | Preventive | CISO + DoE | POL-004 §2.4 | All | See [sod-matrix.md](sod-matrix.md) |
| CTL-ACC-006 | Quarterly access review | Detective | CISO | POL-004 §2.6 | Quarterly | IF quarter_end THEN review_all_privileged(); remediate(5_bdays) |

## Change Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-CHG-001 | Change classification C1–C5 | Preventive | PM + TL + NO | POL-005 §2 | G5, G7, G8 | IF change_request THEN classify(C1_C5); route_approval() |
| CTL-CHG-002 | On-chain change mini-cycle for TVL > $1M | Preventive | TL + CISO | POL-005 §3.2 | G7 | IF tvl > 1M AND change_type = on_chain THEN require(mini_cycle) |
| CTL-CHG-003 | Rollback plan required for C3+ changes | Preventive | TL | POL-005 §3 | G7 | IF change_class >= C3 THEN require(rollback_plan) |

## Privacy Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-PRI-001 | DPIA mandatory for T2+ with EU personal data | Preventive | CISO (DPO) | POL-011 §6.1 | G4 | IF tier >= T2 AND eu_data = TRUE THEN require(DPIA_before_G4) |
| CTL-PRI-002 | DSR response within 30 calendar days | Reactive | CISO (DPO) | POL-011 §7.1 | Post-G8 | IF dsr_received THEN ack(3_bdays); fulfill(30_cdays) |
| CTL-PRI-003 | Data minimization by design | Preventive | TL + CISO | POL-011 §5 | G4 | IF personal_data_collected AND no_lawful_basis THEN reject() |
| CTL-PRI-004 | ROPA maintained and current | Detective | CISO (DPO) | POL-011 §12 | Ongoing | IF new_processing_activity THEN update(REG-505) |
| CTL-PRI-005 | International transfer safeguards (SCCs, adequacy) | Preventive | CISO (DPO) | POL-011 §9 | G4 | IF transfer_outside_eea THEN require(safeguard_mechanism) |

## Assurance Controls

| ID | Control | Type | Owner | Policy Source | Gate | Enforcement |
|---|---|---|---|---|---|---|
| CTL-ASR-001 | Weekly Security 360 review | Detective | CISO | POL-010 §2 | Ongoing | IF week_end THEN review(risk_register, incidents, access_anomalies) |
| CTL-ASR-002 | Annual internal audit | Detective | CISO | POL-010 §2 | Annual | IF year_end THEN audit(full_ISMS_scope); produce(CAPA_plan) |
| CTL-ASR-003 | Annual management review | Detective | NO + DoE + CISO | POL-010 §2 | Annual | IF year_end THEN review(ISMS_performance, policy_adequacy, resources) |
| CTL-ASR-004 | KRI dashboard (8 KRIs with RAG thresholds) | Detective | CISO + NO | POL-010 §3 | Monthly | IF kri_value.status = Red THEN escalate(NO, 48h) |
| CTL-ASR-005 | BCM/DR test annually | Detective | CISO | L1-BC-008, L2-TEST-204 | Annual | IF year_end THEN execute(bcm_test); document(L3-TEST-204) |
