import requests
from state import jobagentstate

def job_search_agent(state : jobagentstate) -> jobagentstate:
    query = state.get("search_query","Analyst")

    print(f"[JobSearchAgent] Searching jobs for: {query}")

    url = "https://remotive.com/api/remote-jobs"

    try:
        resp = requests.get(url, timeout = 10)
        data = resp.json()
    except Exception as e:
        print("Job API error:", e)
        state["jobs_found"] = []
        return state
    
    jobs = []
    all_jobs = data.get("jobs", [])

    print(f"[JobSearchAgent] Total jobs received: {len(all_jobs)}")

    for job in all_jobs[:10]:
         jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("candidate_required_location"),
            "url": job.get("url"),
            "description": job.get("description", "")[:500]  # preview
        })

    state["jobs_found"] = jobs
    return state
