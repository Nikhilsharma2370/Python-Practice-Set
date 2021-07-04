def read(name):
    try:
        with open(name,"r") as f:
         print(f.read())
    except Exception:
        print(f"{name} is not here")
        
read("1.txt")
read("2.txt")
read("3.txt")
