#Create a Person class with private age. Allow setting age only if age >= 0.
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=0
        self.setAge(age)
    def setAge(self,age):
        if age>=0:
            self.__age=age
        else:
            print('Age must be positive')
    def getAge(self):
        return self.__age
p1=person("sam",20)
print("Name:",p1.name)
print("age:",p1.getAge())
