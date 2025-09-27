n=int(inpu("Enter a number:"))
if num>1:
    is_prime=True
    for i in range(2,num):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print(num, "is prime")
    else:
        print(num, "is not a prime")
else:
     print(num, "is not a prime")



