import csv
import time
import bisect
from collections import defaultdict
import os

# Sample dataset (will be written to CSV if it doesn't exist)
data = """Title,Author
The Great Gatsby,F. Scott Fitzgerald
To Kill a Mockingbird,Harper Lee
1984,George Orwell
Pride and Prejudice,Jane Austen
Moby-Dick,Herman Melville
The Catcher in the Rye,J.D. Salinger
The Hobbit,J.R.R. Tolkien
War and Peace,Leo Tolstoy
Crime and Punishment,Fyodor Dostoevsky
The Odyssey,Homer
"""

def create_csv(filename="library.csv"):
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(data)

def load_dataset(filename="library.csv"):
    dataset = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            dataset.append({"Title": row["Title"], "Author": row["Author"]})
    return dataset

def linear_search(dataset, keyword):
    result = []
    for book in dataset:
        if keyword.lower() in book["Title"].lower() or keyword.lower() in book["Author"].lower():
            result.append(book)
    return result

def binary_search(dataset, keyword):
    # Sort dataset by Title
    sorted_data = sorted(dataset, key=lambda x: x["Title"].lower())
    titles = [book["Title"].lower() for book in sorted_data]

    results = []
    idx = bisect.bisect_left(titles, keyword.lower())
    while idx < len(titles) and titles[idx].startswith(keyword.lower()):
        results.append(sorted_data[idx])
        idx += 1
    return results

def build_hash_index(dataset):
    index = defaultdict(list)
    for book in dataset:
        # Index both Title and Author
        index[book["Title"].lower()].append(book)
        index[book["Author"].lower()].append(book)
    return index

def hash_search(index, keyword):
    return index.get(keyword.lower(), [])

def compare_searches(dataset, keyword):
    hash_index = build_hash_index(dataset)

    # Linear Search
    start = time.time()
    linear_results = linear_search(dataset, keyword)
    linear_time = time.time() - start

    # Binary Search
    start = time.time()
    binary_results = binary_search(dataset, keyword)
    binary_time = time.time() - start

    # Hash Search
    start = time.time()
    hash_results = hash_search(hash_index, keyword)
    hash_time = time.time() - start

    return {
        "Linear Search": {"Results": linear_results, "Time": linear_time},
        "Binary Search": {"Results": binary_results, "Time": binary_time},
        "Hash Search": {"Results": hash_results, "Time": hash_time}
    }

if __name__ == "__main__":
    create_csv("library.csv")  # ensure CSV exists
    dataset = load_dataset("library.csv")

    keyword = input("Enter a keyword to search (title/author): ")

    results = compare_searches(dataset, keyword)

    print("\n===== Search Results =====")
    for method, data in results.items():
        print(f"\n{method}: {len(data['Results'])} matches found in {data['Time']:.6f} seconds")
        for book in data['Results']:
            print(f"   {book['Title']} by {book['Author']}")
