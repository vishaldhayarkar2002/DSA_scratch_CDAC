class Student:
    def __init__(self, name, roll_no, total_marks):
        self.name = name
        self.roll_no = roll_no
        self.total_marks = total_marks

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
total_marks = int(input("Enter total marks: "))

student = Student(name, roll_no, total_marks)

print("Student Name:", student.name)
print("Roll Number:", student.roll_no)
print("Total Marks:", student.total_marks)