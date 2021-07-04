# def ns(a,word):
#     newstr=a.replace(word,"####") # write by jester 
#     return newstr

with open("sample.txt","r") as f:
    b = f.read()

b = b.replace("donkey","@@@@") 

with open("sample.txt","w") as f:
    # if b == "donkey":
        f.write(b)
    