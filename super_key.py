#super keyword
class a():
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class a")

class b(a):
    def __init__(self):
        super().__init__() #super keyword access A class constructor 
        print("B")
    def display(self):
        super().display()
        print("You are in class b")

B=b()
B.display()
