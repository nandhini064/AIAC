def word_frequency(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        freq[word] = freq.get(word, 0) + 1
    return freq

# Example usage:
user_input = input("Enter a string: ")
result = word_frequency(user_input)
print("Word frequencies:", result)