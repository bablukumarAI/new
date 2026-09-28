class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

class Salary(Employee):
    def calculate(self):
        HRA = self.salary * 0.20
        DA = self.salary * 0.10
        gross = self.salary + HRA + DA
        print("Name :", self.name)
        print("Id :", self.id)
        print(" :", self.name)