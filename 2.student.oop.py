class Course():
    def __init__(self):
        self.id = input("Enter the course's id: ")
        self.name = input("Enter the course's name: ")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name


class Student():
    def __init__(self):
        self.id = input("Enter the student's id: ")
        self.name = input("Enter the student's name: ")
        self.dob = input("Enter the student's dob: ")

        self.__mark = []

    def add_mark(self, m):
        self.__mark.append(m)

    # Encapsulation part
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

    def get_mark(self):
        return self.__mark


class InputNum:
    # Ask the user to input something
    def input(args):
        return int(input(f"Enter the number of {args}: "))


def listing(input_student, input_course):
    for Student in input_student:
        i = 0
        print(f"""
Student ID: {Student.get_id()} 
Student name: {Student.get_name()} 
Student Dob: {Student.get_dob()}
---------------------------""")
        for Course in input_course:
            print(f"""
Course ID: {Course.get_id()} 
Course name: {Course.get_name()}
Course Mark: {Student.get_mark()[i]}""")
            i += 1


c_nb = InputNum.input("courses")
s_nb = InputNum.input("students")

input_student = []
for i in range(s_nb):
    print(f"Student {i + 1}")
    input_student.append(Student())

input_course = []
for i in range(c_nb):
    print(f"Course {i + 1}")
    input_course.append(Course())

for Student in input_student:
    mark = []
    for Course in input_course:
        m = float(input(f"Mark of {Course.get_name()} of student {Student.get_name()}: "))
        Student.add_mark(m)

listing(input_student, input_course)

