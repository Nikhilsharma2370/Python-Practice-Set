def greater(num):
    if num>5:
        return True
    else:
        return False

li = [1,2,3,5,6,75,8,6,8,68]
a = lambda num: num>10
print(list(filter(greater,li)))
print(list(filter(a,li)))