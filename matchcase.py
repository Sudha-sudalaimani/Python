# Another languages like js and java we use switch case instead of we use match in python

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

operator=input("Enter operator (+,-,*,/): ")

match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case _:
        print("Invalid Operator")
