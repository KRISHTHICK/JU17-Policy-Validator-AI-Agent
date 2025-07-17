
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

