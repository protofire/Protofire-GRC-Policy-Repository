---
id: "DPA-001"
title: "Data Processing Agreement Template"
type: "Legal Template"
level: "L2"
version: "1.0"
status: "Draft"
effective_date: "Pending approval"
review_cycle: "Annual"
owner: "CISO-DPO"
approver: "CISO advisory"
classification: "Confidential — Internal"
last_change: "2026-04-16"
last_approval: "Pending"
source: "reference_policies (DOCX conversion)"
---

# DPA-001 — Data Processing Agreement Template

Data Processing Agreement Template

# 0. Document Control

Attribute

Value

Document ID

DPA-001

Title

Data Processing Agreement Template

Hierarchy Level

L5 - Template

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

DPO / CISO

Approver

Node Owner / CLO

Classification

Confidential - Internal

Supersedes

—

References

POL-011 Data Protection &amp; Privacy Policy; GDPR Art.28; CCPA/CPRA; LGPD Art.39; ISO 27701:2019; SCCs 2021/914

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

DPA-001 is the standard Data Processing Agreement template used when Protofire acts as a data processor on behalf of a client (data controller). It ensures compliance with GDPR Art.28, CCPA/CPRA service provider obligations, LGPD Art.39, and aligns with POL-011 Data Protection &amp; Privacy Policy.

# 2. When to Use

Any engagement where Protofire processes personal data on behalf of a client

Sub-processor appointments where Protofire onboards third parties to assist with client data

Mandatory attachment to MSA per MSA-001 clause MSA-SEC-02

Must be executed before any personal data processing begins (Gate G2 prerequisite)

# 3. DPA Clauses

## 3.1 Definitions

[DPA-DEF] Definitions shall align with GDPR Art.4, including: Personal Data, Processing, Controller, Processor, Sub-processor, Data Subject, Supervisory Authority, International Transfer. Where engagement involves non-EU data subjects, equivalent definitions from applicable law (CCPA, LGPD) shall apply.

## 3.2 Subject Matter &amp; Duration

[DPA-01] This DPA governs the processing of Personal Data by Processor on behalf of Controller as described in Annex I (Processing Details). Duration: co-terminous with the MSA/SOW, plus the data retention period specified in Annex I.

## 3.3 Processing Instructions

[DPA-02] Processor shall process Personal Data only on documented instructions from Controller, including with regard to transfers to third countries. Processor shall inform Controller if, in Processor\&apos;s opinion, an instruction infringes applicable data protection law. Processing outside documented instructions requires prior written authorisation from Controller.

## 3.4 Confidentiality

[DPA-03] Processor shall ensure that all personnel authorised to process Personal Data have committed themselves to confidentiality or are under appropriate statutory obligation. Access shall be limited to personnel who need it for the performance of the engagement (least-privilege, per POL-003).

## 3.5 Security Measures

[DPA-04] Processor shall implement technical and organisational measures as described in Annex II (Security Measures), including: encryption (STD-104), access control (POL-003), logging (STD-102), incident response (PR-203), backup (PLAN-703), and regular security testing (STD-103). Measures shall be reviewed annually and updated to reflect current threats.

## 3.6 Sub-processors

[DPA-05] Processor shall not engage a Sub-processor without prior specific or general written authorisation of Controller. In the case of general authorisation, Processor shall provide Controller with [30] days notice of intended changes, during which Controller may object. Processor shall impose equivalent data protection obligations on Sub-processors.

## 3.7 Data Subject Rights

[DPA-06] Processor shall assist Controller in responding to Data Subject requests (access, rectification, erasure, portability, restriction, objection) within [5] business days of request. Processor shall implement technical measures to enable Controller to fulfil DSR obligations, including data export and deletion capabilities.

## 3.8 Breach Notification

[DPA-07] Processor shall notify Controller of any Personal Data breach without undue delay and within [24/48] hours of becoming aware. Notification shall include: nature of breach, categories and approximate number of data subjects affected, likely consequences, measures taken or proposed. Processor shall cooperate with Controller\&apos;s notification to Supervisory Authority (Art.33) and Data Subjects (Art.34).

## 3.9 Data Protection Impact Assessment

[DPA-08] Processor shall assist Controller with DPIAs and prior consultation with Supervisory Authorities where required by Art.35-36, providing information about processing operations, security measures, and sub-processor arrangements.

## 3.10 International Transfers

[DPA-09] Transfers of Personal Data outside the EEA shall be made only in accordance with Chapter V of the GDPR: (a) adequacy decision, (b) Standard Contractual Clauses (SCCs 2021/914, Annex III), (c) Binding Corporate Rules, or (d) explicit consent of Data Subjects. Processor shall conduct and document a Transfer Impact Assessment for each transfer destination.

## 3.11 Return &amp; Deletion

[DPA-10] Upon termination of processing or Controller instruction, Processor shall: (a) return all Personal Data to Controller in a structured, machine-readable format, and (b) delete all copies within [30] days, unless retention is required by applicable law. Processor shall certify deletion in writing.

## 3.12 Audit

[DPA-11] Processor shall make available to Controller all information necessary to demonstrate compliance with Art.28 obligations, and allow for and contribute to audits and inspections conducted by Controller or an auditor mandated by Controller. Processor may satisfy this obligation by providing: (a) existing audit reports (SOC 2, ISO 27001), (b) completed security questionnaire, (c) on-site or remote audit with [30] days notice.

# 4. Annexes

## Annex I - Processing Details (to be completed per engagement)

Field

Value (Template)

Categories of Data Subjects

[e.g., end users of Client platform, Client employees]

Categories of Personal Data

[e.g., wallet addresses, email addresses, transaction history]

Special Categories

[Typically none for blockchain engagements; specify if applicable]

Processing Activities

[e.g., smart contract development, monitoring, analytics]

Purpose of Processing

[e.g., delivery of services under SOW dated [date]]

Duration

[Co-terminous with MSA + [30] day deletion period]

Retention Period

[Per POL-008 section 4.3; specify engagement-specific requirements]

## Annex II - Security Measures (standard reference)

Encryption: AES-256 at rest, TLS 1.2+ in transit (STD-104)

Access Control: RBAC, MFA, quarterly review (POL-003, STD-101)

Logging &amp; Monitoring: centralised SIEM, 12-month retention (STD-102)

Incident Response: 15-min ack, 24h notification (PR-203, MSA-001)

Backup &amp; Recovery: RPO 1h, RTO 4h for client systems (PLAN-702/703)

Secure Development: SAST, fuzz, code review (STD-103)

Training: annual security awareness (REG-507)

Physical Security: remote-first; cloud provider certifications relied upon

## Annex III - Standard Contractual Clauses

Where required, the EU SCCs (Commission Implementing Decision 2021/914) shall be incorporated by reference. Module selection: Module 2 (Controller-to-Processor) for standard engagements; Module 3 (Processor-to-Processor) for sub-processor chains. UK IDTA supplement applied for UK data subjects.

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

POL-011 Data Protection &amp; Privacy Policy

MSA-001 Security Clauses Template

GL-304 Privacy by Design Guideline

REG-502 Vendor &amp; Third-Party Register
