import requests

def fetch_remoteok_jobs():
    url = "https://remoteok.com/remote-dev-jobs.json"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    try:
        data = response.json()
    except:
        return []

    jobs = []

    for job in data[1:11]:
        jobs.append({
            "title": job.get("position"),
            "company": job.get("company"),
            "location": job.get("location"),
            "url": job.get("url"),
            "source": "RemoteOK"
        })

    return jobs