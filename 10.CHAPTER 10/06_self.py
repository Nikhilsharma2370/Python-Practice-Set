class Employee:
    company = "google"
    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

jester = Employee()
jester.salary = 100000
jester.getsalary() #Employee.getsalary(harry)