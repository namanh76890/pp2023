class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}
    
    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.students = {}
    
    def add_student(self, student):
        self.students[student.id] = student
        
class MarkManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}
    
    def add_student(self, id, name, dob):
        student = Student(id, name, dob)
        self.students[id] = student
        
    def add_course(self, id, name):
        course = Course(id, name)
        self.courses[id] = course
        
    def add_marks(self, student_id, course_id, marks):
        student = self.students[student_id]
        student.add_marks(course_id, marks)
        course = self.courses[course_id]
        course.add_student(student)
    
    def list_courses(self):
        print("List of courses:")
        for course_id, course in self.courses.items():
            print(f"{course_id}: {course.name}")
    
    def list_students(self):
        print("List of students:")
        for student_id, student in self.students.items():
            print(f"{student_id}: {student.name}")
            
    def show_marks(self, student_id, course_id):
        student = self.students[student_id]
        course = self.courses[course_id]
        if student_id not in course.students:
            print("Student not enrolled in the selected course.")
        else:
            marks = student.marks.get(course_id)
            print(f"Marks for {student.name} in {course.name}: {marks}")

#####################################
mark_system = MarkManagementSystem()

# Input students
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    mark_system.add_student(id, name, dob)

# Input courses
num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    mark_system.add_course(id, name)

# Select a course and input marks for students
mark_system.list_courses()
course_id = input("Select a course to input marks: ")
for student_id, student in mark_system.students.items():
    marks = int(input(f"Enter marks for {student.name} ({student_id}) in {mark_system.courses[course_id].name}: "))
    mark_system.add_marks(student_id, course_id, marks)

# List courses, students, and show marks
mark_system.list_courses()
mark_system.list_students()
student_id = input("Select a student to show marks: ")
mark_system.show_marks(student_id, course_id)
