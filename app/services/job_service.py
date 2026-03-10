from typing import Dict, Any


def apply_filters(jobs, filters):
    if not any([
        filters.get("keywords"),
        filters.get("locations"),
        filters.get("companies"),
        filters.get("sources"),
        filters.get("job_types"),
        filters.get("remote_only"),
        filters.get("salary_min"),
    ]):
        return jobs

    results = []

    for job in jobs:
        if not job:
            continue

        checks = [
            keyword_check(job, filters),
            location_check(job, filters),
            company_check(job, filters),
            remote_check(job, filters),
            salary_check(job, filters),
            job_type_check(job, filters),
            source_check(job, filters),
        ]

        if all(checks):
            results.append(job)

    return results


### Individual Filter Rules ###

def keyword_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    keywords = filters.get("keywords", [])
    if not keywords:
        return True
    position = (job.get("position") or "").lower()
    return any(k.lower() in position for k in keywords)


def location_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    locations = filters.get("locations", [])
    if not locations:
        return True
    loc = (job.get("location") or "").lower()
    return any(l.lower() in loc for l in locations)


def company_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    companies = filters.get("companies", [])
    if not companies:
        return True
    comp = (job.get("company") or "").lower()
    return comp in [c.lower() for c in companies]


def remote_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    if not filters.get("remote_only", False):
        return True
    loc = (job.get("location") or "").lower()
    return "remote" in loc


def salary_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    min_salary = filters.get("salary_min", 0)
    if not min_salary:
        return True
    salary = job.get("salary_min") or 0
    return salary >= min_salary


def job_type_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    types_ = filters.get("job_types", [])
    if not types_:
        return True
    jt = (job.get("job_type") or "").lower()
    return jt in [t.lower() for t in types_]


def source_check(job: Dict[str, Any], filters: Dict[str, Any]) -> bool:
    sources = filters.get("sources", [])
    if not sources:
        return True
    src = (job.get("source") or "").lower()
    return src in [s.lower() for s in sources]