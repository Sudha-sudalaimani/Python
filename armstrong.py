number=int(input("Enter a number:"))
order=len(str(number))  #Length of on input
sum=0
temp=number
while temp>0:
    digit=temp%10
    sum+=digit**order  #cube the each digit
    temp//=10
if number==sum:
    print(number,"is an armstrong number")
else:
    print(number,"is not an armstrong number")
