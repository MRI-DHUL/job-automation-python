import requests
from app.utils.formatters import format_epoch_date, clean_description


def fetch_arbeitnow_jobs():
    url = "https://www.arbeitnow.com/api/job-board-api"

    res = requests.get(url)
    res.raise_for_status()

    data = res.json().get("data", [])
    jobs = []

    for j in data:
        job = {}

        job["title"] = j.get("title")
        job["company"] = j.get("company_name")
        job["location"] = j.get("location")
        job["url"] = j.get("url")
        job["source"] = "arbeitnow"
        job["posted"] = format_epoch_date(j.get("created_at"))
        job["description"] = clean_description(j.get("description"))
        job["salary_min"] = None
        job["salary_max"] = None
        job["salary"] = None

        job["tags"] = j.get("tags") or []

        jobs.append(job)

    return jobs