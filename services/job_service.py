from jobs.providers.remoteok import fetch_remoteok_jobs
from jobs.providers.remotive import fetch_remotive_jobs
from jobs.providers.arbeitnow import fetch_arbeitnow_jobs
from jobs.aggregator import fetch_all_jobs

from utils.deduplicator import remove_duplicate_jobs


PROVIDER_MAP = {
    "1": "remoteok",
    "2": "remotive",
    "3": "arbeitnow",
    "4": "all"
}


def validate_provider(choice):
    return choice in PROVIDER_MAP


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


def fetch_jobs(choice):
    match choice:
        case "remoteok":
            jobs = fetch_remoteok_jobs()
        case "remotive":
            jobs = fetch_remotive_jobs()
        case "arbeitnow":
            jobs = fetch_arbeitnow_jobs()
        case "all":
            jobs = fetch_all_jobs()

    return remove_duplicate_jobs(jobs)


def apply_filters(jobs):
    keyword = input("Enter job keyword (or press Enter to skip): ").lower().strip()
    location_filter = input("Enter location (or press Enter to skip): ").lower().strip()
    company_filter = input("Enter company name (or press Enter to skip): ").lower().strip()
    source_filter = input("Enter source (remoteok/remotive/arbeitnow or press Enter to skip): ").lower().strip()

    filtered = []

    for job in jobs:
        title = job["title"].lower()
        location = (job["location"] or "").lower()
        company = job["company"].lower()
        source = job["source"].lower()

        if keyword and keyword not in title:
            continue
        if location_filter and location_filter not in location:
            continue
        if company_filter and company_filter not in company:
            continue
        if source_filter and source_filter != source:
            continue

        filtered.append(job)

    return filtered