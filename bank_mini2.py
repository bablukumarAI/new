import sys
class Customer:
    bankname = "SBI"
    def __init__(self, name, balance = 0.0):
        self.name = name
        self.balance = balance
    def deposite(self, amt):
        self.balance += amt
        print("Balance after deposite :", self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient balance")
            sys.exit()
        self.balance = self.balance - amt
        print("Balance after withdraw :", self.withdraw)

print("Welcome to ", Customer.bankname)
name = input("Enter your name :")
c = Customer(name)

while True:
    print("d-Deposit\n w- withdraw\n e-exit")
    option = input("Choose your option:")
    if option == 'd' or option == 'D':
        amt = float(input("Enter amount:"))
        c.deposite(amt)
    elif option == 'w' or option == 'W':
        amt = float(input("Enter amount:"))
        c.withdraw(amt)
    elif option == 'e' or option == 'E':
        print("Thanks for banking")
        sys.exit()
    else:
        print("Invalid option , plz choose a valid option")
       