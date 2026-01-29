from state import jobagentstate
from matcher import match_resume_to_jd

def matcher_agent(state : jobagentstate) -> jobagentstate:
    resume_data = state["resume_data"]
    jd_data = state["jd_data"]

    matcher = match_resume_to_jd(resume_data,jd_data)
    state["match_result"] = matcher
    
    return state
