num=int(input('Enter a number:'))
if num>1:
    for i in range(2,num):
       if(num%i==0):
           print(num,"is not a prime number")
           break
    else:
        print(num,"Is a prime number")
else:
    print("The number must be greater than 1")

print("------------------------------------------------------------------------------")
import math
num=int(input("Enter a number:"))
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,"Is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print('The number must be greater than 1')
