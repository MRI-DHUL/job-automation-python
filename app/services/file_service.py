import json
from datetime import datetime
from pathlib import Path
import re


def save_jobs(jobs):
    if not jobs:
        print("No jobs to save.")
        return

    output_dir = Path("output")
    output_dir.mkdir(parents=True, exist_ok=True)

    existing_numbers = []

    for f in output_dir.glob("job *.json"):
        match = re.match(r"job (\d+)", f.stem)
        if match:
            existing_numbers.append(int(match.group(1)))

    next_number = max(existing_numbers, default=0) + 1

    now = datetime.now()
    date_part = now.strftime("%d-%m-%Y")
    time_part = now.strftime("%I-%M%p").lower()

    filename = f"job {next_number} - {date_part} - {time_part}.json"
    filepath = output_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)
