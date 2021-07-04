class Vector:
    def __init__(self,val):
        self.val=val
    
    def __str__(self):
        return f"{self.val[0]}i+{self.val[1]}j+{self.val[2]}k"
            

v1 = Vector([1,3,5])
v2 = Vector([2,4,5])
print(v1)
print(v2)