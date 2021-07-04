class Employee:
    company = "Microsoft"
    def info(self):
        print(f"Emplyee name is {self.name} ")
        print(f"Emplyee name is {self.salary} ")

nikhil = Employee()
jester = Employee()
nikhil.name = "Nikhil sharma"   #write by jester
nikhil.salary = 100000
jester.name = "Jester Danger"
jester.salary = 2000000
nikhil.info()
jester.info()