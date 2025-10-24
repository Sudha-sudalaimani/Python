lower=int(input("Enter a number:"))
upper=int(input("Enter a number:"))
for i in range(lower,upper+1):
    if i>1:
        for num in range(2,i):
            if(i%num)==0:
                break
        else:
            print(i)
