import time
import random

# Define the Student class
class Student:
    def __init__(self, name, roll_no, cgpa):  # fixed __init__
        self.name = name
        self.roll_no = roll_no
        self.cgpa = cgpa

    def __repr__(self):  # fixed __repr__
        return f"{self.name} (Roll No: {self.roll_no}, CGPA: {self.cgpa})"


# Quick Sort implementation (supports key and reverse)
def quick_sort(arr, key=lambda x: x, reverse=False):
    def _quick_sort(items, low, high):
        if low < high:
            pi = partition(items, low, high)
            _quick_sort(items, low, pi - 1)
            _quick_sort(items, pi + 1, high)

    def partition(items, low, high):
        pivot = key(items[high])
        i = low - 1
        for j in range(low, high):
            if (key(items[j]) > pivot) if reverse else (key(items[j]) < pivot):
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quick_sort(arr, 0, len(arr) - 1)
    return arr


# Merge Sort implementation (supports key and reverse)
def merge_sort(arr, key=lambda x: x, reverse=False):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L, key=key, reverse=reverse)
        merge_sort(R, key=key, reverse=reverse)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if (key(L[i]) > key(R[j])) if reverse else (key(L[i]) < key(R[j])):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


# Generate random student data
def generate_students(n):
    first_names = [
        "Aarav", "Vihaan", "Vivaan", "Aditya", "Arjun", "Sai", "Krishna", "Ishaan",
        "Anaya", "Diya", "Isha", "Kavya", "Meera", "Saanvi", "Tanya", "Riya", "Neha"
    ]
    last_names = ["Patel", "Sharma", "Reddy", "Verma", "Singh", "Mehta", "Chopra"]

    students = []
    for i in range(1, n + 1):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        roll_no = f"R{i:04d}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append(Student(name, roll_no, cgpa))
    return students


# Print top N students
def print_top_students(students, top_n=10):
    print(f"Top {top_n} Students:")
    for i, student in enumerate(students[:top_n], 1):
        print(f"{i}. {student}")


def main():
    num_students = 100
    students = generate_students(num_students)

    # Quick Sort
    students_qs = students.copy()
    start_qs = time.time()
    quick_sort(students_qs, key=lambda s: s.cgpa, reverse=True)
    end_qs = time.time()
    print("Quick Sort Runtime: {:.6f} seconds".format(end_qs - start_qs))
    print_top_students(students_qs, 10)
    print()

    # Merge Sort
    students_ms = students.copy()
    start_ms = time.time()
    merge_sort(students_ms, key=lambda s: s.cgpa, reverse=True)
    end_ms = time.time()
    print("Merge Sort Runtime: {:.6f} seconds".format(end_ms - start_ms))
    print_top_students(students_ms, 10)


if __name__ == "__main__":  # fixed __main__
    main()
