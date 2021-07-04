class Employee:
    company = "Google"
    salary = 500
nikhil = Employee()
jester = Employee()
# create the instance attribute salary for both the objects
# nikhil.salary = 300
# jester.salary = 400
nikhil.salary = 23
print(nikhil.salary)
print(jester.salary)
# Below line throwa an error as address in not present in the instance/class
# print(jester.address)
