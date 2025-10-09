class employee():
    def __init__(self,i,n,s):
        self.id=i
        self.name=n
        self.salary=s
    def details(self):
        print(f"Id:{self.id}, Name:{self.name}, Salary:{self.salary}")
class manager(employee):
    def __init__(self,i,n,s,dept):
        super().__init__(i,n,s)
        self.dept=dept
    def details(self):
        print(f"Id:{self.id}, Name:{self.name}, Salary:{self.salary} , Department:{self.dept}")
e1=employee(101,"Sam",80000)
e1.details()

m1=manager(100,"Thashlee",850000,"Cse")
m1.details()

        
