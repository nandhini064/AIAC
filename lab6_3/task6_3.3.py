def classify_age(age):
    if age <= 12:
        return "Child"
    elif age <= 19:
        return "Teenager"
    else:
        return "Adult"
age=int(input("Enter your age:"))
print(classify_age(age))
