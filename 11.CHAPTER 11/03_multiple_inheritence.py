class Employee:
    company = "visa"
    ecode = 102

class Freelancer:
    company = "Fiver"
    level = 0
    
    def upgradelevel(self):
        self.level=self.level+1.

class Programmer(Employee,Freelancer):
    name = "nikhil"

a = Programmer()
a.upgradelevel()
print(a.level)
print(a.company)