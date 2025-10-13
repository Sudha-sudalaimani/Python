class Engine():
    def __init__(self,type):
        self.type=type
    def start(self):
        print(f"The {self.type} Engine is started")
class Car():
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=engine
    def car_start(self):
        print(f"The {self.brand} is started")
        self.engine.start()
engine1=Engine("Petrol")
car1=Car("Swift",engine1)
car1.car_start()
