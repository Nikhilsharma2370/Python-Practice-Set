class Employee:
    Salary = 2300
    increment = 2.3

    @property
    def si(self):
        return self.Salary*self.increment
    
    @si.setter
    def si(self,r):
        self.increment = r/self.Salary

a = Employee()

print(a.si)

a.si = 5666
print(a.increment)

