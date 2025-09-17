#using while loop
current_username="thas"
current_password="win"
attempts=0
while attempts<3:
    username=input("Enter your username:")
    password=input("Enter your password:")
    if current_username==username and current_password==password:
        print("Login Successfull!")
        break
    else:
        print("Try Again !")        
        attempts+=1
else:
    print("Account Locked")
