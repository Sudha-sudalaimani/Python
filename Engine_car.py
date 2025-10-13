#Create class Engine and class Car. Car has-an Engine (Composition).
class Engine():
    def __init__(self,horsepower,type):
        self.horsepower=horsepower
        self.type=type
    def start(self):
        print(f"The {self.type} engine with {self.horsepower} Hp is starting")
class Car():
    def __init__(self,brand,model,engine):
        self.brand=brand
        self.model=model
        self.engine=engine# Composition: Car has-an Engine
    def car_start(self):
        print(f"The {self.brand},{self.model}  model is starting ")
        self.engine.start()# Using the Engine's start method
engine1=Engine(150,"Petrol")# Create an Engine object

car1=Car("Swift","E1",engine1) # Car has this Engine

car1.car_start()
        
    
