import os
from student_data import read_students, write_students, DELETED_FILE, header
import csv

def delete_Student():
    print("------ DELETE STUDENT ------")
    students = read_students()
    roll = input("Enter Roll Number to delete: ")
    found = None

    for s in students:
        if s["Roll_no"] == roll:
            found = s
            break

    if not found:
        print("Student not found.")
        return

    confirm = input("Are you sure you want to delete? (Yes/No): ").lower()
    if confirm == "yes":
        students.remove(found)
        write_students(students)

        with open(DELETED_FILE, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if os.path.getsize(DELETED_FILE) == 0:
                writer.writeheader()
            writer.writerow(found)

        print("Student deleted and saved to audit.")
    else:
        print("Deletion cancelled.")
