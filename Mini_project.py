import random

alphabet = "abcdefghijklmnopqrstuvwxyz"
digit = "0123456789"
cities = ["Hydrabad", "Banglore", "Chennai", "delhi", "Bombay"]
designations = ["Manager", "Junior engineer", "Senior engineer", "HR", "Product Manager"]

def get_fake_name():
    name = ""
    nameLen = random.randint(1,10)
    for i in range(nameLen):
        name += random.choice(alphabet)
    return name.capitalize()

def get_fake_empId():
    EmpId = "E"
    for i in range(4):
        EmpId += random.choice(digit)
    return EmpId

def get_fake_salary():
    return str(random.randint(20000, 80000))

def get_fake_city():
    return random.choice(cities)

def get_fake_Mob():
    mobNo = random.choice("6789")
    for i in range(9):
        mobNo += random.choice(digit)
    return mobNo

def get_fake_designation():
    return random.choice(designations)

print("Emp name : ", get_fake_name())
print("Emp id : ", get_fake_empId())
print("Emp salary :", get_fake_salary())
print("Emp city : ",get_fake_city())
print("Emp Phone No :", get_fake_Mob())
print("Emp designation : ", get_fake_designation())