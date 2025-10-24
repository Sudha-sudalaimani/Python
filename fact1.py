num=int(input("Enter a number:"))
factorial=1
if num<0:
    print("Factorial does not exists for negative number")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The Factorial of {num} is {factorial}")
