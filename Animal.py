class Animal():
    def sound(self):
        print("Animal makes sound")
class dog(Animal):
    def sound(self):
        print("Dog barks")
a1=Animal()
a1.sound()
d1=dog()
d1.sound()
