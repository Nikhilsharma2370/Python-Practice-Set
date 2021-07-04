# Creating the empty set
a = set()
print(a)

#adding value to an  empty set
a.add(4)
a.add(5)
a.add(5)
a.add(4) # adding the value repeatedly does not changes a set
a.add((1,3,4))
# a.add([1,35,65]) # Cannot add list to sets
# a.add({1:65}) # Cannot add dictionary to sets

print(a)
# print(len(a)) # Print the length of sets
# a.remove(4)
print(a) #remove the element from the sets
a.pop()
print(a) #randowly remove the element from the sets

# print(a.clear())
print(a.union({3,9}))
print(a.intersection({3,9,4}))