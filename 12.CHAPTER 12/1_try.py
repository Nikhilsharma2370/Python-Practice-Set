while(True):
    print("press q to quit")
    a = input("enter your number")
    if a == "q":
        break
    
    try:
        print("Trying..")
        a = int(a)
        if a>6:
            print("this is large number")
    except Exception as a:
        print(f"your input resulted input error: {a}")
    
print("Thanks for playing game")

