class Cd2vec:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def __str__(self):
        return f"{self.i}i+{self.j}j"

class Cd3vec(Cd2vec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k =k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"




a = Cd2vec(1,5)
b = Cd3vec(1,5,6)
print(a)
print(b)        
