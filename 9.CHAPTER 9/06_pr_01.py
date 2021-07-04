    f = open("poem.txt")
a = f.read()
if 'twinkle' in a:
    print("twinkle in present")
else:
    print("twinkle in not present")
f.close()