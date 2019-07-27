
class Account :
    def __init__(self, accno , name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
    
    def withdraw(self, withdraw_amount):
        self.balance -= withdraw_amount
    
    def show_info(self):
        print(f"Account number :{self.accno}\nName : {self.name}\nBalance : {self.balance}")

obj_1 = Account(123, "Robin" , 10000)
obj_2 = Account(124, "Da bank" , 20000)
obj_1.deposit(100)
obj_2.withdraw(500)
obj_1.show_info()
obj_2.show_info()