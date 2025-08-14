import string
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
def to_lower(text):
    return text.lower()
def remove_stopwords(text, stopwords):
    words = text.split()
    filtered_words = [word for word in words if word not in stopwords]
    return ' '.join(filtered_words)
def main():
    stopwords = {
        'a', 'an', 'the', 'and', 'or', 'but', 'if', 'while', 'with', 'to', 'of', 'at', 'by', 'for', 'from', 'in', 'on', 'off', 'out', 'over', 'under', 'as', 'is', 'it', 'this', 'that', 'these', 'those', 'am', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'so', 'such'
    }
    user_text = input("Enter text: ")
    text_no_punct = remove_punctuation(user_text)
    text_lower = to_lower(text_no_punct)
    result = remove_stopwords(text_lower, stopwords)
    print(result)
if __name__ == "__main__":
    main()
