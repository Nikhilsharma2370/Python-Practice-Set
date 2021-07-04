def present(marks):
    # return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100 
     Ns=((marks[0]+marks[1]+marks[2]+marks[3])/400)*100
     return Ns


marks1 = [100,77,88,99]
percentage1 = present(marks1)
print(percentage1)

marks2 = [88,78,99,71]
percentage2=present(marks2)
print(percentage2)         