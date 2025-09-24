class Student:
    """
    Represents a student with name, age, and a list of marks.
    """
    def __init__(self, name, age, marks):
        """
        Initialize a Student object.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list): List of marks (int or float).
        """
        self.name = name
        self.age = age
        self.marks = marks

    def details(self):
        """
        Print the student's name and age.
        """
        print(f"Name: {self.name}, Age: {self.age}")

    def total(self):
        """
        Calculate and return the total marks.

        Returns:
            int or float: The sum of all marks.
        """
        return sum(self.marks)

    def __str__(self):
        """
        Return a readable string representation of the student.
        """
        return f"Student(Name: {self.name}, Age: {self.age}, Marks: {self.marks})"

if __name__ == "__main__":
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter mark {i}: "))
        marks.append(mark)
    student = Student(name, age, marks)
    student.details()
    print("Total Marks:", student.total())
    print(student)
            