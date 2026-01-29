from state import jobagentstate
from resume_parser import parse_resume

def resume_agent(state : jobagentstate) -> jobagentstate:
    resume_text = state["resume_text"]
    resume_data = parse_resume(resume_text)

    state["resume_data"] = resume_data
    
    return state

