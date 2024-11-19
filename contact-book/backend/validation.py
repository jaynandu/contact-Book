import re

def validate_email(email):
    """
    Validates email format.

    The regular expression used here breaks down as follows:

    ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$

    ^ asserts the start of the string
    [a-zA-Z0-9_.+-]+ asserts at least one character from the set of
        alphanumeric characters, underscores, periods, plus signs, or hyphens
    @ asserts the presence of an at sign
    [a-zA-Z0-9-]+ asserts at least one character from the set of
        alphanumeric characters or hyphens
    \. asserts the presence of a period
    [a-zA-Z0-9-.]+ asserts at least one character from the set of
        alphanumeric characters, periods, or hyphens
    $ asserts the end of the string

    If the provided email does not match this regular expression, a ValueError
    is raised with the message "Invalid email format.".
    """
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")


def validate_phone(phone):
    """Validates phone number format."""
    phone_regex = r"^\+?[0-9\s\-()]{7,15}$"
    if not re.match(phone_regex, phone):
        raise ValueError("Invalid phone number format.")
