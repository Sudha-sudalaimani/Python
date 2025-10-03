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

    def changechargertype(cls):   #class method
        cls.chargertype="B-Type"
        print("Charger type changed to B")

    #if you dont want class variables instance variable use static method
    @staticmethod
    def info(): #note: i dint pass any self parameter because i dont want and class variables and methods so i use static method
        print("This is Laptop class")

hp=laptop()
hp.setprice(23000)
hp.getprice()
laptop.changechargertype(laptop)  #calling class method
hp.info()
