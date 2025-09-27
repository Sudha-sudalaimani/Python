word=input("Enter your sentence:")
vowels="AEIOUaeiou"
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)
