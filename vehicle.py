class vehicle():
    def fuelType(self):
        print("Vehicle use Fuel")

class car(vehicle):
    def fuelType(self):
        print("Car use Fuel")
class bike(car):
    def fuelType(self):
        print("Bike use Fuel")
v1=vehicle()
v1.fuelType()

v2=car()
v2.fuelType()

v3=bike()
v3.fuelType()
