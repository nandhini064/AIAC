import re
from collections import Counter

# Example sentiment lexicon (expand for real use)
SENTIMENT_LEXICON = {
    'good': 1,
    'happy': 1,
    'excellent': 2,
    'bad': -1,
    'sad': -1,
    'terrible': -2,
    'neutral': 0
}

def preprocess_text(text):
    # Lowercase and remove non-alphabetic characters
    return re.findall(r'\b[a-z]+\b', text.lower())

def analyze_sentiment(text, lexicon=SENTIMENT_LEXICON):
    words = preprocess_text(text)
    score = sum(lexicon.get(word, 0) for word in words)
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

def detect_bias(data):
    # Count sentiment classes
    sentiments = [analyze_sentiment(text) for text in data]
    counts = Counter(sentiments)
    total = sum(counts.values())
    bias_report = {}
    for sentiment, count in counts.items():
        bias_report[sentiment] = count / total
    return bias_report

def handle_bias(data, threshold=0.5):
    # Simple undersampling if any class exceeds threshold
    sentiments = [analyze_sentiment(text) for text in data]
    counts = Counter(sentiments)
    max_class = max(counts, key=counts.get)
    if counts[max_class] / len(data) > threshold:
        # Undersample majority class
        filtered_data = [text for text in data if analyze_sentiment(text) != max_class]
        filtered_data += [text for text in data if analyze_sentiment(text) == max_class][:int(threshold * len(data))]
        return filtered_data
    return data

# Example usage
if __name__ == "__main__":
    dataset = [
        "I am very happy with this product.",
        "This is a terrible experience.",
        "The service was good.",
        "I feel sad about the results.",
        "Excellent work!",
        "bad outcome",
        "neutral response"
    ]

    print("Bias report before handling:", detect_bias(dataset))
    balanced_data = handle_bias(dataset)
    print("Bias report after handling:", detect_bias(balanced_data))
    for text in balanced_data:
        print(f"Text: {text} | Sentiment: {analyze_sentiment(text)}")