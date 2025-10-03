#different type of class function or methods
class laptop:
    chargertype="C-Type"

    def __init__(self):   #instance method
        self.brand=""
        self.price=34
    def setprice(self,price):   #instance method
        self.price=price
    def getprice(self):          #instance method
        print("Price:",self.price)
    @classmethod    #using decorator
    def changechargertype(cls):   #class method
        cls.chargertype="B-Type"
        print("Charger type changed to B")

hp=laptop()
hp.setprice(23000)
hp.getprice()
laptop.changechargertype()  #another way calling class method without parameter
