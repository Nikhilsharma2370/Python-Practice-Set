a = int(input("Enter your number 1: "))
b = int(input("Enter your number 2: "))

try:
    c =a/b
    print(c)
except ZeroDivisionError:
    print("infinity")
