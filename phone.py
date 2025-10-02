#variable types
#instance variables => thats is constructor variables if i create multiple objects the value wouble be differ rom the object
#class variable => means the variable is inside the class not a constructor 
#example
class phone:
    chargertype="C-Type" #this is class variable
    def __init__(self,brand,price):
        self.brand=brand #this is instance variable
        self.price=price
    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("ChargerType:",self.chargertype)

realme=phone("Realme",15000)
realme.display()

samsung=phone("Samsung",20000)
samsung.display()

redmi=phone("Redmi",10000)
redmi.display()
