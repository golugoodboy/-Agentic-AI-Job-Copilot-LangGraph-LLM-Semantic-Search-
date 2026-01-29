from langgraph.graph import StateGraph, START, END
from state import jobagentstate

from resume_agent import resume_agent
from jd_agent import jd_agent
from matcher_agent import matcher_agent
from explanation import explanation_agent
from job_search_agent import job_search_agent
from supervisor_agent import supervisor_agent
from llm_jd import extract_jd_with_llm

graph = StateGraph(jobagentstate)

graph.add_node("resume", resume_agent)
graph.add_node("jd", jd_agent)
graph.add_node("matcher", matcher_agent)
graph.add_node("explain", explanation_agent)
graph.add_node("job_search_agent", job_search_agent)
graph.add_node("supervisor_agent", supervisor_agent)


graph.add_edge(START, "resume")
graph.add_edge("resume","job_search_agent")
graph.add_edge("job_search_agent", "supervisor_agent")
graph.add_edge("supervisor_agent", END)

workflow = graph.compile()

initial_state: jobagentstate = {
    "resume_text": """
Data Analyst with 6+ years of experience.
Strong in Python, SQL, Excel, Power BI.
Experience with Machine Learning, Pandas, NumPy, Git.
""",
    "search_query": "AI Engineer",

    "jd_text": "",
    "resume_data": {},
    "jd_data": {},
    "match_result": {},
    "explanation": "",
    "jobs_found": [],
    "scored_jobs": []
}

final_state = workflow.invoke(initial_state)

print("\n=== SCORED JOBS (SUPERVISOR) ===")
for job in final_state["scored_jobs"]:
    print(f"{job['decision']} | {job['score']}% | {job['title']} | {job['company']}")



