
# === 📄 agent/validator_agent.py ===
from utils.rule_engine import rule_based_checks
from utils.llm_validator import llm_validate
import json

def validate_policy(text):
    rule_findings = rule_based_checks(text)
    llm_findings = []

    try:
        raw = llm_validate(text)
        llm_findings = json.loads(raw)
    except Exception as e:
        llm_findings = [{"issue": "LLM validation failed", "suggestion": str(e)}]

    return {
        "summary": {
            "missing_fields": len(rule_findings),
            "llm_issues": len(llm_findings)
        },
        "rule_based": rule_findings,
        "llm_based": llm_findings
    }
