class Employee:
    company = "google"
    
    def __init__(self,name,salary):
        print("this is construction")
        self.name = name        
        self.salary = salary
    def getDetail(self):
        print(f"Employee name is {self.name}")
        print(f"Employee salary is {self.salary}")

    def getsalary(self,signature):
        print(f"salary for this employee working in {self.company} is {self.salary}\n {signature}")
    @staticmethod
    def greet():
        print("Good morning, bro")
    @staticmethod
    def adviced():
        print("never loss your confidence")
    
jester = Employee("nikhil",122)
# jester = Employee()  throw the error
jester.getDetail()