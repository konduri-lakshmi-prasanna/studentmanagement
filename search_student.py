from student_data import read_students

def Search_Student():
    print("------ SEARCH STUDENT ------")
    students = read_students()
    mode = input("Search by Roll_no (R) or Name (N)? ").upper()

    found = []
    if mode == "R":
        roll = input("Enter Roll Number: ")
        found = [s for s in students if s['Roll_no'] == roll]
    elif mode == "N":
        name = input("Enter part of name: ").lower()
        found = [s for s in students if name in s['Name'].lower()]
    else:
        print("Invalid search mode.")
        return

    if found:
        for s in found:
            print(s)
    else:
        print("No student found by the given data.")
