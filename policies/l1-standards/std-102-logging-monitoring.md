---
id: "STD-102"
title: "Logging and Monitoring Standard"
type: "Standard"
level: "L1-STD"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO"
approver: "CISO advisory"
classification: "Confidential — Internal"
last_change: "2026-04-16"
last_approval: "Pending"
source: "reference_policies (DOCX conversion)"
---

# STD-102 — Logging and Monitoring Standard

Logging &amp; Monitoring Standard

# 0. Document Control

Attribute

Value

Document ID

STD-102

Title

Logging &amp; Monitoring Standard

Hierarchy Level

L2 -- Standard

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

CISO / DevOps Lead

Approver

Node Owner

Classification

Confidential -- Internal

Supersedes

—

References

POL-003 Access Control Policy; POL-006 Network &amp; Infrastructure Security; ISO 27001:2022 A.8.15-A.8.17; NIST CSF 2.0 DE.CM; SOC 2 CC7.2

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

STD-102 defines the mandatory requirements for logging, monitoring and alerting across all Protofire systems, networks, applications and smart-contract deployments. Effective logging is the foundation of incident detection, forensic investigation, compliance evidence and operational visibility.

# 2. Scope

Applies to all production systems, staging environments, CI/CD pipelines, cloud infrastructure, SaaS tooling, on-chain monitoring, and any system processing Protofire or client data. Exemptions require POL-009 E2+ exception with CISO sign-off.

# 3. Log Requirements

## 3.1 Mandatory Log Sources

Authentication systems -- all login attempts (success/failure), MFA events, session creation/destruction

Authorization decisions -- privilege escalation, role changes, access denials

Infrastructure -- firewall/WAF, load balancer, DNS, VPN gateway

Application -- API requests, error responses (4xx/5xx), data export events, file uploads

Database -- schema changes, privileged queries, bulk data operations

CI/CD -- build triggers, deployment approvals, secret access, artifact signing

Version control -- repository creation, branch protection changes, force pushes, admin actions

Smart-contract / On-chain -- deployment transactions, admin key usage, upgrade proxy calls, treasury movements exceeding threshold

Cloud provider -- IAM changes, security group modifications, storage bucket policy updates

## 3.2 Mandatory Log Fields

Field

Requirement

Timestamp

ISO 8601 UTC with millisecond precision; clock synchronised via NTP (drift &lt; 1 s)

Event ID

Unique identifier; UUID v4 or monotonic sequence

Source

System/application/service name and version

Actor

Authenticated identity (user ID, service account, API key hash)

Action

Verb describing the operation (e.g., LOGIN, CREATE, DELETE, DEPLOY)

Target

Resource acted upon (file path, API endpoint, contract address, record ID)

Outcome

Success / Failure / Partial + reason code

Source IP

Originating IP address; X-Forwarded-For where applicable

Correlation ID

Request trace ID for distributed tracing

## 3.3 Log Integrity

Logs must be immutable once written -- append-only storage with tamper-detection (hash chain or WORM)

Log forwarding must use TLS 1.2+ encrypted channels

Write access to log storage restricted to service accounts only; no human write access

Retention: minimum 12 months hot, 24 months cold, 7 years archive (per POL-008 §4.3)

# 4. Monitoring &amp; Alerting

## 4.1 Monitoring Coverage

All mandatory log sources must feed a centralised SIEM or log aggregation platform

Real-time correlation rules for: brute-force detection, impossible travel, privilege escalation, data exfiltration patterns

On-chain monitoring via Tenderly/OpenZeppelin Defender for deployed contract events

## 4.2 Alert Classification

Severity

Examples

Response SLA

Notification

P1 -- Critical

Confirmed breach; admin key compromise; mainnet exploit

15 min acknowledge, 1 h contain

PagerDuty → CISO + NO + TL immediate

P2 -- High

Multiple failed MFA; suspicious data export; anomalous on-chain activity

30 min acknowledge, 4 h investigate

CISO + TL; Slack #security-alerts

P3 -- Medium

Single auth anomaly; non-critical config change; threshold breach

4 h acknowledge, 24 h investigate

GRC Manager; Slack #security-alerts

P4 -- Low

Informational; audit log review findings; policy deviation

Next business day

Weekly digest to GRC Manager

## 4.3 On-Chain Monitoring Requirements

All deployed smart contracts must have Tenderly or equivalent monitoring configured within 24 h of deployment

Alert triggers: admin function calls, proxy upgrades, treasury withdrawals &gt; defined threshold, pause/unpause events

Alert delivery: webhook → SIEM + Slack #on-chain-alerts + PagerDuty (P1/P2)

Monthly validation: trigger test alerts to confirm pipeline integrity (logged in REG-504)

## 4.4 DNS Security Monitoring (GAP-19)

All production domains used by Protofire or client deployments (frontends, RPC endpoints, APIs, signing interfaces) must have the following controls applied:

DNSSEC enabled and validated for all production domains — absence is a INFRA-R05 finding

DNS registrar accounts protected with hardware MFA (FIDO2/WebAuthn); password-only registrar access is prohibited

DNS zone change alerting: any A, CNAME, NS, or MX record modification must trigger a P2 alert within 5 minutes of change

Authoritative DNS provider must support DNSSEC and retain change audit logs for minimum 12 months

BGP hijacking monitoring active for all production IP ranges (BGPmon, Cloudflare Radar, or equivalent)

Critical DNS record TTL set to ≤300 seconds to enable rapid recovery in a hijack scenario

DNS zone file version-controlled; monthly diff check to detect unauthorised drift

`IF dns_record_change AND NOT change_authorized THEN alert(CISO, P2, 5min)`

`IF dnssec_validation_fail THEN alert(CISO, P1, immediate)`

# 5. Roles &amp; Responsibilities

Role

Responsibility

CISO

Approve monitoring strategy; review P1/P2 alerts; sign-off on coverage gaps

DevOps Lead

Implement and maintain logging infrastructure; ensure all sources onboarded

TL

Define on-chain monitoring rules; review smart-contract alert configurations

GRC Manager

Audit log coverage quarterly; report compliance to CISO; maintain REG-511 entries

All Personnel

Report suspected security events; do not tamper with or disable logging

# 6. Control Mapping

Framework

Control

ISO 27001:2022

A.8.15 Logging, A.8.16 Monitoring activities, A.8.17 Clock synchronisation

NIST CSF 2.0

DE.CM-01 Networks monitored, DE.CM-06 Personnel activity monitored, DE.CM-09 Hardware/software monitored

SOC 2

CC7.2 System monitoring, CC7.3 Evaluation of events, CC7.4 Incident response

NIST SP 800-53

AU-2 Event logging, AU-3 Content of audit records, AU-6 Audit review, SI-4 System monitoring

CIS Controls v8

8.2 Collect audit logs, 8.5 Collect detailed audit logs, 8.11 Conduct audit log reviews

# 7. Exceptions

Exemptions from any mandatory requirement require POL-009 classification E2+ with CISO sign-off and compensating control documentation. Development/sandbox environments may operate at reduced logging (P4 sources only) with GRC Manager approval and annual revalidation.

# Review &amp; Maintenance

Reviewed on a Annual cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

# Version History

Version

Date

Author

Change Summary

v1.0

2026-04-15

Owner (per Document Control)

Initial audit-ready publication — gap-fill per Drive Housekeeping Plan.

# Appendix — Cross-References

POL-003 Access Control Policy

POL-006 Network &amp; Infrastructure Security

PR-203 Incident Response Procedure

REG-509 Incident Register

PLAN-701 Security Improvement Plan
