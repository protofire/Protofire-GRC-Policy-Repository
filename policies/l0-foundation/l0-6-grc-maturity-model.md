---
id: "L0-6"
title: "GRC Maturity Model"
type: "Model"
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

# L0-6 — GRC Maturity Model

GRC Maturity Model

# 0. Document Control

Attribute

Value

Document ID

L0-6

Title

GRC Maturity Model

Hierarchy Level

L0 -- Foundation

Version

1.0

Status

Approved (pending NOC sign-off)

Effective Date

2026-04-15

Review Cycle

Annual

Owner

CISO / GRC Manager

Approver

Node Owner

Classification

Confidential -- Internal

Supersedes

—

References

GRC-MASTER-001; L0-3 GRC Charter; ISO 27001:2022 §10; NIST CSF 2.0; CMMI

Last Change

2026-04-15

Audit Readiness

Audit-ready v1.0 — generated 2026-04-15; gap-fill batch per Drive Housekeeping Plan §2D/2E.

# 1. Purpose

L0-6 defines the maturity model used to assess, benchmark and drive continuous improvement of Protofire&apos;s GRC capabilities. It provides a consistent vocabulary for measuring current state, setting targets, and reporting progress to leadership.

# 2. Maturity Levels

The model uses five maturity levels aligned with CMMI and adapted for GRC:

Level

Name

Description

ML-1

Initial

Processes are ad hoc, reactive, and dependent on individual heroics. No formal documentation. Compliance is incidental.

ML-2

Managed

Core policies exist and are approved. Key risks are identified. Basic registers are maintained. Compliance activities are planned but not consistently executed.

ML-3

Defined

Full policy hierarchy in place (L0-L6). Procedures are documented and followed. Registers are complete and reviewed on cadence. Training programme operational. Metrics collected.

ML-4

Quantitatively Managed

KRIs are baselined with statistical targets. Processes are measured and controlled. Automated monitoring in place. Exception trends analysed. Audit findings resolved within SLA.

ML-5

Optimising

Continuous improvement is systematic. Lessons learned feed back into policy updates. Predictive risk analytics operational. GRC function is a competitive differentiator for client engagements.

# 3. Assessment Domains

Each GRC domain is assessed independently. Current state and target are tracked per domain:

Domain

Current (2026-Q2)

Target (2026-Q4)

Key Gap / Action

Policy &amp; Governance

ML-2

ML-3

Complete L1 policy set ✓; publish all L2 standards and L3 guidelines

Risk Management

ML-2

ML-3

Operationalise REG-501 with quarterly reviews; implement risk heat-map dashboard

Compliance &amp; Audit

ML-1

ML-2

Establish internal audit programme; SOC 2 Type II readiness assessment

Incident Management

ML-2

ML-3

Automate incident detection; establish MTTD/MTTR baselines via REG-509

Vendor &amp; Third-Party

ML-1

ML-2

Complete REG-502 population; conduct first-round vendor assessments per S-115

Asset Management

ML-1

ML-2

Populate REG-503 CMDB; classify all assets per POL-005 §4.2

Change &amp; Release

ML-2

ML-3

Automate CI/CD security gates; full REG-504 traceability

Training &amp; Awareness

ML-2

ML-3

Launch LMS; achieve 100% completion rate per REG-507

Access Control

ML-2

ML-3

Quarterly access reviews via REG-508; implement RBAC across all critical systems

Business Continuity

ML-1

ML-2

Publish BCP; conduct tabletop exercise; establish RPO/RTO targets

Privacy &amp; Data Protection

ML-2

ML-3

Complete ROPA; conduct first DPIA; operationalise DSR workflow

Smart-Contract Security

ML-2

ML-3

Standardise threat model template; 100% audit coverage for mainnet deployments

# 4. Assessment Methodology

Assessments are conducted quarterly by the GRC Manager with CISO review, using the following process:

Step 1 -- Evidence Collection: gather register data, policy review records, incident logs, training records, audit findings

Step 2 -- Domain Scoring: rate each domain against the maturity level criteria using a preponderance-of-evidence standard

Step 3 -- Gap Analysis: identify specific gaps between current level and target level

Step 4 -- Action Planning: for each gap, define specific remediation actions with owner, deadline and success criteria

Step 5 -- Leadership Review: present assessment to NO with recommended resource allocation

Step 6 -- Tracking: enter actions into REG-511 and track to completion

# 5. Scoring Rubric

Each maturity level has three evidence gates that must all be satisfied:

Level

Documentation Gate

Execution Gate

Measurement Gate

ML-1

None required

Activity exists informally

No metrics

ML-2

Policy/standard published and approved

Process executed ≥ 2 cycles

Basic metrics collected

ML-3

Full hierarchy (policy → procedure → guideline)

Process executed consistently; &lt; 5% deviation

KRIs defined; dashboards operational

ML-4

All ML-3 + exception analysis documented

Statistical process control; automated where feasible

Trend analysis; predictive indicators

ML-5

All ML-4 + continuous improvement records

Process adapts proactively to environment changes

ROI demonstrated; benchmarked externally

# 6. Reporting

Maturity assessment results are reported as follows:

Quarterly Maturity Scorecard -- 12-domain radar chart with current vs. target overlay; delivered to NO

Annual Maturity Report -- full narrative assessment with year-over-year trend; included in GRC Annual Review

Board Summary -- single-page executive view: overall maturity score, top 3 gaps, resource requests

Client-Facing Excerpt -- sanitised maturity summary for inclusion in SEC-POSTURE-001 and RFP responses (ML score only, no gap details)

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

GRC-MASTER-001 Enterprise GRC Framework

L0-3 GRC Charter

REG-511 Document Control Register

PLAN-701 Security Improvement Plan
