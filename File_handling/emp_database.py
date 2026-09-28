import random
alphabet = "abcdefghijklmnopqrstuvwxy"
for i in range(5):
    nameLen = random.randint(3,11)

    # generating the name of the employee
    empName = ""
    for _ in range(nameLen):
        empName += random.choice(alphabet)
    empName = empName.capitalize()
    # generating the emplyee id
    empId = 'e' + str(random.randint(1000, 10000))

    # generating the salary
    salary = random.randint(20000, 80000 + 1)

    # generating the employee city
    cities = ["Hydrabad", "Banglore", "Chennai", "Delhi", "Bombay"]
    empCity = random.choice(cities)

    # generating the mob num
    mobNo = str(random.randint(6, 9))
    mobNo = mobNo +  str(random.randint(100000000, 1000000000))

    file = open("emp_Database.txt", "a")
    file.writelines("Name :"+empName + "\n")
    file.writelines("Emp ID :"+empId + "\n")
    file.writelines("Salary :"+str(salary) + "\n")
    file.writelines("City :"+empCity + "\n")
    file.writelines("Mob No :" + str(mobNo) + "\n"+"\n")
    file.close()