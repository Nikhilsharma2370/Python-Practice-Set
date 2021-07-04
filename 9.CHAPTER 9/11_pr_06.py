with open("log.txt","r") as f:
    a = f.read()
    # a = f.read().lower()
if "python" in a.lower():
    print("python is here ")
    print(a.find("python"))
else:
    print("python is not here") 