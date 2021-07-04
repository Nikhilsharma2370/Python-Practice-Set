def remove_with_strip(string,word):
    newstr =string.replace(word,"")
    return newstr.strip()
a = "        nikhil is good               "
print(remove_with_strip(a,"is"))    