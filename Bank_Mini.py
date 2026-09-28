class Bank:
    bankName = "State bank of india"
    def __init__(self,name):
        self.name = name
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        if(self.balance < amount):
            print("Insufficient amount")
            return
        self.balance -= amount

    def get_info(self):
        print("Name :", self.name)
        print("balance :", self.balance)
        print("Bank name : ", self.bankName)


    @classmethod
    def bank_name(cls):
        print("Bank name : ", cls.bankName)

c1 = Bank("Bablu")
c1.deposit(50)
c1.get_info()
c1.bank_name()