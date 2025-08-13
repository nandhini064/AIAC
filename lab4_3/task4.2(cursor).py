def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    test_strings = ["NICY", "Union", "Sathwik"]
    for s in test_strings:
        print(f"Input: \"{s}\"")
        print(f"Output: {count_vowels(s)}")
