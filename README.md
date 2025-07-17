# JU17-Policy-Validator-AI-Agent
GEN AI

💡 Topic: Policy Validator AI Agent for BFSI Documents
🎯 Goal:
Build a smart Validator Agent that analyzes policy documents (insurance, loan, credit policies, etc.) and automatically checks if they meet regulatory requirements, highlight missing fields, and validate the format using LLMs and custom rule-based checks.

🔍 Features:
Upload policy documents (PDF, DOCX, TXT)

Extract and parse key sections (e.g., customer details, policy clauses, T&Cs)

Validator Agent:

Checks for required fields

Flags missing or invalid info

Highlights inconsistent language using LLM (e.g., "Ambiguity in clause 4.2")

Show Validation Report in tabular and summary view

Download Annotated Report as JSON or PDF

Optionally: Use RAG + Rule Engine + Ollama for offline validation

🛠️ Stack:
Python, Streamlit (Frontend)

Ollama (LLM backend – llama3)

PyMuPDF, docx2txt (file parsing)

ValidatorAgent (custom + LLM logic)

✅ Sample Use Case:
Upload a Life Insurance Policy PDF → Validator Agent reviews document → Detects: Missing signature, vague clause wording, incorrect date format → Generates a JSON validation report.

🚀 Project Overview: Policy Validator AI
Objective: Automatically validate uploaded policy documents (PDF, DOCX) using both:

Rule-based validations (e.g., “must contain a cancellation clause”),

AI agent that analyzes and comments on the validity and completeness.

🧠 Key Features:
Upload Policy Documents

Extract content (text + tables)

Run rule-based validation checks

Validator Agent (LLM) provides reasoning on policy sufficiency

Generate Validation Report (editable & downloadable)

Dashboard for viewing results

🗂️ Project Structure:
pgsql
Copy
Edit
policy-validator-ai/
├── app.py                         # Streamlit main app
├── agent/
│   └── validator_agent.py         # LLM agent logic
├── rules/
│   └── rule_checker.py            # Rule-based validation logic
├── utils/
│   ├── file_loader.py             # Extract text/tables from PDF/DOCX
│   └── report_generator.py        # Generate validation report
├── examples/
│   └── sample_policy.pdf
├── requirements.txt
└── README.md
✅ Validation Rules (Examples):
Must include: Cancellation Clause

Must mention: Effective Date, Coverage Amount

Must contain: Signatures, Terms & Conditions
