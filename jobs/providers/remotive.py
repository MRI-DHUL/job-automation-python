import requests

def fetch_remotive_jobs():
    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for job in data["jobs"][:10]:
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("candidate_required_location"),
            "url": job.get("url"),
            "source": "Remotive"
        })

    return jobs