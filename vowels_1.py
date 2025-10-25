char=input("Enter a single Character:")
vowels="aeiouAEIOU"
for ch in vowels:
    if ch==char:
        print(char,"is vowel")
        break
else:
    print(char,"is not a vowel")
