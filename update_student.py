from student_data import read_students, write_students

def update_Student():
    print("------ UPDATE STUDENT RECORD ------")
    students = read_students()
    roll = input("Enter Roll Number: ")
    found = False

    for s in students:
        if s["Roll_no"] == roll:
            print("Current Record:", s)
            field = input("Update 'marks' or 'attendance'? ").lower()
            if field == "marks":
                s["Mid1_marks"] = input("Mid1: ")
                s["Mid2_marks"] = input("Mid2: ")
                s["Quizmarks"] = input("Quiz: ")
                s["Finalmarks"] = input("Final: ")
            elif field == "attendance":
                s["Attendance"] = input("New Attendance %: ")
            else:
                print("Invalid choice.")
                return
            found = True
            break

    if found:
        write_students(students)
        print("Record updated successfully.")
    else:
        print("Student not found.")
