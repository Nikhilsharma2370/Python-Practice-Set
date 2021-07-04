mydict ={
    "fast":"It is a quick manner",
    "jester": "It is a danger man",
    "marks":[1,2,3],
    "another_dict":{"Nikhil":"Good man"},
    1:2
}
print(mydict.keys()) # Print the key of the dictionary

print(list(mydict.keys())) #typecasting

print(mydict.values()) # Print the value of the dictionary 

print(mydict.items()) # Print the both value (keys,values) all contents of the dictionary

update_dict={
    "nikhil": "bhai",
    "marks":[23,32]
}
mydict.update(update_dict) # update the dictionary by adding  key-value pair from update_dict
print(mydict)
# print(mydict.update({"jester":"good man"}))
print(mydict.get("jester")) # prints  value associated with  key "jester"
print(mydict["jester"]) # prints  value associated with  key "jester"
# different between get and []
print(mydict.get("jester2")) #Return none as jester2 is not present of the dictionary
# print(mydict["jester2"]) #thrown  error as jester2 is not present of the dictionary
