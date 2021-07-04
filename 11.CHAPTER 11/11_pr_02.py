class Animal:
    Animaltype = "mammal"

class pet(Animal):
    colur = "red"

class Dog(pet):
    @staticmethod
    def bark():
        print("bow bow")
    
d = Dog()
d.bark()
print(d.Animaltype)