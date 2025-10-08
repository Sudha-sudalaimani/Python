class Bank():
    def __init__(self,initial_balance=0):
        self.__balance=initial_balance
    def currentbalnce(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited:{amount}")
        else:
            print("amount must be an positive")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrawn:{amount}")
        else:
            print(f"Insufficient Balance or Invalid amount")
    def getBalnce(self):
        return self.__balance

p2=Bank(50000)
balnce=p2.currentbalnce()
print("Current Balnce:",balnce)
p2.deposit(10000)
p2.withdraw(5000)
current=p2.getBalnce()
print(f'current Balnce:{current}')
