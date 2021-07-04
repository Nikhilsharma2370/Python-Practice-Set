import os
with open("rename.txt") as f:
    a= f.read()

with open("renamed.txt","w") as f:
    f.write(a)
os.remove("rename.txt")