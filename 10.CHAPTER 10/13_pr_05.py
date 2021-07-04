class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print("****************************************************")
        print(f" The name of train is {self.name}")
        print(f" The seat  is available in the train are {self.seats}")
        print("****************************************************")
    
    def getfare(self):
        print(f" The fare of train is Rs. {self.fare}")

    def booking(self):
        if (self.seats>0):
            print(f"your ticket are booking {self.seats}")
            self.seats = self.seats-1
            
        else:
            print("sorry seats are full! kindly try in tatkal")

    def set(self,seatNo):
        a=set()
        for i in range(1,self.seats+1):
            a.add(i)

        a.add(seatNo)
        print(f"{seatNo}")
        print(a)
        if a!= self.seats:
            self.seats = self.seats+1

a = Train("Intercity :14010",100,10)

a.getStatus()
a.getfare()
a.booking()
a.booking()
a.booking()
a.getStatus()
a.set(9)

# a.booking()
a.getStatus()