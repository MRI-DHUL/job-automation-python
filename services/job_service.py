from jobs.providers.remoteok import fetch_remoteok_jobs
from jobs.providers.remotive import fetch_remotive_jobs
from jobs.providers.arbeitnow import fetch_arbeitnow_jobs
from jobs.aggregator import fetch_all_jobs

from utils.deduplicator import remove_duplicate_jobs

VALID_PROVIDERS = {
    "remoteok",
    "remotive",
    "arbeitnow",
    "all"
}

def validate_provider(provider):
    """Ensure provider is valid."""
    if provider not in VALID_PROVIDERS:
        raise ValueError(f"Invalid provider: {provider}")
    return True

def fetch_jobs(provider):

    validate_provider(provider)

    match provider:

        case "remoteok":
            jobs = fetch_remoteok_jobs()

        case "remotive":
            jobs = fetch_remotive_jobs()

        case "arbeitnow":
            jobs = fetch_arbeitnow_jobs()

        case "all":
            jobs = fetch_all_jobs()

        case _:
            jobs = []

    return remove_duplicate_jobs(jobs)

def apply_filters(jobs, filters):

    keywords = filters.get("keywords", [])
    locations = filters.get("locations", [])
    companies = filters.get("companies", [])
    sources = filters.get("sources", [])
    job_types = filters.get("job_types", [])
    remote_only = filters.get("remote_only", False)
    salary_min = filters.get("salary_min", 0)

    filtered = []

    for job in jobs:

        title = job.get("title", "").lower()
        location = (job.get("location") or "").lower()
        company = job.get("company", "").lower()
        source = job.get("source", "").lower()
        job_type = (job.get("job_type") or "").lower()
        salary = job.get("salary", 0)

        if keywords and not any(k in title for k in keywords):
            continue

        if locations and not any(l in location for l in locations):
            continue

        if companies and not any(c in company for c in companies):
            continue

        if sources and source not in sources:
            continue

        if job_types and job_type not in job_types:
            continue

        if remote_only and "remote" not in location:
            continue

        if salary_min and salary and salary < salary_min:
            continue

        filtered.append(job)

    return filtered

def search_jobs(filters):
    """Main entry point for UI."""

    provider = filters.get("provider", "all")

    jobs = fetch_jobs(provider)

    filtered_jobs = apply_filters(jobs, filters)

    return filtered_jobs

def get_provider_choice(input_handler):
    print("Select provider:")
    print("1. RemoteOK")
    print("2. Remotive")
    print("3. Arbeitnow")
    print("4. All")

    choice_input = input_handler(
        "Enter your choice (1-4): ",
        validate_fn=validate_provider,
        error_msg="Invalid choice"
    )

    return PROVIDER_MAP[choice_input]
