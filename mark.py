#Using if elif else
tamil=int(input("Enter Tamil mark:"))
english=int(input("Enter English mark:"))
cs=int(input("Enter CS mark:"))

total=tamil+english+cs
avg=total/3
print("Total Marks:",total)
print("Average:",avg)
if tamil>=35 and english>=35 and cs>=35:
    print("Result : Pass")
    if avg>=90 and avg<=100:
        print("Grade A")
    elif avg>=80 and avg<=89:
        print("Grade B")
    elif avg>=70 and avg<=79:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Result : Fail")
    print("No Grade")
