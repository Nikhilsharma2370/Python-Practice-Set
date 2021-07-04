class Person:
    country = "india"
    def __init__(self):
        print("I am fighing")

    def getBreath(self):
        print("i am breathing....")

class Employee(Person):
    company = "google"
    
    def __init__(self):
        # super().__init__()
        print("I am fighing Employee")

    def getBreath(self):
        super().getBreath()
        print("i am breathing Employee ....")

class Programmer(Employee):
    company = "fiberr"
    
    def __init__(self):
        super().__init__()
        print("I am fighing programmer")

    def getBreath(self):
        super().getBreath()
        print("i am breathing Programmer....")
  
# p = Person()
# e = Employee()
pr = Programmer()

# p.getBreath()
# e.getBreath()

# pr.getBreath()
# print(pr.company)
print(pr.country)
pr.getBreath()


