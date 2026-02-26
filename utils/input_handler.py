def get_input_with_attempts(prompt, validate_fn=None, error_msg="Invalid input", max_attempts=3):
    attempts = max_attempts

    while attempts > 0:
        value = input(prompt).strip()

        # If no validation function → accept any input
        if not validate_fn:
            return value

        # If valid
        if validate_fn(value):
            return value

        # If invalid
        attempts -= 1
        print(f"{error_msg}. Attempts left: {attempts}")

    print("Too many invalid attempts. Exiting...")
    exit()