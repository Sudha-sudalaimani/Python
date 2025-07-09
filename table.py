#table using while loop
table_num=int(input("Enter a num:"))
limit=int(input("Enter the limit value:"))
i=1
while i<=limit:
    print(f"{i} * {table_num} = {i*table_num}")
    i+=1
