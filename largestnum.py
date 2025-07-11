#Find second largest number in list
numbers=[]
limit=int(input("Enter limit:"))
for i in range(limit):
    numbers.append(int(input("Enter a number:")))
numbers.sort()
print("THe second largest number:",numbers[-2])
