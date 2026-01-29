from state import jobagentstate
from resume_agent import resume_agent
from jd_agent import jd_agent
from matcher_agent import matcher_agent
from explanation import explanation_agent

initial_state: jobagentstate = {
    "resume_text": """
Data Analyst with 6+ years of experience.
Strong in Python, SQL, Excel, Power BI.
Experience with Machine Learning, Pandas, NumPy, Git.
""",
    "jd_text": """
We are looking for a Data Scientist with strong Python, SQL,
Machine Learning, Deep Learning, PyTorch, and AWS experience.
""",
    "resume_data": {},
    "jd_data": {},
    "match_result": {},
    "explanation": ""
}

state = resume_agent(initial_state)
state = jd_agent(state)
state = matcher_agent(state)
state = explanation_agent(state)

print("FINAL AGENT STATE:")
print(state)

print("\n=== EXPLANATION ===")
print(state["explanation"])