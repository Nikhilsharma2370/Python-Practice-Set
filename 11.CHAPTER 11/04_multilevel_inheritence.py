class Person:
    country = "india"
    def getBreath(self):
        print("i am breathing....")

class Employee(Person):
    company = "google"
    def getBreath(self):
        print("i am breathing....")

class Programmer(Employee):
    company = "fiberr"
    def getBreath(self):
        print("i am breathing....")
  
p = Person()
e = Employee()
pr = Programmer()

p.getBreath()
e.getBreath()

pr.getBreath()
# print(pr.company)
print(pr.country)



