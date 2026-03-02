def show_main_menu():
    print("\n=== MAIN MENU ===")
    print("1. Fetch Jobs")
    print("2. Exit")


def show_fetch_menu(jobs_count, filtered_count):
    print("\n=== FETCH MENU ===")

    print(f"Jobs fetched     : {jobs_count}")
    print(f"Filtered jobs    : {filtered_count}")

    print("\n1. Select Provider")
    print("2. Apply Filters")
    print("3. Save Results")
    print("4. Back to Main Menu")
    print("5. Exit")