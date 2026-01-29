import re

common_skills= [
    # Core
    "python", "sql", "excel", "power bi",

    # AI / ML
    "machine learning", "ml",
    "deep learning", "dl",
    "ai", "artificial intelligence",
    "nlp", "computer vision",

    # Frameworks
    "pytorch", "tensorflow", "keras",
    "scikit-learn", "sklearn",

    # Data
    "pandas", "numpy",
    "data analysis", "data analytics",
    "data scientist", "data science",
    "data engineer", "data engineering",

    # Big Data / Cloud
    "spark", "databricks",
    "aws", "azure", "gcp",
    "s3", "ec2", "lambda",

    # Dev / MLOps
    "docker", "kubernetes",
    "mlops", "airflow",
    "git", "ci/cd",

    # LLM / Agents (for YOU)
    "langchain", "langgraph",
    "llm", "transformers"
]


def extract_skill(resume_text : str):
    found_skills = []
    lower_resume = resume_text.lower()

    for skill in common_skills:
        if skill in lower_resume:
            found_skills.append(skill)
    
    return list(set(found_skills))


def extract_experience(resume_text : str):
    match = re.search(r"(\d+)\+?\s+years", resume_text.lower())

    if match:
        return int(match.group(1))
    return None 

def parse_resume(resume_text : str):
    skills = extract_skill(resume_text)
    experience = extract_experience(resume_text)

    return {
        "skills" : skills,
        "experience" : experience
    }
    

