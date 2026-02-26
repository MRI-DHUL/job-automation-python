import re

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.com$'
    return re.match(pattern, email) is not None