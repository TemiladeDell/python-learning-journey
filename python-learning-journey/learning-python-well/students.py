import random
from datetime import datetime

class student:
    def __init__(self, name, age, Id, course=None, course_years=None, registration_date=None):
        self.name = name
        self.age = age
        self.Id = Id
        self.course = course
        self.course_years = course_years
        self.registration_date = registration_date




class student_manager:
    def __init__(self):
        self.students = []
    
    def add_student(self):
        student_name = input("Enter student name: ")
        student_age = input("Enter student age: ")
        course = input("Enter course: ")
        course_years = input("Enter number of years for the course: ")
        registration_date = input(
            "Enter registration date and time (YYYY-MM-DD HH:MM): "
        )
        try:
            registration_date = datetime.strptime(
                registration_date, "%Y-%m-%d %H:%M"
            )
        except ValueError:
            print("Invalid date and time format")
            return
        id = f"{random.randint(0,99999):05d}"
        student_id = f"STU-{id}"
        


        student_name = student(
            student_name,
            student_age,
            student_id,
            course,
            course_years,
            registration_date,
        )
        self.students.append(student_name)


    def search_students(self):
        student_found = False
        student_search = input("Enter the Id of the student for search: ")
        for student in self.students:
            if student.Id.lower() == student_search.lower():
                student_found = True
                print(f"Student name: {student.name}\nStudent age: {student.age}\nStudent ID: {student.Id}")

        if student_found == False:
            print("Student does not exist")



