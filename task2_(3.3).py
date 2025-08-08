def sort_numbers(numbers):
    """Sort a list of numbers in ascending order using a simple sorting algorithm (e.g., bubble sort)."""
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def main():
    input_str = input("Enter numbers separated by spaces: ")
    num_list = []
    for s in input_str.strip().split():
        if s.isdigit() or (s.startswith('-') and s[1:].isdigit()):
            num_list.append(int(s))
        else:
            print("Invalid input. Please enter only integers separated by spaces.")
            return
    sorted_list = sort_numbers(num_list)
    print("Sorted numbers:", sorted_list)

if __name__ == "__main__":
    main()


