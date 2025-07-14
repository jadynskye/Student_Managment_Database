# student_repo.py

import sqlite3
from student import Student  # grabbing the student class from student.py

class StudentRepository:
    def __init__(self):
        # connect to database file
        self.conn = sqlite3.connect("students.db")
        self.cursor = self.conn.cursor()
        self.create_table()  # make sure the table exists

    def create_table(self):
        # creates "students" table if not there
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                grade INTEGER
            )
        ''')
        self.conn.commit()

    def add_student(self, student):
        # add a new student 
        self.cursor.execute('''
            INSERT INTO students (student_id, name, age, grade)
            VALUES (?, ?, ?, ?)
        ''', (student.student_id, student.name, student.age, student.grade))
        self.conn.commit()

    def get_students(self):
        # gets all the students from the table
        self.cursor.execute('SELECT * FROM students')
        rows = self.cursor.fetchall()

        # turn the data into Student objects
        students = []
        for row in rows:
            student = Student(*row)  # *row unpacks the tuple
            students.append(student)

        return students

    def delete_student(self, student_id):
        # delete the student with the matching ID
        self.cursor.execute('DELETE FROM students WHERE student_id = ?', (student_id,))
        self.conn.commit()