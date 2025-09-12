#Simple Calculator using python 
def add():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    return num1+num2
def subract():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    return num1-num2
def multiply():
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    return num1*num2
def divide(num1,num2):
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))
    if num2==0:
        return "Error! Division by zero"
    return num1/num2

while True:
    print("Welcome to the calculator")
    print("Select operation")
    print("1 is Add function")
    print("2 is Subtract function")
    print("3 is Multiply function")
    print("4 is Divide function")       
    print("5 is Exit")
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        
        res=add()
        print("The Addition of two numbers is:",res)
    elif choice==2:
         res=subract()
         print("The Subraction of two numbers is:",res)
    elif choice==3:
         res=multiply()
         print("The product of two numbers is:",res)
    elif choice==4:
         divide()
         print("The division of two numbers is:",res)
    elif choice==5:
        print("Exiting the calculator")
        break
