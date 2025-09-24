from student_data import read_students, header
import csv

def sort_Students():
    print("------ SORT STUDENTS ------")
    students = read_students()
    sort_field = input("Sort by (Finalmarks / Attendance): ")

    if sort_field not in ["Finalmarks", "Attendance"]:
        print("Invalid field.")
        return

    try:
        sorted_students = sorted(students, key=lambda x: float(x[sort_field]), reverse=True)
        for s in sorted_students:
            print(f'{s["Roll_no"]} - {s["Name"]} - {sort_field}: {s[sort_field]}')

        export = input("Export this sorted list to CSV? (y/n): ").lower()
        if export == 'y':
            filename = f"sorted_{sort_field}.csv"
            with open(filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(sorted_students)
            print(f"Sorted list saved as {filename}")

    except ValueError:
        print("Error sorting: Make sure all fields are numeric.")
