class sru_student:
    def __init__(self):
        self.name = input("Enter student name: ")
        self.roll_no = input("Enter roll number: ")
        self.hostel_status = input("Hostel status (Yes/No): ")
        self.fee_paid = False

    def fee_update(self):
        status = input("Has the fee been paid? (Yes/No): ")
        if status.strip().lower() == "yes":
            self.fee_paid = True
        else:
            self.fee_paid = False

    def display_details(self):
        print("\nStudent Details:")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Paid: {'Yes' if self.fee_paid else 'No'}")

if __name__ == "__main__":
    student = sru_student()
    student.fee_update()
    student.display_details()
