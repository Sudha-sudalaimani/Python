import random
Guess=random.randint(1,10)
atempts=0
while Guess>0:
    num=int(input("Enter Your Number to Guess:"))
    if Guess==num:
        print("You Won!")
        atempts+=1
        break
    elif Guess<num:
        print("Too High,Try Again!")
        atempts+=1
    elif Guess>num:
        print("Too Low,Try Again!")
        atempts+=1
print("No of Atempts:",atempts)
