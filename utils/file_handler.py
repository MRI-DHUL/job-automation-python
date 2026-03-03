import os
from datetime import datetime
import csv


def generate_file_paths():
    os.makedirs("output", exist_ok=True)

    files = os.listdir("output")
    numbers = []

    for file in files:
        if file.startswith("Job"):
            try:
                num = int(file.split("_")[0].replace("Job", ""))
                numbers.append(num)
            except:
                pass

    next_num = max(numbers, default=0) + 1
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    base = f"Job{next_num}_{timestamp}"

    return (
        os.path.join("output", base + ".txt"),
        os.path.join("output", base + ".csv")
    )


def save_txt(path, jobs, email):
    with open(path, "w", encoding="utf-8") as f:
        for i, job in enumerate(jobs, 1):
            text = (
                f"Job {i}\n\n"
                f"Title     : {job['title']}\n"
                f"Company   : {job['company']}\n"
                f"Location  : {job['location'] or 'Not specified'}\n"
                f"Apply Link: {job['url']}\n"
                f"Source    : {job['source']}\n"
                f"Saved For : {email}\n"
                f"{'-'*50}\n"
            )
            # print(text)
            f.write(text)


def save_csv(path, jobs):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Link", "Source"])

        for job in jobs:
            writer.writerow([
                job["title"],
                job["company"],
                job["location"] or "",
                job["url"],
                job["source"]
            ])