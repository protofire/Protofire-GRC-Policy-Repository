"""
Protofire GRC Repository Actualization Script
Scans reference_policies, converts missing DOCX→MD, writes change log.
"""
import os, zipfile, re, json, datetime
from pathlib import Path

REPO = Path(r"C:\Work\protofire\Protofire-GRC-Policy-Repository")
REF  = REPO / "reference_policies"
LOG_PATH = REPO / "repository_update_log.txt"
RUN_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# ── Mapping: ref DOCX basename → (target_folder_rel, target_md_name, meta_dict) ──
MAPPING = {
    # L0 Foundation
    "L0-1_GRC_Charter_Information_Security_v1.0.docx":
        ("policies/l0-foundation", "l0-1-grc-charter.md",
         dict(id="L0-1", title="GRC Charter — Information Security", type="Charter", level="L0", status="Draft", owner="CISO", version="1.0")),
    "L0-2_GRC_Programme_Governance_Charter_v1.0.docx":
        ("policies/l0-foundation", "l0-2-programme-governance-charter.md",
         dict(id="L0-2", title="GRC Programme Governance Charter", type="Charter", level="L0", status="Draft", owner="GRC-Manager", version="1.0")),
    "L0-3_GRC_Charter.docx":
        ("policies/l0-foundation", "l0-3-grc-charter.md",
         dict(id="L0-3", title="GRC Charter", type="Charter", level="L0", status="Draft", owner="CISO", version="1.0")),
    "L0-4_ISMS_Scope_Statement.docx":
        ("policies/l0-foundation", "l0-4-isms-scope-statement.md",
         dict(id="L0-4", title="ISMS Scope Statement", type="Scope Statement", level="L0", status="Approved", owner="CISO", version="1.0")),
    "L0-5_Risk_Appetite_Statement.docx":
        ("policies/l0-foundation", "l0-5-risk-appetite-statement.md",
         dict(id="L0-5", title="Risk Appetite Statement", type="Risk Statement", level="L0", status="Approved", owner="CISO", version="1.0")),
    "L0-6_GRC_Maturity_Model.docx":
        ("policies/l0-foundation", "l0-6-grc-maturity-model.md",
         dict(id="L0-6", title="GRC Maturity Model", type="Model", level="L0", status="Draft", owner="CISO", version="1.0")),
    "GRC-MASTER-001_Enterprise_GRC_Framework_v1.1.docx":
        ("policies/l0-foundation", "grc-master-001-enterprise-framework.md",
         dict(id="GRC-MASTER-001", title="Enterprise GRC Framework", type="Master Framework", level="L0", status="Draft", owner="CISO", version="1.1")),
    "GRC-PF-001_Governance_and_Security_Policy_Framework.docx":
        ("policies/l0-foundation", "grc-pf-001-policy-framework.md",
         dict(id="GRC-PF-001", title="Governance and Security Policy Framework", type="Framework", level="L0", status="Draft", owner="CISO", version="1.0")),
    "GRC-CONC-001_Document_Numbering_Concordance_Table.docx":
        ("policies/l0-foundation", "grc-conc-001-concordance-table.md",
         dict(id="GRC-CONC-001", title="Document Numbering Concordance Table", type="Reference Table", level="L0", status="Generated", owner="GRC-Manager", version="1.0")),
    "SOA-001_Statement_of_Applicability.docx":
        ("policies/l0-foundation", "soa-001-statement-of-applicability.md",
         dict(id="SOA-001", title="Statement of Applicability", type="ISO Statement", level="L0", status="Draft", owner="CISO", version="1.0")),
    "IAP-001_Internal_Audit_Programme.docx":
        ("policies/l0-foundation", "iap-001-internal-audit-programme.md",
         dict(id="IAP-001", title="Internal Audit Programme", type="Programme", level="L0", status="Draft", owner="CISO", version="1.0")),
    "RACI-001_Enterprise_RACI.docx":
        ("policies/l0-foundation", "raci-001-enterprise-raci.md",
         dict(id="RACI-001", title="Enterprise RACI Matrix", type="RACI", level="L0", status="Draft", owner="CISO", version="1.0")),
    "RACI-002_Track_B_RACI_Matrix.docx":
        ("policies/l0-foundation", "raci-002-track-b-raci.md",
         dict(id="RACI-002", title="Track B RACI Matrix", type="RACI", level="L0", status="Draft", owner="CISO", version="1.0")),
    "SEC-POSTURE-001_Security_Posture_Template.docx":
        ("policies/l0-foundation", "sec-posture-001-security-posture-template.md",
         dict(id="SEC-POSTURE-001", title="Security Posture Template", type="Template", level="L0", status="Draft", owner="CISO", version="1.0")),
    # L1 Policies
    "POL-001_Project_Governance_Policy.docx":
        ("policies/l1-policies", "pol-001-project-governance.md",
         dict(id="POL-001", title="Project Governance Policy", type="Policy", level="L1", status="Draft", owner="Node-Owner", version="1.0")),
    "POL-002_Information_Security_Policy.docx":
        ("policies/l1-policies", "pol-002-information-security.md",
         dict(id="POL-002", title="Information Security Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-003_Risk_Management_Policy.docx":
        ("policies/l1-policies", "pol-003-risk-management.md",
         dict(id="POL-003", title="Risk Management Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-004_Access_Control_SoD_Policy.docx":
        ("policies/l1-policies", "pol-004-access-control-sod.md",
         dict(id="POL-004", title="Access Control and Segregation of Duties Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-005_Change_Management_Policy.docx":
        ("policies/l1-policies", "pol-005-change-management.md",
         dict(id="POL-005", title="Change Management Policy", type="Policy", level="L1", status="Draft", owner="Node-Owner", version="1.0")),
    "POL-006_Testing_QA_Policy.docx":
        ("policies/l1-policies", "pol-006-testing-qa.md",
         dict(id="POL-006", title="Testing and QA Policy", type="Policy", level="L1", status="Draft", owner="TL", version="1.0")),
    "POL-007_Vendor_Third_Party_Risk_Policy.docx":
        ("policies/l1-policies", "pol-007-vendor-third-party-risk.md",
         dict(id="POL-007", title="Vendor and Third-Party Risk Policy", type="Policy", level="L1", status="Draft", owner="Node-Owner", version="1.0")),
    "POL-008_Documentation_Records_Policy.docx":
        ("policies/l1-policies", "pol-008-documentation-records.md",
         dict(id="POL-008", title="Documentation and Records Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-009_Exception_Deviation_Policy.docx":
        ("policies/l1-policies", "pol-009-exception-deviation.md",
         dict(id="POL-009", title="Exception and Deviation Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-010_Monitoring_Assurance_Policy.docx":
        ("policies/l1-policies", "pol-010-monitoring-assurance.md",
         dict(id="POL-010", title="Monitoring and Assurance Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-011_Data_Protection_Privacy_Policy.docx":
        ("policies/l1-policies", "pol-011-data-protection-privacy.md",
         dict(id="POL-011", title="Data Protection and Privacy Policy", type="Policy", level="L1", status="Draft", owner="CISO-DPO", version="1.0")),
    "POL-012_Acceptable_Use_Policy.docx":
        ("policies/l1-policies", "pol-012-acceptable-use.md",
         dict(id="POL-012", title="Acceptable Use Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-013_Business_Continuity_Policy.docx":
        ("policies/l1-policies", "pol-013-business-continuity.md",
         dict(id="POL-013", title="Business Continuity Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-014_Cryptographic_Controls_Policy.docx":
        ("policies/l1-policies", "pol-014-cryptographic-controls.md",
         dict(id="POL-014", title="Cryptographic Controls Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-015_Personnel_Security_Policy.docx":
        ("policies/l1-policies", "pol-015-personnel-security.md",
         dict(id="POL-015", title="Personnel Security Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-016_Physical_Environmental_Security_Policy.docx":
        ("policies/l1-policies", "pol-016-physical-environmental-security.md",
         dict(id="POL-016", title="Physical and Environmental Security Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "POL-017_Incident_Management_Policy.docx":
        ("policies/l1-policies", "pol-017-incident-management.md",
         dict(id="POL-017", title="Incident Management Policy", type="Policy", level="L1", status="Draft", owner="CISO", version="1.0")),
    "DAO-001_DAO-Governed_Platforms_Privacy_Policy_Template.docx":
        ("policies/l1-policies", "dao-001-dao-privacy-policy-template.md",
         dict(id="DAO-001", title="DAO-Governed Platforms Privacy Policy Template", type="Policy Template", level="L1", status="Draft", owner="CISO-DPO", version="1.0")),
    # L1 Standards
    "L1-ERM-001_Enterprise_Risk_Governance_and_Acceptance_Authority_Standard_Web3.docx":
        ("policies/l1-standards", "l1-erm-001-risk-governance.md",
         dict(id="L1-ERM-001", title="Enterprise Risk Governance and Acceptance Authority Standard (Web3)", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "L1-ENG-002_Client_Rating_and_Commercial_Guardrails_Standard.docx":
        ("policies/l1-standards", "l1-eng-002-client-rating.md",
         dict(id="L1-ENG-002", title="Client Rating and Commercial Guardrails Standard", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "L1-SDLC-003_Secure_Delivery_Baseline_for_Web3_DeFi.docx":
        ("policies/l1-standards", "l1-sdlc-003-secure-delivery.md",
         dict(id="L1-SDLC-003", title="Secure Delivery Baseline for Web3/DeFi", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "L1-EVID-004_Evidence_and_Recordkeeping_Standard.docx":
        ("policies/l1-standards", "l1-evid-004-evidence-recordkeeping.md",
         dict(id="L1-EVID-004", title="Evidence and Recordkeeping Standard", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "L1-KEY-005_Key_Treasury_and_Signing_Ceremonies_Standard.docx":
        ("policies/l1-standards", "l1-key-005-key-treasury.md",
         dict(id="L1-KEY-005", title="Key Treasury and Signing Ceremonies Standard", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "L1-BC-008_Business_Continuity_Standard.docx":
        ("policies/l1-standards", "l1-bc-008-business-continuity.md",
         dict(id="L1-BC-008", title="Business Continuity Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "L1-INFRA-009_Infrastructure_Security_Baseline_Standard.docx":
        ("policies/l1-standards", "l1-infra-009-infrastructure-security.md",
         dict(id="L1-INFRA-009", title="Infrastructure Security Baseline Standard", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "L1-HR-010_Personnel_Security_Standard.docx":
        ("policies/l1-standards", "l1-hr-010-personnel-security.md",
         dict(id="L1-HR-010", title="Personnel Security Standard", type="Standard", level="L1-STD", status="Approved", owner="CISO", version="1.0")),
    "OPS-001_Project_Risk_Scoring_Framework.docx":
        ("policies/l1-standards", "ops-001-risk-scoring-framework.md",
         dict(id="OPS-001", title="Project Risk Scoring Framework", type="Framework", level="L1-STD", status="Approved", owner="GRC-Committee", version="1.0")),
    "S-109_Data_Classification_Standard.docx":
        ("policies/l1-standards", "s-109-data-classification.md",
         dict(id="S-109", title="Data Classification Standard", type="Standard", level="L1-STD", status="Generated", owner="CISO", version="1.0")),
    "S-115_Vendor_Security_Assessment_Standard.docx":
        ("policies/l1-standards", "s-115-vendor-security-assessment.md",
         dict(id="S-115", title="Vendor Security Assessment Standard", type="Standard", level="L1-STD", status="Generated", owner="CISO", version="1.0")),
    "STD-101_Delivery_Security_Standard.docx":
        ("policies/l1-standards", "std-101-delivery-security.md",
         dict(id="STD-101", title="Delivery Security Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "STD-102_Logging_Monitoring_Standard.docx":
        ("policies/l1-standards", "std-102-logging-monitoring.md",
         dict(id="STD-102", title="Logging and Monitoring Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "STD-103_Secure_Development_Standard.docx":
        ("policies/l1-standards", "std-103-secure-development.md",
         dict(id="STD-103", title="Secure Development Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "STD-104_Cryptographic_Controls_Standard.docx":
        ("policies/l1-standards", "std-104-cryptographic-controls.md",
         dict(id="STD-104", title="Cryptographic Controls Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "STD-105_Transaction_Verification_Simulation_Standard.docx":
        ("policies/l1-standards", "std-105-transaction-verification.md",
         dict(id="STD-105", title="Transaction Verification and Simulation Standard", type="Standard", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    "STD-110_KRI_Dashboard_Specification.docx":
        ("policies/l1-standards", "std-110-kri-dashboard.md",
         dict(id="STD-110", title="KRI Dashboard Specification", type="Specification", level="L1-STD", status="Draft", owner="CISO", version="1.0")),
    # L2 Procedures
    "L2-DEL-101_8-Stage_Delivery_Governance_Procedure_Track_A_B.docx":
        ("policies/l2-procedures", "l2-del-101-delivery-governance.md",
         dict(id="L2-DEL-101", title="8-Stage Delivery Governance Procedure (Track A/B)", type="Procedure", level="L2", status="Approved", owner="Head-of-Delivery", version="1.0")),
    "L2-RISK-102_Delivery_Risk_Operations_Procedure.docx":
        ("policies/l2-procedures", "l2-risk-102-risk-operations.md",
         dict(id="L2-RISK-102", title="Delivery Risk Operations Procedure", type="Procedure", level="L2", status="Approved", owner="Head-of-Risk", version="1.0")),
    "L2-ASSURE-103_External_Assurance_Procedure_Audit_and_Bug_Bounty.docx":
        ("policies/l2-procedures", "l2-assure-103-external-assurance.md",
         dict(id="L2-ASSURE-103", title="External Assurance Procedure (Audit and Bug Bounty)", type="Procedure", level="L2", status="Approved", owner="CISO", version="1.0")),
    "L2-INC-201_Incident_Response_Procedure.docx":
        ("policies/l2-procedures", "l2-inc-201-incident-response.md",
         dict(id="L2-INC-201", title="Incident Response Procedure", type="Procedure", level="L2", status="Draft", owner="CISO", version="1.0")),
    "L2-VULN-202_Vulnerability_Management_Procedure.docx":
        ("policies/l2-procedures", "l2-vuln-202-vulnerability-management.md",
         dict(id="L2-VULN-202", title="Vulnerability Management Procedure", type="Procedure", level="L2", status="Draft", owner="CISO", version="1.0")),
    "L2-ACCESS-203_Access_Management_Procedure_Joiner_Mover_Leaver.docx":
        ("policies/l2-procedures", "l2-access-203-jml.md",
         dict(id="L2-ACCESS-203", title="Access Management Procedure (Joiner/Mover/Leaver)", type="Procedure", level="L2", status="Draft", owner="CISO", version="1.0")),
    "L2-TEST-204_BCM_DR_Testing_Standard.docx":
        ("policies/l2-procedures", "l2-test-204-bcm-dr-testing.md",
         dict(id="L2-TEST-204", title="BCM/DR Testing Standard", type="Standard", level="L2", status="Draft", owner="CISO", version="1.0")),
    "L2-CHANGE-205_Change_Management_Procedure.docx":
        ("policies/l2-procedures", "l2-change-205-change-management.md",
         dict(id="L2-CHANGE-205", title="Change Management Procedure", type="Procedure", level="L2", status="Draft", owner="CISO", version="1.0")),
    "PR-208_Breach_Notification_Procedure.docx":
        ("policies/l2-procedures", "pr-208-breach-notification.md",
         dict(id="PR-208", title="Breach Notification Procedure", type="Procedure", level="L2", status="Generated", owner="CISO-DPO", version="1.0")),
    "PR-209_DSR_Handling_Procedure.docx":
        ("policies/l2-procedures", "pr-209-dsr-handling.md",
         dict(id="PR-209", title="Data Subject Request Handling Procedure", type="Procedure", level="L2", status="Generated", owner="CISO-DPO", version="1.0")),
    "PR-210_Key_Compromise_Response_Procedure.docx":
        ("policies/l2-procedures", "pr-210-key-compromise-response.md",
         dict(id="PR-210", title="Key Compromise Response Procedure", type="Procedure", level="L2", status="Draft", owner="CISO", version="1.0")),
    # L3 Work Instructions
    "GL-304_Privacy_by_Design_Guideline.docx":
        ("policies/l3-work-instructions", "gl-304-privacy-by-design.md",
         dict(id="GL-304", title="Privacy by Design Guideline", type="Guideline", level="L3", status="Generated", owner="CISO-DPO", version="1.0")),
    "GL-305_Signer_OPSEC_Guideline.docx":
        ("policies/l3-work-instructions", "gl-305-signer-opsec.md",
         dict(id="GL-305", title="Signer OPSEC Guideline", type="Guideline", level="L3", status="Draft", owner="CISO", version="1.0")),
    "L3-TEST-204_Test_Evidence_Standard.docx":
        ("policies/l3-work-instructions", "l3-test-204-test-evidence.md",
         dict(id="L3-TEST-204", title="Test Evidence Standard", type="Standard", level="L3", status="Approved", owner="TL", version="1.0")),
    # L4 Plans
    "PLAN-701_Tabletop_IR_Exercise_Plan.docx":
        ("policies/l4-plans", "plan-701-tabletop-ir-exercise.md",
         dict(id="PLAN-701", title="Tabletop IR Exercise Plan", type="Plan", level="L4", status="Draft", owner="CISO", version="1.0")),
    "PLAN-702_Business_Continuity_Plan.docx":
        ("policies/l4-plans", "plan-702-business-continuity-plan.md",
         dict(id="PLAN-702", title="Business Continuity Plan", type="Plan", level="L4", status="Draft", owner="CISO", version="1.0")),
    "PLAN-703_Disaster_Recovery_Plan.docx":
        ("policies/l4-plans", "plan-703-disaster-recovery-plan.md",
         dict(id="PLAN-703", title="Disaster Recovery Plan", type="Plan", level="L4", status="Draft", owner="CISO", version="1.0")),
    # L5 Checklists
    "CL-PHASE-001_Audit_Phase_Checklists.docx":
        ("policies/l5-checklists", "cl-phase-001-audit-checklists.md",
         dict(id="CL-PHASE-001", title="Audit Phase Checklists", type="Checklist", level="L5", status="Approved", owner="CISO", version="1.0")),
    "CL-409_DPIA_Screening_Checklist.docx":
        ("policies/l5-checklists", "cl-409-dpia-screening.md",
         dict(id="CL-409", title="DPIA Screening Checklist", type="Checklist", level="L5", status="Generated", owner="CISO-DPO", version="1.0")),
    "CL-411_Signing_Ceremony_Checklist.docx":
        ("policies/l5-checklists", "cl-411-signing-ceremony.md",
         dict(id="CL-411", title="Signing Ceremony Checklist", type="Checklist", level="L5", status="Generated", owner="CISO", version="1.0")),
    # L6 Registers
    "REG-501_Enterprise_Risk_Register.docx":
        ("policies/l6-registers", "reg-501-risk-register.md",
         dict(id="REG-501", title="Enterprise Risk Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-502_Vendor_Third_Party_Register.docx":
        ("policies/l6-registers", "reg-502-vendor-register.md",
         dict(id="REG-502", title="Vendor and Third-Party Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-503_Asset_Register_CMDB.docx":
        ("policies/l6-registers", "reg-503-asset-register-cmdb.md",
         dict(id="REG-503", title="Asset Register / CMDB", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-504_Change_Release_Register.docx":
        ("policies/l6-registers", "reg-504-change-release-register.md",
         dict(id="REG-504", title="Change and Release Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-505_Record_of_Processing_Activities_ROPA.docx":
        ("policies/l6-registers", "reg-505-ropa.md",
         dict(id="REG-505", title="Record of Processing Activities (ROPA)", type="Register", level="L6", status="Generated", owner="CISO-DPO", version="1.0")),
    "REG-506_Exception_Waiver_Register.docx":
        ("policies/l6-registers", "reg-506-exception-register.md",
         dict(id="REG-506", title="Exception and Waiver Register", type="Register", level="L6", status="Generated", owner="CISO", version="1.0")),
    "REG-507_Training_Awareness_Register.docx":
        ("policies/l6-registers", "reg-507-training-register.md",
         dict(id="REG-507", title="Training and Awareness Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-508_Access_Review_Register.docx":
        ("policies/l6-registers", "reg-508-access-review-register.md",
         dict(id="REG-508", title="Access Review Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-509_Incident_Register.docx":
        ("policies/l6-registers", "reg-509-incident-register.md",
         dict(id="REG-509", title="Incident Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-510_DPIA_Register.docx":
        ("policies/l6-registers", "reg-510-dpia-register.md",
         dict(id="REG-510", title="DPIA Register", type="Register", level="L6", status="Generated", owner="CISO-DPO", version="1.0")),
    "REG-511_Document_Registry.docx":
        ("policies/l6-registers", "reg-511-document-registry.md",
         dict(id="REG-511", title="Document Registry", type="Register", level="L6", status="Generated", owner="GRC-Manager", version="1.0")),
    "REG-512_Evidence_Calendar.docx":
        ("policies/l6-registers", "reg-512-evidence-calendar.md",
         dict(id="REG-512", title="Evidence Calendar", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    "REG-513_Node_Configuration_Register.docx":
        ("policies/l6-registers", "reg-513-node-configuration-register.md",
         dict(id="REG-513", title="Node Configuration Register", type="Register", level="L6", status="Draft", owner="CISO", version="1.0")),
    # Mappings
    "MAP-001_Control_Mapping_Matrix.docx":
        ("mappings", "map-001-control-mapping-matrix.md",
         dict(id="MAP-001", title="Control Mapping Matrix", type="Mapping", level="L0", status="Draft", owner="CISO", version="1.0")),
    # Legal Templates (new subfolder)
    "DPA-001_Data_Processing_Agreement_Template.docx":
        ("policies/legal-templates", "dpa-001-data-processing-agreement.md",
         dict(id="DPA-001", title="Data Processing Agreement Template", type="Legal Template", level="L2", status="Draft", owner="CISO-DPO", version="1.0")),
    "MSA-001_Security_Clauses_Template.docx":
        ("policies/legal-templates", "msa-001-security-clauses.md",
         dict(id="MSA-001", title="Master Service Agreement Security Clauses Template", type="Legal Template", level="L2", status="Draft", owner="CISO", version="1.0")),
}

# IDs flagged as needing manual review of folder placement
AMBIGUOUS_IDS = {
    "L0-3", "SEC-POSTURE-001", "DAO-001", "RACI-001", "RACI-002",
    "MAP-001", "DPA-001", "MSA-001", "PLAN-701", "PLAN-702", "PLAN-703",
    "L0-6", "SOA-001", "IAP-001",
}


def extract_docx_text(docx_path):
    """Extract paragraphs from DOCX with style hints."""
    paragraphs = []
    try:
        with zipfile.ZipFile(str(docx_path), 'r') as z:
            xml = z.read('word/document.xml').decode('utf-8', errors='replace')
        # Extract paragraph elements
        para_matches = re.findall(r'<w:p[ >].*?</w:p>', xml, re.DOTALL)
        for para_xml in para_matches:
            # Style
            style_m = re.search(r'<w:pStyle w:val="([^"]+)"', para_xml)
            style = style_m.group(1) if style_m else "Normal"
            # Text
            runs = re.findall(r'<w:t[^>]*>([^<]*)</w:t>', para_xml)
            text = ''.join(runs).strip()
            if text:
                paragraphs.append((style, text))
    except Exception as e:
        paragraphs.append(("Normal", f"[Extraction error: {e}]"))
    return paragraphs


def style_to_md_prefix(style):
    """Map DOCX style name to Markdown heading prefix."""
    s = style.lower().replace(' ', '')
    mapping = {
        'heading1': '# ', 'heading2': '## ', 'heading3': '### ',
        'heading4': '#### ', 'heading5': '##### ', 'heading6': '###### ',
        'title': '# ', 'subtitle': '## ',
    }
    for k, v in mapping.items():
        if k in s:
            return v
    return ''


def build_frontmatter(meta):
    lines = ['---']
    lines.append(f'id: "{meta["id"]}"')
    lines.append(f'title: "{meta["title"]}"')
    lines.append(f'type: "{meta["type"]}"')
    lines.append(f'level: "{meta["level"]}"')
    lines.append(f'version: "{meta.get("version","1.0")}"')
    lines.append(f'status: "{meta["status"]}"')
    lines.append(f'effective_date: "Pending approval"')
    lines.append(f'review_cycle: "Annual"')
    lines.append(f'owner: "{meta["owner"]}"')
    lines.append(f'approver: "CISO advisory"')
    lines.append(f'classification: "Confidential — Internal"')
    lines.append(f'last_change: "2026-04-16"')
    lines.append(f'last_approval: "Pending"')
    lines.append(f'source: "reference_policies (DOCX conversion)"')
    lines.append('---')
    return '\n'.join(lines)


def docx_to_md(src_path, meta):
    """Convert DOCX file to Markdown string with frontmatter."""
    paragraphs = extract_docx_text(src_path)
    frontmatter = build_frontmatter(meta)
    doc_id = meta['id']
    title = meta['title']

    lines = [frontmatter, '', f'# {doc_id} — {title}', '']
    seen_title = False

    for style, text in paragraphs:
        prefix = style_to_md_prefix(style)
        if not seen_title and text.strip().startswith(doc_id):
            seen_title = True
            continue  # skip duplicate title from DOCX
        if prefix:
            lines.append(f'{prefix}{text}')
        else:
            lines.append(text)
        lines.append('')

    return '\n'.join(lines)


# ── Main processing ──

results = []  # list of dicts: {ref_file, folder, md_name, status, action, note}
added = skipped = updated = conflicts = errors = 0

for ref_file, (folder_rel, md_name, meta) in MAPPING.items():
    src_path = REF / ref_file
    target_dir = REPO / folder_rel
    target_path = target_dir / md_name
    doc_id = meta['id']
    is_ambiguous = doc_id in AMBIGUOUS_IDS

    entry = {
        'ref_file': ref_file,
        'folder': folder_rel,
        'md_name': md_name,
        'id': doc_id,
        'ambiguous': is_ambiguous,
        'src_exists': src_path.exists(),
        'tgt_exists': target_path.exists(),
        'status': None,
        'action': None,
        'note': '',
    }

    if not src_path.exists():
        entry['status'] = 'error'
        entry['action'] = 'skipped'
        entry['note'] = f'Source DOCX not found in reference_policies'
        errors += 1
        results.append(entry)
        continue

    if target_path.exists():
        # File already in repo — check if content differs meaningfully
        existing = target_path.read_text(encoding='utf-8')
        new_content = docx_to_md(src_path, meta)
        # Compare by word count difference (>20% = potential update)
        existing_words = len(existing.split())
        new_words = len(new_content.split())
        ratio = abs(existing_words - new_words) / max(existing_words, 1)
        if ratio > 0.20:
            entry['status'] = 'conflict'
            entry['action'] = 'skipped'
            entry['note'] = (f'Existing repo file has {existing_words} words; '
                             f'DOCX conversion yields {new_words} words '
                             f'({ratio*100:.0f}% difference). Manual review required.')
            conflicts += 1
        else:
            entry['status'] = 'skipped'
            entry['action'] = 'skipped'
            entry['note'] = (f'Already in repo. Word counts within tolerance '
                             f'(repo={existing_words}, docx={new_words}).')
            skipped += 1
        results.append(entry)
        continue

    # Target does not exist — convert and write
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        md_content = docx_to_md(src_path, meta)
        target_path.write_text(md_content, encoding='utf-8')
        entry['status'] = 'added'
        entry['action'] = 'converted DOCX→MD + written'
        entry['note'] = f'New file created. Folder created if needed: {folder_rel}'
        added += 1
    except Exception as e:
        entry['status'] = 'error'
        entry['action'] = 'failed'
        entry['note'] = f'Exception during conversion: {e}'
        errors += 1

    results.append(entry)


# ── Consistency checks ──
consistency_issues = []

# 1. Check for orphan repo files (in repo but not in mapping)
all_mapped_targets = set()
for _, (folder_rel, md_name, _) in MAPPING.items():
    all_mapped_targets.add(str(REPO / folder_rel / md_name))

for md_file in (REPO / 'policies').rglob('*.md'):
    if str(md_file) not in all_mapped_targets:
        consistency_issues.append(f'ORPHAN_IN_REPO: {md_file.relative_to(REPO)} — present in repo but has no matching entry in reference_policies mapping')

# 2. Check naming convention (must be kebab-case, no uppercase, no spaces)
for ref_file, (folder_rel, md_name, meta) in MAPPING.items():
    target_path = REPO / folder_rel / md_name
    if not target_path.exists():
        continue
    if re.search(r'[A-Z _]', md_name):
        consistency_issues.append(f'NAMING: {md_name} — contains uppercase or spaces (expected pure kebab-case)')

# 3. Check for duplicate IDs in mapping
id_map = {}
for ref_file, (folder_rel, md_name, meta) in MAPPING.items():
    doc_id = meta['id']
    if doc_id in id_map:
        consistency_issues.append(f'DUPLICATE_ID: {doc_id} mapped to both {id_map[doc_id]} and {md_name}')
    id_map[doc_id] = md_name

# 4. Report ambiguous placements
ambiguous_notes = []
for ref_file, (folder_rel, md_name, meta) in MAPPING.items():
    if meta['id'] in AMBIGUOUS_IDS:
        ambiguous_notes.append(
            f'{meta["id"]:20} -> {folder_rel}/{md_name}\n'
            f'  Reason: No pre-existing folder for this document type; '
            f'placement based on closest existing pattern. Manual review recommended.'
        )


# ── Write log ──
def sep(char='=', n=80):
    return char * n

log_lines = [
    sep(),
    'PROTOFIRE GRC REPOSITORY ACTUALIZATION LOG',
    f'Run time  : {RUN_TIME}',
    f'Repository: {REPO}',
    f'Reference : {REF}',
    sep(),
    '',
    sep('-'),
    'SECTION 1 — REFERENCE DOCUMENTS SCANNED',
    sep('-'),
]

all_ref_active = sorted([
    f for f in os.listdir(REF)
    if not f.startswith('Retire_') and not f.startswith('Bak_') and not f.startswith('DRAFT')
    and (f.endswith('.docx') or f.endswith('.md') or f.endswith('.xlsx'))
])
log_lines.append(f'Total active files in reference_policies: {len(all_ref_active)}')
log_lines.append(f'Files covered by mapping: {len(MAPPING)}')
unmapped = [f for f in all_ref_active if f not in MAPPING and f.endswith('.docx')]
log_lines.append(f'Active DOCX files not in mapping (see Section 6): {len(unmapped)}')
log_lines.append('')
for f in all_ref_active:
    log_lines.append(f'  {f}')

log_lines += [
    '',
    sep('-'),
    'SECTION 2 — ALREADY IN REPO (SKIPPED)',
    sep('-'),
]
skipped_items = [r for r in results if r['status'] == 'skipped']
log_lines.append(f'Count: {len(skipped_items)}')
log_lines.append('')
for r in skipped_items:
    log_lines.append(f'  [{r["id"]:20}] {r["ref_file"]}')
    log_lines.append(f'    -> {r["folder"]}/{r["md_name"]}')
    log_lines.append(f'    Note: {r["note"]}')
    log_lines.append('')

log_lines += [
    sep('-'),
    'SECTION 3 — ADDED TO REPO',
    sep('-'),
]
added_items = [r for r in results if r['status'] == 'added']
log_lines.append(f'Count: {len(added_items)}')
log_lines.append('')
for r in added_items:
    log_lines.append(f'  [{r["id"]:20}] {r["ref_file"]}')
    log_lines.append(f'    Source    : reference_policies/{r["ref_file"]}')
    log_lines.append(f'    Target    : {r["folder"]}/{r["md_name"]}')
    log_lines.append(f'    Action    : {r["action"]}')
    log_lines.append(f'    Ambiguous : {"YES — see Section 7" if r["ambiguous"] else "No"}')
    log_lines.append(f'    Note      : {r["note"]}')
    log_lines.append('')

log_lines += [
    sep('-'),
    'SECTION 4 — CONFLICTS (file exists but content differs significantly)',
    sep('-'),
]
conflict_items = [r for r in results if r['status'] == 'conflict']
log_lines.append(f'Count: {len(conflict_items)}')
log_lines.append('')
for r in conflict_items:
    log_lines.append(f'  [{r["id"]:20}] {r["ref_file"]}')
    log_lines.append(f'    -> {r["folder"]}/{r["md_name"]}')
    log_lines.append(f'    Note: {r["note"]}')
    log_lines.append(f'    Action required: Compare DOCX source with repo MD; merge manually.')
    log_lines.append('')

log_lines += [
    sep('-'),
    'SECTION 5 — ERRORS',
    sep('-'),
]
error_items = [r for r in results if r['status'] == 'error']
log_lines.append(f'Count: {len(error_items)}')
log_lines.append('')
for r in error_items:
    log_lines.append(f'  [{r["id"]:20}] {r["ref_file"]}')
    log_lines.append(f'    Note: {r["note"]}')
    log_lines.append('')

log_lines += [
    sep('-'),
    'SECTION 6 — UNMAPPED REFERENCE FILES (in reference_policies but not in mapping)',
    sep('-'),
]
log_lines.append(f'Count: {len(unmapped)}')
log_lines.append('')
for f in unmapped:
    log_lines.append(f'  {f}')
    log_lines.append(f'    Action: Manual classification needed.')
    log_lines.append('')

log_lines += [
    sep('-'),
    'SECTION 7 — AMBIGUITIES / MANUAL REVIEW REQUIRED',
    sep('-'),
]
log_lines.append(f'Count: {len(ambiguous_notes)}')
log_lines.append('')
for note in ambiguous_notes:
    log_lines.append(f'  {note}')

log_lines += [
    '',
    sep('-'),
    'SECTION 8 — CONSISTENCY ISSUES',
    sep('-'),
]
log_lines.append(f'Count: {len(consistency_issues)}')
log_lines.append('')
for issue in consistency_issues:
    log_lines.append(f'  {issue}')

log_lines += [
    '',
    sep(),
    'SUMMARY',
    sep(),
    f'  Reference files scanned  : {len(MAPPING)}',
    f'  Already in repo (skipped): {skipped}',
    f'  Added to repo            : {added}',
    f'  Conflicts (not written)  : {conflicts}',
    f'  Errors                   : {errors}',
    f'  Unmapped active files    : {len(unmapped)}',
    f'  Consistency issues found : {len(consistency_issues)}',
    f'  Ambiguous placements     : {len(ambiguous_notes)}',
    '',
    f'  New subfolders created   :',
]
new_folders = set()
for r in added_items:
    fp = REPO / r['folder']
    if fp.exists():
        new_folders.add(r['folder'])
for nf in sorted(new_folders):
    log_lines.append(f'    {nf}')

log_lines += [
    '',
    sep(),
    'END OF LOG',
    sep(),
]

LOG_PATH.write_text('\n'.join(log_lines), encoding='utf-8')
print(f"Log written to: {LOG_PATH}")
print(f"Added: {added}  Skipped: {skipped}  Conflicts: {conflicts}  Errors: {errors}")
print(f"Consistency issues: {len(consistency_issues)}")
