a = int(input("Enter your number"))
for i in range(a):
    print(" "*(a-i-1),"* "*i)
for i in range(a,1,-1):
    print(" "*(a-i),"* "*(i-1))