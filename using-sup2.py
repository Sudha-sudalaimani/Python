class Employee():
    def __init__(self,n,s):
        self.name=n
        self.salary=s
class Manager(Employee):
    def __init__(self,name,salary,dept):
        super().__init__(name,salary)
        self.department=dept
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Dept:",self.department)
m1=Manager("Sam",80000,"Developer")
m1.display()
