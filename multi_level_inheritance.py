#multi level inheritance
class grandpa():
    def phone(self):
        print("grandpa phone")
class dad(grandpa): #dad can access grandpa phone
    def money(self):
        print("Dad's Money")
class son(dad):   #son can access dads money and also grandpa's phone this is multilevel inheritance
    def laptop(self):
        print("son's laptop")

sam=son()
sam.laptop()
sam.money()
sam.phone()
d1=dad()
d1.phone()
