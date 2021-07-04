a = True
i = 1
with open("log.txt","r") as f:
    while a:    
        a = f.readline()
        
        if "python" in a.lower():
            print(f"python is here{i} ")
            print(a)
        i+=1