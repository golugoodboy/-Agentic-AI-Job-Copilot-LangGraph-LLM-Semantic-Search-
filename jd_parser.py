common_skills = [
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


def parse_job_description(jd_text : str):
    lower_jd = jd_text.lower()
    required_skills = []

    for skill in common_skills:
        if skill in lower_jd:
            required_skills.append(skill)
    
    return { "required_skills" : list(set(required_skills))}


