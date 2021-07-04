
# use open function read the content of a file!
# f = open('sample.txt',  'r') 
f = open ('sample.txt') #default use read 
# text = f.read()
text = f.read(5) # read 5 character from the file 
print(text)
f.close()
