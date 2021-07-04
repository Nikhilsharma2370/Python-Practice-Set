class Cd2vec:
    def __init__(self,i,j):
        self.i = i 
        self.j = j
    
    def __str__(self):
        return f"{self.i}i+{self.j}j"

class Cd3vec(Cd2vec):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k= k
    
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

n1 = Cd2vec(2,3)
n2 = Cd3vec(5,6,7)
print(n1)
print(n2)
