def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x
 
def main():
    shape = input("Enter the shape (rectangle, square, circle): ").lower()
    if shape == "rectangle":
        x = float(input("Enter the length: "))
        y = float(input("Enter the width: "))
        area = calculate_area(shape, x, y)
    elif shape == "square":
        x = float(input("Enter the side length: "))
        area = calculate_area(shape, x)
    elif shape == "circle":
        x = float(input("Enter the radius: "))
        area = calculate_area(shape, x)
    else:
        print("Invalid shape.")
        return
    print(f"The area of the {shape} is {area}")

if __name__ == "__main__":
    main()