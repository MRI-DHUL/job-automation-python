from email_validator import validate_email, EmailNotValidError


def validate_and_normalize_email(email: str):
    try:
        valid = validate_email(email)
        return True, valid.email
    except EmailNotValidError as e:
        return False, str(e)