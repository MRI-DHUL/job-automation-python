import requests
from app.utils.formatters import format_posted_date, clean_description


def fetch_remotive_jobs():
    url = "https://remotive.com/api/remote-jobs"

    res = requests.get(url)
    res.raise_for_status()

    data = res.json().get("jobs", [])
    jobs = []

    for j in data:
        job = {}

        job["position"] = j.get("title")
        job["company"] = j.get("company_name")
        job["location"] = j.get("candidate_required_location")
        job["url"] = j.get("url")
        job["source"] = "remotive"
        job["posted"] = format_posted_date(j.get("publication_date"))
        job["description"] = clean_description(j.get("description"))
        job["salary"] = j.get("salary")
        job["salary_min"] = None
        job["salary_max"] = None
        job["tags"] = j.get("tags") or []

        jobs.append(job)

    return jobs