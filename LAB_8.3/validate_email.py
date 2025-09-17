import re
from typing import Pattern


def compile_email_regex() -> Pattern[str]:
    # Pragmatic RFC 5322-inspired regex for common valid emails
    return re.compile(
        r"^(?=.{1,254}$)"  # overall length limit (practical bound)
        r"(?=.{1,64}@)"     # local-part length limit
        r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]+"  # local-part
        r"@"
        r"(?:[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?\.)+"  # subdomains
        r"[A-Za-z]{2,63}$"  # TLD (2-63 characters)
    )


EMAIL_REGEX: Pattern[str] = compile_email_regex()


def is_valid_email(email_address: str) -> bool:
    """Return True if email_address is a valid email (pragmatic regex check)."""
    if not isinstance(email_address, str):
        return False
    candidate = email_address.strip()
    if not candidate:
        return False
    return EMAIL_REGEX.match(candidate) is not None


def _cli() -> None:
    import sys

    if len(sys.argv) == 2:
        # Single argument mode: `python validate_email.py test@example.com`
        email_arg = sys.argv[1]
        print("VALID" if is_valid_email(email_arg) else "INVALID")
        return

    # Interactive mode
    try:
        user_input = input("Enter an email address to validate: ").strip()
    except EOFError:
        user_input = ""

    if not user_input:
        print("No input provided.")
        return

    print("VALID" if is_valid_email(user_input) else "INVALID")


if __name__ == "__main__":
    _cli()


