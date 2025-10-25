num=153
count=0
if num==0:
    count=1
else:
    while num>0:
        num//=10
        count+=1
print(count)

print("----------------------------------------------------------------------------")

#another way
num=-153
count=len(str(abs(num))) #abs removes - sign
print(count)
