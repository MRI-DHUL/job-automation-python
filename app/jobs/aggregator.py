from app.jobs.providers.remoteok import fetch_remoteok_jobs
from app.jobs.providers.remotive import fetch_remotive_jobs
from app.jobs.providers.arbeitnow import fetch_arbeitnow_jobs


def fetch_by_provider(name: str):
    match name.lower():
        case "remoteok":
            return fetch_remoteok_jobs()

        case "remotive":
            return fetch_remotive_jobs()

        case "arbeitnow":
            return fetch_arbeitnow_jobs()

        case _:
            print(f"Unknown provider: {name}")
            return []


def fetch_all_jobs(providers: list[str]):
    all_jobs = []

    for provider in providers:
        jobs = fetch_by_provider(provider)
        all_jobs.extend(jobs)

    return all_jobs
    