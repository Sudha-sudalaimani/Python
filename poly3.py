class vehicle():
    def start(self):
        print("Vehicle Started")
class car(vehicle):
    def start(self):
        print("Car started")
c1=car()
c1.start()
