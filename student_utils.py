import csv
import os

FILENAME = "student.csv"
header = ["Roll_no", "Name", "Branch", "Year", "Gender", "Age", "Attendance",
          "Mid1_marks", "Mid2_marks", "Quizmarks", "Finalmarks"]

# Create CSV if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
    print("student.csv created successfully")

# Read all students
def read_students():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, newline='') as f:
        return list(csv.DictReader(f))

# Write all students
def write_students(students):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(students)
