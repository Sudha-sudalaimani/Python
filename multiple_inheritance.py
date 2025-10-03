#multiple inheritance 
class Dad:
    def phone(self):
        print("Dad's Phone")
class Mom:
    def sweet(self):
        print("Sweet")
class son(Dad,Mom):  #this is multiple inheritance
    def laptop(self):
        print("Son's laptop")
sam=son()
sam.laptop()
sam.phone()
sam.sweet()
