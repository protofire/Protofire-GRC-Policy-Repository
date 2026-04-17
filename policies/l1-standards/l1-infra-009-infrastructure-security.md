---
id: "L1-INFRA-009"
title: "Infrastructure Security Baseline Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Approved"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "NOC"
classification: "Confidential — Internal"
references: "POL-002; ISO 27001 A.8.1-8.34; NIST PR.PT"
last_change: "2026-04-08"
last_approval: "Pending"
---

# L1-INFRA-009 — Infrastructure Security Baseline Standard

## Atomic Requirements

| Req ID | Requirement | Enforcement |
|---|---|---|
| INFRA-R01 | Hardened base images for all production infrastructure. | `IF base_image.hardened = FALSE THEN block(deployment)` |
| INFRA-R02 | Network segmentation between environments (dev/staging/production). | `IF env_segmentation = FALSE THEN flag(critical)` |
| INFRA-R03 | Patch management: Critical within 72h, High within 7d, Medium within 30d. | `IF patch.severity = Critical AND age > 72h THEN flag(overdue)` |
| INFRA-R04 | WAF/DDoS protection for all public endpoints. | `IF public_endpoint AND waf = FALSE THEN flag(gap)` |
| INFRA-R05 | DNSSEC enabled for all production domains; DNS registrar accounts protected with hardware MFA (FIDO2/WebAuthn); any DNS record change triggers P2 alert within 5 minutes (STD-102 §4.4). | `IF dnssec = FALSE OR registrar_mfa != hardware THEN flag(critical)` |
| INFRA-R06 | BGP hijacking monitoring active for all production IP ranges. | `IF bgp_monitoring = FALSE AND public_ip_range THEN flag(gap)` |

