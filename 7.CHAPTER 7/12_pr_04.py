a = int(input("Enter your number\n"))
prime=True
for i in range(2,a):
    if(a%i==0):
       prime=False
       break
if prime:
    print("this is prime number")
else:
     print("this is not prime number")
         
    
     

       