def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    user_input = input().strip()
    # Example: "0 Celsius to Fahrenheit"
    try:
        parts = user_input.split()
        value = float(parts[0])
        from_unit = parts[1].lower()
        to_unit = parts[3].lower()
        if from_unit == "celsius" and to_unit == "fahrenheit":
            result = celsius_to_fahrenheit(value)
            print(f"{int(result) if result.is_integer() else result} Fahrenheit")
        elif from_unit == "fahrenheit" and to_unit == "celsius":
            result = fahrenheit_to_celsius(value)
            print(f"{int(result) if result.is_integer() else result} Celsius")
        else:
            print("Invalid conversion")
    except Exception:
        print("Invalid input format")

if __name__ == "__main__":
    main()
