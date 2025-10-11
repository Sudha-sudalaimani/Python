#I think this is interesting to me 
#question:Write a function makeSound(animal) → if Dog, print “Bark”; if Cat, print “Meow” (polymorphism demo).
class Dog():
    def sound(self):
        return 'Bark'
class Cat():
    def sound(self):
        return "Meow"
def make_sound(animal):#=> here animal means parameter 
    print(animal.sound())

dog=Dog()
cat=Cat()

make_sound(cat)
make_sound(dog)
