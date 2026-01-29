from resume_parser import parse_resume
from jd_parser import parse_job_description
from matcher import match_resume_to_jd

resume_text = """
Data Analyst with 6+ years of experience.
Strong in Python, SQL, Excel, Power BI.
Experience with Machine Learning, Pandas, NumPy, Git.
"""

jd_text = """
We are looking for a Data Scientist with strong Python, SQL,
Machine Learning, Deep Learning, PyTorch, and AWS experience.
"""

resume_data = parse_resume(resume_text)
jd_data = parse_job_description(jd_text)

match = match_resume_to_jd(resume_data, jd_data)

print("Resume Data:", resume_data)
print("JD Data:", jd_data)
print("Match Result:", match)