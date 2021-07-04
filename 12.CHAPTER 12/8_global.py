a = 23 #Global Variable
def func():
    global a 
    print(a)
    a = 8 # local Variable if global keyword is not use
     
    print(a)

func()
print(a)