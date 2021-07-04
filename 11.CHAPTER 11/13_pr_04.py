class Complex:
    
    def __init__(self,r,i):
        self.r = r 
        self.i = i
    
    def __add__(self,a):
        return Complex(self.r+a.r,self.i+a.i)
    def __mul__(self,a):
        mulReal = self.r*a.r-self.i*a.i
        mulImg = self.r*a.i+self.i*a.r
        return Complex(mulReal,mulImg)


    def __str__(self):
        if self.i<0:
              return f"{self.r}-{-self.i}i"
            
        else:
            return f"{self.r}+{self.i}i"
    
    
c1 = Complex(3,2)
c2 = Complex(1,7)
# c3 = Complac(4,1)
print(c1+c2)
print(c1*c2)