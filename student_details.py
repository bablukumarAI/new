class Student:
    def __init__(self):
        self.name = input("Enter student's name : ")
        self.clas = input("Enter student's class : ")
        self.roll = int(input("Enter student's rollno : "))
    def display(self):
        print("----student information---")
        print("Student name :", self.name)
        print("Student class :", self.clas)
        print("student roll no :", self.roll)

s1 = Student()
s1.display()