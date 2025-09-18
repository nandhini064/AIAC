import csv

def stable_sort_employees():
    """
    Reads employee data (hardcoded sample for now),
    sorts by department (ascending) and salary (descending),
    and prints the result in CSV format.
    Sorting is stable → employees with the same dept & salary
    preserve input order.
    """

    # Sample input data
    lines = [
        "name,dept,salary",
        "Raj,Eng,120",
        "Maya,HR,90",
        "Abi,Eng,110"
    ]

    # Parse CSV lines into a list of dicts
    reader = csv.DictReader(lines)
    employees = list(reader)

    # Convert salary to int for sorting
    for emp in employees:
        emp["salary"] = int(emp["salary"])

    # Sort: dept (asc), salary (desc)
    sorted_employees = sorted(
        employees,
        key=lambda x: (x["dept"], -x["salary"])
    )

    # Print output in CSV format
    for emp in sorted_employees:
        print(f'{emp["name"]},{emp["dept"]},{emp["salary"]}')


# Run only if script is executed directly
if __name__ == "__main__":
    stable_sort_employees()
