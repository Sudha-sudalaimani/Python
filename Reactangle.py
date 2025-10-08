class Reactangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def add(self):
        print("The area of the reactangle is:",self.length*self.breadth)
r1=Reactangle(5,2)
r1.add()
