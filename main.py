from jobs.providers.remoteok import fetch_remoteok_jobs
from jobs.providers.remotive import fetch_remotive_jobs
from jobs.aggregator import fetch_all_jobs
from utils.validator import is_valid_email
from utils.input_handler import get_input_with_attempts

import os
from datetime import datetime


def get_next_file_number(folder):
    files = os.listdir(folder)

    numbers = []
    for file in files:
        if file.startswith("Job") and "_" in file:
            try:
                num = int(file.split("_")[0].replace("Job", ""))
                numbers.append(num)
            except:
                pass

    return max(numbers, default=0) + 1


# Provider validation
def validate_provider(choice):
    return choice in ["remoteok", "remotive", "all"]


if __name__ == "__main__":
    print("=== JOB AUTOMATION TOOL ===\n")

    # Email validation (3 attempts)
    email = get_input_with_attempts(
        "Enter your email: ",
        validate_fn=is_valid_email,
        error_msg="Invalid email format"
    )

    print("Email validated\n")

    # Provider selection (3 attempts)
    choice = get_input_with_attempts(
        "Select provider (remoteok / remotive / all): ",
        validate_fn=validate_provider,
        error_msg="Invalid provider"
    ).lower()

    # Fetch jobs
    match choice:
        case "remoteok":
            jobs = fetch_remoteok_jobs()
        case "remotive":
            jobs = fetch_remotive_jobs()
        case "all":
            jobs = fetch_all_jobs()

    # Filters (no strict validation)
    keyword = input("Enter job keyword (or press Enter to skip): ").lower().strip()
    location_filter = input("Enter location (or press Enter to skip): ").lower().strip()
    company_filter = input("Enter company name (or press Enter to skip): ").lower().strip()
    source_filter = input("Enter source (remoteok/remotive or press Enter to skip): ").lower().strip()

    filtered_jobs = []

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

        filtered_jobs.append(job)

    jobs = filtered_jobs

    print(f"\nFiltered Jobs: {len(jobs)}\n")

    if not jobs:
        print("No jobs found with given filters. No file created.")
        exit()
        
    # Ensure output folder
    os.makedirs("output", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_number = get_next_file_number("output")

    file_name = f"Job{file_number}_{timestamp}.txt"
    file_path = os.path.join("output", file_name)

    # Save to file
    with open(file_path, "w", encoding="utf-8") as f:
        for i, job in enumerate(jobs, start=1):
            location = job['location'] or "Not specified"

            job_text = (
                f"Job {i}\n\n"
                f"Title     : {job['title']}\n"
                f"Company   : {job['company']}\n"
                f"Location  : {location}\n"
                f"Apply Link: {job['url']}\n"
                f"Source    : {job['source']}\n"
                f"{'-'*50}\n"
            )

            print(job_text)
            f.write(job_text)

    print(f"\nJobs saved to {file_path}")