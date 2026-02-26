from jobs.providers.remoteok import fetch_remoteok_jobs
from jobs.providers.remotive import fetch_remotive_jobs

def fetch_all_jobs():
    jobs = []

    jobs.extend(fetch_remoteok_jobs())
    jobs.extend(fetch_remotive_jobs())

    return jobs