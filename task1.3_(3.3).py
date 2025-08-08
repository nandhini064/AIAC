def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Please enter a non-negative number.")
            return
        print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
