def factorial(n):
    """Calculate the factorial of a given number n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    try:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(e)
