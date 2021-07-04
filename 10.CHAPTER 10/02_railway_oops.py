class RailwayForm:
    FormType = "RailwayForm"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"=train is {self.train}")
        
    
a = RailwayForm()
a.name = "nikhil"
a.train = "Rajdhani Express"
a.printdata()