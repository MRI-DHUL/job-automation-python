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
    keyword_input = input("Enter job keywords (or press Enter to skip): ").lower().strip()
    location_input = input("Enter locations (or press Enter to skip): ").lower().strip()
    company_input = input("Enter company names (or press Enter to skip): ").lower().strip()
    source_input = input("Enter sources (remoteok/remotive/arbeitnow or press Enter to skip): ").lower().strip()

    # Convert all inputs into lists
    def split_values(value):
        return [v.strip() for v in value.split(",") if v.strip()] if value else []

    keywords = split_values(keyword_input)
    locations = split_values(location_input)
    companies = split_values(company_input)
    sources = split_values(source_input)

    filtered = []

    for job in jobs:
        title = job["title"].lower()
        location = (job["location"] or "").lower()
        company = job["company"].lower()
        source = job["source"].lower()

        if keywords and not any(k in title for k in keywords):
            continue
        if locations and not any(l in location for l in locations):
            continue
        if companies and not any(c in company for c in companies):
            continue
        if sources and not any(s == source for s in sources):
            continue

        filtered.append(job)

    return filtered