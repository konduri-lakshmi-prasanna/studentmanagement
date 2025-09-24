import csv
import os

FILENAME = "student.csv"
DELETED_FILE = "students_deleted.csv"

header = ["Roll_no", "Name", "Branch", "Year", "Gender", "Age", "Attendance",
          "Mid1_marks", "Mid2_marks", "Quizmarks", "Finalmarks"]

# Ensure CSV exists
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        print("student.csv created successfully")

def read_students():
    with open(FILENAME, newline='') as f:
        return list(csv.DictReader(f))

def write_students(students):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(students)
