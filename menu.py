from add_student import add_Student
from search_student import Search_Student
from update_student import update_Student
from delete_student import delete_Student
from report import generate_report
from sort_students import sort_Students
from filter_students import filter_Students

def menu():
    while True:
        print("\n------------- STUDENT MANAGEMENT SYSTEM --------------")
        print("1. Add New Student")
        print("2. Search Student")
        print("3. Update Student Record")
        print("4. Delete Student")
        print("5. Generate Report")
        print("6. Sort Students")
        print("7. Filter Students by Attendance")
        print("8. Exit")

        choice = input("Enter a choice: ")

        if choice == "1":
            add_Student()
        elif choice == "2":
            Search_Student()
        elif choice == "3":
            update_Student()
        elif choice == "4":
            delete_Student()
        elif choice == "5":
            generate_report()
        elif choice == "6":
            sort_Students()
        elif choice == "7":
            filter_Students()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice")
