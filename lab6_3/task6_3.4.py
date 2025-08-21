def sum_to_n(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total
def print_first_n_numbers(n):
    print("Using for loop:")
    for i in range(1, n + 1):
        print(i, end=' ')
    print("\nUsing while loop:")
    i = 1
    while i <= n:
        print(i, end=' ')
        i += 1
        print()

    # Example usage:
n = int(input("Enter n: "))
print_first_n_numbers(n)
print(f"Sum of first {n} numbers is: {sum_to_n(n)}")
