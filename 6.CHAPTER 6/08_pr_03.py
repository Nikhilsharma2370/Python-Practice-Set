a=input("enter your text:\n")

if("make a money" in a):
    spam = True
elif("click now" in a):
    spam = True
elif("subscribe" in a):
    spam = True
else:
    spam = False

if(spam):
    print("This is a spam")
else:
    print("This is not a spam")