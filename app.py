# === 📁 Folder Structure ===
# policy-validator-ai-agent/
# ├── app.py                       # Main Streamlit app
# ├── agent/
# │   └── validator_agent.py     # Core logic for validation
# ├── utils/
# │   ├── extractor.py           # PDF/DOCX/Text parser
# │   ├── rule_engine.py         # Rule-based checks
# │   └── llm_validator.py       # LLM-based smart validation
# └── samples/
#     └── sample_policy.pdf        # Sample input for testing

# === 📄 app.py ===
import streamlit as st
from utils.extractor import extract_text
from agent.validator_agent import validate_policy

st.set_page_config(page_title="Policy Validator AI Agent", layout="wide")
st.title("🌐 Policy Validator AI Agent")

uploaded_file = st.file_uploader("Upload a policy document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded_file:
    text = extract_text(uploaded_file)
    st.subheader("📄 Extracted Text Preview")
    st.text_area("Text", text[:2000], height=300)

    if st.button("✅ Run Validation"):
        with st.spinner("Validating with AI Agent..."):
            result = validate_policy(text)
            st.success("Validation Completed!")

            st.subheader("🔒 Validation Report")
            st.json(result)

            if st.button("💾 Download JSON Report"):
                import json
                import datetime
                st.download_button("Download", json.dumps(result, indent=2), file_name=f"report_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.json")


# === 📄 utils/extractor.py ===
import fitz  # PyMuPDF
import docx2txt

def extract_text(file):
    if file.name.endswith(".pdf"):
        doc = fitz.open(stream=file.read(), filetype="pdf")
        return "\n".join([page.get_text() for page in doc])
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return "Unsupported format"


# === 📄 utils/rule_engine.py ===
REQUIRED_SECTIONS = ["Customer Name", "Policy Number", "Date of Issue", "Signature", "Coverage Details"]

def rule_based_checks(text):
    findings = []
    for field in REQUIRED_SECTIONS:
        if field.lower() not in text.lower():
            findings.append({"type": "missing", "field": field})
    return findings


# === 📄 utils/llm_validator.py ===
from llama_cpp import Llama

llm = Llama(model_path="llama-3.gguf", n_ctx=2048)  # Adjust your model path here

def llm_validate(text):
    prompt = f"""
Act as a BFSI Policy Validator.
Analyze the following document text and list 3 vague or ambiguous phrases or missing legal constructs. Return JSON:
[{{ "issue": "...", "suggestion": "..." }}]

Text:
{text[:3000]}
"""
    response = llm(prompt=prompt, stop=["\n"], max_tokens=512)
    return response["choices"][0]["text"].strip()


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
