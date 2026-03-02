def remove_duplicate_jobs(jobs):
    seen = set()
    unique_jobs = []

    for job in jobs:
        key = (job["title"], job["company"])

        if key in seen:
            continue

        seen.add(key)
        unique_jobs.append(job)

    return unique_jobs