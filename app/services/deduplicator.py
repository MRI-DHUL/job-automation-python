def remove_duplicate_jobs(jobs):
    seen = set()
    unique = []
    for j in jobs:
        key = (j.get("position"), j.get("company"), j.get("location"))
        if key not in seen:
            seen.add(key)
            unique.append(j)
    return unique