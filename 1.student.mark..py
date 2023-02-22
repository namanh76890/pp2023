#Input name and ID of students
def input_info_students():
    num_students = int(input("Enter the number of students: "))
    info_students = []
    for i in range(num_students):
        name = input("Enter a student name: ")
        id_students = input("Enter the Student ID: ")
        info_students.append((name, id_students))
    return info_students

#Input Mark titles
def input_marks():
    num_marks = int(input("Enter the number of marks: "))
    title_marks = []
    for i in range(num_marks):
        subject_marks = input("Enter the subject mark: ")
        title_marks.append(subject_marks)
    return title_marks

#Input school_year
def input_school_year():
    school_year = input("Enter school year: ")
    return school_year

#Input semester
def input_semester():
    semester = input("Enter semester: ")
    return semester

#Input marks for each subject
def input_students_marks(info_students, title_marks):
    marks = []
    for name, id_students in info_students:
        for title_mark in title_marks:
            print("Student name:", name, "Student ID:", id_students, "Subject:", title_mark)
            score = input("Enter mark: ")
            marks.append((name, id_students, title_mark, score))
    return marks

#Display info
def display(students_marks):
    for student_mark in students_marks:
        print("Student name:", student_mark[0], "; Student ID:", student_mark[1], "; Subject:", student_mark[2], "; Mark:", student_mark[3])

#Modify Main Def
def main():
    info_students = input_info_students()
    title_marks = input_marks()
    school_year = input_school_year()
    semester = input_semester()
    students_marks = input_students_marks(info_students, title_marks)
    print("School year:", school_year)
    print("Semester:", semester)
    display(students_marks)


#Run
main()
