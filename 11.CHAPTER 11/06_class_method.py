class Employee:
    company = "google"
    salary = 100
    # def changesalary(self,sel):
    #     self.__class__.salary= sel
    
    @classmethod
    def changeSalary(cls, sal):
        cls.salary= sal

e = Employee()
print(e.salary)
e.changeSalary(200)
print(e.salary)
# print(e.salary)
print(Employee.salary)