from student_data import read_students, header
import csv

def filter_Students():
    print("------ FILTER STUDENTS BY ATTENDANCE ------")
    try:
        threshold = float(input("Enter attendance threshold (e.g., 75): "))
        students = read_students()
        filtered = [s for s in students if float(s["Attendance"]) < threshold]

        if not filtered:
            print("No students found with attendance below the threshold.")
            return

        print("Students below threshold:")
        for s in filtered:
            print(f'{s["Roll_no"]} - {s["Name"]} - Attendance: {s["Attendance"]}%')

        export = input("Export this filtered list to CSV? (y/n): ").lower()
        if export == 'y':
            filename = f"filtered_attendance_below_{threshold}.csv"
            with open(filename, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=header)
                writer.writeheader()
                writer.writerows(filtered)
            print(f"Filtered list saved as {filename}")

    except ValueError:
        print("Invalid input. Please enter a numeric threshold.")
