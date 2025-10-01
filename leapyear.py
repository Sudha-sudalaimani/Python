year=int(input("Enter a year: "))

if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} Leap Year")
        else:
            print(f"{year} Not Leap Year")
    else:
        print(f"{year} Leap year")
else:
    print(f"{year} Not leap Year")
