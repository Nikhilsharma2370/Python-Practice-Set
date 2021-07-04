from functools import reduce

sum = lambda a,b : a+b

li = [1,2,3,4]
val = reduce(sum,li)
print(val)