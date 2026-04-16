---
id: "IAP-001"
title: "Internal Audit Programme"
type: "Programme"
level: "L0"
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

# IAP-001 — Internal Audit Programme

# Internal Audit Programme (2026–2028)

Field

Value

Document ID

IAP-001

Version

1.0-draft

Effective date

On approval

Review cadence

Annually

Owner

CISO

Approver

vCISO (independent) + Board

Classification

Confidential — Internal

Status

Draft — awaiting review

Issued

2026-04-15

# 1. Purpose

This programme governs Protofire's internal audit activity in support of ISMS conformance (ISO/IEC 27001), ISO 22301 business continuity, GDPR obligations, and contractual client-security obligations. It defines the audit universe, cadence, independence rules, reporting lines, and escalation thresholds.

Per the Security Brief §7 (Compliance and Evidence Management), internal audits occur bi-annually at minimum, with subject-matter experts from the Internal Auditing Team who are not directly involved in the projects or controls under review.

# 2. Scope and audit universe

The audit universe covers every L0–L6 document in the GRC repository, every operational control in the Control Catalogue (40+ items, including the 20 mandatory controls C01–C20), and every active engagement classified Tier 2 or higher. Low-risk T1 engagements are audited by sampling (minimum one engagement per node per year).

# 3. Independence requirements

The lead auditor for any engagement must not be in the project's RACI or have been a contributor in the preceding 12 months.

Key/treasury, secure delivery, and data-protection audits require either vCISO or an external assessor as lead (CISO cannot audit their own controls).

The Node Owner under review cannot override the auditor's findings.

Reports are shared with the GRC Committee before remediation negotiation.

# 4. Three-year rolling schedule

The schedule spans twelve audit engagements over three years (2026 Q3 – 2028 Q4), covering every high-impact domain at least once and every T3+ engagement annually. The programme resets each year; residual items roll forward.

#

Audit title

Scope

Lead auditor

Quarter

Year

Criteria

Reporting to

1

ISMS Governance &amp; Scope

L0-1, L0-2, L0-4, SoA

vCISO (independent)

Q3

2026

ISO 27001:2022 §4–10

GRC Committee

2

Risk Management

POL-003, L1-ERM-001, REG-501

Internal Audit Team

Q4

2026

ISO 31000; OPS-001

GRC Committee

3

Access &amp; SoD

POL-004, L2-ACCESS-203, sod-matrix

Internal Audit Team

Q1

2027

POL-004; Annex A 5.15, 5.16, 8.2

CISO

4

Secure Delivery (Web3)

L1-SDLC-003, POL-006, L3-TEST-204

External assessor (Tier 3+)

Q2

2027

L1-SDLC-003; OWASP SCSVS

CISO + CEO

5

Key &amp; Treasury

L1-KEY-005, CL-411 Signing Ceremony

vCISO + Treasury auditor

Q2

2027

L1-KEY-005; C02 cold storage

GRC Committee

6

Incident Response

POL-017, L2-INC-201, incident registry

Internal Audit Team

Q3

2027

L2-INC-201; NIST 800-61

CISO

7

Vendor &amp; Third-Party Risk

POL-007, S-115

Internal Audit Team

Q3

2027

POL-007; Annex A 5.19–5.23

GRC Committee

8

Business Continuity &amp; DR

L1-BC-008, POL-013, L2-TEST-204

vCISO

Q4

2027

ISO 22301; L1-BC-008

GRC Committee

9

Data Protection (GDPR)

POL-011, REG-505, PR-208, PR-209, CL-409

DPO (who is CISO) + Legal

Q1

2028

GDPR Arts. 5, 24, 30, 32–34

CEO + Board

10

Change Management

POL-005, L2-CHANGE-205

Internal Audit Team

Q2

2028

POL-005 (C1–C5 classification)

CISO

11

Vulnerability Management

L2-VULN-202, L1-INFRA-009

Internal Audit Team

Q3

2028

L2-VULN-202; CVSS v3.1

CISO

12

Evidence &amp; Recordkeeping

L1-EVID-004, REG-511, Evidence Calendar

vCISO

Q4

2028

L1-EVID-004; ISO 17021-1:2015

GRC Committee

# 5. Audit methodology

## 5.1 Planning

Auditor drafts audit plan using the template (Appendix A): objectives, criteria, sampling approach, evidence requirements, risk-rated scope.

CISO or vCISO approves the plan and confirms auditor independence.

Auditee receives plan and the evidence request list at least ten working days before fieldwork.

## 5.2 Fieldwork

Evidence gathered through document review, system-configuration inspection, walk-throughs, and interviews.

Findings logged in the working paper with unique ID, severity (Critical/High/Medium/Low), criteria reference, and supporting evidence link in the Evidence Calendar.

Preliminary findings reviewed with auditee before closing meeting to verify factual accuracy.

## 5.3 Reporting

Draft report issued within ten working days of fieldwork close.

Auditee has five working days to comment and propose remediation.

Final report delivered to the GRC Committee and, for CEO/Board-level findings, to the Board.

## 5.4 Remediation and follow-up

Critical findings: 30-day remediation target, interim compensating controls within 48 hours.

High: 60 days. Medium: 90 days. Low: next planned review.

Follow-up audit verifies closure; unresolved findings age into the next year's plan.

# 6. Escalation thresholds

Hard Stop triggered during audit (HS-01 to HS-07): notify CEO within 24 hours.

Any control rated Critical non-conformant on the SoA: notify vCISO within 24 hours.

Three or more Medium+ findings in the same control domain: open an NC-Trend case for GRC Committee review.

# 7. Resourcing

Internal audits are staffed from the [Security Team roster](https://docs.google.com/spreadsheets/d/1yPTJDAlrwC0Dm7qn_c9oCtUvvcynfypU9BHXNPOmS5w/edit), filtered for members not embedded in the audited project. For specialised domains (smart-contract security, cryptographic key ceremonies), the programme contracts external assessors under L2-ASSURE-103.

# 8. Reporting to Board

vCISO produces a quarterly summary to the Board covering: audits completed, open findings by severity, remediation status against SLA, thematic risk observations, and proposed changes to the audit universe. An annual ISMS management-review pack consolidates all internal and external audit outcomes for the Board's ISO 27001 management review (Clause 9.3).

# 9. Related documents

L1-EVID-004 Evidence and Recordkeeping Standard

L2-ASSURE-103 External Assurance Procedure

REG-511 Document Registry

REG-512 Evidence Calendar (NEW)

POL-010 Monitoring and Assurance Policy
