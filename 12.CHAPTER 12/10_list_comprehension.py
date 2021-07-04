a = [1,5,7,2,3,4,5,8]
# b = []
# for i in a:
#     if i%2== 0 :
#         b.append(i)
# print(b)
b=[i for i in a if i%2==0 ]
print(b)

t = [1,3,5,5,5,32]
s = {i for i in t}

print(s)