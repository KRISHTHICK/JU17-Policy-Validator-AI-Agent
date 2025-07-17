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
