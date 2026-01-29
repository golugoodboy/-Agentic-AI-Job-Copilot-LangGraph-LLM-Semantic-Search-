from state import jobagentstate
from utils import clean_html
from llm_jd import extract_jd_with_llm
from matcher import match_resume_to_jd_v2
from embeddings import get_embedding, cosine_similarity

# Target roles you want to prioritize
TARGET_ROLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "data scientist"
]

# Hybrid scoring weights
FINAL_RULE_WEIGHT = 0.7
FINAL_SEMANTIC_WEIGHT = 0.3


def supervisor_agent(state: jobagentstate) -> jobagentstate:
    print("USING LLM + SEMANTIC POWERED SUPERVISOR AGENT")

    resume_data = state.get("resume_data", {})
    jobs = state.get("jobs_found", [])
    resume_text = state.get("resume_text", "")

    scored_jobs = []

    print("[SupervisorAgent] Scoring jobs...")

    # Build resume embedding ONCE
    try:
        resume_embedding = get_embedding(resume_text)
    except Exception as e:
        print("[SupervisorAgent] Resume embedding failed:", e)
        resume_embedding = None

    for job in jobs:
        title = job.get("title", "")
        raw_desc = job.get("description", "")

        # Combine title + description for better context
        combined_text = f"{title} {raw_desc}"
        clean_text = clean_html(combined_text)

        # Limit text for LLM + embeddings
        clean_text = clean_text[:2000]

        # =========================
        # 1. LLM-based JD extraction
        # =========================
        llm_jd = extract_jd_with_llm(clean_text)

        print(f"[SupervisorAgent][LLM] {title} →", llm_jd)

        jd_data = {
            "required_skills": llm_jd.get("skills", [])
        }

        # =========================
        # 2. Rule-based v2 matching
        # =========================
        match = match_resume_to_jd_v2(resume_data, jd_data)
        rule_score = match.get("match_score", 0)

        # =========================
        # 3. Role-based bonus
        # =========================
        role = llm_jd.get("role", "").lower()
        if any(target in role for target in TARGET_ROLES):
            print(f"[SupervisorAgent] Role match bonus for role: {role}")
            rule_score = min(rule_score + 10, 100)

        # =========================
        # 4. Semantic similarity
        # =========================
        semantic_score = 0
        if resume_embedding is not None:
            try:
                jd_embedding = get_embedding(clean_text)
                semantic_sim = cosine_similarity(resume_embedding, jd_embedding)
                semantic_score = int(max(0, min(semantic_sim, 1)) * 100)
            except Exception as e:
                print(f"[SupervisorAgent] Semantic embedding failed for {title}:", e)

        # =========================
        # 5. Hybrid final score
        # =========================
        final_score = int(
            FINAL_RULE_WEIGHT * rule_score +
            FINAL_SEMANTIC_WEIGHT * semantic_score
        )

        print(
            f"[SupervisorAgent][SEMANTIC] {title} → "
            f"rule={rule_score}, semantic={semantic_score}, final={final_score}"
        )

        # =========================
        # 6. Decision logic
        # =========================
        if final_score >= 50:
            decision = "APPLY"
        elif final_score >= 30:
            decision = "MAYBE"
        else:
            decision = "SKIP"

        scored_jobs.append({
            "title": title,
            "company": job.get("company"),
            "location": job.get("location"),
            "url": job.get("url"),
            "score": final_score,
            "decision": decision,
            "matched_skills": match.get("matched_skill", []),
            "missing_skills": match.get("missing_skill", []),
            "llm_role": llm_jd.get("role", ""),
            "llm_seniority": llm_jd.get("seniority", ""),
        })

    # =========================
    # 7. Sort by final score
    # =========================
    scored_jobs.sort(key=lambda x: x["score"], reverse=True)

    state["scored_jobs"] = scored_jobs
    return state
