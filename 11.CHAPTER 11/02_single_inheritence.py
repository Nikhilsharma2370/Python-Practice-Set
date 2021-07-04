class Employee:
    company = "google"
    def info(self):
        print("this is danger")

class Programmer(Employee):
    comany = "youtude"
    def get(self):
        print("this is hard")
    # def info(self):
    #     print("this is ranger")

a = Employee()
b = Programmer()
a.info()
b.info()
print(a.company)