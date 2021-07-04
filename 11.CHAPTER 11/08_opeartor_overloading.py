class Number:
    def __init__(self,num):
        self.num=num
    
    def __add__(self,num2):
        print("let do it fight")
        return self.num + num2.num
    
    def __mul__(self,num2):
        print("let do it fight")
        return self.num * num2.num

n1 = Number(1)
n2 = Number(2)
sum = n1+n2
mul = n1*n2
print(sum)
print(mul)