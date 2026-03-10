import requests
from app.utils.formatters import (
    format_posted_date,
    format_epoch_date,
    clean_description,
)


def fetch_remoteok_jobs():
    url = "https://remoteok.com/api"
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()

    data = res.json()[1:]
    jobs = []

    for j in data:
        job = {}

        job["position"] = j.get("position")
        job["company"] = j.get("company")
        job["location"] = j.get("location") or "Remote"
        job["url"] = j.get("apply_url") or j.get("url")
        job["source"] = "remoteok"
        job["posted"] = (
            format_posted_date(j.get("date"))
            if j.get("date")
            else format_epoch_date(j.get("epoch"))
        )
        job["description"] = clean_description(j.get("description"))
        job["salary_min"] = j.get("salary_min")
        job["salary_max"] = j.get("salary_max")
        job["tags"] = j.get("tags") or []

        jobs.append(job)

    return jobs