def calculate_bill(units):
    """
    Calculate electricity bill based on units consumed.
    Slabs:
    - First 100 units: Rs. 5/unit
    - Next 100 units (101-200): Rs. 7/unit
    - Above 200 units: Rs. 10/unit
    """
    bill = 0
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)
    else:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return bill

def main():
    while True:
        try:
            units = int(input("Enter the number of electricity units consumed: "))
            if units < 0:
                print("Units cannot be negative. Please enter a valid number.")
                continue
            total_bill = calculate_bill(units)
            print(f"Total electricity bill for {units} units: Rs. {total_bill}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for units.")

if __name__ == "__main__":
    main()
