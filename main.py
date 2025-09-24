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
    with open(FILENAME, newline='') as f:
        return list(csv.DictReader(f))

# Write all students
def write_students(students):
    with open(FILENAME, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(students)

# Add Student
def add_student():
    print("------ ADD NEW STUDENT ------")
    students = read_students()
    roll_no_set = {s['Roll_no'] for s in students}
    roll = input("Enter Roll Number: ")

    if roll in roll_no_set:
        print("Student with this roll number already exists.")
        return

    try:
        name = input("Enter Name: ")
        branch = input("Enter Branch: ")
        year = input("Enter Year: ")
        gender = input("Enter Gender: ")
        age = int(input("Enter Age: "))
        attendance = float(input("Enter Attendance %: "))
        mid1 = float(input("Enter Mid1 Marks: "))
        mid2 = float(input("Enter Mid2 Marks: "))
        quiz = float(input("Enter Quiz Marks: "))
        final = float(input("Enter Final Marks: "))

        student = {
            "Roll_no": roll,
            "Name": name,
            "Branch": branch,
            "Year": year,
            "Gender": gender,
            "Age": age,
            "Attendance": attendance,
            "Mid1_marks": mid1,
            "Mid2_marks": mid2,
            "Quizmarks": quiz,
            "Finalmarks": final
        }

        students.append(student)
        write_students(students)
        print("Student added successfully.")

    except ValueError:
        print("Invalid input. Please enter numbers for age and marks.")

# Menu (only Add Student)
def menu():
    while True:
        print("\n------------- STUDENT MANAGEMENT SYSTEM --------------")
        print("1. Add New Student")
        print("2. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
