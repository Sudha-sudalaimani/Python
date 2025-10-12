#Create abstract class Shape with abstract method area(). Implement Circle and Square.
from abc import ABC,abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        circle_area=math.pi*self.radius**2
        return circle_area
class square(ABC):
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side**2

c=circle(5)
s=square(4)

print(f"Area of circle is:{c.area():.2f}")
print(f"Area of square is:{s.area():.2f}")
