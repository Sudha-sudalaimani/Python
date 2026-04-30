'''The Secure Vault: Create a BankCard class with a private attribute __pin. Write a method to
 update the PIN, but only if the "old PIN" provided matches the current one.'''

class BankCard:
    def __init__(self,p):
        self.__pin=p
    def update_pin(self,verify):
        if self.__pin == verify:
            self.__pin = int(input("Enter New Pin: "))
            print("Successfully New Pin set")
        else:
            print("You have to give the previous pin correctly !")
b1=BankCard(1234)
b1.update_pin(1264)
