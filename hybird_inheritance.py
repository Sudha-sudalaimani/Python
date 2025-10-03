# hybird inheritance => one program that has multiple inheitance hirerachy inheritance or single etc its holds all inheritance
class dad():
    def money(self):
        print("Money")
class land():
    def important(self):
        print("This is land")

class son1(dad,land):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

sam=son2()
sam.money()
s1=son1()
s1.money()
s1.important()
