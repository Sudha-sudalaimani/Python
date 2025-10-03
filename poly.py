#polymorphism
class Animal():
    def sound(self):
        print("Animal Makes Sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Bird(Animal):
    def sound(self):
        print("Birds Sing")
a1=Animal()
a1.sound()
d1=Dog()
d1.sound()
b1=Bird()
b1.sound()
