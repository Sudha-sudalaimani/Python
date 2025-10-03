#single inheritance 
class Dad:
    def phone(self):
        print("Dad's Phone")
class son(Dad):  #this is single inheritance
    def laptop(self):
        print("Son's laptop")
sam=son()
sam.laptop()
sam.phone()
