from student_data import read_students, write_students, header

def add_Student():
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
