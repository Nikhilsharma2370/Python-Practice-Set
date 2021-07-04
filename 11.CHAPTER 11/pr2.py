class Animal():
    Animaltype = "Dog"

class Pet(Animal):
    colour = "red"

class Dog(Pet):
    @staticmethod
    def bark():
        print("bow bow")

a = Dog()
a.bark()
print(a.colour)