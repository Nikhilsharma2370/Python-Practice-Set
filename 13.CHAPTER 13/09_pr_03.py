a = int(input("Enter your number:  "))
list = [str(i*a) for i in range(1,11)]
print(list)
op = "\n".join(list)
print(op)