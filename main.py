# main.py

from student_service import StudentService  # import service

# service becomes an object so it can be used
service = StudentService()

# bool to run the program until user chooses to exit
while True:
    #options
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        # get info from user
        try:
            student_id = int(input("Enter student ID: "))
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = int(input("Enter grade: "))

            service.add_student(student_id, name, age, grade)

        except ValueError:
            print("Invalid input. Please enter numbers for ID, age, and grade.")

    elif choice == "2":
        # show all students
        students = service.get_students()
        print("\n Student List:")
        for s in students:
            print(f"ID: {s.student_id}, Name: {s.name}, Age: {s.age}, Grade: {s.grade}")

    elif choice == "3":
        try:
            student_id = int(input("Enter the ID of the student to delete: "))
            service.delete_student(student_id)
        except ValueError:
            print("Invalid ID.")

    elif choice == "4":
        print("Exiting!")
        break

    else:
        print("Not a valid choice. Please pick between 1 and 4.")