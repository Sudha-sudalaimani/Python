class Shape():
    def area(self):
        return 0
class Reactangle(Shape):
    def area(self):
        l=20
        b=20
        return l*b
r1=Reactangle()
r1.area()
