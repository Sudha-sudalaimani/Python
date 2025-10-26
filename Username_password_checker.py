curent_username="Coder"
curent_password=123
attempts=0
while attempts<3:
    username=input("Enter Your Username:")
    password=int(input("Enter Your password:"))
    if username==curent_username and password==curent_password:
        print("Logine SucessFull")
        break
    else:
        print("Username or Password mismatch,Try Again!")
        attempts+=1
else:
    print("Account Locked")
