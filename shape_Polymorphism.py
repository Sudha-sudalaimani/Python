#Overriding → Create Shape → Circle, Rectangle override area().
import math
class shape():
    def area(self):
        print('Shapes Area')
class circle(shape):
    def area(self,r):
        area_circle=math.pi*r*r
        print("Area of Circle is:",area_circle)
class reactangle(shape):
    def area(self,l,b):
        rectangle_area=l*b
        print("Area of Reactangle is:",rectangle_area)
c1=circle()
c1.area(5)

r1=reactangle()
r1.area(2,5)
