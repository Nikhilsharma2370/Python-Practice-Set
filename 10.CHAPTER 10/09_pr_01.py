class Programmer:
    company = "Microsoft"
        
    def __init__(self,name,product):
        self.name=name
        self.product=product
    
    def getinfo(self):
        print(f"the name of {self.company} programmer is {self.name} and the product is {self.product}")

nikhil = Programmer("Nikhil sharma","fighting machine")
jester = Programmer("Jester danger","killing machine")

nikhil.getinfo()
jester.getinfo()        
