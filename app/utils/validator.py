from email_validator import validate_email, EmailNotValidError

### Email Validation ###

def validate_email_address(email: str) -> bool:
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

### Retry Validator ###

def prompt_email_with_retry(input_func=input) -> str:
    attempts = 3

    for i in range(attempts):
        email = input_func("Enter email: ").strip()

        if validate_email_address(email):
            return email

        print(f"Invalid email. Attempts left: {attempts - i - 1}")

    raise ValueError("Maximum attempts exceeded for email input")

### Validators ###

def validate_non_empty(value: str, field: str) -> str:
    if not value or not value.strip():
        raise ValueError(f"{field} cannot be empty")
    return value.strip()


def validate_positive_int(value: int, field: str) -> int:
    if value < 0:
        raise ValueError(f"{field} must be positive")
    return value