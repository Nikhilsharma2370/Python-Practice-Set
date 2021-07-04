class rj:
    def __init__(self,val):
        self.val = val

    def __str__(self):
        return f"{self.val[0]}i+{self.val[1]}j+{self.val[2]}k"

a = rj([1,2,4])
print(a)