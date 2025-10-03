# hirerachy inheritance => one base class that inheritates two are more class 
class dad():
    def money(self):
        print("Money")
class son1(dad):
    pass
class son2(dad):
    pass
class son3(dad):
    pass

sam=son2()
sam.money()
