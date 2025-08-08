def get_numbers():
    """Prompt the user to enter numbers separated by spaces and return as a list of integers."""
    input_str = input("Enter numbers separated by spaces: ")
    num_list = []
    for s in input_str.strip().split():
        if s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
            num_list.append(int(s))
        else:
            print("Invalid input. Please enter only integers separated by spaces.")
            return None
    return num_list

def sort_numbers(numbers):
    """Sort a list of numbers in ascending order using bubble sort."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def display_sorted(numbers):
    """Display the sorted list of numbers."""
    print("Sorted numbers:", numbers)

def main():
    numbers = get_numbers()
    if numbers is not None:
        sorted_list = sort_numbers(numbers)
        display_sorted(sorted_list)

if __name__ == "__main__":
    main()
