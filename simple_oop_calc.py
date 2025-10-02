class calculator:
    def  __init__(self,a,b): #constructor
        self.num1=a
        self.num2=b
    def add(self):
        print("Sum:",self.num1+self.num2)
    def sub(self):
        print("Subraction:",self.num1-self.num2)
    def mul(self):
        print("Multiplication:",self.num1*self.num2)
    def div(self):
        print("Division:",self.num1/self.num2)
obj=calculator(110,20)
obj.add()
obj.sub()
obj.mul()
obj.div()
