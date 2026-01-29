from typing import TypedDict , List, Optional

class jobagentstate(TypedDict):
    resume_text : str
    jd_text : str
    resume_data : dict
    jd_data : dict
    match_result : dict
    explanation: str
    search_query: str
    jobs_found: List[dict]
    scored_jobs: List[dict]

