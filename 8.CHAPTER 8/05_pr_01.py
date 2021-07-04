def max(a,b,c):
    if a<b:
        if a<c:
            return c
        else:
            return b
    if b<a:
        if b<c:
            return c
        else: 
            return a

m = max(78,34,2)
print("the max number", m)                   