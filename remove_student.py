from student_utils import read_students, write_students

def remove_student():
    print("------ REMOVE STUDENT ------")
    students = read_students()
    roll = input("Enter Roll Number of student to remove: ")

    for s in students:
        if s['Roll_no'] == roll:
            students.remove(s)
            write_students(students)
            print(f"Student with Roll No {roll} removed successfully.")
            return

    print("No student found with that Roll Number.")
