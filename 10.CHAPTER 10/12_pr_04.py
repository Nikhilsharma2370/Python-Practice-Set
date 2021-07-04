class calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"the square of {self.number} is {self.number **2}") 
    
    def squareroot(self):
        print(f"the square of {self.number} is {self.number **0.5}") 

    def cube(self): 
        print(f"the square of {self.number} is {self.number **3}") 
    @staticmethod
    def greet():
        print("hello")

a=calculator(3)
a.square()
a.squareroot()
a.cube()
a.greet()