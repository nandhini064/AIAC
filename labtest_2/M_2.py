def is_palindrome(s: str) -> bool:
    """
    Check whether the input string `s` is a palindrome.

    Rules:
    - Ignores case (case-insensitive).
    - Ignores all non-alphanumeric characters (spaces, punctuation, etc.).
    - Empty string and single-character strings are considered palindromes.

    Parameters:
        s (str): Input string to check.

    Returns:
        bool: True if `s` is a palindrome under the rules above, False otherwise.
    """
    # Keep only alphanumeric characters in lowercase
    filtered = [ch.lower() for ch in s if ch.isalnum()]

    # Compare using two pointers
    i, j = 0, len(filtered) - 1
    while i < j:
        if filtered[i] != filtered[j]:
            return False
        i += 1
        j -= 1
    return True


# ---- Main program ----
user_input = input("Enter a string to check for palindrome: ")
if is_palindrome(user_input):
    print("True")
else:
    print("False ")
