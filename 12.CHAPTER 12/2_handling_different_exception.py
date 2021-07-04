try:
    a = int(input("enter your number:  "))
    b = 1/a
    print(b)
except ValueError as e:
    print("Please Enter a valid number")
    print(e)

except ZeroDivisionError as e:
    print("make sure you not division by Zero 0")
    print(e)
print("Thanks for typing code")
