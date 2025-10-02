s_username="EMC"
s_password="123"
uname=input("Enter Your Username: ")
password=input("Enter Your password: ")
def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False

check=validate()
print(check)
