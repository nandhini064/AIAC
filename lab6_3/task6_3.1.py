def calculate_marks(marks):
    if(marks>=90):
        return "A"
    elif(marks>=75):
        return "B"
    elif(marks>=60):
        return "C"
    else:
        return "fail"
def student(name,rollno,marks):
    print("----Student Marks----")
    print("Name:", name)
    print("Roll No:", rollno)
    print("Marks:", marks)
    grade = calculate_marks(marks)
    print("Grade:", grade)
    if grade == "fail":
        print("Better luck next time!")
        print("You can do it!")
    else:
        print("Congratulations! You have passed.")
        print("Keep up the good work!")
name=input("Enter your name: ")
rollno=input("Enter your roll number: ")
marks=float(input("Enter your marks: "))
student(name,rollno,marks)
