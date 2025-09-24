operation = "multiply"
a, b = 5, 3

# First method: using if-elif-else
if operation == "add":
    result = a + b
elif operation == "subtract":
    result = a - b
elif operation == "multiply":
    result = a * b
else:
    result = None

# Second method: using dictionary mapping
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y
}

result = operations.get(operation, lambda x, y: None)(a, b)
print(result)
