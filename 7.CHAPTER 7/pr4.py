a = int(input("enter your number"))

i = 1
f = 1                  
# while i <= a:        
#     f = f*i     this question not solve using by the while loop because this 
#                  value and again take change value1        
#     i += i               
#     print(f)
# print(f)
f = 1
for i in range(1,a+1):
    f = f * i
    print(f)
print(f) 