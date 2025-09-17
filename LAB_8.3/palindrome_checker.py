import re
def is_palindrome(sentence: str) -> bool:
    """Check if a given sentence is a palindrome.
    A palindrome reads the same forwards and backwards, ignoring:
    - Case (uppercase/lowercase)
    - Spaces
    - Punctuation marks
    - Special characters
    Examples:
    - "A man a plan a canal Panama" -> True
    - "race a car" -> False
    - "Was it a car or a cat I saw?" -> True
    """
    if not isinstance(sentence, str):
        return False
    # Convert to lowercase and remove all non-alphanumeric characters
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', sentence.lower())
    # Check if empty after cleaning
    if not cleaned:
        return True  # Empty string is considered palindrome
    # Compare with its reverse
    return cleaned == cleaned[::-1]
def _cli() -> None:
    import sys
    if len(sys.argv) == 2:
        # Single argument mode: `python palindrome_checker.py "A man a plan a canal Panama"`
        sentence = sys.argv[1]
        result = is_palindrome(sentence)
        print("PALINDROME" if result else "NOT PALINDROME")
        return
    # Interactive mode
    try:
        user_input = input("Enter a sentence to check: ").strip()
    except EOFError:
        user_input = ""
    if not user_input:
        print("No input provided.")
        return
    result = is_palindrome(user_input)
    print("PALINDROME" if result else "NOT PALINDROME")
if __name__ == "__main__":
    _cli()
