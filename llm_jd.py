from state import jobagentstate
import json
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import re

env_path = r"C:\Users\Goludev\Desktop\langchain\job_agent\.env" 

load_dotenv(dotenv_path = env_path)

def call_llm(prompt : str):
    try:
        llm = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        task="text-generation",
        max_new_tokens=150,
        do_sample=True,
        temperature=0.0)
        model = ChatHuggingFace(llm = llm)

        response = model.invoke(prompt)

        if hasattr(response, "content"):
            text = response.content
        else:
            text = str(response)

        return text
    
    except Exception as e:
        print("[call_llm] LLM call failed:", e)
        return ""


def safe_json_from_llm(text: str) -> dict:
    try:
        return json.loads(text)
    except:
        # Try to extract JSON block from messy output
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group())
            except:
                pass

    return {
        "skills": [],
        "role": "",
        "seniority": ""
    }



def extract_jd_with_llm(jd_text: str) -> dict:
    jd_text = jd_text[:1500]
    prompt = f"""
You are an expert technical recruiter.

Read the following job description and extract:
1. Required technical skills
2. Role type (e.g., Data Scientist, AI Engineer, ML Engineer, Data Engineer, etc.)
3. Seniority level (Junior, Mid, Senior, Lead, etc.)

Return ONLY valid JSON in this format:

{{
  "skills": ["python", "aws", "machine learning"],
  "role": "AI Engineer",
  "seniority": "Senior"
}}

Job Description:
----------------
{jd_text}
"""

    raw_response = call_llm(prompt)
    data = safe_json_from_llm(raw_response)

    if not isinstance(data, dict):
        data = {
            "skills": [],
            "role": "",
            "seniority": ""
        }

    # Ensure keys exist
    data.setdefault("skills", [])
    data.setdefault("role", "")
    data.setdefault("seniority", "")
    
    data["skills"] = [s.lower() for s in data.get("skills", [])]

    print("[LLM JD Extractor] Parsed:", data)

    return data




