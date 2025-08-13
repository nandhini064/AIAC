def count_lines_in_file(filename):
    """
    Reads a .txt file and returns the number of lines.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

# Example usage:
# print(count_lines_in_file("data.txt"))
# print(count_lines_in_file("notes.txt"))