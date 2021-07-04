a = input("Enter your post\n")

if "harry" in a :
    b=True
elif "Harry" in a :
    b=True    
elif "HArry" in a :
    b=True
elif "HARry" in a :
    b=True  
elif "HARRy" in a :
    b=True
elif "HARRY" in a :
    b=True 
else:
    b=False

if(b):
    print("Harry in this post")
else:
    print("harry not found in this post")         