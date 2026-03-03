from utils.validator import validate_and_normalize_email
from utils.input_handler import get_input_with_attempts

from services.job_service import (
    get_provider_choice,
    fetch_jobs,
    apply_filters
)

from services.file_service import save_jobs
from services.cli_menu import show_main_menu, show_fetch_menu


def main():
    print("=== JOB AUTOMATION TOOL ===\n")

    # Email validation
    email = get_input_with_attempts(
        "Enter your email: ",
        validate_fn=validate_and_normalize_email,
        error_msg="Invalid email address"
    )

    print("Email validated successfully\n")

    jobs = []
    filtered_jobs = []
    filters_applied = False

    while True:
        show_main_menu()
        choice = input("Select option: ").strip()

        # FETCH JOBS
        if choice == "1":

            print("\nFetching jobs from all providers...\n")

            jobs = fetch_jobs("all")
            filtered_jobs = []
            filters_applied = False

            print(f"Fetched {len(jobs)} jobs.\n")

            while True:
                show_fetch_menu(len(jobs), len(filtered_jobs))
                sub_choice = input("Select option: ").strip()

                # Select Provider
                if sub_choice == "1":
                    provider = get_provider_choice(get_input_with_attempts)

                    print(f"\nFetching jobs from {provider}...\n")

                    jobs = fetch_jobs(provider)
                    filtered_jobs = []
                    filters_applied = False

                    print(f"Fetched {len(jobs)} jobs.\n")

                # Apply Filters
                elif sub_choice == "2":
                    if not jobs:
                        print("⚠ Fetch jobs first.")
                        continue

                    filtered_jobs = apply_filters(jobs)
                    filters_applied = True

                    print(f"\nFiltered Jobs: {len(filtered_jobs)}\n")

                # Save Results
                elif sub_choice == "3":
                    success, message = save_jobs(
                        jobs,
                        filtered_jobs,
                        filters_applied,
                        email
                    )

                    if success:
                        print(f"Success: {message}")
                    else:
                        print(f"Error: {message}")

                # Back to Main Menu
                elif sub_choice == "4":
                    break

                # Exit
                elif sub_choice == "5":
                    print("Exiting... Goodbye!")
                    return
                
                else:
                    print("Invalid option.")

        # EXIT
        elif choice == "2":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()