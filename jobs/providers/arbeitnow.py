import requests

def fetch_arbeitnow_jobs():
    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    jobs = []

    for job in data.get("data", []):
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "url": job.get("url"),
            "source": "Arbeitnow"
        })

    return jobs