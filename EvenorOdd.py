#user input concept in list
numbers=[]
limit=int(input("Enter a limit:"))
for i in range(limit):
    numbers.append(int(input("Enter a number:")))
even=[]
odd=[]
for number in numbers:
    if number %2==0:
        even.append(number)
    else:
        odd.append(number)

print(even,odd)
    
