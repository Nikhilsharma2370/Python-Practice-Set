class Employee:
    company ="jester company"
    salary = 2000
    salarybonus = 300
    
    # totalsalary = 2300

    @property
    def totalsalary(self):
       a= self.salary+self.salarybonus
       return a
    
    @totalsalary.setter
    def totalsalary(self,val):
        self.salarybonus=val-self.salary

e = Employee()
print(e.totalsalary)
e.totalsalary = 2200
print(e.salary)
print(e.salarybonus)