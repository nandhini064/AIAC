def factorial(n):
    """Calculate the factorial of a given number n using a for loop."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number to calculate its factorial: "))
    try:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
    except ValueError as e:
        print(e)


