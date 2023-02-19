# data section
# student = [(1, "student 1", "0/0/0"),]
# course = [(1, "course 1"),(2, "course 2"),]
# mark = [(0,0),]

student = []
course = []
mark = []

# Input function
def inputfunc():
    c_nb = int(input("Input number of course: "))
    print("Number of course: ", c_nb)
    for i in range(c_nb):
        course.append((
            str(input("\nCourse ID: ")),
            str(input("Course name: ")),
        ))

    s_nb = int(input("\nInput number of student: "))
    print("Number of student: ", s_nb)
    for i in range(s_nb):
        student.append((
            str(input("\nStudent ID: ")),
            str(input("Student name: ")),
            str(input("Student DoB: "))
        ))

        std_mark = []
        for crs in course:
            std_mark.append(float(input(f"Course {crs[1]} mark: ")))
        mark.append(std_mark)

# List function
def listfunc():
    for idx, std in enumerate(student):
        print(f"""
Student: {std[1]}
-----------------------
Student ID: {std[0]}
Student Name: {std[1]}
Student DoB: {std[2]}""")

        for jdx, crs in enumerate(course):
            print(f"""
Course ID: {crs[0]}
Course Name: {crs[1]}
Course Mark: {mark[idx][jdx]}""")

# Test section
if __name__ == "__main__":
    print("Hello user")
    print("Starting program: \n")
    print("Input from user...")
    inputfunc()

    print("Listing...")
    listfunc()