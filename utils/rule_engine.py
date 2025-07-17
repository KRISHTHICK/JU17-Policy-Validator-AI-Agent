
# === 📄 utils/rule_engine.py ===
REQUIRED_SECTIONS = ["Customer Name", "Policy Number", "Date of Issue", "Signature", "Coverage Details"]

def rule_based_checks(text):
    findings = []
    for field in REQUIRED_SECTIONS:
        if field.lower() not in text.lower():
            findings.append({"type": "missing", "field": field})
    return findings

