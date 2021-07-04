def maximum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return print(num1,"is a greatest number")
    elif num2>num1 and num2>num3:
        return print(num2,"is a greatest number") 
    else:
        return print(num3, "is a greatest number")

num1=int(input("enter your num 1: "))
num2=int(input("enter your num 2: "))
num3=int(input("enter your num 3: "))
maximum(num1,num2,num3)