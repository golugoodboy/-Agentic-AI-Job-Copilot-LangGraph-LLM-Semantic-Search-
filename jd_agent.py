from state import jobagentstate
from jd_parser import parse_job_description

def jd_agent(state : jobagentstate) -> jobagentstate:
    jd_text = state["jd_text"]
    jd_data = parse_job_description(jd_text)

    state["jd_data"] = jd_data

    return state
