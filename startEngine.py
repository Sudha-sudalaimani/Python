from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def startEngine(self):
       print("Vehicle Engine is started")
class car(vehicle):
    def startEngine(self):
        print("Car Engine is started")
class bike(vehicle):
    def startEngine(self):
        print("Bike Engine is started")

#v=vehicle()
#v.startEngine()
c=car()
c.startEngine()
b=bike()
b.startEngine()
