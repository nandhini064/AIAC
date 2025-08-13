def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)

# Example usage:
if __name__ == "__main__":
    test_files = ["sample1.txt", "notes.txt", "empty.txt"]
    for fname in test_files:
        print(f"Input: \"{fname}\"")
        print(f"Output: {count_lines_in_file(fname)}")
