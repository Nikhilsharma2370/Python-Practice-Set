with open("poem.txt","r") as f:
    n = f.read()

if "twinkle" in n:
    print("yes")
else:
    print("no")

    