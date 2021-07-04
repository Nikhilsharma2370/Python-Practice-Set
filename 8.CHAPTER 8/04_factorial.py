# def factorial_iter(a):

#     b=1
#     for i in range(a):
#         b=b*(i+1)
#     return b
# print(factorial_iter(4))
def factorial_recursive(n):
#     if n==0:
#         return 1
#     return n*factorial_recursive(n-1)
# print(factorial_recursive(5))
        if n==0 or n==1:
         return 1
        return n*factorial_recursive(n-1)
print(factorial_recursive(5))

def a(n):            #factorial_recursive not a method
#     
        if n==0 or n==1:
         return 1
        return n*a(n-1)
print(a(5))