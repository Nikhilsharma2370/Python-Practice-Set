class Employee:
    salary = 2334
    increment = 2.3

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
        self.increment = sai / self.salary
    
e =Employee()

print(e.salaryAfterIncrement)
# e.salaryAfterIncrement= 12000

# print(e.increment)
