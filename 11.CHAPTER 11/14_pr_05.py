class Vector:
    def __init__(self,val):
        self.val=val
    
    def __str__(self):
        str1 = ""
        index = 0
        for i in self.val:
            str1 += f" {i}a{index} +"
            index += 1
        return str1[:-1]
    
    def __add__(self,val2):
        newlist=[]
        for i in range(len(self.val)):
            newlist.append(self.val[i]+val2.val[i])
        return Vector(newlist)
        
    def __mul__(self,val2):
        sum = 0 
        for i in range(len(self.val)):
            sum += self.val[i]*val2.val[i]
        
        return sum
            

v1 = Vector([1,3,5])
v2 = Vector([2,4,5])
print(v1+v2)
print(v1*v2)