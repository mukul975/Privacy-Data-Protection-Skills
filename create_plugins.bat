@echo off
setlocal enabledelayedexpansion

set "BASE=D:\Privacy&Data Protection-Skills"

REM ============================================================
REM Plugin 1: privacy-skills-complete (ALL 282 skills)
REM ============================================================
set "PLUGIN=privacy-skills-complete"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul

for /d %%S in ("%BASE%\skills\privacy\*") do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%~nxS" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%~nxS" "%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 2: gdpr-compliance-skills
REM ============================================================
set "PLUGIN=gdpr-compliance-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (gdpr-accountability gdpr-certification gdpr-codes-of-conduct gdpr-compliance-audit gdpr-doc-review gdpr-dpa-art28 gdpr-dpa-cooperation gdpr-eu-representative gdpr-gap-analysis gdpr-one-stop-shop gdpr-policy-framework gdpr-prior-consultation gdpr-remediation-roadmap gdpr-ropa-audit gdpr-self-assessment joint-controller-art26 lawful-basis-assessment legitimate-interest-lia) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 3: privacy-impact-assessment-skills
REM ============================================================
set "PLUGIN=privacy-impact-assessment-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (ai-privacy-assessment biometric-dpia cloud-migration-dpia comparing-pia-methodologies conducting-gdpr-dpia dpia-automated-decisions dpia-mitigation-plan dpia-risk-scoring dpia-stakeholder-consult employee-surveillance-dpia health-data-dpia marketing-analytics-dpia new-tech-pia nist-privacy-identify pia-review-cadence pia-threshold-screening prior-consultation-dpa privacy-threshold-analysis) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 4: data-subject-rights-skills
REM ============================================================
set "PLUGIN=data-subject-rights-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (automated-decision-rights ccpa-consumer-requests cpra-opt-out-signals data-portability direct-collection-notice dsar-intake-system dsar-processing indirect-collection-notice marketing-objection regulatory-complaints restriction-of-processing right-to-erasure right-to-object right-to-rectification transparent-communication) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 5: ai-privacy-governance-skills
REM ============================================================
set "PLUGIN=ai-privacy-governance-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (ai-act-high-risk-docs ai-automated-decisions ai-bias-special-category ai-data-retention ai-data-subject-rights ai-deployment-checklist ai-dpia ai-federated-learning ai-model-privacy-audit ai-privacy-impact-template ai-privacy-inference ai-training-lawfulness ai-transparency-reqs ai-vendor-privacy-due llm-output-privacy-risk) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 6: consent-management-skills
REM ============================================================
set "PLUGIN=consent-management-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (cnil-compliant-cookies consent-for-transfers consent-platform-eval consent-pref-center consent-record-keeping consent-withdrawal cookie-consent-ab-audit double-opt-in-email gdpr-valid-consent global-privacy-control legit-interest-vs-consent managing-consent-for-children managing-consent-for-research managing-mobile-app-consent) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 7: privacy-engineering-skills
REM ============================================================
set "PLUGIN=privacy-engineering-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (consent-receipt-spec differential-privacy-prod linddun-threat-model nist-pf-communicate nist-pf-control nist-pf-govern nist-pf-identify nist-pf-protect pii-detection-pipeline privacy-api-design privacy-data-sharing privacy-metrics-dashboard privacy-record-linkage purpose-based-access) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 8: privacy-by-design-skills
REM ============================================================
set "PLUGIN=privacy-by-design-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (applying-privacy-design-patterns automating-storage-limitation-controls building-purpose-limitation-enforcement conducting-linddun-threat-modeling designing-federated-learning-architecture designing-privacy-preserving-analytics implementing-data-minimization-architecture implementing-data-protection-by-default implementing-homomorphic-encryption implementing-secure-multi-party-computation preparing-iso-31700-certification pseudonymization-risk selecting-privacy-enhancing-technologies) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 9: data-breach-response-skills
REM ============================================================
set "PLUGIN=data-breach-response-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (breach-72h-notification breach-credit-monitor breach-detection-system breach-documentation breach-forensics breach-multi-jurisdiction breach-remediation breach-response-playbook breach-risk-assessment breach-simulation breach-subject-comms ca-breach-notification hipaa-breach-notification) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 10: us-state-privacy-skills
REM ============================================================
set "PLUGIN=us-state-privacy-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (california-consumer-rights ccpa-cpra-compliance colorado-cpa-compliance connecticut-ctdpa cpra-sensitive-pi kentucky-kppa montana-mtdpa multi-state-compliance oregon-ocpa-compliance state-law-applicability texas-tdpsa-compliance universal-opt-out vcdpa-compliance) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 11: cross-border-transfers-skills
REM ============================================================
set "PLUGIN=cross-border-transfers-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (adequacy-assessment apac-transfers art49-derogations bcr-establishment data-flow-mapping data-localization eu-us-dpf-assessment scc-implementation supplementary-measures transfer-impact-assessment transfer-records uk-transfer-mechanisms) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 12: cookie-consent-skills
REM ============================================================
set "PLUGIN=cookie-consent-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (analytics-cookie-consent cnil-cookie-banner cookie-audit cookie-consent-testing cookieless-alternatives cookie-lifetime-audit cross-jurisdiction-cookies eprivacy-essential-cookies google-consent-mode-v2 gpc-cookie-integration server-side-tracking tcf-v2-implementation) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 13: data-classification-skills
REM ============================================================
set "PLUGIN=data-classification-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (ai-training-data-class auto-data-discovery classification-policy criminal-data-handling cross-jurisdiction-class data-inventory-mapping data-labeling-system data-lineage-tracking personal-data-test pii-in-unstructured pseudo-vs-anon-data special-category-data) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 14: data-retention-skills
REM ============================================================
set "PLUGIN=data-retention-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (anonymization-alternative auto-deletion-workflow backup-retention-erasure ccpa-right-to-delete cloud-retention-config financial-retention litigation-hold-mgmt retention-exception-mgmt retention-impact-assess retention-schedule search-engine-erasure secure-data-destruction) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 15: global-privacy-regulations-skills
REM ============================================================
set "PLUGIN=global-privacy-regulations-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (australia-privacy-act brazil-lgpd china-pipl conflicting-laws-mgmt india-dpdp-act japan-appi korea-pipa multi-jurisdiction-matrix privacy-law-gap-analysis privacy-law-monitoring singapore-pdpa thailand-pdpa) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 16: vendor-privacy-management-skills
REM ============================================================
set "PLUGIN=vendor-privacy-management-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (cloud-provider-assessment dpa-drafting saas-vendor-inventory sub-processor-management vendor-breach-cascade vendor-cert-acceptance vendor-monitoring-program vendor-privacy-audit vendor-privacy-due-diligence vendor-risk-scoring vendor-termination-data) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 17: healthcare-privacy-skills
REM ============================================================
set "PLUGIN=healthcare-privacy-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (42-cfr-part-2 healthcare-ai-privacy hipaa-baa-management hipaa-breach-notify hipaa-deidentification hipaa-minimum-necessary hipaa-privacy-rule hipaa-risk-analysis hipaa-security-rule hitech-act-privacy telehealth-privacy) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 18: employee-privacy-skills
REM ============================================================
set "PLUGIN=employee-privacy-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (background-check-privacy byod-privacy-policy employee-biometric-data employee-dsar-response employee-health-data employee-monitoring-dpia employment-consent-limits hr-system-privacy-config remote-work-monitoring whistleblower-data workplace-email-privacy) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 19: privacy-audit-skills
REM ============================================================
set "PLUGIN=privacy-audit-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (apec-cbpr-cert audit-remediation-program continuous-compliance dpa-inspection-prep eu-code-of-conduct gdpr-certification-scheme internal-privacy-audit iso-27701-pims privacy-maturity-model privacy-program-metrics soc2-privacy-audit) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 20: records-of-processing-skills
REM ============================================================
set "PLUGIN=records-of-processing-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (automated-ropa-generation controller-ropa-creation group-structure-ropa processor-ropa-creation ropa-250-exemption ropa-completeness-audit ropa-dpia-linkage ropa-executive-dashboard ropa-maintenance-workflow ropa-tool-integration) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

REM ============================================================
REM Plugin 21: children-privacy-skills
REM ============================================================
set "PLUGIN=children-privacy-skills"
mkdir "%BASE%\plugins\%PLUGIN%\.claude-plugin" 2>nul
mkdir "%BASE%\plugins\%PLUGIN%\skills" 2>nul
for %%S in (age-gating-services age-verification-methods children-data-minimization children-deletion-requests children-privacy-notice children-profiling-limits coppa-compliance edtech-privacy-assessment gdpr-parental-consent uk-aadc-implementation) do (
    if not exist "%BASE%\plugins\%PLUGIN%\skills\%%S" (
        mklink /J "%BASE%\plugins\%PLUGIN%\skills\%%S" "%BASE%\skills\privacy\%%S"
    )
)
echo Done: %PLUGIN%

echo.
echo All 21 plugins created successfully!
