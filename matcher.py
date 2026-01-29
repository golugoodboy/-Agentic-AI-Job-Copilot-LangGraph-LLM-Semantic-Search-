from utils import normalize_skill

CRITICAL_SKILLS = {
    "python": 3,
    "machine learning": 3,
    "deep learning": 2,
    "pytorch": 2,
    "tensorflow": 2,
    "sql": 1,
    "aws": 1,
    "azure": 1,
    "gcp": 1,
}

def match_resume_to_jd_v2(resume_data, jd_data):
    resume_skills_raw = resume_data.get("skills", [])
    jd_skills_raw = jd_data.get("required_skills", [])

    resume_skills = set(normalize_skill(s) for s in resume_skills_raw)
    jd_skills = set(normalize_skill(s) for s in jd_skills_raw)

    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills - resume_skills

    # Base score (coverage)
    if not jd_skills:
        base_score = 0
    else:
        base_score = len(matched) / len(jd_skills)

    # Weighted critical skills bonus
    critical_bonus = 0
    for skill in matched:
        critical_bonus += CRITICAL_SKILLS.get(skill, 0)

    # Normalize bonus (cap it)
    critical_bonus = min(critical_bonus * 0.05, 0.25)  # max +25%

    final_score = base_score + critical_bonus

    final_score_pct = int(min(final_score * 100, 100))

    return {
        "match_score": final_score_pct,
        "matched_skill": list(matched),
        "missing_skill": list(missing)
    }

def match_resume_to_jd(resume_text,jd_text):
    resume_skills = set(resume_text.get("skills", []))
    jd_skill = set(jd_text.get("required_skills", []))

    matched = resume_skills.intersection(jd_skill)
    missing = jd_skill - resume_skills

    if len(jd_skill) == 0:
        score = 0
    else:
        score = int((len(matched) / len(jd_skill)) * 100)

    return {
        "match_score" : score,
        "matched_skill" : list(matched),
        "missing_skill" : list(missing)
    }

