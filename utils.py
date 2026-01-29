import re

SKILL_SYNONYMS = {
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "dl": "deep learning",
    "sklearn": "scikit-learn",
}

def normalize_skill(skill: str) -> str:
    skill = skill.lower().strip()
    return SKILL_SYNONYMS.get(skill, skill)


def clean_html(raw_html: str) -> str:
    clean_text = re.sub(r"<.*?>", " ", raw_html)
    clean_text = re.sub(r"\s+", " ", clean_text)
    return clean_text.lower()