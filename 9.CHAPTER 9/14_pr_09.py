with open("this.txt") as f:
    a = f.read()
with open ("copy.txt") as f:
    b = f.read()

if a == b :
    print("same content in this files")
else:
    print("Not same content in this files")
