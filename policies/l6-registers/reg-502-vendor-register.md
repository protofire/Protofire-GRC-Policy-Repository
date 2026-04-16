---
id: "REG-502"
title: "Vendor and Third-Party Register"
type: "Register"
level: "L6"
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

# REG-502 — Vendor and Third-Party Register

Vendor &amp; Third-Party Register

# 0. Document Control

Attribute

Value

Document ID

REG-502

Title

Vendor &amp; Third-Party Register

Hierarchy Level

L6 — Register

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Quarterly

Owner

GRC Manager / Procurement

Approver

Node Owner (NO) / CISO

Classification

Confidential — Internal

Supersedes

None

References

POL-007 Vendor &amp; Third-Party Risk Policy; S-115 Vendor Security Assessment Standard; ISO 27001:2022 A.5.19–A.5.23; NIST CSF 2.0 GV.SC

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

REG-502 is the authoritative enterprise register of every external vendor, processor, sub-processor, cloud provider and third-party service that processes Protofire data, client data, or supports delivery. It is the primary artefact for vendor-risk audits, SOC 2 CC9.2 evidence, and GDPR Art.28 sub-processor disclosures.

# 2. Scope

In scope: all paid and unpaid third parties with access to Protofire or client data, production systems, repositories, credentials, or key-management infrastructure; including SaaS, IaaS, PaaS, open-source-with-support contracts, contractors operating on vendor-owned infrastructure, and DAO-governed services where Protofire is a consumer.

# 3. Register Schema

Field

Description / Domain

Vendor_ID

Format V-{NNN}; immutable

Legal_Name / Trading_Name

Full legal entity name and public trading name if different

Class

Critical | High | Medium | Low — per S-115 §3 classification matrix

Service_Description

Plain-language description of the service consumed

Data_Categories

Personal data | Special-category | Financial | Code/IP | Credentials | Metadata | None

Data_Residency

Primary and DR regions; countries of processing

DPA_Status

Signed (date) | Negotiating | Not required with justification

MSA_SOW_Ref

CLM link; expiry date; notice period

Security_Assessment

S-115 assessment date; score; reassessment due date

Certifications

SOC 2 Type II | ISO 27001 | PCI | HIPAA | FedRAMP — with validity date

SLA / Availability

Contracted availability; RTO; RPO; penalty clause reference

Exit_Plan

Data-export format; deletion SLA; alternative-vendor identified

Business_Owner

Named Protofire owner

Technical_Owner

Named Protofire technical contact

Risk_Rating

Inherited from last S-115 assessment

Status

Active | Sunsetting | Terminated

Last_Review / Next_Review

Dates per cadence in §6

# 4. Roles &amp; Responsibilities

Role

Responsibility

GRC Manager

Accountable for register integrity and cadence.

Procurement / Commercial

Responsible for MSA/SOW/DPA tracking and expiry alerts.

CISO

Consulted on Critical and High class entries; approves risk-accept decisions above tier thresholds.

DPO

Consulted on DPA completeness for vendors processing personal data.

Business Owner

Confirms service is still in use at each review cycle.

Technical Owner

Provides integration / access topology updates.

Internal Audit

Verifies coverage against purchase ledger at least annually.

# 5. Control Mapping

Framework

Clause / Control

ISO/IEC 27001:2022

A.5.19 Information security in supplier relationships; A.5.20 Addressing security within supplier agreements; A.5.21 ICT supply chain; A.5.22 Monitoring, review &amp; change management; A.5.23 Cloud services

NIST CSF 2.0

GV.SC-01..10 Supply Chain Risk Management

SOC 2

CC9.2 Vendor/business-partner risk assessment &amp; monitoring

GDPR

Art.28 Processor obligations; Art.30(1)(e) Records of transfers

# 6. KRIs &amp; Thresholds

KRI

Target

Amber / Red

Coverage vs. purchase ledger

100%

95% Amber / 90% Red

DPA signed for vendors processing personal data

100%

98% Amber / 95% Red

S-115 assessment within cadence (Critical ≤ 12 mo; High ≤ 18 mo; Med ≤ 24 mo)

100%

95% Amber / 90% Red

Open Critical / High findings past due

0

1 Amber / 3 Red

Vendor contract expiring ≤ 30 days without renewal decision

0

1 Amber / 3 Red

# 7. Evidence &amp; Recordkeeping

Executed MSAs / SOWs / DPAs (links to CLM)

S-115 security assessments per vendor (most recent + prior)

SOC 2 / ISO 27001 reports per vendor (attested copies)

Quarterly vendor-review minutes (GRC Manager + CISO)

Vendor termination records with data-return / deletion attestations

# 8. Exceptions

Any exception to the mandatory fields or review cadence of this register requires POL-009 classification E2+ with CISO co-sign. HS-01/HS-02 hard stops are non-exceptable.

# Review &amp; Maintenance

Reviewed on a Quarterly cadence by the named Owner, and upon material change, regulatory change, audit finding, or supersession of any referenced document. Review actions are recorded in REG-511 and approved by the named Approver.

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

POL-007 Vendor &amp; Third-Party Risk Policy

S-115 Vendor Security Assessment Standard

REG-506 Exception &amp; Waiver Register

POL-011 Data Protection &amp; Privacy Policy (DPA requirements)

CL-PHASE-001 Lifecycle Checklist
