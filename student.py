#student.py

# class to hold info about each student
class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id  # unique ID number
        self.name = name              # name
        self.age = age                # age
        self.grade = grade            # grade