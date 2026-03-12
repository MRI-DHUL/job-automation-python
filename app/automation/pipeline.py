from app.utils.config_loader import load_config
from app.providers.aggregator import fetch_all_jobs
from app.services.job_service import apply_filters
from app.services.deduplicator import remove_duplicate_jobs
from app.services.file_service import save_jobs


def run_pipeline(return_jobs=False, override_filters=None, override_providers=None):
    cfg = load_config()

    providers = override_providers or cfg.get("providers", [])
    filters = override_filters or cfg.get("filters", {})

    jobs = fetch_all_jobs(providers)
    jobs = remove_duplicate_jobs(jobs)
    filtered = apply_filters(jobs, filters)

    if cfg.get("output", {}).get("save_to_file", True):
        save_jobs(filtered)

    if return_jobs:
        return filtered