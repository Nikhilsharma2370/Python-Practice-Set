def gt(a,b,c):
    if a>b:
        if a>c:
           return a
        else:
            return c
    else:
        if b>c:
            return b 
        else:
            return c


print(gt(1,3,5))