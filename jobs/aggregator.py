from jobs.providers.remoteok import fetch_remoteok_jobs
from jobs.providers.remotive import fetch_remotive_jobs
from jobs.providers.arbeitnow import fetch_arbeitnow_jobs

def fetch_all_jobs():
    jobs = []

    jobs.extend(fetch_remoteok_jobs())
    jobs.extend(fetch_remotive_jobs())
    jobs.extend(fetch_arbeitnow_jobs())
    
    return jobs