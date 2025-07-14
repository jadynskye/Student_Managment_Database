# student_service.py

from student import Student  # import the student class
from student_repo import StudentRepository  # import the repo class

class StudentService:
    def __init__(self):
        self.repo = StudentRepository()  # set up the database stuff

    def add_student(self, student_id, name, age, grade):
        # only add if age > 15 and grade > 70
        if age <= 15:
            print("Age must be greater than 15.")
            return
        if grade <= 70:
            print("Grade must be greater than 70.")
            return

        # if all good, make a student and add to database
        student = Student(student_id, name, age, grade)
        self.repo.add_student(student)
        print("Student added!")

    def get_students(self):
        # get all students from the database
        return self.repo.get_students()

    def delete_student(self, student_id):
        # delete student by ID
        self.repo.delete_student(student_id)
        print("Student deleted (if they existed).")