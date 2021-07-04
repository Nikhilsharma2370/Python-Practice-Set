class Employee:
    company = "Google"
    salary = 500
nikhil = Employee()
jester = Employee()
print(jester.company)
print(nikhil.company)
Employee.company = "youtube"
# nikhil.company="google"


print(jester.company)
print(nikhil.company)
nikhil.salary = 300
jester.salary = "infinity"
print(jester.salary)