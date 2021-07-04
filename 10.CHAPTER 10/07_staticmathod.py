class Employee:
    company = "google"
    def getsalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")
    @staticmethod
    def greet():
        print("Good morning, bro")
    @staticmethod
    def adviced():
        print("never loss your confidence")
jester = Employee()
jester.salary = 100000
jester.getsalary("Thanks") #Employee.getsalary(harry)
jester.greet()
jester.adviced()