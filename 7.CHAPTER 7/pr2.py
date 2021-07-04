a = int(input("enter your number"))
prime = False
for i in range(2,a):
    if a%i==0:
        prime = False
    else:
        prime = True
    break

if(prime):
    print("this is prime")
else:
    print("this is not prime")