import csv
from student_data import read_students, header

def generate_report():
    print("------ GENERATE REPORT ------")
    students = read_students()
    branch = input("Enter Branch: ")
    year = input("Enter Year: ")
    filtered = [s for s in students if s["Branch"] == branch and s["Year"] == year]

    if not filtered:
        print("No students found.")
        return

    total = len(filtered)
    marks = [float(s["Finalmarks"]) for s in filtered]
    average = sum(marks) / total
    highest = max(marks)
    lowest = min(marks)

    print(f"Total Students: {total}")
    print(f"Class Average: {average:.2f}")
    print(f"Highest Score: {highest}")
    print(f"Lowest Score: {lowest}")

    grades = {"A": 0, "B": 0, "C": 0, "D": 0}
    for m in marks:
        if m >= 85:
            grades["A"] += 1
        elif m >= 70:
            grades["B"] += 1
        elif m >= 50:
            grades["C"] += 1
        else:
            grades["D"] += 1

    print("Grade Distribution:")
    for grade, count in grades.items():
        print(f"{grade}: {count} students")

    export = input("Do you want to export this report? (y/n): ").lower()
    if export == 'y':
        filename = f"report_{branch}_{year}.csv"
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(filtered)
        print(f"Report saved as {filename}")
