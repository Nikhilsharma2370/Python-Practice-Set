words=["donkey","monkey","dog","bitch"]

with open("sample.txt","r") as f:
    b = f.read()
for word in words:
    b = b.replace(word,"@@@@") 
    with open("sample.txt","w") as f:
    # if b == "donkey":
        f.write(b)
    