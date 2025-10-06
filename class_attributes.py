#Create a Car class with attributes (brand, model, price). Create 3 objects and print details.
class car():
    def __init__(self,b,m,p):
        self.brand=b
        self.model=m
        self.price=p
    def display(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")
bmw=car("BMW","Model S",1200000000)
audi=car("Audi","x5",2500000)
car1=car("Car","c4",250000)
bmw.display()
audi.display()
car1.display()
