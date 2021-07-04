class Sample:
    a = "Nikhil"

obj = Sample()
obj.a = "Jester"
Sample.a = "jester"
print(Sample.a)
print(obj.a)