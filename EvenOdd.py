#even or odd using list
numbers=[22,33,24,46,87]
even=[]
odd=[]
for number in numbers:
    if number%2==0:
        even.append(number)
    else:
        odd.append(number)
print("Even:",even,"Odd:",odd)
