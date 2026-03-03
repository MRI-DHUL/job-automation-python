from utils.file_handler import generate_file_paths, save_txt


def save_jobs(jobs, filtered_jobs, filters_applied, email):
    if not jobs:
        return False, "No jobs to save"

    if filters_applied and not filtered_jobs:
        return False, "No filtered jobs to save"

    if filters_applied:
        data_to_save = filtered_jobs
        count = len(filtered_jobs)
        label = "filtered jobs"
    else:
        data_to_save = jobs
        count = len(jobs)
        label = "total jobs"

    txt_path, csv_path = generate_file_paths()

    # save_txt
    save_txt(txt_path, data_to_save, email)

    return True, f"File saved successfully ({count} {label})"