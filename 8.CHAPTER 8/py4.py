def a(n,w):
    return n.replace(w,"")
    # return n.replace(w,"").strip()


b = "     my name is danger"
print(a(b,"name").strip())