#Write a Python program to find the sum of all numbers from 1 to n.
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
