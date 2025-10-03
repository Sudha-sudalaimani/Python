#Encapsulation
class company():
    def __init__(self):
        self.__company="Google" #__underscore means that variable is private
    def name(self): #private variables access only within the class so we use the function to display
        print(self.__company)
c1=company()
c1.name()
