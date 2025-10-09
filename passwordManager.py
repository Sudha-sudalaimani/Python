class passwordManager():
    def __init__(self):
        self.__password=None
        self.__key="admin@sam"
    def set_password(self,password,key):
        if key==self.__key:
            self.__password=password
            print("Password set sucessfully")
        else:
            print("Wrong key,Try again!")
    def getpassword(self,key):
        if key==self.__key:
            print("Stored passwor:",self.__password)
        else:
            print("Wrong key,Try again!")
p1=passwordManager()
p1.set_password("spidey","admin@sam")
p1.getpassword("admin@sam")
