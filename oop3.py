class Laptop:
    def __init__(self): #constructor
        self.ram=""
        self.processor=""
    def display(self): #self denots current object
        print("Ram:",self.ram)
        print("Processor:",self.processor)
hp=Laptop()
hp.ram="16gb"
hp.processor="i7H"
hp.display()# how self work is => hp.display means hp.display(hp) it denotes current object
#here current object is hp
