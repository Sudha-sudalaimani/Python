class teacher:
    def __init__(self,n,r):
        self.name=n
        self.regno=r
    def display(self):
        print("Name: ",self.name)
        print("regno:",self.regno)

t1=teacher("Nirmala",101)
t2=teacher("Senthil",102)
t1.display()
t2.display()
